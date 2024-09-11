import os

class ProfileManager:
    def __init__(self) -> None:
        self.__data = []
        self.__choosen_profile = ""
        self.__folder_path = "profiles"
        self.list_csv_profiles()
   

    def list_csv_profiles(self):

       if os.path.exists(self.__folder_path):
        files = os.listdir(self.__folder_path)
        
        for file_name in files:
            if file_name.endswith('.csv'):
                name_without_extension = file_name.replace('.csv', '')
                self.__data.append(name_without_extension)



    def get_data(self):
        return self.__data
    
    def get_profile_count(self):
        return len(self.__data)
    
    def create_profile(self, profile_name):
        if profile_name in self.__data:
            print("Profile already exists.")
        else:
            os.makedirs(self.__folder_path, exist_ok=True)
            with open(f'{self.__folder_path}/{profile_name}.csv', 'w', newline='') as file:
                pass
            self.__data.append(profile_name)
            self.__choosen_profile = profile_name


    def choose_profile(self, number):
        self.__choosen_profile = self.__data[number]
        return self.__choosen_profile

    def get_chosen_profile(self):
        return self.__choosen_profile 
    
    def delete_profile(self, number):
        if self.__data[number]:
            deleted_profile = self.__data[number]
            file_path = os.path.join(self.__folder_path, self.__data[number] + '.csv')
            self.__data.remove(self.__data[number])
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Profile '{deleted_profile}' deleted.")
            else:
                print(f"File '{file_path}' does not exist.")
        else:
            print(f"Profile '{deleted_profile}' not found in the list.")


    def delete_all_profiles(self):
        for i in range(0, self.get_profile_count()):
            self.delete_profile(self.get_data()[0])
