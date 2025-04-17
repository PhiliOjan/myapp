import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import logging
import os

# Setup logging (optional for debugging)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Your functions here (same as you already have) ---
# Paste load_data, preprocess_data, get_sample_size, 
# proportional_sample_within_village, assign_samples_with_sub_village

# Streamlit App
def main():
    st.title("📊 Household Sampling Tool")

    uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])

    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            st.success("✅ Data uploaded successfully.")

            # Show a preview of uploaded data
            st.subheader("📋 Raw Data Preview")
            st.dataframe(df.head())

            # Preprocess and sample
            df_clean = preprocess_data(df)
            final_sample = assign_samples_with_sub_village(df_clean)

            if not final_sample.empty:
                st.success("✅ Sampling completed.")

                # Display sample preview
                st.subheader("📋 Sampled Data Preview")
                st.dataframe(final_sample.head())

                # Download button
                st.download_button(
                    label="📥 Download Sampled Excel",
                    data=final_sample.to_excel(index=False, engine='openpyxl'),
                    file_name="Randomized_Sample.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )
            else:
                st.warning("⚠️ Sampling resulted in an empty dataset.")
        except Exception as e:
            st.error(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
