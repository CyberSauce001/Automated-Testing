from PIL import Image, ImageDraw
from selenium import webdriver
import os
import sys
import time

pjs = '/path/phantomjs.exe'


class Screenshot():

  #this is hard coded, can use input str() in order to get url
    print('Choose the following:')
    print('1. ')
    print('2. ')
    choice = int(input("Enter choice:"))
    if choice == 1:
        argv = ''
        argv2 = ''
    elif choice == 2:
        argv = ''
        argv2 = ''
    else:
        print('Error!:', choice)

    Test = argv
    Live = argv2


    def __init__(self):
        self.set_up()
        self.capture_screens()
        self.analyze()

    def set_up(self):
       self.driver = webdriver.PhantomJS(pjs)

    def capture_screens(self):
        self.screenshot(self.Test, 'Test.png')
        self.screenshot(self.Live, 'Live.png')

    def screenshot(self, url, file_name):
        print(url)
        self.driver.get(url)
        time.sleep(10)
        self.driver.set_window_size(1024, 800) #height, width
        time.sleep(10)
        self.driver.save_screenshot(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'path/', file_name))
        self.driver.get_screenshot_as_png()
       

    def analyze(self):
        ss_Test = Image.open("path/Test.png")
        ss_Live = Image.open("pathLive.png")
        columns = 100
        rows = 100
        screen_width, screen_height = ss_Test.size

        block_width = ((screen_width - 1) // columns) + 1 
        block_height = ((screen_height - 1) // rows) + 1

        for y in range(0, screen_height, block_height+1):
            for x in range(0, screen_width, block_width+1):
                box_Test = self.process_region(ss_Test, x, y, block_width, block_height)
                box_Live = self.process_region(ss_Live, x, y, block_width, block_height)

                if box_Test is not None and box_Live is not None and box_Live != box_Test:
                    draw = ImageDraw.Draw(ss_Test)
                    draw.rectangle((x, y, x+block_width, y+block_height), outline = "red")

        ss_Test.save(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'path/',"errors.png"))

    def process_region(self, image, x, y, width, height):
        region_total = 0
        factor = 25

        for coordinateY in range(y, y+height):
            for coordinateX in range(x, x+width):
                try:
                    pixel = image.getpixel((coordinateX, coordinateY))
                    region_total += sum(pixel)/4
                except:
                    return

        return region_total/factor


Screenshot()

