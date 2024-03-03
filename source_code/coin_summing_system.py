'''
Programmer name: Cheng Yong Tat
Program name: Coin Summing System
Program description: This program will calculate the numbers and total sum of coins based on                       the uploaded coin image.
Date: 20/09/2022
'''
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename
from fileinput import filename
from PIL import Image, ImageTk
import numpy as np
import cv2
import os

# Create window object
app = Tk()
app.destroy()
'''
#file_dir = os.path.dirname(os.path.realpath('__file__'))
script_path = os.path.abspath(__file__)
file_dir = os.path.split(script_path)[0]
print("Path:" + file_dir)

logoImage = os.path.join(file_dir, 'assets/logo.png')
masterNewCoinImage = os.path.join(file_dir, 'assets/new_coin_0.png')
masterOldCoinImage = os.path.join(file_dir, 'assets/old_coin_0.png')
coverImage = os.path.join(file_dir, 'assets/cover.png')

print("Path 2:" + logoImage)'''

def openAbout():
    
    about = tk.Toplevel() # TOPLEVEL IS IMPORTANT FOR POP UP WINDOW
    about.grab_set() # Used to prevent any interactions with other windows

    # Get screen width and height
    screenWidth = app.winfo_screenwidth()
    screenHeight = app.winfo_screenheight()
    
    # Calculate position x and y coordinates to center the window
    x = (screenWidth/2) - (500/2)
    y = (screenHeight/2) - (500/2)
    about.geometry('%dx%d+%d+%d' % (500, 270, x, y))
    about.title('About this program')
    about.resizable(width=False, height=False) # Set the resizable window property to false

    # Create title
    titleLabel = tk.Label(about, text='ABOUT THIS SYSTEM', font=('times', 18, 'bold'))
    titleLabel.pack(pady=(20), side=TOP)

    # Create content labels
    aboutLabel = tk.Text(about, font=('times', 14), height=20, padx=20, pady=10)
    aboutLabel.pack(padx=30, pady=(0, 15), side=TOP)

    # Insert contents
    # Need to separate different lines to differenciate bold and normal text
    aboutLabel.tag_configure("bold", font=('times', 14, 'bold'))
    aboutLabel.insert("end", 'Programmer name: ', "bold")
    aboutLabel.insert("end", 'Cheng Yong Tat')
    aboutLabel.insert("end", '\n\nProgram name: ', "bold")
    aboutLabel.insert("end", 'Coin Summing System')
    aboutLabel.insert("end", '\n\nProgram Description: ', "bold")
    aboutLabel.insert("end", 'This program will calculate ')
    aboutLabel.insert("end", '\nthe amount and total sum of coins based on the ')
    aboutLabel.insert("end", '\nuploaded coin image.')
    aboutLabel.config(state=DISABLED)

class CoinSummingSystem(tk.Tk):
    def __init__(app, *args, **kwargs):
        tk.Tk.__init__(app, *args, **kwargs)
        
        # Get screen width
        screenWidth = app.winfo_screenwidth()
        
        # Calculate position x and y coordinates to center the window
        x = (screenWidth/2) - (850/2)
        y = 30
        app.geometry('%dx%d+%d+%d' % (850, 700, x, y))
        app.title('Coin Summing System')
        app.resizable(width=False, height=False) # set the resizable window property to false

        app.configure(bg='#fafdf3')
        container = tk.Frame(app)
        container.pack()

        # The container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others

        app.frames = {}
        for F in (StartPage, OldCoin, NewCoin):
            page_name = F.__name__
            frame = F(parent=container, controller=app)
            app.frames[page_name] = frame

            # Put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        app.show_frame("StartPage")

    def show_frame(app, page_name):
        # Show a frame for the given page name
        frame = app.frames[page_name]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(app, parent, controller):
        tk.Frame.__init__(app, parent)
        app.controller = controller
        app.configure(bg='#fafdf3')

        frame1 = Frame(app, bg='#fafdf3', width=300, height=300)
        frame1.pack(side=TOP)

        # Create a label to display the image
        img1 = ImageTk.PhotoImage(Image.open('cover.png'))
        imgLabel = Label(frame1, image=img1)
        imgLabel.pack(pady=(30, 20), side=TOP)
        imgLabel.configure(image=img1, bg='#fafdf3')
        imgLabel.image=img1

        # Create title for coin summing system
        titleLabel = tk.Label(app, text='COIN SUMMING SYSTEM', bg='#fafdf3', font=('times', 24, 'bold'), width=30)
        titleLabel.pack(pady=(0, 30), side=TOP)

        oldCoinButton = tk.Button(app, text="OLD COINS", font=('times', 12), width=25, height=2, relief="groove",
                                command=lambda: controller.show_frame("OldCoin"))
        newCoinButton = tk.Button(app, text="NEW COINS", font=('times', 12), width=25, height=2, relief="groove",
                                command=lambda: controller.show_frame("NewCoin"))
        aboutButton = tk.Button(app, text="ABOUT", font=('times', 12), width=25, height=2, relief="groove",
                                command=openAbout)
        exitButton = tk.Button(app, text="EXIT", font=('times', 12), width=25, height=2, relief="groove",
                                command=app.quit)

        oldCoinButton.pack(pady=10)
        newCoinButton.pack(pady=(0, 10))
        aboutButton.pack(pady=(0, 10))
        exitButton.pack()


