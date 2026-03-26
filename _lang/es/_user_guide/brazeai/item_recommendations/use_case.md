---
nav_title: Casos de uso
article_title: "Casos de uso: descubrimiento de contenido tras la visualización"
description: "Este ejemplo muestra cómo una marca ficticia utiliza las recomendaciones de artículos de Braze AI para entregar contenido personalizado y sugerencias de productos en momentos clave para los clientes."
page_type: tutorial
---

# Casos de uso: Impulsa el descubrimiento de contenido después de verlo

> Este ejemplo muestra cómo una marca ficticia utiliza las recomendaciones de artículos de Braze AI para entregar contenido personalizado y sugerencias de productos en momentos clave para los clientes. Descubre cómo la lógica de recomendación puede mejorar la interacción, aumentar las conversiones y reducir el esfuerzo manual.

Supongamos que Camila es administradora de CRM en MovieCanon, una plataforma de streaming que ofrece películas y series seleccionadas. 

El objetivo de Camila es mantener la interacción de los espectadores después de que terminen de ver algo. Históricamente, los mensajes «También te puede interesar» de MovieCanon se basaban en una amplia coincidencia de géneros y se enviaban en momentos arbitrarios, a menudo horas o días después de una sesión. La interacción era baja, y su equipo sabía que podía hacerlo mejor.

Mediante [las recomendaciones de artículos basadas en inteligencia artificial]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/), Camila configura un sistema que recomienda automáticamente nuevos títulos en función del historial de visualización de cada espectador, que se entregan inmediatamente después de que el usuario termine de ver una película o un episodio. Es una forma más inteligente y de personalización de ayudar a los usuarios a descubrir contenido que realmente querrán ver a continuación y mantenerlos en interacción con la plataforma.

![Mensaje dentro de la aplicación que dice: «Lo siguiente, solo para ti». Porque has visto «Nomads of the Sun», con una imagen, el nombre del título, una descripción y una llamada a la acción para «Ver ahora» o «Saltar» a la siguiente recomendación.]({% image_buster /assets/img/ai_use_cases/recommendation_rendered.png %})

Este tutorial explica cómo Camila:

- Mensaje personalizado que se activa cuando el usuario termina de ver algo.
- Recomendaciones adaptadas a las preferencias del espectador, extraídas automáticamente del catálogo de MovieCanon e insertadas en el mensaje. 

## Paso 1: Crear un modelo de predicción de abandono

Camila comienza creando una recomendación que mostrará títulos relevantes cada vez que un usuario termine de ver algo. Quiere que sea dinámico, para que los usuarios reciban diferentes sugerencias basadas en lo que han visto recientemente.

1. En el panel de Braze, Camila accede a **«Recomendaciones de artículos basadas en IA**».
2. Crea una nueva recomendación y la titula «Sugerencias tras el visionado».
3. Para el tipo de recomendación, ella elige **«Personalizada por IA»**, de modo que cada usuario ve recomendaciones personalizadas basadas en comportamientos anteriores.
4. Selecciona **No recomendar elementos con los que los usuarios hayan interactuado anteriormente** para que no reciban recomendaciones de algo que ya hayan visto. 
5. Ella selecciona el catálogo que contiene la biblioteca de contenidos actual de MovieCanon. Camila no añade una selección de catálogo, ya que quiere que todos los artículos del catálogo sean artículos elegibles para recomendación.
6. Camila vincula la recomendación al evento`Watched Content`personalizado, que realiza un seguimiento de las visualizaciones completadas, y establece el **nombre de la propiedad** como el título del contenido.
7. Ella crea la recomendación.

## Paso 2: Configurar un mensaje dentro de la aplicación

Una vez finalizado el entrenamiento de la recomendación, Camila crea un flujo de mensajería que llega al usuario en el momento adecuado: inmediatamente después de que termines un título. El mensaje incluye una lista de tres sugerencias de personalización extraídas directamente del catálogo.

1. Camila crea una campaña de mensajes dentro de la aplicación utilizando el editor de arrastrar y soltar.
2. Ella configura el activador para tu evento personalizado: `Watched Content`.
3. Diseña un mensaje dentro de la aplicación de varias páginas con imágenes de título, nombres y una llamada a la acción «Ver ahora».

![Abre el modal «Añadir personalización» en el editor de Braze, con «Recomendación de artículos» seleccionado como tipo de personalización.]({% image_buster /assets/img/ai_use_cases/recommendation_add_personalization.png %})

{: start="4"}

4. En el cuerpo del mensaje, Camila utiliza el [modal Añadir personalización]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#inserting-pre-formatted-variables) para añadir variables como el nombre, la descripción y la miniatura del título recomendado utilizando Liquid, que rellena dinámicamente el contenido del catálogo. Ella crea una plantilla en un atributo personalizado para`Last Watched Movie`que los usuarios sepan que esta recomendación se basa en su historial de visualizaciones. 

![Editor de mensajes dentro de la aplicación con Liquid sin procesar para crear plantillas en campos específicos a partir de elementos del catálogo de la recomendación.]({% image_buster /assets/img/ai_use_cases/recommendation_liquid.png %})

{% details Show Liquid used in image %}

{% raw %}

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].name }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].description }}
```

```liquid
{% assign items = {{product_recommendation.${Post-viewing suggestions}}} %}{{ items[0].thumbnail }}
```

{% endraw %}

{% enddetails %}

{: start="5"}

5. A continuación, Camila duplica su página e incrementa la matriz Liquid{% raw %}  (`{{ items[0]}}` to `{{items[1]}}`){% endraw %}  en cada variable para crear una plantilla en el siguiente elemento de la lista de recomendaciones.

## Paso 3: Medir y optimizar

Una vez lanzada la campaña, Camila supervisa las tasas de apertura, los CTR y el comportamiento de visualización posterior. Compara el rendimiento con campañas de recomendación estáticas anteriores y observa una mayor interacción y más sesiones de contenido por usuario.

También tiene previsto realizar pruebas A/B:

- Momento (inmediato frente a 10 minutos después de ver el reloj)
- Diseño del contenido (carrusel frente a lista)
- Variaciones de CTA («Ver ahora» frente a «Añadir a la cola»)

Al combinar los mensajes basados en eventos con las recomendaciones de artículos basadas en inteligencia artificial, Camila convierte el descubrimiento de contenido en una experiencia automática y de personalización. MovieCanon mantiene la interacción de los usuarios sin conjeturas, entregando contenido relevante en el momento adecuado para impulsar la profundidad de la sesión y reducir la tasa de abandonos.





