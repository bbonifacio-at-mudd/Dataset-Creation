# Dataset Creation Documentation
## WARNING: There are a lot of images in this repo, so this will take up a lot of storage space (several GB)

Creates a dataset using object images (such as Table Chips) and Background Images. It does this by placing the object images on top of the Background Images in a way that you can control with the settings. Chip objects are retrieved from the Chip-Scraper repo: https://github.com/bbonifacio-at-mudd/Chip-Scraper/tree/main

This repository is structured as follows: 
- Backgrounds: the choice of background images we want to use. If we want to use different backgrounds, we can just create a new subfolder in this.
- Chips: the Table Chips. We have uncropped and circle-cropped. I went through and cleaned the circle-cropped, and I put the few bad images in the badChips folder. If we want other objects to overlay on the backgrounds, we just create a new subfolder in this. I also made folders for post-2010 and post-2020 chips. 
- Dataset: the resulting datasets that are created.  
- lib: Supporting files and Jupyter notebooks. The most important of these is dataset_file.py, which contains the dataset_class. This class holds all the currently supported functionality. 
- Dataset Creation.ipynb - The Primary Notebook for this repo that controls everything. If you want to make a dataset, open this file, fill in the settings within the file, and make your dataset!

Below, I include some example images created by this dataset. To figure out how everything works, open the Dataset Creation jupyter notebook and read through the settings: 

![image](https://github.com/bbonifacio-at-mudd/Dataset-Creation/assets/114462423/f3c9bfa4-c4eb-479d-818c-f0b4d2b9cd10)
![image](https://github.com/bbonifacio-at-mudd/Dataset-Creation/assets/114462423/0bd989ab-3de1-43ba-984c-0a2d76afef07)
![image](https://github.com/bbonifacio-at-mudd/Dataset-Creation/assets/114462423/9c3b7a92-dce3-401d-9fa2-720b6f3d0040)

