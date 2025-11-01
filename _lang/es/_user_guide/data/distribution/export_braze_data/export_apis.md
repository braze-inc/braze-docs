---
nav_title: API de exportación
article_title: API de exportación
page_order: 8
page_type: reference
description: "Este artículo de referencia describe por qué podrías exportar mediante programación un archivo JSON de datos del panel, en lugar de exportar un CSV directamente desde el panel."
platform: API

---

# API de exportación

> Esta página cubre las API de exportación de Braze, que te permiten exportar mediante programación un archivo JSON de datos del panel. Consulta [Puntos finales de exportación]({{site.baseurl}}/api/endpoints/export/) para ver una lista de los datos a los que puedes acceder, incluidas las instrucciones y el código de muestra para la exportación.

## Cuándo utilizar API de exportación en lugar de descargas CVS

Hay algunas razones por las que preferirías este método a exportar un CSV directamente desde el panel:

 - Tu archivo es muy grande. Desde nuestro panel, puedes exportar un CSV con un máximo de 500.000 filas. Si vas a exportar datos de un segmento con más de 500.000 usuarios, tendrás que utilizar nuestra API de exportación, que no tiene límite en cuanto a la cantidad que puedes exportar.
 -  Quieres interactuar con los datos mediante programación.

{% alert tip %}
Para obtener ayuda con las exportaciones CSV y API, consulta [Solución de problemas de exportación]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %}

