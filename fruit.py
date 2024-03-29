def main():
    try:
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"original: {fruit_list}")


        fruit_list.reverse()
        print(f"reverse: {fruit_list}")

        fruit_list.append("orange")
        print(f"append: {fruit_list}")

        index = fruit_list.index("apple")
        fruit_list.insert(index, "cherry")
        print(f"insert: {fruit_list}")

        fruit_list.pop(1)
        print(f"pop: {fruit_list}")

        fruit_list.pop()
        print(f"pop: {fruit_list}")

        fruit_list.sort()
        print(f"sort: {fruit_list}")

        fruit_list.clear()
        print(f"clear: {fruit_list}")
        
    except IndexError as index_err:
        print(type(index_err).__name__, index_err, sep=": ")

# Call main to start this program.
if __name__ == "__main__":
    main()