from mongoengine import DynamicDocument, StringField, DictField


class RequestLog(DynamicDocument):
    request_id = StringField()
    headers = DictField()
