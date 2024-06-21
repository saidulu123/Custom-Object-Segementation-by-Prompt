Selective-Object-Segmentation

Installation of Grouding DINO, SAM and DEVA

To work locally, Must need GPU Support and C++ Extensions 

```markdown
# Setting Up Local GPU Environment for Grounded-SAM

## Set Environment Variables

Set the following environment variables manually:

```bash
export AM_I_DOCKER=False
export BUILD_WITH_CUDA=True
export CUDA_HOME=/path/to/cuda-11.3/
```

## Install Segment Anything

```bash
python -m pip install -e segment_anything
```

## Install Grounding DINO

```bash
pip install --no-build-isolation -e GroundingDINO
```

## Install Diffusers

```bash
pip install --upgrade diffusers[torch]
```

## Install OSX

```bash
git submodule update --init --recursive
cd grounded-sam-osx && bash install.sh
```

## Install RAM & Tag2Text

```bash
git clone https://github.com/xinyu1205/recognize-anything.git
pip install -r ./recognize-anything/requirements.txt
pip install -e ./recognize-anything/
```

## Optional Dependencies

These dependencies are necessary for mask post-processing, saving masks in COCO format, the example notebooks, and exporting the model in ONNX format. `jupyter` is also required to run the example notebooks.

```bash
pip install opencv-python pycocotools matplotlib onnxruntime onnx ipykernel
```

Important Note
Please make sure to follow the installation steps strictly. If the program produces:

```csharp
NameError: name '_C' is not defined
If this happens, please reinstall Grounding DINO by recloning the git repository and performing all the installation steps again.
```

For more details, refer to the individual installation guides for [Segment Anything](https://github.com/facebookresearch/segment-anything), [Grounding DINO](https://github.com/IDEA-Research/GroundingDINO), and [OSX](https://github.com/your-osx-repository).
```
