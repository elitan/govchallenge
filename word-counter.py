import os
import time
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter#process_pdf
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO


def pdf_to_text(pdfname):

	# PDFMiner boilerplate
	rsrcmgr = PDFResourceManager()
	sio = StringIO()
	codec = 'utf-8'
	laparams = LAParams()
	device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
	interpreter = PDFPageInterpreter(rsrcmgr, device)

	# Extract text
	fp = open(pdfname, 'rb')
	for page in PDFPage.get_pages(fp):
		interpreter.process_page(page)
	fp.close()

	# Get text from StringIO
	text = sio.getvalue()

	# Cleanup
	device.close()
	sio.close()

	return text

def main():

	agencies = [
		'forsakringskassan',
		'migrationsverket',
		'polisen',
		'pensionsmyndigheten',
		'skolverket',
		'forsvarsmakten',
	]

	for agency in agencies:

		print('agency: ', agency)

		for root, dirs, files in os.walk('./year-reports/{}'.format(agency)):

			for file in files:

				# skip non pdf files
				if not file.endswith('.pdf'):
					continue

				pdf_text = pdf_to_text(os.path.join(root, file))

				word_count = {
					'problem': 0,
					'utmaning': 0,
					'lösning': 0,
				}

				for word in word_count.keys():
					word_count[word] += pdf_text.lower().count(word)

				print('year: ', file)
				print(word_count)
				print('')

if __name__ == '__main__':
    main()
