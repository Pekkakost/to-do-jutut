import PySimpleGUI as sg
import zipfile
import pathlib

def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, "w") as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

label1 = sg.Text("Select files to compress: ")
input1 = sg.Input(key="files")
choose_button1 = sg.FilesBrowse("Choose", key="files")

label2 = sg.Text("Select destination folder: ")
input2 = sg.Input(key="folder")
choose_button2 = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")
output_label = sg.Text("", key="output")

layout = [[label1, input1, choose_button1],
          [label2, input2, choose_button2],
          [compress_button, output_label]]

window = sg.Window("File Compressor", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Compress":
        filepaths = values["files"].split(";")
        folder = values["folder"]
        make_archive(filepaths, folder)
        window["output"].update(value="Compression completed")

window.close()
