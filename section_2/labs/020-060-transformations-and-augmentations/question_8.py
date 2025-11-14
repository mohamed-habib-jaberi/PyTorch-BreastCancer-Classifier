""""
Apply a pipeline to a Dataset. 

The pipeline will have 2 steps. 
1. The first step is to transform an image into a tensor. 
2. The second step is to normalize an image using 0.5 for all mean and standard deviation values for RGB channels. 

Create a dataset from the MNIST preloaded dataset and apply pipeline to the dataset.

Use version 1 of the transforms API.
"""


import torchvision.datasets
from torchvision import transforms

# Set the MNIST mirror to an official source
torchvision.datasets.MNIST.mirrors = [
    "https://ossci-datasets.s3.amazonaws.com/mnist/"  # Official PyTorch mirror
]

# Create the pipeline transform
transform = transforms.Compose([
   transforms.ToTensor(),
   transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])

# Create the dataset
mnist_ds = torchvision.datasets.MNIST(
    root='mnist',
    train=False,
    download=True,
    transform=transform
)

# Print the transformed dataset object
print(mnist_ds)