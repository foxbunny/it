from it import it


def test_equals():
    eq = it == 5
    assert eq(5), "5 equals 5"
    assert not eq(4), "4 does not equal 5"


def test_it_less_than():
    lt = it < 5
    assert lt(4), "4 is less than 5"
    assert not lt(6), "6 is not less than 5"
    assert not lt(5), "5 is not less than 5"


def test_it_less_than_left():
    lt = 5 < it
    assert lt(6), "5 is less than 6"
    assert not lt(4), "5 is not less than 4"
    assert not lt(5), "5 is not less than 5"


def test_greater_than():
    gt = it > 5
    assert gt(6), "6 is greater than 5"
    assert not gt(4), "4 is not greater than 5"
    assert not gt(5), "5 is not greater than 5"


def test_greater_than_left():
    gt = 5 > it
    assert gt(4), "5 is greater than 4"
    assert not gt(6), "5 is not greater than 6"
    assert not gt(5), "5 is not greater than 5"


def test_less_than_or_equal():
    lte = it <= 5
    assert lte(4), "4 is less than 5"
    assert not lte(6), "6 is not less than 5"
    assert lte(5), "5 is equal to 5"


def test_less_than_or_equal_left():
    lte = 5 <= it
    assert lte(6), "5 is less than 5"
    assert not lte(4), "5 is not less than 4"
    assert lte(5), "5 is equal to 5"


def test_greater_than_or_equal():
    gte = it >= 5
    assert gte(6), "6 is greater than 5"
    assert not gte(4), "4 is not greater than 5"
    assert gte(5), "5 is equal to 5"


def test_greater_than_or_equal_left():
    gte = 5 >= it
    assert gte(4), "5 is greater than 4"
    assert not gte(6), "5 is not greater than 6"
    assert gte(5), "5 is equal to 5"


def test_attribute_access():
    class Foo:
        foo = 12

    f = Foo()
    get_foo = it.foo
    assert get_foo(f) == 12, "foo is 12"


def test_call():
    def pair(x, y):
        return (x, y)
    call = it(2, 3)
    ret = call(pair)
    assert ret == (2, 3)


def test_call_kwargs():
    def pair(x, y):
        return (x, y)
    call = it(y=2, x=3)
    ret = call(pair)
    assert ret == (3, 2)


def test_key():
    d = {
        'foo': 'bar'
    }
    get_foo = it['foo']
    assert get_foo(d) == 'bar'


def test_index():
    a = [1, 2, 3, 4]
    get_2 = it[2]
    assert get_2(a) == 3


def test_slice():
    a = [1, 2, 3, 4]
    get_first_2 = it[:2]
    assert get_first_2(a) == [1, 2]


def test_add_number():
    inc = it + 1
    assert inc(1) == 2
    assert inc(2) == 3


def test_add_string():
    suffix = it + '-suffixed'
    assert suffix('foo') == 'foo-suffixed'


def test_add_number_left():
    inc = 1 + it
    assert inc(1) == 2
    assert inc(2) == 3


def test_add_string_left():
    prefix = 'prefixed-' + it
    assert prefix('foo') == 'prefixed-foo'


def test_subtract():
    dec = it - 1
    assert dec(1) == 0
    assert dec(2) == 1


def test_subtract_left():
    diff_12 = 12 - it
    assert diff_12(6) == 6
    assert diff_12(12) == 0


def test_multiplication():
    double = it * 2
    assert double(1) == 2
    assert double(2) == 4


def test_multiplication_left():
    double = 2 * it
    assert double(1) == 2
    assert double(2) == 4


def test_division():
    halve = it / 2
    assert halve(4) == 2
    assert halve(8) == 4


def test_division_left():
    factor_of_8 = 8 / it
    assert factor_of_8(2) == 4
    assert factor_of_8(4) == 2


def test_floordiv():
    halve = it // 2
    assert halve(4) == 2
    assert halve(5) == 2


def test_floordiv_left():
    factor_of_8 = 8 // it
    assert factor_of_8(2) == 4
    assert factor_of_8(3) == 2


def test_modulo():
    mod2 = it % 2
    assert mod2(4) == 0
    assert mod2(5) == 1


def test_modulo_left():
    mod_of_8 = 8 % it
    assert mod_of_8(2) == 0
    assert mod_of_8(3) == 2


def test_divmod():
    divmod2 = divmod(it, 2)
    assert divmod2(8) == (4, 0)
    assert divmod2(5) == (2, 1)


def test_divmod_left():
    divmod_of_8 = divmod(8, it)
    assert divmod_of_8(2) == (4, 0)
    assert divmod_of_8(3) == (2, 2)


def test_power():
    square = pow(it, 2)
    assert square(2) == 4
    assert square(11) == 121


def test_power_modulo():
    square_mod2 = pow(it, 2, 2)
    assert square_mod2(4) == 0
    assert square_mod2(3) == 1


def test_power_left():
    power_of_2 = pow(2, it)
    assert power_of_2(2) == 4
    assert power_of_2(3) == 8


def test_lshift():
    shift_by_3 = it << 3
    assert shift_by_3(4) == 32
    assert shift_by_3(10) == 80


def test_lshift_left():
    shift_3_by = 3 << it
    assert shift_3_by(3) == 24
    assert shift_3_by(6) == 192


def test_rshift():
    shift_by_3 = it >> 3
    assert shift_by_3(128) == 16
    assert shift_by_3(510) == 63


def test_rshift_left():
    shift_128_by = 128 >> it
    assert shift_128_by(3) == 16
    assert shift_128_by(2) == 32


def test_and():
    and4 = it & 4
    assert and4(4) == 4
    assert and4(2) == 0


def test_and_left():
    four_and = 4 & it
    assert four_and(4) == 4
    assert four_and(2) == 0


def test_xor():
    xor3 = it ^ 3
    assert xor3(5) == 6
    assert xor3(12) == 15


def test_xor_left():
    twelve_xor = 12 ^ it
    assert twelve_xor(3) == 15
    assert twelve_xor(12) == 0


def test_or():
    or4 = it | 4
    assert or4(8) == 12
    assert or4(16) == 20


def test_or_left():
    four_or = 4 | it
    assert four_or(8) == 12
    assert four_or(16) == 20


def test_neg():
    neg = -it
    assert neg(12) == -12
    assert neg(-4) == 4


def test_pos():
    pos = +it
    assert pos(12) == 12
    assert pos(-4) == -4


def test_invert():
    inv = ~it
    assert inv(12) == -13
    assert inv(-12) == 11
