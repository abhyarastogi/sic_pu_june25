import re

data = ["abc123", "hello2024abh23ya", "no digits", "zip007"]

# Extract digits using regex and lambda
digits = list(map(lambda s: re.findall(r'\d+', s), data))
print(digits)  # [['123'], ['2024'], [], ['007']]