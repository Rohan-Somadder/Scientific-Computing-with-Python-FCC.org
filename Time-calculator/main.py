# This entrypoint file to be used in development. Start by reading README.md
from unittest import main
from time_calculator import add_time


print(add_time("11:06 PM", "2:02"))


# Run unit tests automatically
main(module='test_module', exit=False)
