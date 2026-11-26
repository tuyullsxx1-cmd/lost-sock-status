def main():
    line = "Day 12 under the fridge. I've seen things. The dust bunnies have accepted me as one of their own."
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
