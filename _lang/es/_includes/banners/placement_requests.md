Cuando [creas ubicaciones en tu aplicación o sitio web]({{site.baseurl}}/developer_guide/banners/placements/#requestBannersRefresh), tu aplicación envía una solicitud a Braze para obtener mensajes de banner para cada ubicación.  

- Puedes solicitar hasta **10 ubicaciones por cada solicitud de actualización**.  
- Para cada ubicación, Braze devuelve el **banner con mayor prioridad** para el usuario que es elegible para recibirlo.  
- Si se solicitan más de 10 ubicaciones en una actualización, solo se devuelven las primeras 10; el resto se descartan.  

Por ejemplo, una aplicación podría solicitar tres ubicaciones en una solicitud de actualización: `homepage_promo`, y`cart_abandonment` `seasonal_offer`. Cada solicitud devuelve el banner más relevante para esa ubicación.

#### Límite de velocidad para las solicitudes de actualización

Si utilizas versiones anteriores del SDK (anteriores a SWIFT 13.1.0, Android 38.0.0, Web 6.1.0, React Native 17.0.0 y Flutter 15.0.0), solo se permite una solicitud de actualización por sesión de usuario.

Si utilizas versiones mínimas más recientes del SDK (SWIFT 13.1.0+, Android 38.0.0+, Web 6.1.0+, React Native 17.0.0+ y Flutter 15.0.0+), las solicitudes de actualización se controlan mediante un algoritmo de contenedor de tokens para evitar un sondeo excesivo:

- Cada sesión de usuario comienza con cinco tokens de actualización.
- Los tokens se recargan a una tasa de un token cada 180 segundos (3 minutos).

Cada llamada a`requestBannersRefresh`  consume un token. Si intentas actualizar cuando no hay tokens disponibles, el SDK no realiza la solicitud y registra un error hasta que se repone un token. Esto es importante para las actualizaciones a mitad de sesión y las actualizaciones que se desencadenan por eventos. Para implementar actualizaciones dinámicas (por ejemplo, después de que un usuario complete una acción en la misma página), llama al método de actualización después de que se registre el evento personalizado, pero ten en cuenta el retraso necesario para que Braze ingiera y procese el evento antes de que el usuario reúna los requisitos para una campaña de Banner diferente.
