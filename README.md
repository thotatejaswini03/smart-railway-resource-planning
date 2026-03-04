# 🚆 Smart Railway Resource Planning System

## 📌 Overview

Railway systems handle thousands of trains, platforms, and passengers every day. Manual planning often leads to inefficient resource allocation, overcrowding, and delays.

The **Smart Railway Resource Planning System** is a data-driven dashboard that helps railway planners make better operational decisions using historical data and machine learning.

This system predicts passenger demand, detects overcrowding risks, analyzes platform usage, and recommends resource allocation improvements.

---

## 🎯 Problem Statement

Railways move millions of passengers daily, but planning train schedules, platform allocation, and coach capacity is complex.

Challenges include:

* Overcrowded trains during peak hours
* Underutilized trains during low demand
* Platform congestion
* Lack of data-driven planning

This project provides a **smart planning dashboard** that helps optimize railway resources using analytics and machine learning.

---

## 🚀 Key Features

### 📊 Passenger Demand Prediction

Predicts future passenger demand using a **Machine Learning model (Random Forest)**.

### 🚨 Overcrowding Risk Detection

Detects trains likely to exceed capacity and alerts planners.

### 🚉 Platform Utilization Analysis

Analyzes which platforms are most congested.

### 🔥 Peak Travel Time Detection

Identifies hours with the highest passenger demand.

### 🧠 AI Operational Alerts

Automatically detects potential operational issues such as overcrowded trains.

### 🏆 Route Popularity Ranking

Ranks routes by passenger demand to identify high-traffic corridors.

### 📈 Interactive Dashboard

A user-friendly **Streamlit dashboard** that visualizes all insights for planners.

---

## 🛠️ Tech Stack

| Component            | Technology        |
| -------------------- | ----------------- |
| Programming Language | Python            |
| Data Processing      | Pandas, NumPy     |
| Machine Learning     | Scikit-learn      |
| Visualization        | Plotly            |
| Dashboard            | Streamlit         |
| Dataset              | Synthetic Dataset |
| Model Storage        | Joblib            |

---

## 📂 Project Structure

```
smart-railway-resource-planning
│
├── app
│   └── dashboard.py
│
├── src
│   ├── __init__.py
│   ├── data_generator.py
│   ├── train_model.py
│   └── recommendation.py
│
├── data
│   └── railway_data.csv
│
├── models
│   └── demand_model.pkl
│
├── requirements.txt
└── README.md
```

---

## 📊 Dataset

A **synthetic railway dataset** was generated for this project.

Example fields:

* Train ID
* Source
* Destination
* Date
* Time
* Passenger Count
* Number of Coaches
* Platform Number
* Delay
* Holiday Indicator

Synthetic data allows realistic simulation of railway operations without using confidential data.

---

## 🤖 Machine Learning Model

The system uses a **Random Forest Regressor** to predict passenger demand.

### Input Features

* Day of week
* Month
* Route
* Holiday indicator

### Output

* Predicted passenger demand

This prediction helps determine whether additional coaches are required.

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/thotatejaswini03/smart-railway-resource-planning.git
```

Move into the project directory:

```
cd smart-railway-resource-planning
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Step 1 — Generate Dataset

```
python src/data_generator.py
```

### Step 2 — Train Model

```
python src/train_model.py
```

### Step 3 — Launch Dashboard

```
streamlit run app/dashboard.py
```

Open the browser:

```
http://localhost:8501
```

---

## 📷 Dashboard Preview

Main features include:

* Demand prediction panel
* Route demand visualization
* Peak travel detection
* Platform congestion analysis
* AI operational alerts

---

## 💡 Example Insight

Example system recommendation:

> "Delhi–Jaipur route experiences high passenger demand during weekends. The system recommends adding 2–3 additional coaches for evening departures."

---

## 🔮 Future Improvements

* Real-time railway API integration
* Train delay prediction model
* AI-based schedule optimization
* Railway network visualization using maps
* Reinforcement learning for train scheduling

---

## 📜 License

This project is created for educational and hackathon purposes.

---

## 👨‍💻 Author

Developed by Thota Tejaswini as part of the **Smart Railway Resource Planning Hackathon**.
