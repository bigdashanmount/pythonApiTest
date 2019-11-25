# coding:utf-8

import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.utils import formataddr
from configs.config_reader import ReadConfig


class Email:
    def __init__(self):
        self._user = ReadConfig().get_email("sender_username")
        self._pwd = ReadConfig().get_email("sender_password")
        self.now = time.strftime("%Y-%m-%d")

    def send_attach(self, receive_users, email_title, html_report_path, html_report_name):
        f = open(html_report_path, 'rb')
        mail_body = f.read()
        f.close()
        msg = MIMEMultipart()
        msg["Subject"] = '%s %s' % (email_title, str(self.now))
        msg["From"] = formataddr([u"QA", self._user])
        msg["To"] = ",".join(receive_users)
        part = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        msg.attach(part)
        if html_report_path is not None:
            attach = MIMEApplication(open(html_report_path, 'rb').read())
            attach.add_header('Content-Disposition', 'attachment', filename=html_report_name)
            msg.attach(attach)
        else:
            pass
        s = smtplib.SMTP(ReadConfig().get_email("host"), ReadConfig().get_email("port"))
        s.starttls()
        s.login(self._user, self._pwd)
        s.sendmail(self._user, receive_users, msg.as_string())
        s.close()

    def send(self, e_users, e_title, e_content):

        msg = MIMEText(e_content, _subtype='html', _charset='utf-8')
        msg["Subject"] = '%s %s' % (e_title, str(self.now))
        msg["From"] = formataddr([u"QA", self._user])
        msg["To"] = ",".join(users)
        try:
            s = smtplib.SMTP(ReadConfig().get_email("host"), ReadConfig().get_email("port"))
            s.starttls()
            s.login(self._user, self._pwd)
            s.sendmail(self._user, e_users, msg.as_string())
            s.close()
        except smtplib.SMTPException:
            print("发送邮件失败！")


if __name__ == "__main__":
    # 若从配置文件读取收件人，先要将str转换为list
    # receive_users = eval(ReadConfig().get_email("receive_users"))
    users = ["137775605@qq.com"]
    title = ReadConfig().get_email("email_title")
    content = ReadConfig().get_email("email_content")
    report_path = ReadConfig().get_report("html_report_path")
    report_name = ReadConfig().get_report("html_report_name")
    project_name = ReadConfig().get_project("project_name")
    full_title = project_name + title
    e = Email()
    # e.send_attach(users, full_title, report_path, report_name)
    e.send(users, title, content)


