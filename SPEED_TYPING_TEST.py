import time

def run_test(text):
    """Run the typing test"""
    print("Type the following text:")
    print(text)
    input("Press Enter to start...")

    start_time = time.time()

    # Ask the user to type the text
    typed_text = input()

    end_time = time.time()

    # Calculate the elapsed time and speed
    elapsed_time = end_time - start_time
    speed = len(typed_text) / elapsed_time

    print("Elapsed time:", round(elapsed_time, 2), "seconds")
    print("Typing speed:", round(speed, 2), "characters per second")

# Example usage: run the typing test
text = "The grass is always greener on the other side of the fence."
run_test(text)


