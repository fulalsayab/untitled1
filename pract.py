import pytest


def find_first_count(line):
    word_repeated = {}

    for word in line.split(" "):
        if word in word_repeated:
            return word
        else:
            word_repeated[word] = True
    return None


def test_file1_method1():
    line = "hi my name is ausaif. what is your name? ausaif"
    assert "is" == find_first_count(line), "Test Passes"
    assert "name" == find_first_count(line), "Test failed"
