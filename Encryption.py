def encryption(secret_message, pixels):        
        binary_message = ''.join(format(ord(char), '08b') for char in secret_message)
        message = ""
        for i in range(0, len(binary_message), 8):
            byte = binary_message[i:i+8]
            if byte:
                message += chr(int(byte, 2))
            if "#####" in message: 
                 # Stop at delimiter
                break
        message_index = 0

        # Embed the binary message into the image pixels
        for i in range(pixels.shape[0]):
            for j in range(pixels.shape[1]):
                for k in range(3):  # RGB channels
                    if message_index < len(binary_message):
                        # Replace the LSB of the pixel with the binary message bit
                        pixels[i][j][k] = (pixels[i][j][k] & 0b11111110) | int(binary_message[message_index])
                        message_index += 1 
                    else:
                        break
        return pixels