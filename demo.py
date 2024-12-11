import os
from PyPDF2 import PdfFileMerger

def merge_pdf_files(input_files, output_file):

    merger = PdfFileMerger()

    for file in input_files:
        if not os.path.isfile(file):
            print(f"Warning: 文件 {file} 不存在，将跳过此文件")
            continue

        try:
            merger.append(file)
        except Exception as e:
            print(f"Warning: 在处理文件 {file} 时发生错误：{e}")
            continue


    with open(output_file, "wb") as f:
        merger.write(f)

    print(f"成功将 {len(input_files)} 个PDF文件合并为 {output_file}")

