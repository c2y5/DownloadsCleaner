from os import path, mkdir
import os
import pathlib
import shutil

user = path.expanduser("~")
downloadsPath = path.join(user, "Downloads")

folders = {
    "picFolder": path.join(downloadsPath, "Pictures"),
    "exeFolder": path.join(downloadsPath, "Executables"),
    "compressedFolder": path.join(downloadsPath, "Compressed"),
    "txtDoc": path.join(downloadsPath, "Text Documents"),
    "audioFolder": path.join(downloadsPath, "Audios"),
    "vidsFolder": path.join(downloadsPath, "Videos"),
    "dscFolder": path.join(downloadsPath, "Disc & Medias"),
    "dbFolder": path.join(downloadsPath, "Database"),
    "progFolder": path.join(downloadsPath, "Codes"),
    "others": path.join(downloadsPath, "Others"),
}

fileTypes = {
    "picFolder": [".ai", ".bmp", ".gif", ".ico", ".jpeg", ".png", ".jpg", ".ps", ".psd", ".svg", ".tif", ".tiff", ".webp"],
    "exeFolder": [".apk", ".bat", ".cgi", ".pl", ".com", ".exe", ".gadget", ".jar", ".msi"],
    "compressedFolder": [".7z", ".arj", ".deb", ".pkg", ".rar", ".rpm", ".tar.gz", ".z", ".zip"],
    "txtDoc": [".doc", ".docx", ".odt", ".pdf", ".rtf", ".tex", ".txt", ".wpd"],
    "audioFolder": [".aif", ".cda", ".mid", ".midi", ".mp3", ".ogg", ".wav", ".wma", ".wpl"],
    "vidsFolder": [".mp4", ".mov", ".avi", ".wmv", ".avchd", ".webm", ".flv"],
    "dscFolder": [".bin", ".dmg", ".iso", ".toast", ".vcd"],
    "dbFolder": [".csv", ".dat", ".db", ".dbf", ".log", ".mdb", ".sav", ".sql", ".tar", ".xml"],
    "progFolder": [".c", ".class", ".cpp", ".cs", ".h", ".java", ".php", ".py", ".sh", ".swift", ".vb", ".vbs", ".js", ".html", ".java", ".css", ".htm", ".xhtml", ".rs"],
}

for x in folders:
    if not path.exists(folders[x]):
        print(f"Creating Folders: {folders[x]}")
        mkdir(folders[x])

items = [f for f in os.listdir(downloadsPath) if path.isfile(path.join(downloadsPath, f))]
files = []

for item in items:
    files.append(path.join(downloadsPath, item))

for file in files:
    suffix = pathlib.Path(file).suffix
    fileType = None

    for filetype in fileTypes:
        if suffix in fileTypes[filetype]:
            fileType = filetype

    if fileType is None:
        fileType = "others"

    dest = folders[fileType]
    shutil.move(file, path.join(dest, path.basename(file)))
