"""
Create a dataloader from our dataset named cd_dataset called cd_dataloader and then iterate through a batch and print the features and labels shape. 

When creating the dataloader, set the size of the batch to 4.  
"""
from question_3 import cd_dataset
# Import dataloader utility here
from torch.utils.data import DataLoader

# Create the dataloader called cd_dataloader and set size to 4. 
cd_dataloader = DataLoader(dataset=cd_dataset, batch_size=4, shuffle=True)

# Iterate through this dataloader like we did above
features, labels, urls = next(iter(cd_dataloader))

# Print the batch size and the number of labels
print(f"Features batch shape: {features.size()}")
print(f"Labels batch size shape: {labels.size()}")

print(features.shape)
print(labels.shape)
