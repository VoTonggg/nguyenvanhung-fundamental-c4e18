from gmail import GMail, Message
from random import choice
import datetime

gmail = GMail('VoTong <englishsiteforkid@gmail.com', 'tonghen97')

html_content = """
<p style="text-align: center;"><strong>C&ocirc;ng h&ograve;a x&atilde; hội chủ nghĩa Việt Nam</strong></p>
<p style="text-align: center;"><strong>Độc lập - Tự do - Hạnh ph&uacute;c</strong></p>
<p style="text-align: center;">&nbsp;</p>
<p style="text-align: center;"><strong>ĐƠN XIN NGHỈ HỌC</strong></p>
<p style="text-align: left;">K&iacute;nh gửi : thầy gi&aacute;o chủ nhiệm bộ m&ocirc;n tin học lớp c4e</p>
<p style="text-align: left;">K&iacute;nh gửi : hiệu trưởng trường techkids</p>
<p style="text-align: left;">T&ecirc;n em l&agrave; V&otilde; T&ograve;ng</p>
<p style="text-align: left;">H&ocirc;m nay em viết đơn n&agrave;y xin thầy gi&aacute;o v&agrave; nh&agrave; trường cho ph&eacute;p em được nghỉ học buổi h&ocirc;m nay, l&yacute; do l&agrave; v&igrave; {{reason}}</p>
<p style="text-align: left;">Em hứa sẽ học b&agrave;i v&agrave; l&agrave;m b&agrave;i đầy đủ.&nbsp;</p>
<p style="text-align: left;">Em xin ch&acirc;n th&agrave;nh c&aacute;m ơn !</p>
<p style="text-align: left;">V&otilde; T&ograve;ng</p>
 """

reasons = ["ay chia", "sot xuat huyet", "gay chan", "ban gai om"]

html_content_to_send = html_content.replace("{{reason}}", choice(reasons))

msg = Message('Don Xin Nghi Hoc', to = '20130075@student.hust.edu.vn', html = html_content_to_send)

now = datetime.datetime.now()

while True:
    if now.hour > 19:
        gmail.send(msg)
        print("Done")
        break
    else:
        print("Running ... ( still too early to send )")
