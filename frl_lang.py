print("created by Athariz21")
print("write 'exit' to exit")
def run():
    print("=== FRL LANG 0.1 ===")

    while True:
        line = input("FRL > ")

        if line.startswith("write "):
            text = line[6:]
            print(text.strip('"'))

        elif line == "ext":
            print("Leaving FRL Lang...")
            break

        else:
            print("Unknown command!")

