lines = []

file = open("Data_Cran/querys.txt", "r")
# with open("Data_Cran/querys.txt") as archivo:
lines = file.read().split(".I")

print(lines)

# final_lines = [lines]
# lines = []
# for line in final_lines:
#     index = 0
#     while line[index] != '\n' and index < len(line):
#         print(index)
#         print(len(line))
#         index += 1
    
#     lines.append(final_lines[index+1:-1*(len(line) - 2)])
    
    
print(len(lines))
print(lines)
