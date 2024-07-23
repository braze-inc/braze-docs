---
nav_title: Problèmes de connectivité réseau d’API
article_title: Problèmes de connectivité réseau d’API
page_order: 4
description: "Cet article de référence aborde les problèmes de connectivité d’API et comment les résoudre."
page_type: reference

---

# Problèmes de connectivité réseau de l’API

> Cet article de référence aborde les problèmes de connectivité d’API et comment les résoudre.

Les endpoints API de Braze utilisent un CDN qui achemine le trafic vers le POP le plus proche selon les informations du DNS.  Si vous rencontrez des problèmes de connexion ou remarquez que vous vous connectez à un POP inefficace, assurez-vous d’utiliser les serveurs DNS de votre fournisseur ou les serveurs DNS configurés dans le même centre de données que votre serveur et de disposer des métadonnées appropriées de localisation IP associées à ces derniers.

Nous avons remarqué qu’une poignée de pare-feu tentent de modifier ou de sécuriser HTTPS/TLS traffic which interferes with connections to Braze API endpoints. If your servers are behind any sort of physical firewall, disable any HTTPS/TLS acceleration or modifications that the firewall or router is performing. Additionally, you can allowlist outbound traffic to our CDN providers (Fastly.com) to see if that resolves the issue.

Occasionnellement, les configurations iptables qui filtrent sur les paquets SYN/ACK/RST packets can also cause issues, so if you are using iptables on your host you could also allowlist outbound traffic to our CDN providers (Fastly.com) to see if that resolves the issue.

Si vous rencontrez toujours des problèmes de réseau lors de la connexion aux points de terminaison de l’API Braze, fournissez un [test MTR][1] et les résultats de [Fastly Debug][2] lors de la rencontre d’un problème et soumettez-les à votre demande d’assistance. Notez que les résultats des tests doivent être obtenus à partir d’un serveur ayant des problèmes liés à l’endpoint d’API de Braze, et non à partir d’un ordinateur de développement. Une capture du réseau (fichier tcpdump ou .pcap) sera également utile si elle peut être obtenue.

Pour plus d’informations sur le MTR, consultez ces ressources en fonction de votre système d’exploitation :

- [][4]GNU/Linux
- [macOS][5]

## Liste d’autorisation des plages d’adresses IP des points de terminaison de l’API Braze

Pour établir la liste blanche des endpoints d’API de Braze via votre pare-feu, notre CDN donne accès à la liste des plages IP attribuées en utilisant la méthode json.dump. Pour obtenir la liste des plages d’adresses IP de l’API Braze, reportez-vous à la [liste des adresses IP publiques de Fastly][3] et à [la liste des adresses IP publiques de Cloudflare][6]. Notez que ces adresses IP peuvent changer.

[1]: https://www.privateinternetaccess.com/helpdesk/kb/articles/what-is-an-mtr-test-and-how-do-i-run-one-2
[2]: http://www.fastly-debug.com/
[3]: https://api.fastly.com/public-ip-list
[4]: https://www.digitalocean.com/community/tutorials/how-to-use-traceroute-and-mtr-to-diagnose-network-issues
[5]: https://formulae.brew.sh/formula/mtr
[6]: https://api.cloudflare.com/client/v4/ips
