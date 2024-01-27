# Dataset Creation Documentation
Creates the chips dataset using the data scraped from Chip-Scraper

This repository is structured as follows: 
- Backgrounds: the choice of background images we want to use. If we want to use different backgrounds, we can just create a new subfolder in this.
- Chips: the Table Chips. We have uncropped and circle-cropped. I went through and cleaned the circle-cropped, and I put the few bad images in the badChips folder.
- Dataset: the datasets we're going to make with the chips on the backgrounds
- Notebooks: the jupyter notebooks used to run the code. Why jupyter notebook? no specific reason, it just feels nice. if you want, feel free to copy-paste it into a .py file to run it. Each notebook is specific for cropping or making a specific type of dataset, such as Singleton vs. Multiple

Here are the different types of datasets this will make: 

1. Singleton Chips - A single random chip on a random background with a random position (such that the entire chip is in the image) and a random rotation.
2. Multiple Chips - Same as Singleton Chips, except there are multiple chips on the page (random number between 2-10?). This is done such that the chips do not overlap with each other. 
3. Stacked Chips - Unsure about how this one works, need to ask.
4. Overlaid Chips - Also unsure about this one. I assume this is equivalent to multiple chips except that the chips overlap with each other (but not entirely?)
