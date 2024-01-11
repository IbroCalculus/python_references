import PyPDF2

#Visit https://realpython.com/pdf-python/ for more. ie: Rotate, merge, split, add watermark, encrypt pdf etc

#NB: Some pdf document I observed, can't be read properly, generating errors sometimes
# E.g: pdfbook.pdf when it comes to reader.getDocumentInfo



with open('pdfbook1.pdf', 'rb') as fileObj:

    # 1. ===========    Read pdf file   ===========
    reader = PyPDF2.PdfFileReader(fileObj)
    print(f'THE NUMBER OF PAGES ARE: {reader.numPages}')    # OR reader.getNumPages()
    print('=========================== END =========================\n')


    # 2. ===========    Read Particular Page. (Page count starts from zero)   ===========
    Page4 = reader.getPage(10)
    Page = Page4.extractText()
    print(f'THE CONTENT OF PAGE 4 is:\n {Page}')
    print('=========================== END =========================\n')


    # #3. ==========  Extract document info from PDF  ===================
    #Extractable info are: Author, Creator, Producer, Subject, Title, Number of Pager

    numberOfPages = str(reader.getNumPages())
    info = reader.getDocumentInfo()
    author = info.author
    creator = info.creator
    producer = info.producer
    subject = info.subject
    title = info.title


    print(f'The number of pages in the PDF are: {numberOfPages}')
    print(f'The Author of this PDF is: {author}')
    print(f'The Creator of this PDF is: {creator}')
    print(f'The Producer of this PDF is: {producer}')
    print(f'The Subject of this PDF is: {subject}')
    print(f'The Title of this PDF is: {title}')

    print('=========================== END =========================\n')


# fileObj = open('PDFBook.pdf', 'rb')
# reader = PyPDF2.PdfFileReader(fileObj)
# print(f'The number of pages: {reader.numPages}')
