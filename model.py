import torch


def net(x: torch.Tensor):
    """Predict next token."""
    return x**2
