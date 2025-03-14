import os
import csv
import schedule
import time

# Load csv configuration file

def load_config():
    config = {}
    with open('paths.csv', 'r', newline='') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader) # Here I am skipping the header row
        for row in csv_reader:
            config[row[0]] = row[1]

    return config

config = load_config()

def is_valid_directory(directory):
    # Check if the given directory is directly listed in the config
    if directory in config.values():
        return False  # Directory is already in the config

    return True  # Directory is not in the config

try:
    def file_organizer():
        allfiles = os.listdir(config['source'])
        print("All Files inside the source folder--", config['source']+"\n\n", allfiles)

        for f in allfiles:
            file_path = os.path.join(config['source'],f)
            print("Full Current File Path:",file_path)

            if "mp3" in f:
                dstMp3_path = os.path.join(config['Music'], f)
                if not os.path.exists(config['Music']):
                    os.makedirs(config['Music'])
                if os.path.exists(dstMp3_path):
                    print(f + " already exists in destination folder.")
                    continue
                # print("dstMp3_path: " + dstMp3_path)
                os.rename(file_path, dstMp3_path)
            
            elif "zip" in f:
                dstZip_path = os.path.join(config['Zip'], f)
                if not os.path.exists(config['Zip']):
                    os.makedirs(config['Zip'])
                if os.path.exists(dstZip_path):
                    print(f + " already exists in destination folder.")
                    continue
                # print("dstZip_path: " + dstZip_path)
                os.rename(file_path, dstZip_path)

            elif "pdf" in f:
                dstPDF_path = os.path.join(config['PDF'], f)
                if not os.path.exists(config['PDF']):
                    os.makedirs(config['PDF'])
                if os.path.exists(dstPDF_path):
                    print(f + " already exists in destination folder.")
                    continue
                # print("dstPDF_path: " + dstPDF_path)
                os.rename(file_path, dstPDF_path)

            elif "docx" in f:
                dstWord_path = os.path.join(config['Word'], f)
                if not os.path.exists(config['Word']):
                    os.makedirs(config['Word'])
                if os.path.exists(dstWord_path):
                    print(f + " already exists in destination folder.")
                    continue
                # print("dstWord_path: " + dstWord_path)
                os.rename(file_path, dstWord_path)
                
            elif "xlsx" in f:
                dstExcel_path = os.path.join(config['Excel'], f)
                if not os.path.exists(config['Excel']):
                    os.makedirs(config['Excel'])
                if os.path.exists(dstExcel_path):
                    print(f + " already exists in destination folder.")
                    continue
                # print("dstExcel_path: " + dstExcel_path)
                os.rename(file_path, dstExcel_path)
                
            elif "csv" in f:
                dstCSV_path = os.path.join(config['CSV'], f)
                if not os.path.exists(config['CSV']):
                    os.makedirs(config['CSV'])
                if os.path.exists(dstCSV_path):
                    print(f + " already exists in destination folder.")
                    continue
                # print("dstCSV_path: " + dstCSV_path)
                os.rename(file_path, dstCSV_path)
            
            elif "ppt" in f:
                dstPPT_path = os.path.join(config['PPT'], f)
                if not os.path.exists(config['PPT']):
                    os.makedirs(config['PPT'])
                if os.path.exists(dstPPT_path):
                    print(f + " already exists in destination folder.")
                    continue
                # print("dstPPT_path: " + dstPPT_path)
                os.rename(file_path, dstPPT_path)
            
            elif ("exe" in f) or ("msi" in f):
                dstInstallers_path = os.path.join(config['Installers'], f)
                if not os.path.exists(config['Installers']):
                    os.makedirs(config['Installers'])
                if os.path.exists(dstInstallers_path):
                    print(f + " already exists in destination folder.")
                    continue
                # print("dstInstallers_path: " + dstInstallers_path)
                os.rename(file_path, dstInstallers_path)

            
            elif ("png" in f) or ("jpg" in f) or ("jpeg" in f):
                dstIMG_path = os.path.join(config['IMG'], f)
                if not os.path.exists(config['IMG']):
                    os.makedirs(config['IMG'])
                if os.path.exists(dstIMG_path):
                    print(f + " already exists in destination folder.")
                    continue
                # print("dstIMG_path: " + dstIMG_path)
                os.rename(file_path, dstIMG_path)

            elif ("mp4" in f):
                dstVideo_path = os.path.join(config['Video'], f)
                if not os.path.exists(config['Video']):
                    os.makedirs(config['Video'])
                if os.path.exists(dstVideo_path):
                    print(f + " already exists in destination folder.")
                    continue
                # print("dstVideo_path: " + dstVideo_path)
                os.rename(file_path, dstVideo_path)
            
            elif os.path.isdir(file_path):
                if not is_valid_directory(file_path):
                    print("Folder should not be moved")
                else:
                    dstFolder_path = os.path.join(config['Folder'], f)
                    if not os.path.exists(config['Folder']):
                        os.makedirs(config['Folder'])
                    if os.path.exists(dstFolder_path):
                        print(f + " already exists in destination folder.")
                        continue
                    os.rename(file_path, dstFolder_path)


except Exception as e:
    print("Exception found in the fie_organizer function:", e)


schedule.every(0.1).minutes.do(file_organizer)

while True:
    schedule.run_pending()
    time.sleep(1)
