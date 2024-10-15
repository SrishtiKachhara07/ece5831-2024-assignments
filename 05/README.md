# Rock-Paper-Scissors Classification Using Teachable Machine

This project implements a Rock-Paper-Scissors classification system using a neural network model trained with Teachable Machine. The system can classify images in both static and live camera feed settings.

## Table of Contents
- [Project Overview](#project-overview)
- [Files](#files)
- [Conclusion](#conclusion)
- [YouTube Channel](#youtube-channel)

## Project Overview

The goal of this project is to classify images of rock, paper, and scissors using a deep learning model. The model was trained using Google’s Teachable Machine, allowing for custom image datasets. The project consists of two main scripts:

- `rock-paper-scissors.py`: Classifies static images passed as command-line arguments.
- `rock-paper-scissors-live.py`: Uses a webcam to classify live video feed.

### Note
- For real-time prediction, run `rock-paper-scissors-live.py`.
- For static image classification, run `rock-paper-scissors.py`.
- For understanding the implementation in detail, please refer to the `teachable.ipynb` file.

## Files

- `README.md`: This documentation file.
- `rock-paper-scissors.py`: Script for classifying static images.
- `rock-paper-scissors-live.py`: Script for classifying live webcam feed.
- `teachable.ipynb`: Jupyter Notebook demonstrating the model implementation and testing.
- `labels.txt`: Contains the names of the classes used in the model.
- `sample/`: Directory containing sample images organized in subfolders (`rock`, `paper`, `scissors`).

## Conclusion

This project demonstrates the capabilities of using a pre-trained neural network model for real-time gesture classification. It provides a functional application for classifying rock, paper, and scissors gestures with high accuracy.

## YouTube Channel

For a demonstration of the live classification in action, please visit my YouTube channel: [https://youtube.com/@srishtikachhara?si=N1iPAzLU3Rel6LLY](<YOUR_YOUTUBE_LINK>).
