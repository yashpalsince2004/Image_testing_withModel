import cv2
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model

# ✅ Load trained model
model = load_model("mnist_cnn_model.h5")

# ✅ Load and preprocess the input image
img = cv2.imread("Day7_image_testing.png", cv2.IMREAD_GRAYSCALE)
img_resized = cv2.resize(img, (28, 28))  # Resize to MNIST size
img_inverted = 255 - img_resized         # Invert: black digit on white
img_norm = img_inverted / 255.0          # Normalize 0–1
img_input = img_norm.reshape(1, 28, 28, 1)  # Reshape for model

# ✅ Predict
pred = model.predict(img_input)
predicted_digit = np.argmax(pred)
confidence = np.max(pred)
print(f"Predicted Digit: {predicted_digit}, Confidence: {confidence:.2f}")

# ✅ Visualization using matplotlib
plt.figure(figsize=(4, 4))
plt.imshow(img_resized, cmap='gray')
plt.title(f"Predicted Digit: {predicted_digit} (Confidence: {confidence:.2f})")
plt.axis('off')
plt.show()
