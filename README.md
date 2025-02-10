## **📌 Project Title: Student Rank Predictor for NEET Exam**  

### **📃 Project Overview**  
The **Student Rank Predictor** is a **data-driven Machine Learning solution** designed to analyze students' **quiz performance** and predict their **NEET exam rank**. The model utilizes **historical quiz data** and **real-time quiz submissions** to assess **topic-wise strengths, weaknesses, mistake patterns, and rank progression**.  

---

### **🎯 Key Objectives**
✔ **Analyze student quiz performance** based on accuracy, speed, and scores.  
✔ **Identify weak topics & mistake trends** to help students improve.  
✔ **Predict students' NEET rank** using a Machine Learning model.  
✔ **Provide insights on college admission chances** based on rank predictions.  

---

### **📊 Approach & Workflow**
1️⃣ **Data Ingestion:**  
- Collected **current and past quiz data** from APIs.  
- Preprocessed and stored data for further analysis.  

2️⃣ **Data Transformation:**  
- Cleaned & formatted **timestamps, scores, accuracy**, and negative scoring impact.  
- Encoded **categorical data (topics, quiz types, sources, etc.).**  
- Scaled **numerical features** for model training.  

3️⃣ **Exploratory Data Analysis (EDA):**  
- Identified **weak topics**, mistake patterns, and rank progression over time.  
- Analyzed the **relationship between speed & accuracy**.  

4️⃣ **Machine Learning Model:**  
- Trained a **Random Forest Regressor & AdaBoost Regressor** for **rank prediction**.  
- Evaluated model performance using **R² Score, MAE, and RMSE**.  

5️⃣ **Rank Prediction & Insights Generation:**  
- Predicted **students’ expected NEET rank** based on quiz performance.  
- Provided **actionable insights** to improve weak areas.  

6️⃣ **Deployment & API Integration (Optional):** (In Progress)
- Designed a **Flask API** for real-time rank prediction.  
- Hosted the model to make predictions from user input.  

---

### **📌 Key Insights from Analysis**
📌 **Weak Topics:** Identified **Principles of Inheritance, Reproduction, and Respiration** as **difficult topics**.  
📌 **Mistake Patterns:** High **negative scores** indicate frequent errors in certain areas.  
📌 **Speed vs Accuracy Tradeoff:** High-speed attempts led to lower accuracy.  
📌 **Rank Progression:** Some students showed **consistent improvement**, while others had fluctuating ranks.  
📌 **College Admission Estimation:** Predicted rank ranges to **estimate probable college admissions**.  

---

### **🛠️ Technologies Used**
- **Programming Languages:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  
- **Machine Learning Models:** Random Forest, AdaBoost Regressor  
- **Data Processing:** OneHotEncoder, StandardScaler, SimpleImputer  
- **Deployment (Optional):** Flask API for real-time predictions  

---

### **🚀 Project Outcome**
✔ **Built a working rank prediction model** based on quiz performance.  
✔ **Generated actionable insights** to guide students in their preparation.  
✔ **Designed a scalable & modular framework** for future enhancements.  
✔ **Enabled real-time predictions** using a trained ML model.  

---
