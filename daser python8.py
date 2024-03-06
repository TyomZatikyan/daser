import random
import os

# Initialize game variables
lives = 3
bananas_eaten = 0

# Function to create a new matrix
def create_matrix(size):
    return [['🌴' for _ in range(size)] for _ in range(size)]

# Function to place objects in the matrix
def place_objects(matrix, monkey_row, monkey_col, snake_row, snake_col, banana_row, banana_col):
    matrix[monkey_row][monkey_col] = '🐵'
    matrix[snake_row][snake_col] = '🐍'
    matrix[banana_row][banana_col] = '🍌'
    return matrix

# Function to display the matrix
def display_matrix(matrix):
    os.system('clear' if os.name == 'posix' else 'cls')  # Clear the console
    for row in matrix:
        print(' '.join(row))

# Function to move the snake
def move_snake(monkey_row, monkey_col, snake_row, snake_col):
    direction = random.choice(['up', 'down', 'left', 'right'])
    
    if direction == 'up' and snake_row > 0:
        snake_row -= 1
    elif direction == 'down' and snake_row < matrix_size - 1:
        snake_row += 1
    elif direction == 'left' and snake_col > 0:
        snake_col -= 1
    elif direction == 'right' and snake_col < matrix_size - 1:
        snake_col += 1

    return snake_row, snake_col

# Main game loop
while True:
    matrix_size = 20
    matrix = create_matrix(matrix_size)

    # Place the monkey, snake, and banana randomly
    monkey_row, monkey_col = random.randint(0, matrix_size - 1), random.randint(0, matrix_size - 1)
    snake_row, snake_col = random.randint(0, matrix_size - 1), random.randint(0, matrix_size - 1)
    banana_row, banana_col = random.randint(0, matrix_size - 1), random.randint(0, matrix_size - 1)

    # Ensure that monkey, snake, and banana don't overlap
    while (monkey_row, monkey_col) == (snake_row, snake_col) or \
          (monkey_row, monkey_col) == (banana_row, banana_col) or \
          (snake_row, snake_col) == (banana_row, banana_col):
        monkey_row, monkey_col = random.randint(0, matrix_size - 1), random.randint(0, matrix_size - 1)
        snake_row, snake_col = random.randint(0, matrix_size - 1), random.randint(0, matrix_size - 1)
        banana_row, banana_col = random.randint(0, matrix_size - 1), random.randint(0, matrix_size - 1)

    matrix = place_objects(matrix, monkey_row, monkey_col, snake_row, snake_col, banana_row, banana_col)
    display_matrix(matrix)

    # Game logic
    while True:
        move = input("Enter your move (a/w/s/d): ").lower()

        # Update previous positions with palm trees
        matrix[monkey_row][monkey_col] = '🌴'
        matrix[snake_row][snake_col] = '🌴'

        # Update monkey position based on user input
        if move == 'a' and monkey_col > 0:
            monkey_col -= 1
        elif move == 'd' and monkey_col < matrix_size - 1:
            monkey_col += 1
        elif move == 'w' and monkey_row > 0:
            monkey_row -= 1
        elif move == 's' and monkey_row < matrix_size - 1:
            monkey_row += 1

        # Move the snake
        snake_row, snake_col = move_snake(monkey_row, monkey_col, snake_row, snake_col)

        # Check if the snake caught the monkey
        if (monkey_row, monkey_col) == (snake_row, snake_col):
            print("Oh no! The snake caught you.")
            lives -= 1
            break

        # Check if the monkey ate a banana
        if (monkey_row, monkey_col) == (banana_row, banana_col):
            bananas_eaten += 1
            print(f"Yum! You've eaten {bananas_eaten} banana{'s' if bananas_eaten > 1 else ''}.")
            # Place a new banana randomly
            banana_row, banana_col = random.randint(0, matrix_size - 1), random.randint(0, matrix_size - 1)
            # Ensure that the new banana doesn't overlap with other objects
            while (banana_row, banana_col) == (monkey_row, monkey_col) or \
                  (banana_row, banana_col) == (snake_row, snake_col):
                banana_row, banana_col = random.randint(0, matrix_size - 1), random.randint(0, matrix_size - 1)
            # Decrease matrix size
            matrix_size -= 1

        # Update monkey position in the matrix
        matrix[monkey_row][monkey_col] = '🐵'
        # Update snake position in the matrix
        matrix[snake_row][snake_col] = '🐍'

        # Display the updated matrix
        display_matrix(matrix)

        # Check win condition
        if bananas_eaten == 5:
            print("Congratulations! You've won!")
            exit()

        # Check lose condition
        if lives == 0:
            print("Game over. Better luck next time!")
            exit()
