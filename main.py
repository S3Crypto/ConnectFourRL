from connect_four import ConnectFour

def main():
    game = ConnectFour()
    play_again = 'y'
    
    while play_again.lower() == 'y':
        game_over = False
        game.reset_board()
        
        while not game_over:
            game.display_board()
            print(f"Player {game.current_player}'s turn")
            
            valid_move = False
            while not valid_move:
                user_input = input(f"Player {game.current_player}, choose column (0-6) or 'q' to quit: ")
                
                if user_input.lower() == 'q':
                    print("Quitting the game...")
                    return  # Exit the game loop and end the program
                
                try:
                    column = int(user_input)
                    if 0 <= column < 7:
                        valid_move = game.drop_disc(column)
                        if not valid_move:
                            print("Column is full. Try another column.")
                    else:
                        print("Invalid column. Choose a number between 0 and 6.")
                except ValueError:
                    print("Invalid input. Please enter a number between 0 and 6, or 'q' to quit.")
            
            if game.is_winning_move(game.current_player):
                game.display_board()
                print(f"Player {game.current_player} wins!")
                game.update_score(game.current_player)
                game_over = True
            elif game.is_full():
                game.display_board()
                print("It's a tie!")
                game_over = True
            else:
                game.switch_player()
        
        game.display_scoreboard()
        play_again = input("Do you want to play again? (y/n): ")

if __name__ == "__main__":
    main()
