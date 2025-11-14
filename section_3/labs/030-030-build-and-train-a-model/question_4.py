"""
Define a loss function. 

Import the module and create an instance of a loss function called “criterion” using Cross Entropy Loss.

"""
# Import the module as nn

import torch.nn as nn

# Define Binary Cross Entropy loss function
criterion = nn.BCELoss()
