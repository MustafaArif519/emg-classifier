import numpy as np
import pandas as pd
from pathlib import Path
import torch
import random
from torch.utils.data import Dataset, DataLoader
from models.model import EMG_Model


class EMGDataset(Dataset):
    def __init__(self, partition, data_folder):
        super().__init__()

        if partition not in ['train', 'val']:
            raise ValueError("Partition {} does not exist".format(partition))
        
        np.random.seed(42)
        torch.manual_seed(42)
        random.seed(42)
        self.partition = partition
        self.data_folder = data_folder
        self.X, self.y = self._load_data()
        print(self.X.shape) # 150 x 8 x 1500
        print(self.y.shape)

    def __len__(self):
        """Return size of dataset."""
        return len(self.X)

    def __getitem__(self, idx):
        """Return (image, label) pair at index `idx` of dataset."""
        return torch.from_numpy(self.X[idx]).float(), torch.tensor(self.y[idx]).long()

    def _load_data(self):
        x, y = []
        for label in range(1, 6):
            p = self.data_folder / str(label)
            txts = (list)(p.glob('*.txt'))
            for txt in txts:
                a = np.loadtxt(txt, dtype=np.float64, delimiter=',')
                print(a.shape)
                # transpose a
                a = np.transpose(a)
                x.append(a)
                y.append(label)
        return np.array(x), np.array(y)

def get_train_val_datasets(train_folder, val_folder):
    tr = EMGDataset('train', train_folder)
    va = EMGDataset('val', val_folder)
    return tr, va


def get_train_val_loaders(batch_size, train_folder, val_folder):
    tr, val = get_train_val_datasets(train_folder, val_folder)
    tr_loader = DataLoader(tr, batch_size=batch_size, shuffle=True)
    va_loader = DataLoader(val, batch_size=batch_size, shuffle=False)
    return tr_loader, va_loader

def evaluate_performance(tr_loader, val_loader, model, criterion, epoch):
    pass

def train_epoch(data_loader, model, criterion, optimizer):
    for i, (X, y) in enumerate(data_loader):
        output = model(X)
        loss = criterion(output, y)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()
        if i % 100 == 0:
            print(f"Training batch loss {loss}")



def main():
    # p = Path('./EMG_data_trimmed/1/trimmed_0.txt')
    # a = np.loadtxt(p, dtype=np.float64, delimiter=',')
    # a = np.transpose(a)
    # print(a.shape)
    train, val = get_train_val_loaders(20)
    data_directory = Path('./EMG_data_trimmed')

    model = EMG_Model()



if __name__ == "__main__":
    main()