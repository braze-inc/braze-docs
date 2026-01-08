---
nav_title: Catálogos
article_title: Catálogos
page_order: 6
layout: dev_guide

guide_top_header: "Catálogos"
guide_top_text: "Los catálogos acceden a datos de archivos CSV importados y puntos finales de API para enriquecer tus mensajes, de forma similar a como accederías a atributos personalizados o propiedades del evento personalizadas a través de Liquid."

description: "Esta página de inicio alberga catálogos. Utiliza catálogos y conjuntos filtrados para aprovechar los datos de no usuarios en tus campañas Braze para enviar mensajes personalizados."

guide_featured_title: "Artículos de sección"
guide_featured_list:
- name: Crear un catálogo
  link: /docs/user_guide/data/activation/catalogs/create/
  image: /assets/img/braze_icons/users-01.svg
- name: Utilizar los catálogos
  link: /docs/user_guide/data/activation/catalogs/use/
  image: /assets/img/braze_icons/users-01.svg
- name: Notificaciones de reposición de existencias
  link: /docs/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Notificaciones de bajada de precios
  link: /docs/price_drop_notifications/
  image: /assets/img/braze_icons/shopping-cart-03.svg
- name: Selecciones
  link: /docs/user_guide/data/activation/catalogs/selections/
  image: /assets/img/braze_icons/list.svg

guide_menu_title: "Other articles"
guide_menu_list:
- name: Catálogos Puntos finales de la API
  link: /docs/api/endpoints/catalogs/
  image: /assets/img/braze_icons/server-01.svg
- name: Bloques de producto arrastrar y soltar
  link: /docs/dnd_product_blocks/
  image: /assets/img/braze_icons/columns-01.svg
---
<br><br>

## Casos de uso del catálogo

Puedes introducir cualquier tipo de datos en un catálogo. Normalmente, los datos son metadatos sobre ofertas, como productos, descuentos, promociones, eventos y similares. Consulta los casos de uso siguientes para ver algunos ejemplos de cómo puedes utilizar estos datos para dirigirte a los usuarios con mensajes muy relevantes.

### Comercio minorista y comercio electrónico

- **Promociones de temporada:** Importa colecciones de productos de temporada y personaliza los mensajes para reflejar las tendencias actuales.
- **Mensajes localizados:** Importa las direcciones, horarios y servicios de tu ubicación física y, a continuación, personaliza las notificaciones en función de la ubicación de los usuarios.
- **Notificaciones de agotamiento de existencias:** Importa información de productos que incluya la cantidad de existencias y, a continuación, utiliza [las notificaciones de reposición de existencias]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/) y los eventos personalizados de Braze para desencadenar una campaña o Canvas que envíe a los usuarios una notificación de que un producto ya está en existencias.
- **Notificaciones de bajada de precios:** Importa información de productos que incluya sus precios y, a continuación, utiliza [notificaciones de bajada de precios]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/price_drop_notifications/) y eventos personalizados de Braze para desencadenar un Canvas que envíe a los usuarios una notificación de que el precio de un producto ha bajado.

### Entretenimiento

- **Planes de suscripción:** Importa planes de suscripción y promociona complementos para tus usuarios basándote en sus patrones de uso y en los tipos de contenido que consumen más a menudo.
- **Próximos eventos:** Importa los listados de próximos eventos y sus ubicaciones y edades de la audiencia, y luego envía notificaciones personalizadas a los usuarios que estén dentro de la zona y tengan las edades objetivo.
- **Preferencias de los medios de comunicación:** Importa información sobre películas y series, y luego recomienda contenidos a tus usuarios en función de sus títulos favoritos y los géneros más vistos.

### Viajes y hostelería

- **Destinos:** Importa destinos de viaje y sus atracciones, restaurantes y actividades más populares, y luego personaliza las recomendaciones a tus usuarios basándote en sus viajes anteriores.
- **Alojamiento:** Importa propiedades hoteleras y sus servicios, tipos de habitación y precios, y luego envía promociones a tus usuarios en función de sus preferencias seleccionadas.
- **Métodos de viaje**: Importa ofertas y promociones de modos de viaje (como vuelos, trenes, coches de alquiler y otros) y envíalas a tus usuarios en función de su historial de búsqueda reciente.
- **Preferencias alimentarias:** Importa información sobre las ofertas de comidas y utiliza [las selecciones]({{site.baseurl}}/user_guide/data/activation/catalogs/selections/) para enviar mensajes personalizados a los usuarios que tengan preferencias de comida específicas basadas en la categoría de comida que hayan visto más recientemente.

## Cómo colaboran los catálogos y Liquid

Los catálogos son una característica del almacenamiento de datos. Contienen grandes conjuntos de datos a los que se puede hacer referencia en tus mensajes para su personalización. Para hacer referencia a los datos, utilizarás [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) como lenguaje de plantilla. En otras palabras, los catálogos son el almacenamiento donde se guardan los datos, y Liquid es el lenguaje que extrae los datos relevantes del almacenamiento.

Para ver ejemplos de cómo puedes utilizar Liquid para extraer información del catálogo, consulta los casos de uso adicionales en [Crear un catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#additional-use-cases/).

#### Limitaciones de almacenamiento de datos

El almacenamiento de datos para los catálogos está limitado en función del tamaño de los elementos del catálogo, que puede ser diferente de los tamaños de los archivos CSV cargados.

Para la versión gratuita de los catálogos, la cantidad de almacenamiento permitida es de hasta 100 MB. Puedes tener elementos ilimitados siempre que el espacio de almacenamiento no supere los 100 MB.

Para Catálogos Pro, las opciones de tamaño de almacenamiento son: 5 GB, 10 GB, 15 GB o 50 GB. Ten en cuenta que el almacenamiento de la versión gratuita (100 MB) está incluido en cada uno de estos planes.
