[![Python 3.9](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)

# Deep Learning reproduction of: Leveraging triplet loss for unsupervised action segmentation

This repository is part of the reproducibility project of the CS4240 Deep Learning course at TU Delft.

The reproduction is based on:
- this paper: https://arxiv.org/pdf/2304.06403v2.pdf  
- the publicly available code from: https://github.com/elenabbbuenob/TSA-ActionSeg
- and the Breakfast dataset: https://serre-lab.clps.brown.edu/resource/breakfast-actions-dataset/#Downloads


## Setup
1. Download [NVIDIA driver for your GPU](https://www.nvidia.com/download/index.aspx?lang=en-us)
   1. For Windows, you can figure out what GPU you have by going to "Device Manager" > "Display adaptors" 
2. Download the [CUDA Toolkit](https://developer.nvidia.com/cuda-downloads) 
3. Download [anaconda3](https://www.anaconda.com/download) and open the `Anaconda Prompt`, 
   1. Update conda with `conda update conda` (takes about **5min**) and 
   2. Clean anything that you have installed in the base package (clean the cache): `conda clean -a`
4. Create the environment: `conda create --name tsa-action-seg python=3.9`, this should say where the environment was created
   1. REMEMBER that file path, should be something like:
   ```
   ## Package Plan ##

     environment location: C:\Users\...\anaconda3\envs\tsa-action-seg
   ```
   2. Here you should find a file called `python.exe`, so full path (called from now ENV_PATH) should be something like `C:\Users\...\anaconda3\envs\tsa-action-seg\python.exe`
5. Activate the conda environment:
   ```
   conda activate tsa-action-seg
   ```
6. Run the command below, for me it took about **5min** for it to download everything, so just let it run for a bit... (if it seems to get stuck, i.e. you wait for more than 10min you might have to update conda - see above)
   ```
   conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
   ```
7. In the conda terminal go to the root path of this project (`C:\...\dl-action-segmentation\`, in Pycharm you can Right-Click on root folder > Copy Path/Reference > Absolute Path), and run: 
    ```
    conda install --file requirements.txt
    ```
   1. If conda gets stuck, you could also try running it with pip (but I'd recommend you stick to ONE package manager): `pip install -r requirements.txt`
8. Open Pycharm, in bottom right you can select your interpreter:   
   ![setup_img/interpreter.png](setup_img/interpreter.png)
9. Add the Conda environment that we just created, using the ENV_PATH from above ![setup_img/conda_env.png](setup_img/conda_env.png)

### Helper commands (in case you want to reset the instalation)
- See all the conda environments `conda env list`
- Remove the created env: `conda env remove --name tsa-action-seg`

## Datasets

### Breakfast dataset
1. You can run the `setup_file_structure.py` file from the root of this folder to setup the dataset folders inside TSA-ActionSeg

2. Download ([BreakfastII_15fps_qvga_sync.tar.gz 3.6 GB](https://drive.google.com/open?id=1I70VymcaQypIcJ8TXhb2_AlSmoo6MUm4)) from: https://serre-lab.clps.brown.edu/resource/breakfast-actions-dataset/#Downloads, and we probably also need the "I3D feature (pretrained on Kinetics, no fine-tuning) for rgb and flow (2048 dim): [bf_kinetics_feat.tar.gz (27.7 GB)](https://drive.google.com/open?id=1I70VymcaQypIcJ8TXhb2_AlSmoo6MUm4)"

3. Change in `breakfast_action.py` the following lines (11-14):
```
features_path = "datasets/breakfast_action/features/"
self.labels_path = "datasets/breakfast_action/groundTruth/"
self.features_files = sorted(glob.glob(features_path + "/**/**/*.txt"))
self.mapping_file = "datasets/breakfast_action/mappping/mapping.txt"
```

### Inria_YT dataset
Not relevant for our project, but you can look into this Github repo for details: https://github.com/jalayrac/instructionVideos

### Camma dataset
Silvia's suggestion, download from here: http://camma.u-strasbg.fr/datasets

## Run

### Do I have a GPU?
You can check if you have a GPU by running the file called `whats_my_GPU.py`

### Run on Breakfast dataset
In Pycharm you can right-click on `tsa.py` file > `More Run/Debug` > `Modify Run Configuration..` and in `Parameters` you should put:
- if you have a GPU: `--config_exp configs/breakfast_action.yml --gpu <NAME_OF_YOUR_GPU> --name <NAME_OF_EXPERIMENT>`
- if you don't have a GPU: `--config_exp configs/breakfast_action.yml --name <NAME_OF_EXPERIMENT>`
- example: `--config_exp configs/breakfast_action.yml --name experiment_1`


# TODO...
- [ ] TODO: we don't have the `/datasets/breakfast_action/mappping/mapping.txt` file, and IDK where to get it from!!!!!!!
  - Improved dense trajectories: [here](https://thoth.inrialpes.fr/people/wang/improved_trajectories.html) and [paper here](https://www.cv-foundation.org/openaccess/content_iccv_2013/papers/Wang_Action_Recognition_with_2013_ICCV_paper.pdf)
  - IDT features provided: [here](https://github.com/annusha/unsup_temp_embed) and [paper here](https://openaccess.thecvf.com/content_CVPR_2019/papers/Kukleva_Unsupervised_Learning_of_Action_Classes_With_Continuous_Temporal_Embedding_CVPR_2019_paper.pdf)
  - ![setup_img/input_features_breakfast.png](setup_img/input_features_breakfast.png)