---
nav_title: API y puntos finales SDK
article_title: API y puntos finales SDK
page_order: 1
page_type: reference
description: "Este artículo de referencia enumera las URL del panel, los puntos finales API y los puntos finales SDK para las instancias de Braze disponibles."

---

# API y puntos finales SDK

> Tu instancia de Braze determina la URL necesaria para iniciar sesión en Braze, acceder a la API e integrar tu SDK. Obtén más información sobre el SDK de Braze en nuestro curso de Braze Learning, [Braze 101](https://learning.braze.com/braze-101).

Braze gestiona varias instancias diferentes para nuestro panel, SDK y puntos finales REST, que llamamos "clusters". Tu administrador de incorporación a Braze te dirá en qué grupo te encuentras.

Si te registras en [dashboard.braze.com](https://dashboard.braze.com) te enviará automáticamente a la dirección correcta del clúster.

{% multi_lang_include data_centers.md datacenters='instances' %}

{% alert important %}
Cuando integres tu SDK, utiliza el punto final SDK. Cuando realices llamadas a nuestra API REST, utiliza el punto final REST.
{% endalert %}

Para más detalles sobre cómo acceder a la API, consulta nuestro [artículo sobre el resumen de la API]({{site.baseurl}}/api/basics/). 
