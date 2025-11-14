"""
Create a transform pipeline. 

The first step of the pipeline is to resize the image to 100 by 100 pixels. 

The second step of the pipeline is to randomly horizontally flip the image 50% of the time. 

The third and final step is to randomly distort the image by changing the contrast of the image with a minimum of .7 and a maximum of 1.2. 

Apply the transformation using v2 of the API.
"""


from torchvision.transforms import v2
from PIL import Image

# Load the image into memory
image = Image.open("images/dog/dog-5.jpg")

# Create the Pipeline transform
pipeline = v2.Compose([
   v2.Resize(size=(100, 100)),
   v2.RandomHorizontalFlip(p=0.5),
   v2.RandomPhotometricDistort(
       contrast=(0.7, 1.2))
])

# Apply the pipeline
pipeline_image = pipeline(image)

# Print the pipeline transformed object
print(pipeline_image)