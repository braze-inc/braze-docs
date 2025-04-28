---
nav_title: API y puntos finales SDK
article_title: API y puntos finales SDK
page_order: 1
page_type: reference
description: "Este artículo de referencia enumera las URL del panel, los puntos finales API y los puntos finales SDK para las instancias de Braze disponibles."

---

# API y puntos finales SDK

> Su instancia de Braze determina la URL necesaria para iniciar sesión en Braze, acceder a la API e integrar su SDK. Obtén más información sobre el SDK de Braze en nuestro curso de Braze Learning, [Braze 101][1].

Braze gestiona varias instancias diferentes para nuestro panel, SDK y puntos finales REST, que llamamos "clústeres". Tu administrador de incorporación a Braze te dirá en qué grupo te encuentras.

Si inicia sesión en [dashboard.braze.com](https://dashboard.braze.com) le enviará automáticamente a la dirección correcta del clúster.

|Instancia|URL|Punto final de REST|Punto final de SDK|
|---|---|---|
|US-01| `https://dashboard-01.braze.com` | `https://rest.iad-01.braze.com` | `sdk.iad-01.braze.com` |
|US-02| `https://dashboard-02.braze.com` | `https://rest.iad-02.braze.com` | `sdk.iad-02.braze.com` |
|US-03| `https://dashboard-03.braze.com` | `https://rest.iad-03.braze.com` | `sdk.iad-03.braze.com` |
|US-04| `https://dashboard-04.braze.com` | `https://rest.iad-04.braze.com` | `sdk.iad-04.braze.com` |
|US-05| `https://dashboard-05.braze.com` | `https://rest.iad-05.braze.com` | `sdk.iad-05.braze.com` |
|US-06| `https://dashboard-06.braze.com` | `https://rest.iad-06.braze.com` | `sdk.iad-06.braze.com` |
|US-07| `https://dashboard-07.braze.com` | `https://rest.iad-07.braze.com` | `sdk.iad-07.braze.com` |
|US-08| `https://dashboard-08.braze.com` | `https://rest.iad-08.braze.com` | `sdk.iad-08.braze.com` |
|EU-01| `https://dashboard-01.braze.eu` | `https://rest.fra-01.braze.eu` | `sdk.fra-01.braze.eu` |
|EU-02| `https://dashboard-02.braze.eu` | `https://rest.fra-02.braze.eu` | `sdk.fra-02.braze.eu` |
|AU-01| `https://dashboard.au-01.braze.com`| `https://rest.au-01.braze.com` | `sdk.au-01.braze.com` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

{% alert important %}
Cuando integres tu SDK, utiliza el punto final SDK. Cuando realices llamadas a nuestra API REST, utiliza el punto final REST.
{% endalert %}

Para más detalles sobre el acceso a la API, consulta el [artículo sobre el resumen de la API][2]. 


[1]: https://learning.braze.com/braze-101
[2]: {{site.baseurl}}/api/basics/