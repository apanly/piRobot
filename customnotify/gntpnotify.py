from gntp import notifier

class gntpnotify:
    def __init__(self):
        pass
    def ownnotify(self):
        #notifications using growl
        growl = notifier.GrowlNotifier(
            applicationName = "piRobot",
            notifications = ["Speech","New Updates","New Messages"],
            defaultNotifications = ["Speech"]
            # hostname = "computer.example.com", # Defaults to localhost
            # password = "123456" # Defaults to a blank password
        )
        growl.register()
        # Send one message
        growl.notify(
            noteType = "New Messages",
            title = "You have a new message",
            description = "A longer message description",
            icon = "http://www.baidu.com/img/bdlogo.gif",
            sticky = False,
            priority = 1,
        )
        growl.notify(
            noteType = "New Updates",
            title = "There is a new update to download",
            description = "A longer message description",
            icon = "http://www.baidu.com/img/bdlogo.gif",
            sticky = False,
            priority = -1,
        )