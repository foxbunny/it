class It:
    __instance__ = None

    def __new__(class_, *args, **kwargs):
        if class_.__instance__ is None:
            class_.__instance__ = object.__new__(class_, *args, **kwargs)
        return class_.__instance__

    def __eq__(self, x):
        return lambda y: y == x

    def __ne__(self, x):
        return lambda y: y != x

    def __lt__(self, x):
        return lambda y: y < x

    def __gt__(self, x):
        return lambda y: y > x

    def __le__(self, x):
        return lambda y: y <= x

    def __ge__(self, x):
        return lambda y: y >= x

    def __getattr__(self, name):
        return lambda x: getattr(x, name)

    def __call__(self, *args, **kwargs):
        return lambda fn: fn(*args, **kwargs)

    def __getitem__(self, key):
        return lambda x: x[key]

    def __add__(self, x):
        return lambda y: y + x

    def __radd__(self, x):
        return lambda y: x + y

    def __sub__(self, x):
        return lambda y: y - x

    def __rsub__(self, x):
        return lambda y: x - y

    def __mul__(self, x):
        return lambda y: y * x

    def __rmul__(self, x):
        return lambda y: x * y

    def __matmul__(self, x):
        return lambda y: y @ x

    def __rmatmul__(self, x):
        return lambda y: x @ y

    def __truediv__(self, x):
        return lambda y: y / x

    def __rtruediv__(self, x):
        return lambda y: x / y

    def __floordiv__(self, x):
        return lambda y: y // x

    def __rfloordiv__(self, x):
        return lambda y: x // y

    def __mod__(self, x):
        return lambda y: y % x

    def __rmod__(self, x):
        return lambda y: x % y

    def __divmod__(self, x):
        return lambda y: divmod(y, x)

    def __rdivmod__(self, x):
        return lambda y: divmod(x, y)

    def __pow__(self, x, modulo=None):
        return lambda y: pow(y, x, modulo)

    def __rpow__(self, x):
        return lambda y: pow(x, y)

    def __lshift__(self, x):
        return lambda y: y << x

    def __rlshift__(self, x):
        return lambda y: x << y

    def __rshift__(self, x):
        return lambda y: y >> x

    def __rrshift__(self, x):
        return lambda y: x >> y

    def __and__(self, x):
        return lambda y: y & x

    def __rand__(self, x):
        return lambda y: x & y

    def __xor__(self, x):
        return lambda y: y ^ x

    def __rxor__(self, x):
        return lambda y: x ^ y

    def __or__(self, x):
        return lambda y: y | x

    def __ror__(self, x):
        return lambda y: x | y

    def __neg__(self):
        return lambda x: -x

    def __pos__(self):
        return lambda x: +x

    def __invert__(self):
        return lambda x: ~x


it = It()
