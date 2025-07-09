# color-thread-calculator
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


