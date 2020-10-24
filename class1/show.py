# show databases;                                           //查看所有数据库
# create database hrz;                                      //创建数据库hrz
# use hrz;                                                  //切换数据库
# create table data (name char(16),password char(16));      //创建data表字段为name,password
# show tables;                                              //查看表
# desc data;                                                //查看表中结构字段
# insert into data (name,password) values ('hrz','123');    //给表data表添加内容
# select * from data;                                       //查看表中内容
# update data set password=321 where name='hrz';             //将表中的hrz用户密码有原来的123改为321
# select * from data;                                        //查看密码已经修改成功
# insert into data (name,password) values ('h','123');
# insert into data (name,password) values ('r','123');
# insert into data (name,password) values ('z','123');
# select * from data;
# delete from data where name='hrz';                         //删除data表中hrz用户
# select * from data;
# delete from data;                                          //删除表中所有数据
# select * from data;
# drop table data;                                           //删除数据表data
# show tables;
# drop database hrz;                                         //删除数据库hrz
# show databases;
# alter table data rename data2;                             //修改表明为data2
# alter table data2 add "email" char(48)NOT NULL;            //在表data2中添加email字段
# alter table data2 change "email" "qq" char(10) NOT NULL;   //将data2表中的字段email改为qq
# alter table data2 drop "password";                         //删除data2表中的password字段
# import pymysql

