import chess
import chess.engine
import chess.pgn
import random
import time

start_time = time.time()
engine = chess.engine.SimpleEngine.popen_uci("stockfish")


def minimax(board, depth, maximizingplayer):
    if depth == 0 or board.is_game_over():
        score = str(engine.analyse(board, chess.engine.Limit(depth=0, time=1))['score'])
        if score[0] == '#':
            score = score[1:]

        return float(score)
    if maximizingplayer:
        value = float('-inf')
        legal = board.legal_moves
        for move in legal:
            board.push(move)
            value = max(value, minimax(board, depth - 1, False))
            board.pop()
        return value
    else:
        value = float('inf')
        for move in board.legal_moves:
            board.push(move)
            value = min(value, minimax(board, depth - 1, True))
            board.pop()
        return value


pgn = open('lichess_StLolek_2020-10-13.pgn')
list = []
while True:
    game = chess.pgn.read_game(pgn)
    if game is None:
        break
    list.append(game)
print('Wszystkie prezentowane wyniki są obliczane do głębokości:', 3)
l = len(list)
for j in range(5):
    number = random.randint(0,l)
    game = list[number]
    moves = 0
    for move in game.mainline_moves():
        moves += 1
    board = chess.Board()
    movenumber = random.randint(2,moves)
    i = 0

    for move in game.mainline_moves():
        if i < movenumber:
            board.push(move)
            i += 1
        else:
            break

    print(board, '\n Wynik dla powyższej pozycji: ', minimax(board, 3, board.turn) )

print("\n--- %s seconds ---" % (time.time() - start_time))
