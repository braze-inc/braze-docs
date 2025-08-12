---
nav_title: Superposición de la barra de desplazamiento
article_title: Superposición de la barra de desplazamiento
page_order: 0

page_type: solution
description: "Este artículo de ayuda explica a los usuarios de Mac cómo resolver el problema de las barras de desplazamiento que se superponen al contenido de los documentos de Braze."
---

# Superposición de la barra de desplazamiento

¿Utilizas un Mac y encuentras que tus barras de desplazamiento se superponen al contenido dentro de Braze Docs como en el siguiente ejemplo?

![Ejemplo de superposición de la barra de desplazamiento]({% image_buster /assets/img/scroll-overlap.png %})

Comprueba si tu barra de desplazamiento se superpone al siguiente bloque de código:

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.S3.integration.<integration-id>/event_type=<event-type>/date=<date>/<schema-id>/<zone>/dataexport.<cluster-identifier>.S3.integration.<integration-id>+<partition>+<offset>.avro
```

Si tu barra de desplazamiento se superpone al bloque de código, te sugerimos que cambies el ajuste **Mostrar barras de desplazamiento:** a **Siempre** en tu **Configuración general**. Esto ampliará las características de Docs (como los bloques de código) para mostrar siempre la barra de desplazamiento y evitar la ilegibilidad.

![Configuración general de MacOS]({% image_buster /assets/img/general-on-mac.png %})

Este es el aspecto que debería tener ahora tu barra de desplazamiento actualizada:

![Ejemplo de barra de desplazamiento fija sin superposición]({% image_buster /assets/img/scroll-bar-on.png %})

_Última actualización el 27 de marzo de 2019_

{% comment %}
Insértalo donde haya una sola línea de código larga que pueda causar problemas:
_¿No puedes ver el código debido a la barra de desplazamiento? Mira cómo solucionarlo [aquí]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/)._
{% endcomment %}

