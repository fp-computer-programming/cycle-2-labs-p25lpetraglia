#lab 8-9
# Solution for Cycle 8 Labs Assignment


print("Multiplication Table")
for i in range(1, 13):
    for j in range(1, 13):
        print(f"{i * j:4}", end=" ")
    print()


paragraph = input("Enter a paragraph: ")
words = paragraph.split()
longest_word = ""
for word in words:
    clean_word = ''.join(char for char in word if char.isalnum())
    if len(clean_word) > len(longest_word):
        longest_wor = clean_word
print("The longest word is:", longest_word)

print("FizzBuzz")
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

data = [3, 7, 1, 4]
print("Histogram:")
for value in data:
    print("*" * value)

string = input("Enter a stringg: ")
char_count = {}
repeated_char = None
for char in string:
    if char in char_count:
        repeated_char = char
        break
    char_count[char] = 1
if repeated_char:
    print("The first repeated character is:", repeated_char)
else:
    print("No repeated characters found.")

rows = int(input("Enter the number of rows for Pascal's Triangle: "))
triangle = []
for i in range(rows):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = triangle[i-1][j-1] + triangle[i-1][j]
    triangle.appendrow)
    print(" ".join(map(str, row)))


text = input("Enter a paragraph: ")
text = text.lower()
words = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text).split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
print("Word Frequencies:")
for word, count in sorted_words:
    print(f"{wor}: {count}")


grid = [
    [0, 1, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 0]
]
def count_live_neighbors(grid, x, y):
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),         (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= x < len(grid) and 0 <= ny < len(grid[0]):
            count += grid[nx][ny]
    return count

next_grid = [[0] * 5 for _ in range(5)]
for i in range(5):
    for j in range(5):
        live_neighbors = count_live_neighbors(grid, i, j)
        if grid[i][j] == 1 and live_neighbors in (2, 3):
            nextgrid[i][j] = 1
        elif grid[i][j] == 0 and live_neighbors == 3:
            next_grid[i][j] = 1

print("Next State of the Grid:")
for row in next_grid:
    printrow)
