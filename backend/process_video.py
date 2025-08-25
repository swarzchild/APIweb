import os
from extract_landmark import extract_landmark_sequence
from predict_gesture_knn import predict_gesture_knn


def process_video(video_path: str) -> dict:
    """
    ประมวลผลวิดีโอ:
      1. Extract landmark เป็น .csv
      2. ใช้โมเดล KNN ทำนาย gesture
    :param video_path: path ของไฟล์วิดีโอที่อัปโหลดมา
    :return: dict {gesture, confidence หรือ error}
    """
    try:
        print(f"📹 Processing video: {video_path}")

        # 1) Extract landmark → CSV
        csv_path = extract_landmark_sequence(
            video_path,
            label="predict_tmp",
            out_dir="backend/uploads"
        )

        if csv_path is None:
            return {"error": "❌ ไม่สามารถดึง landmark จากวิดีโอได้"}

        print(f"✅ Landmark extracted to {csv_path}")

        # 2) Predict gesture ด้วยโมเดล KNN
        gesture, prob = predict_gesture_knn(csv_path)

        result = {"gesture": gesture}
        if prob is not None:
            result["confidence"] = float(max(prob))  # ความมั่นใจสูงสุด

        print(f"🎯 Prediction: {result}")
        return result

    except FileNotFoundError as e:
        return {"error": str(e)}
    except ValueError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": f"Unexpected error: {str(e)}"}
