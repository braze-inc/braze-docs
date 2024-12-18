---
nav_title: Recomendaciones basadas en reglas
article_title: Recomendaciones basadas en reglas
page_type: tutorial
page_order: 16
alias: "/rules_based_recommendations/"
description: "Este artículo describe cómo crear una herramienta de recomendaciones basada en reglas que utilice catálogos o Contenidos Conectados."
tool:
  - Campaigns
  - Canvas

---

# Recomendaciones basadas en reglas

> Una herramienta de recomendaciones basada en reglas utiliza datos de usuario e información sobre productos para sugerir a los usuarios elementos relevantes dentro de los mensajes. Utiliza [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) y [los catálogos]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/) Braze o [el Contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), para personalizar dinámicamente el contenido en función del comportamiento y los atributos del usuario.

Para saber más sobre Liquid, catálogos y contenido conectado, consulta estos cursos de Braze Learning:

- [Recomendaciones personalizadas por correo electrónico](https://learning.braze.com/personalized-recommendations-with-email)
- [Personalización dinámica con Liquid](https://learning.braze.com/path/dynamic-personalization-with-liquid)
- [Fundamentos del contenido conectado](https://learning.braze.com/path/dynamic-personalization-with-liquid/connected-content-fundamentals)

{% alert important %}
Las recomendaciones basadas en reglas se basan en una lógica fija que debes establecer manualmente. Esto significa que tus recomendaciones no se ajustarán al historial de compras y gustos de un usuario a menos que actualices la lógica.<br><br>Para crear recomendaciones de IA personalizadas que se ajusten automáticamente al historial del usuario, consulta [Recomendaciones de artículos de IA]({{site.baseurl}}/user_guide/brazeai/recommendations/ai_item_recommendations/).
{% endalert %}

## Creación de una herramienta de recomendaciones de catálogos

1. [Crea un catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/) de productos.
2. Para cada producto, añade una lista de productos recomendados como una cadena separada por un delimitador (como una tubería `|`) en una columna llamada "recomendaciones_productos".
3. Pasa al catálogo el ID del producto para el que quieres encontrar recomendaciones.
4. Obtén el valor `product_recommendations` de ese artículo del catálogo y divídelo por el delimitador con un filtro de división Liquid.
5. Vuelve a pasar uno o varios de esos ID al catálogo para recoger los demás detalles del producto.

### Caso de uso de los catálogos

Supongamos que tienes una aplicación de comida sana y quieres crear una campaña de tarjeta de contenido que envíe recetas diferentes en función del tiempo que un usuario lleva registrado en tu aplicación. 

1. Crea y sube un catálogo mediante CSV que incluya la siguiente información:<br>- **ID:** Un número único que se correlaciona con el número de días transcurridos desde que el usuario se registró en tu aplicación. Por ejemplo, `3` se correlaciona con tres días.<br>- **tipo:** La categoría de la receta, como `comfort`, `fresh`, y otras.<br>- **título:** El título de la tarjeta de contenido que se enviará para cada ID, como "Prepárate para comer esta semana" o "Hagamos un taco al respecto".<br>- **enlace:** El enlace al artículo de la receta.<br>- **imagen_url:** La imagen que corresponde a la receta.

{: start="2"}
2\. Una vez cargado el catálogo en Braze, comprueba la vista previa de un número selecto de elementos del catálogo para confirmar que la información importada es correcta. Los elementos pueden ser aleatorios en la vista previa, pero esto no afectará al resultado de la herramienta de recomendaciones.

![][1]

{: start="3"}
3\. Crea una campaña de tarjeta de contenido. En el compositor, introduce la lógica Liquid para determinar qué usuarios deben recibir la campaña, y qué receta e imagen deben mostrarse. En este caso de uso, Braze obtendrá el `start_date` (o fecha de registro) del usuario y lo comparará con la fecha actual. La diferencia de días determinará qué tarjeta de contenido se envía. 

![][2]

**Título,**

{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].title }}
```
{% endraw %}

**Mensaje:**

{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{% if items[0].title != blank %}
{{ items[0].body }}
{% else %}
{% abort_message('no card for today') %}
{% endif %}
```
{% endraw %}

**Imagen:**

{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].image_url }}
```
{% endraw %}

{: start="4"}
4\. En la sección **Comportamiento al hacer clic**, introduce la lógica Liquid para saber a dónde deben ser redirigidos los usuarios cuando hacen clic en la tarjeta de contenido en dispositivos iOS, Android y Web. 

{% raw %}
```liquid
{% assign start_date = {{custom_attribute.${start_date}}} | date: "%s" %}
{% assign current_date = "now" | date: "%s" %}
{% assign diff = {{current_date}} | minus: {{start_date}} | divided_by: 86400 %}
{% assign days = {{diff}} | round %}
{% catalog_items Healthy_Recipe_Catalog_SMB {{days}} %}
{{ items[0].link }}
```
{% endraw %}

![][3]{: style="max-width:60%;"}<br><br>

{: start="5"}
5\. Ve a la pestaña de **Prueba** y selecciona **Usuario personalizado** en **Vista previa del mensaje como usuario**. Introduce una fecha en el campo **Atributo personalizado** para obtener una vista previa de la tarjeta de contenido que se enviaría a un usuario que se hubiera registrado en esa fecha. <br><br>

![][4]

## Creación de una herramienta de recomendaciones de contenido conectado

1. Crea un punto final de Contenido conectado de una de las siguientes maneras:
- Convierte una hoja de cálculo en un punto final API JSON utilizando un servicio como SheetDP, y toma nota de la URL API que esto genera
- Construir, alojar y mantener un punto final interno personalizado
- Compra una herramienta de recomendaciones a través de un socio externo, como uno de nuestros [socios de Alloys]({{site.baseurl}}/partners/message_personalization/dynamic_content/), entre los que se incluyen [Amazon Personalise]({{site.baseurl}}/partners/message_personalization/dynamic_content/amazon_personalize/), [Certona]({{site.baseurl}}/partners/message_personalization/dynamic_content/certona/), [Dynamic Yield]({{site.baseurl}}/partners/message_personalization/dynamic_content/dynamic_yield/) y otros.

2. Escribe Contenido conectado Liquid en el cuerpo del mensaje o en el bloque de contenido del editor HTML que llamará a tu punto final para buscar en tu base de datos.
3. Alinea el Liquid con un valor de atributo personalizado que encuentre en el perfil de un usuario determinado.
4. Tira de la recomendación correcta como resultado.

{% raw %}
```
{% connected_content YOUR-API-URL :save items %}

