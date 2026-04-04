#!/usr/bin/env python3
"""
Interactive square crop tool for team profile images.

Controls:
  Drag            — move the crop box
  Scroll wheel    — resize the crop box
  + / =           — grow crop box
  - / _           — shrink crop box
  Enter / Space   — save crop and next
  S               — skip (don't save)
  Q / Esc         — quit
"""

import cv2
import numpy as np
from PIL import Image
import os, sys

SUPPORTED = {'.jpg', '.jpeg', '.png', '.JPG', '.JPEG', '.PNG'}
MAX_DIM   = 800
BOX_COLOR = (255, 170, 0)
DIM_ALPHA = 0.45
STEP      = 20   # resize step per key press

state = dict(drag=False, drag_start=(0,0), box_origin=(0,0),
             box_x=0, box_y=0, box_side=0, disp_w=0, disp_h=0)


def clamp_box(x, y, side, w, h):
    side = max(40, min(side, w, h))
    x    = max(0, min(x, w - side))
    y    = max(0, min(y, h - side))
    return x, y, side


def mouse_cb(event, x, y, flags, param):
    s = state
    if event == cv2.EVENT_LBUTTONDOWN:
        s['drag']       = True
        s['drag_start'] = (x, y)
        s['box_origin'] = (s['box_x'], s['box_y'])

    elif event == cv2.EVENT_MOUSEMOVE and s['drag']:
        dx = x - s['drag_start'][0]
        dy = y - s['drag_start'][1]
        nx = s['box_origin'][0] + dx
        ny = s['box_origin'][1] + dy
        nx, ny, side = clamp_box(nx, ny, s['box_side'], s['disp_w'], s['disp_h'])
        s['box_x'], s['box_y'] = nx, ny

    elif event == cv2.EVENT_LBUTTONUP:
        s['drag'] = False

    # Scroll wheel resize (macOS sends MOUSEWHEEL)
    elif event == cv2.EVENT_MOUSEWHEEL:
        delta = STEP if flags > 0 else -STEP
        resize_box(delta)


def resize_box(delta):
    s    = state
    side = s['box_side'] + delta
    cx   = s['box_x'] + s['box_side'] // 2
    cy   = s['box_y'] + s['box_side'] // 2
    nx   = cx - side // 2
    ny   = cy - side // 2
    nx, ny, side = clamp_box(nx, ny, side, s['disp_w'], s['disp_h'])
    s['box_x'], s['box_y'], s['box_side'] = nx, ny, side


def draw_overlay(base):
    s  = state
    x0, y0 = s['box_x'], s['box_y']
    x1, y1 = x0 + s['box_side'], y0 + s['box_side']
    w, h   = s['disp_w'], s['disp_h']

    frame = base.copy()

    # Dim outside
    mask      = np.zeros(frame.shape[:2], dtype=np.uint8)
    cv2.rectangle(mask, (x0, y0), (x1, y1), 255, -1)
    outside   = mask == 0
    dim       = (frame * (1 - DIM_ALPHA)).astype(np.uint8)
    frame[outside] = dim[outside]

    # Box border
    cv2.rectangle(frame, (x0, y0), (x1, y1), BOX_COLOR, 2)

    # Rule-of-thirds
    side = s['box_side']
    for i in (1, 2):
        fx = x0 + i * side // 3
        fy = y0 + i * side // 3
        cv2.line(frame, (fx, y0), (fx, y1), BOX_COLOR, 1, cv2.LINE_AA)
        cv2.line(frame, (x0, fy), (x1, fy), BOX_COLOR, 1, cv2.LINE_AA)

    # Corner handles
    hs = 10
    for hx, hy in [(x0, y0), (x1, y0), (x0, y1), (x1, y1)]:
        cv2.rectangle(frame, (hx - hs, hy - hs), (hx + hs, hy + hs), BOX_COLOR, -1)

    return frame


def process(paths):
    s   = state
    win = "Crop Tool"
    cv2.namedWindow(win, cv2.WINDOW_AUTOSIZE)
    cv2.setMouseCallback(win, mouse_cb)

    for idx, path in enumerate(paths):
        pil    = Image.open(path).convert("RGB")
        ow, oh = pil.size
        scale  = min(MAX_DIM / ow, MAX_DIM / oh, 1.0)
        dw, dh = int(ow * scale), int(oh * scale)
        s['disp_w'], s['disp_h'] = dw, dh

        pil_d  = pil.resize((dw, dh), Image.LANCZOS)
        base   = cv2.cvtColor(np.array(pil_d), cv2.COLOR_RGB2BGR)

        # Initial centered square
        side       = min(dw, dh)
        s['box_side'] = side
        s['box_x']    = (dw - side) // 2
        s['box_y']    = (dh - side) // 2

        name = os.path.basename(path)
        print(f"\n[{idx+1}/{len(paths)}] {name}  ({ow}x{oh})")

        while True:
            frame = draw_overlay(base)
            hint  = f"[{idx+1}/{len(paths)}] {name}  | scroll=resize  +/-=resize  Enter=save  S=skip  Q=quit"
            cv2.putText(frame, hint, (8, 22),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
            size_hint = f"box: {s['box_side']}px (display)"
            cv2.putText(frame, size_hint, (8, dh - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, BOX_COLOR, 1, cv2.LINE_AA)
            cv2.imshow(win, frame)

            key = cv2.waitKey(16) & 0xFF

            if key in (13, 32):      # Enter / Space → save
                ox   = int(s['box_x'] / scale)
                oy   = int(s['box_y'] / scale)
                side = int(s['box_side'] / scale)
                ox   = max(0, min(ox, ow - side))
                oy   = max(0, min(oy, oh - side))
                pil.crop((ox, oy, ox + side, oy + side)).save(path)
                print(f"  Saved  crop=({ox},{oy},{ox+side},{oy+side})")
                break

            elif key in (ord('s'), ord('S')):
                print("  Skipped.")
                break

            elif key in (ord('q'), ord('Q'), 27):
                print("Quit.")
                cv2.destroyAllWindows()
                return

            elif key in (ord('+'), ord('=')):
                resize_box(+STEP)

            elif key in (ord('-'), ord('_')):
                resize_box(-STEP)

    print("\nAll done.")
    cv2.destroyAllWindows()


def get_images(folder):
    script = os.path.basename(__file__)
    return sorted([
        os.path.join(folder, f)
        for f in os.listdir(folder)
        if os.path.splitext(f)[1] in SUPPORTED and f != script
    ])


def rebuild_site(folder):
    site_root = os.path.abspath(os.path.join(folder, '..', '..'))
    print(f"\nRebuilding Jekyll site at {site_root} ...")
    ret = os.system(f'cd "{site_root}" && bundle exec jekyll build --baseurl ""')
    if ret == 0:
        print("Jekyll build complete.")
    else:
        print("Jekyll build failed — check output above.")


def main():
    folder = os.path.dirname(os.path.abspath(__file__))
    paths  = get_images(folder)
    if not paths:
        print("No images found.")
        sys.exit(0)
    print(f"Found {len(paths)} image(s).")
    process(paths)
    rebuild_site(folder)


if __name__ == "__main__":
    main()
