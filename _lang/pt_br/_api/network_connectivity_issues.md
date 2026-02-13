---
nav_title: Problemas de conectividade de rede da API
article_title: Problemas de conectividade de rede da API
page_order: 4
description: "Este artigo de referência aborda os problemas de conectividade da API e como solucioná-los."
page_type: reference

---

# Problemas de conectividade de rede da API

> Este artigo de referência aborda os problemas de conectividade da API e como solucioná-los.

Os pontos de extremidade da API do Braze usam uma CDN que roteia o tráfego para o POP mais próximo com base nas informações de DNS.  Se estiver tendo problemas de conexão ou perceber que está se conectando a um POP que não é eficiente, certifique-se de usar os servidores DNS do seu provedor ou servidores DNS que estejam configurados no mesmo data center que o seu servidor e que tenham meta-informações de local IP adequadas associadas a eles.

Percebemos que alguns firewalls tentam modificar ou proteger o tráfego HTTPS/TLS, o que interfere nas conexões com os endpoints da API do Braze. Se seus servidores estiverem atrás de qualquer tipo de firewall físico, desative qualquer aceleração ou modificação de HTTPS/TLS que o firewall ou roteador esteja realizando. Além disso, você pode permitir a lista de tráfego de saída para nossos provedores de CDN (Fastly.com) para ver se isso resolve o problema.

Ocasionalmente, as configurações do iptables que filtram os pacotes SYN/ACK/RST também podem causar problemas; portanto, se você estiver usando o iptables em seu host, também poderá colocar na lista de permissões o tráfego de saída para nossos provedores de CDN (Fastly.com) para ver se isso resolve o problema.

Se ainda estiver tendo problemas de rede com a conexão aos endpoints da Braze API, forneça um [teste MTR](https://www.privateinternetaccess.com/helpdesk/kb/articles/what-is-an-mtr-test-and-how-do-i-run-one-2) e os resultados do [Fastly Debug](http://www.fastly-debug.com/) enquanto estiver enfrentando um problema e envie-os com sua solicitação de suporte. Note que os resultados do teste devem ser obtidos de um servidor que esteja tendo problemas para se conectar aos endpoints da API do Braze, e não de uma máquina de desenvolvimento. Uma captura de rede (tcpdump ou arquivo .pcap) também será útil se puder ser obtida.

Para saber mais sobre o MTR, consulte estes recursos com base em seu sistema operacional:

- [GNU/Linux](https://www.digitalocean.com/community/tutorials/how-to-use-traceroute-and-mtr-to-diagnose-network-issues)
- [MacOS](https://formulae.brew.sh/formula/mtr)

## Permitir a listagem dos intervalos de IP dos pontos de extremidade da Braze API

Para permitir que os endpoints da API do Braze passem pelo seu firewall, nossa CDN fornece acesso à lista de intervalos de IP atribuídos por meio de um dump JSON. Para obter uma lista dos intervalos de IPs do Braze API, consulte [a lista de IPs públicos da Fastly](https://api.fastly.com/public-ip-list) e a [lista de IPs públicos da Cloudflare](https://api.cloudflare.com/client/v4/ips). Note que esses IPs podem mudar.

