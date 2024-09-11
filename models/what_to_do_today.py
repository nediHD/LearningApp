import json
from datetime import datetime, timedelta

class WhatToDoToday():
    def __init__(self):
        today = datetime.now()
        yesterday = (today - timedelta(days=1)).strftime('%Y-%m-%d')
        self.__What_to_do = ["Words", "Practice", "Practice",yesterday]

    def adding_profile_to_json(self,file_name):
        with open('what_to_do.json', 'r') as file:
            data = json.load(file)

        new_data = {
            file_name: self.__What_to_do
        }
        data.update(new_data)
        with open('what_to_do.json', 'w') as file:
            json.dump(data, file, indent=4)

    def checking_if_file_name_alreday_in_json(self, filename):
        try:
            with open("what_to_do.json", 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
        
            return False
        return filename in data
    
    def rotete_one_left(self,filename):
        with open('what_to_do.json', 'r') as file:
            data = json.load(file)

        datum = data[filename][3]
        date_to_compare = datetime.strptime(datum, '%Y-%m-%d')
        today = datetime.now()

        if date_to_compare.date() < today.date():
            lista_za_promjenu = data[filename][:3]                                   
            pomaknuta_lista = lista_za_promjenu[1:] + lista_za_promjenu[:1]
            today = datetime.now().strftime('%Y-%m-%d')
            data[filename] = pomaknuta_lista
            data[filename].append(today)
            with open('what_to_do.json', 'w') as file:
                json.dump(data, file, indent=4)
            return True
        else:
            return False

    def what_to_do_today(self,filename):
        with open('what_to_do.json', 'r') as file:
            data = json.load(file)

        lista_za_promjenu = data[filename][0]

        return lista_za_promjenu
    


         

         



"""
with open('data.json', 'r') as file:
        data = json.load(file)

new_data = {
    "newfile.csv": ["NewWord1", "NewPractice1", "NewPractice2"]
}

data.update(new_data)
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

    """