
## Environment

```
# Create conda environment
conda create -n pytorch_env python=3.12
conda activate pytorch_env 

# Install PyTorch
# Make sure cuXXX matches the supported cuda version
# More information: https://pytorch.org/get-started/locally/
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install packages
conda install jupyter ipykernel pandas trimesh
```