import kivy
import cv2
kivy.require('1.10.1')


from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup


import os

import digit_recog as dr

class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)


class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    im = ObjectProperty(None)
    im2 = ObjectProperty(None)
    lbl = ObjectProperty(None)
    content = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        
        self.content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", title_align="center", content=self.content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        
        answer = dr.calculate_image(os.path.join(path, filename[0]))
        self.im.source = os.path.join(path, filename[0])
        self.im2.source = 'output.jpg'
        self.im.reload()
        self.im2.reload()
        self.im.opacity = 1
        self.im2.opacity = 1
        self.lbl.text = str("Digit : "+str(answer))
        self.dismiss_popup()

    def show_camera(self):
        cap = cv2.VideoCapture(0)
        while(True):
            ret, frame = cap.read()
            cv2.imshow('Capture Image',frame)
            if(cv2.waitKey(1)& 0xFF == ord('c')):
                if(cv2.waitKey(0)& 0xFF == ord('c')):
                    cv2.imwrite('input.jpg',frame)
                    cap.release()
                    cv2.destroyAllWindows()
                    self.calculate()
                    return
                else:
                    cap.release()
                    cv2.destroyAllWindows()
                    return
    def calculate(self):
        answer = dr.calculate_image("input.jpg")
        self.im.source = "input.jpg"
        self.im2.source = 'output.jpg'
        self.im.reload()
        self.im2.reload()
        self.im.opacity = 1
        self.im2.opacity = 1
        self.lbl.text = str("Digit : "+str(answer))



class Digit_Recogniser(App):
    pass

Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)

if __name__ == '__main__':
    Digit_Recogniser().run()