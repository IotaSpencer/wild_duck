import requests

class RequestTree:
  def __init__(self):
    self.audit = Audit()
    self.addresses = Addresses()
    self.asps = ApplicationSpecificPasswords()
    self.archive = Archive()
    self.auth = Authentication()
    self.autoreplies = AutoReplies()
    self.dkim = DKIM()
    self.domainaliases = DomainAliases()
    self.filters = Filters()
    self.mailboxes = Mailboxes()
    self.messages = Messages()
    self.storage = Storage()
    self.submit = Submission()
    self.tfa = TwoFA()
    self.users = Users()
