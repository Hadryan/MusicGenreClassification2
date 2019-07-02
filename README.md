# MusicGenreClassification

Music Genre classification is an important problem for the services like spotify etc. We have tackled this problem by creating the mel spectograms of the data and converting them into images. The dataset used was fma_small which can be found [here](https://github.com/mdeff/fma). Spectograms were created using [librosa](https://librosa.github.io/librosa/). Preprocessed images can be downloaded using this [link](https://drive.google.com/open?id=1SKW6aNswBzWhG-LylVopaHTgz60mBLnx) and [labels](https://drive.google.com/file/d/1tIxKbROqtlHqk1COuuc9VFd3Iq5zVcvP/view?usp=sharing).

# Preprocessing Pipeline:

Code for preprocessing - [here](https://github.com/sanchit2843/MusicGenreClassification/blob/master/Data/data_preprocessing.py)
Audio was read using librosa library at a sampling rate of 44100. The data was then converted into frequency domain using librosa.stft. The output was converted in dB scale and the spectogram was plotted and saved as image. This image was chopped into 10 parts each labelled same.

# Data Visualization
Few samples from dataset
![](https://github.com/sanchit2843/MusicGenreClassification/blob/master/assets/spectogram.png)

