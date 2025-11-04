---
nav_title: Selecciones
article_title: Selecciones
page_order: 5
description: "Este artículo de referencia explica cómo crear y utilizar selecciones con tus catálogos para referenciar datos en tus campañas Braze."
---

# Selecciones

> Las selecciones son grupos de datos que pueden utilizarse para personalizar un mensaje para cada usuario de tu campaña. Cuando utilizas una selección, básicamente estás configurando filtros personalizados basados en columnas específicas de tu catálogo. Esto podría incluir filtros por marca, tamaño, ubicación, fecha de adición, etc. Te da el control sobre lo que muestras a los usuarios permitiéndote definir criterios que los elementos deben cumplir primero.<br><br>Esta página explica cómo crear y utilizar selecciones con tus catálogos.

Después de crear un [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/), puedes seguir haciendo referencia a los datos de tu catálogo incorporando selecciones en tus campañas o recomendaciones Braze.

La sección Selecciones de un catálogo de ejemplo.]({% image_buster /assets/img_archive/catalog_selections1.png %})

## Lo que debes saber

- Puedes crear hasta 30 selecciones por catálogo.
- Puedes añadir hasta 10 filtros por selección.
- Las selecciones son estupendas para refinar las recomendaciones a partir de los datos del catálogo de Braze. Si buscas inspiración, echa un vistazo a [las recomendaciones de Acerca del artículo]({{site.baseurl}}/user_guide/brazeai/recommendations/) para ver ejemplos de casos de uso.

## Crear una selección

Para crear una selección, haz lo siguiente

1. Ve a **Catálogos** y selecciona tu catálogo de la lista.
2. Selecciona la pestaña **Selección** y haz clic en **Crear selección**.
3. Dale a tu selección un nombre y una descripción opcional.
4. En **Campo de filtrado**, selecciona la columna del catálogo por la que quieres filtrar. Los campos de cadena con más de 1.000 caracteres no se pueden seleccionar para filtrar.
5. Termina de definir los criterios para filtrar seleccionando el operador correspondiente (por ejemplo, "es igual" o "no es igual") y el atributo.
6. En la sección **Tipo de ordenación**, determina cómo se ordenan los resultados. Por defecto, los resultados no se muestran en un orden determinado. Para especificar la ordenación por un campo concreto, desactiva **Ordenar aleatoriamente** y especifica el **Campo de Ordenación** y el **Orden de Ordenación** (ascendente o descendente).
7. En la sección **Límite de** resultados, introduce los resultados (hasta 50).
8. Selecciona **Crear selección**.

### Prueba y vista previa

Después de crear una selección, puedes utilizar la sección **Vista previa para el usuario** para ver lo que devolvería una selección para un usuario aleatorio o para un usuario concreto. Para las selecciones que utilizan personalización, sólo puedes ver la vista previa después de seleccionar un usuario.

### Liquid en los resultados de la selección

El uso de cualquier Liquid en los catálogos, como atributos personalizados y eventos personalizados, puede hacer que se devuelvan resultados diferentes para cada usuario de tu selección. 

{% alert note %}
Contenido conectado Liquid no se admite en esta configuración de filtrar.
{% endalert %}

\![Filtrar la configuración para la selección del catálogo cuando el atributo está configurado como un atributo personalizado de Liquid.]({% image_buster /assets/img_archive/catalog_selections7.png %})

## Utilizar selecciones en mensajería

Tras crear tu selección, personaliza tus mensajes con Liquid para insertar los elementos filtrados de ese catálogo. Puedes hacer que Braze genere el Liquid por ti desde la ventana de personalización que se encuentra en los creadores de mensajes:

1. En cualquier creador de mensajes que admita la personalización, selecciona <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Añadir personalización"></i> para abrir la ventana de personalización.
2. En **Tipo de personalización**, selecciona **Elementos de catálogo**.
3. Selecciona el nombre de tu catálogo.
4. En **Método de selección de elementos**, selecciona **Utilizar una selección**.
4. Selecciona tu selección de la lista.
5. En **Información a mostrar**, selecciona qué campos del catálogo deben incluirse para cada artículo.
6. Selecciona el icono **Copiar** y pega el Liquid donde sea necesario en tu mensaje.

El modal Añadir personalización con las siguientes selecciones: "Elementos del catálogo" para "Tipo de personalización", "Juegos" para "Nombre del catálogo", "Selecciones" para "Tipo de selección", "game_selection" para "Selección", y "título" y "description_en" para "Información a mostrar".]({% image_buster /assets/img_archive/catalog_selections6.png %}){: style="max-width:70%;"}

## Casos de uso

Supongamos que tienes un servicio de entrega de comidas y quieres enviar un mensaje personalizado a tus usuarios que tienen preferencias de comida específicas basadas en la categoría de comida que han visto más recientemente. 

Utilizando un catálogo con la información de tu servicio de entrega de comidas para el nombre de la comida, el precio, la imagen y la categoría de la comida, puedes crear una selección para recomendar tres comidas basándote en la categoría que el usuario haya visto más recientemente.

\![Ejemplo de selección para un servicio de entrega de comida con dos filtros: uno que identifica un tipo de producto como comida y otro que identifica la categoría como la más vista recientemente. La selección se establece para aleatorizar el orden en que se devuelven los tres resultados.]({% image_buster /assets/img_archive/catalog_selections2.png %}){: style="max-width:90%;"}

Para utilizar este catálogo y esta selección en una campaña, utiliza el modal **Añadir personalización** en la sección de composición de mensajes de la creación de una campaña. En este ejemplo, hemos seleccionado el catálogo con la información de tu servicio de entrega de comidas, y la selección de recomendaciones de comidas basada en la categoría vista más recientemente. Esto nos permite mostrar el nombre de la comida y el precio. Para construir aún más tu mensaje, puedes utilizar la selección para añadir también una imagen de la primera comida recomendada.

\![Una tarjeta de contenido con el encabezamiento "¡Te ENCANTARÁN estas comidas tan valoradas!" con la selección "recommendations_be_recent_category" en la sección de composición del mensaje.]({% image_buster /assets/img_archive/catalog_selections3.png %}){: style="max-width:90%;"}

Por ejemplo, supongamos que tienes un usuario cuya categoría vista más recientemente es "Pollo". Utilizando la personalización establecida y una campaña de tarjeta de contenido, puedes enviar tres recomendaciones de comidas que incluyan pollo para este usuario.

\![Una tarjeta de contenido con una imagen de pollo al limón a la parrilla y una lista de tres recomendaciones de comidas que incluyen pollo, basadas en la categoría que el usuario haya visto más recientemente.]({% image_buster /assets/img_archive/catalog_selections4.png %}){: style="max-width:90%;"}

Utilizando la misma personalización, también puedes enviar tres recomendaciones de comidas para un usuario cuya categoría vista más recientemente sea "Carne de vaca".

\![Una tarjeta de contenido con una imagen de stroganoff de ternera y una lista de dos recomendaciones de comidas que incluyen ternera basadas en la categoría que el usuario ha visto más recientemente.]({% image_buster /assets/img_archive/catalog_selections5.png %}){: style="max-width:90%;"}


