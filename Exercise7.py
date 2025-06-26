####################################### Neural Networks
####################### Packages
import torch
import numpy as np
import torchvision
import torchvision.transform as transforms

torch.manual_seed(42)
print("Using torch", torch.__version__)

####################### Fundamental data structure is the Tensor

M = torch.Tensor([[1, 2], [3, 4]])
M

### Create a 3x3 tensor
shape = (3,3)

rand_tensor = torch.rand(shape) # Create random 3x3 tensor
ones_tensor = torch.ones(shape) # All 1s
zeros_tensor = torch.zeros(shape) # All 0s

### Print
print(f"Random Tensor: \n {rand_tensor} \n")
print(f"Ones Tensor: \n {ones_tensor} \n")
print(f"Zeros Tensor: \n {zeros_tensor}")

### Create 3x3 tensor w/ random values between 0 & 4
tensor = torch.randint(0, 4, (3,3))
tensor

print(f"Shape of tensor: {tensor.shape}") # Print tensor shape
print(f"Datatype of tensor: {tensor.dtype}") # Print tensor datatype
print(f"Device tensor is stored on: {tensor.device}") # Print location (CPU)

### Add values to a tensor
t = torch.tensor(3)
t = t + 10
print(t)

### Transpose a tensor
M.t()

### Reshaping a tensor
t = torch.arange(20)
t.view(2, 10) # np.reshape







