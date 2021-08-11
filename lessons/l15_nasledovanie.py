# наследование в классах
import json



class JsonWorkerList:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.read_json()

    class JsonWorkerDict:
        def __init__(self, filename):
            self.filename = filename
            self.data = self.read_json()


    def read_json(self):
        with open(self.filename, "r") as json_file:
            data = json.load(json_file)
            return data


    def sort(self):
        keys = self.data.keys()
        keys = sorted(keys)
        new_data = {}
        for key in keys:
            new_data[key] = self.data[key]
        self.data = new_data


json_worker = JsonWorkerList("../data_list.json")
json_worker.sort()
print(json_worker.data)


# второй вариант

# class JsonWorker:
#     def __init__(self, filename):
#         self.filename = filename
#         self.data = None
#
#
#     def read_json(self):
#         with open(self.filename, "r") as json_file:
#             self.data = json.load(json_file)
#
# json_worker = JsonWorker("data_list.json")
# json_worker.read_json()
# data = json_worker.data
# print(data)