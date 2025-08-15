---
nav_title: Catálogos
article_title: Catálogos
page_order: 6
layout: dev_guide

guide_top_header: "Catálogos"
guide_top_text: "Los catálogos acceden a datos de archivos CSV importados y de puntos finales de API para enriquecer sus mensajes, de forma similar a como accedería a atributos personalizados o propiedades de eventos personalizados a través de Liquid."

description: "Esta página de destino alberga catálogos. Utilice catálogos y conjuntos filtrados para aprovechar los datos de no usuarios en sus campañas Braze para enviar mensajes personalizados."

guide_featured_title: "Artículos de sección"
guide_featured_list:
- name: Crear un catálogo
  link: /docs/user_guide/personalization_and_dynamic_content/catalogs/catalog/
  image: /assets/img/braze_icons/users-01.svg
- name: Uso de catálogos
  link: /docs/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/
  image: /assets/img/braze_icons/users-01.svg
- name: Notificaciones de existencias
  link: /docs/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Notificaciones de bajada de precios
  link: /docs/price_drop_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Selecciones
  link: /docs/user_guide/personalization_and_dynamic_content/catalogs/selections/
  image: /assets/img/braze_icons/list.svg
- name: Puntos finales de la API de catálogos
  link: /docs/api/endpoints/catalogs/
  image: /assets/img/braze_icons/server-01.svg

guide_menu_title: "Other articles"
guide_menu_list:
- name: Bloques de producto arrastrar y soltar
  link: /docs/dnd_product_blocks/
  image: /assets/img/braze_icons/columns-01.svg
---
<br><br>

## Casos de uso del catálogo

Puede introducir cualquier tipo de datos en un catálogo. Normalmente, los datos son metadatos sobre ofertas, como productos, descuentos, promociones, eventos y similares. En los siguientes casos de uso encontrará algunos ejemplos de cómo puede utilizar estos datos para dirigirse a los usuarios con mensajes de gran relevancia.

### Comercio minorista y comercio electrónico

- **Promociones de temporada:** Importe colecciones de productos de temporada y personalice los mensajes para reflejar las tendencias actuales.
- **Mensajes localizados:** Importe las direcciones, horarios y servicios de su ubicación física y, a continuación, personalice las notificaciones en función de la ubicación de los usuarios.
- **Notificaciones de existencias:** Importe información de productos que incluya la cantidad de existencias y, a continuación, utilice [las notificaciones de reposición de existencias]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications/) y los eventos personalizados Braze para activar una campaña o Canvas que envíe a los usuarios una notificación de que un producto ya está en existencias.
- **Notificaciones de bajada de precios:** Importe información de productos que incluya precios de productos y, a continuación, utilice [notificaciones de bajada de precios]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/price_drop_notifications/) y eventos personalizados Braze para activar un Canvas que envíe a los usuarios una notificación de que el precio de un producto ha bajado.

### Entretenimiento

- **Planes de suscripción:** Importe planes de suscripción y promocione complementos a sus usuarios en función de sus pautas de uso y de los tipos de contenidos que consumen con más frecuencia.
- **Próximos eventos:** Importa las listas de los próximos eventos, su ubicación y la edad del público, y envía notificaciones personalizadas a los usuarios que se encuentren en la zona y tengan la edad deseada.
- **Preferencias multimedia:** Importa información sobre películas y programas y, a continuación, recomienda contenidos a tus usuarios en función de sus títulos favoritos y los géneros más vistos.

### Viajes y hostelería

- **Destinos:** Importe destinos de viaje y sus atracciones, restaurantes y actividades más populares y, a continuación, personalice las recomendaciones a sus usuarios basándose en sus viajes anteriores.
- **Alojamiento:** Importe establecimientos hoteleros y sus servicios, tipos de habitación y precios, y envíe promociones a sus usuarios en función de las preferencias que hayan seleccionado.
- **Métodos de viaje**: Importe ofertas y promociones para modalidades de viaje (como vuelos, trenes, coches de alquiler y otros) y envíelas a sus usuarios en función de su historial de búsqueda reciente.
- **Preferencias alimentarias:** Importe información sobre la oferta de comidas y utilice [las selecciones]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/) para enviar mensajes personalizados a los usuarios que tengan preferencias de comida específicas en función de la categoría de comida que hayan consultado más recientemente.

## Cómo colaboran los catálogos y Liquid

Los catálogos son una característica del almacenamiento de datos. Contienen grandes conjuntos de datos a los que puede hacer referencia en sus mensajes para personalizarlos. Para hacer referencia a los datos, utilizarás [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) como lenguaje de plantilla. En otras palabras, los catálogos son el almacenamiento donde se guardan los datos, y Liquid es el lenguaje que extrae los datos relevantes del almacenamiento.

Para ver ejemplos de cómo puede utilizar Liquid para extraer información del catálogo, consulte los casos de uso adicionales en [Creación de un catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#additional-use-cases/).

#### Limitaciones de almacenamiento de datos

El almacenamiento de datos para los catálogos está limitado en función del tamaño de los elementos y selecciones del catálogo, que puede ser diferente de los tamaños de los archivos CSV cargados.

Para la versión gratuita de los catálogos, la cantidad de almacenamiento permitida es de hasta 100 MB. Puedes tener elementos ilimitados siempre que el espacio de almacenamiento no supere los 100 MB. Las selecciones contribuirán a su almacenamiento. Cuanto más compleja sea una selección, más espacio ocupará.

Para Catálogos Pro, las opciones de tamaño de almacenamiento son: 5 GB, 10 GB, 15 GB o 50 GB. Ten en cuenta que el almacenamiento de la versión gratuita (100 MB) está incluido en cada uno de estos planes.
