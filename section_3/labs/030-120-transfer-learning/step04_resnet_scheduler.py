"""
Create StepLR scheduler that reduces the learning rate by 0.1 every 2 epochs
"""
from step03_modify_resnet_output import model
# Import module
import torch.nn as nn
import torch.optim as optim

# Define the loss function
criterion = nn.CrossEntropyLoss()

# Set up the optimizer
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

# Create a StepLR scheduler
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=2, gamma=0.1)

# Print the components
print(criterion, optimizer, scheduler)