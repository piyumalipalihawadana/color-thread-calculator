# color-thread-calculator
developing to  solve a encounted issue in garment industry
Tool for garment manufacturers to detect colors from customer design images and calculate thread requirements for production

# 🎨🧵 Color Thread Calculator for Garment Industry

This is a smart, lightweight tool designed for garment manufacturers to:

✅ Extract **dominant fabric and elastic colors** from customer-submitted design images  
✅ Let users **label parts** (e.g., fabric, elastic)  
✅ Define **thread requirement per part**  
✅ Calculate **total thread needed per color** for any number of boxers or garments  

---

## 🧠 How It Works

1. Upload a customer’s design image (e.g., boxer or T-shirt)
2. Use OpenCV to **manually select regions** (like fabric or elastic)
3. The system:
   - Detects the **dominant color**
   - Converts to **RGB and HEX**
   - Asks for part name and thread-per-unit input
4. User enters how many garments to produce
5. The tool outputs a **thread requirement summary** for ordering

---

## 🔧 Tech Used

- Python 3
- OpenCV (image processing)
- scikit-learn (KMeans clustering)
- matplotlib (for color previews)

---

## 📦 Sample Output
🎯 Detected Dominant Color:
RGB: [255 215 0]
HEX: #ffd700

📊 FINAL THREAD ORDER SUMMARY
Fabric:
Color: #ffd700
RGB: [255, 215, 0]
Thread per boxer: 25.0 meters
➤ Total thread needed: 250.0 meters
Elastic:
Color: #000000
RGB: [0, 0, 0]
Thread per boxer: 15.0 meters
➤ Total thread needed: 150.0 meters

## to be developing features:
-identify the garment patterns and predict the results

