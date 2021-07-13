import zipfile
import shutil
import os

def zipthefolders(subfolders, aformat):
    for subfolder in subfolders:
        files = [f for f in os.listdir(subfolder) if os.path.isfile(os.path.join(subfolder, f))]
        zip_file = zipfile.ZipFile(f'{subfolder}.{aformat.lower()}', 'w')
        for F in files:
            zip_file.write( f'{subfolder}\\{F}', f'{F}', compress_type=zipfile.ZIP_DEFLATED)
        zip_file.close()

folder = os.getcwd()
subfolders = [ f.name for f in os.scandir(folder) if f.is_dir() ]
print("Detected The Following Folders:")
for folder in subfolders:
    print(folder)
print("\nThese Folders will be converted to an Archive Format, is this Okay? (Y/N)")
choice = input()
if(choice=='N' or choice=='n'):
    exit()
elif(choice=='Y' or choice=='y'):
    print("What Format do you want to convert into? (zip/cbz/cbr)")
    aformat = input()
    if(aformat=="zip" or aformat=="cbz" or aformat=="cbr"):
        print("Archiving...")
        zipthefolders(subfolders, aformat)
        print("Converted to archives.\nDelete Original Folders? (Y/N)")
        delch = input()
        if(delch=='N' or delch=='n'):
            exit()
        elif(delch=='Y' or delch=='y'):
            for folder in subfolders:
                shutil.rmtree(folder)
            print(f'{len(subfolders)} Folders Removed.')
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")