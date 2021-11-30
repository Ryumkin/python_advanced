def check_and_transform_to_complex(func):
    def new_func(*args, **kwargs):
        new_args = []
        for i in args:
            if not isinstance(i, (float, int, Complex)):
                raise TypeError
            if isinstance(i, (float, int)):
                new_args.append(Complex(i))
            else:
                new_args.append(i)
        return func(*new_args, **kwargs)

    return new_func


class Complex:
    # Part 1
    def __init__(self, re=0, im=0):
        if isinstance(re, (float, int)) and isinstance(im, (float, int)):
            self.re = re
            self.im = im
        else:
            raise TypeError

    def __str__(self):
        return f'{self.re}{self.im:+}i'

    # Part 2
    @check_and_transform_to_complex
    def __add__(self, other):
        return Complex(self.re + other.re, self.im + other.im)

    @check_and_transform_to_complex
    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)

    # Part 3
    @check_and_transform_to_complex
    def __mul__(self, other):
        re = self.re*other.re - self.im*other.im
        im = self.re*other.im + self.im*other.re
        return Complex(re, im)

    @check_and_transform_to_complex
    def __truediv__(self, other):
        denominator = other.re ** 2 + other.im ** 2
        re = (self.re * other.re + self.im * other.im)/denominator
        im = (self.im * other.re - self.re * other.im)/denominator
        return Complex(re, im)
