# TDD  - Test-Driven Development - czyli programowanie sterowane testami
# Jest to technika tworzenia oprogramowania,
# w której testy jednostkowe są pisane przed napisaniem kodu implementacyjnego

import pytest


def calculate_square(num):
    return num ** 2


def test_squre_1():
    assert calculate_square(2) == 4
