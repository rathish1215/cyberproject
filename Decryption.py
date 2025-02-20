def decryption(pixels):
# Extract the binary message from the image pixels
    binary_message = ""
    for i in range(pixels.shape[0]):
        for j in range(pixels.shape[1]):
            for k in range(3):  # RGB channels
                binary_message += str(pixels[i][j][k] & 1)  # Extract LSB directly as string


    # Convert binary message to characters
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte:
            message += chr(int(byte, 2))
        if "#####" in message: 
            # print('hello') # Stop at delimiter
            break
    return message