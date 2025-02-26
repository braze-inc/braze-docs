---
nav_title: Obtención de datos de perfil de usuario
article_title: Obtención de datos de perfil de usuario en llamadas de contenido conectado
page_order: 5
description: "En este artículo se explica cómo incluir perfiles de usuario en las llamadas a Connected Content, así como las mejores prácticas en relación con las plantillas Liquid."

---

# Obtención de datos del perfil del usuario

> Si una respuesta de contenido conectado contiene campos de perfil de usuario (dentro de una etiqueta de personalización de Liquid), estos valores deben definirse antes en el mensaje a través de Liquid, antes de la llamada de contenido conectado, a fin de representar correctamente el passback de Liquid. 

Del mismo modo, la bandera `:rerender` debe incluirse en la solicitud. Tenga en cuenta que el indicador `:rerender` sólo tiene un nivel de profundidad, lo que significa que no se aplicará a ninguna etiqueta de contenido conectado anidada.

Para la personalización, Braze extrae los campos de perfil de usuario antes de pasar ese campo a Liquid, de modo que si la respuesta de Connected Content tiene campos de perfil de usuario, debe definirse de antemano. 

Por ejemplo, si esta fuera la llamada de Contenido Conectado:
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}
Y la respuesta Contenido conectado es {% raw %}`Your language is ${language}`{% endraw %}, el contenido mostrado en este escenario será `Hi Jon, your language is`. El idioma en sí no tendrá plantilla. Esto se debe a que Braze necesita saber qué campos recuperar del usuario antes de realizar la llamada a Contenido Conectado.

Para renderizar correctamente el passback de Liquid, debe colocar la etiqueta {% raw %}`${language}`{%endraw%} en cualquier lugar de la solicitud, como se muestra en el siguiente fragmento de código. El preprocesador Liquid sabrá tomar el atributo "idioma" del usuario para tenerlo listo para la plantilla de la respuesta.
{%raw%}
```liquid
"Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}
{% alert important %}
Recuerde que la opción de bandera `:rerender` sólo tiene un nivel de profundidad. Si la propia respuesta de contenido conectado tiene más etiquetas de contenido conectado, Braze no volverá a renderizar esas etiquetas adicionales.
{% endalert %}
