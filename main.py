from ast import Break
import pymysql 
import psutil
import os
import threading
import math
import sys
#print(sys.setrecursionlimit(2000))
from config import keyw,host,user,password,db_name;

     
#получаем id
def returnid(login,curs):
    q = "select iduser from user where usercol='%s'"%(login);
    curs.execute(q);
    res = curs.fetchone();
    return  res[0];
                 
#среднее значение загруженности процессора агента

def average(id,curs):
    query = "select AVG(info_pers) as avg from info where user_iduser='%i'"%(id);
    curs.execute(query);
    res = curs.fetchone();
    return res[0];


#среднее значение загруженности процессора всех агентов

def common_average(curs):
    query = "select AVG(info_pers) as avg from info";
    curs.execute(query);
    res = curs.fetchone();
    return res[0];  

 #до    
def add_user(curs,name):
    t = (name)
    query = "Insert into user(usercol) values(%s)";
    curs.execute(query,t);
    #curs.commit();
    return 1;

#поток добаваления информации в БД о системе каждые 1 мин
def thread_to_add():
    threading.Timer(60.0, thread_to_add).start(); # Перезапуск через 5 секунд
    def add_info():
        #threading.Timer(5.0, add_info).start()  # Перезапуск через 5 секунд
        con = pymysql.connect(host=host, user=user, passwd=password, db=db_name);
        info = math.floor(psutil.cpu_percent(interval=1));
        with con:
            with con.cursor() as curs111:
                id = returnid(login,curs111);
            # threading.Timer(5.0, add_info).start()  # Перезапуск через 5 секунд
                t = (info,id)
                query = "Insert into info (info_pers,user_iduser) values(%s,%s)";
                curs111.execute(query,t);
                con.commit();
        return 1;
    add_info()





#основная программа
while True:
    print("--------------------------------------------");
    print("1) Зарегистрироваться как пользователь");
    print("2) Вход в систему");
    print("3) Выход из системы");
    choise =int(input());

    con = pymysql.connect(host=host, user=user, passwd=password, db=db_name);
    with con:
        if choise == 1:
            login = input("Вваедите ваше имя для регистрации:");
            key =input("Введите ключевое слово :");
            if key == keyw:
                with con.cursor() as cursor3:                    
                    add_user(cursor3,login);
                    con.commit();
                    print("Пользователь успешно зарегистрирован!");

        elif choise == 2:
            login = input("Введите имя пользователья для входа в систему :");
            key =input("Введите ключевое слово :");
            if key == keyw:
                print("Добро пожаловать",login,"!");
                with con.cursor() as cursor1:
                    userid = returnid(login,cursor1);
            thread_to_add();  
            while True:

                print("--------------------------------------------");
                print("1 - Узнать ID");
                print("2 - Среднее значение использования ЦП ",login);
                print("3 - Среднее значение использования ЦП все пользователей");
                print("4 - Проверить отклонения от среднего значения");

                print("0 - Выход");
        
                choise1 = int(input());
                if choise1 == 1:
                        print("Ваш ID = ",userid);
                    
                elif choise1 == 2:
                    with con.cursor() as cursor:
                        average =average(userid,cursor);
                        print("Среднее значение использования процессора во всех ядрах на вашем компютере : ",average,"%");
                elif choise1 == 3:
                    with con.cursor() as cursor2:
                        common_average = common_average(cursor2);
                        print("Среднее значение использования процессора во всех ядрах во всех компютерах системы : ",common_average,"%");
                elif choise1 == 4:
                    deviation = average-common_average;
                    if deviation <0:
                        print("Ваш процессор работает отлично, и загружена на ",abs(deviation),"% меньше чем среднее значение загруженности системы");
                    elif deviation > 40:
                        print("Ваш процессор нагружен сильно, на",deviation,"%")
                    else:
                        print("Ваш процессов работает в нормальном состоянии");
                else:
                    break      
            else:
                print("Неверное ключевое слово, повторите, пожалуйста");

        elif choise == 3:
            break





        






