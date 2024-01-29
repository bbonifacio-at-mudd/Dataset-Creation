#This file is not a script - only use it from the Dataset Creation jupyter notebook

class dataset_class():
    """
    Class for creating the dataset. Used in the Dataset Creation jupyter notebook. 
    """

    def __init__(self, size, folder_name, settings):
        self.size = size
        self.folder_name = "Dataset/" + folder_name
        self.settings = settings
        self.extract_settings()
        self.backgrounds = []
        self.chips = []

    def extract_settings(self):
        try: 
            # Extracting data settings
            self.data_settings = self.settings["data"]

            # Extracting background settings
            self.background = self.data_settings["background"]
            if self.background == "random":
                self.background_dir = "Backgrounds/Random"
            elif self.background == "walls":
                self.background_dir = "Backgrounds/Walls"
            elif self.background == "simple":
                self.background_dir = "Backgrounds/Simple"
            elif self.background == "desktop_backgrounds":
                self.background_dir = "Backgrounds/Desktop_Backgrounds"
            elif self.background == "landscape":
                self.background_dir = "Backgrounds/Landscape"
            else:
                raise Exception(f"Unsupported background type: {self.background}")
            
            # Extracting chips settings
            self.chips = self.data_settings["chips"]
            if self.chips == "all":
                self.chips_dir = "Chips/CleanedCroppedChips"
            elif self.chips == "post2020":
                self.chips_dir = "Chips/Post2020"
            else:
                raise Exception(f"Unsupported chips type: {self.chips}")
            
            # Extracting placement settings
            self.placement_type = self.settings["placement"]["type"]
            if self.placement_type == "singleton":
                self.singleton_settings = self.settings["placement"]["singleton_settings"]
            elif self.placement_type == "multiple":
                self.multiple_settings = self.settings["placement"]["multiple_settings"]
            elif self.placement_type == "stacked":
                self.stacked_settings = self.settings["placement"]["stacked_settings"]
            elif self.placement_type == "overlaid":
                self.overlaid_settings = self.settings["placement"]["overlaid_settings"]
            else:
                raise Exception(f"Unsupported placement type: {self.placement_type}")
            
            # Extracting truth data settings
            self.truth_data_settings = self.settings["truth_data_settings"]

        except Exception as e:
            raise Exception(f"{e} \n Error extracting settings from settings file. Erorr given above. \n Exiting...")

    def create_dataset(self):
        # Get the background images
        self.get_background_images()

        # Get the chip images
        self.get_chip_images()

        # Create the dataset folder
        self.create_dataset_folder()

        # Create the dataset
        if self.placement_type == "singleton":
            self.create_singleton_dataset()
        elif self.placement_type == "multiple":
            self.create_multiple_dataset()
        elif self.placement_type == "stacked":
            self.create_stacked_dataset()
        elif self.placement_type == "overlaid":
            self.create_overlaid_dataset()
        else:
            raise Exception(f"Unsupported placement type: {self.placement_type}")
        
    def get_background_images(self):

        # Check to see if the background folder exists
        if not os.path.exists(self.background_dir):
            raise Exception(f"Background folder {self.background_dir} does not exist. Exiting...")

        # Get all the background images
        for background_file in os.listdir(self.background_dir):
            self.backgrounds.append(os.path.join(self.background_dir, background_file))

    def get_chip_images(self):
        # Check to see if the chips folder exists
        if not os.path.exists(self.chips_dir):
            raise Exception(f"Chips folder {self.chips_dir} does not exist. Exiting...")

        # Get all the chip images
        for root, dirs, files in tqdm(os.walk(self.chips_dir), desc = "Loading Chips"):
            for chip_file in files:
                self.chips.append(os.path.join(root, chip_file))


    def create_dataset_folder(self):
        # Check to see if the dataset folder exists. If it does, delete it. Get confirmation from the user before doing this
        if os.path.exists(self.folder_name):
            print(f"Dataset folder {self.folder_name} already exists. Do you want to delete it and create a new one? (y/n)")
            response = input()
            if response == "y":
                shutil.rmtree(self.folder_name)
                print(f"Deleted {self.folder_name}")
            else:
                raise Exception(f"Dataset folder {self.folder_name} already exists. Exiting...")

        # Create the dataset folder
        os.mkdir(self.folder_name)
        print(f"Created {self.folder_name}")

    def create_singleton_dataset(self):
        # Create the dataset
        for i in tqdm(range(self.size), desc = "Creating Dataset"):
            # Randomly select a chip and a background, and place the chip on the background
            selected_chip = random.choice(self.chips)
            selected_background = random.choice(self.backgrounds)

            output_image_path = os.path.join(self.folder_name, f"{i}.png")

            # Load the chip and background images
            chip = Image.open(selected_chip).convert("RGBA")
            background = Image.open(selected_background).convert("RGBA")

            # Randomly rotate the chip if desired
            if self.singleton_settings["random_rotation"]:
                angle = random.randint(0, 360)
                chip = chip.rotate(angle, expand=1)

            # Background dimensions
            bg_width, bg_height = background.size
                    
            # Determine a random scale factor based on the background width and settings
            self.size_range = self.singleton_settings["size_range"]
            scale_factor = random.uniform(self.size_range[0], self.size_range[1])
            new_chip_width = int(bg_width * scale_factor)

            # Calculate new height to maintain aspect ratio
            chip_aspect_ratio = chip.width / chip.height
            new_chip_height = int(new_chip_width / chip_aspect_ratio)

            # Resize the chip
            chip = chip.resize((new_chip_width, new_chip_height), Image.Resampling.LANCZOS)

            # Ensure the resized chip can fit into the background
            if new_chip_width > bg_width or new_chip_height > bg_height:
                raise ValueError("The resized chip is too large for the background.")

            # Randomly position the resized chip on the background
            max_x, max_y = bg_width - new_chip_width, bg_height - new_chip_height
            pos_x = random.randint(0, max_x)
            pos_y = random.randint(0, max_y)

            # Extract the alpha channel from the chip as the transparency mask
            mask = chip.split()[3]

            # Paste the resized chip onto the background using the mask
            background.paste(chip, (pos_x, pos_y), mask)

            # Save the combined image to the output path
            background.save(output_image_path)

    def create_multiple_dataset(self):
        # Create the dataset
        for i in tqdm(range(self.size), desc = "Creating Dataset"):
            # Randomly select a number of chips and a background
            num_chips = random.randint(self.multiple_settings["num_chips_range"][0], self.multiple_settings["num_chips_range"][1])
            selected_chips = random.sample(self.chips, num_chips)
            selected_background = random.choice(self.backgrounds)

            output_image_path = os.path.join(self.folder_name, f"{i}.png")

            # Load the background image
            background = Image.open(selected_background).convert("RGBA")

            # Background dimensions
            bg_width, bg_height = background.size

            # Initialize the list of chips to add with their positions and mask
            chips_to_add = []

            for chip_path in selected_chips:
                # Load and process each chip
                chip = Image.open(chip_path).convert("RGBA")
                
                # Randomly rotate the chip if desired
                if self.multiple_settings["random_rotation"]:
                    angle = random.randint(0, 360)
                    chip = chip.rotate(angle, expand=1)

                # Determine a random scale factor based on the background width and settings
                self.size_range = self.multiple_settings["size_range"]
                scale_factor = random.uniform(self.size_range[0], self.size_range[1])
                new_chip_width = int(bg_width * scale_factor)

                # Calculate new height to maintain aspect ratio
                chip_aspect_ratio = chip.width / chip.height
                new_chip_height = int(new_chip_width / chip_aspect_ratio)

                # Resize the chip
                chip = chip.resize((new_chip_width, new_chip_height), Image.Resampling.LANCZOS)

                # Randomly position the resized chip on the background
                max_x, max_y = bg_width - new_chip_width, bg_height - new_chip_height
                pos_x = random.randint(0, max_x)
                pos_y = random.randint(0, max_y)

                # Extract the alpha channel from the chip as the transparency mask
                mask = chip.split()[3]

                # Add the chip to the list of chips to add along with its data
                chips_to_add.append((chip, pos_x, pos_y, mask))

            # Sort the chips by size with the largest chips first - small measure to prevent total overlap. Doesn't guarantee no overlap
            chips_to_add.sort(key=lambda x: x[0].size[0], reverse=True)

            # Add the chips to the background
            for chip, pos_x, pos_y, mask in chips_to_add:
                background.paste(chip, (pos_x, pos_y), mask)

            # Save the combined image to the output path
            background.save(output_image_path)


import os
import shutil
import random
from PIL import Image
from tqdm import tqdm