# Create new db

create database titanic;
use titanic;

# Create table

create table passengers (
     survived bool not null, 
     passengerClass  int not null,
     name  varchar(255) not null,
     sex ENUM ('male', 'female', 'other') not null,
     age int not null,
     siblingsOrSpousesAboard tinyint not null,
     parentsOrChildrenAboard tinyint not null,
     fare   decimal not null,
     uuid varchar(255) not null, 
     primary key (uuid),
     key name (name)
     )engine=innodb
     default charset=utf8;
     
# Load data titanic.csv into table passengers
# note that LOAD DATA must be enbled 
# see https://stackoverflow.com/questions/10762239/mysql-enable-load-data-local-infile
     
LOAD DATA LOCAL INFILE '/titanic.csv' INTO TABLE passengers FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS (survived,passengerClass,name,sex,age,siblingsOrSpousesAboard,parentsOrChildrenAboard,fare,@uuid)  SET uuid = UUID() ;
