from tkinter import * 
from models.profile_menager import *
import tkinter as tk
from tkinter import messagebox
from models.words_manager import *
from models.practice_manager import *
from models.what_to_do_today import *
from tkinter import simpledialog


profile_manager = ProfileManager()
word_manager = WordsManager()
practice_manager = PracticeManager()
what_to_do = WhatToDoToday()

def go_menu(self, parent):
    from views.tkinter.view import MenuFrame
    self.destroy()
    MenuFrame(parent)

def go_profiles_menu(self, parent):
    from views.tkinter.view import ProfilesMenu  
    self.destroy()
    ProfilesMenu(parent)




def go_words_menu(self, parent):
    from views.tkinter.view import WordsMenu  
    self.destroy()
    WordsMenu(parent)


def go_adding_words(self, parent):
    from views.tkinter.view import AddWords
    self.destroy()
    AddWords(parent)
   

def button_add_new_profile(entry_get):
    profile_manager .create_profile(entry_get)

def go_menu_and_add_new_profile(entry, self, parent):
    button_add_new_profile(entry.get())
    entry.delete(0, tk.END)
    go_menu(self, parent)

def get_profile():
    return profile_manager .get_chosen_profile()   

def get_amount_profiles():
    return profile_manager .get_profile_count()

def get_all_profiles():
    return profile_manager .get_data()

def go_to_add_profile_window(self,parent):
    if profile_manager .get_profile_count() < 7:
        from views.tkinter.view import AddNewProfile
        self.destroy()
        AddNewProfile(parent)


def choose_profile_with_button_and_go_menu(number, self, parent):
    profile_manager .choose_profile(number)
    go_menu(self, parent)

def go_choose_profile(self,parent):
    if profile_manager .get_profile_count() > 1:
        from views.tkinter.view import ChooseProfile
        self.destroy()
        ChooseProfile(parent)

def go_delete_profile(self, parent):
    from views.tkinter.view import DeleteProfiles
    self.destroy()
    DeleteProfiles(parent)


def delete_profile(profile_number,self,parent):
    if get_all_profiles()[profile_number] == get_profile():
        messagebox.showwarning("Warning", "This Profile cannot be deleted")
    else:
        response = messagebox.askquestion("Confirm Deletion", f"Do you want to delete {profile_manager .get_data()[profile_number]}?")
        if response == 'yes':
            print("User chose Yes")
            with open('what_to_do.json', 'r') as file:
                data = json.load(file)
                if profile_manager .get_data()[profile_number] in data:
                    del data[profile_manager .get_data()[profile_number]]
                with open('what_to_do.json', 'w') as file:
                    json.dump(data, file, indent=4)
            profile_manager .delete_profile(profile_number)
            
        else:
            print("User chose No")
        go_delete_profile(self,parent)
        

def add_word(entry):
    path = f'profiles/{get_profile()}.csv'
    print(path)
    french_word = entry.get()
    entry.delete(0, tk.END)
    print(french_word)
    word_manager.add_word_to_profile_to_de(path,word_manager.translate_to_german(french_word, path),french_word)


def go_learning_words(self,parent):
    data = word_manager.get_words_to_learn(f'profiles/{get_profile()}.csv',)
    if len(data) != 0:
        from views.tkinter.view import LearningWords
        self.destroy()
        LearningWords(parent)  
    else:
        messagebox.showwarning("Warning", "There is nothing to learn")

def give_translations(data,randomizes,label):
    if randomizes == 0 or randomizes== 1: 
        label.config(text=f'{data[0][1]}')
    else:
        label.config(text=f'{data[0][2]}')

def go_revising_words(self,parent):
    

    data = word_manager.get_words_to_revise(f'profiles/{get_profile()}.csv',)
    if len(data) != 0:
        from views.tkinter.view import ReviseWords
        self.destroy()
        ReviseWords(parent)  
    else:
        messagebox.showwarning("Warning", "There is nothing to revise")


def go_deleting_words(self,parent):
    from views.tkinter.view import DeleteWords
    self.destroy()
    DeleteWords(parent)  

def go_deleting_words(self,parent):
    from views.tkinter.view import DeleteWords
    self.destroy()
    DeleteWords(parent)  

def go_practising(self,parent):
    from views.tkinter.view import PracticeMenu
    self.destroy()
    PracticeMenu(parent) 

def go_ShortStory(self,parent):
    from views.tkinter.view import ShortStory
    self.destroy()
    ShortStory(parent)


def text_creation(_20_words):
    text = practice_manager.create_text(_20_words)
    while (len(text) > 3000):
        text = practice_manager.create_text(_20_words)
    return text

def delete_file(mp3file):
        if os.path.exists(mp3file):
            try:
                os.remove(mp3file)
                messagebox.showinfo("Success", f"File '{mp3file}' deleted successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting file: {str(e)}")
        else:
            messagebox.showwarning("Warning", f"File '{mp3file}' does not exist.")

def go_textCreation(self, parent):
    print("Switching to TextCreation frame")
    from views.tkinter.view import TextCreation
    self.destroy()
    text_creation_frame = TextCreation(parent)
    text_creation_frame.pack(expand=True, fill='both')
    print("TextCreation frame created and packed")

def go_practising_ovo_ono(ovovono,parent, lista):
        lista.clear()
        go_practising(ovovono,parent)

def check_word_in_data(data, word):
    return word in data[0]

def get_matching_words_for_deletion(path):
    ime = simpledialog.askstring("Unos rijeci", "Which word would you like to enter?")
    sve_rijeci = word_manager.get_all_words(path)
    samo_rijeci = []
    rijeci_koje_se_podudaraju = []
    for i in sve_rijeci:
        francuska_rijeci = [i[1],1]
        njeamcka_rijec = [i[2],2]
        samo_rijeci.append(francuska_rijeci)
        samo_rijeci.append(njeamcka_rijec)
    for i in samo_rijeci:
        if check_word_in_data(i,ime):
            rijeci_koje_se_podudaraju.append(i)
    with open(path, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            rows = list(reader)
    francuska_rijec = []
    for i in rijeci_koje_se_podudaraju:
        if i[1]==1:
            for _ in rows:
                if i[0] == _[1]:
                    francuska_rijec.append(_)
        else:
            for _ in rows:
                if i[0] == _[2]:
                    francuska_rijec.append(_)
    if francuska_rijec:
        return True, francuska_rijec
    else:
        return False, francuska_rijec
    
  

    

