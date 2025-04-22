---
nav_title: Obtención de datos de perfil de usuario
article_title: Obtención de datos de perfil de usuario en llamadas de contenido conectado
page_order: 3
description: "En este artículo se explica cómo incluir perfiles de usuario en las llamadas a Connected Content, así como las mejores prácticas en relación con las plantillas Liquid."
toc_headers: h2
---

# Obtención de datos del perfil del usuario

>  

## 

Si una respuesta de contenido conectado contiene campos de perfil de usuario (dentro de una etiqueta de personalización de Liquid), estos valores deben definirse antes en el mensaje con Liquid, antes de la llamada de contenido conectado para que el passback de Liquid se represente correctamente. Del mismo modo, la bandera `:rerender` debe incluirse en la solicitud. Tenga en cuenta que el indicador `:rerender` sólo tiene un nivel de profundidad, lo que significa que no se aplicará a ninguna etiqueta de contenido conectado anidada.

## 

Para la personalización, Braze extrae los campos de perfil de usuario antes de pasar ese campo a Liquid, de modo que si la respuesta de Connected Content tiene campos de perfil de usuario, debe definirse de antemano. 

Por ejemplo, si esta fuera la llamada de Contenido Conectado:
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}

  

 Esto se debe a que Braze necesita saber qué campos recuperar del usuario antes de realizar la llamada a Contenido Conectado.

 El preprocesador Liquid sabrá tomar el atributo "idioma" del usuario para tenerlo listo para la plantilla de la respuesta.


```liquid
"Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}


 Si la propia respuesta de contenido conectado tiene más etiquetas de contenido conectado o cualquier etiqueta de catálogo, Braze no volverá a renderizar esas etiquetas adicionales.


## Buenas prácticas

### Utiliza `json_escape` con etiquetas de Liquid que podrían romper el formato JSON

Cuando utilices `:rerender`, añade el filtro `json_escape` a cualquier etiqueta de Liquid que pudiera romper el formato JSON. Si tus etiquetas de Liquid contienen caracteres que rompen el formato JSON, toda la respuesta de Contenido conectado se interpretará como texto y se incluirá en la plantilla del mensaje, y no se guardará ninguna de las variables.

Por ejemplo, si la propiedad del evento `message` del ejemplo siguiente contiene caracteres que podrían romper el formato JSON, añade el filtro `json_escape` como en este ejemplo:

{% raw %}
```liquid
[{
"message":"{{event_properties.${message} | json_escape}}"
}]
```
{% endraw %}