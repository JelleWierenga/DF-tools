import base64

base64_string = "your_base64_string"

try:
    decoded_data = base64.b64decode(base64_string)
    print("Encoded data:", decoded_data)
except Exception as e:
    print("There was a error while decoding:", e)
