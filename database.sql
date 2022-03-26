drop database if exists contacts;

create database contacts;

use contacts;

create table numbers (
    UID int,
    Name varchar(25),
    Phone_Number varchar(20),
    profilepic varchar(65535)
);

create table users (
    UID int not null PRIMARY KEY,
    username varchar(25),
    password varchar(100),
    Phone_Number varchar(20)
);