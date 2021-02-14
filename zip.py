def zip():
    answer_yes_list = ["yes", "yes", "y", "ye"]

    userzip = input("Do you want to zip all files and directories in the current folder? Yes or No?")

    if userzip.lower() not in answer_yes_list:
        print("Stopping zip process")
        return

    for entry in os.scandir(sys.path[0]):
        if entry.is_dir():
            dir_path = Path(sys.path[0] + '/' + entry.name)
            with ZipFile(sys.path[0] + '/organized.zip', 'w') as zip:
                zip.write(dir_path, entry.name)
                zip_path = entry.name + "/"
                zip_recursively(dir_path, zip, zip_path)
        else:
            continue
        
def zip_recursively(dir_path, zip, zip_path):
    for entry in os.scandir(dir_path):
        current_dir_path = Path(str(dir_path) + "/" + entry.name)

        if entry.is_dir():
            zip.write(current_dir_path, entry.name)
            zip_path = entry.name + "/"

            # Process all files in current_dir_path recursively
            zip_recursively(current_dir_path, zip, zip_path)
        else:
            file_zip_path = zip_path + "/" + entry.name
            zip.write(current_dir_path, file_zip_path)
        break

#start of the script
if __name__ == "__main__":
    zip()
