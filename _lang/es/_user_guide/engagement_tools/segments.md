---
nav_title: Segmentos
article_title: Segmentos
page_order: 1
layout: dev_guide
guide_top_header: "Segmentos"
guide_top_text: "La segmentación del público es clave para el marketing estratégico, ya que puede evitar que se dirija demasiado a un cliente, que le moleste o que pierda una conexión potencial con él. Consulte los siguientes artículos para aprender a segmentar y filtrar su audiencia para su mayor beneficio (y el de ellos)."
descriptions: "La segmentación del público es clave para el marketing estratégico, ya que puede evitar que se dirija demasiado a un cliente, que le moleste o que pierda una conexión potencial con él. Consulta esta página de aterrizaje para aprender a segmentar y filtrar tu audiencia para tu mayor beneficio (y el suyo)."
search_rank: 4
tool: Segments
page_type: landing
description: "Esta página de inicio cubre artículos sobre Segmentación dentro de campañas de paneles. Aquí encontrarás información sobre cómo configurar un segmento, filtros, embudos, insights, extensiones y mucho más."

guide_featured_title: "Artículos populares"
guide_featured_list:
  - name: Creación de un segmento
    link: /docs/user_guide/engagement_tools/segments/creating_a_segment/
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Administrador de segmentos
    link: /docs/user_guide/engagement_tools/segments/managing_segments/
    image: /assets/img/braze_icons/edit-05.svg
  - name: Filtros de segmentación
    link: /docs/user_guide/engagement_tools/segments/segmentation_filters/
    image: /assets/img/braze_icons/flag-02.svg
  - name: Datos de los segmentos
    link: /docs/viewing_and_understanding_segment_data/
    image: /assets/img/braze_icons/pie-chart-01.svg

guide_menu_title: "More articles"
guide_menu_list:
  - name: Información del segmento
    link: /docs/user_guide/engagement_tools/segments/segment_insights/
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Ampliación de segmento
    link: /docs/user_guide/engagement_tools/segments/segment_extension/
    image: /assets/img/braze_icons/users-01.svg
  - name: Segmentos SQL
    link: /docs/sql_segments/
    image: /assets/img/braze_icons/users-01.svg
  - name: Segmentos del catálogo
    link: /docs/catalog_segments/
    image: /assets/img/braze_icons/users-01.svg
  - name: Perfiles de usuario
    link: /docs/user_guide/engagement_tools/segments/user_profiles/
    image: /assets/img/braze_icons/users-01.svg
  - name: Segmentación de ubicación
    link: /docs/user_guide/engagement_tools/segments/location_targeting/
    image: /assets/img/braze_icons/marker-pin-06.svg
  - name: Expresiones regulares
    link: /docs/user_guide/engagement_tools/segments/regex/
    image: /assets/img/braze_icons/search-sm.svg
  - name: Listas de supresión
    link: /docs/user_guide/engagement_tools/segments/suppression_lists/
    image: /assets/img/braze_icons/list.svg 
  - name: Medir el tamaño de los segmentos
    link: /docs/user_guide/engagement_tools/segments/measuring_segment_size/
    image: /assets/img/braze_icons/pie-chart-02.svg
  - name: Solución de problemas
    link: /docs/user_guide/engagement_tools/segments/troubleshooting/
    image: /assets/img/braze_icons/annotation-question.svg

guide_menu_title2: "Other"
guide_menu_list2:
  - name: Atributos personalizados
    link: /docs/user_guide/data/custom_data/custom_attributes/
    image: /assets/img/braze_icons/table.svg

---

## Acerca de los segmentos Braze

En Braze, los segmentos son grupos dinámicos de usuarios que se ajustan a criterios específicos definidos por usted, como atributos de usuario, comportamiento de usuario y eventos personalizados. Puede definir criterios más detallados anidando segmentos dentro de otros segmentos y aplicando funciones adicionales, reduciendo el alcance de su audiencia para poder enviar contenidos altamente personalizados y atractivos a los usuarios adecuados.

Puede crear tantos segmentos como desee para dirigirse a los usuarios. Explore diferentes combinaciones de funciones y filtros de segmentación para descubrir formas creativas de utilizar los datos de sus usuarios y descubrir nuevas maneras de enviar mensajes relevantes a los usuarios y aumentar la participación.

Eche un vistazo a los siguientes casos de uso para ver un pequeño avance de cómo los segmentos Braze pueden ayudarle a segmentar a sus usuarios.

### Ejemplos

- **Mensajes de bienvenida:** Segmente a los nuevos usuarios para poder enviarles correos electrónicos de incorporación o mensajes dentro de la aplicación que les presenten su aplicación.
- **Recompensas por fidelización:** Segmente a los usuarios en función de su frecuencia de compra, aniversario de afiliación u otros hitos, y envíe ofertas o recompensas exclusivas a sus usuarios más fieles.
- **Desencadenantes del comportamiento:** Segmente a los usuarios en función de sus acciones, como el abandono de un carrito en la caja, para activar mensajes en la aplicación o notificaciones push.
- **Recomendación de elementos:** Segmente a los usuarios que compraron productos específicos y envíeles recomendaciones de productos complementarios o de nivel superior.
- **Pruebas A/B:** Segmente a los usuarios para realizar pruebas A/B de diferentes mensajes, líneas de asunto o contenidos para determinar qué resuena mejor con usuarios de edades, géneros y otros atributos específicos.

#### Casos prácticos de ampliación de segmentos

Puede refinar aún más sus segmentos utilizando [las Extensiones de Segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) para dirigirse a los usuarios en función de eventos personalizados o comportamientos de compra almacenados durante toda la vida de su perfil de usuario.

- **Compras históricas:** Segmente a los usuarios en función de si han comprado un color concreto de un producto específico al menos dos veces en los últimos dos años.
- **Eventos e interacciones de mensajes:** Segmente a los usuarios en función de si han realizado una compra en los últimos treinta días y también han interactuado con un mensaje específico dentro de la aplicación.
- **Datos de consulta:** 
  - **Consulta Snowflake:** Segmente a los usuarios con datos combinados de Braze y fuentes externas, como un CRM o un almacén de datos, mediante el uso de [SQL Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) para consultar Snowflake.
  - **Sincronización desde el almacén de datos:** Segmente los usuarios con datos sincronizados directamente desde su almacén de datos o sistema de almacenamiento de archivos a Braze mediante [segmentos CDI]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/).

