import os
import ffmpeg

print(
    """
    *** FILE CONVERTER ***

    To begin, add the file you wish to convert into the "input" folder.

    Once you are done, press enter."""
)

input(
    """
    [Press enter to continue]"""
)

for file_name in os.listdir("./input"):
    file_path = "input/" + file_name

    file_name, file_extension = os.path.splitext(file_name)

    print(
        """
        Choose a conversion by entering a number from the list below: """
    )

    if file_extension == ".mp4":
        conversion = input(
            """
            1: MP4 -> GIF
            2: MP4 -> MP3

            Input: """
        )
    elif file_extension == ".mov":
        conversion = input(
            """
            1: MOV -> GIF
            2: MOV -> MP3

            Input: """
        )
    else:
        conversion = ""
        print(
            """
              ** Unsupported file type **"""
        )

    if conversion == "1":
        ffmpeg.input(file_path).output("output/" + file_name + ".gif").run()
    elif conversion == "2":
        ffmpeg.input(file_path).output("output/" + file_name + ".mp3").run()
    elif conversion == "":
        print(
            """
            Skipping to next file..."""
        )
    else:
        print(
            """
            ** Invalid input **

            Skipping to next file..."""
        )

    input(
        """
        [Press enter to continue]"""
    )

print(
    """
    No more files to covert. Program ending.
    """
)
