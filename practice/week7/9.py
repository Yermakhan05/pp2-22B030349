import os

# create output directory if it does not exist
if not os.path.exists('output'):
    os.mkdir('output')
else:
    # delete the contents of the output directory if it already exists
    for file_name in os.listdir('output'):
        file_path = os.path.join('output', file_name)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(f"Error: {e}")

# read input.txt file
with open('input.txt', 'r') as input_file:
    content = input_file.read()

# write to output1.txt file
with open('output/output1.txt', 'w') as output_file:
    output_file.write(content.upper())
    print("output1.txt file created.")

# write to output2.txt file
with open('output/output2.txt', 'w') as output_file:
    output_file.write(content.lower())
    print("output2.txt file created.")
