class Message:
    """
    Represents an email message parsed into useful values.
    """
    def __init__(self):
        self.subject = ""
        """
        Subject of the email
        :type str
        """

        self.from_addr = None
        """
        From address of the email. Note that technically there can be multiple froms. If your
        code anticipates that, you can read the value from headers instead.
        :type str | None
        """

        self.to_addrs = None
        """
        To addresses the email was sent to.
        :type list[addr] | None
        """

        self.cc_addrs = None
        """
        CC addresses the email was sent to.
        :type list[addr] | None
        """

        self.bcc_addrs = None
        """
        BCC'd addresses the email was sent to. Note that incoming email won't have any record of these (hence being blind).
        :type list[addr] | None
        """

        self.reply_to_addr = None
        """
        Reply-to address the email has specified.
        :type str | None
        """

        self.date = None
        """
        The date the email was read. Note that this is not necessarily the date the email was actually sent.
        :type datetime.datetime
        """

        self.message_date = None
        """
        The date on the email itself (may be spoofed).
        :type datetime.datetime
        """

        self.body_parts = []
        """
        Body parts we've detected are the message contents. Can be multiple (e.g. a text and an html part).
        :type list[body]
        """

        self.files = []
        """
        File attachments in the email.
        :type list[file]
        """

        self.headers = None
        """
        Headers on the message 
        """

        self.raw_headers = None
        """
        Headers on the message with their raw string values. Note this differs
        from message.headers in that these are raw string values, whereas headers will be
        parsed into useful values where it makes sense (e.g. email addresses will be Addr lists). 
        """