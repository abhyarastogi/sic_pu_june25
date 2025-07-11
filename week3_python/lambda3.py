#Convert all email addresses to domain names

import re

emails = ["alice@gmail.com", "bob@yahoo.com", "user@outlook.com"]

# Extract domain using regex
domains = list(map(lambda s: re.search(r'@(\w+)\.com', s).group(1), emails))
print(domains)  # ['gmail', 'yahoo', 'outlook']