from PyQt5 import QtSql

db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
db.setDatabaseName('db.sqlite')

if not db.open():
    print("Cannot open database")

query = QtSql.QSqlQuery()
# query.exec_("drop table users if exists")
query.exec_("create table users (id integer primary key autoincrement not null, username varchar(20) not null, password varchar(20) not null);")
query.exec_("insert into users (username, password) values ('admin', 'admin');")

query.exec_("select * from users")
query.first()
print(query.value("username"), query.value("password"))