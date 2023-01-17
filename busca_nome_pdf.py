import os
import PyPDF2
import sys

if len(sys.argv) != 2:
    print("Uso: ", sys.argv[0].split('/')[-1], " <nome_buscado>")
    exit(0)

nome_buscado = sys.argv[1]

arquivos = sorted(os.listdir())
total = len(arquivos)
comprimento = len(str(total))
lidos = 0
for arquivo in arquivos:
    lidos += 1
    print("Processados", str(lidos).zfill(comprimento), "de", total, end='\r')

    try:
        reader = PyPDF2.PdfReader(arquivo)
    except:
        continue

    for page in reader.pages:
        if nome_buscado.upper() in page.extract_text().upper():
            print("Termo encontrado em:", arquivo)
            break

