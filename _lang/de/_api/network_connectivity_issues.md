---
nav_title: Probleme mit der API-Netzwerkkonnektivität
article_title: Probleme mit der API-Netzwerkkonnektivität
page_order: 4
description: "Dieser Referenzartikel befasst sich mit Problemen der API-Konnektivität und deren Behebung."
page_type: reference

---

# Probleme mit der API-Netzwerkkonnektivität

> Dieser Referenzartikel befasst sich mit Problemen der API-Konnektivität und deren Behebung.

Braze API-Endpunkte verwenden ein CDN, das den Datenverkehr auf der Grundlage von DNS-Informationen an den nächstgelegenen POP weiterleitet.  Wenn Sie Probleme mit der Verbindung haben oder feststellen, dass Sie eine Verbindung zu einem POP herstellen, der nicht effizient ist, stellen Sie sicher, dass Sie die DNS-Server Ihres Providers oder DNS-Server verwenden, die im selben Rechenzentrum wie Ihr Server eingerichtet sind und mit den richtigen IP-Standort-Metainformationen versehen sind.

Wir haben festgestellt, dass einige Firewalls versuchen, den HTTPS/TLS-Verkehr zu modifizieren oder zu sichern, was die Verbindungen zu den API-Endpunkten von Braze stört. Wenn sich Ihre Server hinter einer physischen Firewall befinden, deaktivieren Sie jegliche HTTPS/TLS-Beschleunigung oder Modifikationen, die die Firewall oder der Router vornimmt. Zusätzlich können Sie den ausgehenden Datenverkehr zu unseren CDN-Anbietern (Fastly.com) zulassen, um zu sehen, ob das Problem dadurch behoben wird.

Gelegentlich können auch iptables-Setups, die auf SYN/ACK/RST Pakete filtern, Probleme verursachen. Wenn Sie also iptables auf Ihrem Host verwenden, könnten Sie auch den ausgehenden Datenverkehr zu unseren CDN-Anbietern (Fastly.com) zulassen, um zu sehen, ob das Problem dadurch gelöst wird.

Wenn Sie immer noch Netzwerkprobleme mit der Verbindung zu Braze-API-Endpunkten haben, stellen Sie einen [MTR-Test][1] und die Ergebnisse von [Fastly Debug][2] zur Verfügung, während das Problem auftritt, und reichen Sie diese zusammen mit Ihrer Supportanfrage ein. Beachten Sie, dass die Testergebnisse von einem Server stammen müssen, der Probleme mit der Verbindung zu Braze-API-Endpunkten hat, und nicht von einem Entwicklungsrechner. Eine Netzwerkaufzeichnung (tcpdump oder .pcap-Datei) ist ebenfalls hilfreich, wenn Sie sie erhalten können.

Weitere Informationen über MTR finden Sie in den folgenden Ressourcen für Ihr Betriebssystem:

- [GNU/Linux][4]
- [macOS][5]

## Auflistung der IP-Bereiche der Braze API-Endpunkte zulassen

Um Braze-API-Endpunkte durch Ihre Firewall zuzulassen, bietet unser CDN Zugriff auf die Liste der zugewiesenen IP-Bereiche über einen JSON-Dump. Eine Liste der IP-Bereiche der Braze API finden Sie in der [öffentlichen IP-Liste von Fastly][3] und der [öffentlichen IP-Liste von Cloudflare][6]. Beachten Sie, dass sich diese IPs ändern können.

[1]: https://www.privateinternetaccess.com/helpdesk/kb/articles/what-is-an-mtr-test-and-how-do-i-run-one-2
[2]: http://www.fastly-debug.com/
[3]: https://api.fastly.com/public-ip-list
[4]: https://www.digitalocean.com/community/tutorials/how-to-use-traceroute-and-mtr-to-diagnose-network-issues
[5]: https://formulae.brew.sh/formula/mtr
[6]: https://api.cloudflare.com/client/v4/ips
