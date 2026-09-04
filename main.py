from pathlib import Path
import shutil

downloads_path = Path.home() / "Downloads"
sorter = Path.home() / "3D Objects"

def get_unique_path(target_folder: Path, file_name: str) -> Path:
    destination = target_folder / file_name
    
    if not destination.exists():
        return destination

    stem = destination.stem
    suffix = destination.suffix 
    counter = 1

    while destination.exists():
        destination = target_folder / f"{stem} ({counter}){suffix}"
        counter += 1

    return destination

for item in downloads_path.iterdir():
    text_folder = sorter / "Txt"
    pdf_folder = sorter / "Pdf"
    jpg_folder = sorter / "Jpg"
    screenshot_folder = sorter / "Screenshot"
    doc_folder = sorter / "Doc"
    zip_folder = sorter / "Zip"
    exe_folder = sorter / "Exe"
    program_folder = sorter / "Program"
    if item.is_file():
        if item.suffix == ".txt":
            text_folder.mkdir(parents=True, exist_ok=True)
            dest = get_unique_path(text_folder, item.name)
            shutil.move(item, dest)
            print('Переміщено:' + item.name + " В папку Txt")
        elif item.suffix == ".pdf":
            pdf_folder.mkdir(parents=True, exist_ok=True)
            dest = get_unique_path(pdf_folder, item.name)
            shutil.move(item, dest)
            print('Переміщено:' + item.name + " В папку Pdf")
        elif item.suffix == ".jpg" or item.suffix == ".jpeg" or item.suffix == ".png":
            jpg_folder.mkdir(parents=True, exist_ok=True)
            dest = get_unique_path(jpg_folder, item.name)
            shutil.move(item, dest)
            print('Переміщено:' + item.name + " В папку Jpg")
        elif item.suffix == ".doc" or item.suffix == ".docx" or item.suffix == ".xls" or item.suffix == ".xlsx" or item.suffix == ".ppt" or item.suffix == ".pptx":
            doc_folder.mkdir(parents=True, exist_ok=True)
            dest = get_unique_path(doc_folder, item.name)
            shutil.move(item, dest)
            print('Переміщено:' + item.name + " В папку Doc")
        elif item.suffix == ".rar" or item.suffix == ".zip" or item.suffix == ".7z" or item.suffix == ".tar" or item.suffix == ".gz":
            zip_folder.mkdir(parents=True, exist_ok=True)
            dest = get_unique_path(zip_folder, item.name)
            shutil.move(item, dest)
            print('Переміщено:' + item.name + " В папку Zip")
        elif item.suffix == ".exe":
            exe_folder.mkdir(parents=True, exist_ok=True)
            dest = get_unique_path(exe_folder, item.name)
            shutil.move(item, dest)
            print('Переміщено:' + item.name + " В папку Exe")
        elif item.suffix == ".py" or item.suffix == ".pyw" or item.suffix == ".html" or item.suffix == ".css" or item.suffix == ".js":
            program_folder.mkdir(parents=True, exist_ok=True)
            dest = get_unique_path(program_folder, item.name)
            shutil.move(item, dest)
            print('Переміщено:' + item.name + " В папку Program")