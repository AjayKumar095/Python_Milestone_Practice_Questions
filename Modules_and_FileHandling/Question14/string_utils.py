
def lowercase(string:str)->str:
    """_summary_  Convert the given string into lowercase.

    Args:
        string (str): Any string value

    Returns:
        str: lowercase string.
    """
    try:
       return string.lower()
    except Exception as e:
        return e
    
def uppercase(string:str)->str:
    """_summary_  Convert the given string into uppercase.

    Args:
        string (str): Any string value

    Returns:
        str: uppercase string.
    """
    try:
       return string.upper()
    except Exception as e:
        return e
    
def capitalizing(string:str)->str:    
    """_summary_  Convert the given string into capitalizing string.

    Args:
        string (str): Any string value

    Returns:
        str: capitalizing the string.
    """
    try:
       return string.capitalize()
    except Exception as e:
        return e    
    
    
def reversing(string:str)->str:    
    """_summary_  Convert the given string into reversing string.

    Args:
        string (str): Any string value

    Returns:
        str: reverse the string.
    """
    try:
       return string[::-1]
    except Exception as e:
        return e        