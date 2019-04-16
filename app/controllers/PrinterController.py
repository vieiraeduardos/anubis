from app import app

from app.models.Printer import Printer
from app.models.Judge import Judge

from flask_mail import Mail
from flask_mail import Message

app.config.update(
        MAIL_SERVER='smtp.gmail.com',
        MAIL_PORT=465,
        MAIL_USE_SSL=True,
        MAIL_USERNAME = 'edusvieirap@gmail.com',
        MAIL_PASSWORD = '@edusvieirap'
        )

mail=Mail(app)


@app.route("/judges/print/")
def print():
    #judges = Judge().getAllJudges()
    judges = [
        {
            "name": "Eduardo",
            "email": "edusvieirap@gmail.com"
        },
        {
            "name": "Eduardo",
            "email": "edusvieirap@gmail.com"
        } 
    ]
    
    for judge in judges:
        printer = Printer()

        filename = printer.print(name=judge["name"])
        
        msg = Message("9º CBTms - Certificado de avaliador", sender="edusvieirap@gmail.com",
        recipients=[judge["email"]])
        
        with app.open_resource(app.static_folder + "/files/" + filename) as fp:
            msg.attach("Certificado.pdf", "application/pdf", fp.read())
            
            msg.html = "Olá,<br>Agradecemos sua participação e grande ajuda na avaliação dos trabalhos submetidos ao 9º Congresso Brasileiro de Telemedicina e Telessaúde / 1º Global Summit & Digital Health.<br>Estamos enviando em anexo o seu certificado de participação.<br><br>Atenciosamente"
            
            mail.send(msg)

    return "Certificados enviados"
