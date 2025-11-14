"""
Define an optimizer. 

Import the module for optimizers and create using the Adam optimizer using our model weights and a learning rate of 0.001. 

"""
from question_2 import model
# Import the module
import torch.optim as optim

# Create the optimizer and pass in the model weights and an learning rate of 0.001
optimizer = optim.Adam(model.parameters(), lr=0.001)
