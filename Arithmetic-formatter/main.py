# This entrypoint file to be used in development. Start by reading README.md
from pytest import main

from arithmetic_arranger import arithmetic_arranger


print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))


# Run unit tests automatically
main()
# NOTE : 8 Test case passed
# !2 Test case Failed
# !test_two_problems_with_solutions
# !test_five_problems_with_solutions
