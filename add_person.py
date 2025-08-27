import cv2
import os

dataset_dir = "dataset"

# Ask for person's name
person_name = input("Enter the person's name: ").strip()
person_folder = os.path.join(dataset_dir, person_name)

# Create folder if not exists
os.makedirs(person_folder, exist_ok=True)

# Start webcam
cap = cv2.VideoCapture(0)
count = 0
print("[INFO] Capturing images. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Add Person - Press 'q' to stop", frame)

    # Save image every 5 frames for variety
    if count % 5 == 0:
        img_path = os.path.join(person_folder, f"{person_name}_{count}.jpg")
        cv2.imwrite(img_path, frame)
        print(f"[SAVED] {img_path}")

    count += 1

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print(f"[INFO] Saved {count//5} images for {person_name}")
