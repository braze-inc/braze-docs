Cuando [creas ubicaciones en tu aplicación o sitio web]({{site.baseurl}}/developer_guide/banners/placements/#requestBannersRefresh), tu aplicación envía una solicitud a Braze para obtener mensajes de Banner para cada ubicación.  

- Puedes solicitar hasta **10 colocaciones por sesión de usuario**.  
- Para cada colocación, Braze devuelve el **Banner de mayor prioridad** que el usuario es elegible para recibir.  
- Si se solicitan más de 10 colocaciones en una sesión, sólo se devuelven las 10 primeras; el resto se descartan.  

Por ejemplo, una aplicación puede solicitar tres ubicaciones durante una sola sesión: `homepage_promo`, `cart_abandonment`, y `seasonal_offer`. Cada petición devuelve el Banner más relevante para esa colocación.
