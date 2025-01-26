import FreeSimpleGUI as sg
import os
from pathlib import Path
import shutil


homeDir = Path.home()
userPath = homeDir/"AppData"/"Local"/"SnuggetSaveCopier"
userPath.mkdir(parents=True,exist_ok=True)


layout = [
    [sg.Text("Select Original Save File")],
    [sg.Input(key="originSaveFile"), sg.FileBrowse(initial_folder = homeDir),sg.Button("Clear")],
    [sg.Text(key="userMessage")],
    [sg.Button("Copy Save"), sg.Button("Restore Save"), sg.Button("Go to Copier Files")],
]

window = sg.Window("Snuget's Simple Save Copier",layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    if event == "Clear":
        window["originSaveFile"].update("")
    if event == "Go to Copier Files":
        os.startfile(userPath)
    if event == "Copy Save":
        if not values["originSaveFile"]:
            continue
        saveFileLocation = Path(values["originSaveFile"])
        backupFileName = f"new_{saveFileLocation.name}"
        shutil.copy(saveFileLocation,userPath)
        shutil.copy(saveFileLocation, userPath / backupFileName)

        window["userMessage"].update("File Copied",text_color="yellow")
    if event == "Restore Save":
        if not values["originSaveFile"]:
            continue
        saveFileLocation = Path(values["originSaveFile"])
        restoreFile = f"{saveFileLocation.name}"
        shutil.copy(userPath / restoreFile, saveFileLocation)
        window["userMessage"].update("File Restored",text_color="yellow")

