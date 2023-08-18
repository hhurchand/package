def is_float(x: float):
    try:
        float(x)
        print("Hello")
        return True
    except ValueError:
        return False