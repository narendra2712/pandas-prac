import os
def cf(pp):
    folders=["Assets", "Materials", "textures", "Maps"]
    for folder in folders:
        fp=os.path.join(pp,folder)
        if not os.path.exists(fp):
            os.makedirs(fp)
            print(f"folder created:{fp}")
            print(cf(pp))
        else:
            print(f"Folder exists:{fp}")
    pp="D:/prac/projects/"
    cf(pp)

'''import os

# define the name of the directory with its subdirectories
path = 'D:/content/projects/games/game01'
path2= 'D:/content/projects'

os.makedirs(path, exist_ok=True)'''

