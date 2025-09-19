# File: app.py

import streamlit as st
import pandas as pd
import joblib
import time

# --- Load Model and Initial Setup ---
try:
    model = joblib.load('fraud_model.pkl')
except FileNotFoundError:
    st.error("Model file 'fraud_model.pkl' not found. Please run 'train_model.py' first.")
    st.stop()

st.set_page_config(page_title="Quantum Fraud Detection", layout="wide")
st.title("Quantum-Edge Fraud Detection System Demo 🛰️")

# --- UI for Transaction Input ---
st.sidebar.header("Transaction Input")
st.sidebar.write("Use sliders to simulate a new transaction.")
v17 = st.sidebar.slider("Feature V17", -30.0, 10.0, -0.5, 0.1)
v14 = st.sidebar.slider("Feature V14", -20.0, 12.0, -1.9, 0.1)
v12 = st.sidebar.slider("Feature V12", -20.0, 8.0, 0.8, 0.1)
v10 = st.sidebar.slider("Feature V10", -25.0, 25.0, -0.5, 0.1)

# Create a full feature vector for the model
# Create a full feature vector for the model
feature_values = [0.0] * 30  # <-- THE FIX IS HERE
feature_names = [f'V{i}' for i in range(1, 29)] + ['scaled_amount', 'scaled_time']
feature_values[feature_names.index('V17')] = v17
feature_values[feature_names.index('V14')] = v14
feature_values[feature_names.index('V12')] = v12
feature_values[feature_names.index('V10')] = v10
input_df = pd.DataFrame([feature_values], columns=feature_names)
st.subheader("Live System Log:")
log_placeholder = st.empty()

# --- Simulation Logic ---
if st.sidebar.button("Process Transaction"):
    log_text = ""
    
    # 1. Green Edge Layer Simulation: Performs first-level fraud detection at the edge [cite: 91, 92]
    log_text += "➡️ [EDGE] Transaction received. Running lightweight model for instant screening...\n"
    log_placeholder.info(log_text)
    time.sleep(1)
    
    edge_probabilities = model.predict_proba(input_df)[0]
    fraud_probability = edge_probabilities[1]
    
    # 2. Hybrid Model Logic: Forwards suspicious cases to a deeper module [cite: 52, 58]
    if fraud_probability < 0.3:
        log_text += f"   - Fraud Confidence: {fraud_probability:.2%}\n"
        log_text += "✅ [ACTUATION] Decision: APPROVED. Low risk.\n" # [cite: 144, 146]
        log_placeholder.success(log_text)
    elif fraud_probability > 0.9:
        log_text += f"   - Fraud Confidence: {fraud_probability:.2%}\n"
        log_text += "🚨 [ACTUATION] Decision: BLOCKED. High-confidence fraud detected.\n" # [cite: 144]
        log_placeholder.error(log_text)
    else: 
        log_text += f"   - Fraud Confidence: {fraud_probability:.2%}\n"
        log_text += "⚠️ [EDGE] Suspicious. Forwarding to Quantum Service Layer...\n"
        log_placeholder.warning(log_text)
        time.sleep(1.5)

        # 3. Quantum Service Layer Simulation: Acts as the high-complexity detection engine [cite: 97, 98]
        log_text += "➡️ [QUANTUM] Engaging simulated Quantum module for deep pattern recognition...\n"
        log_placeholder.warning(log_text)
        time.sleep(2.5)
        
        log_text += "🚨 [ACTUATION] Final Verdict: BLOCKED. Subtle anomaly pattern detected by Quantum module.\n"
        log_placeholder.error(log_text)