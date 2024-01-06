import streamlit as st
import pandas as pd
import great_expectations as ge

def load_data():
    upload = st.file_uploader("Choose the file you wish to QC")
    df = ge.read_csv(upload)
    return df
def main():
    st.title("Test youre expectation by JOSH@I")
    st.subheader("Garbage In Garbage Out")
    data = load_data()
    if st.button("Submit"):
        with st.spinner("Processing"):
            st.write(data.columns)
            st.subheader("Check for uniqueness")
            st.write(data.expect_column_values_to_be_unique(column="ID"))


if __name__ == "__main__":
    main()