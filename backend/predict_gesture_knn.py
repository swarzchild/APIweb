# 🔧 scripts/predict_gesture_knn.py — ทำนาย gesture ด้วยโมเดล KNN
import pandas as pd
import numpy as np
import joblib
import os

MODEL_PATH = "models/knn_gesture_model.pkl"


def extract_vector_from_csv(path):
    df = pd.read_csv(path)
    if len(df) < 4:
        return None
    mid = df.iloc[len(df)//4 : len(df)*3//4].mean(axis=0)
    vec = mid.values
    return vec


def predict_gesture_knn(csv_path):
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError("❌ ไม่พบโมเดล KNN กรุณารัน train_knn_model.py ก่อน")

    clf = joblib.load(MODEL_PATH)
    vec = extract_vector_from_csv(csv_path)

    if vec is None:
        raise ValueError("❌ ไฟล์ไม่มีข้อมูลเพียงพอ")

    pred = clf.predict([vec])[0]
    proba = clf.predict_proba([vec])[0] if hasattr(clf, "predict_proba") else None

    return pred, proba


# ✅ ตัวอย่างการใช้งาน
if __name__ == "__main__":
    test_csv = "data/landmarks/sawasdee3_sawasdee_phon.csv"
    label, prob = predict_gesture_knn(test_csv)
    print(f"🎯 Prediction: {label}")
    if prob is not None:
        print(f"Confidence: {np.max(prob):.2%}")
