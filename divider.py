#divider.py 
print("Dividing 10 by an integer")

while True:
    try:
        request = int(input("Provide an integer:"))
        print(10 / request)
    except ValueError:
        print("Your input must be an integer")
    except ZeroDivisionError:
        print("Your input must not be zero(0)")

"""
We don't want nested exception suites in your
"a series of except statements" -- semantically proper
to have one try with multiple excepts.

while True:
    try:
        request = int(input("Provide an integer:"))
        print (10/request)
    except (ValueError):
        print("Your input must be an integer")
        except (ZeroDivisionError):  #  <-- should not be indented
        print("Your input must not be zero(0)")  #  <--- should be indented if a suite for the exception handling.

Don't feel obligated to put parens around the exception you're aiming to trap -- only
needed if you're building a tuple of several, to be handled with the same suite.
"""

