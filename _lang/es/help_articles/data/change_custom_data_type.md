---
nav_title: Cambiar el tipo de datos de atributos o eventos personalizados
article_title: Cambiar el tipo de datos del atributo personalizado o del evento
page_order: 1

page_type: solution
description: "Este artículo de ayuda te explica cómo cambiar el tipo de datos de un atributo personalizado o de un evento personalizado, y las implicaciones de hacerlo."
---

# Cambiar el tipo de datos de atributos o eventos personalizados

Para cambiar el tipo de datos de un atributo o evento personalizado, desde el panel de Braze, ve a **Configuración de datos** y selecciona **Atributos personalizados** o **Eventos personalizados**.

![Pestaña Atributos personalizados para editar atributos o tipos de datos]({% image_buster /assets/img/change_custom_attribute.png %})

Si debes cambiar el tipo de datos de un atributo personalizado o de un evento (por ejemplo, cambiar `time` por `string`), ten en cuenta lo siguiente:

- Los filtros relevantes en segmentos, campañas, Lienzos u otras ubicaciones que utilicen el atributo o evento modificado no se actualizan automáticamente. Antes de poder modificar los atributos, debes detener cualquier campaña o Lienzo que utilice los atributos en segmentos o filtros, y eliminar los atributos de los filtros que hagan referencia a ellos.
- Los datos de usuario no se actualizarán con carácter retroactivo. Si el atributo modificado estaba en un perfil de usuario antes del cambio de tipo de datos, ese valor seguirá siendo el tipo de datos antiguo. Eso puede hacer que los usuarios queden fuera de los segmentos que contienen el atributo modificado. El filtro buscará activamente el nuevo tipo de datos, pero si un perfil sigue teniendo el tipo de datos anterior, ese usuario quedará excluido del segmento. Tales usuarios deben actualizarse para que vuelvan a incluirse en los segmentos adecuados. Puedes hacerlo con el [punto final `users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).
- No se aceptarán nuevos datos si no son del nuevo tipo. Por ejemplo, no se aceptará una llamada de la API al punto final `users/track` que contenga el tipo de datos anterior para un atributo modificado. Debes llamar al nuevo tipo de datos.

{% alert important %}
La posibilidad de impedir que la detección automática actualice el tipo de datos de atributo personalizado está actualmente en acceso temprano. Ponte en contacto con tu administrador del éxito del cliente si estás interesado en participar en este acceso anticipado.
{% endalert %}

_Última actualización: 8 de febrero de 2024_

