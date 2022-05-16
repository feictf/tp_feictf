# feictf

## Návod na spustenie vlastnej inštancie

Platforma feictf bola testovaná na operačných systémoch Debian GNU/Linux 11 (bullseye) x86_64 a Ubuntu 20.04.1 LTS x86_64.
Medzi požiadavky na nainštalovanie vlastnej inštancie feictf patrí docker. 

`curl -fsSL https://get.docker.com | /bin/sh`

Následne si treba naklonovať repozitár: 
`git clone https://github.com/tp\_feictf`

Ďalej treba upraviť prihlasovací port na ssh z 22 na iný (napríklad 2222) v súbore `etc/ssh/sshd\_config` a reštartovať ssh service:
`service ssh restart`


Pri prvom spustení je treba definovať globálnu premennú **SETUP_HOSTNAME**, čiže v tomto prípade danú url či IP adresu alebo *localhost*.
`SETUP\_HOSTNAME=localhost ./run.sh`

*Poznámka: V prípade, že sa po úspešnom spustení na prehliadači objaví chyba 503, môže ísť o miskofinguráciu nginx pre vnútorný proxy https://github.com/pwncollege/dojo/issues/52.*

