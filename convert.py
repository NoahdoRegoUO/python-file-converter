import os
import ffmpeg

input_files = "input"

print(
    """
      *** FILE CONVERTER ***

      To begin, add the file you wish to convert into the "input" folder.

      Once you are done, press enter.
      """
)

input("[Press enter]")

for filename in os.listdir(input_files):
    filepath = "input/" + filename

    print(
        """
        Choose a conversion by entering a number from the list below
        1: MP4/MOV -> GIF
        2: MP4/MOV -> MP3
        """
    )

    conversion = input("Conversion: ")

    ffmpeg.input(filepath).output("input.gif").run()
