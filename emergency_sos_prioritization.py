import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

def perform_data_analysis():
    try:
        # Sample dataset for emergency SOS prioritization (example data)
        X = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]])
        y = np.array([0, 0, 1, 1, 1])

        # Split the dataset into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train the SVM model for emergency SOS prioritization
        model = SVC(kernel='linear')
        model.fit(X_train, y_train)

        # Example usage to prioritize emergency SOS based on input data
        input_data = np.array([[4, 5]])  # Example input data for emergency situation
        priority = model.predict(input_data)

        # Print the prioritization result
        if priority == 0:
            print("Low priority for emergency SOS.")
        elif priority == 1:
            print("High priority for emergency SOS.")

    except Exception as e:
        print(f"Error occurred during data analysis: {e}")

if __name__ == '__main__':
    perform_data_analysis()
