from model import Model
import torch.optim as optim
from torch.optim import lr_scheduler
import torch.nn as nn
from Data.data_preprocessing import Dataset


if __name__ == "__main__":
    csv_path = ''
    mp3_path = ''
    new_images_path = ''
    
    preprocess = Dataset(mp3_path,new_images_path,csv_path)
    preprocess.create_data()
    
    
    
    model_object = Model()
    model = model_object.get_model()
    
    criterion = nn.CrossEntropyLoss()
    optimizer_ft = optim.SGD(model.parameters(), lr=0.0001 , momentum = 0.9)
    exp_lr_scheduler = lr_scheduler.StepLR(optimizer_ft, step_size=2, gamma=0.1)
    