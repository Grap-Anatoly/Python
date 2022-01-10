import draw

def play_game():
    print ("Game started!")

def main():
    result = play_game()
    draw.draw_game(result)

# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()
