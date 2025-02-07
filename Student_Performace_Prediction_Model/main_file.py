"""Importing necessary modules
to work seamlessly with data 
preprocessing, feature engineering, 
and model training."""
import pandas as pd
from plot_graph import PlotGraph


if __name__ == "__main__":
    """### Main function code:

    **pupose:** To control Everything from here."""

    # for checking errors in code
    try:
        # dictionary for storing the values to give for prediction model
        test_data = {
                "Hours Studied": [6, 4, 7, 5, 8],
                "Previous Scores": [85, 60, 90, 50, 95],
                "Extracurricular Activities": ["Yes", "No", "No", "Yes", "No"],
                "Sleep Hours": [7, 5, 6, 4, 7],
                "Sample Question Papers Practiced": [4, 2, 5, 3, 6]
                }

        # creating an instance and passing the required args
        obj = PlotGraph(dataset = "Student_Performance.csv",
                       label = "Performance Index",
                       category_column = "Extracurricular Activities")
        
        # calling this method to extract the features and label from dataframe
        obj.features_label_extraction()
        
        # calling this method to train the model
        obj.train_model()
        
        # calling this method for value prediction
        obj.predict_value(dataframe = pd.DataFrame(test_data),
                          category_column = "Extracurricular Activities")
        
        # for showing the graph on screen 
        obj.plot_graph()
    
    # for handling errors in code
    except Exception as e:
        print(f"Error message from main function(): {e}")