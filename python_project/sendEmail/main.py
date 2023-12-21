# This project is read the excel and send email
# Version 1.0.0 - Initial Release
    #Added basic functionality for sending email
    #The structure and the Compatibility should be improved

import numpy as np
import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.header import Header #Header是用来构建邮件
from email.mime.base import MIMEBase
from email import encoders
import time      #时间模块
import os,sys
import jinja2

tips = """tips"""
connect_detail = """connect_detail"""
detail_content = """detail_content"""
 
#数据
data_name= []
data_email = []
data_content = []

# 网易/Gmail第三方 SMTP 服务
WANGYI = False
GMAIL = True

if WANGYI:
    mail_port = 465
    mail_host = "smtp.163.com"        
    mail_user = "xxx@163.com"            
    mail_pass = "xxx"   
    sender = 'xxx@163.com'       

if GMAIL:
    mail_port = 587
    mail_host = "smtp.gmail.com:587"  
    mail_user = "xxx@gmail.com"
    mail_pass = "xxx"  
    sender = 'xxx@gmail.com'   


# 发送邮件
def sendEmailMsg(msg, receivers):

    try:
        if WANGYI:
            smtpObj = smtplib.SMTP_SSL(mail_host, mail_port) 

        if GMAIL:
            smtpObj = smtplib.SMTP(mail_host)
            smtpObj.ehlo()
            smtpObj.starttls()

        smtpObj.login(mail_user, mail_pass) 
        smtpObj.sendmail(sender,receivers, msg.as_string())
        print("mail has been send successfully.")
        smtpObj.quit()

    except smtplib.SMTPException as e:
        print('error', e)

def sendEmail(content, title, receivers):
    message = MIMEText(content, 'plain', 'utf-8') 
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title
 
    try:
        if WANGYI:
            smtpObj = smtplib.SMTP_SSL(mail_host, mail_port) 

        if GMAIL:
            smtpObj = smtplib.SMTP(mail_host)
            smtpObj.ehlo()
            smtpObj.starttls()
        
        smtpObj.login(mail_user, mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string()) 
        print("mail has been send successfully.")
        smtpObj.quit()

    except smtplib.SMTPException as e:
        print('error', e)

def addPicture(path, picturePath, title,receivers):
    #加入图片
    msg = MIMEMultipart()
    msg['Subject'] = title
    msg['From'] = "{}".format(sender)
    msg['To'] = ",".join(receivers)
    
    #正文-图片 只能通过html格式来放图片
    htmlFile = """\
    <html>
        <head></head>
        <body>
            <pre style="font-family:arial;margin:left;">
            Tips:xxx
            <img src="cid:image1">
            </pre>
        </body>
    </html>
    """
    htmlpart = MIMEText(htmlFile,'html','utf-8')
    msg.attach(htmlpart)
    
    os.chdir(path)
    #在正文中显示图片
    File1 = str(path + '/' + picturePath)
    image = MIMEImage(open(File1,'rb').read(),File1.split('.')[-1])
    # 定义图片 ID，在 HTML 文本中引用
    image.add_header('Content-ID','<image1>')
    msg.attach(image)
    
    # 附件中含有图片
    # image_file = open(r'','rb').read()
    # pic = MIMEImage(image_file)
    # pic.add_header('Content-Disposition','attachment',filename='接机群.jpg')
    # msg.attach(pic)

    return msg
       
def getExcelInfo(start,end):
    global data_name
    global data_email
    global data_content
    data=pd.read_excel(r'test.xlsx', 
                        sheet_name= 0,
                        header=0)
    
    data_name=data.loc[start:end,"姓名"]
    data_email=data.loc[start:end,"邮箱"]
    data_content=data.iloc[start:end, -2]

if __name__ == '__main__':

    dir = './sendEmail/tmp'  #need add the full path
    pictureName = 'test.png' #need change the name

    start_origin = 2 #the start row in the excel
    end_origin = 2 #the end row in the excel

    start_send = start_origin -2
    end_send = end_origin - 2 + 1

    getExcelInfo(start_send,end_send)

    data_name_list= list(data_name)
    data_email_list = list(data_email)
    data_content_list = list(data_content)

    data_email_test = ['xxx@gmail.com']

    print(end_send - start_send)

    for i in range(end_send - start_send):
        # receiver = [str(data_email_test[i])]
        receiver = [str(data_email_list[i])]

        title = 'To ' + data_name_list[i] + ': tips'
        title2 = 'To ' + data_name_list[i] + ': tips'
        content = "To %s:\n" %(data_name_list[i]) + "\n%s\n" %(tips) + "\n%s\n" %(data_content_list[i]) + "\n%s\n" %(detail_content) + "\n%s\n"  %(connect_detail) + "\nFrom Tianfu \n"
        
        sendEmail(content, title, receiver)

        msg = addPicture(dir, pictureName, title2, receiver)
        sendEmailMsg(msg, receiver)

        print(receiver)
        print("Num: " + str(start_origin + i) + "\n" + title)
        time.sleep(1)


