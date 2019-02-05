import librosa
import cv2
import numpy as np
import os
from tqdm import tqdm
import librosa.display
import matplotlib.pyplot as plt
#from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

class Dataset:
    def __init__(self,song_folder,new_folder):
        self.song_folder = song_folder
        self.new_folder = new_folder
        
    def chop_image(self, img_path, out_path):
        img = cv2.imread(img_path)
        height, width, channels = img.shape
        w = width // 10
        for i in range(0,10):
          temp = img[:, (i*w):((i+1)*w), :]
          temp = cv2.resize(temp,(128,128))
          cv2.imwrite((out_path+'_{}.png'.format(i)), temp)
    
    def spec_create(self, in_path,out_path):
        x,sr = librosa.load(in_path,sr=44100,mono=True)
        fig = plt.Figure(figsize=(36,15))   
        #canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(x))),sr=sr,ax=ax)
        output = out_path + '/test_img.jpg'
        fig.tight_layout()
        fig.savefig(output)
        self.chop_image(output, out_path)
    
    def create_data(self):
        for i in tqdm(self.song_folder):
            folder = os.path.join(self.song_folder,i)
            sub_folder = os.listdir(folder)
            for track in sub_folder:
                path = os.path.join(folder,track)
                track = list(track)
                track = track[:-4]
                track = "".join(track)
                track = int(track)
                track = str(track)
                output = os.path.join(self.new_folder,track)
                try:
                    self.spec_create(path,output)
                except:
                    print('Corrupt file {}'.format(path))