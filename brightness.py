import time
import warnings
warnings.filterwarnings("ignore")
import mediapipe as mp
import cv2
from keras import models
import numpy as np
from textblob import TextBlob
model = models.load_model("C:/Users/91797/OneDrive/Desktop/2 way communicator/Models/br.h5")
hm = {}

j = 0
for i in range(97, 123):
    hm[j] = chr(i)
    j += 1


def cropped_img(frame, arr):
    return frame[arr[1]: arr[3], arr[0]: arr[2]]


mphands = mp.solutions.hands
hands = mphands.Hands()
mp_drawing = mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

_, frame = cap.read()

h, w, c = frame.shape
current = ""
word = ""
i = 0
def start():
    mphands = mp.solutions.hands
    hands = mphands.Hands()
    mp_drawing = mp.solutions.drawing_utils
    cap = cv2.VideoCapture(0)

    _, frame = cap.read()

    h, w, c = frame.shape
    current = ""
    word = " "
    i = 0
    ptr = 0
    frames_remaining_to_Stop = 100
    while True and frames_remaining_to_Stop > 0:
            _, frame = cap.read()
            if i == 0:
                print("ready your hand to start")
                time.sleep(3)
                i = 1
            framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(framergb)
            hand_landmarks = result.multi_hand_landmarks
            if hand_landmarks is None:
                if word[-1] == " ":
                    pass
                else:
                    word += " "
                frames_remaining_to_Stop -= 1
            if hand_landmarks is not None and len(hand_landmarks) >= 2:
                time.sleep(3)
                word += current
                print(word)
            if hand_landmarks:
                frames_remaining_to_Stop = 100
                for handLMs in hand_landmarks:
                    x_max = 0
                    y_max = 0
                    x_min = w
                    y_min = h
                    for lm in handLMs.landmark:
                        x, y = int(lm.x * w), int(lm.y * h)
                        if x > x_max:
                            x_max = x
                        if x < x_min:
                            x_min = x
                        if y > y_max:
                            y_max = y
                        if y < y_min:
                            y_min = y
                    try:
                        #print(f'found: {[x_min, y_min, x_max, y_max]}')
                        detected_img = cropped_img(frame, [x_min, y_min, x_max, y_max])
                        detected_img = detected_img/255
                        detected_img = cv2.resize(detected_img, (40, 40))
                        cv2.imshow("detected_img", detected_img)
                        detected_img = np.expand_dims(detected_img, axis=0)
                        prediction = np.argmax(model.predict(detected_img))
                        current = hm[prediction]
                        print(current)
                        temp2 = cv2.rectangle(frame, (x_min, y_min), (x_max, y_max), (0, 0, 255), 2)
                        temp2 = cv2.putText(temp2, "Alphabet prediction: " + hm[prediction], (x_min, y_max),
                                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
                    except:
                        print("error")
                        pass
                    #mp_drawing.draw_landmarks(frame, handLMs, mphands.HAND_CONNECTIONS)
            cv2.imshow("Frame", frame)
            cv2.waitKey(1)
    cv2.destroyAllWindows()
    temp = word
    sentence = TextBlob(word)
    word = sentence.correct()
    return word, temp


#print(start())
