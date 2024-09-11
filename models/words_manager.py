from google.cloud import translate_v2
import os
import csv
from datetime import date
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import json



class WordsManager:
    def __init__(self) -> None:
        load_dotenv()
        google_service_account_info = os.getenv('GOOGLE_SERVICE_ACCOUNT_INFO')
        if google_service_account_info:
            self.__credentials = json.loads(google_service_account_info)
            print(self.__credentials)




    def translation_to_fr(self, word_to_translate,path):
        if len(word_to_translate) < 150 and self.check_how_many_words_added_today(path) < 150: 
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"google.json"
            translate_client = translate_v2.Client()
            target = "fr"
            output = translate_client.translate(word_to_translate , target_language=target)
            return  output["translatedText"]
        else:
            return  bool(False)
        
    def add_word_to_profile_to_fr(self,path, translation, input):
        translation = str(translation)    
        escaped_translation = translation.replace('&#39;', "'" )
        escaped_input = input.replace(',', '&#39;')

        if translation == "None":
            with open(path, 'a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                data = ["word", escaped_translation, escaped_input, str(date.today()), True, False, 0, 0]
                csv_writer.writerow(data)

    def translate_to_german(self, word_to_translate,path):
        if len(word_to_translate) < 150 and self.check_how_many_words_added_today(path) < 30: 
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"google.json"
            translate_client = translate_v2.Client()
            target = "de"
            output = translate_client.translate(word_to_translate , target_language=target)
            return  output["translatedText"]
        else:
            return bool(False)
        
    def add_word_to_profile_to_de(self,path, translation, input):
        translation = str(translation)    
        escaped_translation = translation.replace('&#39;', "'" )
        escaped_input = input.replace(',', '&#39;')
        if translation :
            with open(path, 'a', newline='', encoding='utf-8') as csvfile:
                csv_writer = csv.writer(csvfile)
                data = ["word",escaped_input, escaped_translation , str(date.today()), True, False, 0, 0]
                csv_writer.writerow(data)


    def check_how_many_words_added_today(self, path):
        with open(path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            if csv_reader:
                sorted_rows = [row for row in csv_reader if row[0] == "word" and row[3] == str(date.today())]
                return len(sorted_rows)
            else:
                return None

    def words_to_learn(self, path):
        with open(path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            if csv_reader:
                words_to_learn = [row for row in csv_reader if row[4] == "True"]
                return words_to_learn
            else:
                return None
            

            
    def  get_words_to_learn(self,path):
        all_words = self.words_to_learn(path)
        _10_words_to_learn = all_words[:10]
        return _10_words_to_learn
    
    def change_to_learn_to_false(self, path,row_outsiede):
        with open(path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            for row in rows:
                if row == row_outsiede:
                    if row[4] == 'True':
                        row[4] = 'False'
                        today = datetime.now().date()
                        row[7] = int(row[7]) + 1
                        row[5] = today + timedelta(days=row[7])
                    with open(path, 'w', newline='', encoding='utf-8') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerows(rows)


    def reduce_10_Points(self, path, row_outside):
        with open(path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            for row in rows:
                if row == row_outside:
                    row[6] = int(row[6]) - 10
                    with open(path, 'w', newline='', encoding='utf-8') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerows(rows)
                    return row

            
    def  words_to_revise_today(self, path):
                with open(path, 'r', newline='', encoding='utf-8') as csvfile:
                    csv_reader = csv.reader(csvfile)
                    if csv_reader:
                        today = datetime.now().date()
                        today_string = today.strftime('%Y-%m-%d')
                        words_to_revise = []
                        for row in csv_reader:
                            try:
                                word_date = datetime.strptime(row[5], '%Y-%m-%d').date()
                                if word_date <= today:
                                    words_to_revise.append(row)
                            except ValueError:
                                pass
                        return words_to_revise
                      

                      
    def get_words_to_revise(self, path):
        if self.words_to_revise_today:
            all_words = self.words_to_revise_today(path)
            _10_words_to_revise = all_words[:10]
            return _10_words_to_revise
        else:
            return None
    
    def update_revise(self, path, row_outside, lose_or_win):
        with open(path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            for row in rows:
                if row[1] == row_outside[1]:
                    
                    if lose_or_win == "Yes":
                        row[6] = int(row[6]) + 10
                        today = datetime.now().date()
                        row[7] = int(row[7]) + 1
                        row[5] = today + timedelta(days=row[7])
                    elif lose_or_win == "No":
                        row[6] = int(row[6]) - 15
                        row[7] = 0
                    with open(path, 'w', newline='', encoding='utf-8') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerows(rows)

                    return row
    
    def delete_word(self,path, word_to_delete):
        with open(path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            rows = [row for row in rows if row[1] != word_to_delete]
        with open(path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)
    
    def get_all_words(self,path):
        with open(path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            if csv_reader:
                all_words = [row for row in csv_reader ]
                return all_words
            else:
                return None
            
    def get_20_words_with_least_points(self,path):
        words = []
        frenc_words = []
        with open(path, 'r', newline='', encoding='utf-8') as csvfile:
            csv_reader = csv.reader(csvfile)
            for row in csv_reader:
                if row[4] == 'False':
                    words.append(row)
            words.sort(key=lambda x: int(x[-2]))
            words = words[:20]
            for i in words:
                to_append = [i[1],i[2]]
                frenc_words.append(to_append)

        return frenc_words
                    

                
            