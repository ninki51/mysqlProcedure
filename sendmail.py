#!/usr/local/bin/python3.5
# coding=gbk
from email.mime.text import MIMEText
from smtplib import SMTP_SSL
import time
import warnings
warnings.filterwarnings("ignore")

msg = MIMEText('hello,send by Python...','html','utf-8')

mail_info = {
        'From':'admin@wfw99.com',
        'Password':'aotofx1234',
        'To':'2556792125@qq.com',
        'Mail_server':'smtp.163.com',
}


if __name__ == '__main__':
        smtp = SMTP_SSL(mail_info['Mail_server'])

        smtp.ehlo(mail_info['Mail_server'])
        smtp.login(mail_info['From'],mail_info['Password'])

        str = 'AOTOFX部分产品保证金政策调整通知...'
        msg = MIMEText(str,'html','utf-8')
        msg['Subject'] = 'AOTO FX 部分产品保证金政策调整通知'
        msg['From'] = mail_info['From']
        msg['To'] = mail_info['To']


        arr = ['2556792125@qq.com','12345678@qq.com']

        for to in arr:
            smtp.sendmail(mail_info['From'], to, msg.as_string())
            print(to)
            time.sleep(10.0)
        smtp.quit()