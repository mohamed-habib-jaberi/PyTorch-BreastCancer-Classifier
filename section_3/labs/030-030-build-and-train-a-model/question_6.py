"""
Create a training loop for 10 epochs. 

Be sure to initialize the loss for the current epoch as `running_loss`.

Clear the gradients, get the model predictions

Calculate the loss, compute the gradients

Update the module parameters

Accumulate the loss for the current epoch.
"""

from pre import train_dataloader
from question_2 import model
from question_4 import criterion
from question_5 import optimizer

# Set number of epochs
N_EPOCHS = 10

# Run the training loop for each epoch
for epoch in range(N_EPOCHS):
    
    # Initialize the running loss for the current epoch
    running_loss = 0.0
    
    # Loop over the training data in batches
    for i, data in enumerate(train_dataloader, 0):
        inputs, labels = data
        # Set labels for binary float
        labels = labels.unsqueeze(1).float()
        # Clear the gradients for the optimizer
        optimizer.zero_grad()
        # Get model predictions    
        outputs = model(inputs)
        # Calculate the loss with the loss function
        loss = criterion(outputs, labels)
        # Compute the gradients of the loss
        loss.backward() 
        # Update the model parameters
        optimizer.step()
        # Accumulate the loss for the epoch
        running_loss += loss.item()  

    # Print the epoch and running loss
    print(f"Epoch: {epoch} Loss: {running_loss/len(train_dataloader)}")
