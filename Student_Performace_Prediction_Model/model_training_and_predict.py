"""Importing necessary modules
to work seamlessly with data 
preprocessing, feature engineering, 
and model training."""
import pandas as pd
from sklearn import linear_model
from data_splitting import DataSplit
from pre_processing import DataPreProcessing


class TrainModelAndPredict(DataSplit):
    """### Class TrainModelAndPredict inherits DataSplit class.
    
    **Purpose:** 
                - To train the model here.
                - To predict the values."""
    
    # creating private instance of LinearRegression class
    __multi_linear_regression = linear_model.LinearRegression()
    
    # to store the dataframe here
    _df : pd.DataFrame
     
                
    def train_model(self) -> None:
        """**Method train_model() returns None.**
        
        **Purpose:** To train the model here."""
        
        # for checking errors in code
        try:
            # fitting the model with training features and label
            self.__multi_linear_regression.fit(self._training_features, self._training_label)
            
            # showing for an acknowledgement
            print("\nModel has trained succesfully!")
            
            # printing model's training score
            print(f"\nModel Training score: {self.__multi_linear_regression.score(self._training_features, 
                  self._training_label) * 100:.2f} %")
            
            # printing model's training score
            print(f"\nModel Testing score: {self.__multi_linear_regression.score(self._testing_features, 
                  self._testing_label) * 100:.2f} %")
        
        # for handling other errors in code
        except Exception as e:
            print(f"Error message from TrainModelAndPredict class's train_model() method: {e}")
            
            
    def predict_value(self, dataframe : pd.DataFrame,
                      category_column : str) -> None:
        """**Method predict_value() returns None.**
        
        **Purpose:** To predict the value and paste into a csv file."""
        
        # for checking errors in code
        try:
            # storing the original given dataframe here
            original_df : pd.DataFrame
            
            # creating object of DataPreprocessing class
            obj = DataPreProcessing()
            
            """Predicting for the 20% testing data"""
            # passing the testing features to the model for prediction
            predicted_output = self.__multi_linear_regression.predict(self._testing_features)
            
            # storing new predicted_ouput as a column
            self._original_dataframe["Predicted Performance Index"] = predicted_output
            # changing the datatype to int for better visualization
            self._original_dataframe["Predicted Performance Index"] = self._original_dataframe["Predicted Performance Index"].astype(int)
            # saving into csv file
            self._original_dataframe.to_csv("Model_Testing.csv", index = False)
            """Prediction for 20% testing data ended"""
            
            
            """Predicting for new given data"""
            # type checking of given dataframe
            if (type(dataframe) == pd.core.frame.DataFrame):
                # storing the dataframe into class variable
                self._df = dataframe
                original_df = dataframe.copy() # storing here for pasting into csv file
                
                # checking the category column exist or not
                if (category_column not in self._df.columns):
                    # raising index error
                    raise IndexError(f"Error! {category_column} not exist in given dataframe.")
                
                # calling this method for pre_process the dataframe before giving to predict() method
                self._df = obj.data_preprocessing(dataframe = self._df, 
                                       category_column = category_column)
                
                # storing the predicted_output here
                predicted_output = self.__multi_linear_regression.predict(self._df)
                
                # storing the predicted output into original given dataframe
                original_df["Predicted Performance Index"] = predicted_output
                
                # changing the datatype to integer for better readability
                original_df["Predicted Performance Index"] = original_df["Predicted Performance Index"].astype(int)
                
                # storing the predicted output into csv file
                original_df.to_csv("Predicted_Ouput.csv", index = False)
                
                # showing for an acknowledgement
                print("\nModel has successfully predicted the given values.\n-> You can check them in the folder with \"Predicted_Ouput.csv\" named file.")
                
        # for handling index errors in code
        except IndexError as i:
            print(f"Error message from TrainModelAndPredict class's predict_value() method: {i}")
        
        # for handling other errors in code
        except Exception as e:
            print(f"Error message from TrainModelAndPredict class's predict_value() method: {e}")