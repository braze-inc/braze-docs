---
nav_title: Problemas de conectividad de la red API
article_title: Problemas de conectividad de la red API
page_order: 4
description: "Este artículo de referencia aborda los problemas de conectividad de la API y cómo solucionarlos."
page_type: reference

---

# Problemas de conectividad de la red API

> Este artículo de referencia aborda los problemas de conectividad de la API y cómo solucionarlos.

Los puntos finales de la API de Braze utilizan una CDN que dirige el tráfico al POP más cercano basándose en la información DNS.  Si tienes problemas para conectarte o notas que te conectas a un POP que no es eficiente, asegúrate de utilizar los servidores DNS de tu proveedor o servidores DNS que estén configurados en el mismo centro de datos que tu servidor y que tengan asociada la metainformación adecuada sobre la ubicación de la IP.

Observamos que algunos cortafuegos intentan modificar o proteger el tráfico HTTPS/TLS, lo que interfiere en las conexiones a los puntos finales de la API de Braze. Si tus servidores están detrás de algún tipo de cortafuegos físico, desactiva cualquier aceleración o modificación HTTPS/TLS que esté realizando el cortafuegos o el router. Además, puedes permitir el tráfico saliente a nuestros proveedores de CDN (Fastly.com) para ver si eso resuelve el problema.

Ocasionalmente, las configuraciones de iptables que filtran los paquetes de SYN/ACK/RST también pueden causar problemas, así que si utilizas iptables en tu host también podrías permitir el tráfico saliente a nuestros proveedores de CDN (Fastly.com) para ver si eso resuelve el problema.

Si sigues teniendo problemas de red al conectarte a los puntos finales de la API de Braze, proporciona una [prueba MTR][1] y los resultados de [Fastly Debug][2] mientras experimentas el problema y envíalos con tu solicitud de asistencia. Ten en cuenta que los resultados de la prueba deben obtenerse de un servidor que tenga problemas para conectarse a los puntos finales de la API de Braze, no de una máquina de desarrollo. Una captura de red (archivo tcpdump o .pcap) también será útil si se puede obtener.

Para más información sobre MTR, consulta estos recursos en función de tu sistema operativo:

- [GNU/Linux][4]
- [macOS][5]

## Permiso de los rangos de IP para permitir los puntos finales de la API de Braze

Para permitir que los puntos finales de la API de Braze atraviesen tu cortafuegos, nuestra CDN proporciona acceso a la lista de rangos de IP asignados a través de un volcado de JSON. Para obtener una lista de los rangos de IP de la API de Braze, consulta [la lista de IP públicas de Fastly][3] y [la lista de IP públicas de Cloudflare][6]. Ten en cuenta que estas IP pueden cambiar.

[1]: https://www.privateinternetaccess.com/helpdesk/kb/articles/what-is-an-mtr-test-and-how-do-i-run-one-2
[2]: http://www.fastly-debug.com/
[3]: https://api.fastly.com/public-ip-list
[4]: https://www.digitalocean.com/community/tutorials/how-to-use-traceroute-and-mtr-to-diagnose-network-issues
[5]: https://formulae.brew.sh/formula/mtr
[6]: https://api.cloudflare.com/client/v4/ips
