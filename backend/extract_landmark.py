# 🔧 scripts/extract_landmark.py
import os
import cv2
import mediapipe as mp
import pandas as pd

def extract_landmark_sequence(video_path, label, out_dir="data/landmarks"):
    """
    ดึงลำดับ landmark 3D จากวิดีโอ และบันทึกเป็น .csv
    :param video_path: path ของไฟล์วิดีโอ
    :param label: ชื่อ gesture (ใช้ตั้งชื่อไฟล์)
    :param out_dir: โฟลเดอร์เก็บไฟล์ .csv
    :return: path ของไฟล์ที่บันทึก (หรือ None ถ้าล้มเหลว)
    """
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1)

    cap = cv2.VideoCapture(video_path)
    sequence = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            hand = results.multi_hand_landmarks[0]
            flat = []
            for lm in hand.landmark:
                flat.extend([lm.x, lm.y, lm.z])
            sequence.append(flat)

    cap.release()

    if not sequence:
        print("❌ ไม่พบ landmark ในวิดีโอนี้")
        return None

    df = pd.DataFrame(sequence)
    os.makedirs(out_dir, exist_ok=True)
    name = os.path.splitext(os.path.basename(video_path))[0]
    out_path = os.path.join(out_dir, f"{name}_{label}.csv")
    df.to_csv(out_path, index=False)
    print(f"✅ Saved landmark sequence to {out_path}")
    return out_path


# ✅ ตัวอย่างการเรียกใช้
if __name__ == "__main__":
    video_file = "data/raw_videos/demo_hello.mp4"
    extract_landmark_sequence(video_file, label="hello")
