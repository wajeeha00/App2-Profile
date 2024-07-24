import smtplib, ssl, os
def send_email(message):
    host = 'smtp.gmail.com'
    port = 465



    username = 'wajeehaaftab7890@gmail.com'
    # password = 'smjeaxywujnfcqph'
    password = os.getenv('EMAIL_PASSWORD')
    message,sender = message.split('\n')
    receiver_email = username
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver_email, message)

send_email("Hello, this is a test email\nfrom")

