class CustomDate:
    def __init__(self, day, month, year):
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
    def changer(cls):
        cls =


day1 = CustomDate(10,10,2022)
day2 = CustomDate(2,2,1982)
CustomDate.datePrint(day1)
CustomDate.datePrint(day2)