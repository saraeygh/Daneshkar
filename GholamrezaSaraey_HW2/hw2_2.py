def celsius_to_fahrenheit(degree: int | float) -> float:
    """_summary_

    Args:
        degree (int | float): _description_

    Returns:
        int | float: _description_
    """
    return degree *9/5 + 32

degrees = map(int, input("please input: ").split())
print (list(map(celsius_to_fahrenheit, degrees)))