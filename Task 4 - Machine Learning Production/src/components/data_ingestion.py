# data_ingestion.py

import pandas as pd

def load_data(file_path):
    """
    Load the dataset from a CSV file into a pandas DataFrame.
    
    Parameters:
    - file_path (str): Path to the CSV file containing the dataset.
    
    Returns:
    - df (DataFrame): Loaded dataset as a pandas DataFrame.
    """
    try:
        # Load dataset
        df = pd.read_csv(file_path)
        # print(df)
        return df
    except FileNotFoundError:
        raise FileNotFoundError("File not found. Please provide a valid file path.")
    except Exception as e:
        raise Exception(f"An error occurred while loading the dataset: {str(e)}")
