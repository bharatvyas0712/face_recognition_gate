import cv2
import face_recognition
import pickle
import numpy as np

# Load model and label encoder
with open("svm_model.pkl", "rb") as f:
    clf = pickle.load(f)

with open("label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

video = cv2.VideoCapture(0)
print("[INFO] Starting real-time recognition...")

while True:
    ret, frame = video.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        probabilities = clf.predict_proba([face_encoding])[0]
        predicted_label = clf.predict([face_encoding])[0]
        name = label_encoder.inverse_transform([predicted_label])[0]
        confidence = probabilities[predicted_label] * 100

        if confidence > 80:  # Threshold for gate opening
            text = f"{name} ({confidence:.1f}%) - Gate Open"
            color = (0, 255, 0)
            # Simulate gate open action
            print(f"[GATE] Access Granted to {name}")
        else:
            text = "Unknown - Access Denied"
            color = (0, 0, 255)

        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(frame, text, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("Face Recognition Gate - SVM", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

video.release()
cv2.destroyAllWindows()
