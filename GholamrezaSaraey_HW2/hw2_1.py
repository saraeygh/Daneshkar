#!/usr/bin/python3
# Released under GPLv3+ License, 2022.

def is_valid_zip_code(zip_code: str) -> bool:
    """check if zip code is valid.

    Args:
        zip_code (str): zip code string

    Returns:
        bool: valid of not
    """
    return(
        isinstance(zip_code, str)
        and len(zip_code) == 11 
        and zip_code[5] == "-" 
        and zip_code[:5].isdigit() 
        and zip_code[6:].isdigit()
        )

zip_codes = [ 
    "1235-hello", 
    "123$5-12345",
    "1234512345",
    "123.5-12345",
    "12345-54321"
]

print(list(filter(is_valid_zip_code, zip_codes)))