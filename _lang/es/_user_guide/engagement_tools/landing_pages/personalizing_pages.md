---
nav_title: Personalización de las páginas de destino
article_title: Personalización de las páginas de destino
description: "Este artículo explica cómo personalizar las páginas de destino Braze con el editor de arrastrar y soltar."
page_order: 4
---

# Personalización de las páginas de destino

> Utiliza la personalización Liquid en las páginas de destino para adaptar dinámicamente el contenido con los datos del perfil de usuario. Por ejemplo, puedes personalizar los titulares en función de distintos atributos de los usuarios sin tener que gestionar varias páginas de destino estáticas.

{% alert important %}
La personalización Liquid para páginas de destino sólo está disponible en el nivel Pro de páginas de destino. Actualmente, el [contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) y los [códigos promocionales]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes) no son compatibles con la personalización de Liquid en las páginas de destino.
{% endalert %}

## Introducir Liquid

En el editor de arrastrar y soltar, puedes insertar la personalización de Liquid tanto en el editor como en la configuración de la página o del bloque en el panel derecho. Para obtener instrucciones sobre la implantación de Liquid, consulta nuestra [documentación]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid-1) dedicada [a Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid-1).

\![Editor de páginas de destino con personalización Liquid añadida.]({% image_buster /assets/img/landing_pages/lp_liquid_.png %})

## Vista previa y pruebas

Al previsualizar una página de destino en el editor, puedes ver la página como un usuario aleatorio, un usuario existente o un usuario personalizado.

Sin embargo, al previsualizar la página **de** destino desde la tabla de datos o la página de **detalles de la página de destino**, sólo podrás verla como un usuario cualquiera.

## Consideraciones sobre la personalización

Para mantener un rendimiento óptimo con las páginas de destino personalizadas, toma nota de los siguientes límites de tamaño:

- **Guardar una página de destino:** Si el tamaño supera los 500 KB, es posible que recibas un mensaje de advertencia indicando que la página ha superado nuestros límites de tamaño, lo que puede impedir su publicación.
- **Renderizado con personalización Liquid:** El tamaño total no debe superar 1 MB. De lo contrario, la página puede ser despublicada automáticamente por Braze.

### Evita despublicar páginas de destino

Si tu página supera estos límites de tamaño, recibirás un correo electrónico en el que se te informará de que puede dejar de publicarse si sigue superando el límite. Cuando se alcance el umbral, la página se despublicará automáticamente y recibirás una notificación.

Para evitar que tu página supere los límites de tamaño o experimente tiempos de carga lentos, asegúrate de utilizar la personalización Liquid que:

- No realiza bucles continuos ni hace referencia a grandes conjuntos de datos.
- No depende de una amplia lógica condicional o matemática dentro del bloque Liquid.

## Páginas alternativas

Si tus usuarios intentan acceder a una página que ha sido despublicada, verán un mensaje indicando que la página no puede cargarse actualmente. Las razones por las que una página no se ha publicado incluyen:

- Liquid complejo o roto, que puede provocar largos tiempos de renderizado
- Problemas de red de los usuarios
- Superar los límites de tamaño máximo de la página de destino
