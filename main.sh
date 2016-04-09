source ~/.zshrc
export REALM=ntu.prod TMP=$(mktemp)
echo $REALM && cat haproxy.cfg | envsubst |tee $TMP
export PORT_PREFIX=3
dod -p ${PORT_PREFIX}5432:5432 -p ${PORT_PREFIX}8080:8080 -p ${PORT_PREFIX}6379:6379 -p ${PORT_PREFIX}8083:8083 -p ${PORT_PREFIX}8086:8086 -p ${PORT_PREFIX}5601:5601 -p ${PORT_PREFIX}3000:3000 -p ${PORT_PREFIX}5000:5000 -p ${PORT_PREFIX}9200:9200 -p ${PORT_PREFIX}7017:27017 -v $TMP:/usr/local/etc/haproxy/haproxy.cfg haproxy

