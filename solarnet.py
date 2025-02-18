import torch
import torch.nn as nn

class SolarNet(nn.Module):
    def __init__(self):
        super(SolarNet, self).__init__()
        # 编码器
        self.conv1 = nn.Conv2d(2, 32, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=3, padding=1)
        self.conv3 = nn.Conv2d(64, 128, kernel_size=3, padding=1)

        # 解码器
        self.up1 = nn.ConvTranspose2d(128, 64, kernel_size=2, stride=2)
        self.up2 = nn.ConvTranspose2d(64, 32, kernel_size=2, stride=2)
        self.up3 = nn.ConvTranspose2d(32, 1, kernel_size=2, stride=2)

        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = self.pool(torch.relu(self.conv2(x)))
        x = self.pool(torch.relu(self.conv3(x)))
        x = torch.relu(self.up1(x))
        x = torch.relu(self.up2(x))
        x = self.up3(x)
        return self.sigmoid(x)
