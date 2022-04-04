from datetime import datetime

class CustomDate:
    def __init__(self, day, month, year):
        self.dateValidation(day, month, year)

        if day < 10:
            day = "0"+str(day)
        self.day = day

        if month < 10:
            month = "0"+str(month)
        self.month = month
        self.year = year

    def datePrint(self):
        print(f"{self.day}-{self.month}-{self.year}")

    @classmethod
    def splitter(cls, splitDate):
        day, month, year = splitDate.split("-")
        return cls(int(day), int(month), int(year))

    @classmethod
    def txtFile(cls, file):
        objectsArray = []
        with open(file, 'r') as file:
            text_data = file.read().splitlines()
        for date in text_data:
            date_object = cls.splitter(date)
            objectsArray.append(date_object)
        return objectsArray

    @staticmethod
    def dateValidation(day, month, year):
        try:
            datetime(year, month, day)
        except ValueError:
            raise ValueError("Wrong date!")


day1 = CustomDate(10,10,2022)
day2 = CustomDate(2,2,1982)
CustomDate.datePrint(day1)
CustomDate.datePrint(day2)
day3 = CustomDate.splitter("12-10-1999")
day4 = CustomDate.splitter("03-8-1998")
CustomDate.datePrint(day3)
CustomDate.datePrint(day4)

dates = CustomDate.txtFile("dates.txt")
for date in dates:
    CustomDate.datePrint(date)