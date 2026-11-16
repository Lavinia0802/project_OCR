import easyocr

def extract_and_save_text(image_path, output_file="result.txt"):
    reader = easyocr.Reader(["ro", "en"], gpu=False)
    results = reader.readtext(image_path, detail=0)

    with open(output_file, "w", encoding="utf-8") as file:
        for line in results:
            file.write(line + "\n")

    print(f"Done! Text saved to '{output_file}'.")

if __name__ == "__main__":
    extract_and_save_text("image.jpg", "result.txt")