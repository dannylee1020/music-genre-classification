# Music Genre Classification with Audio Tracks

## Project Overview
Can computer listen to a piece of music and classify its genre? As the technology rapidly increases along with the size of music industry, huge amount of data is now availble for companies to use to create products for their consumers. Audio files have been the main source of data to extract numerous features to make the process easier. However, the best way to handle these for different tasks is not defined. Machine learning techniques are widely used in the industry to optimize the best practices of performing these tasks to ulitmately deliver and improve personalized experience to the users. 

## Model Overview
In this project, two different approaches were considered to compare how well it classifies a music genre based on audio track given. The first approach is image classification using 2D CNN on spectrograms. Using Librosa library, convert .wav files to respective mel-spectrogram and use them to train 2D CNN model. The second approach is sequence modeling on MFCCs using 1D CNN - LSTM model structure. Convert .wav files into sequence of MFCC and use to train CNN-LSTM model.
<br>
<br>
Both models were trained for 100 epochs with learning rate of 0.00025. The summary of the model architecture is below. For detail, please see [here](https://colab.research.google.com/drive/1uJ17DcjCrDZlqStpYh5jQ-gbNhcG8FmL?usp=sharing)

### 2D CNN
The model has three 2D convolutional layers with 32 nodes followed by two fully connected layers with 32 and 16 nodes and a output layer with 10 nodes and softmax activation. Dropout and Batch Normalization layers were used throughout the model to prevent overfitting. 
<br>
<img src='https://github.com/dannylee1020/music-genre-classification/blob/master/image/2d_accuracy.png' width=400 height=300>
<img src='https://github.com/dannylee1020/music-genre-classification/blob/master/image/2d_loss.png' width=400 height=300>

### 1D CNN - LSTM
The model has three 1D convolutional layers with 32 nodes followed by two LSTM layers with 128 nodes, then followed by  one fully connected layer of 50 nodes and an output layer of 10 nodes and softmax activation. Dropout and Batch Normalization layers were used throughout the model to prevent overfitting. 
<br>
<img src='https://github.com/dannylee1020/music-genre-classification/blob/master/image/1d_accuracy.png' width=400 height=300>
<img src='https://github.com/dannylee1020/music-genre-classification/blob/master/image/1d_loss.png' width=400 height=300>

## Results
Both models had similar performance, with 1D CNN - LSTM model slightly outperforming 2D CNN. More rigorous hyperparameter tuning with different model structure and more training epochs may increase the overall accuracy of these models

| Model | Loss | Accuracy |
| --- | --- | -----|
| 2D CNN | 1.34 | 55% |
| 1D CNN - LSTM | 1.12 | 59% |


## Data
Data used for this project is GTZAN dataset. It is consisted of 1000 audio tracks of length 30 seconds, categorized into 10 genres of 100 tracks each. The genres are blues, classical, country, disco, hip hop, jazz, metal, pop, reggae and rock. The dataset can be found on [Kaggle](https://www.kaggle.com/andradaolteanu/gtzan-dataset-music-genre-classification)


## Test
Scripts for simple unit tests for model prediction is written in `test.py`. Run `pytest test.py` for testing both models 


## Reference
[Music Genre Recognition using Deep Neural Networks and Transfer Learning](https://www.isca-speech.org/archive/Interspeech_2018/pdfs/2045.pdf)
<br>
[A comparative analysis of CNN and LSTM for music genre classification](https://www.diva-portal.org/smash/get/diva2:1354738/FULLTEXT01.pdf)
<br>





