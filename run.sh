#!/bin/sh

echo "ahoj kubo -> cau palo"
echo $(date); echo "Run spusteny! od" $(tty) | wall

DIR="$(readlink -f $(dirname $0))"

if [ ! -f "$DIR/data/config.env" ] && [ -z "$SETUP_HOSTNAME" ]; then
    echo "Error: instance not setup; rerun with SETUP_HOSTNAME environment variable!"
    exit 1
fi

docker kill pwn.college
docker build -t pwn.college .

docker run \
       --privileged \
       --detach \
       --rm \
       --volume $PWD/data/docker:/var/lib/docker \
       --volume $PWD/data:/opt/pwn.college/data \
       --publish 22:22 \
       --publish 80:80 \
       --publish 443:443 \
       --env SETUP_HOSTNAME="$SETUP_HOSTNAME" \
       --name pwn.college \
       pwn.college

#docker exec pwn.college bash
docker exec -it pwn.college bash -c "sleep 18; docker exec -it ctfd_proxy bash -c 'sed -i \"53,59d\" /etc/nginx/conf.d/default.conf; sleep 4; service nginx restart; sed -i \"58d\" /etc/nginx/conf.d/default.conf; service nginx restart;'"


echo "Run done." | wall