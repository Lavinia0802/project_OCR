# Image Text Extractor (OCR)

A lightweight Python script that extracts text from images using Optical Character Recognition (OCR) and saves the output to a UTF-8 encoded `.txt` file. Powered by [EasyOCR](https://github.com/JaidedAI/EasyOCR), it supports both Romanian and English text out of the box.

## Features

* **Bilingual Recognition:** Accurately detects Romanian (including diacritics like `ă, â, î, ș, ț`) and English text simultaneously.
* **Clean Text Output:** Saves extracted lines directly into a plain text file (`result.txt`) with proper UTF-8 encoding.
* **CPU Friendly:** Configured to run on standard CPUs without requiring a dedicated GPU.

## Prerequisites

* Python 3.8 or higher
* `pip` (Python package manager)

## Installation

1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/Lavinia0802/project_OCR.git](https://github.com/Lavinia0802/project_OCR.git)
   cd project_OCR
