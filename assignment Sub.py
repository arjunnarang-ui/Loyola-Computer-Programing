#Arjun Narang
#Period 4
#9/18/2026
playList = ["I got a love", "Rather Lie", "Take me (To the moon)", "GASS"]
newSong = input("Please input a song: ")
newSong.title().strip()
playList.append (newSong)
print (len(playList))
playList.insert (0, "Love")
print ("Love" in playList)
playList.pop (1)
del playList [3]
print (sorted(playList))
playList.sort ()
playList.reverse ()
for thing in playList: 
    print (thing.upper ())
for i in range(len(playList)):
    print (i+1, playList [i])