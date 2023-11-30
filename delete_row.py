def delete_lines(file_path, ranges):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Delete the specified ranges of lines
    lines_to_delete = set()
    for start, end in ranges:
        lines_to_delete.update(range(start, end + 1))

    filtered_lines = [line for i, line in enumerate(lines, start=1) if i not in lines_to_delete]

    # Write the filtered lines back to the file
    with open(file_path, 'w') as file:
        file.writelines(filtered_lines)


# Define the ranges of lines to delete
line_ranges = []
start_line = 1
end_line = 7
while end_line <= 2112:
    line_ranges.append((start_line, end_line))
    start_line = end_line + 2
    end_line = start_line + 6

# Specify the path to your text file
file_path = r'D:\Videos\learnesp32.com\16. Website on a chip\test.txt'

# Call the function to delete the lines
delete_lines(file_path, line_ranges)


# Specify the path to your text file
#file_path = r'D:\Videos\learnesp32.com\16. Website on a chip\test.txt'

# Specify the start and end lines for each range to delete
#start_lines = [1, 9, 17, 25, 33]
#end_lines = [7, 15, 23, 31, 39]

# Call the function to delete the lines
#delete_lines(file_path, start_lines, end_lines)
