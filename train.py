import os
import face_recognition
import numpy as np
from sklearn import svm
from sklearn.preprocessing import LabelEncoder
import pickle

# Dataset path: each folder inside 'dataset/' is a person name
dataset_dir = "dataset"
encodings = []
names = []

print("[INFO] Loading images and extracting embeddings...")
for person_name in os.listdir(dataset_dir):
    person_folder = os.path.join(dataset_dir, person_name)
    if not os.path.isdir(person_folder):
        continue

    for image_file in os.listdir(person_folder):
        image_path = os.path.join(person_folder, image_file)
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)

        if len(face_locations) != 1:
            print(f"[WARN] Skipping {image_file} (no face or multiple faces detected)")
            continue

        face_encoding = face_recognition.face_encodings(image, known_face_locations=face_locations)[0]
        encodings.append(face_encoding)
        names.append(person_name)

# Encode labels
label_encoder = LabelEncoder()
labels = label_encoder.fit_transform(names)

# Train SVM
print("[INFO] Training SVM classifier...")
clf = svm.SVC(kernel='linear', probability=True)
clf.fit(encodings, labels)

# Save model & label encoder
with open("svm_model.pkl", "wb") as f:
    pickle.dump(clf, f)

with open("label_encoder.pkl", "wb") as f:
    pickle.dump(label_encoder, f)

print("[INFO] Training complete. Model saved as svm_model.pkl")
