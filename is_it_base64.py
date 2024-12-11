import re
import logging
import hashlib

logging.basicConfig(filename='is_it_base64.log', level=logging.INFO, format='%(asctime)s - %(message)s')

input_file = 'input.txt'
validation_output_file = 'validation_result.txt'

try:
    with open(input_file, 'r') as infile:
        base64_string = infile.read().strip()
    logging.info("read the input string from %s", input_file)

    input_hash = hashlib.sha256(base64_string.encode()).hexdigest()
    logging.info("Input hash (SHA-256): %s", input_hash)

    logging.info("validating the base64 sting stardet.")
    if re.fullmatch(r'[A-Za-z0-9+/]+={0,2}', base64_string) and len(base64_string) % 4 == 0:
        validation_result = "The string is a valid Base64."
        logging.info("validation completed, the string is a valid Base64.")
    else:
        validation_result = "The string is not a valid Base64."
        logging.warning("Validation failed, the string is not a valid Base64.")

    with open(validation_output_file, 'w') as outfile:
        outfile.write(validation_result + "\n")
        outfile.write(f"Input hash (SHA-256): {input_hash}\n")
    logging.info("VValidation results stored in %s", validation_output_file)

    print("Validation complete. Result saved to:", validation_output_file)

except Exception as e:
    logging.error("There was a error during validation: %s", e)
    print("There was a error during validation:", e)
