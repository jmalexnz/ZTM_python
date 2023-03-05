# Working with PyPDF2
import PyPDF2
import sys

def pdf_playground():
    with open(r".//pdf_files//dummy.pdf", 'rb') as file:
        # rb = read binary
        reader = PyPDF2.PdfFileReader(file)
        print(reader.numPages)
        print(reader.getPage(0))
        page = reader.getPage(0)
        page.rotateClockwise(180)
        writer = PyPDF2.PdfFileWriter()
        writer.addPage(page)
        with open(".//pdf_files//tilt.pdf", 'wb') as new_file:
            writer.write(new_file)


def merge_pdfs(pdf_list):
    ''' Merge the listed PDFS'''
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('.//pdf_files//super_pdf.pdf')

def watermark_pdf(pdf_path, watermark_file):
    ''' 
    add a watermark to pdf file
    '''
    pdf = PyPDF2.PdfFileReader(pdf_path)
    watermark = PyPDF2.PdfFileReader(watermark_file)
    watermark_pg = watermark.getPage(0)

    marked_pdf = PyPDF2.PdfFileWriter()
    for i in range(pdf.numPages):
        page = pdf.getPage(i)
        page.mergePage(watermark_pg)
        marked_pdf.addPage(page)
    with open('.//pdf_files//watermarked.pdf', 'wb') as new_file:
        marked_pdf.write(new_file) 


if __name__ == "__main__":
    # pdf_list = sys.argv[1:]
    # merge_pdfs(pdf_list)

    pdf_file = sys.argv[1]
    watermark_file = sys.argv[2]
    watermark_pdf(pdf_file, watermark_file)