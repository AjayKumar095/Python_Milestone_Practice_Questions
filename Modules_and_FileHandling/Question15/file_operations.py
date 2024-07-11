
def read(filepath:str):
    """_summary_ function to read from a text file.

    Args:
        filepath (str): file path 

    Returns:
        str: test data form the file
    """
    try:
        with open(file=filepath, mode='r') as file:
            content=file.read()
            return content
    except Exception as e:
        return e    
    
def write(filepath:str, text:str):
    """_summary_ function to write in a text file.

    Args:
        filepath (str): file path 

    Returns:
        str: none
    """
    try:
        with open(file=filepath, mode='w') as file:
            file.write(text)
            return 'Content added'
    except Exception as e:
        return e    
    
def appending(filepath:str, text:str):
    """_summary_ function to append new data in a text file.

    Args:
        filepath (str): file path 

    Returns:
        str: none
    """
    try:
        with open(file=filepath, mode='+a') as file:
            file.write(text)
            return 'Content added'
    except Exception as e:
        return e    
    