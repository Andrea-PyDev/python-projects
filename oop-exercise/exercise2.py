
from abc import ABC, abstractmethod

class Notifier(ABC):
    def send(self,recipient,message):
        self.validate(recipient)
        formatted = self.format_message(message)
        self.deliver(formatted,recipient)
        self.log(recipient,message)

    def validate(self,recipient):
        if not recipient:
            raise InvalidRecipientError("Invalid Recipient Error")
        else:
            print(f"{recipient} is validated")
    
    @abstractmethod
    def format_message(self,message):
        pass
        

    @abstractmethod
    def deliver(self,formatted,recipient):
         pass

    def log(self,recipient,message):
        print(f"{recipient}| {message}")
    
class InvalidRecipientError(Exception):
        pass


class EmailNotifier(Notifier):
     def format_message(self, message):
          return f"<html><body><p>{message}</p></body></html>"
     
     def deliver(self,formatted,recipient):
          print(f"{formatted} to {recipient}")
     
     

class SMSNotifier(Notifier):
     def format_message(self,message):
          sliced_message = message[:160]
          return sliced_message
     
     def deliver(self,formatted,recipient):
          print(f"{formatted} to {recipient}")


class PushNotifier(Notifier):
     def format_message(self,message):
          title_body = {"Title": message[:20], "Body": message}
          return title_body
     
     def deliver(self,formatted,recipient):
          print(f"{formatted} to {recipient}")


class NotificationService:
    def __init__(self,notifiers):
        self.notifiers = notifiers

    def broadcast(self,recipient,message):
         for notifier in self.notifiers:
            notifier.send(recipient,message)

if __name__ == "__main__":
    email = EmailNotifier()
    sms = SMSNotifier()
    push = PushNotifier()
    service = NotificationService([email,sms,push])
    service.broadcast("WebCompany","Welcome to Internet")
    try:
        service.broadcast("","")
    except InvalidRecipientError as e:
         print(e)

     


     



         
    