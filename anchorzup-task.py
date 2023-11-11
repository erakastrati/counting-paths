def calculate_paths(x, y):
    matrix = [[1] * (y + 1) for _ in range(x + 1)]
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
    return matrix[x][y]

def find_paths(x, y, path=""):
    if x == 0 and y == 0:
        print(path)
        return
    if x > 0:
        find_paths(x - 1, y, path + "E")
    if y > 0:
        find_paths(x, y - 1, path + "N")

def main():
    try:
        x = int(input("Enter X: "))
        y = int(input("Enter Y: "))
        if x < 0 or y < 0:
            raise ValueError("Input values must be non-negative integers.")
        print("Paths:", calculate_paths(x, y), "\nRoutes:")
        find_paths(x, y)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
