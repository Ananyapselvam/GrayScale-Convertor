import cv2

# 📸 Load the image (make sure 'image.jpg' is in the same folder!)
img = cv2.imread("bhirat.jpg")
if img is None:
    print("❌ Image not found! Please check if 'image.jpg' is in the same folder 😭")
else:
    # 🎨 Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 🖼️ Show the images
    cv2.imshow("Original Image 💖", img)
    cv2.imshow("Grayscale ✨", gray)

    # 🛑 Wait for a key press
    cv2.waitKey(0)
    cv2.destroyAllWindows()
