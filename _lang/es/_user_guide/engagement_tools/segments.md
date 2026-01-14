---
nav_title: Segmentos
article_title: Segmentos
page_order: 1
layout: dev_guide
guide_top_header: "Segmentos"
guide_top_text: "La segmentación de la audiencia es clave para el marketing estratégico: puede evitar que te dirijas demasiado a un cliente, que lo molestes o que pierdas una conexión potencial con él. Consulta los siguientes artículos para aprender a segmentar y filtrar tu audiencia para tu mayor beneficio (y el suyo)."
descriptions: "La segmentación de la audiencia es clave para el marketing estratégico: puede evitar que te dirijas demasiado a un cliente, que lo molestes o que pierdas una conexión potencial con él. Consulta esta página de aterrizaje para aprender a segmentar y filtrar tu audiencia para tu mayor beneficio (y el suyo)."
search_rank: 4
tool: Segments
page_type: landing
description: "Esta página de aterrizaje cubre artículos sobre Segmentación dentro de campañas de paneles. Aquí encontrarás información sobre cómo configurar un segmento, filtros, embudos, información, extensiones y mucho más."

guide_featured_title: "Artículos populares"
guide_featured_list:
  - name: Crear un segmento
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
  - name: Información por segmentos
    link: /docs/user_guide/engagement_tools/segments/segment_insights/
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Extensión de segmento
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
  - name: Localización
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

En Braze, los segmentos son grupos dinámicos de usuarios que se ajustan a los criterios específicos que definas, como atributos del usuario, comportamiento del usuario y eventos personalizados. Puedes ser más granular con los criterios anidando segmentos dentro de otros segmentos y aplicando características adicionales, reduciendo el alcance de tu audiencia para que puedas enviar contenido altamente personalizado y atractivo a los usuarios adecuados.

Puedes crear tantos segmentos como quieras para dirigirte a los usuarios. Explora diferentes combinaciones de características de segmentos y filtros de segmentación para descubrir formas creativas de utilizar tus datos de usuario, y descubre nuevas maneras de enviar mensajes relevantes a los usuarios y aumentar la interacción.

Echa un vistazo a los casos de uso siguientes para obtener una pequeña vista previa de cómo los segmentos Braze pueden ayudarte a dirigirte a tus usuarios.

### Casos de uso

- **Mensajes de bienvenida:** Segmenta a los nuevos usuarios para que puedas enviarles correos electrónicos de incorporación o mensajes dentro de la aplicación que les presenten tu aplicación.
- **Recompensas por fidelización:** Segmenta a los usuarios en función de su frecuencia de compra, aniversario de afiliación u otros hitos, y envía ofertas o recompensas exclusivas a tus usuarios más fieles.
- **Desencadenantes del comportamiento:** Segmenta a los usuarios en función de sus acciones, como abandonar un carrito en la caja, para desencadenar mensajes dentro de la aplicación o notificaciones push.
- **Recomendaciones de artículos:** Segmenta a los usuarios que compraron productos específicos y envíales recomendaciones de productos complementarios o de nivel superior.
- **Pruebas A/B:** Segmenta a los usuarios para realizar pruebas A/B con diferentes mensajes, líneas del asunto o contenidos para determinar qué resuena mejor entre los usuarios de edades, géneros y otros atributos específicos.

#### Casos de uso de las extensiones de segmento

Puedes refinar aún más tus segmentos utilizando [las extensiones de segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) para dirigirte a los usuarios en función de un evento personalizado o del comportamiento de compra almacenado durante toda la vida de su perfil de usuario.

- **Compras históricas:** Segmenta a los usuarios en función de si compraron un color concreto de un producto específico al menos dos veces en los últimos dos años.
- **Eventos e interacciones de mensajes:** Segmenta a los usuarios según si hicieron una compra en los últimos treinta días y también interactuaron con un mensaje dentro de la aplicación específico.
- **Consulta los datos:** 
  - **Consulta Snowflake:** Segmenta a los usuarios con datos combinados de Braze y fuentes externas, como un CRM o un almacén de datos, utilizando [las extensiones de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/) para consultar Snowflake.
  - **Sincroniza desde el almacén de datos:** Segmenta a los usuarios con datos sincronizados directamente desde tu almacén de datos o sistema de almacenamiento de archivos a Braze utilizando [las extensiones de segmento CDI]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/).

