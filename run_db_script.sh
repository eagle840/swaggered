echo pulling/running sql
docker run -d --name dbtx -e MYSQL_ROOT_PASSWORD=1234 mysql
sleep 10

echo change the my.cnf to allow LOAD DATA INLINE
docker cp dbtx:/etc/mysql/my.cnf .
cat add.txt >> my.cnf
docker cp my.cnf dbtx:/etc/mysql/.

echo copy files to dbtx

docker cp db_script.sql dbtx:/.
docker cp titanic.csv dbtx:/.
docker cp runsql.sh dbtx:/.
echo restarting mysql server dbtx
docker restart dbtx

echo running db input script
# docker exec -it dbtx mysql < db_script.sql
# [failed] docker exec -d dbtx  /usr/bin/mysql -uroot -p1234 < db_script.sql
docker exec -d dbtx /bin/sh -c ./runsql.sh

echo cmd prompt sql server
docker exec -it dbtx /bin/bash




