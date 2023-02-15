# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

name_array = []
with open("Input\\Names\invited_names.txt") as name_txt:
    for namex in name_txt:
        y = namex.strip()
        name_array.append(y)


for z in name_array:
    with open("Input\Letters\starting_letter.txt") as data:
        dest = f"Output\ReadyToSend\letter_for_{z}.txt"
        with open(dest, "a") as dest_file:
            for line in data:
                x = line.replace("[name]", z)
                dest_file.writelines(x)

#print(name_array)
