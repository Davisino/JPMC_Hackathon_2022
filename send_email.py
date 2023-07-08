import win32com.client

def send_email(receiver)
    outlook = win32com.client.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = receiver
    mail.Subject = 'Sample Email without pop up'
    mail.HTMLBody = '<h3>This is HTML Body</h3>'
    mail.Body = "This is the normal body"
    mail.Send()

send_email('example@yahoo.com')