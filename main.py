import cv2
import numpy as np
import urllib.request
from findImage import *
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk
from Computer import *
import serial

# url = "http://192.168.100.43:8080/shot.jpg"
# imgResp = urllib.request.urlopen(url)
# image = np.array(bytearray(imgResp.read()), dtype=np.uint8)
# image = cv2.imdecode(image, -1)

# image = cv2.imread('D:\\OCR\\train-data\\ZTable\\t2.png')
# image = cv2.imread('D:\\OCR\\train-data\\ZTable\\2.jpg')

vid = cv2.VideoCapture(0)

_, frame = vid.read()
# print(frame.shape)
frame = frame[:320, 160:frame.shape[1] - 160]
image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
img = Image.fromarray(image)
#
# print(image.shape)
#
image = cv2.resize(image, (500, 500))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# cv2.imshow("test", gray)

ret, thresh = cv2.threshold(gray, 137, 255,  cv2.THRESH_BINARY_INV)

# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# print(len(contours))

# find = find_image(gray, thresh, contours)
# data = find.listData

# <============= era bo gamakaya ===================>
root = tk.Tk()

# img = ImageTk.PhotoImage(image=Image.fromarray(gray))

rgb = tk.Label(root)
rgb.grid(column=2, row=0)
grays = tk.Label(root)
grays.grid(column=3, row=0)
threshhold = tk.Label(root)
threshhold.grid(column=4, row=0)

def video_stream():
    _, frame = vid.read()
    imrgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    imrgb = imrgb[:320, 160:frame.shape[1] - 160]
    imrgb = cv2.resize(imrgb, (500, 500))
    imgray = cv2.cvtColor(imrgb, cv2.COLOR_BGR2GRAY)
    ret, imthresh = cv2.threshold(imgray, 137, 250, cv2.THRESH_BINARY_INV)

    img = Image.fromarray(imrgb)
    imgtkrgb = ImageTk.PhotoImage(image=img)
    imgg = Image.fromarray(imgray)
    imgtkgray = ImageTk.PhotoImage(image=imgg)
    imgt = Image.fromarray(imthresh)
    imgtkth = ImageTk.PhotoImage(image=imgt)

    rgb.imgtkgray = imgtkrgb
    rgb.configure(image=imgtkrgb)

    grays.imgtkgray = imgtkgray
    grays.configure(image=imgtkgray)

    threshhold.imgtkth = imgtkth
    threshhold.configure(image=imgtkth)

    root.after(10, video_stream)


def isWinner(bo, le):
    return ((bo[6] == le and bo[7] == le and bo[8] == le) or
            (bo[3] == le and bo[4] == le and bo[5] == le) or
            (bo[0] == le and bo[1] == le and bo[2] == le) or
            (bo[6] == le and bo[3] == le and bo[0] == le) or
            (bo[8] == le and bo[5] == le and bo[2] == le) or
            (bo[7] == le and bo[4] == le and bo[1] == le) or
            (bo[6] == le and bo[4] == le and bo[2] == le) or
            (bo[8] == le and bo[4] == le and bo[0] == le))




def DrawMove(board):
    print("+-----------+")
    print('|   |   |   |')
    print('| ' + board[8] + ' | ' + board[7] + ' | ' + board[6] + ' |')
    print('|   |   |   |')
    print('+-----------+')
    print('|   |   |   |')
    print('| ' + board[5] + ' | ' + board[4] + ' | ' + board[3] + ' |')
    print('|   |   |   |')
    print('+-----------+')
    print('|   |   |   |')
    print('| ' + board[2] + ' | ' + board[1] + ' | ' + board[0] + ' |')
    print('|   |   |   |')
    print("+-----------+")


board = [' '] * 9
count = 0

xpoints = []
ypoints = []

# ser = serial.Serial('COM3', 9600)


def drawX(start, end):
    cv2.line(gray, (start[0], start[1]), (end[0], end[1]), (0, 0, 0), 3)
    cv2.line(gray, (start[0], end[1]), (end[0], start[1]), (0, 0, 0), 3)

def moveCom(i):
    if i == 0:
        drawX([381, 75], [427, 122])
    elif i == 1:
        drawX([383, 212], [424, 223])
    elif i == 2:
        drawX([378, 361], [430, 424])

    elif i == 3:
        drawX([234, 64], [280, 126])
        # drawX([383, 212], [424, 223])
    elif i == 4:
        drawX([241, 210], [285, 270])
    elif i == 5:
        drawX([230, 357], [280, 419])
    elif i == 6:
        drawX([97, 80], [138, 118])
    elif i == 7:
        drawX([84, 200], [127, 262])
    elif i == 8:
        drawX([91, 359], [137, 418])


def paint(event):
    x1, y1 = (event.x - 4), (event.y - 4)
    x2, y2 = (event.x + 4), (event.y + 4)
    canvas.create_oval(x1, y1, x2, y2, fill='black')
    xpoints.append(x1)
    ypoints.append(y1)
    # print(x1, y1)

def process():

    global xpoints
    global ypoints

    # elementos = len(xpoints)

    # for p in range(elementos):
    #     x = xpoints[p]
    #     y = ypoints[p]
    #     cv2.circle(gray, (x, y), 3, (0, 0, 255), -1)

    _, frame = vid.read()
    imrgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    imrgb = imrgb[:320, 160:frame.shape[1] - 160]
    imrgb = cv2.resize(imrgb, (500, 500))
    gray = cv2.cvtColor(imrgb, cv2.COLOR_BGR2GRAY)

    # cv2.imshow('image', gray)

    ret, imthresh = cv2.threshold(gray, 137, 250, cv2.THRESH_BINARY_INV)

    dilate = cv2.dilate(imthresh, None)
    erode = cv2.erode(dilate, None)

    contours, hierarchy = cv2.findContours(erode, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    find = find_image(gray, imthresh, contours)
    data = find.listData

    # print("2 ", data)
    if find.count == 9:
        for d in data:
            board[d[0]] = d[1]
        DrawMove(board)
        com = Computer()
        move = com.ComputerMove(board, 'X')
        # ser.write(str(move+1).encode())
        if(move is not None):
            board[move] = 'X'
            DrawMove(board)
            # moveCom(move)
        if(isWinner(board, 'X')):
            print("Computer Win !")
        if (isWinner(board, 'O')):
            print("User Win !")
        if(len(data) >= 9):
            print("No Winner !")
        print(len(data))
        cv2.imshow('image', gray)


video_stream()

# canvas = tk.Canvas(root, width=500, height=600)
# canvas.grid(column=0, row=0)
# canvas.create_image(0, 0, anchor="nw", image=img)

# canvas.bind("<B1-Motion>", paint)

button = tk.Button(root, text='Save image', width=20, command=process).grid(column=2, row=2)

tk.mainloop()


cv2.waitKey(0)
cv2.destroyAllWindows()








# contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
# min_rect_len = 90
# max_rect_len = 150
# # bo detnawae 4 goshakan
# c = 0
#
# im = []
# for contour in contours:
#     (x, y, w, h) = cv2.boundingRect(contour)
#     if (h > min_rect_len and w > min_rect_len) and (h < max_rect_len and w < max_rect_len):
#         cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 1)
#         cv2.putText(image, str(c), (x + 20, y + 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
#         im.append(thresh[y + 3: y + h - 3, x + 3: x + w - 3])
#         c += 1
#
# cv2.imshow('i', image)

