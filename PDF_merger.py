from PyPDF2 import PdfFileMerger
import os 

path = r"C:/Users/julie/OneDrive/Bureau/PDF_to_merge/" #We need to create somewhere à directory where we put our PDF to merge and give the path of this directory here
pdf_files = ['1.pdf','2.pdf','3.pdf'] #Here we need the names of the pdf to merge
merger = PdfFileMerger()

for files in pdf_files:
	merger.append(path+files)
if not os.path.exists(path+'merged.pd'):
	merger.write(path+'merged.pdf')
merger.close()

