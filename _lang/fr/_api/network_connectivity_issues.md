---
nav_title: Problèmes de connectivité réseau d’API
article_title: Problèmes de connectivité réseau d’API
page_order: 4
description: "Cet article de référence aborde les problèmes de connectivité d’API et comment les résoudre." 
page_type: reference

---
# Problèmes de connectivité d’API

> Cet article de référence aborde les problèmes de connectivité d’API et comment les résoudre. 

Les endpoints API de Braze utilisent un CDN qui achemine le trafic vers le POP le plus proche selon les informations du DNS.  Si vous rencontrez des problèmes de connexion ou remarquez que vous vous connectez à un POP inefficace, assurez-vous d’utiliser les serveurs DNS de votre fournisseur ou les serveurs DNS configurés dans le même centre de données que votre serveur et de disposer des métadonnées appropriées de localisation IP associées à ces derniers.

Nous avons remarqué que quelques pare-feux tentaient de modifier ou de sécuriser
le trafic HTTPS/TLS, ce qui interfère avec les connexions aux endpoints d’API de Braze. Si vos serveurs se trouvent derrière un pare-feu physique, désactivez toutes les accélérations ou modifications HTTPS/TLS que le ou les pare-feux et/ou routeurs effectuent.  De plus, vous pouvez établir une liste blanche du trafic sortant auprès de nos fournisseurs CDN (Fastly.com) pour voir si cela résout le problème.

Occasionnellement, les configurations iptables qui filtrent les paquets SYN/ACK/RST peuvent également causer des problèmes. Si vous utilisez des tables iptables sur votre hôte, vous pouvez également établir une liste blanche du trafic sortant après de nos fournisseurs CDN (Fastly.com) pour voir si cela résout le problème.

Si vous rencontrez toujours des problèmes réseau en vous connectant à l’endpoint d’API de Braze, fournissez un [test MTR][1] et les résultats du [débogage de Fastly][2]
au moment du problème et soumettez-les avec votre demande d’assistance.
Notez que les résultats des tests doivent être obtenus à partir d’un serveur ayant des problèmes liés à l’endpoint d’API de Braze, et non à partir d’un ordinateur de développement.  Une capture du réseau (fichier tcpdump ou .pcap) sera également utile si elle peut être obtenue.

Pour plus d’informations sur le MTR, consultez ces ressources en fonction de votre système d’exploitation :

- [GNU/Linux][4]
- [macOS][5]

## Établir une liste blanche des plages IP de l’endpoint d’API de Braze

Pour établir la liste blanche de l’endpoint d’API de Braze via votre pare-feu, notre CDN donne accès à la liste des plages IP attribuées en utilisant la méthode json.dump. Pour obtenir une liste des plages IP de Fastly, consultez leur [liste d’IP publiques][3].


[1]: https://www.privateinternetaccess.com/helpdesk/kb/articles/what-is-an-mtr-test-and-how-do-i-run-one-2
[2]: http://www.fastly-debug.com/
[3]: https://api.fastly.com/public-ip-list
[4]: https://www.digitalocean.com/community/tutorials/how-to-use-traceroute-and-mtr-to-diagnose-network-issues
[5]: https://formulae.brew.sh/formula/mtr

