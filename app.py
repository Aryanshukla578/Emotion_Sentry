import streamlit as st
import cv2
import numpy as np
import os

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

st.title("HoloSentry Emotion-Locked File")
status_placeholder = st.empty()
file_lock_placeholder = st.empty()

if 'emotion' not in st.session_state:
    st.session_state['emotion'] = None
if 'face_detected' not in st.session_state:
    st.session_state['face_detected'] = False
if 'capture_requested' not in st.session_state:
    st.session_state['capture_requested'] = False

img_file = st.camera_input("Take a picture to detect your emotion")
if img_file is not None:
    file_bytes = np.asarray(bytearray(img_file.read()), dtype=np.uint8)
    frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    if frame is not None:
        if len(frame.shape) == 3 and frame.shape[2] == 4:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(60, 60))
        detected_emotion = None
        if len(faces) == 0:
            status_placeholder.error("No face detected! Please ensure your face is well-lit and clearly visible to the camera.")
            st.session_state['face_detected'] = False
            st.session_state['emotion'] = None
        else:
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                roi_gray = gray[y:y+h, x:x+w]
                smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.7, minNeighbors=20)
                if len(smiles) > 0:
                    detected_emotion = "smile"
                    cv2.putText(frame, "Smiling", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,0), 2)
                else:
                    detected_emotion = "neutral"
                    cv2.putText(frame, "Neutral", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0,255,255), 2)
            st.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), channels="RGB")
            status_placeholder.success(f"Face detected! Emotion: {detected_emotion if detected_emotion else 'Unknown'}")
            st.session_state['face_detected'] = True
            st.session_state['emotion'] = detected_emotion
    else:
        status_placeholder.error("Could not decode image. Please try again.")
        st.session_state['face_detected'] = False
        st.session_state['emotion'] = None

if st.session_state['face_detected'] and st.session_state['emotion'] and not st.session_state['capture_requested']:
    if st.button(f"Capture this emotion ({st.session_state['emotion']}) to lock a file?", key=f"capture_{st.session_state['emotion']}"):
        st.session_state['capture_requested'] = True

if st.session_state['capture_requested']:
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f != 'app.py']
    file_to_lock = file_lock_placeholder.selectbox("Select a file to lock with your emotion:", files, key="file_select")
    if st.button("Lock File", key="lock_file"):
        st.success(f"File '{file_to_lock}' locked with emotion '{st.session_state['emotion']}'. (Demo: implement actual locking logic)")