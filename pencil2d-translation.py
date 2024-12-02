# I want to unzip the pencil2d translation file

# Import the required libraries
import zipfile
import os
import shutil
import glob


# search for zip file in the Downloads directory
# get the newest file if there are multiple files
# Exmpale: pencil2d_pencil2d_b9a9857e-e9e5-4d98-ba86-8fe91bb450bb.zip

# Get Download directory Path
download_dir = os.path.expanduser("~") + "/Downloads"
print("Download Directory Path: ", download_dir)

# List all .zip files in the Downloads directory and get the newest file
zip_files = glob.glob(os.path.join(download_dir, "pencil2d_pencil2d_*.zip"))
zip_files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
newest_file = zip_files[0] if zip_files else None

zipFileName = newest_file
print("Newest File: ", zipFileName)

# Remove the temporary directory if it exists
if os.path.exists("pencil2d_translations"):
    shutil.rmtree("pencil2d_translations")
    print("Removed the directory")

# Open the zip file and extract the contents to the temporary directory
with zipfile.ZipFile(zipFileName, 'r') as zip_ref:
    zip_ref.extractall("pencil2d_translations")
    print("Unzipped the file")

# Go to the directory and list the files
os.chdir("pencil2d_translations")
print("Changed the directory")

# List the files in the directory
print("The files in the directory are:")
print(os.listdir())

# Iterate through the files and rename pencil-ts-master-LANG.ts to pencil_LANG.ts
# the LANG is the language code
for file in os.listdir():
    if file.startswith("pencil-ts-master-") and file.endswith(".ts"):
        lang = file.split("-")[-1].split(".")[0]
        new_name = "pencil_" + lang + ".ts"
        os.rename(file, new_name)
        print(f"Renamed {file} to {new_name}")

# Change the language code the second part to Uppercase
# e.g. pencil_zh_tw.ts to pencil_zh_TW.ts
for file in os.listdir():
    if file.startswith("pencil_") and file.endswith(".ts"):
        tokens = file.split("_")
        if len(tokens) == 3:
            lang1 = tokens[1]
            lang2 = tokens[2].split(".")[0]
            lang2 = lang2.upper()
            new_name = f"pencil_{lang1}_{lang2}.ts"
            os.rename(file, new_name)
            print(f"Renamed {file} to {new_name}")

# Find the correct pencil2d repository
if os.path.exists("C:/github/pencil"):
    pencil2d_repo = "C:/github/pencil"
elif os.path.exists("D:/github/pencil"):
    pencil2d_repo = "D:/github/pencil"

# Copy the ts files if there is a corresponding file in the pencil/translations directory
for file in os.listdir():
    if file.endswith(".ts"):
        dest_file = pencil2d_repo + "/translations/" + file
        if os.path.exists(dest_file):
            shutil.copy(file, dest_file)
            print(f"Copied {file} to {dest_file}")

# Copy desktop entry
shutil.copy("desktop-entry-en.desktop", pencil2d_repo + "/app/data/org.pencil2d.Pencil2D.desktop")

# Rename mui_po-zh_tw.po to mui_zh_TW.po
# the LANG is the language code
for file in os.listdir():
    if file.startswith("mui_po-") and file.endswith(".po"):
        lang = file.split("-")[-1].split(".")[0]
        langTokens = lang.split("_")
        if len(langTokens) == 2:
            lang1 = langTokens[0]
            lang2 = langTokens[1].upper()
            lang = lang1 + "_" + lang2
        new_name = "mui_" + lang + ".po"  
        os.rename(file, new_name)
        print(f"Renamed {file} to {new_name}")

# Copy mui.po if there is a corresponding file in the app/translations directory
for file in os.listdir():
    if file.startswith("mui_") and file.endswith(".po"):
        dest_file = pencil2d_repo + "/app/translations/" + file
        if os.path.exists(dest_file):
            shutil.copy(file, dest_file)
            print(f"Copied {file} to {dest_file}")

# Rename pencil2d-wxl-xlf-zh_tw.xlf to pencil2d_zh_TW.wxl.xlf
# the LANG is the language code
for file in os.listdir():
    if file.startswith("pencil2d-wxl-xlf-") and file.endswith(".xlf"):
        lang = file.split("-")[-1].split(".")[0]
        langTokens = lang.split("_")
        if len(langTokens) == 2:
            lang1 = langTokens[0]
            lang2 = langTokens[1].upper()
            lang = lang1 + "_" + lang2
        new_name = "pencil2d_" + lang + ".wxl.xlf"  
        os.rename(file, new_name)
        print(f"Renamed {file} to {new_name}")

# Copy wxl.xlf if there is a corresponding file in the pencil2d-wxl directory
for file in os.listdir():
    if file.startswith("pencil2d_") and file.endswith(".wxl.xlf"):
        dest_file = pencil2d_repo + "/util/installer/translations/" + file
        if os.path.exists(dest_file):
            shutil.copy(file, dest_file)
            print(f"Copied {file} to {dest_file}")




