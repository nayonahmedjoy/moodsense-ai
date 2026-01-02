import cv2
from deepface import DeepFace

cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        try:
            result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
            if isinstance(result, list) and len(result) > 0:
                first_result = result[0]
                dominant_emotion = first_result['dominant_emotion']
                emotion_scores = first_result['emotion']
                filtered_emotions = {k: emotion_scores[k] for k in ['happy', 'neutral', 'surprise'] if k in emotion_scores}

                cv2.putText(frame, f"Emotion: {dominant_emotion}", (50, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

                for i, (emotion, score) in enumerate(filtered_emotions.items()):
                    cv2.putText(frame, f"{emotion}: {score:.2f}%", (50, 100 + i * 30),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

        except Exception as e:
            print("Error:", e)

        # Show frame
        cv2.imshow("Emotion Detector", frame)

        # Break if 'q' is pressed OR window is closed
        if cv2.getWindowProperty("Emotion Detector", cv2.WND_PROP_VISIBLE) < 1:
            print("Window closed manually.")
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Pressed Q. Exiting...")
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
