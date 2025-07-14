# Streamlit ML Model Prediction Tutorial

Welcome to the **Streamlit ML Model Prediction Tutorial**!  
This repository is designed for beginners who want to learn how to build and deploy machine learning model predictions using Python and [Streamlit](https://streamlit.io/).

## Overview

This tutorial walks you through:
- Building a simple machine learning model in Python (using the classic **Iris flower dataset** with scikit-learn)
- Creating an interactive web app with Streamlit to make predictions with your model
- Understanding the basics of model input, output, and UI integration

## Features

- Step-by-step Python code for training a model on the Iris dataset
- Streamlit app for real-time predictions
- Clean and beginner-friendly explanations
- Example dataset included

## Getting Started

### Prerequisites

- Python 3.7+
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/hrishabh-dev/Streamlit_tutorial.git
   cd Streamlit_tutorial
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   # or install manually
   pip install streamlit scikit-learn pandas
   ```

3. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

## Usage

- Open your browser and go to the local URL provided by Streamlit
- Input sample flower features (Sepal/Petal length and width)
- Click "Predict" to see the model's prediction of the Iris species in real time

## Folder Structure

```
Streamlit_tutorial/
├── app.py                 # Main Streamlit app
├── model.py               # ML model code (Iris flower dataset)
├── requirements.txt       # Python dependencies
├── data/                  # Example datasets
└── README.md              # This file
```

## Learn More

- [Streamlit Documentation](https://docs.streamlit.io/)
- [scikit-learn Documentation](https://scikit-learn.org/)
- [Python Official Site](https://www.python.org/)
- [Iris Dataset Info (UCI ML Repository)](https://archive.ics.uci.edu/ml/datasets/iris)

## Contributing

Pull requests and suggestions are welcome!  
If you find something confusing or have ideas for improvement, feel free to open an issue.

## License

This project is licensed under the MIT License.

---

Happy learning and building with Streamlit and ML! 🚀
