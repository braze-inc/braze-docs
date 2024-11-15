---
nav_title: Braze Go
permalink: "/braze_go/"
hidden: true
noindex: true
hide_toc: true
---

# Braze Go

> Braze Go ofrece un acceso simplificado a la plataforma de interacción con los clientes Braze para ayudar a tus equipos de marketing a empezar en cualquier lugar e ir a todas partes. Diseñado para ser sencillo y eficaz, Braze Go está hecho a medida para determinados mercados emergentes.

{% alert important %}
Braze Go no está disponible en todos los mercados. Si te interesa saber más sobre Braze Go, ponte en contacto con tu director de cuentas.
{% endalert %}

Braze Go ofrece toda la misma funcionalidad que Braze, con los cambios centrados en las siguientes características: 

- Puedes tener hasta 30 campañas activas.
- Puedes tener hasta 20 Lienzos activos.
- El límite de velocidad total predeterminado de la API REST es de 50.000 por hora, por espacio de trabajo.
    - Si no utilizas Braze Go, obtén más información sobre [los límites de la API REST]({{site.baseurl}}/api/api_limits/#rate-limits-by-request-type).
- La retención de datos de campañas e interacciones en Canvas es de 2 meses sin restauración.
    - Si no utilizas Braze Go, obtén más información sobre [la disponibilidad de datos de interacción de mensajería]({{site.baseurl}}/messaging_interaction_data/).

{% alert note %}
Los datos de interacción de campañas y Lienzos son diferentes de los datos de Snowflake y no tienen ningún efecto.
{% endalert %}

- Los webhooks Braze to Braze no son compatibles.
- No se admiten filtros relacionados con las etiquetas, concretamente los siguientes filtros:
    - Campaña clicada o abierta o Canvas con etiqueta
    - Último mensaje recibido de la campaña o Canvas con etiqueta
    - Campaña recibida o Canvas con etiqueta
- Braze también puede aplicar una política de retención de datos para los eventos del perfil de usuario y los datos de compra que elimine los eventos, compras o ambos con más de 1 año de antigüedad que no se hayan vuelto a realizar en 1 año. Sin embargo, estos datos seguirían estando disponibles en Extensiones de segmento SQL durante 2 años.

Si se actualiza alguna de las funciones anteriores, se reflejará en este artículo y se anotará en nuestras [notas de la versión]({{site.baseurl}}/help/release_notes/#most-recent-braze-release-notes).