import math
import string
x_win = False
o_win = False
player = "X"
dict={
  "1 1":6,
  "1 2":3,
  "1 3":0,
  "2 1":7,
  "2 2":4,
  "2 3":1,
  "3 1":8,
  "3 2":5,
  "3 3":2,
}

def change_player():
    global player
    if player == "X":
        player = "O"
    else:
        player = "X"
    return player

def check_column(list):
    global o_win,x_win
    if all((list[i] == 'X' for i in range(len(list)))):
        x_win = True
    elif all((list[i] == 'O' for i in range(len(list)))):
        o_win = True
    else:
            pass

def who_win(insert):

    global x_win,o_win
    for i in range(3):  #rows
        check_column([insert[i*3],insert[i*3+1],insert[i*3+2]])
    for i in range(3):  #colomn
        check_column([insert[i],insert[i+3],insert[i+6]])
    if (insert[0] == insert[4] == insert[8]):
        if insert[4] == 'X':
            x_win = True
        elif insert[4] == 'O':
            o_win = True
        else:
            pass
    if (insert[6] == insert[4] == insert[2]):
        if insert[6] == 'X':
            x_win = True
        elif insert[6] == 'O':
            o_win = True
        else:
            pass

def there_is_more_move(insert):
    return any([insert[i]=="_" for i in range(len(insert))])
#    free=False
#   for j in insert:
 #       if j=='_':
  #         free=True
   # return free

def print_table(insert):
    print('---------')
    print('| '+insert[0]+' '+insert[1]+' '+insert[2]+' |')
    print('| '+insert[3]+' '+insert[4]+' '+insert[5]+' |')
    print('| '+insert[6]+' '+insert[7]+' '+insert[8]+' |')
    print('---------')

insert= "_________"
insert=[x for x in insert]
print_table(insert)
who_win(insert)

while( not x_win and not o_win and there_is_more_move(insert)):
    coordinates = input('Enter the coordinates:')
    if (string.ascii_letters in coordinates):
        print("You should enter numbers!")
    elif coordinates not in ("1 1","1 2","1 3","2 1", "2 2","2 3","3 1","3 2","3 3"):
        print("Coordinates should be from 1 to 3!")
    elif insert[dict[coordinates]]=="_":
        insert[dict[coordinates]] = player
        change_player()
        print_table(insert)
        who_win(insert)
    else:
        print("This cell is occupied! Choose another one!")

if abs(insert.count('O')-insert.count('X'))>1 or (x_win and o_win):
    print("Impossible")
elif (not x_win and not o_win):
    print("Draw")
elif x_win:
    print("X wins")
elif o_win:
    print("O wins")
else:
  print("sta sad")
