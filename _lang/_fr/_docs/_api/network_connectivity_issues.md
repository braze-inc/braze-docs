---
nav_title: Problèmes de connectivité réseau API
article_title: Problèmes de connectivité réseau API
page_order: 4
description: "Cet article de référence traite des problèmes de connectivité API et comment les résoudre."
page_type: Référence
---

# Problèmes de connectivité API

> Cet article de référence traite des problèmes de connectivité API et comment les résoudre.

Les terminaux de l'API de Braze utilisent un CDN qui achemine le trafic vers le POP le plus proche en se basant sur les informations DNS.  Si vous rencontrez des problèmes de connexion ou de notification que vous vous connectez à un POP qui n'est pas efficace, assurez-vous d'utiliser les serveurs DNS ou les serveurs DNS de votre fournisseur qui sont configurés dans le même centre de données que votre serveur et qui ont les métadonnées de l'emplacement IP qui y sont associées.

Nous avons remarqué qu'une poignée de pare-feu tentent de modifier ou de sécuriser le trafic HTTPS/TLS qui interfère avec les connexions aux terminaux de l'API de Braze. Si vos serveurs sont derrière une sorte de pare-feu physique, veuillez désactiver toute accélération HTTPS/TLS ou toute modification que le ou les pare-feu et/ou routeurs effectuent.  De plus, vous pouvez mettre en liste blanche le trafic sortant vers nos fournisseurs de CDN (Fastly.com) pour voir si cela résout le problème.

Parfois, les configurations iptables qui filtrent sur les paquets SYN/ACK/RST peuvent également causer des problèmes. donc si vous utilisez iptables sur votre hôte, vous pouvez aussi ajouter une liste blanche au trafic sortant vers nos fournisseurs de CDN (Rapidement. om) pour voir si cela résout le problème.

Si vous rencontrez toujours des problèmes de réseau lors de la connexion au point de terminaison de l'API de Braze, veuillez fournir un [test MTR][1] et les résultats de [Débogage rapide][2] en cas de problème et soumettez cela avec votre demande d'assistance. Notez que les résultats de test doivent être obtenus à partir d'un serveur qui a des problèmes de connexion au point de terminaison de l'API de Braze, pas à partir d'une machine de développement.  Une capture réseau (fichier tcpdump ou .pcap) sera également utile si elle peut être obtenue.

Pour plus d'informations sur MTR, consultez ces ressources en fonction de votre système d'exploitation :

- [GNU/Linux][4]
- [macOS][5]

## Intervalle IP des points de terminaison API de Braze

Pour mettre en liste blanche le point de terminaison de l'API Braze à travers votre pare-feu, notre CDN fournit un accès à la liste des plages d'adresses IP assignées via un dépôt JSON. Vous pouvez accéder à la liste publique des plages d'IP Fastly [ici][3].


[1]: https://www.privateinternetaccess.com/helpdesk/kb/articles/what-is-an-mtr-test-and-how-do-i-run-one-2
[2]: http://www.fastly-debug.com/
[3]: https://api.fastly.com/public-ip-list
[4]: https://www.digitalocean.com/community/tutorials/how-to-use-traceroute-and-mtr-to-diagnose-network-issues
[5]: https://formulae.brew.sh/formula/mtr
