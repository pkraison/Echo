import megengine.functional as F
import megengine.module as M
import megengine as mge


# FReLU


class FReLU(M.Module):

    def __init__(self, in_channels):
        """
        Init method.
        """
        super(FReLU,self).__init__()
        self.conv_frelu = M.Conv2d(in_channels, in_channels, 3, 1, 1, groups=in_channels)
        self.bn_frelu = M.BatchNorm2d(in_channels)

    def forward(self, input):
        """
        Forward pass of the function.
        """
        tau = self.conv_frelu(input)
        tau = self.bn_frelu(tau)
        output = F.maximum(input, tau)
        return output


# Mish


class Mish(M.Module):

    def __init__(self):
        """
        Init method.
        """
        super(Mish,self).__init__()

    def forward(self, input):
        """
        Forward pass of the function.
        """
        return input * F.tanh(F.softplus(input))