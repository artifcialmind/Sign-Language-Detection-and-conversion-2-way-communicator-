import numpy as np
import speech_recognition as sr

import cv2


def speech2text(dur):
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            data = r.record(source, duration=dur)
            text = r.recognize_google(data)
        return text
    except:
        print("Couldn't here properly, try again or try with text")
        return None


def get_signs(text):

        text.capitalize()
        path = "C:/Users/91797/OneDrive/Desktop/feature2/"
        arr = []
        for y in text:
            if y == " ":
                img = cv2.imread(path + "space.png")
                img = cv2.resize(img, (80, 80))
                arr.append(img)
            else:
                img = cv2.imread(path + y + ".png")
                img = cv2.resize(img, (80, 80))
                arr.append(img)
        if len(arr) % 16 != 0:
            while len(arr) % 16 != 0:
                im = cv2.imread(path + "space.png")
                im = cv2.resize(im, (80, 80))
                arr.append(im)
        current = arr[0]
        j = 1
        images = []
        print(len(arr))
        while j <= len(arr):
            if j % 16 == 0:
                images.append(current)
                if j == len(arr):
                    break
                current = arr[j]
            else:
                print(f'current shape: {current.shape}, img: {arr[j].shape}')
                current = np.concatenate((current, arr[j]), axis=1)
            j += 1
        final_img = images[0]
        j = 1
        while j < len(images):
            final_img = np.concatenate((final_img, images[j]), axis=0)
            j += 1
        print(len(arr))
        cv2.imshow("Frame", final_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        print("Couldn't here")


# print("Enter duration: ")
# x = int(input())
# temp = speech2text(x)
# if temp is not None:
    # get_signs(temp)
