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
