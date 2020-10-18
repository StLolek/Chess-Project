import chess
import chess.pgn
import time

start_time = time.time()

pgn = open("lichess_db_standard_rated_2013-01.pgn")
moves = 0
legalmoves = 0
games = 0

board = chess.Board()
while True:
    game = chess.pgn.read_game(pgn)
    if game is None:
        break  # end of file

    games += 1
    for move in game.mainline_moves():
        legalmoves += board.legal_moves.count()
        board.push(move)
        moves += 1
    board.reset()
avgpergame = moves / games
legalavgpermove = legalmoves / moves
print("Zadanie 1. \n")
print("Średnia liczba wykonanych ruchów na gre: ", avgpergame)
print("Średnia liczba dostępnych ruchów na ruch: ", legalavgpermove)
print("\nZłożoność gry: ", avgpergame, "^", legalavgpermove, " = ", avgpergame ** legalavgpermove)
print("\n--- %s seconds ---" % (time.time() - start_time))
