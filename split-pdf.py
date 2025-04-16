import sys
import os
from PyPDF2 import PdfReader, PdfWriter


def parse_ranges(range_str):
    ranges = []
    for part in range_str.split(","):
        if "-" in part:
            start, end = map(int, part.split("-"))
            ranges.append((start, end))
        else:
            num = int(part)
            ranges.append((num, num))
    return ranges


def split_pdf_by_ranges(input_path, output_dir, ranges):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    reader = PdfReader(input_path)
    total_pages = len(reader.pages)

    for i, (start, end) in enumerate(ranges, start=1):
        writer = PdfWriter()
        for page_num in range(start - 1, end):
            if 0 <= page_num < total_pages:
                writer.add_page(reader.pages[page_num])
        output_path = os.path.join(output_dir, f"split_part_{i}.pdf")
        with open(output_path, "wb") as f_out:
            writer.write(f_out)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python split-pdf.py <input_pdf_path> <page_ranges>")
        print("Example: python split-pdf.py file.pdf 1-3,5-7,9")
        sys.exit(1)

    input_pdf = sys.argv[1]
    range_str = sys.argv[2]
    page_ranges = parse_ranges(range_str)
    output_folder = "splits"
    split_pdf_by_ranges(input_pdf, output_folder, page_ranges)

