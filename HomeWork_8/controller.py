import view

main_dct = {}
student_name = []
lessons = []

def start():
    while True:
        op = view.get_op()
        if op == 1:
            student = view.input_student()
            if student not in student_name:
                main_dct[student] = {}
                student_name.append(student)
                if lessons:
                    for less in lessons:
                        main_dct[student][less] = []
            print(main_dct)
           
        elif op == 2:
            less = view.input_lesson()
            lessons.append(less)
            for name in student_name:
                main_dct[name][less] = []
            print(main_dct)
        
        elif op == 3:
            name, less, mark = view.input_mark()
            main_dct[name][less].append(mark)
            print(main_dct)
            
        elif op == 4:
            print(main_dct)
            
        elif op == 5:
            name = view.get_name_to_show()
            print(f'Оценки {name} - {main_dct[name]}')
            print(main_dct)
           
        elif op == 6:
            break
        
    
        