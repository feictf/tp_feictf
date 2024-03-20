# feictf

`curl -fsSL https://get.docker.com | /bin/sh`

`git clone https://github.com/feictf/tp_feictf.git /opt/dojo`

upraviť port na ssh z 22 na iný (napríklad 2222) v súbore `/etc/ssh/sshd_config` (iptables -I INPUT -p tcp --dport 2222 -j ACCEPT)
`service ssh restart`

`SETUP_HOSTNAME=<IP> ./run.sh`

prihlasovacie údaje do admin účtu sú v `data/initial_credentials`

*Poznámka: V prípade, že sa po úspešnom spustení na prehliadači objaví chyba 503, môže ísť o miskofinguráciu nginx pre vnútorný proxy https://github.com/pwncollege/dojo/issues/52.*

