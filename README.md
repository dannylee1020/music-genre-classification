# Music Genre Classification with Audio Files

## Project Overview
Can computer listen to a piece of music and classify its genre? As the technology rapidly increases as with the size of music industry, huge amount of data is now availble for companies to use to create products for their consumers. Audio files have been the main source of data to extract numerous features to make the process easier. However, the best way to handle these for different tasks is not defined. Machine learning techniques are widely used in the industry to optimize the best practices of performing these tasks to ulitmately deliver and improve personalized experience to the users. 

## Model Overview
In this project, the two different approaches will be considered to compare how well it classifies a music genre based on audio data given. The first approach is image classification using 2D CNN on spectrograms. Convert .wav files to respective mel-spectrogram and use them to train 2D CNN model. The second approach is sequence modeling on MFCCs using 1D CNN - LSTM model structure. Convert .wav files into sequence of MFCC and use to train CNN-LSTM model. 

## Data
Data used for this project is GTZAN dataset. It is consisted of 1000 audio tracks of length 30 seconds, categorized into 10 genres of 100 tracks each. The genres are blues, classical, country, disco, hip hop, jazz, metal, pop, reggae and rock. The dataset can be found on [Kaggle](https://www.kaggle.com/andradaolteanu/gtzan-dataset-music-genre-classification)


## Reference
[Music Genre Recognition using Deep Neural Networks and Transfer Learning](https://www.isca-speech.org/archive/Interspeech_2018/pdfs/2045.pdf)
<br>
[A comparative analysis of CNN and LSTM for music genre classification](https://www.diva-portal.org/smash/get/diva2:1354738/FULLTEXT01.pdf)
<br>





