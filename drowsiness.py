from scipy.spatial import distance as dist
from imutils.video import VideoStream
from imutils import face_utils
import imutils
import time
import dlib
import cv2
import threading
import winsound
import pyttsx3

# -------------------- VOICE ENGINE -------------------- #

engine = pyttsx3.init()

alarm_active = False

# -------------------- ALARM FUNCTION -------------------- #

def sound_alarm(message):
    global alarm_active

    try:
        engine.stop()

        # Voice alert (plays once)
        engine.say(message)
        engine.runAndWait()

    except RuntimeError:
        pass

    # Continuous beep until alert ends
    while alarm_active:
        winsound.Beep(1000, 700)
        time.sleep(0.3)

# -------------------- EYE ASPECT RATIO -------------------- #

def eye_aspect_ratio(eye):

    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])

    ear = (A + B) / (2.0 * C)

    return ear

# -------------------- MOUTH ASPECT RATIO -------------------- #

def mouth_aspect_ratio(mouth):

    A = dist.euclidean(mouth[2], mouth[10])
    B = dist.euclidean(mouth[4], mouth[8])
    C = dist.euclidean(mouth[0], mouth[6])

    mar = (A + B) / (2.0 * C)

    return mar

# -------------------- THRESHOLDS -------------------- #

EYE_AR_THRESH = 0.25
EYE_AR_CONSEC_FRAMES = 20

MAR_THRESHOLD = 0.75
YAWN_CONSEC_FRAMES = 15

COUNTER = 0
yawn_counter = 0

# -------------------- LOAD MODELS -------------------- #

print("[INFO] Loading models...")

detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor(
    "shape_predictor_68_face_landmarks.dat"
)

# Facial landmark indexes
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]
(mStart, mEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]

# -------------------- START CAMERA -------------------- #

print("[INFO] Starting camera...")

vs = VideoStream(src=0).start()

time.sleep(2.0)

# -------------------- MAIN LOOP -------------------- #

while True:

    frame = vs.read()

    frame = imutils.resize(frame, width=640)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 0)

    for rect in rects:

        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        # -------------------- EYES -------------------- #

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)

        ear = (leftEAR + rightEAR) / 2.0

        # -------------------- MOUTH -------------------- #

        mouth = shape[mStart:mEnd]

        mar = mouth_aspect_ratio(mouth)

        # Draw contours
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        mouthHull = cv2.convexHull(mouth)

        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [mouthHull], -1, (255, 0, 0), 1)

        # -------------------- DROWSINESS DETECTION -------------------- #

        if ear < EYE_AR_THRESH:

            COUNTER += 1

            if COUNTER >= EYE_AR_CONSEC_FRAMES:

                cv2.putText(frame,
                            "DROWSINESS ALERT!",
                            (120, 100),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 0, 255),
                            3)

                if not alarm_active:

                    alarm_active = True

                    threading.Thread(
                        target=sound_alarm,
                        args=("Wake up! Driver is feeling sleepy!",),
                        daemon=True
                    ).start()

        else:

            COUNTER = 0
            alarm_active = False

        # -------------------- YAWNING DETECTION -------------------- #

        if mar > MAR_THRESHOLD:

            yawn_counter += 1

            if yawn_counter >= YAWN_CONSEC_FRAMES:

                cv2.putText(frame,
                            "YAWN ALERT!",
                            (170, 150),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (255, 0, 0),
                            3)

                if not alarm_active:

                    alarm_active = True

                    threading.Thread(
                        target=sound_alarm,
                        args=("Warning! Yawning detected!",),
                        daemon=True
                    ).start()

        else:

            yawn_counter = 0

        # -------------------- DISPLAY VALUES -------------------- #

        cv2.putText(frame,
                    f"EAR: {ear:.2f}",
                    (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2)

        cv2.putText(frame,
                    f"MAR: {mar:.2f}",
                    (10, 60),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (255, 0, 0),
                    2)

    # -------------------- SHOW FRAME -------------------- #

    cv2.imshow("Driver Drowsiness Detection System", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

# -------------------- CLEANUP -------------------- #

cv2.destroyAllWindows()
vs.stop()