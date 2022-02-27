import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread("data/barricade/JPEGImages/train_144.jpg")
print(img.shape)

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()
