# =========================================================
# 🖼️ Grayscale Image Manipulator using NumPy
# =========================================================
# Concepts Covered:
# ✅ Image Loading
# ✅ Grayscale Conversion
# ✅ Brightness Adjustment
# ✅ Image Flipping
# ✅ Cropping
# ✅ Blur Effect
# ✅ Display Multiple Images
# =========================================================

# =========================================================
# IMPORT LIBRARIES
# =========================================================

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


# =========================================================
# STEP 1 — LOAD IMAGE
# =========================================================

# Load image from current folder
image = mpimg.imread(r"try\tasks\sample.jpg")

# Print image dimensions
print("=================================================")
print("📌 IMAGE INFORMATION")
print("=================================================")

print("Image Shape :", image.shape)
print("Image Type  :", image.dtype)


# =========================================================
# STEP 2 — CONVERT IMAGE TO GRAYSCALE
# =========================================================
# Formula:
# Gray = (R + G + B) / 3

grayscale = np.mean(image, axis=2)


# =========================================================
# STEP 3 — INCREASE BRIGHTNESS
# =========================================================
# Add constant value to each pixel

bright_image = np.clip(image + 50, 0, 255)


# =========================================================
# STEP 4 — DECREASE BRIGHTNESS
# =========================================================

dark_image = np.clip(image - 50, 0, 255)


# =========================================================
# STEP 5 — FLIP IMAGE HORIZONTALLY
# =========================================================

horizontal_flip = np.fliplr(image)


# =========================================================
# STEP 6 — FLIP IMAGE VERTICALLY
# =========================================================

vertical_flip = np.flipud(image)


# =========================================================
# STEP 7 — CROP IMAGE
# =========================================================
# Syntax:
# image[row_start:row_end, col_start:col_end]

cropped_image = image[100:400, 200:500]


# =========================================================
# STEP 8 — BLUR EFFECT (BONUS)
# =========================================================

blurred_image = image.copy()

# Apply blur using neighboring pixels
for i in range(1, image.shape[0] - 1):
    for j in range(1, image.shape[1] - 1):

        blurred_image[i, j] = np.mean(
            image[i-1:i+2, j-1:j+2],
            axis=(0, 1)
        )


# =========================================================
# STEP 9 — DISPLAY ALL IMAGES
# =========================================================

fig, axes = plt.subplots(3, 3, figsize=(15, 15))


# ---------------------------------------------------------
# ORIGINAL IMAGE
# ---------------------------------------------------------

axes[0, 0].imshow(image)
axes[0, 0].set_title("Original Image")
axes[0, 0].axis("off")


# ---------------------------------------------------------
# GRAYSCALE IMAGE
# ---------------------------------------------------------

axes[0, 1].imshow(grayscale, cmap='gray')
axes[0, 1].set_title("Grayscale Image")
axes[0, 1].axis("off")


# ---------------------------------------------------------
# BRIGHT IMAGE
# ---------------------------------------------------------

axes[0, 2].imshow(bright_image.astype(np.uint8))
axes[0, 2].set_title("Brightened Image")
axes[0, 2].axis("off")


# ---------------------------------------------------------
# DARK IMAGE
# ---------------------------------------------------------

axes[1, 0].imshow(dark_image.astype(np.uint8))
axes[1, 0].set_title("Dark Image")
axes[1, 0].axis("off")


# ---------------------------------------------------------
# HORIZONTAL FLIP
# ---------------------------------------------------------

axes[1, 1].imshow(horizontal_flip)
axes[1, 1].set_title("Horizontal Flip")
axes[1, 1].axis("off")


# ---------------------------------------------------------
# VERTICAL FLIP
# ---------------------------------------------------------

axes[1, 2].imshow(vertical_flip)
axes[1, 2].set_title("Vertical Flip")
axes[1, 2].axis("off")


# ---------------------------------------------------------
# CROPPED IMAGE
# ---------------------------------------------------------

axes[2, 0].imshow(cropped_image)
axes[2, 0].set_title("Cropped Image")
axes[2, 0].axis("off")


# ---------------------------------------------------------
# BLURRED IMAGE
# ---------------------------------------------------------

axes[2, 1].imshow(blurred_image.astype(np.uint8))
axes[2, 1].set_title("Blurred Image")
axes[2, 1].axis("off")


# ---------------------------------------------------------
# EMPTY SPACE
# ---------------------------------------------------------

axes[2, 2].axis("off")


# =========================================================
# FINAL DISPLAY SETTINGS
# =========================================================

plt.tight_layout()

print("\n=================================================")
print("✅ IMAGE PROCESSING COMPLETED SUCCESSFULLY!")
print("=================================================")

# Show all images
plt.show()