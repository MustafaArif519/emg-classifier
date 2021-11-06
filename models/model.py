import torch
import torch.nn as nn
from math import sqrt
import torch.nn.functional as F

class EMG_Model(nn.Module):
    def __init__(self):
        super().__init__()

        # TODO
        self.conv1 = nn.Conv2d(1, 16, kernel_size=(3, 7), stride=2, padding=())
        self.pooling = nn.MaxPool2d(2,2)

        # linear layer gives us different predictions on each class, since we have 5 class, the output is 5
        self.linear = nn.Linear(128, 5) # TODO, change 128

    def init_weights(self):
        # TODO
        # try different methods to initialize weight to see effects
        for conv in [self.conv1]:
            C_in = conv.weight.size(1)
            print(conv.weight)
            nn.init.normal_(conv.weight, 0.0, 1 / sqrt(5 * 5 * C_in))
            nn.init.constant_(conv.bias, 0.0)
        pass
    
    def forward(self, X):
        # N: number of 2D input we feed in
        # C: number of channels in each input - 1
        # H: height
        # W: width
        N, C, H, W = X.shape 
        # TODO, change it to your own model
        out = F.relu(self.conv1(X))
        out = self.pool(out)

        # Flattern it out for linear layer (2D -> 1D)
        out = out.view(N, -1)
        out = self.linear(out)
        return out
    

