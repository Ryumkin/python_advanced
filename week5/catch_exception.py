def exception_logger(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ZeroDivisionError:
            print("ZeroDivisionError")
        except AssertionError:
            print("AssertionError")
        except ArithmeticError:
            print("ArithmeticError")
    return inner
