while True:
    text = input("What you gotta say? : " if 'text' not in locals() else "I got that! Anything else? : ")
    if text == "STOP":
        break