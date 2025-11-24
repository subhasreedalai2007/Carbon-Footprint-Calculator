# validation.py

def validate_number(value):
    """Check if the number is valid & positive."""
    try:
        value = float(value)
        if value < 0:
            return None
        return value
    except:
        return None


def validate_diet(diet):
    """Check if diet input is valid."""
    diet = diet.lower()
    return diet if diet in ["veg", "non-veg"] else None