# InspireMe-App
*Have you ever felt the need of quote that inspires you keep going forward with your life or simply to make you feel better? <br/>
Here's InspireMe for you!*

# Objective
**InspireMe is a python-based application made using Kivy that provides motivational quotes to the user depending upon their mood by analyzing their written text using Machine Learning Algorithm.**

# Contents
- [Tech Stack](#tech-stack)
- [Features](#features)
- [Application Overview](#application-overview)
- [ML Algorithm](#ml-algorithms)
- [Challenges Faced](#challenges-faced)
- [Future Scope](#future-scope)
- [Learnings](#learnings)
- [Contributers](#contributors)

# Tech Stack
![](https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white)
![](https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
<br/><br/>
**Language-:** *Python* <br/>
**Framework-:** *Kivy*<br/>
Kivy is a free and open source Python framework for developing mobile apps and other multitouch application software with a natural user interface.



# Features
- The app offers the firstly, the basic feature for the user to sign-in and register.
- After successfully logging in, the user is taken to a screen where they can type their feelings(or sentences)
- The ML algorithm analyses the sentiment/emotions of the written text and return one of the emotions - anger, joy, fear, sadness, surprise, love.
- The quotes for each of the emotions is present in the quotes folder. The program randomly chooses a quote and displays to the user.

# Application Overview
- *First/Home Screen of the App* <br/><br/>
<center><img src = "https://github.com/kashika0112/InspireMe-App/blob/main/Images/SS1.png" width="300" height="500"></center>

- *Sign-in/Login Page* <br/><br/>
<center><img src = "https://github.com/kashika0112/InspireMe-App/blob/main/Images/SS2.png" width="300" height="500"></center>

- *Analysing Text and Displaying Quote* <br/><br/>
<center><img src = "https://github.com/kashika0112/InspireMe-App/blob/main/Images/SS3.png" width="300" height="500"></center>


# ML Algorithms
- **Algorithm Used: Naive Bayes Algorithm**
  - It is a classification technique based on Bayes' Theorem with an assumption of independence among predictors. In simple terms, a Naive Bayes classifier assumes that the presence of a particular feature in a class is unrelated to the presence of any other feature.
- **Dataset Used: Emotions Dataset from Kaggle with 16000 sentences**
- **Accuracy Obtained: 80% Accuracy was obtained.**

# Challenges Faced
The following are the challenges I came across whilst making this project
- Lack of resources to study the framework of Kivy which made the app development difficult.
- The ML model obtained only 80% accuracy because of lesser data.


# Future Scope
- This app can be modified into a full *Mental Health* app by including more features. For example, incorporating posting blogs, chatbot and other mental health resources.
- We can improve the accuracy of the model by adding cleaner and larger data. 
- The app can be deployed for both android and ios uers.

# Learnings
I learnt a lot as a developer while making this project. I learned an entirely new framework of Kivy, strengthened my skills in Python, dived a little deeper into data science, mainly NLTK and Classification Algorithms.

# Contributors
The repository has been made and maintained by [Kashika Akhouri](https://github.com/kashika0112)
