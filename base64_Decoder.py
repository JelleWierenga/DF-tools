import base64
import logging
import hashlib

logging.basicConfig(filename='base64_decoder.log', level=logging.INFO, format='%(asctime)s - %(message)s')

input_file = 'input.txt'
output_file = 'decoded_output.txt'

try:
    with open(input_file, 'r') as infile:
        base64_string = infile.read().strip()
    logging.info("read the string from %s", input_file)

    input_hash = hashlib.sha256(base64_string.encode()).hexdigest()
    logging.info("Input hash (SHA-256): %s", input_hash)

    decoded_data = base64.b64decode(base64_string)
    logging.info("Base64 decoding worked.")

    output_hash = hashlib.sha256(decoded_data).hexdigest()
    logging.info("Output hash (SHA-256): %s", output_hash)

    with open(output_file, 'wb') as outfile:
        outfile.write(decoded_data)
    logging.info("decoded data stored in %s", output_file)

    print("Decoding successful. Output saved to:", output_file)

except Exception as e:
    logging.error("There was a error during decoding: %s", e)
    print("There was a error during decoding:", e)
