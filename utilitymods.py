import torch

class DanMod(torch.nn.Module):
  def param_count(self):
    return sum(p.numel() for p in self.parameters() if p.requires_grad)
