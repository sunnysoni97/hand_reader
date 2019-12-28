
---

#### This is the reader's manual for using and editing this software project as you may like!

---  

<br/>

# About the Project  

This software recognises the numerical digit (0-9) from the image containing any digit (currently limited to 1 digit per file). This is accomplished with the help of preprocessing of each image done using OpenCV library in accordance with the MNIST database recommendations.

The artificial neural network is trained from the MNIST training data set available at its official website.

End user can browse any file (image) containing the handwritten digit, or he can capture a new image from the attached camera device.

---
## Prerequisites before using this software :

1. Make sure you have **Python 3.x** setup on your operating system.  
   
2. Install the follow libraries to meet the dependencies :  
    (i) **Tensorflow**  
    (ii) **OpenCV**  
	(iii) **kivy** *(and its supporting gstreamer libraries)*  
    (iv) The supporting libraries like numpy,pil and all others *(which are automatically installed while installing the above mentioned libraries)*  

3. You need a working camera for the image capture option to work.

---

## Compiling and Running :

Execute `main.py` using the terminal of your choice.

_Example Syntax_ : `python3 main.py`

---

### Important Usage Instructions : 

To capture a new image, press C to pause the captured video stream, then press C to capture the image or any other key to abort the capture operation.

---

## Screenshots

<img src="https://github.com/sunnysoni97/sunnysoni97.github.io/blob/master/static/skills_applied/portfolio_screencaps/hand_reader_screencaps/cap1.png?raw=true" alt="hand reader screenshot 1" width=300px />
&emsp;

<img src="https://github.com/sunnysoni97/sunnysoni97.github.io/blob/master/static/skills_applied/portfolio_screencaps/hand_reader_screencaps/cap2.png?raw=true" alt="hand reader screenshot 2" width=300px />

<br/>

<img src="https://github.com/sunnysoni97/sunnysoni97.github.io/blob/master/static/skills_applied/portfolio_screencaps/hand_reader_screencaps/cap3.png?raw=true" alt="hand reader screenshot 3" width=300px />
&emsp;
<img src="https://github.com/sunnysoni97/sunnysoni97.github.io/blob/master/static/skills_applied/portfolio_screencaps/hand_reader_screencaps/cap4.png?raw=true" alt="hand reader screenshot 4" width=300px />

---

## Note for the Developers : 

- `image_processor.py` contains all the preprocessing operations.

- `model_trainer.py` contains the neural network training functions.

- `digit_recog.py` contains the backend function to calculate the answer from the estimated input image.

- `main.py` contains all the gui operations and the front end of the software. This is the entry point of the software.

- `digit_recogniser.kv` is the kivy builder file for the front-end.

- `input_data.py` is the mnist database importer library given by official Tensorflow website.

---

Feel free to try out my project, make your own implementations, suggest changes and modification and help in improving my project. :)

---

**P.S.** : *Hail the internet for all the awesome resources and information present on anything you want to learn. My whole hearted gratitude to everybody who made it possible for me to complete this project of mine.* :)

---
