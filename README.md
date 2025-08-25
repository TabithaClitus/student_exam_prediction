App Link:https://studentexamprediction-kh8gbzrjjm9bvafxywu7qp.streamlit.app/

🎓 Student Exam Pass/Fail Prediction using Decision Tree

This project demonstrates how to use a Decision Tree Classifier in Python to predict whether a student will Pass (1) or Fail (0) based on:

📘 Hours Studied

😴 Sleep Hours

🏫 Class Attendance (%)

📂 Dataset

The dataset is a small synthetic set created for demonstration.

Features: hours_studied, sleep_hours, attendance

Target: Pass (1) or Fail (0)

⚙️ Workflow

Import dataset into a Pandas DataFrame.

Split data into training (80%) and testing (20%).

Fit a DecisionTreeClassifier from scikit-learn.

Evaluate the model using:

✅ Accuracy

🎯 Precision

🔄 Recall

📊 F1-score

Visualize the decision tree.

Predict for a new student (example: hours=8, sleep=6, attendance=80%).

📌 Requirements

Python 

pandas

scikit-learn

matplotlib

streamlit

🚀 Future Improvements

Added more features ( assignments).

🚀 Streamlit App

The trained model is saved as exam_model.sav and loaded in a Streamlit frontend.

Run the app:
streamlit run app.py

App Features:

✅ Input student details (hours studied, sleep hours, attendance)

✅ Predict Pass/Fail

✅ Display result interactively

VISUALIZATION:

📊 Pass vs Fail Distribution

The bar chart shows the distribution of students who passed (1) and failed (0) the exam.

Majority of students passed the exam.

A smaller proportion of students failed.

This visualization highlights the overall performance trend in the dataset.

<img width="543" height="450" alt="image" src="https://github.com/user-attachments/assets/9fa4706d-68b2-48b6-a192-08544635dcc3" />

📊 Feature Distributions

The histograms show the distribution of key features in the dataset:

Hours Studied: Most students studied between 7–10 hours, while fewer studied less than 3 hours.

Sleep Hours: The majority of students sleep between 6–8 hours, with some outliers at 4–5 hours.

Class Attendance: Attendance is spread across different ranges, with many students attending between 60–90% of classes.

These distributions help in understanding the spread and variability of input features.

<img width="835" height="565" alt="image" src="https://github.com/user-attachments/assets/3724dcb5-6c97-45a3-b34a-b2e55ee2b738" />

🔍 How It Works

The model was trained using a Decision Tree Classifier on synthetic student performance data.

The app takes user input (hours studied, sleep hours, attendance).

It predicts whether the student will PASS ✅ or FAIL ❌.

The prediction is displayed in a clean UI built with Streamlit.


<img width="1261" height="841" alt="Studend exam prediction" src="https://github.com/user-attachments/assets/5710ed27-3fde-442e-9931-7d76e5379449" />



