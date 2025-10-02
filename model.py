import torch


def net(x: torch.Tensor):
    """Predict next token."""
    return x.relu()**2
