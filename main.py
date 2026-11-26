def main():
    """Write the sock's status update: one line, first-person, under the fridge."""
    line = "Day 12 under the fridge. I've seen things. The dust bunnies have accepted me as one of their own."
    assert line == line.strip()
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
