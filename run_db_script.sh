echo pulling/running sql
docker run -d --name dbtx -e MYSQL_ROOT_PASSWORD=1234 mysql
sleep 10

# following lines removed and just replaced with a my.cnf ready to go
# echo change the my.cnf to allow LOAD DATA INLINE
# docker cp dbtx:/etc/mysql/my.cnf .
# cat add.txt >> my.cnf
echo copy my.cnf to container
docker cp my.cnf dbtx:/etc/mysql/.

echo copy files to dbtx

docker cp db_script.sql dbtx:/.
docker cp titanic.csv dbtx:/.
docker cp runsql.sh dbtx:/.
echo restarting mysql server dbtx
docker restart dbtx

echo running db input script
# docker exec -it dbtx mysql < db_script.sql
# [failed  noted uses -d] docker exec -d dbtx  /usr/bin/mysql -uroot -p1234 < db_script.sql
# [failed, but manually it works] docker exec -d dbtx /bin/sh -c ./runsql.sh
echo checking version
docker exec  dbtx  /usr/bin/mysql --version
echo checking dbs
docker exec  dbtx  /usr/bin/mysql -uroot -p1234 -e "show status;"
docker exec  dbtx  /usr/bin/mysql -uroot -p1234 -e "show databases;"
echo running script
docker exec  dbtx  /usr/bin/mysql -uroot -p1234 < db_script.sql
echo checkig databases
docker exec  dbtx  /usr/bin/mysql -uroot -p1234 -e "show databases;"

echo cmd prompt sql server
docker exec -it dbtx /bin/bash




