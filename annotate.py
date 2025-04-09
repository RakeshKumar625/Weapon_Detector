import cv2
import os

img_dir = "negative"
output_file = "negatives.txt"

images = [f for f in os.listdir(img_dir) if f.endswith(".jpg") or f.endswith(".jpeg")]

with open(output_file, "w") as f:
    for img_name in images:
        img_path = os.path.join(img_dir, img_name)
        img = cv2.imread(img_path)
        if img is None:
            continue

        roi = cv2.selectROI(f"Annotating {img_name}", img, fromCenter=False)
        cv2.destroyWindow(f"Annotating {img_name}")

        if sum(roi) > 0:  # skip if nothing selected
            x, y, w, h = roi
            line = f"{img_dir}/{img_name} 1 {x} {y} {w} {h}\n"
            f.write(line)
            print("Annotated:", line.strip())
