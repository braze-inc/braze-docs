---
nav_title: Casos de uso
article_title: Caso de uso Impulsa la búsqueda de contenidos después de verlos
description: "Este ejemplo muestra cómo una marca ficticia utiliza las recomendaciones de artículos de la IA de Braze para entregar contenido personalizado y sugerencias de productos en los momentos clave del cliente."
page_type: tutorial
---

# Casos de uso: Impulsa el descubrimiento de contenidos después de verlos

> Este ejemplo muestra cómo una marca ficticia utiliza las recomendaciones de artículos de la IA de Braze para entregar contenido personalizado y sugerencias de productos en los momentos clave del cliente. Descubre cómo la lógica de recomendación puede mejorar la interacción, aumentar las conversiones y reducir el esfuerzo manual.

Digamos que Camila es administradora de CRM en MovieCanon, una plataforma de streaming que selecciona películas y series. 

El objetivo de Camila es mantener la interacción de los espectadores cuando terminan de ver algo. Históricamente, los mensajes "Puede que también te guste" de MovieCanon se basaban en una amplia coincidencia de géneros y se enviaban en momentos arbitrarios, a menudo horas o días después de una sesión. La interacción era escasa, y su equipo sabía que podían hacerlo mejor.

Utilizando [las Recomendaciones de elementos de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/creating_recommendations/ai/), Camila crea un sistema para recomendar automáticamente nuevos títulos basados en el historial de visionado de cada espectador, que se entregan inmediatamente después de que el usuario termine una película o un episodio. Es una forma más inteligente y personal de ayudar a los usuarios a descubrir contenidos que realmente querrán ver a continuación y mantener su interacción con la plataforma.

\![Mensaje dentro de la aplicación con la leyenda "A continuación, sólo para ti. Porque viste "Nómadas del Sol", con una imagen, un nombre de título, una descripción y un CTA para "Ver ahora" o "Saltar" a la siguiente recomendación.]({% image_buster /assets/img/ai_use_cases/recommendation_rendered.png %})

Este tutorial explica cómo funciona Camila:

- Un mensaje personalizado desencadenado cuando un usuario termina de ver algo
- Recomendaciones adaptadas a las preferencias del espectador, extraídas automáticamente del catálogo de MovieCanon e insertadas en el mensaje. 

## Paso 1: Crear un modelo de predicción del abandono de clientes

Camila empieza creando una recomendación que mostrará títulos relevantes cada vez que un usuario termine de ver algo. Quiere que sea dinámico, para que los usuarios reciban sugerencias diferentes en función de lo que hayan visto recientemente.

1. En el panel de Braze, Camila navega hasta **Recomendaciones de Artículos AI**.
2. Crea una nueva recomendación y nómbrala "Sugerencias posteriores a la visualización".
3. Para el tipo de recomendación elige **AI Personalizada**, para que cada usuario vea recomendaciones a medida basadas en comportamientos anteriores.
4. Selecciona **No recomendar elementos con los que los usuarios hayan interactuado** previamente para que los usuarios no reciban recomendaciones de algo que ya han visto. 
5. Selecciona el catálogo que contiene la biblioteca de contenidos actuales de MovieCanon. Camila no añade una selección de catálogo, ya que quiere que todos los artículos del catálogo sean elegibles para la recomendación.
6. Camila vincula la recomendación al evento personalizado `Watched Content`, que realiza un seguimiento de las visualizaciones completadas, y establece el **Nombre de la propiedad** en el título del contenido.
7. Ella crea la recomendación.

## Paso 2: Configurar un mensaje dentro de la aplicación

Una vez que la recomendación ha terminado de entrenarse, Camila construye un flujo de mensajería que llega al usuario en el momento adecuado: inmediatamente después de que termine un título. El mensaje incluye una lista de tres sugerencias personalizadas extraídas directamente del catálogo.

1. Camila crea una campaña de mensajería dentro de la aplicación utilizando el editor de arrastrar y soltar.
2. Configura el desencadenamiento a su evento personalizado: `Watched Content`.
3. Diseña un mensaje dentro de la aplicación de varias páginas con imágenes de títulos, nombres y una CTA de "Ver ahora".

\!["Añadir personalización" modal abierto en el editor de Braze, con "Recomendación de artículos" seleccionada como tipo de personalización.]({% image_buster /assets/img/ai_use_cases/recommendation_add_personalization.png %})

{: start="4"}

4. En el cuerpo del mensaje, Camila utiliza el [modal Añadir personalización]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#inserting-pre-formatted-variables) para añadir variables como el nombre, la descripción y la miniatura del título recomendado utilizando Liquid, que rellena dinámicamente el contenido del catálogo. Plantilla un atributo personalizado para `Last Watched Movie` para que los usuarios sepan que esta recomendación se basa en su historial de relojes. 

\![Editor de mensajes dentro de la aplicación con Liquid sin procesar para crear plantillas en campos específicos a partir de elementos del catálogo de la recomendación.]({% image_buster /assets/img/ai_use_cases/recommendation_liquid.png %})

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

5. A continuación, Camila duplica su página e incrementa la matriz Liquid {% raw %} (`{{ items[0]}}` a `{{items[1]}}`) {% endraw %} en cada variable de la plantilla en el siguiente elemento de la lista de recomendaciones.

## Paso 3: Medir y optimizar

Con la campaña en vivo, Camila supervisa las tasas abiertas, los CTR y el comportamiento de seguimiento. Compara el rendimiento con el de anteriores campañas de recomendación estáticas y observa una mayor interacción y más sesiones de contenido por usuario.

También tiene previsto hacer pruebas A/B:

- Tiempo (inmediato frente a 10 minutos después de la observación)
- Diseño del contenido (carrusel frente a lista)
- Variaciones de CTA ("Ver ahora" frente a "Añadir a la cola")

Al combinar la mensajería basada en eventos con las Recomendaciones de Artículos de IA, Camila convierte el descubrimiento de contenidos en una experiencia automática y personalizada. MovieCanon mantiene la interacción de los usuarios sin conjeturas, entregando contenido relevante en el momento justo para profundizar en la sesión y reducir el abandono.





