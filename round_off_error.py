print(.1 + .2)

# python round_off_error.py
# 0.30000000000000004

# Computers store information using 0's and 1's. All information must be converted to a string of 0's and 1's. Ex: 5 is converted to 101. Since only two values, 0 or 1, are allowed the format is called binary.
# Floating-point values are stored as binary by Python. The conversion of a floating point number to the underlying binary results in specific types of floating-point errors.
# A round-off error occurs when floating-point values are stored erroneously as an approximation. The difference between an approximation of a value used in computation and the correct (true) value is called a round-off error.
# Ex: Storing the float (0.1) 10 results in binary values that actually produce (0.1000000000000000055511151231257827021181583404541015625) 10 when converted back, which is not exactly equal to (0.1) 10 .