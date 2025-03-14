# File Organizer

A Python-based automated file organization tool that categorizes files from a source directory into specific destination directories based on their file types. The program runs on a scheduled basis and supports a wide range of file extensions.

---

## Features

- Automatically organizes files from a source directory into categorized folders.
- Supports the following file types:
  - **Audio Files** (`.mp3`)
  - **Compressed Files** (`.zip`)
  - **Documents** (`.pdf`, `.docx`, `.xlsx`, `.csv`, `.ppt`)
  - **Executable Files** (`.exe`, `.msi`)
  - **Image Files** (`.png`, `.jpg`, `.jpeg`)
  - **Video Files** (`.mp4`)
  - **Folders**
- Skips processing for invalid directories (directories mentioned in the paths csv).
- If there is already a file with the same name as the file to be moved, the file is moved but renamed by adding a timestamp suffix (format: filename_ddMMyyyy_hhmm)
- Dynamically creates destination folders if they don’t exist.
- Runs on a schedule (every 6 seconds in the current setup).

---

## Prerequisites

Before running the program, ensure you have the following installed:

1. **Python** (version 3.6 or higher)
2. Required Python libraries:  
   - `schedule`  
   - `os`  
   - `csv`  
   - `time`

You can install missing dependencies using pip:
pip install schedule or pip install -r requirements.txt
