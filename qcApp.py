import streamlit as st
import pandas as pd
import great_expectations as ge

def load_data():
    upload = st.file_uploader("Choose the file you wish to QC")
    df = ge.read_csv(upload)
    return df
def main():
    st.title("Test your data expectation by JOSH@I")
    st.subheader("Garbage In Garbage Out")
    data = load_data()
    if st.button("Submit"):
        with st.spinner("Processing"):
            # st.write(data.columns)
            st.write(data)
            st.subheader("Check for uniqueness")
            st.write(data.expect_column_values_to_be_unique(column="ID"))
            st.subheader("Check for integrity")
            activity = ["Summer","Winter"]
            st.write(data.expect_column_values_to_be_in_set('Season',value_set = activity))
            st.subheader("Check for accuracy")
            st.write(data.expect_column_values_to_be_between('Weight',0,500))



if __name__ == "__main__":
    main()