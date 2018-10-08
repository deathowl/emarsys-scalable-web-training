set harakiri timeout, also enable master
uwsgi --socket 0.0.0.0:8000 --protocol=http -w webapp -t 5 --master


REDIS_HOST="localhost" rq worker    