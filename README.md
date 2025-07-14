
# 🖼️ MNIST Digit Prediction on Custom Image

This project demonstrates how to test a trained Convolutional Neural Network (CNN) model for handwritten digit recognition (MNIST) on a custom grayscale image.  

It loads a trained `mnist_cnn_model.h5` model, processes an input image (`Day7_image_testing.png`), predicts the digit, and visualizes the result with confidence.

---

## 📄 Overview

- Loads a pre-trained Keras CNN model for MNIST digit recognition.
- Preprocesses a custom image to match MNIST format:
  - Resize to 28×28.
  - Invert colors (black digit on white background).
  - Normalize pixel values.
  - Reshape for model input.
- Predicts the digit with confidence score.
- Displays the prediction along with the image using matplotlib.

---

## 🚀 Usage

### 1️⃣ Prerequisites

- Python ≥ 3.6
- Installed packages:
  - `tensorflow`
  - `numpy`
  - `opencv-python`
  - `matplotlib`

Install the dependencies via pip:
```bash
pip install tensorflow numpy opencv-python matplotlib
```

---

### 2️⃣ Input Files

- `mnist_cnn_model.h5` — Pre-trained CNN model trained on the MNIST dataset.
- `Day7_image_testing.png` — Grayscale image of a single handwritten digit.  
  Make sure this image is present in the same directory.

---

### 3️⃣ Run the Script

```bash
python Day7_Image_testing_withmodel.py
```

Sample Output:
```
Predicted Digit: 7, Confidence: 0.98
```

A window will also pop up showing the image with the predicted digit and confidence.

---

## 📂 Project Structure

```
.
├── Day7_Image_testing_withmodel.py   # Main script
├── mnist_cnn_model.h5                # Trained model (not included)
├── Day7_image_testing.png            # Test image (not included)
└── README.md                         # This file
```

---

## 📝 Notes

✅ Ensure the input image is clear, centered, and resembles MNIST-style (28×28 grayscale, white background).  
✅ If you need to train the model yourself, you can use any MNIST CNN training script and save it as `mnist_cnn_model.h5`.

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!  
If you find an issue or have an enhancement in mind:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-xyz`)
3. Commit your changes (`git commit -m 'Add feature xyz'`)
4. Push to the branch (`git push origin feature-xyz`)
5. Open a Pull Request

Let’s collaborate and make it better!

---

## 📜 License

This project is licensed under the MIT License.  
You’re free to use, modify, and distribute it with attribution.

---

## 📚 References

- [MNIST Database](http://yann.lecun.com/exdb/mnist/)
- [Keras Documentation](https://keras.io/)
- [TensorFlow](https://www.tensorflow.org/)

---

## 👨‍💻 Author

Created by **Yash**.  
Feel free to connect and share your thoughts:  
[LinkedIn](https://www.linkedin.com/in/yash-pal-since2004)

---

### 🌟 If you like this project, please ⭐ star the repo and share it!
