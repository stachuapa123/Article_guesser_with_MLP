import torch 
from torch.utils.data import Dataset

class ArticleDataset(Dataset):
    def __init__(self,X,y):
        self.X = X
        self.y = y

    def __len__(self):
        return len(self.X)
    
    def __getitem__(self, idx):
        if idx >= len(self):
            raise IndexError("dataset index out of range")
          # 1st index after window
        return self.X[idx], self.y[idx]