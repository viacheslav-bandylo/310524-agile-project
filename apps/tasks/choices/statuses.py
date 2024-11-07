from enum import Enum


class Statuses(Enum):
    New = 'New'
    InProgress = 'In progress'
    Pending = 'Pending'
    Blocked = 'Blocked'
    Testing = 'Testing'
    Completed = 'Completed'


    @classmethod
    def choices(cls):
        return [(i.name, i.value) for i in cls]
