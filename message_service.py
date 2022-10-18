class MessageService:
    # Employees API endpoint
    employees_api = 'https://interview-assessment-1.realmdigital.co.za/employees'

    def __init__(self, sender_email, password, receiver_email):
        self.admin_email_address = sender_email
        self.admin_email_password = password
        self.distribution_email = receiver_email

    def send_mail(self, email_message):
        import smtplib, ssl
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        sender_email = self.admin_email_address
        password = self.admin_email_password
        receiver_email = self.distribution_email

        message = MIMEMultipart("alternative")
        message["Subject"] = "multipart test"
        message["From"] = sender_email
        message["To"] = self.distribution_email

        # Create HTML version of the message
        html = """\
        <html>
          <body>
            <p>Hi,<br>
               {}
            </p>
          </body>
        </html>
        """.format(email_message)

        # Turn this into html MIMEText objects
        mimeObj = MIMEText(html, "html")
        message.attach(mimeObj)

        # Create secure connection with server and send email
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )

    def send_birthday_wishes(self):
        """ send birthday wishes function """
        employees = self.employee_exclusions(MessageService.get_employees())
        # I am assuming 'lastNotification' key is for employees who do want birthday wishes
        employees_do_want_wishes = [emp for emp in employees if 'lastNotification' in emp.keys()]
        employees_born_today = MessageService.get_employees_born_today(employees_do_want_wishes)
        if len(employees_born_today) > 0:
            msg = "Happy birthday {}".format(",".join([emp.name for emp in employees_born_today]))
            self.send_mail(msg)


    @staticmethod
    def get_employees_born_today(employees):
        """ Extracting employees who have birthdays today """
        from datetime import datetime
        current_date = MessageService.get_todays_date()
        employees_born_today = list()
        for each_emp in employees:
            try:
                emp_dob = datetime.strptime(each_emp['dateOfBirth'].replace("T00:00:00",""), '%Y-%m-%d')
                if current_date.month == 2 and emp_dob.month == 2:
                    if emp_dob.day == 29 and MessageService.is_leap_year(current_date.year):
                        employees_born_today.append(each_emp)
                else:
                    if current_date.month == emp_dob.month and current_date.day == emp_dob.day:
                        employees_born_today.append(each_emp)
            except ValueError as e:
                print('Employee {} date of birth {}'.format(each_emp,e))
        return employees_born_today

    @staticmethod
    def employee_exclusions(employees):
        """ exclude employees that no longer work nor has started working """
        excluded_employees = list(filter(lambda emp: (emp['employmentEndDate'] is None and emp['employmentStartDate'] is not None), [emp for emp in employees if 'employmentEndDate' in emp.keys()]))
        return excluded_employees

    @staticmethod
    def get_todays_date():
        """ get todays date """
        import datetime
        # from datetime import date
        # return date.today()
        return datetime.datetime.now()

    @staticmethod
    def is_leap_year(y):
        """ check year is leap year """
        if y % 400 == 0:
            return True
        if y % 100 == 0:
            return False
        if y % 4 == 0:
            return True
        else:
            return False

    @classmethod
    def get_employees(cls):
        """ get all employees function """
        import requests
        response = requests.get(MessageService.employees_api)
        return response.json()


