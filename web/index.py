    #encoding: utf-8
import tornado.ioloop
import tornado.web
import xml.etree.ElementTree as ET
import serial
import os
import binascii

msg=0
all_buttons=0

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<title>家用万能WEB遥控系统</title>'
        '<meta name="viewport" content="width=device-width, initial-scale=1″/>'
        '<html><body><form action="/" method="post">'
        '<table><tr>'
        '<td><input type="submit" style="background:#ADFF2F" name="message" value="电视机开关"></td>'
        '<td><input type="submit" style="background:#FFA500″ name="message" value="静 音"></td>'
        '<td><input type="submit" style="background:#FF0000″ name="message" value="机顶盒开关"></td>'
        '</tr><tr>'
        '<td><input type="submit" name="message" value="1"></td>'
        '<td><input type="submit" name="message" value="2"></td>'
        '<td><input type="submit" name="message" value="3"></td>'
        '</tr><tr>'
        '<td><input type="submit" name="message" value="4"></td>'
        '<td><input type="submit" name="message" value="5"></td>'
        '<td><input type="submit" name="message" value="6"></td>'
        '</tr><tr>'
        '<td><input type="submit" name="message" value="7"></td>'
        '<td><input type="submit" name="message" value="8"></td>'
        '<td><input type="submit" name="message" value="9"></td>'
        '</tr><tr>'
        '<td></td>'
        '<td><input type="submit" name="message" value="0"></td>'
        '<td></td>'
        '</tr><tr>'
        '<td><input type="submit" name="message" value="菜 单"></td>'
        '<td><input type="submit" name="message" value="频道 +"></td>'
        '<td><input type="submit" name="message" value="点 播"></td>'
        '</tr><tr>'
        '<td><input type="submit" name="message" value="音量 -"></td>'
        '<td><input type="submit" name="message" value="确 定"></td>'
        '<td><input type="submit" name="message" value="音量 +"></td>'
        '</tr><tr>'
        '<td><input type="submit" name="message" value="返 回"></td>'
        '<td><input type="submit" name="message" value="频道 -"></td>'
        '<td><input type="submit" name="message" value="退 出"></td>'
        '</tr></table>'
        '</form></body></html>')

    def post(self):
        global ser
        global all_buttons
        global binascii
        msg=self.get_argument("message")
        #root = ET.parse(“button.xml").getroot()
        #all_buttons = root.findall('button')
        for button in all_buttons:
            if(msg == button.find('name').text):
                value=button.find('value').text
                print(value)
                valuebyte=value.encode()
                print(binascii.b2a_hex(value))
                ser.write(valuebyte)
                MainHandler.get(self)

settings = {
"static_path": os.path.join(os.path.dirname(__file__), "static"),
}
application = tornado.web.Application([
(r"/", MainHandler),
(r"/(favicon\.ico)", tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
],**settings)

if __name__ == "__main__":
    application.listen(8888)
    #ser=serial.Serial('/dev/ttyUSB0′,9600)
    #ser=serial.Serial('com8′,9600)
    all_buttons = ET.parse("button.xml").getroot().findall('button')
    tornado.ioloop.IOLoop.instance().start()
