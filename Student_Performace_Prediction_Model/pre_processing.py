"""Importing necessary modules
to work seamlessly with data 
preprocessing, feature engineering, 
and model training."""
import pandas as pd
from feature_engineering import FeatureEngineer


class DataPreProcessing:
    """### Class DataPreProcessing:

    **Purpose:** To preprocess the dataframe by removing null 
         and duplicate rows."""
    
    # class attributes
    _dataframe : pd.DataFrame # to store the dataframe here    


    def data_preprocessing(self, dataframe : pd.DataFrame, 
                           category_column : str) -> pd.DataFrame:
        """**Method data_preprocessing() that returns pandas DataFrame**
    
        **Purpose:** we checking if there any null values, 
                     or any duplicate values."""
                     
        # for checking errors in code
        try:
            # creating instance of FeatureEngineer class
            obj = FeatureEngineer()
            
            # first, type checking for safety
            if (type(dataframe) == pd.core.frame.DataFrame): 
                # assigining the dataframe into class attribute
                self._dataframe = dataframe           
                # calling this method to remove null values
                self.remove_null_values()
                # calling this method to remove duplicate values
                self.remove_duplicate_values()
                
                # calling this method to apply feature engineering in the dataframe
                self._dataframe = obj.feature_engineering(dataframe = self._dataframe,
                                                          category_column = category_column)
                
                # returning the modified dataframe
                return self._dataframe
                
            # otherwise raising type error
            else:
                raise TypeError("Error! we only accepts pandas dataframe.")
        
        # for handling type errors in code            
        except TypeError as t:
            print(f"Error message from DataPreProcessing class's data_preprocessing() method: {t}")
            
        # for handling errors in code
        except Exception as e:
            print(f"Error message from DataPreProcessing class's data_preprocessing() method: {e}")
            
         
    def remove_null_values(self) -> None:
        """**Method remove_null_values() that returns None**
    
        **Purpose:** we checking if there any null values, 
                     then we will remove directly as there 
                     are 10000+ rows"""
                     
        # for checking errors in code
        try:           
            # checking for null values
            if (self._dataframe.isnull().values.any()):
                # dropping the null values by keeping only first value
                self._dataframe.dropna(inplace = True)
                    
        # for handling errors in code
        except Exception as e:
            print(f"Error message from DataPreProcessing class's remove_null_values() method: {e}")
            
            
    def remove_duplicate_values(self) -> None:
        """**Method remove_duplicate_values() that returns None**
    
        **Purpose:** we checking if there any duplicate 
                    values, then we will delete them, 
                    otherwise they will lead to wrong output."""
                     
        # for checking errors in code
        try:
            # checking for duplicate values
            if (self._dataframe.duplicated().values.any()):
                # dropping the null values by keeping only first value
                self._dataframe.drop_duplicates(keep = "first", inplace = True)
                    
        # for handling errors in code
        except Exception as e:
            print(f"Error message from DataPreProcessing class's remove_duplicate_values() method: {e}")  