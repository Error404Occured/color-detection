# Color Detection Project

This project includes two Python scripts for color detection:
1. `color_detection_image.py` - Detects colors from a static image.
2. `color_detection_webcam.py` - Detects colors from a live webcam feed.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Files](#files)
- [Usage](#usage)
  - [Color Detection from Image](#color-detection-from-image)
  - [Color Detection from Webcam](#color-detection-from-webcam)
- [Instructions](#instructions)

## Prerequisites

Make sure you have the following libraries installed:
- OpenCV
- Pandas
- NumPy

You can install these libraries using pip:
```bash
pip install opencv-python pandas numpy
```

## Files
1. colors.csv: A CSV file containing color names and their corresponding RGB and HEX values.
2. color_detection_image.py: Script for detecting colors in a static image.
3. color_detection_webcam.py: Script for detecting colors in a live webcam feed.


## Usage

### Color Detection from Image

1. **Ensure `colors.csv` is in the same directory as `color_detection_image.py`.**

2. **Prepare an image**: Make sure you have an image (e.g., `colorpic.jpg`) in the specified directory.

3. **Run the script**:
   ```bash
   python color_detection_image.py
   ```

### Color Detection from Webcam
1. Ensure colors.csv is in the same directory as color_detection_webcam.py.

2. Run the script:

```bash
python color_detection_webcam.py
```

## Instructions:

1. A window will open displaying the live webcam feed.
2. Double-click on any part of the video feed to see the RGB values and the closest color name.
3. The detected color name and RGB values will be displayed as text on the video feed.
4. Press the 'ESC' key to exit the program.
