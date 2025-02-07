"""Importing necessary modules
to work seamlessly with data 
preprocessing, feature engineering, 
and model training."""
import pandas as pd
from pre_processing import DataPreProcessing


class LoadData:
    """### Class LoadData
    
    Purpose: To load the dataset here."""
    
    # protected class attributes
    """saving original dataframe here, 
    to insert the csv file as output"""
    _original_dataframe : pd.DataFrame 
    """here storing the dataframe that 
    will be modified in operation"""
    _dataframe : pd.DataFrame 
    _label : str # to store the label string
    _category_column : str # to store the string featured column here
    
    
    def __init__(self, dataset : str,
                 category_column : str, 
                 label : str) -> None:
        """**init() constructor that returns None.** 
    
        **Purpose:** to take the required arguments from 
        the main function()."""
        # for checking errors in code
        try:
            # first checking that it is a csv file or not
            if (dataset.endswith(".csv")):
                # creating instance of DataPreProcessing class
                obj = DataPreProcessing()
                
                # reading the csv file as pandas dataframe and storing into class attribute
                self._dataframe = pd.read_csv(dataset)
                    
                """checking the label exist in dataframe or not"""
                if (label not in self._dataframe.columns):
                    # otherwise raising Index error
                    raise IndexError(f"Error! {label} named column doesn't exist in the dataframe.")
                
                """checking the string featured column exist or not"""
                if (category_column not in self._dataframe.columns):
                    # otherwise raising Index error
                    raise IndexError(f"Error! {category_column} named column doesn't exist in the dataframe.")
                
                """if condition satisfies then storing
                features and label into corresponding attributes"""
                self._label = label
                self._category_column = category_column
                
                # showing as an acknoledgement
                print("\nDataset has loaded succesfully into pandas dataframe!")
                
                # calling this method for pre process the dataframe
                self._dataframe = obj.data_preprocessing(dataframe = self._dataframe,
                                                         category_column = self._category_column)
                
                # creating a copy of original unchanged dataframe
                self._original_dataframe = self._dataframe.copy()
                
                # reseting the index of unchanged dataframe
                self._original_dataframe = self._original_dataframe.reset_index()
                
                # showing for an acknowledgement
                print("\nDataframe has Preprocessed successfully!")
            
            # otherwise raising error here    
            else:
                raise TypeError(f"Error! LoadData class only accepts .csv file.")
                
        # for handling index errors in code
        except IndexError as i:
            print(f"Error message from LoadData class's init() constructor: {i}")
        
        # for handling type errors in code
        except TypeError as t:
            print(f"Error message from LoadData class's init() constructor: {t}")
        
        # for handling other errors in code
        except Exception as e:
            print(f"Error message from LoadData class's init() constructor: {e}")