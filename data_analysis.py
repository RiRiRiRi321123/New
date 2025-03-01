import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
def load_dataset(file_path):
    """
    Load a dataset from a CSV file.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The loaded dataset.
    """
    try:
        data = pd.read_csv(file_path)
        print("Dataset loaded successfully.")
        return data
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None

# Display summary statistics
def display_summary_statistics(data):
    """
    Display summary statistics of the dataset.

    Parameters:
    data (pd.DataFrame): The dataset.

    Returns:
    None
    """
    print("Summary Statistics:")
    print(data.describe())

# Visualize data
def visualize_data(data, column_name):
    """
    Visualize data by plotting a histogram of a specified column.

    Parameters:
    data (pd.DataFrame): The dataset.
    column_name (str): The name of the column to visualize.

    Returns:
    None
    """
    try:
        plt.figure(figsize=(10, 6))
        data[column_name].hist()
        plt.title(f'Histogram of {column_name}')
        plt.xlabel(column_name)
        plt.ylabel('Frequency')
        plt.show()
    except Exception as e:
        print(f"Error visualizing data: {e}")

def main():
    # File path to the dataset
    file_path = 'your_dataset.csv'

    # Load the dataset
    data = load_dataset(file_path)

    if data is not None:
        # Display summary statistics
        display_summary_statistics(data)

        # Visualize data (example: visualize the 'age' column)
        visualize_data(data, 'age')

if __name__ == "__main__":
    main()