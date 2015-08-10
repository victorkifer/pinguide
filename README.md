# Content-based Image Recommendations for Online Social Networks 
## [X AACIMP Summer School 2015](http://summerschool.ssa.org.ua/) project

### Abstract

In this project we look at the problem of modeling and predicting user preferences in image content from a perspective of the fastest growing and the third biggest social network - [Pinterest](https://www.pinterest.com/). Pinterest is an image bookmarking and sharing social network where users curate web images by pinning them into their personal pinboards. To facilitate Pinterest users in their search for interesting image content we propose a recommendation system which learns to recognize users' preferences and predict which other images a user might be interested in. We describe the content of images and users' preferences with over 6K features extracted with the state-of-the-art deep convolutional neural network and formalize the recommendation problem as a supervised learning task where for a user U and an image I we train a binary classifier to predict whether U will pin I or not.

This project is inspired by the results described in [this article](http://www.inf.kcl.ac.uk/staff/nrs/pubs/www15-predicting-pinterest.pdf)
and is based on the publicly available [dataset](http://www.inf.kcl.ac.uk/staff/nrs/projects/cd-gain/dataset.html).

### Getting started

```
git clone %URL% aacimp
cd aacimp
git checkout dev
cp config.py-template config.py
// edit config.py with your favorite editor
// for example, nano
nano config.py
```

```
ipython notebook
```