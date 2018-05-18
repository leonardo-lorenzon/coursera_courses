import fatorial
import pytest

def test_fatorial_0():
	assert fatorial.fatorial(0) == 1

def test_fatorial_1():
	assert fatorial.fatorial(1) == 1

def test_fatorial_2():
	assert fatorial.fatorial(2) == 2

def test_fatorial_3():
	assert fatorial.fatorial(3) == 6

def test_fatorial_4():
	assert fatorial.fatorial(4) == 24

def test_fatorial_5():
	assert fatorial.fatorial(5) == 120
	