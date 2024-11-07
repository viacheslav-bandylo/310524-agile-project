from enum import Enum


class Priority(Enum):
    LOW = (1, 'Low')
    MEDIUM = (2, 'Medium')
    HIGH = (3, 'High')
    CRITICAL = (4, 'Critical')

    @classmethod
    def choices(cls):
        return [(priority.value[0], priority.value[1]) for priority in cls]

    def __getitem__(self, item):
        return self.value[item]