{% assign recommended_item_ids_from_user_profile = custom_attribute.${RECOMMENDED_ITEM_IDS} | split: ';' %}

{% for item_id in recommended_item_ids_from_user_profile %}
  {% assign recommended_item = items | where: "ITEM_ID", ITEM_ID | first %}
  recommended_item.item_name
{% endfor %}
```
{% endraw %}

| Atributo | Sustitución |
| --- | --- |
|`YOUR-API-URL` | Sustitúyelo por la URL real de tu API. |
|`RECOMMENDED_ITEM_IDS` | Sustitúyelo por el nombre real de tu atributo personalizado que contiene los ID de los elementos recomendados. Se espera que este atributo sea una cadena de ID separados por punto y coma. |
|`ITEM_ID` | Sustitúyelo por el nombre real del atributo de tu respuesta a la API que corresponda al ID del artículo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Éste es un ejemplo básico y puede que tengas que modificarlo más en función de tus necesidades específicas y de la estructura de tus datos. Para obtener información más detallada, consulta la [documentación de Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) o a un desarrollador.
{% endalert %}

## Caso de uso del Contenido conectado

Supongamos que quieres extraer recomendaciones de restaurantes de la base de datos Zomato Restaurants y guardar el resultado como una variable local llamada `restaurants`. Puedes hacer la siguiente llamada de Contenido conectado:

{% raw %}
```liquid

{% connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{{city_food.restaurants[0]}}
```
{% endraw %}

A continuación, digamos que quieres obtener recomendaciones de restaurantes en función de la ciudad y el tipo de comida de un usuario. Puedes hacerlo insertando dinámicamente los atributos personalizados para la ciudad y el tipo de comida del usuario al principio de la llamada, y asignando después el valor de `restaurants` a la variable `city_food.restaurants`.

La llamada al Contenido conectado tendría el siguiente aspecto:

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}

{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:“USER_KEY”} :save restaurants %}

{% assign restaurants = city_food.restaurants %}

{{city_food.restaurants[0]}}
```
{% endraw %}

Si quieres adaptar la respuesta para recuperar sólo el nombre y la tasa del restaurante, puedes añadir filtros al final de la llamada, de esta forma

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}

{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:”USER_KEY”} :save restaurants %}
{% assign restaurants = city_food.restaurants %}

