import pdfkit

path_wkthmltopdf = "E:\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf = path_wkthmltopdf)

pdfkit.from_url("http://google.com", "out.pdf", configuration=config)
