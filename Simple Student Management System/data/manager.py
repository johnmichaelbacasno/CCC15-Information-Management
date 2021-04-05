import csv

class connect:   
    def __init__(self, file, fields, key):
        self.file = file
        self.fields = fields
        
        if key not in self.fields:
            raise KeyError
        else:
            self.key = key
        
        self.__data = {}
        self.load()
       
    def search(self, key, attr):
        return self.__data[key][attr]
     
    def add(self, **info):
        if info[self.key] in self.keys():
            raise KeyError
        else:
            new = {}
            for attr in self.fields:
                try:
                    new[attr] = info[attr]
                except:
                    new[attr] = ''
            self.__data[new[self.key]] = new
        self.save()
    
    def update(self, **info):
        for attr in info.keys():
            if attr in self.fields and info[attr]:
                self.__data[info[self.key]][attr] = info[attr]
        self.save()
    
    def delete(self, key):
        del self.__data[key]
        self.save()
    
    def load(self):
        with open(self.file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f, fieldnames=self.fields)
            for row in reader:
                self.__data[row[self.key]] = row
    
    def save(self):
        with open(self.file, 'w', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.fields)
            writer.writerows(self.values())
    
    def keys(self):
        return tuple(self.__data.keys())
    
    def values(self):
        return tuple(self.__data.values())
    
    def __len__(self):
        return len(self.__data)