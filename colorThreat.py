import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % tuple(int(c) for c in rgb)

def extract_dominant_color(region, k=3):
    pixels = region.reshape((-1, 3))
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(pixels)

    labels = kmeans.labels_
    counts = np.bincount(labels)
    dominant_index = np.argmax(counts)
    dominant_color_bgr = kmeans.cluster_centers_[dominant_index].astype(int)
    return dominant_color_bgr[::-1]  # BGR → RGB

# === STEP 1: Load image ===
image_path = "resources/img_1.png"  # change this path
img = cv2.imread(image_path)
img = cv2.resize(img, (600, 400))

# === STEP 2: Input order quantity ===
order_qty = int(input("📦 Enter number of boxers to produce: "))

thread_data = {}

while True:
    # Select region
    roi = cv2.selectROI("Select a region (Fabric/Elastic), ESC to skip", img, False, False)
    if roi == (0, 0, 0, 0):
        break

    x, y, w, h = roi
    region = img[y:y+h, x:x+w]

    # Extract color
    dominant_rgb = extract_dominant_color(region, k=3)
    hex_code = rgb_to_hex(dominant_rgb)

    # Ask part name
    part = input(f"🧵 What part is this color for (e.g., fabric, elastic)? ").strip().lower()

    # Ask thread per boxer
    thread_per_unit = float(input(f"🔢 How much thread (in meters) needed per boxer for {part}? "))

    # Save data
    thread_data[part] = {
        "color": hex_code,
        "rgb": dominant_rgb.tolist(),
        "thread_per_boxer": thread_per_unit,
        "total_thread": thread_per_unit * order_qty
    }

    # Show color block
    block = np.zeros((100, 300, 3), dtype='uint8')
    block[:] = dominant_rgb[::-1]  # RGB to BGR
    plt.imshow(cv2.cvtColor(block, cv2.COLOR_BGR2RGB))
    plt.title(f"{part.upper()} → {hex_code}")
    plt.axis('off')
    plt.show()

    print(f"✅ Saved: {part} ({hex_code}) needs {thread_per_unit * order_qty:.2f} meters total.\n")

cv2.destroyAllWindows()

# === STEP 3: Summary Output ===
print("\n📊 FINAL THREAD ORDER SUMMARY")
print(f"Total boxers to produce: {order_qty}\n")
for part, info in thread_data.items():
    print(f"{part.capitalize()}:")
    print(f"  Color: {info['color']}")
    print(f"  RGB: {info['rgb']}")
    print(f"  Thread per boxer: {info['thread_per_boxer']} meters")
    print(f"  ➤ Total thread needed: {info['total_thread']} meters\n")
