
import pymysql 
from config import keyw,host,user,password,db_name;
def returnid(login,curs):
    q = "select iduser from user where usercol='%s'"%(login);
    curs.execute(q);
    res = curs.fetchone();
    return  res[0];
                 
def average(id,curs):
    query = "select AVG(info_pers) as avg from info where user_iduser='%i'"%(id);
    curs.execute(query);
    res = curs.fetchone();
    return res[0];


while True:
    print("--------------------------------------------");
    print("1) Вход в систему");
    print("2) Выход из системы");
    choise =int(input())
    if choise == 1:
        login = input("Введите имя пользователья для входа в систему :");
        key =input("Введите ключевое слово :");
        if key == keyw:
            print("Добро пожаловать",login,"!")
            con = pymysql.connect(host=host, user=user, passwd=password, db=db_name);
            with con:
                while True:
                    print("--------------------------------------------");
                    print("1 - Узнать ID");
                    print("2 - Среднее значение использования ЦП");
                    print("0 - Выход");

                    with con.cursor() as cursor1:
                            userid = returnid(login,cursor1)
                    choise1 = int(input());

                    if choise1 == 1:
                        print("Ваш ID = ",userid);
                    elif choise1 == 2:
                        with con.cursor() as cursor:
                            print("Среднее значение использования процессора во всех ядрах на вашем компютере : ",average(userid,cursor),"%");
                    else:
                        exit()
                   
        else:
            print("Неверное ключевое слово, повторите, пожалуйста");

     



        






