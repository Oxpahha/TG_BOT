from datetime import datetime

token_path = ".env"
logger_path = ""

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