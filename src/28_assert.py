# Author: Allen Anker
# Created by Allen Anker on 2019-10-25


def apply_discount(price, discount):
    updated_price = price * (1 - discount)
    assert 0 <= updated_price <= price, 'price should be greater or equal to 0 and less or equal to original price'
    return updated_price


apply_discount(100, 0.2)


# apply_discount(100, 2)


def calculate_average_price(total_sales, num_sales):
    assert num_sales > 0, 'number of sales should be greater than 0'
    return total_sales / num_sales


def func(input):
    assert isinstance(input, list), 'input must be type of list'
    if len(input) == 1:
        pass
    elif len(input) == 2:
        pass
    else:
        pass
