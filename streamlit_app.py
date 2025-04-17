import streamlit as st
import pandas as pd
from your_script_name import load_data, preprocess_data, assign_samples_with_sub_village

st.title("Household Sampling App")

uploaded_file = st.file_uploader("Upload Excel File", type=["xlsx"])

if uploaded_file:
    try:
        df = load_data(uploaded_file)
        st.success("File uploaded and data loaded successfully!")
        
        df_clean = preprocess_data(df)
        sampled_df = assign_samples_with_sub_village(df_clean)
        
        st.subheader("Sampled Data Preview")
        st.dataframe(sampled_df)

        # Download link
        st.download_button("Download Sampled File", sampled_df.to_excel(index=False), file_name="sampled_output.xlsx")

    except Exception as e:
        st.error(f"Error: {e}")
