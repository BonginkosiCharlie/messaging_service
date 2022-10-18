from message_service import MessageService
if __name__ == '__main__':
    message_service = MessageService("bonginkosimtyali@gmail.com", "Password123", "distribution@gmail.com")
    message_service.send_birthday_wishes()


