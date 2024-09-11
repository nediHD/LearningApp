import csv
from pathlib import Path
from openai import OpenAI
from groq import Groq
import pyttsx3
import requests
import json

class PracticeManager():
    def __init__(self) -> None:
        self.__all_words = []
        
        with open('keys.json', 'r') as file:
            data = json.load(file)
            groq = data["Groq"]
            openai = data["OpenAI"]
        self.__client = Groq(api_key=groq)
        self.__client1  = OpenAI(api_key=openai)



    def take_all_words_to_practice(self,path):
        with open(path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
            rows.reverse()
            for row in rows:
                points = int(row[6])
                notlearnt = row[4]
                if points <= 100 and notlearnt != "True":
                    self.__all_words.append([row[1],row[6]])
            self.__all_words = sorted(self.__all_words, key=lambda x: int(x[1]))
        return self.__all_words
    
    def teke_fiert_20_words(self, words):
        _first_15_words = words[:20]
        return _first_15_words
        

    def create_text(self, text):
        completion = self.__client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional teacher fluent in French."
                },
                {
                    "role": "user",
                    "content": (
                        f'Create a short storry with those words: {text}. The story should be in french '
                        f'You dont have to teake phrases in that order. You can change order of the words but make sure that the text should obtain all given words/prahese'
                        f'Do not write any comment before and after the text.'
                        f'Text should be longer than 300  Words'
                        f'Make sure that the text has some logic an donot just put words to use it, make logical sentencec so the thext can be undestandabel'
                        
                    )
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        hola = completion
        response_text = "".join(chunk.choices[0].delta.content or "" for chunk in completion)
        return response_text
    
    
    def text_questions(self,text):
        completion = self.__client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional teacher fluent in French."
                },
                {
                    "role": "user",
                    "content": (
                        f'Ask me 5 questions about the text in french: {text} '
                        f'The questions should be asked so i can practise my written skills in french'
                        f'I dont want to see any comments before neither after the quetions'
                        f'The should not be any empyty lines between quesitons' 
                        f'The questions should be i order from 1. - 5.'
                        )
                        
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        
        response_text = "".join(chunk.choices[0].delta.content or "" for chunk in completion)
        return response_text
    
    def questions_correction(self,question, answer, text):
            completion = self.__client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional teacher fluent in French."
                },
                {
                    "role": "user",
                    "content": (
                        f'You need to corret my answers to a quenton. For that use this text: {text} '
                        f'Here ist the question: {question}, and here is my respones {answer}'
                        f'If my answer ist correct say that i am right if not tell me what i done wrong. Firstly correct the content of the answer and than the grammer'
                        f'Make sure the orrection to be as short as possible' 
                        )
                        
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        
            response_text = "".join(chunk.choices[0].delta.content or "" for chunk in completion)
            return response_text
        


    def text_to_speech(self,text):
        speech_file_path = Path(__file__).parent / "speech.mp3"
        response = self.__client1.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text
        )

        response.stream_to_file(speech_file_path)

    def text_tospeeec(self, text):
        engine = pyttsx3.init()
        engine.say(text)
        voices = engine.getProperty('voices')
        for voice in voices:
            print("Voice:")
            print(" - ID: %s" % voice.id)
            print(" - Name: %s" % voice.name)
            print(" - Languages: %s" % voice.languages)
            print(" - Gender: %s" % voice.gender)
            print(" - Age: %s" % voice.age)
        engine.runAndWait()

    def get_question_list(self,text):
        questions=self.text_questions(text)
        try:
            questions_list = [line.split('. ', 1)[1] for line in questions.strip().split('\n')]
            return questions_list
        except IndexError:
            print()
            print("Quenstion coud not be generated")
            question_list = self.get_question_list(text)
            return questions_list
        

    def written_text_task(self, words):
        completion = self.__client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional teacher fluent in French."
                },
                {
                    "role": "user",
                    "content": (
                        f'Create a task for me  in french where i should use following words/phrasers to practise my written skills in frenc: {words}. ' 
                        f'I should write an essay of about 100 words, give me topic for that'
                        f'Give me only the topic of a essay that i  should use'
                        f'Even  the instruction of the tsak should be in french'
                        f'Dont give any comments, just give me the topic that i should use. Exempel: le theme : Un séjour difficile sur une île déserte'
                        )
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        
        response_text = "".join(chunk.choices[0].delta.content or "" for chunk in completion)
        if len(response_text) > 150:
            print()
            print(f'response text je prevelik {len(response_text)}')
            print()
            response_text = self.written_text_task(words)
       
        return response_text
    
    """

    OVO VISE NE KORISTIM




    def correction_text_task(self, text, topic):
        completion = self.__client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional teacher fluent in French."
                },
                {
                    "role": "user",
                    "content": (
                        f'Please analyze the following text and identify all grammatical errors. For each error, provide a brief description of the error (maximum one sentences) and specify the type of error such as: incorrect conjugation, incorrect preposition, incorrect word order, etc. '
                        f'Text for analysis: {text}'
                        f'The error report should be in the format:'
                        f'Fehler : [identified error]'
                        f'Beschreibung : [brief description of the error](exempel. Should be "des fruits" (plural form of "fruit"), DEscription should be in german)'
                        f'Art der Feher: [type of error]'
                        f'Repeat this format for each identified error.'
                        )

                        
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        
        response_text = "".join(chunk.choices[0].delta.content or "" for chunk in completion)
        return response_text
    """

    def corrected_text(self, text):
        completion = self.__client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
            {
                "role": "system",
                "content": "Sie sind ein professioneller Lehrer, der fließend Französisch spricht. Ihre Aufgabe ist es, jeden Ihnen bereitgestellten Text zu korrigieren und dabei perfekte Grammatik, Rechtschreibung und Syntax zu gewährleisten. Geben Sie nur die korrigierte Version des Textes ohne zusätzliche Kommentare an."

            },
            {
                "role": "user",
                "content": (
                    f'Machen Sie keine Kommentare vor der Korrektur.'
                    f'Bitte korrigieren Sie den folgenden Text: {text}\n'
                    f'Analysieren Sie jeden Satz und korrigieren Sie ihn. Korrigieren Sie nur die Grammatik- und Rechtschreibfehler, nicht den Inhalt des Satzes.\n'
                    f'Wenn ein Fehler vorliegt, geben Sie den Satz in der Form an:\n'
                    f'Nummer des Satzes.\n'
                    f'Der vollständige Satz\n'
                    f'Kurz, was ich falsch gemacht habe. Nennen Sie einfach den Fehler und dann die Korrektur in der Form:\n'
                    f'Fehler -> Korrektur\n'
                    f'(Grund für den Fehler)\n'
                    f'Korrigierter Satz:\n'
                )
            }
        ],
            temperature=1,
            max_tokens=8000,
            top_p=1,
            stream=True,
            stop=None,
        )
        
        response_text = "".join(chunk.choices[0].delta.content or "" for chunk in completion)
        return response_text
    

    def gap_text(self,word):
            completion = self.__client.chat.completions.create(
            model="llama-3.1-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional teacher fluent in French."
                },
                {
                    "role": "user",
                    "content": (
                    f'From the following word:{word}, please generate a gap text for practice. '
                    f'The gap text should contain 1 sentence. Make sure that a given word is a missing word '
                    f'Please ensure that each sentence is properly structured and clear.'
                    f'this is an exempel of how i want it: Les personnes sont souvent _______________________, mais parfois elles ne font que passer.'
                    f'Dont write any comments, hust provide me  with sentences'


                        )
                        
                }
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=True,
            stop=None,
        )
        
            response_text = "".join(chunk.choices[0].delta.content or "" for chunk in completion)
            return response_text
        
