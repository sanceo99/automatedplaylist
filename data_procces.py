import start

datas = str(start.text)

songs = []
splitted = datas.splitlines()
index = 1

for i in range(len(splitted)):
    if (splitted[i] == str(index)):
        songs.append(str(splitted[i+1] + " " + str(splitted[i+2])))
        index = index+1
