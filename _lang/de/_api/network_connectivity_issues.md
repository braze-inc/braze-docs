---
nav_title: Probleme mit der API-Netzwerkkonnektivität
article_title: Probleme mit der API-Netzwerkkonnektivität
page_order: 4
description: "Dieser referenzierte Artikel befasst sich mit Problemen bei der API-Konnektivität und deren Fehlerbehebung."
page_type: reference

---

# Probleme mit der API-Netzwerkkonnektivität

> Dieser referenzierte Artikel befasst sich mit Problemen bei der API-Konnektivität und deren Fehlerbehebung.

Die API Endpunkte von Braze verwenden ein CDN, das den Datenverkehr auf der Grundlage von DNS-Informationen an den nächstgelegenen POP weiterleitet.  Wenn Sie Probleme mit der Verbindung haben oder feststellen, dass Sie sich mit einem POP verbinden, der nicht effizient ist, stellen Sie sicher, dass Sie die DNS-Server Ihres Providers oder DNS-Server verwenden, die im selben Rechenzentrum wie Ihr Server eingerichtet sind und mit den richtigen Metainformationen zum IP-Standort versehen sind.

Wir haben festgestellt, dass einige Firewalls versuchen, den HTTPS/TLS-Datenverkehr zu modifizieren oder zu sichern, wodurch Verbindungen zu Braze APIs Endpunkten gestört werden. Wenn sich Ihre Server hinter einer physischen Firewall befinden, deaktivieren Sie jegliche HTTPS/TLS-Beschleunigung oder Änderungen, die die Firewall oder der Router vornimmt. Zusätzlich können Sie den ausgehenden Datenverkehr zu unseren CDN-Anbietern (Fastly.com) zulassen, um zu sehen, ob das Problem dadurch behoben wird.

Gelegentlich können auch iptables-Setups, die nach SYN/ACK/RST-Paketen filtern, Probleme verursachen. Wenn Sie also iptables auf Ihrem Host verwenden, könnten Sie auch den ausgehenden Verkehr zu unseren CDN-Anbietern (Fastly.com) zulassen, um zu sehen, ob das Problem dadurch behoben wird.

Wenn Sie immer noch Netzwerkprobleme mit der Verbindung zu Braze API Endpunkten haben, stellen Sie einen [MTR-Test](https://www.privateinternetaccess.com/helpdesk/kb/articles/what-is-an-mtr-test-and-how-do-i-run-one-2) und die Ergebnisse von [Fastly Debug](http://www.fastly-debug.com/) zur Verfügung, während das Problem auftritt, und reichen Sie diese zusammen mit Ihrer Anfrage an den Support ein. Beachten Sie, dass die Testergebnisse von einem Server stammen müssen, der Probleme mit der Verbindung zu Braze APIs Endpunkten hat, und nicht von einem Entwickler:in. Eine Netzwerkaufzeichnung (tcpdump oder .pcap-Datei) ist ebenfalls hilfreich, wenn Sie sie erhalten können.

Weitere Informationen zu MTR finden Sie in den folgenden, auf Ihr Betriebssystem abgestimmten Ressourcen:

- [GNU/Linux](https://www.digitalocean.com/community/tutorials/how-to-use-traceroute-and-mtr-to-diagnose-network-issues)
- [macOS](https://formulae.brew.sh/formula/mtr)

## Auflistung der IP-Bereiche der Braze API Endpunkte zulassen

Um die Liste der Braze API Endpunkte durch Ihre Firewall hindurch zuzulassen, bietet unser CDN über einen JSON-Dump Zugriff auf die Liste der zugewiesenen IP-Bereiche. Eine Liste der IP-Bereiche der Braze APIs finden Sie sowohl in [der öffentlichen IP-Liste von Fastly](https://api.fastly.com/public-ip-list) als auch in der [öffentlichen IP-Liste von Cloudflare](https://api.cloudflare.com/client/v4/ips). Beachten Sie, dass sich diese IPs ändern können.

