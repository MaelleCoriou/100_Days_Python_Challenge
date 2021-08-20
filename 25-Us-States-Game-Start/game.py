def find_state(file, answer, turtle):
    for index, row in file.iterrows():
        if answer == row.state:
            turtle.goto(int(row.x), int(row.y))
            turtle.write(f'{row.state}')
            return True


def show_state(file, guessed, turtle):
    for index, row in file.iterrows():
        if row.state != guessed:
            turtle.goto(int(row.x), int(row.y))
            turtle.write(f'{row.state}')

