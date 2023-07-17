import os


def proceed_prompt():
    ask = input("Do you want to proceed(y/n)? ")
    while ask.lower() != "n" and ask.lower() != "y":
        ask = input("Do you want to proceed(y/n)? ")
    if ask.lower() == "n":
        print("Exit Operation")
        exit()
    elif ask.lower() == "y":
        print("Operation Complete")
        pass


folder_dir = input("what is the folder directory? ")
try:
    os.startfile(folder_dir)
except:
    print("couldn't open folder")
    exit()

proceed_prompt()

# os.chdir(r"D:\Save\Courses\4-Languages\files\Screenshots and Notes")
os.chdir(folder_dir)


for file in os.listdir(os.getcwd()):
    p_old = os.path.join(os.getcwd(), file)
    if file.endswith(".txt"):
        path = os.path.join(os.getcwd(), "Text")
        try:
            os.mkdir(path)
        except FileExistsError:
            pass
        p_new = os.path.join(path, file)
        os.rename(p_old, p_new)
    if file.endswith(".png") or file.endswith("webp"):
        path = os.path.join(os.getcwd(), "Images")
        try:
            os.mkdir(path)
        except FileExistsError:
            pass
        p_new = os.path.join(path, file)
        os.rename(p_old, p_new)
    if file.endswith(".mp4") or file.endswith(".srt"):
        path = os.path.join(os.getcwd(), "Videos & Subtitles")
        try:
            os.mkdir(path)
        except FileExistsError:
            pass
        p_new = os.path.join(path, file)
        os.rename(p_old, p_new)
    if file.endswith(".pdf") or file.endswith(".epud") or file.endswith(".doc") or file.endswith(".docx"):
        path = os.path.join(os.getcwd(), "Books, Sheets & Documents")
        try:
            os.mkdir(path)
        except FileExistsError:
            pass
        p_new = os.path.join(path, file)
        os.rename(p_old, p_new)

