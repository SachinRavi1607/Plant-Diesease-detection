import numpy as np
import matplotlib.pyplot as plt

# Example RGB 50x50 array
image = np.ones((50, 50, 3), dtype="uint8") * [255, 0, 0]  # Red color

# Display the image
plt.imshow(image)
plt.axis("off")  # Hide axes
plt.show()
