from tkinter import *
from controllers.controller import *
import pygame
import os
import httpx




class MenuFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        if not what_to_do.checking_if_file_name_alreday_in_json(get_profile()):
            what_to_do.adding_profile_to_json(get_profile())

        self.pack(pady=20)

        self.__my_label = Label(self, text = "Menu", font =("Helvetica", 42))
        self.__my_label.pack(pady=5)

        self.__hallo_label = Label(self, text=f'Profile: {get_profile()}',font =("Helvetica", 24) )
        self.__hallo_label.pack(pady=5)


        self.__to_do = Label(self, text=f'What to do today: {what_to_do.what_to_do_today(get_profile())}',font =("Helvetica", 12) )
        self.__to_do.pack(pady=5)

        self.__button_job_done = Button(self, text="job Done ;)", command=lambda: self.job_done(get_profile()),font =("Helvetica", 17))
        self.__button_job_done.pack(pady=10)

        self.__profiles_menu = Button(self, text ="Profiles", command=lambda: go_profiles_menu(self,parent),  font =("Helvetica", 17),)
        self.__profiles_menu.pack(pady= 10)

        self.my_botton2 = Button(self, text ="Words", command= lambda: go_words_menu(self, parent), font =("Helvetica", 17),)
        self.my_botton2.pack(pady= 10)

        self.my_botton3 = Button(self, text ="Practice", command= lambda: go_practising(self, parent),font =("Helvetica", 17))
        self.my_botton3.pack(pady= 10)


    def job_done(self,filename):
        if what_to_do.rotete_one_left(filename):
            messagebox.showinfo("Information", "You have completed your session for today")
            self.__to_do.config(text=f'What to do tommorrow: {what_to_do.what_to_do_today(get_profile())}')
        else:
            messagebox.showerror("Information", "You’re done for today ;)")





