---
nav_title: Problèmes de connectivité réseau d’API
article_title: Problèmes de connectivité réseau d’API
page_order: 4
description: "Cet article de référence aborde les problèmes de connectivité d’API et comment les résoudre."
page_type: reference

---

# Problèmes de connectivité réseau de l’API

> Cet article de référence aborde les problèmes de connectivité d’API et comment les résoudre.

Les endpoints de l'API de Braze utilisent un réseau de diffusion de contenu qui achemine le trafic vers le POP le plus proche en fonction des informations DNS.  Si vous rencontrez des problèmes de connexion ou remarquez que vous vous connectez à un POP inefficace, assurez-vous d’utiliser les serveurs DNS de votre fournisseur ou les serveurs DNS configurés dans le même centre de données que votre serveur et de disposer des métadonnées appropriées de localisation IP associées à ces derniers.

Nous avons remarqué qu'une poignée de pare-feu tentent de modifier ou de sécuriser le trafic HTTPS/TLS, ce qui interfère avec les connexions aux points d'extrémité de l'API de Braze. Si vos serveurs se trouvent derrière un quelconque pare-feu physique, désactivez toute accélération ou modification HTTPS/TLS effectuée par le pare-feu ou le routeur. En outre, vous pouvez autoriser le trafic sortant vers nos fournisseurs de réseau de diffusion de contenu (Fastly.com) pour voir si cela résout le problème.

Parfois, les configurations d'iptables qui filtrent les paquets SYN/ACK/RST peuvent également causer des problèmes. Si vous utilisez iptables sur votre hôte, vous pouvez également autoriser le trafic sortant vers nos fournisseurs de réseau de diffusion de contenu (Fastly.com) pour voir si cela résout le problème.

Si vous rencontrez toujours des problèmes de réseau lors de la connexion aux endpoints de l'API Braze, fournissez un [test MTR](https://www.privateinternetaccess.com/helpdesk/kb/articles/what-is-an-mtr-test-and-how-do-i-run-one-2) et les résultats de [Fastly Debug](http://www.fastly-debug.com/) pendant que vous rencontrez un problème et soumettez-les avec votre demande d'assistance. Notez que les résultats du test doivent être obtenus à partir d'un serveur qui rencontre des problèmes de connexion aux points d'extrémité de l'API Braze, et non à partir d'une machine de développement. Une capture du réseau (fichier tcpdump ou .pcap) sera également utile si elle peut être obtenue.

Pour plus d’informations sur le MTR, consultez ces ressources en fonction de votre système d’exploitation :

- [GNU/Linux](https://www.digitalocean.com/community/tutorials/how-to-use-traceroute-and-mtr-to-diagnose-network-issues)
- [macOS](https://formulae.brew.sh/formula/mtr)

## Autoriser la liste des plages d'adresses IP des points d'extrémité de l'API Braze

Pour autoriser les points d'extrémité de l'API Braze à travers votre pare-feu, notre réseau de diffusion de contenu permet d'accéder à la liste des plages d'adresses IP attribuées par le biais d'un vidage JSON. Pour obtenir une liste des plages d'IP de l'API de Braze, reportez-vous à la fois à la [liste des IP publiques de Fastly](https://api.fastly.com/public-ip-list) et à [celle de Cloudflare](https://api.cloudflare.com/client/v4/ips). Notez que ces adresses IP peuvent changer.

