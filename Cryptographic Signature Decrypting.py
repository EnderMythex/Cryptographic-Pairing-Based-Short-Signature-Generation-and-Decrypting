import binascii

# The signature in hexadecimal format
signature = "3045022011a64d7dd94724e549d3c769ba0c412e056c88f5fb5b65dcade98a6cb90d9ad2022100dd1cfdea977e9ef6674b26915b536715908dd46a24e0899ad116f7c91378ba64"

# Convert the signature to binary format
binary_signature = binascii.unhexlify(signature)

# Split the binary signature into r and s values
r_value = binary_signature[1:33]
s_value = binary_signature[33:65]

# Print the r and s values
print("r value:", binascii.hexlify(r_value))
print("s value:", binascii.hexlify(s_value))