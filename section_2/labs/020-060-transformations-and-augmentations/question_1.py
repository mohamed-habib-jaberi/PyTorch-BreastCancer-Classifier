"""
Import PyTorch’s image transformation module two different ways for version 1 of the API.
"""
# Import the transformation module in the first way using full path
import torchvision.transforms

# Import the transformation module in the second way using alias
from torchvision import transforms

# Print both imported objects to validate
print(torchvision.transforms)
print(transforms)
