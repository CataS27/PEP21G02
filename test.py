"""
A factory needs an iterable object to keep track of employee working hours for each day.
Each employee has a string name and a tuple containing start work and end work time (use format you like).
Iterating the object will return tuple with name and hours worked that day for each employee
1) 40p: Definition
    a) 10p: Class with constructor that receives the date in the format you desire (representing the day)
    b) 10p: Create method to add worker start time
         - if start time has already been added a custom exception inheriting ValueError (exception: WorkStartError)
         exception will be raised with message indicating employee name and existing start time
    c) 10p: Create method to add worker end time
         - if end time has already been added a custom exception inheriting ValueError (exception: WorkEndError)
         exception will be raised with message indicating employee name and existing end time
    c) 10p: Iterating the object will return tuple with name and time worked that day for each employee
2) 40p: Execution:
    a) 10p: Create instance of class with date format you selected.
    b) 10p: Add start of work for the following employees:
        - Joe: 09:01:20 - start time
        - Ana: 09:03:15 - start time
        - Tim: 09:04:25 - start time
        - Tim: 09:04:30 - start time - treat this exception
    c) 10p: Add end of work for the following employees:
        - Joe: 16:01:20 - end time
        - Ana: 18:04:15 - end time
        - Tim: 18:05:25 - end time
        - Tim: 18:05:30 - end time - treat this exception
    d) 10p: Iterate the created object and save each value on a new line in a file
3) 20p: Documenting:
   a) 5p: type hints for all arguments (optional for returned values)
   a) 5p: module documentation
   b) 5p: class documentation for all classes
   c) 5p: method documentation for all methods
"""
class DuplicateDataException(ValueError):
    pass
from datetime import date
class ShoIter:
    def __init__(self, data: list):
        self.data = data

    def __iter__(self):
        return self
    def __next__(self):
        if not self.data:
            raise StopIteration
        return self.data.pop(0)


'''
Class Documentation
'''
class Factory:
    def __init__(self, date):
        self.date = date
        self.starttime = {}
        self.endtime = {}
        self.workhours_dict = {}

    def add_work(self, name: str, time1: list): #type int
        for worker_name, workstart_data in self.starttime.items():
            for j in workstart_data:
                if j in series:

                    if workstart_data == time1:
                        raise DuplicateDataException('WorkStartError')
                    else:
                        time1.remove(j)
                        self.starttime[time] = time1
                        list_to_modify = self.work[workstart_data]
                        list_to_modify.remove(j)
                        self.workhours_dict[j] = (worker_name, name, starttime, time1)
                        raise ValueError(f"WorkStartError: {j}, Workstart: {worker_name}, {name}, {starttime},{time1} ")
        self.starttime[time] = time1

    class Factory:
    def __init__(self, date):
            self.date = date
            self.starttime = {}
            self.endtime = {}
            self.workhours_dict = {}
    def add_work(self, name: str, time2: list): #type int
        for worker_name, workend_data in self.endtime.items():
            for j in workend_data:
                if j in series:

                    if workend_data == time2:
                        raise DuplicateDataException('WorkEndError')
                    else:
                        time2.remove(j)
                        self.endtime[time] = time2
                        list_to_modify = self.work[workend_data]
                        list_to_modify.remove(j)
                        self.workhours_dict[j] = (worker_name, name, endtime, time2)
                        raise ValueError(f"WorkEndError: {j}, Workend: {worker_name}, {name}, {endtime},{time2} ")
        self.endtime[time] = time2

    def __iter__(self):
        result = ()
        for v in self.starttime.values():
            result.extend(v)
        return ShoIter(result)

    def __iter__(self):
        result = ()
        for v in self.endtime.values():
            result.extend(v)
        return ShoIter(result)


from datetime import datetime as d
date = d.now()
print(date.strftime("%Y-%m-%d %H:%M:%S"))
try:
    t.add_work('Ana',('18:04:15, 18:04:15'))
except ValueError:
    pass

print(t.work)
print(t.workhours_dict)
for y in t:
    print(t)