class OldCoin(tk.Frame):
    def __init__(app, parent, controller):
        tk.Frame.__init__(app, parent)
        app.controller = controller
        app.configure(bg='#fafdf3')

        # Create title for old coin system
        titleLabel = tk.Label(app, text='OLD MALAYSIAN COINS', bg='#fafdf3', font=('times', 22, 'bold'), width=30)
        titleLabel.pack(padx=20, pady=20, side=TOP)

        # Create frames for image and display output
        frame1 = Frame(app, highlightbackground="black", bg='#fafdf3', highlightthickness=2, width=300, height=300)
        frame1.pack(side=TOP)
        frame2 = Frame(app, highlightbackground="grey", bg='#f5f5f5', highlightthickness=1)
        frame2.pack(pady=(0, 25), side=BOTTOM)
        frame3 = Frame(frame2, bg='#f5f5f5')
        frame3.pack(pady=(10, 15), side=TOP)
        frame4 = Frame(frame2, bg='#f5f5f5')
        frame4.pack(pady=(0, 15), side=BOTTOM)

        # Create a label to display the image
        img1 = ImageTk.PhotoImage(Image.open('logo.png'))
        imgLabel = Label(frame1, image=img1)
        imgLabel.pack()
        imgLabel.configure(image=img1, bg="white")
        imgLabel.image=img1
        
        # Create labels to display amount of coins
        # 50 cents
        cents50Label = tk.Label(frame3, text='50 Cents:', font=('times', 14, 'bold'), bg='#f5f5f5')
        cents50Label.pack(padx=(20, 5), side=LEFT)
        cents50TextLabel = tk.Label(frame3, text="0", font=('times', 18, 'bold'), bg="white", width=6, height=2, relief="groove")
        cents50TextLabel.pack(side=LEFT)
        # 20 cents
        cents20Label = tk.Label(frame3, text='20 Cents:', font=('times', 14, 'bold'), bg='#f5f5f5')
        cents20Label.pack(padx=(25, 5), side=LEFT)
        cents20TextLabel = tk.Label(frame3, text="0", font=('times', 18, 'bold'), bg="white", width=6, height=2, relief="groove")
        cents20TextLabel.pack(side=LEFT)
        # 10 cents
        cents10Label = tk.Label(frame3, text='10 Cents:', font=('times', 14, 'bold'), bg='#f5f5f5')
        cents10Label.pack(padx=(25, 5), side=LEFT)
        cents10TextLabel = tk.Label(frame3, text="0", font=('times', 18, 'bold'), bg="white", width=6, height=2, relief="groove")
        cents10TextLabel.pack(side=LEFT)
        # 5 cents
        cents5Label = tk.Label(frame3, text='5 Cents:', font=('times', 14, 'bold'), bg='#f5f5f5')
        cents5Label.pack(padx=(25, 5), side=LEFT)
        cents5TextLabel = tk.Label(frame3, text="0", font=('times', 18, 'bold'), bg="white", width=6, height=2, relief="groove")
        cents5TextLabel.pack(padx=(0, 20), side=LEFT)

        # Create labels to display total coin value
        totalCoinValueTextLabel = tk.Label(frame4, text="RM 0", font=('times', 22, 'bold'), bg="white", width=15, height=2, relief="groove")
        totalCoinValueTextLabel.pack(side=BOTTOM)
        totalCoinValueLabel = tk.Label(frame4, text='Total:', font=('times', 14, 'bold'), bg='#f5f5f5')
        totalCoinValueLabel.pack(side=BOTTOM)

        def upload_image():

            width = 1000
            height = 500
            dim1 = (width, height)
            dim2 = (300, 300)
            dim3 = (3024, 3024)
            sum = 0
            num = 0
            cents_50 = 0
            cents_20 = 0
            cents_10 = 0
            cents_5 = 0

            masterFilepath = ('old_coin_0.jpg')

            # Declare required file types when user press 'Upload Image Button'
            f_types = [('Jpg files', '*.jpg'), ('PNG files', '*.png')]
            fileName = tk.filedialog.askopenfile(mode='r', filetypes=f_types)
            filepath = os.path.abspath(fileName.name) #Copy the file path

            # Upload the image via file path and filter it for image processing purpose
            masterImg = cv2.imread(masterFilepath)
            uploadImg = cv2.imread(filepath)
            uploadImg = cv2.resize(uploadImg, dim3, interpolation = cv2.INTER_AREA)
            vis = np.concatenate((masterImg, uploadImg), axis=1)
            resizeImg1 = cv2.resize(vis, dim1, interpolation = cv2.INTER_AREA)
            resizeImg2 = cv2.resize(uploadImg, dim2, interpolation = cv2.INTER_AREA)

            # Convert image to grayscale
            gray1 = cv2.cvtColor(resizeImg1, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(resizeImg2, cv2.COLOR_BGR2GRAY)
            grayBlur1 = cv2.GaussianBlur(gray1, (15, 15), 0)
            grayBlur2 = cv2.GaussianBlur(gray2, (15, 15), 0)

            # Determine all circles in the image
            # Accumulator resolution, min dis of detected circles, first method-specific parameter, second method-specific parameter
            circles1 = cv2.HoughCircles(grayBlur1, cv2.HOUGH_GRADIENT, 1, 40, param1=42, param2=35, minRadius=0, maxRadius=0)
            circles2 = cv2.HoughCircles(grayBlur2, cv2.HOUGH_GRADIENT, 1, 40, param1=42, param2=35, minRadius=0, maxRadius=0)
            circles1 = np.uint16(np.around(circles1))
            circles2 = np.uint16(np.around(circles2))
            
            # Identify the largest radius in the image
            largestRadius = 0
            for i in circles1[0,:]:
                if largestRadius < i[2]:
                    largestRadius = i[2]

            # Assign value to the recognized circles based on their sizes
            for i in circles1[0,:]:
                cv2.circle(resizeImg1, (i[0], i[1]), i[2], (0,255,0), 2)
                cv2.circle(resizeImg1, (i[0], i[1]), 2, (0,0,255), 3)
                radius = i[2]
                ratio = ((radius*radius) / (largestRadius*largestRadius))
                if(ratio >= 0.85):
                    sum = sum + 0.5
                    cents_50 = cents_50 + 1
                elif((ratio >= 0.60) and (ratio < 0.85)):
                    sum = sum + 0.2
                    cents_20 = cents_20 + 1
                elif((ratio >= 0.40) and (ratio < 0.60)):
                    sum = sum + 0.1
                    cents_10 = cents_10 + 1
                elif(ratio < 0.40):
                    sum = sum + 0.05
                    cents_5 = cents_5 + 1
                num = num + 1

            # Calculate the correct total coin value
            finalNum = num - 4
            finalCents_50 = cents_50 - 1
            finalCents_20 = cents_20 - 1
            finalCents_10 = cents_10 - 1
            finalCents_5 = cents_5 - 1
            finalSum = sum - 0.85

            # Display amount of coins in label
            cents50TextLabel.config(text = finalCents_50)
            cents20TextLabel.config(text = finalCents_20)
            cents10TextLabel.config(text = finalCents_10)
            cents5TextLabel.config(text = finalCents_5)
            totalCoinValueTextLabel.config(text = "RM " + str("%.2f" % round(finalSum, 2)))

            # For data validate purpose
            print("Total coins: ", finalNum)
            print("50 Cents = ", finalCents_50)
            print("20 Cents = ", finalCents_20)
            print("10 Cents = ", finalCents_10)
            print("5 Cents = ", finalCents_5)
            print("Total sum: RM ", finalSum)

            # Convert the greyscaled image back to RGB colored
            # Assign the coin image to tkinter label and display it
            outputImg = cv2.cvtColor(resizeImg2, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(outputImg)
            img2 = ImageTk.PhotoImage(img)

            imgLabel.configure(image=img2)
            imgLabel.image=img2

            '''font = cv2.FONT_HERSHEY_DUPLEX
            text = "Total value: RM " + str("%.2f" % round(finalSum, 2))

            cv2.putText(resizeImg1, text, (20, 50), font, 0.6, (255, 0, 255), 1, cv2.LINE_AA)
            cv2.imshow('Detected coins', resizeImg1)
            cv2.waitKey()'''

        # Create upload button
        uploadButton = tk.Button(app, text='Upload image', font=('times', 14), relief="groove", width=20, 
                                    command = upload_image)
        uploadButton.pack(pady=20, side=TOP)

        # Create home button
        homeButton = tk.Button(app, text="Home",  relief="groove", width=10,
                                    command=lambda: controller.show_frame("StartPage"))
        homeButton.pack(side=LEFT)

class NewCoin(tk.Frame):
    def __init__(app, parent, controller):
        tk.Frame.__init__(app, parent)
        app.controller = controller
        app.configure(bg='#fafdf3')

        # Create title for old coin system
        titleLabel = tk.Label(app, text='NEW MALAYSIAN COINS', bg='#fafdf3', font=('times', 22, 'bold'), width=30)
        titleLabel.pack(padx=20, pady=20, side=TOP)

        # Create frames for image and display output
        frame1 = Frame(app, highlightbackground="black", highlightthickness=2, bg='#fafdf3', width=300, height=300)
        frame1.pack(side=TOP)
        frame2 = Frame(app, highlightbackground="grey", highlightthickness=1, bg='#f5f5f5')
        frame2.pack(pady=(0, 25), side=BOTTOM)
        frame3 = Frame(frame2, bg='#f5f5f5')
        frame3.pack(pady=(10, 15), side=TOP)
        frame4 = Frame(frame2, bg='#f5f5f5')
        frame4.pack(pady=(0, 15), side=BOTTOM)

        # Create a label to display the image
        img1 = ImageTk.PhotoImage(Image.open('logo.png'))
        imgLabel = Label(frame1, image=img1)
        imgLabel.pack()
        imgLabel.configure(image=img1, bg='white')
        imgLabel.image=img1
        
        # Create labels to display amount of coins
        # 50 cents
        cents50Label = tk.Label(frame3, text='50 Cents:', font=('times', 14, 'bold'), bg='#f5f5f5')
        cents50Label.pack(padx=(20, 5), side=LEFT)
        cents50TextLabel = tk.Label(frame3, text="0", font=('times', 18, 'bold'), bg="white", width=6, height=2, relief="groove")
        cents50TextLabel.pack(side=LEFT)
        # 20 cents
        cents20Label = tk.Label(frame3, text='20 Cents:', font=('times', 14, 'bold'), bg='#f5f5f5')
        cents20Label.pack(padx=(25, 5), side=LEFT)
        cents20TextLabel = tk.Label(frame3, text="0", font=('times', 18, 'bold'), bg="white", width=6, height=2, relief="groove")
        cents20TextLabel.pack(side=LEFT)
        # 10 cents
        cents10Label = tk.Label(frame3, text='10 Cents:', font=('times', 14, 'bold'), bg='#f5f5f5')
        cents10Label.pack(padx=(25, 5), side=LEFT)
        cents10TextLabel = tk.Label(frame3, text="0", font=('times', 18, 'bold'), bg="white", width=6, height=2, relief="groove")
        cents10TextLabel.pack(side=LEFT)
        # 5 cents
        cents5Label = tk.Label(frame3, text='5 Cents:', font=('times', 14, 'bold'), bg='#f5f5f5')
        cents5Label.pack(padx=(25, 5), side=LEFT)
        cents5TextLabel = tk.Label(frame3, text="0", font=('times', 18, 'bold'), bg="white", width=6, height=2, relief="groove")
        cents5TextLabel.pack(padx=(0, 20), side=LEFT)

        # Create labels to display total coin value
        totalCoinValueTextLabel = tk.Label(frame4, text="RM 0", font=('times', 22, 'bold'), bg="white", width=15, height=2, relief="groove")
        totalCoinValueTextLabel.pack(side=BOTTOM)
        totalCoinValueLabel = tk.Label(frame4, text='Total:', font=('times', 14, 'bold'), bg='#f5f5f5')
        totalCoinValueLabel.pack(side=BOTTOM)

        def upload_image():

            width = 1000
            height = 500
            dim1 = (width, height)
            dim2 = (300, 300)
            dim3 = (3024, 3024)
            sum = 0
            num = 0
            cents_50 = 0
            cents_20 = 0
            cents_10 = 0
            cents_5 = 0

            masterFilepath = ('new_coin_0.jpg')

            # Declare required file types when user press 'Upload Image Button'
            f_types = [('Jpg files', '*.jpg'), ('PNG files', '*.png')]
            fileName = tk.filedialog.askopenfile(mode='r', filetypes=f_types)
            filepath = os.path.abspath(fileName.name) #Copy the file path

            # Upload the image via file path and filter it for image processing purpose
            masterImg = cv2.imread(masterFilepath)
            uploadImg = cv2.imread(filepath)
            uploadImg = cv2.resize(uploadImg, dim3, interpolation = cv2.INTER_AREA)
            vis = np.concatenate((masterImg, uploadImg), axis=1)
            resizeImg1 = cv2.resize(vis, dim1, interpolation = cv2.INTER_AREA)
            resizeImg2 = cv2.resize(uploadImg, dim2, interpolation = cv2.INTER_AREA)

            # Convert image to grayscale
            gray1 = cv2.cvtColor(resizeImg1, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(resizeImg2, cv2.COLOR_BGR2GRAY)
            grayBlur1 = cv2.GaussianBlur(gray1, (15, 15), 0)
            grayBlur2 = cv2.GaussianBlur(gray2, (15, 15), 0)

            # Determine all circles in the image
            # Accumulator resolution, min dis of detected circles, first method-specific parameter, second method-specific parameter
            circles1 = cv2.HoughCircles(grayBlur1, cv2.HOUGH_GRADIENT, 1, 30, param1=50, param2=30, minRadius=0, maxRadius=0)
            circles2 = cv2.HoughCircles(grayBlur2, cv2.HOUGH_GRADIENT, 1, 30, param1=50, param2=30, minRadius=0, maxRadius=0)
            circles1 = np.uint16(np.around(circles1))
            circles2 = np.uint16(np.around(circles2))

            # Identify the largest radius in the image
            largestRadius = 0
            for i in circles1[0,:]:
                if largestRadius < i[2]:
                    largestRadius = i[2]

            print("largestRadius: ", largestRadius)

            #Assign value to the recognized circles based on their sizes
            for i in circles1[0,:]:
                cv2.circle(resizeImg1, (i[0], i[1]), i[2], (0,255,0), 2)
                cv2.circle(resizeImg1, (i[0], i[1]), 2, (0,0,255), 3)
                radius = i[2]
                print("radius: ", radius)
                ratio = ((radius*radius) / (largestRadius*largestRadius))
                if(ratio >= 0.90):
                    sum = sum + 0.5
                    cents_50 = cents_50 + 1
                elif((ratio >= 0.75) and (ratio < 0.90)):
                    sum = sum + 0.2
                    cents_20 = cents_20 + 1
                elif((ratio >= 0.65) and (ratio < 0.75)):
                    sum = sum + 0.1
                    cents_10 = cents_10 + 1
                elif(ratio < 0.65):
                    sum = sum + 0.05
                    cents_5 = cents_5 + 1
                num = num + 1

            # Calculate the correct total coin value
            finalNum = num - 4
            finalCents_50 = cents_50 - 1
            finalCents_20 = cents_20 - 1
            finalCents_10 = cents_10 - 1
            finalCents_5 = cents_5 - 1
            finalSum = sum - 0.85

            # Display amount of coins in label
            cents50TextLabel.config(text = finalCents_50)
            cents20TextLabel.config(text = finalCents_20)
            cents10TextLabel.config(text = finalCents_10)
            cents5TextLabel.config(text = finalCents_5)
            totalCoinValueTextLabel.config(text = "RM " + str("%.2f" % round(finalSum, 2)))

            # For data validate purpose
            print("Total coins: ", finalNum)
            print("50 Cents = ", finalCents_50)
            print("20 Cents = ", finalCents_20)
            print("10 Cents = ", finalCents_10)
            print("5 Cents = ", finalCents_5)
            print("Total sum: RM ", finalSum)

            # Convert the greyscaled image back to RGB colored
            # Assign the coin image to tkinter label and display it
            outputImg = cv2.cvtColor(resizeImg2, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(outputImg)
            img2 = ImageTk.PhotoImage(img)

            imgLabel.configure(image=img2)
            imgLabel.image=img2

            '''font = cv2.FONT_HERSHEY_DUPLEX
            text = "Total value: RM " + str("%.2f" % round(finalSum, 2))

            cv2.putText(resizeImg1, text, (20, 50), font, 0.6, (255, 0, 255), 1, cv2.LINE_AA)
            cv2.imshow('Detected coins', resizeImg1)
            cv2.waitKey()'''

        # Create upload button
        uploadButton = tk.Button(app, text='Upload image', font=('times', 14), relief="groove", width=20, 
                                    command = upload_image)
        uploadButton.pack(pady=20, side=TOP)

        # Create home button
        homeButton = tk.Button(app, text="Home",  relief="groove", width=10,
                                    command=lambda: controller.show_frame("StartPage"))
        homeButton.pack(side=LEFT)

    


if __name__ == "__main__":
    app = CoinSummingSystem()
    app.mainloop()