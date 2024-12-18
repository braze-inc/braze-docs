---
nav_title: Selecciones
article_title: Selecciones
page_order: 5
description: "Este artículo de referencia explica cómo crear y utilizar selecciones con sus catálogos para referenciar datos en sus campañas Braze."
---

# Selecciones

> Aprenda a crear y utilizar selecciones con sus catálogos.

Las selecciones son grupos de datos que pueden utilizarse para personalizar un mensaje para cada usuario de su campaña. Cuando utiliza una selección, básicamente está configurando filtros personalizados basados en columnas específicas de su catálogo. Puede incluir filtros por marca, tamaño, ubicación, fecha de adición, etc. Le da el control sobre lo que muestra a los usuarios al permitirle definir criterios que los artículos deben cumplir primero.

Después de crear un [catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalog/), puede seguir haciendo referencia a los datos de su catálogo incorporando selecciones en sus campañas o recomendaciones Braze.

![La sección Selecciones de un catálogo de ejemplo.][1]

## Lo que hay que saber

- Puede crear hasta 30 selecciones por catálogo.
- Puedes añadir hasta cuatro filtros por selección.
- Las selecciones son estupendas para refinar las recomendaciones a partir de los datos del catálogo de Braze. Si busca inspiración, eche un vistazo a [las recomendaciones de About item]({{site.baseurl}}/user_guide/sage_ai/recommendations/about_item_recommendations/) para ver ejemplos de casos de uso.

## Crear una selección

Para crear una selección, haga lo siguiente.

1. Vaya a **Catálogos** y seleccione su catálogo de la lista.
2. Seleccione la pestaña **Selección** y haga clic en **Crear selección**.
3. Dé a su selección un nombre y una descripción opcional.
4. En **Campo de filtro**, seleccione la columna del catálogo por la que desea filtrar. Los campos de cadena con más de 1.000 caracteres no pueden seleccionarse para los filtros.
5. Termine de definir los criterios de filtrado seleccionando el operador correspondiente (por ejemplo, "igual" o "no igual") y el atributo.
6. En la sección **Tipo de ordenación**, determine cómo se ordenan los resultados. Por defecto, los resultados no se muestran en un orden determinado. Para especificar la ordenación por un campo concreto, desactive **Ordenar aleatoriamente** y especifique el **Campo de ordenación** y el **Orden de ordenación** (ascendente o descendente).
7. En la sección **Límite de resultados**, introduzca el número máximo de resultados, hasta 50.
8. Haga clic en **Crear selección**.

### Líquido en los resultados de la selección

El uso de cualquier Líquido en los catálogos, como atributos personalizados y eventos personalizados, puede hacer que se devuelvan resultados diferentes para cada usuario de su selección.

![Ajustes de filtro para la selección de catálogos en los que el atributo se establece en un atributo personalizado de Liquid.][7]

## Utilizar selecciones en la mensajería

Tras crear tu selección, personaliza tus mensajes con Liquid para insertar los elementos filtrados de ese catálogo. Puede hacer que Braze genere el Líquido por usted desde la ventana de personalización que se encuentra en los compositores de mensajes:

1. En cualquier compositor de mensajes que admita la personalización, haga clic en <i class="fa-solid fa-circle-plus" style="color: #12aec5;" title="Añadir personalización"></i> para abrir la ventana de personalización.
2. En **Tipo de personalización**, seleccione **Elementos de catálogo**.
3. Seleccione el nombre de su catálogo.
4. En **Método de selección de elementos**, seleccione **Utilizar una selección**.
4. Seleccione su selección de la lista.
5. En **Información a mostrar**, seleccione qué campos del catálogo deben incluirse para cada artículo.
6. Haga clic en el icono **Copiar** y pegue el Líquido donde tenga que ir en su mensaje.

![El modal Añadir Personalización con las siguientes selecciones: "Catalog Items" para "Personalization Type", "Games" para "Catalog Name", "Selections" para "Selection Type", "game_selection" para "Selection", y "title" y "description_es" para "Information to Display".][6]{: style="max-width:70%;"}

## Casos de uso

Supongamos que tienes un servicio de reparto de comida a domicilio y quieres enviar un mensaje personalizado a los usuarios que tienen preferencias específicas de comida en función de la categoría de alimentos que hayan consultado más recientemente. 

Utilizando un catálogo con la información de su servicio de reparto de comidas para el nombre de la comida, el precio, la imagen y la categoría de la comida, puede crear una selección para recomendar tres comidas en función de la categoría que el usuario haya visto más recientemente.

![Ejemplo de selección para un servicio de reparto de comidas con dos filtros: uno que identifica un tipo de producto como comida y otro que identifica la categoría como la más vista recientemente. La selección se establece para aleatorizar el orden en que se devuelven los tres resultados.][2]{: style="max-width:90%;"}

Para utilizar este catálogo y esta selección en una campaña, utilice el modal **Añadir personalización** en la sección de composición de mensajes de la creación de una campaña. En este ejemplo, hemos seleccionado el catálogo con la información de su servicio de reparto de comidas, y la selección para recomendaciones de comidas basada en la categoría vista más recientemente. Esto nos permite mostrar el nombre de la comida y el precio. Para reforzar aún más su mensaje, puede utilizar la selección para añadir también una imagen de la primera comida recomendada.

![Una tarjeta de contenido con el encabezado "¡Te ENCANTARÁN estas comidas tan valoradas!" con la selección "recomendaciones_recientes_categoría" en la sección de composición del mensaje.][3]{: style="max-width:90%;"}

Por ejemplo, supongamos que tiene un usuario cuya última categoría consultada es "Pollo". Utilizando la personalización establecida y una campaña de tarjeta de contenido, puede enviar tres recomendaciones de comidas que incluyan pollo para este usuario.

![Una tarjeta de contenido con una imagen de pollo al limón a la parrilla y una lista de tres recomendaciones de comidas que incluyen pollo, basadas en la última categoría consultada por el usuario.][4]{: style="max-width:90%;"}

Utilizando la misma personalización, también puede enviar tres recomendaciones de comidas a un usuario cuya última categoría consultada sea "Carne de vacuno".

![Una tarjeta de contenido con una imagen de stroganoff de ternera y una lista de dos recomendaciones de comidas que incluyen ternera, basada en la última categoría consultada por el usuario.][5]{: style="max-width:90%;"}


[1]: {% image_buster /assets/img_archive/catalog_selections1.png %}
[2]: {% image_buster /assets/img_archive/catalog_selections2.png %}
[3]: {% image_buster /assets/img_archive/catalog_selections3.png %}
[4]: {% image_buster /assets/img_archive/catalog_selections4.png %}
[5]: {% image_buster /assets/img_archive/catalog_selections5.png %}
[6]: {% image_buster /assets/img_archive/catalog_selections6.png %}
[7]: {% image_buster /assets/img_archive/catalog_selections7.png %}
