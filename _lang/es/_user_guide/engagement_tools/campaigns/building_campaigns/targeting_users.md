---
nav_title: Segmentación de usuarios
article_title: Segmentación de usuarios
page_order: 4
tool: Campaigns
page_type: reference
description: "Este artículo de referencia trata sobre las Opciones de segmentación que se encuentran en el paso Públicos objetivo de la creación de campañas."
---

# Segmentación de usuarios

> Después de [componer su campaña][1] y determinar su [calendario de entrega][2], puede establecer los destinatarios de su campaña en el paso **Destinatarios**. 

## Opciones de segmentación

En la sección **Opciones de segmentación**, encontrará varias opciones para saber a quién puede enviar su campaña.

{% alert note %}
Sólo los usuarios que coincidan con los criterios definidos recibirán la campaña. Tenga en cuenta que la pertenencia exacta a un segmento siempre se calcula justo antes de enviar el mensaje.
{% endalert %}

### Dirigirse a usuarios de un segmento existente {#existing-segment}

Para dirigirse a los miembros de un segmento creado previamente, seleccione un segmento del desplegable en **Usuarios objetivo por segmento**.

### Dirigirse a usuarios de múltiples segmentos existentes {#multiple-existing-segment}

Para dirigirse a usuarios que pertenecen a varios segmentos creados previamente, añada varios segmentos desde el menú desplegable en **Usuarios objetivo por segmento**. La audiencia objetivo resultante serán usuarios tanto del primer segmento como del segundo y del tercero, etc.

### Diríjase a usuarios de múltiples segmentos y filtros existentes {#existing_segment_filter}

También puede dirigirse a los usuarios de uno o varios segmentos creados previamente que también estén incluidos en filtros adicionales. Después de seleccionar primero sus segmentos, puede refinar aún más su audiencia en la sección **Filtros adicionales**. Esto se demuestra en la siguiente captura de pantalla, que se dirige a los usuarios que se encuentran en el segmento de Usuarios activos diarios, en el segmento de Correos electrónicos no abiertos y que realizaron una compra hace menos de 30 días.

![][25]

### Dirigirse a usuarios sin segmentos {#without-segment}

Para dirigirse a los usuarios sin añadir un segmento, puede utilizar una serie de filtros. Esto significa que no necesita dirigir una campaña a un segmento preexistente, puede crear un público improvisado durante la creación de la campaña utilizando simplemente los filtros adicionales, y no seleccionando ningún segmento en **Dirigir usuarios por segmento**. Esto le permitirá omitir la creación de segmentos cuando envíe campañas a públicos puntuales.

![][26]

## Segmentación de grupos semilla

En el caso de las campañas por correo electrónico, puede dirigirse a los Grupos semilla en la sección **Grupos semilla**. Tenga en cuenta que los grupos de semillas no están disponibles para las campañas de API, aunque puede incluir grupos de semillas a través de una entrada activada por API en una campaña. Para más información, consulta [Grupos semilla]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#seed-groups).

## Prueba tu audiencia

Después de añadir segmentos y filtros a su público, puede probar si su público está configurado como se esperaba [buscando un usuario]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) para confirmar si coincide con los criterios del público.

![]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:60%"}

## Resumen para la audiencia

Una vez que haya añadido segmentos o filtros para afinar su audiencia, el **Resumen de audiencia** le mostrará una visión general de quiénes forman parte de su audiencia objetivo. Aquí puedes limitar aún más la audiencia de tu campaña estableciendo un tope máximo de usuarios o [limitando][3] la velocidad de envío. Para las campañas de correo electrónico y notificaciones push, puedes seleccionar a qué estado de suscripción y adhesión voluntaria deseas dirigirte.

![][27]

## Pruebas A/B

En la sección **Pruebas A/B**, puede configurar una prueba para comparar las respuestas de los usuarios a varias versiones de la misma campaña de marketing. Estas versiones comparten objetivos de marketing similares, pero difieren en la redacción y el estilo. El objetivo es identificar la versión de la campaña que mejor cumpla sus objetivos de marketing. 

Para obtener más información y conocer las mejores prácticas, consulta [Multivariante y pruebas A/B][4].

## Estadísticas de audiencia

Braze proporciona estadísticas detalladas de audiencia de los canales seleccionados en el pie de página. 

Cuanto mayor sea tu base de usuarios, más probable es que la cantidad **de Usuarios alcanzables** sea una estimación aproximada. El número de usuarios accesibles puede disminuir si utiliza un [Grupo de Control Global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) o configura la elegibilidad de mensajes. Selecciona [Calcular estadísticas exactas]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics) para determinar un número exacto de tus usuarios alcanzables, ya que se buscará entre todos los usuarios de tu base de usuarios. 

Toma nota:

- Calcular las estadísticas exactas puede llevar unos minutos. Esta función sólo calcula las estadísticas exactas a nivel de segmento, no a nivel de filtro o grupo de filtros.
- En el caso de segmentos grandes, es normal que se produzcan ligeras variaciones incluso cuando se calculan estadísticas exactas. Se espera que la precisión de esta característica sea del 99,999 % o superior.

![][24]

Para ver a qué porcentaje de tu base de usuarios se dirige o el valor de duración del ciclo de vida (LTV) de este segmento, selecciona **Mostrar estadísticas adicionales**.

[1]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/
[3]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/
[4]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/
[24]: {% image_buster /assets/img_archive/multi_channel_footer.png %}
[25]: {% image_buster /assets/img_archive/target_segmenter.png %}
[26]: {% image_buster /assets/img_archive/additional_filters.png %}
[27]: {% image_buster /assets/img_archive/audience_summary.png %}
