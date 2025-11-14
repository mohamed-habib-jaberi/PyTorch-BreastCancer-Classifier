"""
Load the `mobilenet_v3_large` pre-trained model from `v0.10.0` of the PyTorch vision github repo. 

Be sure to load the pre-trained parameters.

"""
# import modules
#from torch import hub


# Load Model from the hub
#model = hub.load('pytorch/vision:v0.10.0', 'mobilenet_v3_large', pretrained=True, skip_validation=True)

# Fixed code (no hub): using torchvision directly instead of torch.hub 
# because torch.hub loads old torchvision versions that break with newer PyTorch/ONNX APIs.
# This avoids compatibility errors and still gives the same pretrained model.

"""
we’re hitting a Torch / TorchVision version mismatch because torch.hub.load('pytorch/vision:v0.10.0', …) pulls an old TorchVision (0.10.0) repo that doesn’t match your installed PyTorch, causing the ONNX import error.

Fastest fix: don’t use torch.hub here—load MobileNetV3 directly from our installed torchvision with its 

"""
from torchvision.models import mobilenet_v3_large, MobileNet_V3_Large_Weights

# Get the default pretrained weights
weights = MobileNet_V3_Large_Weights.DEFAULT

# Load the pretrained model
model = mobilenet_v3_large(weights=weights)
#model.eval()  # inference mode