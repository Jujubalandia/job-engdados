import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# app = st.App(title="Data Quality Proj Tap Calculator RD", layout="wide")

st.set_page_config(
    page_title="Data Quality Proj Tap Calculator RD",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.title("Data Quality Proj Tap Calculator RD")

# Define the variables
total_tables = st.slider(
    "Total Number of Tables", min_value=500, max_value=2000, value=1040, step=10
)
data_quality_issues = st.slider(
    "Data Quality Issues", min_value=1000, max_value=10000, value=5654, step=10
)
avg_table_size = st.slider(
    "Average Table Size (GB)", min_value=50, max_value=500, value=100, step=10
)
processing_time = st.slider(
    "Processing Time (hours)", min_value=1.0, max_value=10.0, value=3.75, step=0.25
)
node_count = st.slider(
    "Number of Redshift Nodes", min_value=5, max_value=20, value=10, step=1
)
node_cost = st.slider(
    "Cost per Node-Hour ($)", min_value=0.10, max_value=1.00, value=0.25, step=0.05
)

# Calculate the total processing size
total_processing_size = data_quality_issues * avg_table_size
total_processing_size_tb = total_processing_size / 1024

# Calculate the total cost
total_node_cost = node_count * node_cost * processing_time
total_processing_cost = total_processing_size_tb * 0.25
total_cost = total_node_cost + total_processing_cost

# Display the results
st.write(f"Total Number of Tables: {total_tables}")
st.write(f"Data Quality Issues: {data_quality_issues}")
st.write(f"Average Table Size: {avg_table_size} GB")
st.write(f"Total Processing Size: {total_processing_size_tb:.2f} TB")
st.write(f"Processing Time: {processing_time:.2f} hours")
st.write(f"Number of Redshift Nodes: {node_count}")
st.write(f"Cost per Node-Hour: ${node_cost:.2f}")
st.write(f"Total Node Cost: ${total_node_cost:.2f}")
st.write(f"Total Processing Cost: ${total_processing_cost:.2f}")
st.write(f"Estimated ETL Cost: ${total_cost:.2f}")

# Plot the cost breakdown
labels = ["Node Cost", "Processing Cost"]
values = [total_node_cost, total_processing_cost]
plt.figure(figsize=(8, 6))
plt.pie(values, labels=labels, autopct="%1.1f%%")
plt.title("ETL Cost Breakdown")
plt.axis("equal")
st.pyplot(plt.gcf())
