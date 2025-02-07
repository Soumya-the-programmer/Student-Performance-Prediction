"""Importing necessary modules
to work seamlessly with data 
preprocessing, feature engineering, 
and model training."""
import pandas as pd
from load_data import LoadData


class DataSplit(LoadData):
    """### Class DataSplit inherits LoadData class.

    **purpose**: 
            - To extract the features and labels 
                from the dataset.
            - To split into 80-20 split the dataframe."""
            
    # protected class attribute
    _split_range : int # to store the split range
    # to store the training features and label
    _training_features : pd.DataFrame
    _training_label : pd.DataFrame
    # to store the testing features and label
    _testing_features : pd.DataFrame
    _testing_label : pd.DataFrame
    
    
    def features_label_extraction(self) -> None:
        """**Method features_label_extraction() returns None.**
        
        **Purpose:** To extract the features and label from the dataset."""
        
        # for checking errors in code
        try:
            # extracting the label dataframe here
            self._label = pd.DataFrame(self._dataframe.loc[:, self._label])
            # removing the label from the dataframe
            self._dataframe.drop(self._label.columns, inplace = True, 
                                                axis = 'columns') 
            
            # resetting the index of both features and label
            self._dataframe = self._dataframe.reset_index(drop = True)
            self._label = self._label.reset_index(drop = True)
            
            # calling the data_split() method to split the dataframe
            self.data_split() 
            
        # for handling other errors in code
        except Exception as e:
            print(f"Error message from DataSplit class's features_label_extraction() method: {e}")
        
    
    def data_split(self) -> None:
        """**Method data_split() returns None.**
        
        **Purpose:** To split the dataset into two parts."""
        
        # for checking errors in code
        try:            
            # getting the total rows in preprocessed dataframe
            total_rows = len(list(self._dataframe.index))
            # to get the 80% rows 
            split_range = int(total_rows * (80/100))
            
            # splitting the training features and label 
            self._training_features = self._dataframe.loc[:split_range - 1, :]
            self._training_label = self._label.loc[:split_range - 1, :]
            
            # splitting the testing features and label
            self._testing_features = self._dataframe.loc[split_range:, :]
            self._testing_label = self._label.loc[split_range:, :] 
            
            
            # slicing the original pre-saved dataframe
            self._original_dataframe = self._original_dataframe.loc[split_range:, :]         
        
        # for handling other errors in code
        except Exception as e:
            print(f"Error message from DataSplit class's data_split() method: {e}")
        