# 📚 Student Performance Prediction Model

🚀 **A Machine Learning model to predict student performance using multiple regression and feature engineering.**

## 📌 Project Overview
This project uses **Multiple Linear Regression** to predict student performance based on various academic and extracurricular factors. The model was trained and evaluated using **data preprocessing, feature engineering, and performance metrics**.

📊 **Dataset Source:** [Kaggle - Student Performance Dataset](https://www.kaggle.com/datasets/nikhil7280/student-performance-multiple-linear-regression)

## 🔹 Features
- **Regression Model:** Multiple Linear Regression
- **Feature Engineering:** One-Hot Encoding.
- **Evaluation Metrics:** R² Score
- **Visualization:** Actual vs. Predicted Performance Comparison
- **Structured OOP Implementation:** Modularized code with multiple Python files

## 📊 Model Performance
- **Training Accuracy:** 98.88%
- **Testing Accuracy:** 98.82%

### 📈 Performance Graph
Here’s a visual representation of the model's predictions:

![Actual vs. Predicted Performance](https://github.com/user-attachments/assets/6386c7c0-e9e5-4893-9e7f-bc57a140cac2)


## 📝 Sample Predictions
| Performance Index | Predicted Performance Index |
|------------------|--------------------------|
| 39               | 41                        |
| 80               | 80                        |
| 35               | 35                        |
| 52               | 51                        |
| 34               | 36                        |

## 🛠️ Technologies Used
- **Python** 🐍
- **pandas & NumPy** for data manipulation
- **Scikit-learn** for regression modeling
- **Matplotlib** for data visualization

## 📂 Project Structure
```
├── load_data.py                      # Loads dataset
├── pre_processing.py                 # Cleans & preprocesses data
├── feature_engineering.py            # Encodes categorical data
├── data_splitting.py                 # Split the data into two parts for training and testing
├── model_training_and_predict.py     # Test the model and Predicts new values
├── plot_graph.py                     # Plots graphs & insights
├── main_file.py                      # Runs the entire pipeline
├── Student_Performance.csv           # original dataset
```

## 🚀 How to Run the Project
1. Clone the repository:
   ```bash
   git clone https://github.com/Soumya-the-programmer/Student-Performance-Prediction.git
   ```
2. Install dependencies:
   ```bash
   pip install numpy pandas matplotlib scikit-learn
   ```
3. Run the main script:
   ```bash
   python main_file.py
   ```

## 🤝 Connect With Me

📌 **Star this repo if you find it useful! ⭐**


