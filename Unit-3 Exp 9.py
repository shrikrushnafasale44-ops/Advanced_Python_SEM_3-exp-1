import re

text = """
hello student!
for any queries, contact abc@gmail.com or teacher@gmail.com
you can also contact support@gmail.com
"""
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

emails = re.findall(email_pattern, text)

print("Email addresses found: ")

for email in emails :
    print(email)
