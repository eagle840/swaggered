docker run -d --name dbtx -e MYSQL_ROOT_PASSWORD=1234 mysql
sleep 10

# change the my.cnf to allow LOAD DATA INLINE
docker cp dbtx:/etc/mysql/my.cnf .
echo add.txt >> my.cnf
docker cp my.cnf dbtx:/etc/mysql/.

# copy db script over

docker cp db_script.sql dbtx:/.

docker restart dbtx






