#! /bin/sh
CURRENTDIR="$PWD"
SPIDERS=('OSC')
DIR_ANTH='/Volumes/MyPassport/ANTH/'
MDB=/usr/local/bin/mongod
DIR_MDB_DB="${DIR_ANTH}"
DIR_MDB_LOG="${DIR_ANTH}"

for spider in ${SPIDERS}
do
    DIR_MDB_LOG="${DIR_MDB_DB}${spider}/mongodb.log"
    DIR_MDB_DB="${DIR_MDB_DB}${spider}/db"
    mkdir -p "$DIR_MDB_DB"
    MDB_CFG="--dbpath $DIR_MDB_DB --logpath $DIR_MDB_LOG"

    # start mongodb server daemon
    ${MDB} ${MDB_CFG} > /dev/null 2>&1 &

    # run spider
    cd ${CURRENTDIR}/${spider}
    scrapy crawl ${spider} > /dev/null 2>&1
done
