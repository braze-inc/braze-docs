Cuando [creas ubicaciones en tu aplicación o sitio web]({{site.baseurl}}/developer_guide/banners/placements/#requestBannersRefresh), tu aplicación envía una solicitud a Braze para obtener mensajes de Banner para cada ubicación.  

- Puedes solicitar hasta **10 colocaciones por solicitud de actualización**.  
- Para cada colocación, Braze devuelve el **Banner de mayor prioridad** que el usuario es elegible para recibir.  
- Si se solicitan más de 10 colocaciones en una actualización, sólo se devuelven las 10 primeras; el resto se descartan.  

Por ejemplo, una aplicación puede solicitar tres ubicaciones en una solicitud de actualización: `homepage_promo`, `cart_abandonment`, y `seasonal_offer`. Cada petición devuelve el Banner más relevante para esa colocación.

#### Limitación de velocidad para solicitudes de actualización

Si estás en versiones antiguas del SDK (anteriores a Swift 13.1.0, Android 38.0.0, Web 6.1.0, React Native 17.0.0 y Flutter 15.0.0), sólo se permite una solicitud de actualización por sesión de usuario.

Si utilizas versiones más recientes del SDK (Swift 13.1.0+, Android 38.0.0+, Web 6.1.0+, React Native 17.0.0+ y Flutter 15.0.0+), las solicitudes de actualización se controlan mediante un algoritmo de contenedor de tokens para evitar un sondeo excesivo:

- Cada sesión de usuario comienza con cinco tokens de actualización.
- Las fichas se rellenan a una tasa de una ficha cada 180 segundos (3 minutos).

Cada llamada a `requestBannersRefresh` consume un token. Si intentas una actualización cuando no hay tokens disponibles, el SDK no realiza la solicitud y registra un error hasta que se rellene un token. Esto es importante para las actualizaciones a mitad de sesión y desencadenadas por eventos. Para implementar actualizaciones dinámicas (por ejemplo, después de que un usuario complete una acción en la misma página), llama al método de actualización después de que se registre el evento personalizado, pero ten en cuenta el retraso necesario para que Braze ingiera y procese el evento antes de que el usuario se clasifique para una campaña de Banner diferente.
