import re

COMPILED_PATTERN = re.compile(r"_(.*)\.")


# Challenge
def decode_filename(filename: str) -> str:
    return COMPILED_PATTERN.findall(filename)[0]


if __name__ == "__main__":
    print(decode_filename("2023122512345678_sleighDesign.png.grinchwa"))
    print(decode_filename("42_chimney_dimensions.pdf.hack2023"))
    print(decode_filename("987654321_elf-roster.csv.tempfile"))
