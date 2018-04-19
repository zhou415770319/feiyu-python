import os
from django.core.mail import send_mail

os.environ['DJANGO_SETTINGS_MODULE'] = 'feiyu.settings'

if __name__ == '__main__':

    send_mail(
        '来自www.zhoufeiblog.com的测试邮件',
        '欢迎访问www.zhoufeiblog.com，这里是周飞的站点，本站专注于技术的分享！',
        'zhou415770319@163.com',
        ['415770319@qq.com'],
    )