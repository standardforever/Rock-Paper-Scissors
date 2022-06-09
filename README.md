This dirctory contains Rock-Paper-Scissors game


A brief summary of the Rules:
    1. If the two players choose the same “character” it’s a tie, and game repeats.
    2. Rock beats Scissors
    3. Paper beats Rock
    4. Scissors beats Paper

How the game works:

    When the program is run, ask the user to pick an option between "R", "P" or "S"
    If user input is invalid (not amongst our options), print an error, and ask for their input again
    Uses the `choice` function from the inbuilt Python `random` module to make a choice for CPU player(computer).
    Print both player's moves in the format: `Player (Rock) : CPU (Paper)`