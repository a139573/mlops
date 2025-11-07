import math

# • Removal of missing values
# o Input: List of values, including missing values like None, '' and NaN
# o Output: List of values with the missing ones removed
def remove_missing_values(values):
    filtered_values = []
    for value in values:
        if value is None or value == '' or math.isnan(value):
            continue
        filtered_values.append(value)
    return filtered_values


# • Filling missing values
# o Inputs:
#   ▪ List of values, including missing values
#   ▪ The value to fill the missing values (default to 0)
# o Output: List of values where the missing values are replaced with the given filling value
def fill_missing_values(values, filling_value=0):
    filled_values = []
    for value in values:
        if value is None or value == '' or math.isnan(value):
            filled_values.append(filling_value)
        else:
            filled_values.append(value)
    return filled_values




# • Removal of duplicated values
# o Input: List of values
# o Output: List of unique values
def remove_duplicates(values):
    unique_values_set = set(values)
    unique_values = [value for value in unique_values_set] 
    return unique_values


# • Normalization of numerical values using the min-max method
# o Inputs:
# ▪ List of numerical values
# ▪ New minimum (default to 0.0)
# ▪ New maximum (default to 1.0)
# o Output: list of normalized values
def normalize_values(values, new_min=0.0, new_max=1.0):
    normalized_values = [(value - new_min) / (new_max - new_min) for value in values]  
    return normalized_values

# import numpy as np
# • Standardization of numerical values using the z-score method
# o Input: List of numerical values
# o Output: List of standardized values
def standardize_values(values):
    mean = sum(values) / len(values)
    std = (sum([(value - mean) ** 2 for value in values]) / len(values)) ** 0.5
    standardized_values = [(value - mean) / std for value in values]
    return standardized_values  


# • Clipping numerical values to a certain range
# o Inputs:
# ▪ List of numerical values
# ▪ Minimum value to clip
# ▪ Maximum value to clip
# o Output: List of clipped values
def clip_values(values, min_value, max_value):
    clipped_values = []
    for value in values:
        if value < min_value:
            clipped_values.append(min_value)
        elif value > max_value:
            clipped_values.append(max_value)
        else:
            clipped_values.append(value)
    return clipped_values


# • Conversion of values to integers
# o Input: List of strings (it can include both numerical and non-numerical
# values)
# o Output: List of values converted to integers (non-numerical values are
# excluded from the output)
def convert_to_int(strings):
    values = []
    for string in strings:
        try:
            values.append(int(string))
        except (ValueError, TypeError):
            continue
    return values


# • Logarithmic scale transformation
# o Input: List of values
# o Output: List of values converted to logarithmic scale (just the original
# positive numbers)
def log_transform(values): 
    log_values = [math.log(value) for value in values if value > 0] 
    return log_values


import re
# • Tokenization of text into words, selecting only alphanumeric characters and lowercasing words
# o Input: Text to be processed
# o Output: Processed text
def tokenize_text(text):
    text = text.lower()
    tokens = re.findall(r'\b[\w]+\b', text)
    return tokens


# • Selection of alphanumerical characters and spaces
# o Input: Text to be processed
# o Output: Processed text

def keep_alphanumeric_and_spaces(text):
    text = text.lower()
    cleaned = re.sub(r'[^a-z0-9\s]', '', text)
    return cleaned



# • Removal of stop-words from text (it should be lower-cased)
# o Inputs
# ▪ Text to be processed
# ▪ Stop words to be removed
# o Output: Processed text
def remove_stopwords(text, stopwords):
    processed_text =[word for word in text if word not in stopwords] 
    return processed_text


# #
# #import numpy as np
# • Flatten a list of lists
# o Input: A list of lists
# o Output: A flattened list
def flatten_lists(lists):
    flattened_list = [element for individual_list in lists for element in individual_list]
    return flattened_list



import random
# • Random shuffling of a list of values
# o Inputs
# ▪ List of values
# ▪ Seed to ensure reproducibility
# o Output: list of shuffled values
def shuffle_list(list_values, seed=123):
    random.seed(seed)
    shuffled = list_values.copy()
    random.shuffle(shuffled)
    return shuffled