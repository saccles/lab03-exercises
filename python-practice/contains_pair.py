def check(l: list):
    unique = set(l)
    
    return len(unique) != len(l)


# Should print True
input1 = [1, 2, 3, 2]

# Should print False
input2 = [5, 2, -10, 44, 90]

# Should print True
input3 = [1, 3, 4, 5, 6, 7, 7]

inputs = [input1, input2, input3]
expected_results = [True, False, True]

inputs_length = len(inputs)
last_index = inputs_length - 1

for i in range(inputs_length):
    print(f"Input: {inputs[i]}")
    print(f"Expected result: {expected_results[i]}")
    print(f"Actual result: {check(inputs[i])}")
    
    if i != last_index:
        print()
