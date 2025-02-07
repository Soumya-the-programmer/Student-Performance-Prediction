"""Importing necessary modules
to work seamlessly with data 
preprocessing, feature engineering, 
and model training."""
import pandas as pd


class FeatureEngineer:
    """### Class FeatureEngineer:

    **Purpose:** To apply feature engineering to 
                 required column."""
     
    # class attribute
    _dataframe : pd.DataFrame # to store the dataframe here
       
                 
    def feature_engineering(self, dataframe : pd.DataFrame,
                            category_column : str) -> pd.DataFrame:
        """**Method feature_engineering() that returns pandas DataFrame**
    
        **Purpose:** To apply feature engineering to the dataframe."""
        
         # for checking errors in code
        try:        
            # checking the type first for safety
            if (type(dataframe) == pd.core.frame.DataFrame):
                # calling this method to apply one_hot_encode here
                self.one_hot_encode(dataframe = dataframe,
                                    category_column = category_column)
                
                # returning the applied dataframe
                return self._dataframe
            
            # otherwise showing type error
            else:
                raise TypeError("Error! we only accepts pandas dataframe.")
        
        # for handling type errors in code            
        except TypeError as t:
            print(f"Error message from FeatureEngineer class's feature_engineering() method: {t}")
            
        # for handling errors in code
        except Exception as e:
            print(f"Error message from FeatureEngineer class's feature_engineering() method: {e}")
    
    
    def one_hot_encode(self, dataframe : pd.DataFrame,
                       category_column : str) -> pd.DataFrame:
        """**Method one_hot_encode() that returns pandas DataFrame**
    
        **Purpose:** To apply one-hot-encoding to the dataframe."""
            
        # for checking errors in code
        try:
            # storing the dataframe here
            self._dataframe = dataframe
            # checking column is valid or not
            if (category_column not in self._dataframe):
                # otherwise showing index error
                raise IndexError(f"Error! {category_column} named column doesn't exist inside the dataframe.")
            
            # creating dummy values of that column
            dummy_values = pd.get_dummies(self._dataframe[category_column],  
                                          dtype = int, drop_first = True)
            
            # dropping the original column
            self._dataframe.drop(category_column, axis = "columns", inplace = True)
            
            # adding the dummy column here
            self._dataframe = pd.concat([self._dataframe, dummy_values], axis = 'columns')
            
            # returning the new dataframe
            return self._dataframe
        
        # for handling index errors in code            
        except IndexError as i:
            print(f"Error message from FeatureEngineer class's one_hot_encode() method: {i}")
            
        # for handling errors in code
        except Exception as e:
            print(f"Error message from FeatureEngineer class's one_hot_encode() method: {e}")