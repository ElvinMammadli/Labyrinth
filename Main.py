import time
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
import matplotlib.pyplot as plt
from PIL import Image, ImageTk, ImageDraw
import Functions as algo
from dot_functions import Dot

root = Tk()
# add Label for helping
information_label = Label(root, text="Left Click for Source\nRight Click for Destination ")
information_label.pack()

# adding the image
File = askopenfilename(parent=root, initialdir="./", title='Select File')
original = Image.open(File)

image = ImageTk.PhotoImage(original)
frame = Frame(root, width=300, height=300)
frame.pack(expand=True, fill=BOTH)

# setting up a tkinter canvas
w = Canvas(frame, bg='#FFFFFF', width=300, height=300, scrollregion=(0, 0, 2000, 2000))
hbar = Scrollbar(frame, orient=HORIZONTAL)
hbar.pack(side=BOTTOM, fill=X)
hbar.config(command=w.xview)
vbar = Scrollbar(frame, orient=VERTICAL)
vbar.pack(side=RIGHT, fill=Y)
vbar.config(command=w.yview)

w.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
w.pack(side=LEFT, expand=True, fill=BOTH)

# add image to canvas
w.create_image(0, 0, image=image, anchor="nw")
draw = ImageDraw.Draw(original)

# convert picture to rgb
rgb_im = original.convert('RGB')
# create Dots
sourceDot = Dot(0, 0, rgb_im)
destDot = Dot(0, 0, rgb_im)
# set Dot names
sourceDot.setDotName("Source Dot")
destDot.setDotName("Dest Dot")
# set Dots as not selected
sourceDotSelected = False
destDotSelected = False


def pop_msg(msg):
    pop_message = tk.Toplevel(root)
    pop_message.wm_title("!")
    pop_message.tkraise(root)  # This just tells the message to be on top of the root window.
    tk.Label(pop_message, text=msg).pack(side="top", fill="x", pady=10)
    tk.Button(pop_message, text="Ok", command=pop_message.destroy).pack()
    # Notice that you do not use mainloop() here on the Toplevel() window


def draw_to_image(image, end_point, imageName):
    global original
    image = original.copy()
    while end_point.parent is not False:
        draw = ImageDraw.Draw(image)
        draw.point((end_point.parent.x, end_point.parent.y), fill="red")
        end_point = end_point.parent
    image.save(imageName)
    image.close()

def startAlgorithms():
    if sourceDotSelected and destDotSelected:
        global sourceDot
        global destDot
        sourceDot1 = sourceDot
        destDot1 = destDot
        sourceDot2 = sourceDot
        destDot2 = destDot
        sourceDot3 = sourceDot
        destDot3 = destDot
        sourceDot4 = sourceDot
        destDot4 = destDot

        print("Source and Destination Dot are selected.")

        t0 = time.time()
        end_point1, readCountStack1, writeCountStack1 = algo.bfs_heap(sourceDot1, destDot1)
        t1 = time.time()
        totalbestfirstheap = t1 - t0
        draw_to_image(original, end_point1, "_bfsHeap.png")

        t0 = time.time()
        end_point2, readCountStack2, writeCountStack2 = algo.bfs_stack(sourceDot2, destDot2)
        t1 = time.time()
        totalbestfirststack = t1 - t0
        draw_to_image(original, end_point2, "_bfsStack.png")

        t0 = time.time()
        end_point3, readCountStack3, writeCountStack3 = algo.as_stack(sourceDot3, destDot3)
        t1 = time.time()
        totalaStarStack = t1 - t0
        draw_to_image(original, end_point3, "_aStarStack.png")

        t0 = time.time()
        end_point4, readCountStack4, writeCountStack4 = algo.as_heap(sourceDot4, destDot4)
        t1 = time.time()
        totalaStarHeap = t1 - t0
        draw_to_image(original, end_point4, "_aStarHeap.png")


        timeArray = [totalbestfirstheap, totalbestfirststack, totalaStarStack, totalaStarHeap]
        namesArray = ["BFSHeap", "BFSStack", "A*Stack", "A*Heap"]
        costArray = [end_point1.distance_between_start, end_point2.distance_between_start, end_point3.distance_between_start,
                     end_point4.distance_between_start]
        readCountArray = [readCountStack1, readCountStack2, readCountStack3, readCountStack4]
        writeCountArray = [writeCountStack1, writeCountStack2, writeCountStack3, writeCountStack4]
        axis_font = {'fontname': 'Arial', 'size': '14'}

        plt.subplot(221)
        plt.bar(namesArray, costArray, 0.3)
        plt.title('Cost')
        plt.subplot(222)
        plt.bar(namesArray, timeArray, 0.3)
        plt.title('Time')

        # symmetric log
        plt.subplot(223)
        plt.bar(namesArray, writeCountArray, 0.3)
        plt.title('Write')

        # logit
        plt.subplot(224)
        plt.bar(namesArray, readCountArray, 0.3)
        plt.title('Read')
        plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
                            wspace=0.35)
        plt.savefig("graph.png")

    else:
        pop_msg("Source and Destination Dot are not selected.")


# create button to start algorithms
button1 = Button(root, text="startAlgorithms", command=startAlgorithms)
button1.pack()


# Determine the origin by clicking
def getoriginSource(eventorigin):
    global sourceDotSelected
    if not sourceDotSelected:
        sourceDotSelected = True
        global sourceDot
        global x0, y0
        global original, w, image
        x0 = eventorigin.x
        y0 = eventorigin.y
        sourceDot.setCoordinates(x0, y0)
        draw = ImageDraw.Draw(original)
        for i in range(-1, 1):
            for j in range(-1, 1):
                draw.point((x0 + i, y0 + j), fill=255)

        image = ImageTk.PhotoImage(original)
        w.create_image(0, 0, image=image, anchor="nw")
        original.save("asd.png")
    sourceDot.setRedValue()


def getoriginDestination(eventorigin):
    global destDotSelected
    if not destDotSelected:
        destDotSelected = True
        global destDot
        global x0, y0
        global original, w, image
        x0 = eventorigin.x
        y0 = eventorigin.y
        destDot.setCoordinates(x0, y0)
        draw = ImageDraw.Draw(original)
        for i in range(-1, 1):
            for j in range(-1, 1):
                draw.point((x0 + i, y0 + j), fill=255)

        image = ImageTk.PhotoImage(original)
        w.create_image(0, 0, image=image, anchor="nw")
        original.save("asd.png")
    destDot.setRedValue()


# mouseclick event
w.bind("<1>", getoriginSource)
w.bind("<3>", getoriginDestination)

root.mainloop()