class AddNewProfile(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(pady=20)

        self.my_label = Label(self, text = "Profiles", font =("Helvetica", 42))
        self.my_label.pack(pady=20)

        self.__entry = Entry(self, text="Add new profile", width=80, font =("Helvetica", 17))
        self.__entry.pack(pady=20)

        self.__button_submit = Button(self, text ="Submit",command=lambda:go_menu_and_add_new_profile(self.__entry,self,parent), font =("Helvetica", 17))
        self.__button_submit.pack(pady= 20)

    
class ProfilesMenu(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(pady=20)

        self.__my_label = Label(self, text = "Profiles", font =("Helvetica", 42))
        self.__my_label.pack(pady=10)

        self.__add_new_profile = Button(self, text ="Add new Profile", command=lambda: go_to_add_profile_window(self, parent), font =("Helvetica", 17))
        self.__add_new_profile.pack(pady= 10)

        self.__choose_profile = Button(self, text ="Choose Profile", command=lambda:go_choose_profile(self, parent), font =("Helvetica", 17))
        self.__choose_profile.pack(pady= 10)

        self.__delete_profiles = Button(self, text ="Delete Profiles", command= lambda: go_delete_profile(self,parent), font =("Helvetica", 17))
        self.__delete_profiles.pack(pady= 10)

        self.__menu_button = Button(self, text="Menu", command= lambda: go_menu(self,parent), font =("Helvetica", 17))
        self.__menu_button.pack()

class ChooseProfile(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(pady=20)

        self.__my_label = Label(self, text = "Choose Profile", font =("Helvetica", 42))
        self.__my_label.pack(pady=20)

        numbers = 0
        self.__buttons = []
        for name in get_all_profiles():
            button = Button(self, text=name, command=lambda n=numbers: choose_profile_with_button_and_go_menu(n, self,parent),  font =("Helvetica", 17))
            button.pack(pady=10)
            self.__buttons.append(button)
            numbers += 1


class DeleteProfiles(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(pady=20)

        self.__my_label = Label(self, text = "Delete Profiles", font =("Helvetica", 30))
        self.__my_label.pack(pady=20)

        numbers = 0
        self.__buttons = []
        for name in get_all_profiles():
                button = Button(self, text=name, command=lambda n=int(numbers): delete_profile(n, self,parent), font =("Helvetica", 17))
                button.pack(pady=10)
                self.__buttons.append(button)
                numbers += 1

        self.__menu_button = Button(self, text="Profiles", command= lambda: go_profiles_menu(self,parent), font =("Helvetica", 17))
        self.__menu_button.pack()
    


  
class WordsMenu(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__path = f'profiles/{get_profile()}.csv'

        self.pack(pady=20)

        self.__my_label = Label(self, text = "Words - Menu", font =("Helvetica", 42))
        self.__my_label.pack(pady=20)

        self.__my_label1 = Label(self, text = f'Words to learn: {len(word_manager.words_to_learn(self.__path))}', font =("Helvetica", 20))
        self.__my_label1.pack(pady=3)

        self.__my_label2 = Label(self, text = f'Words to reapet : {len(word_manager.words_to_revise_today(self.__path))}', font =("Helvetica", 20))
        self.__my_label2.pack(pady=3)

        self.__my_botton_add_words = Button(self, text ="Add Words", command= lambda: go_adding_words(self,parent), font =("Helvetica", 17))
        self.__my_botton_add_words.pack(pady= 10)

        self.__my_botton_delete_words = Button(self, text ="Delete Words", command= lambda: go_deleting_words(self,parent), font =("Helvetica", 17))
        self.__my_botton_delete_words.pack(pady= 10)

        self.__my_botton_add_words = Button(self, text ="Learn words", command=lambda: go_learning_words(self,parent), font =("Helvetica", 17))
        self.__my_botton_add_words.pack(pady= 10)

        self.__my_botton_add_words = Button(self, text ="Revising words", command=lambda: go_revising_words(self,parent), font =("Helvetica", 17))
        self.__my_botton_add_words.pack(pady= 10)

        self.__my_botton = Button(self, text ="Menu", command= lambda: go_menu(self,parent), font =("Helvetica", 17))
        self.__my_botton.pack(pady= 10)


class AddWords(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(pady=20)

        self.__my_label = Label(self, text = "Add Word", font =("Helvetica", 20))
        self.__my_label.pack(pady=20)

        self.__entry = Entry(self, text="Add new word",font =("Helvetica", 17), width=80)
        self.__entry.pack(pady=10)

        self.__my_botton_add_words = Button(self, text ="Submit", command=lambda: self.on_Submit(), font =("Helvetica", 17))
        self.__my_botton_add_words.pack(pady= 10)

        self.__my_botton = Button(self, text ="Menu", command= lambda: go_menu(self,parent), font =("Helvetica", 17))
        self.__my_botton.pack(pady= 10)

        self.canvas = Canvas(self,  height=470, width=1100, background=self["bg"])
        self.canvas.pack_propagate(False)
        self.scrollbar = Scrollbar(self.canvas, orient="vertical", command=self.canvas.yview,)
        self.scrollable_frame = Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="n")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="top", pady=10, fill="y")
        self.scrollbar.pack(side="right", fill="y")
        self.__buttons = []
    
    def delete_word(self, word):
        if messagebox.askyesno("Deleting Word", f'Are you sure you want to delete {word}'):
                word_manager.delete_word(f'profiles/{get_profile()}.csv', word)
                self.refresh_view()
        else:
            pass
        

    def refresh_view(self):
        for button in self.__buttons:
            button.destroy()
        self.__buttons.clear()
        words = word_manager.get_all_words(f'profiles/{get_profile()}.csv')
        today = datetime.now().date()
        today_string = today.strftime('%Y-%m-%d')
        todays_words = []
        for i in words:
            if i[3] == today_string:
                todays_words.append(i)
        for word in todays_words:
            button = Button(self.scrollable_frame, text=word[1], command=lambda w=word[1]: self.delete_word(w), font =("Helvetica", 17))
            button.pack(pady=5, side="top", anchor="w")
            self.__buttons.append(button)

    def on_Submit(self):
        add_word(self.__entry)
        if self.__buttons:  
            for widget in self.__buttons:
                    widget.destroy()
        words = word_manager.get_all_words(f'profiles/{get_profile()}.csv')
        today = datetime.now().date()
        today_string = today.strftime('%Y-%m-%d')
        todays_words = []
        for i in words:
            if i[3] == today_string:
                todays_words.append(i)
        for word in todays_words:
            sto_napisati = f'{word[1]} - {word[2] }'
            button = Button(self.scrollable_frame, text=sto_napisati, command=lambda w=word[1]: self.delete_word(w), font =("Helvetica", 17))
            button.pack(pady=5, side="top", anchor="w")
            self.__buttons.append(button)

class LearningWords(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.data = word_manager._10_words_to_lern(f'profiles/{get_profile()}.csv',)
        self.randomisez = 0
        self.pack(pady=20)

        self.__my_label = Label(self, text = f'{self.data[0][2]}', font =("Helvetica", 20))
        self.__my_label.pack(pady=20)

        self.__my_label_1 = Label(self, text = f'', font =("Helvetica", 20))
        self.__my_label_1.pack(pady=20)

        self.__entry = Entry(self, text="Add new word",width=80, font =("Helvetica", 17))
        self.__entry.pack(pady=10)

        self.__my_botton_check = Button(self, text ="Cehck", command=lambda: give_translations(self.data, self.randomisez, self.__my_label_1), font =("Helvetica", 17))
        self.__my_botton_check.pack(pady= 10)

        self.__my_botton_Yes = Button(self, text ="Ok", command=lambda: self.ok(self,parent), font =("Helvetica", 17))
        self.__my_botton_Yes.pack(pady= 10)

        self.__my_botton_No = Button(self, text ="Nah", command=lambda: self.nah(self,parent), font =("Helvetica", 17))
        self.__my_botton_No.pack(pady= 10)

        self.__my_botton = Button(self, text ="Menu", command= lambda: go_menu(self,parent), font =("Helvetica", 17))
        self.__my_botton.pack(pady= 10)


    def ok(self,self1,parent):
        if self.randomisez < 2:
            self.randomisez += 1
        else:
            self.randomisez = 0
        row = self.data[0]
        word_manager.change_to_learn_to_false(f'profiles/{get_profile()}.csv', row)
        del self.data[0]
        if 0 == len(self.data):
            self.__entry.delete(0, 'end') 
            go_words_menu(self1,parent)
            return
        else:
            if self.randomisez == 0 or self.randomisez == 1:
                self.__my_label.config(text=f'{self.data[0][2]}')
                self.__my_label_1.config(text=f'')
            else:
                self.__my_label.config(text=f'{self.data[0][1]}')
                self.__my_label_1.config(text=f'')
        self.__entry.delete(0, 'end') 

    def nah(self,self1 ,parent):
        new_row_0 =word_manager.reduce_10_Points(f'profiles/{get_profile()}.csv',self.data[0])
        new_row_0[6] = str(new_row_0[6])
        self.data[0] = new_row_0
        if self.randomisez < 2:
            self.randomisez += 1
        else:
            self.randomisez = 0
        self.data.append(self.data[0])
        del self.data[0]
        if 0 == len(self.data):
            go_words_menu(self1,parent)
            self.__entry.delete(0, 'end') 
            return
        else:
            if self.randomisez == 0 or self.randomisez ==1:
                self.__my_label.config(text=f'{self.data[0][2]}')
                self.__my_label_1.config(text=f'')
            else:
                self.__my_label.config(text=f'{self.data[0][1]}')
                self.__my_label_1.config(text=f'')
        self.__entry.delete(0, 'end') 
        






class ReviseWords(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.data = word_manager._10_words_to_revise(f'profiles/{get_profile()}.csv',)
        self.randomisez = 0

        self.pack(pady=20)

        self.__my_label = Label(self, text = f'{self.data[0][2]}', font =("Helvetica", 20))
        self.__my_label.pack(pady=20)

        self.__my_label_1 = Label(self, text = f'', font =("Helvetica", 20))
        self.__my_label_1.pack(pady=20)

        self.__entry = Entry(self, text="Add new word",width=80, font =("Helvetica", 17))
        self.__entry.pack(pady=20)

        self.__my_botton_check = Button(self, text ="Cehck", command=lambda: give_translations(self.data, self.randomisez, self.__my_label_1),font =("Helvetica", 17))
        self.__my_botton_check.pack(pady= 10)

        text_ok = f'OK - in {int(self.data[0][7]) +1} days'
        self.__my_botton_Yes = Button(self, text =text_ok, command=lambda: ok_revising(), font =("Helvetica", 17))
        self.__my_botton_Yes.pack(pady= 10)

        self.__my_botton_No = Button(self, text ="Nah", command=lambda: nah_revasing(), font =("Helvetica", 17))
        self.__my_botton_No.pack(pady= 10)

        self.__my_botton = Button(self, text ="Menu", command= lambda: go_menu(self,parent), font =("Helvetica", 17))
        self.__my_botton.pack(pady= 10)


        def ok_revising():

            if self.randomisez < 2:
                self.randomisez += 1
            else:
                self.randomisez = 0
            row = self.data[0]
            word_manager.update_revise(f'profiles/{get_profile()}.csv', row, "Yes")
            
            del self.data[0]
            
            if 0 == len(self.data):
                self.__entry.delete(0, 'end') 
                go_words_menu(self,parent)

                return 
            else:
                if self.randomisez == 0 or self.randomisez == 1:
                    self.__my_label.config(text=f'{self.data[0][2]}')
                    self.__my_label_1.config(text=f'')
                else:
                    self.__my_label.config(text=f'{self.data[0][1]}')
                    self.__my_label_1.config(text=f'')
            text_ok = f'OK in {int(self.data[0][7])+1} days'
            self.__my_botton_Yes.config(text=text_ok)
            self.__entry.delete(0, 'end') 

        def nah_revasing():
            if self.randomisez < 2:
                self.randomisez += 1
            else:
                self.randomisez = 0

            row = row = self.data[0]
            word_manager.update_revise(f'profiles/{get_profile()}.csv', row, "No")
            self.data[0][7] = '0'
            self.data.append(self.data[0])
            del self.data[0]
            if 0 == len(self.data):
                self.__entry.delete(0, 'end') 
                go_words_menu(self,parent)
                return
            else:
                if self.randomisez == 0 or self.randomisez == 1:
                    self.__my_label.config(text=f'{self.data[0][2]}')
                    self.__my_label_1.config(text=f'')
                    text_ok = f'OK in {int(self.data[0][7])+1} days'
                    self.__my_botton_Yes.config(text=text_ok)
                else:
                    self.__my_label.config(text=f'{self.data[0][1]}')
                    self.__my_label_1.config(text=f'')
                    text_ok = f'OK in {int(self.data[0][7])+1} days'
                    self.__my_botton_Yes.config(text=text_ok)
            self.__entry.delete(0, 'end') 





class DeleteWords(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.__path = f'profiles/{get_profile()}.csv'

        self.pack(fill=BOTH, expand=True, pady=20)  # Use fill and expand to allow resizing

        # Create a frame for the menu button and title
        self.top_frame = Frame(self)
        self.top_frame.pack(fill=X, pady=10)

        self.__my_label = Label(self.top_frame, text="Delete Words", font=("Helvetica", 30))
        self.__my_label.pack(side="top", pady=20)  # Align below the button

        self.__menu_button = Button(self.top_frame, text="Words Menu", command=lambda: go_words_menu(self, parent), font =("Helvetica", 17))
        self.__menu_button.pack(side="top", pady=10)  # Align at the top

        self.__menu_button = Button(self.top_frame, text="Search", command=lambda: self.on_search(), font =("Helvetica", 17))
        self.__menu_button.pack(side="top", pady=10)  # Align at the top

        

        # Create a canvas and scrollbar
        self.canvas = Canvas(self,  height=470, width=1100, background=self["bg"])
        self.canvas.pack_propagate(False)
        self.scrollbar = Scrollbar(self.canvas, orient="vertical", command=self.canvas.yview,)
        self.scrollable_frame = Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="n")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="top", pady=10, fill="y")
        self.scrollbar.pack(side="right", fill="y")

        

        self.__buttons = []
        words = word_manager.get_all_words(self.__path)
        for word in words:
            button = Button(self.scrollable_frame, text=word[1], command=lambda w=word[1]: self.delete_word(w), font =("Helvetica", 17))
            button.pack(pady=5, side="top", anchor="w")
            self.__buttons.append(button)

    def delete_word(self, word):
        if messagebox.askyesno("Deleting Word", f'Are you sure you want to delete {word}'):
                word_manager.delete_word(self.__path, word)
                self.refresh_view()
        else:
            pass
        

    def refresh_view(self):
        for button in self.__buttons:
            button.destroy()
        self.__buttons.clear()
        words = word_manager.get_all_words(self.__path)
        for word in words:
            button = Button(self.scrollable_frame, text=word[1], command=lambda w=word[1]: self.delete_word(w), font =("Helvetica", 17))
            button.pack(pady=5, side="top", anchor="w")
            self.__buttons.append(button)
            
    
    def on_search(self):
        true_or_false, rijeci = get_matching_words_for_deletion(self.__path)
        if true_or_false:
            for widget in self.__buttons:
                widget.destroy()
            for word in rijeci:
                sta_pisati = f'{word[1]} - {word[2]}'
                button = Button(self.scrollable_frame, text=sta_pisati, command=lambda w=word[1]: self.delete_word(w), font =("Helvetica", 17),wraplength=1100)
                button.pack(pady=5, side="top", anchor="w")
                self.__buttons.append(button)
        else:
            messagebox.showwarning("Warning", "This Word could not be founded")


class PracticeMenu(Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.pack(pady=20)

        self.my_label = Label(self, text='Practice', font=("Helvetica", 42))
        self.my_label.pack(pady=5)

        self.menu_button_short_story = Button(self, text="Short Story", command=lambda: go_ShortStory(self,parent), font =("Helvetica", 17))
        self.menu_button_short_story.pack(pady=10)

        self.menu_button_text_creation = Button(self, text="Text Creation", command=lambda: go_textCreation(self,parent), font =("Helvetica", 17))
        self.menu_button_text_creation.pack(pady=10)

        self.menu_button_menu = Button(self, text="Menu", command=lambda: go_menu(self,parent), font =("Helvetica", 17))
        self.menu_button_menu.pack(pady=10)


class ShortStory(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        pygame.mixer.init()
        try:
            self.__mp3_file = "models\speech.mp3"
            self.__all_words_list = practice_manager.take_all_words_to_practice(f'profiles/{get_profile()}.csv')
            self.__take20_words = practice_manager.teke_fiert_20_words(self.__all_words_list)
            self.__all_words = " ".join(i[0] for i in self.__take20_words)
            self.story_text = text_creation(self.__all_words)
            self.question_list = practice_manager.get_question_list(self.story_text)
            self.__counter = 0


            practice_manager.text_to_speech(self.story_text)
            self.pack(pady=1)

            self.text_widget = Text(self, height=13, width=115, font=("Helvetica", 14))
            self.text_widget.insert(END, self.story_text)
            self.text_widget.config(state='disabled')  
            self.text_widget.pack()

            self.menu = Button(self, text="Menu - Practice", command=lambda: self.on_preesed_menu_button(self,parent), font =("Helvetica", 13))
            self.menu.pack(pady=1)

            self.control_button = Button(self, text="Play Audio", command=self.control_audio, font =("Helvetica", 13))
            self.control_button.pack(pady=(0,1))

            self.Frame_for_question = Frame(self, )
            self.Frame_for_question.pack(padx=10, pady=1)

            self.next_question_Button =  Button(self.Frame_for_question, text="Check the answer", command=lambda: self.next_questions(), font =("Helvetica", 13))
            self.next_question_Button.pack()
            self.next_question_Button_state = False

            self.question= Label(self.Frame_for_question, text=self.question_list[self.__counter], font=("Helvetica", 14))
            self.question.pack(pady=1)

            self.entry_question = Entry(self.Frame_for_question, textvariable="Enter your question", width=170,  font=("Helvetica", 17))
            self.entry_question.pack()

            self.correction_widget = Text(self.Frame_for_question, height=10, width=115, font=("Helvetica", 14))
            self.correction_widget.config(state='disabled')
            self.correction_widget.pack(pady=5)
            #self.entry_question.bind("<Return>", self.answer_correction()) 
            # Track the playback state
            self.playing = False
            self.paused = False

        except httpx.ReadTimeout as e:
            messagebox.showwarning("httpx.ReadTimeout", "Try some other time")
            go_menu(self,parent)

    

    def control_audio(self):

        if not os.path.exists(self.__mp3_file):
            messagebox.showwarning("File Not Found", "The audio file does not exist. Please wait until the audio is generated.")
            return
        if not self.playing:
            # Start playback
            pygame.mixer.music.load(self.__mp3_file)
            pygame.mixer.music.play()
            self.playing = True
            self.paused = False
            self.control_button.config(text="Pause Audio")
        elif self.paused:
            # Resume playback
            pygame.mixer.music.unpause()
            self.paused = False
            self.control_button.config(text="Pause Audio")
        else:
            # Pause playback
            pygame.mixer.music.pause()
            self.paused = True
            self.control_button.config(text="Resume Audio")
        self.check_audio_finished()

    
    def check_audio_finished(self):
        if not pygame.mixer.music.get_busy() and not self.paused:
            # Audio has finished, reset the state
            self.playing = False
            self.paused = False
            self.control_button.config(text="Play Again")  # Reset button to 'Play'
    
        self.after(500, self.check_audio_finished)

    def stop_and_delete_audio(self):
        try:
            # Stop the playback if playing
            if self.playing or self.paused:
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                self.playing = False
                self.paused = False
            delete_file(self.__mp3_file)
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting file: {str(e)}")

    def on_preesed_menu_button(self,self1,parent):
        self.entry_question.delete(0, END)
        self.__all_words_list.clear()
        go_practising(self1,parent)
        self.stop_and_delete_audio()

    def next_questions(self):
        if self.__counter >= len(self.question_list):
            messagebox.showerror("Error", "No more questions")
            return

        if not self.next_question_Button_state:
            
            self.answer_correction()
            self.next_question_Button_state = True
            self.next_question_Button.config(text='Next question')
            if  self.__counter == len(self.question_list) - 1:
                self.__counter += 1
            return

        # At this point, next_question_Button_state is True
        if self.__counter + 1 < len(self.question_list):
            self.__counter += 1
            self.question.config(text=f'{self.question_list[self.__counter]}')
            self.entry_question.delete(0, END)
            self.correction_widget.config(state='normal')
            self.correction_widget.delete('1.0', END)
            self.correction_widget.config(state='disabled')

        self.next_question_Button_state = False
        self.next_question_Button.config(text='Check the answer')


    def answer_correction(self): 
        correction_text = practice_manager.questions_correction(self.question_list[self.__counter], self.entry_question.get(), self.story_text)
        self.correction_widget.config(state='normal')
        self.correction_widget.insert(END, correction_text)
        self.correction_widget.config(state='disabled')


class TextCreation(Frame):
    def __init__(self, parent):
        super().__init__(parent)
        try:
            self.n = 0
            self.pack(expand=True, fill='both')

            bla = practice_manager.take_all_words_to_practice(f'profiles/{get_profile()}.csv')
            bla1 = practice_manager.teke_fiert_20_words(bla)

            self.__topic = practice_manager.written_text_task(bla1)

            self.__topic_label = Label(self, text=self.__topic, font=("Helvetica", 14))
            self.__topic_label.pack(pady=1)
            
            self.__help_label = Label(self, text="Here are help words:", font=("Helvetica", 14))
            self.__help_label.pack(pady=5)
            
            self.correction_text = Text(self, width=100, height=10, font=("Helvetica", 14))
            """
            self.__my_frame = customtkinter.CTkScrollableFrame(self,corner_radius=20, bg_color="transparent")
            self.__my_frame.pack(pady=5, fill = "x")

            for i in range(0,len(bla1)):             
                text_za_check_box =bla1[i][0]
                button = customtkinter.CTkCheckBox(self.__my_frame, text= text_za_check_box, font=("Helvetica", 14))
                button.pack(pady = 5)
                """
            """
            self.__my_frame = Frame(self, width=1100, height=250, background="white")
        # Onemogućava promjenu veličine Frame-a zbog unutrašnjih widgeta
            self.__my_frame.pack(padx=10, pady=10)
            self.__my_frame.pack_propagate(False)
            for i in range(0,len(bla1)):             
                text_za_check_box =bla1[i][0]
                button = Checkbutton(self.__my_frame, text= text_za_check_box, font=("Helvetica", 14))
                button.pack(pady=5, side="top", anchor="w")
            """
            # Dodavanje widgeta unutar Frame-a
            
            self.canvas = Canvas(self,  height=250, width=1100, background=self["bg"])
            self.canvas.pack_propagate(False)
            self.scrollbar = Scrollbar(self.canvas, orient="vertical", command=self.canvas.yview,)
            self.scrollable_frame = Frame(self.canvas)
           
            self.scrollable_frame.bind(
                "<Configure>",
                lambda e: self.canvas.configure(
                    scrollregion=self.canvas.bbox("all")
                )
            )

            self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="n", )
            self.canvas.configure(yscrollcommand=self.scrollbar.set)

            self.canvas.pack(side="top", pady=10)
            self.scrollbar.pack(side="right", fill="y")

           

            #self.buttons_frame.pack(side="top")

            """
            for i in range(0,50):
                button = Button(self.scrollable_frame, text=i,background="green")
                button.pack(pady=10, side="top")
                """



            for i in range(0,len(bla1)):             
                text_za_check_box =bla1[i][0]
                button = Checkbutton(self.scrollable_frame, text= text_za_check_box, font=("Helvetica", 20), )
                button.pack(pady=2, side="top", anchor="w")




        

            self.write_text = Text(self, width=100, height=10, font=("Helvetica", 14))
            self.write_text.pack(pady=5)
            

            self.practise_button =  Button(self, text="Back", command=lambda: go_practising_ovo_ono(self,parent,bla))
            self.practise_button.pack()

            self.submit_Button= Button(self, text="Submit",command=lambda: self.Correction(parent,bla))
            self.submit_Button.pack()
        except httpx.ReadTimeout as e:
            messagebox.showwarning("httpx.ReadTimeout", "Try some other time")
            go_menu(self,parent)

    def Correction(self, parent,bla):
        self.canvas.destroy()
        self.practise_button.destroy()
        self.submit_Button.destroy()

        text = self.write_text.get('1.0', END)
        self.__help_label.config(text="Correction of the text: ")
        corrected_text = practice_manager.corrected_text(text)
        self.correction_text.config(state="normal")
        self.correction_text.delete('1.0', END)
        self.correction_text.insert(END, corrected_text)
        self.correction_text.config(state="disabled")
        self.write_text.config(state="disabled")

        self.correction_text.pack(pady=10)

        self.practise_button =  Button(self, text="Back", command=lambda: go_practising_ovo_ono(self,parent,bla))
        self.practise_button.pack()


        
       


        
        
        