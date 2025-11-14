"""
Utilize Accuracy from torchmetrics to compute accuracy.

Be sure to set the model to evaluation model as well as set the code to not compute gradients.
"""
from step01_load_data import test_loader
# Import modules
import torchmetrics
import torch

# Initialize the accuracy metric as a multiclass task and set number of classes to 2
accuracy_metric = torchmetrics.Accuracy(task="multiclass", num_classes=2)

# Function for 
def evaluate_model(model):
    
    # Set model to evaluation mode
    model.eval()
    # Disable gradient computation
    with torch.no_grad():
        # Loop over the test dataloader
        for i, data in enumerate(test_loader, 0):
            inputs, labels = data
            outputs = model(inputs)

            # Get predicted class
            _, predicted = torch.max(outputs.data, 1)

            # Update the accuracy metric with predictions and true labels
            accuracy_metric.update(predicted, labels)

    # Compute the final accuracy
    final_accuracy = accuracy_metric.compute()
    print(f"Accuracy: {final_accuracy * 100}%")
