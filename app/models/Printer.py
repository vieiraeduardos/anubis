import os
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import date
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader

from app import app

from flask import send_from_directory

UPLOAD_FOLDER = "/home/nigellima/Music/anubis/app/static/files/"

class Printer():
    def __init__(self):
        pass

    def print(self, name):
        filename = generate_password_hash("form_letter") + ".pdf"
        logo = app.static_folder + "/files/" + "certificado.png"

        logo = ImageReader(logo)
        canvas = Canvas(UPLOAD_FOLDER + filename)
        canvas.setPageSize((1100, 800))
        canvas.drawImage(logo, 20, 20, mask='auto')
        canvas.setFont('Helvetica-Bold', 14)
        canvas.setFillColorRGB(0, 0, 0)
        canvas.drawString(100, 500, "Certificamos que %s foi avaliador dos trabalhos científicos, na modalidade e-pôsteres, apresentados" % (name))
        canvas.drawString(60, 450, "durante o 9º Congresso Brasileiro de Telemedicina e Telessaúde - 9º CBTms / 1º Global Summit Telemedicine & Digital Health")
        canvas.drawString(60, 400, "realizado no período de 03/04/2019 a 07/04/2019, na cidade de São Paulo (SP).")

        canvas.showPage()
        canvas.save()

        return filename
