#/usr/bin/env python

def test_solution():

    with open('solution.txt', 'r') as f:

        first_line = f.readline()
        print(first_line)

        assert first_line.rstrip() == "Hello, World!"


