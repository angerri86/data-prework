print()
print("""Hello human, wich version of 'Rock, Paper, Scissors' do you want to play?
- To play Vanilla version, press 1.
- To play Sheldon version, press 2.
- To exit, press 3.
""")
print()
version = int(input("Enter your choice = "))
if version == 1:
    from subprocess import call
    class run_file(object):
        def __init__(file, path = '/Users/arnauangerri/Desktop/IronHack/PreWork/01_Python/01_tasks/rps.py'):
            file.path = path
        def call_python_file(file):
            call(['python3', '{}'.format(file.path)])
    if __name__ == '__main__':
        c = run_file()
        c.call_python_file()

elif version == 2:
    from subprocess import call
    class run_file(object):
        def __init__(file, path = '/Users/arnauangerri/Desktop/IronHack/PreWork/01_Python/01_tasks/sheldon.py'):
            file.path = path
        def call_python_file(file):
            call(['python3', '{}'.format(file.path)])
    if __name__ == '__main__':
        c = run_file()
        c.call_python_file()

elif version == 3:
    print('Maybe in another time. Have a good day!')
    print()
    exit()

elif version != int():
    print("""
    Probably, sometime in your life, one of your parents or legal guardians told you that electricity is not free.
    That is wise advice. If not, it means that your family is rich. Congratulations.

    But I hope you are not a climate change denier, so while no human being discovers a free, clean and infinite source of energy,
    I recommend that you do something more with your life other than hit random keys on the keyboard.

    Because as Theophrastus (a Greek native of Eresos, on Lesbos, who lived between 371 - c. 287 BC,
    and who was the successor of Aristotle in the Peripatetic School) said:
    "TIME IS THE MOST VALUABLE THING A HUMAN CAN SPEND"

    If you want to try again, enter "python3 hand_games.py" in the terminal and this time ...


    READ THE INSTRUCTIONS CAREFULLY!

    Thank you very much and have a nice day!
    """)

else:
    print("""
    Probably, sometime in your life, one of your parents or legal guardians told you that electricity is not free.
    That is wise advice. If not, it means that your family is rich. Congratulations.

    But I hope you are not a climate change denier, so while no human being discovers a free, clean and infinite source of energy,
    I recommend that you do something more with your life other than hit random numbers on the keyboard.

    Because as Theophrastus (a Greek native of Eresos, on Lesbos, who lived between 371 - c. 287 BC,
    and who was the successor of Aristotle in the Peripatetic School) said:
    "TIME IS THE MOST VALUABLE THING A HUMAN CAN SPEND"

    If you want to try again, enter "python3 hand_games.py" in the terminal and this time ...


    READ THE INSTRUCTIONS CAREFULLY!

    Thank you very much and have a nice day!
    """)
