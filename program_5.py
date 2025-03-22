#By: Sabria Fafach
#Date: March 21, 2025
#Title: program_5.py


def make_dictionary():
    input_info=input("Do you want to enter the name and ID for a course? If yes, enter y:")
    course_dict={}
    while input_info=="y":
        name=input("Enter the name of the course:")
        ID=input(f"Enter the course ID for {name}.")
        course_dict[ID] = name
        input_info=input("Do you want to enter the name and ID for another course? If yes, enter y:")
        
    return course_dict

def search_subjects(dictionary):
    search_subject=input("Do you want to search for a subject in the dictionary? If yes, enter y:")
    while search_subject=="y":

        subject=input("Enter the name of the subject(Example:COS):")
        keys=""
        for key in dictionary:
            courses = []
            keys+=key
            if subject in keys:
                 courses.append(key)
                 courses.append(dictionary.get(key))
            print(f"The courses that teach the subject you chose are {courses}.")
        search_subject=input("Do you want to search for another subject in the dictionary? For yes, enter y: ")

    return courses

def main():
    course_dictionary=make_dictionary()


    search_subjects(course_dictionary)



if __name__ == '__main__':
    main()











