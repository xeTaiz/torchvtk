import os

import torch
from batchviewer import view_batch

from torchvtk.augmentation.DictTransform import BlurDictTransform, NoiseDictTransform, RotateDictTransform, CroppingTransform

# import test image
file_path = os.path.join("D:", os.sep, "DownloadDatasets", "medical_decathlon", "Numpy", "torch", "0.pt")
file = torch.load(file_path)

# Test Noise Transform.
# tfms = NoiseDictTransform(device="cpu", apply_on=["vol"], noise_variance=(0.01, 0.02))
# noise_cpu = tfms(file).copy()
# del tfms
# tfms = NoiseDictTransform(device="cuda", apply_on=["vol"], noise_variance=(0.01, 0.02))
# noise_gpu = tfms(file)
#
# file["vol"] = file["vol"].to("cpu")
# # test for gaussian blur
# tfms = BlurDictTransform(apply_on=["vol"], device="cpu", channels=1, kernel_size=(3, 3, 3), sigma=1)
# blur_cpu = tfms(file)
# tmp = blur_cpu["vol"]
# tmp = tmp.squeeze(0).squeeze(0)
#
# view_batch(tmp, width=512, height=512)
# tfms = BlurDictTransform(apply_on=["vol"], device="cuda", channels=1, kernel_size=(3, 3, 3), sigma=1)
# blur_gpu = tfms(file)
# view_batch(blur_gpu["vol"].squeeze(0).squeeze(0), width=512, height=512)
# file["vol"] = file["vol"].to("cpu")

# Cropping
# view_batch(file["vol"], width=512, height=512)
# tfms = CroppingTransform(device="cuda",  apply_on=["vol"], dtype=torch.float32)
# noise_cpu = tfms(file)
# noise_cpu["vol"] = noise_cpu["vol"].squeeze(0).squeeze(0)
# view_batch(noise_cpu["vol"], width=512, height=512)
# del tfms

# check for random rotation
# fixme rotation is on the wrong axis and resampling does not seem to work
tfms = RotateDictTransform(device="cpu", degree=4, axis=0, apply_on=["vol"], fillcolor_vol=0, fillcolor_mask=0)
noise_cpu = tfms(file)
noise_cpu["vol"] = noise_cpu["vol"].squeeze(0).squeeze(0)
view_batch(noise_cpu["vol"], width=512, height=512)
del tfms



# check for specific rotation
# todo add tests for torch 16