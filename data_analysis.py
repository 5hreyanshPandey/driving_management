'''import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

def perform_data_analysis():
    try:
        # Sample dataset for data analysis (example data)
        data = {
            'hours_driven': [1, 2, 3, 4, 5],
            'driver_fatigue_score': [3, 4, 6, 8, 9]
        }
        df = pd.DataFrame(data)

        # Perform linear regression for data analysis
        X = df[['hours_driven']]
        y = df['driver_fatigue_score']
        model = LinearRegression()
        model.fit(X, y)

        # Generate predictions based on the linear regression model
        y_pred = model.predict(X)

        # Visualize the data and regression line
        plt.scatter(X, y, color='blue')
        plt.plot(X, y_pred, color='red')
        plt.xlabel('Hours Driven')
        plt.ylabel('Driver Fatigue Score')
        plt.title('Driver Fatigue Analysis')
        plt.show()

    except Exception as e:
        print(f"Error occurred during data analysis: {e}")

if __name__ == '__main__':
    perform_data_analysis()
'''
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

def perform_data_analysis():
    try:
        # Generate a sample dataset for data analysis
        hours_driven = np.array([1, 2, 3, 4, 5])
        driver_fatigue_score = np.array([3, 4, 6, 8, 9])
        df = pd.DataFrame({'hours_driven': hours_driven, 'driver_fatigue_score': driver_fatigue_score})

        # Perform linear regression for data analysis
        X = df[['hours_driven']]
        y = df['driver_fatigue_score']
        model = LinearRegression()
        model.fit(X, y)

        # Generate predictions based on the linear regression model
        y_pred = model.predict(X)

        # Visualize the data and regression line
        plt.scatter(X, y, color='blue')
        plt.plot(X, y_pred, color='red')
        plt.xlabel('Hours Driven')
        plt.ylabel('Driver Fatigue Score')
        plt.title('Driver Fatigue Analysis')
        plt.show()

    except Exception as e:
        print(f"Error occurred during data analysis: {e}")

if __name__ == '__main__':
    perform_data_analysis()
