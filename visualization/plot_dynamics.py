import matplotlib.pyplot as plt
import streamlit as st

def plot_dynamics(dynamics):
    """Plot conversation dominance (dynamics) as a pie chart."""
    labels = list(dynamics.keys())
    sizes = list(dynamics.values())
    
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig)
