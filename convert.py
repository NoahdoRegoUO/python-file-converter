import os
import ffmpeg

print("\n*** FILE CONVERTER ***")
print("\nTo begin, add the file you wish to convert into the 'input' folder.")
print("\nOnce you are done, press enter.")

input("\n[Press enter to continue]")

for file_name in os.listdir("./input"):
    file_path = "input/" + file_name

    file_name, file_extension = os.path.splitext(file_name)

    print("\nChoose a conversion by entering a number from the list below: ")

    if file_extension == ".mp4":
        print("1: MP4 -> GIF")
        print("2: MP4 -> MP3")
        print("3: MP4 -> MOV")
        conversion = input("Input: ")
    elif file_extension == ".mov":
        print("\n1: MOV -> GIF")
        print("2: MOV -> MP3")
        print("3: MOV -> MP4")
        conversion = input("\nInput: ")
    else:
        conversion = ""
        print("\n** Unsupported file type (" + file_extension + ") **")

    if conversion == "1":
        ffmpeg.input(file_path).output("output/" + file_name + ".gif").run()
    elif conversion == "2":
        ffmpeg.input(file_path).output("output/" + file_name + ".mp3").run()
    elif conversion == "3":
        if file_extension == ".mp4":
            ffmpeg.input(file_path).output("output/" + file_name + ".mov").run()
        else:
            ffmpeg.input(file_path).output("output/" + file_name + ".mp4").run()
    elif conversion == "":
        print("\nSkipping to next file...")
    else:
        print("\n** Invalid input **")
        print("\nSkipping to next file...")

    input("\n[Press enter to continue]")

print("\nNo more files to covert. Program ending.\n")