{{city_food.restaurants[0].restaurant.name}}
{{city_food.restaurants[0].restaurant.user_rating.rating_text}}
```
{% endraw %}

Por último, supongamos que quieres agrupar las recomendaciones de restaurantes por tasas. Haz lo siguiente:

1. Utiliza `assign` para crear matrices en blanco para las categorías de valoración "excelente", "muy bueno" y "bueno".
2. Añade un bucle `for` que examine la tasa de cada restaurante de la lista. 
- Si la tasa es "Excelente", añade el nombre del restaurante a la cadena `excellent_restaurants` y, a continuación, añade un carácter * al final para separar cada nombre de restaurante. 
- Si la tasa es "Muy buena", añade el nombre del restaurante a la cadena `very_good_restaurants` y, a continuación, añade un carácter * al final.
- Si la valoración es "Buena", añade el nombre del restaurante a la cadena `good_restaurants` y, a continuación, añade un carácter * al final.
3. Limita el número de recomendaciones de restaurantes devueltas a cuatro por categoría.

Así sería la convocatoria final:

{% raw %}
```liquid
{% assign city_id = {{custom_attribute.${city_id} | default: ‘306’}} %}
{% assign food_type = {{custom_attribute.${food_type} | default: ‘471’}} %}
{%- connected_content https://developers.zomato.com/api/v2.1/search?entity_id={{city_id}}&entity_type=city&count=20&cuisines={{food_type}}&sort=rating:headers{“user-key”:”USER_KEY”} :save restaurants %}
{% assign restaurants = city_food.restaurants %}
{% assign excellent_restaurants = “” %}
{% assign very_good_resturants = “” %}
{% assign good_restaurants = “” %}
{% for list in restaurants %}
{% if {{list.restaurant.user_rating.rating_text}} == `Excellent` %}
{% assign excellent_restaurants = excellent_restaurants | append: list.restaurant.name | append: `*` %}
{% elseif {{list.restaurant.user_rating.rating_text}} == `Very Good` %}
{% assign very_good_restaurants = very_good_restaurants | append: list.restaurant.name | append: `*` %}
{% elseif {{list.restaurant.user_rating.rating_text}} == `Good` %}
{% assign good_restaurants = good_restaurants | append: list.restaurant.name | append: `*` %}
{% endif %}
{% endfor %}
{% assign excellent_array = excellent_restaurants | split: `*` %}
{% assign very_good_array = very_good_restaurants | split: `*` %}
{% assign good_array = good_restaurants | split: `*` %}

Excellent places
{% for list in excellent_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}

Very good places
{% for list in very_good_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}

Good places
{% for list in good_array %}

{{list}}
{% assign total_count = total_count | plus:1 %}
{% if total_count >= 4 %}
{% break %}
{% endif %}
{% endfor %}
```
{% endraw %}

Mira la siguiente captura de pantalla para ver un ejemplo de cómo se muestra la respuesta en el dispositivo de un usuario.

![][5]{: style="max-width:30%;"}

## Consideraciones

Cuando decidas qué herramienta de recomendaciones se adapta a tus recursos disponibles y a tus casos de uso, consulta esta tabla de consideraciones:

| Consideraciones | Liquid | Catálogos CSV | API de catálogos | Contenido conectado |
| --- | --- | --- | --- | --- |
| No consume puntos de datos | No se admite | Apoyado | Apoyado | Apoyado |
| Sin solución de código | No se admite | Admitido si está pregenerado Liquid | No se admite | No se admite |
| Liquid avanzado a menudo necesario | Apoyado | No se admite | No se admite | Apoyado |
| Actualizaciones de datos en la fuente de productos | No se admite | Apoyado si las recomendaciones no se actualizan a menudo | Se admite si las recomendaciones se actualizan hasta cada hora | Las ayudas y recomendaciones se actualizan en tiempo real |
| Generar recomendaciones en la interfaz de usuario de Braze | Apoyado | Apoyado | Apoyado | No se admite si se genera fuera de Braze |
| No alojar, administrar, solución de problemas recomendaciones datos | Apoyado | Apoyado | Apoyado | No se admite |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

[1]: {% image_buster /assets/img/recs/catalog_items.png %}
[2]: {% image_buster /assets/img/recs/content_card_preview.png %}
[3]: {% image_buster /assets/img/recs/on_click_behavior.png %}
[4]: {% image_buster /assets/img/recs/custom_attributes_test.png %}
[5]: {% image_buster /assets/img/recs/sample_response.png %}