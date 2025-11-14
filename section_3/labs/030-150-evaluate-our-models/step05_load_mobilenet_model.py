"""
From torchvision models, load the pre-trained mobilenet_v3_large model with default MobileNet_V3_Large_Weights weights.

Modify the last layer for 2 classes.

Load the model from checkpoint.

Load the model parameters from the checkpoint.
"""
# Import modules
import torch
import torch.nn as nn
from torchvision import models

# Load the mobilenet_v3_large model with default weights
model = models.mobilenet_v3_large(weights=models.MobileNet_V3_Large_Weights.DEFAULT)


# Modify last layer of the model for 2 classes as output
model.classifier[-1] = nn.Linear(model.classifier[-1].in_features, 2)

# Load the model from checkpoint
checkpoint = torch.load('mobilenet_checkpoint.tar', weights_only=True)

# Load the parameters from the checkpoint
model.load_state_dict(checkpoint['model_state_dict'])

# Print the model
print(model)
