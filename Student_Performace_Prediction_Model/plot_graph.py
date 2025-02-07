"""Importing necessary modules
to work seamlessly with data 
preprocessing, feature engineering, 
and model training."""
import numpy as np
from matplotlib import pyplot as plt
from model_training_and_predict import TrainModelAndPredict


class PlotGraph(TrainModelAndPredict):
    """### Class PlotGraph inherits TrainModelAndPredict class.
    
    **Purpose:** To plot the data points for comparing into graph."""
    
    
    def plot_graph(self) -> None:
        """**Method plot_graph() that returns None.**
        
        **Purpose:** To plot the data points into graph"""
        
        # for checking errors in code
        try:
            # first, reseting the index or dataframe to start with 0
            self._original_dataframe.reset_index(drop = True, inplace = True)
            
            # getting the original price
            original_price = self._original_dataframe.loc[:4, "Performance Index"]
            # getting the predicted price
            predicted_price = self._original_dataframe.loc[:4, "Predicted Performance Index"]
            # getting a sample index
            index = np.arange(5)
            
            # plotting the original price graph
            plt.bar(index - 0.2, original_price, 
                     label = "Original Performance Index", color = "teal", width= 0.4)
            # plotting the predicted price graph
            plt.bar(index + 0.2, predicted_price, 
                     label = "Predicted Performance Index", color = "purple", width= 0.4)
            
            plt.legend(prop = {"weight" : "bold", "size" : 10}) # for showing the graph labels
            plt.xlabel("Sample Index", 
                       fontsize = 18, fontweight = "bold") # for showing x label
            plt.ylabel("Performance Index", 
                       fontsize = 18, fontweight = "bold") # for showing y label
            plt.title("Original Performance Vs. Predicted Performance", 
                      fontsize = 24, fontweight = "bold") # for showing the title
            plt.show() # for showing the graph into screen window
        
        # for handling other errors in code
        except Exception as e:
            print(f"Error message from PlotGraph class's plot_graph() method: {e}")