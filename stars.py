import numpy as np 
import matplotlib.pyplot as plt
from skimage.morphology import (binary_erosion, binary_dilation, binary_closing, binary_opening)
from skimage.measure import label 

stars=np.load("stars.npy")

star_mask=np.array([[1, 0, 0, 0, 1],
                    [0, 1, 0, 1, 0],
                    [0, 0, 1, 0, 0],
                    [0, 1, 0, 1, 0],
                    [1, 0, 0, 0, 1]])
cross_mask=np.array([[0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0],
                    [1, 1, 1, 1, 1],
                    [0, 0, 1, 0, 0],
                    [0, 0, 1, 0, 0]])
stars_new=(binary_erosion(stars,star_mask))
labeled=label(stars_new)
num_components = np.max(labeled)
print(f"количество крестов {num_components}")
cross_new=(binary_erosion(stars,cross_mask))
labeled1=label(cross_new)
num_components1 = np.max(labeled1)
print(f"количество плюсов {num_components1}")
print((f"количество звездочек {num_components+num_components1}"))
plt.imshow (stars)
plt.show()
