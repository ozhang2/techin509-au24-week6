from notifications import NotificationMethod

class SMSNotification(NotificationMethod):
    def send(self, message):
        # use Twilio API

        pr