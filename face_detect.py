import cv2
import os

print("Animal Face Detector")

# Load Haar cascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
cat_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalcatface.xml')

# Input image name (use raw string for Windows path)
img_name = r"C:\Users\Chaitra G\OneDrive\Pictures\Screenshots\Screenshot 2026-04-13 180605.png"

# Check file exists
if not os.path.exists(img_name):
    print("File not found! Please keep image in same folder.")
    exit()

# Read image
img_color = cv2.imread(img_name)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

# Detect faces
human_faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)
cat_faces = cat_cascade.detectMultiScale(img_gray, 1.1, 4)

print(f"Human faces: {len(human_faces)}")
print(f"Cat faces: {len(cat_faces)}")

# Draw rectangles
for (x, y, w, h) in human_faces:
    cv2.rectangle(img_color, (x, y), (x+w, y+h), (0, 255, 0), 3)

for (x, y, w, h) in cat_faces:
    cv2.rectangle(img_color, (x, y), (x+w, y+h), (0, 255, 255), 3)

# Save output image
cv2.imwrite("animals_found.jpg", img_color)
print("Saved output as animals_found.jpg")

# Show output window
cv2.imshow("Animal Face Detector", img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
