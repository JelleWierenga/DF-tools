import re

base64_string = "your_base64_string"

if re.fullmatch(r'[A-Za-z0-9+/]+={0,2}', base64_string) and len(base64_string) % 4 == 0:
    print("The string seems to be base64 encoded.")
else:
    print("The string might not be a valid base64.")
