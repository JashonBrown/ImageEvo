from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image, ImageDraw
import random
import numpy as np

    
class GAImageRecreator:

    ORIGINAL_IMAGE = 'A:/AI Projects/ImageEvo/mona-lisa.jpg'
    NEW_IMAGE = 'A:/AI Projects/ImageEvo/newCandidate.png'
    BEST_IMAGE = 'A:/AI Projects/ImageEvo/bestCandidate.png'
    IMAGE_WIDTH = 0
    IMAGE_HEIGHT = 0

    def __init__(self, master):
        self.frame = Frame(master)
        self.frame.pack()

        self.imageButton = Button(self.frame, text="Choose Image", command=self.chooseImage)
        self.imageButton.pack(side=TOP)

        self.generationButton = Button(self.frame, text="Generate", command=self.generateImage)
        self.generationButton.pack(side=TOP)

        self.GOFButton = Button(self.frame, text="GOF", command=self.calculateGOF)
        self.GOFButton.pack(side=TOP)

        #original image
        oimg = ImageTk.PhotoImage(Image.open(self.ORIGINAL_IMAGE))
        self.originalImage = Label(self.frame, image=oimg)
        self.originalImage.image = oimg

        #Best candidate image
        bimg = ImageTk.PhotoImage(Image.open(self.BEST_IMAGE))
        self.bestImage = Label(self.frame, image=bimg)
        self.bestImage.image = bimg

        #new candidate image
        nimg = ImageTk.PhotoImage(Image.open(self.NEW_IMAGE))
        self.newImage = Label(self.frame, image=nimg)
        self.newImage.image = nimg

        self.chooseImage()
        
        
    def chooseImage(self):
        filename = askopenfilename()
        self.ORIGINAL_IMAGE = filename;
        
        im = Image.open(self.ORIGINAL_IMAGE)
        self.IMAGE_WIDTH, self.IMAGE_HEIGHT = im.size
        im = Image.new('RGBA', (self.IMAGE_WIDTH, self.IMAGE_HEIGHT))
        im.save('newCandidate.png')
        im.save('bestCandidate.png')

        

        self.refreshImages()

        
    def generateImage(self):
        for i in range(0,1):
            num_points = random.randint(2, 8)
            p_list = []
            for x in range(0,num_points):
                p_list.append(random.randint(0,self.IMAGE_WIDTH))
                p_list.append(random.randint(0,self.IMAGE_HEIGHT))
            
            points = (random.randint(0,self.IMAGE_WIDTH),20), (20, 100), (100,20)
            im = Image.open(self.BEST_IMAGE)
            draw = ImageDraw.Draw(im)

            draw.polygon(p_list, fill=(random.randint(0,255), random.randint(0,255), random.randint(0,255), 10))
            im.save('newCandidate.png')

            self.calculateGOF()
        
            self.refreshImages()

        

    def refreshImages(self):
        #Refresh original image
        oimg = ImageTk.PhotoImage(Image.open(self.ORIGINAL_IMAGE))
        self.originalImage.configure(image = oimg)
        self.originalImage.image = oimg
        self.originalImage.pack(side=LEFT)

        #Refresh best image
        bimg = ImageTk.PhotoImage(Image.open(self.BEST_IMAGE))
        self.bestImage.configure(image = bimg)
        self.bestImage.image = bimg
        self.bestImage.pack(side=LEFT)
        
        #Refresh new image
        nimg = ImageTk.PhotoImage(Image.open(self.NEW_IMAGE))
        self.newImage.configure(image = nimg)
        self.newImage.image = nimg
        self.newImage.pack(side=RIGHT)



    def getGOF(self, nim):
        GOF = 0 
        oim = Image.open(self.ORIGINAL_IMAGE)
        
        for i in range(0,self.IMAGE_WIDTH):
            for j in range(0,self.IMAGE_HEIGHT):
                #ro, go, bo = oim.getpixel((i, j))
                #rn, gn, bn = nim.getpixel((i, j))
                #GOF += abs(ro-rn)
                #GOF += abs(go-gn)
                #GOF += abs(bo-bn)
                GOF = 0
        return GOF


    def calculateGOF(self):
        bgof = self.getGOF(Image.open(self.BEST_IMAGE))
        ngof = self.getGOF(Image.open(self.NEW_IMAGE))
        print("Best: " + str(bgof) + " | New: " + str(ngof))

        if(ngof < bgof):
            im = Image.open(self.NEW_IMAGE)
            im.save('bestCandidate.png')
            
        #TODO: If GOF of new is better than old, save new bestCandidate

        
root = Tk()

im = Image.open('A:/AI Projects/ImageEvo/bestCandidate.png')
photo = ImageTk.PhotoImage(im)

label = Label(root, image=photo)
label.image = photo  # keep a reference!
label.pack()
        
root.title("Image Evoloution")
b = GAImageRecreator(root)
root.mainloop()
