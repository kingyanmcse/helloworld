import pickle

game_data = open('save.dat', 'rb')
load_game_data = pickle.load(game_data)
game_data.close()
print(load_game_data)
