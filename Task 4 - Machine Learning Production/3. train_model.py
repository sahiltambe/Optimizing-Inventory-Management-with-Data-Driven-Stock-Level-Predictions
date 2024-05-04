# train_model.py

# Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import StandardScaler

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
        return df
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return None
    except Exception as e:
        print(f"An error occurred while loading the dataset: {str(e)}")
        return None

def train_model(df, k=10, split=0.75):
    """
    Train a Random Forest Regressor model on the provided dataset using K-fold cross-validation.
    
    Parameters:
    - df (DataFrame): Dataset containing the features and target variable.
    - k (int): Number of folds for cross-validation.
    - split (float): Proportion of data to include in the training split.
    
    Returns:
    - None
    """
    try:
        # Initialize list to store MAE for each fold
        accuracy = []
        
        for fold in range(k):
            # Split data into features (X) and target variable (y)
            X = df.drop(columns=['estimated_stock_pct'])
            y = df['estimated_stock_pct']
            
            # Instantiate algorithm and scaler
            model = RandomForestRegressor()
            scaler = StandardScaler()

            # Create training and test samples
            X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=split, random_state=42)

            # Scale X data
            scaler.fit(X_train)
            X_train = scaler.transform(X_train)
            X_test = scaler.transform(X_test)

            # Train model
            trained_model = model.fit(X_train, y_train)

            # Generate predictions on test sample
            y_pred = trained_model.predict(X_test)

            # Compute accuracy, using mean absolute error
            mae = mean_absolute_error(y_true=y_test, y_pred=y_pred)
            accuracy.append(mae)
            print(f"Fold {fold + 1}: MAE = {mae:.3f}")

        # Print average MAE across all folds
        print(f"Average MAE: {(sum(accuracy) / len(accuracy)):.3f}")
        
    except Exception as e:
        print(f"An error occurred while training the model: {str(e)}")

def main():
    # Path to the CSV file containing the dataset
    file_path = 'final_dataset.csv'
    
    # Load data
    df = load_data(file_path)
    if df is None:
        return
    
    # Train model with K-fold cross-validation
    train_model(df)

if __name__ == "__main__":
    main()
