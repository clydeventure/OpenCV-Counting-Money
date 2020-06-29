[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

<br />
<p align="center">
    <img src="https://github.com/clydeventure/OpenCV-Counting-Money/blob/master/img/computervision.jpg?raw=true" width="100%" >
  </a>

  <h3 align="center">Counting Coins</h3>



---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About the Project](#about-the-project)
- [How it Works](#how-it-works)
- [What I Learned](#what-i-learned)

---
## About the Project

As the capstone project for my Python Bootcamp Udemy course, we were required to make a program that would identify British pounds and return the amount. In order to do this, we were introduced to the OpenCV library.

---

## How it Works

This program uses OpenCV to process the image.

1. The image is converted to grayscale and a Gaussian blur is added for easier processing.

2. The circles in the image were identified using the Hough circles method (specification was pulled from the OpenCV documentation).
   
3. An outer perimeter was drawn along the rim and a circle was drawn in the center of each coin.
   
4. The coin count number was also added to each coin.
   
5. The radius and brightness of each coin is then retrieved.
   
6. The coins' brightness and radius is compared, and the coins are categorized accordingly.
   
7. The total value of the coins is displayed in the upper left-hand corner of the image.

---

## What I Learned

This project really pushed me to work outside of my comfort zone. My bootcamp course did not teach NumPy or OpenCV intentionally so that we, the students, would have to find solutions through reading the documentation. We were provided hints as to what we should be doing, but the rest was up to us.

At the moment, I am trying to make myself hirable as soon as possible. Therefore, I am focusing more on Django and app development with Python. Due to time constraints, I made this program per instruction. When time is abundant, I would love to come back and rewrite the program to identify coins based off of ratio, and to count paper money as well.

[Back To The Top](#table-of-contents)
