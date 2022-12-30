from datetime import datetime
import csv

token_path = ".env"
logger_path = ""
book_path = "./.book/book.csv"


def add_book_user(subject, id='', username='', first_name='', last_name='', check = '1'):
    write_book(f'\n{subject},{id},{username},{first_name},{last_name},{check}')

def write_book(data):
    with open(book_path,'a',encoding= 'utf-8') as file:
        file.writelines(data)

def find_book_csv(data):
    with open(book_path, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if data in row:
                return(row)

def check_set_book_csv(user_id, check):
    with open(book_path, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if user_id in row:
                row[5] = check




        
# test_subject = 'politiес'
# test_id = '23121'
# test_username = 'jobb'
# test_first_name = 'Jack'
# test_last_name = 'Jojo'
# add_book_user(test_subject,test_id,test_username,test_first_name,test_last_name)

# print(find_book_csv('str3'))


def log_init():
    global logger_path
    logger_path = f'./.logs/logs.{datetime.now().strftime("%d.%m")}.csv'

def read_token():
    with open(token_path,'r',encoding= 'utf-8') as file:
        return file.readlines()

def current_time():
    return(datetime.now().strftime('%H:%M:%S'))

def current_date():
    return(datetime.now().strftime('%d/%m/%Y'))

def write_log(data):
    with open(logger_path,'a',encoding= 'utf-8') as file:
        file.writelines(data)

def read_log():
    with open(logger_path,'r',encoding= 'utf-8') as file:
        return file.readlines()      

def log_data_check():
    if str.split(logger_path,'.')[3] != datetime.now().strftime('%d'):
        return True
    else : return False

def add_log(text='', id='', username='', first_name='', last_name=''):
    if log_data_check():
        new_log_file()
    write_log(f'\n{current_date()},{current_time()},{text},{id},{username},{first_name} {last_name}')

def new_log_file():
    global logger_path
    logger_path = f'./.logs/logs.{datetime.now().strftime("%d.%m")}.csv'
    with open(logger_path,'w+',encoding='utf-8') as file:
        file.writelines('Date,Time,MSG,User_ID,UserName,User_Full_Name')
    return 0


# for i in range(1,len(read_log())):
#     if day != str.split((str.split((read_log()[i]),',')[0]),'/')[0]: