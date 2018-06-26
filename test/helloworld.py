import pickle

game_date = {'name': 'KingYan', 'money': 150.98, 'weapon': ['rife', 'AK']}
save_file = open('save.dat', 'wb')
pickle.dump(game_date, save_file)
save_file.close()
