import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(to_addrs, body):
    '''Sends an email to a list of recipients with the specified body content.

    Args:
        to_addrs (List[str]): List of recipient email addresses.
        body (str): The body content of the email.

    Returns:
        None
    '''
    from_addr = "mc7ed6khjmm3my77@ethereal.email"
    login = "mc7ed6khjmm3my77@ethereal.email"
    password = "MdC71Fmn2QTqbAj3QF"

    msg = MIMEMultipart()
    msg["from"] = "viagens_confirmar@email.com"
    msg["to"] = ", ".join(to_addrs)

    msg["subject"] = "Confirmação de Viagem"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(login, password)
    text = msg.as_string()

    for email in to_addrs:
        server.sendmail(from_addr, email, text)

    server.quit()
