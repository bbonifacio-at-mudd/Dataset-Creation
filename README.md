# Dataset-Creation
 Creates the chips dataset using the data scraped from Chip-Scraper


Here are the different types of datasets this will make: 

1. Singleton Chips - A single random chip on a random background with a random position (such that the entire chip is in the image) and a random rotation.
2. Multiple Chips - Same as Singleton Chips, except there are multiple chips on the page (random number between 2-10?). This is done such that the chips do not overlap with each other. 
3. Stacked Chips - Unsure about how this one works, need to ask.
4. Overlaid Chips - Also unsure about this one. I assume this is equivalent to multiple chips except that the chips overlap with each other (but not entirely?)


This code assumes that all the data is already scraped. So, this code is not I/O intensive, but rather computationally intensive. Due to the code being computationally intensive, I recommend running it in Google Collab on a GPU: 


How to open notebook in google collab:
Go to https://colab.research.google.com/. 

When opening a notebook, enter the url for this repo as shown in the image below. The most up-to-date version of the notebook will be the Primary Notebook.

**If you'd like to start from a blank notebook, open Untitled0.ipynb**

![image](https://github.com/bbonifacio-at-mudd/E208_Final/assets/114462423/1236da58-bed0-4ac3-ba1b-aa584b07493d)



After you open the Primary notebook, there's one more step in order to save any changes you make. Hit **File** and then **Save a copy in Github** as shown below. 
You have a choice to either overwrite the current **Primary Notebook** or to save your changes to a new notebook. Do whichever is appropriate. 
But as a general rule of thumb, if you were just experimenting with changing stuff, save it to a new notebook. If your changes are significant, clean, and 
are appropriate for future notebooks to be branched from, overwrite the Primary Notebook. If not, there's never any harm in saving to a new notebook. 

![image](https://github.com/bbonifacio-at-mudd/E208_Final/assets/114462423/1a1aecea-2d7f-4b6b-9f8a-5ac632fb3f7b)
![image](https://github.com/bbonifacio-at-mudd/E208_Final/assets/114462423/d865d9a5-19ad-4772-9ad0-4e5d6dc59a13)
