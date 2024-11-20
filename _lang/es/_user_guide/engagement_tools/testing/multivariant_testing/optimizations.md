---
nav_title: Optimizaciones
article_title: Optimización de pruebas A/B con variante ganadora o variantes personalizadas
page_order: 1
page_type: reference
description: "Aprenda a utilizar Variante ganadora o Variante personalizada al crear pruebas multivariante y A/B."
---

# Optimización de pruebas A/B con Variante Ganadora o Variantes Personalizadas

Al [crear una prueba A/B][1] para campañas de correo electrónico, push, webhook, SMS y WhatsApp programadas para enviarse una vez, puede seleccionar una optimización. Hay dos opciones de optimización: **Variante Ganadora** y **Variante Personalizada**.

![Opciones de optimización enumeradas en la sección Pruebas A/B al elegir tu audiencia objetivo. Hay tres opciones: Sin optimización, Variante ganadora y Variante personalizada. Variante personalizada seleccionada.]({% image_buster /assets/img_archive/ab_personalized_variant.png %})

Ambas opciones funcionan enviando una prueba inicial a un porcentaje de su segmento objetivo. Una vez finalizada la prueba, se envía a los usuarios restantes la variante con mejores resultados (variante ganadora) o la variante con la que es más probable que interactúen (variante personalizada).

{% alert tip %}
Las optimizaciones se encuentran en el paso **Públicos objetivo** de la creación de campañas, en **Pruebas A/B**.
{% endalert %}

## Variante ganadora

El envío de la Variante Ganadora es similar a una prueba A/B estándar. Los usuarios de este grupo recibirán la Variante Ganadora cuando finalice la prueba inicial.

1. Seleccione Variante **ganadora** y, a continuación, especifique qué porcentaje del público de su campaña debe asignarse al grupo Variante ganadora.
2. Configure los siguientes ajustes adicionales.

| Campo | Descripción |
| --- | --- | 
| Métrica de optimización | La métrica para la que optimizar. Elija entre *Aperturas Únicas* o *Clics* para correo electrónico, *Aperturas* para push, o *Tasa de Conversión Primaria* para todos los canales. Seleccionar *Aperturas* o *Clics* para determinar el ganador no afecta a lo que elija para los [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/) de la campaña. <br><br>Tenga en cuenta que si utiliza un grupo de control, los usuarios del grupo de control no pueden realizar *Aperturas* ni *Clics*, por lo que el rendimiento del grupo de control está garantizado en `0`. Como resultado, el grupo de control no puede ganar la prueba A/B. Sin embargo, es posible que aún desee utilizar un grupo de control para realizar un seguimiento de otras métricas para los usuarios que no reciben un mensaje. |
| Fecha de inicio de la prueba inicial | La fecha y hora de inicio de la prueba inicial. |
| Fecha de finalización de la prueba inicial | La fecha y hora de finalización de la prueba inicial. Es entonces cuando se envía la Variante Ganadora al resto de usuarios.<br><br>Cuando se envía en la hora local de los usuarios o con Temporización inteligente, la Variante ganadora debe enviarse al menos 24 horas después de la prueba A/B para garantizar la entrega a todos los usuarios del grupo de la Variante ganadora. |
| Alternativa | Qué ocurre si ninguna variante gana por un margen estadísticamente significativo. Elija entre enviar de todos modos la variante con mejores resultados o finalizar la prueba y no enviar más mensajes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Variante personalizada

Utilice Variantes Personalizadas para enviar a cada usuario de su segmento objetivo la variante con la que es más probable que interactúe.

Para determinar la mejor variante para cada usuario, Braze enviará una prueba inicial a una parte de su público objetivo para buscar asociaciones entre las características de los usuarios y las preferencias de los mensajes. En función de cómo respondan los usuarios a cada variante en la prueba inicial, estas características se utilizan para determinar qué usuarios restantes recibirán cada variante. Si no se encuentran asociaciones y no se pueden realizar personalizaciones, la Variante Ganadora se envía automáticamente a los usuarios restantes. Para saber más sobre cómo se determinan las Variantes Personalizadas, consulte [Análisis multivariante y test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#personalized-variant).

1. Seleccione Variante **personalizada** y, a continuación, especifique qué porcentaje del público de su campaña debe asignarse al grupo Variante personalizada.
2. Configure los siguientes ajustes adicionales.

| Campo | Descripción |
| --- | --- | 
| Métrica de optimización | La métrica para la que optimizar. Elija entre *Aperturas Únicas* o *Clics* para correo electrónico, *Aperturas* para push, o *Tasa de Conversión Primaria* para todos los canales. Seleccionar *Aperturas* o *Clics* para determinar el ganador no afecta a lo que elija para los [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#conversion-events) de la campaña. <br><br>Tenga en cuenta que si utiliza un grupo de control, los usuarios del grupo de control no pueden realizar *Aperturas* ni *Clics*, por lo que el rendimiento del grupo de control está garantizado en `0`. Como resultado, el grupo de control no puede ganar la prueba A/B. Sin embargo, es posible que aún desee utilizar un grupo de control para realizar un seguimiento de otras métricas para los usuarios que no reciben un mensaje. |
| Fecha de inicio de la prueba inicial | La fecha y hora de inicio de la prueba inicial. |
| Fecha de finalización de la prueba inicial | La fecha y hora de finalización de la prueba inicial. Es entonces cuando se envían las Variantes Personalizadas al resto de usuarios. Recomendamos 24 horas como referencia para garantizar unos resultados estadísticamente significativos. Cuanto más tiempo dedique a la prueba, más respuestas recibirá y más podrá optimizar Braze. Esto es especialmente importante para las campañas por correo electrónico. Las pruebas iniciales de Variantes Personalizadas no deberían durar menos de 4 horas.<br><br>Cuando se envían en la hora local de los usuarios o con Temporización inteligente, las Variantes personalizadas deben enviarse al menos 24 horas después de la prueba A/B para garantizar la entrega a todos los usuarios del grupo de Variantes personalizadas. |
| Alternativa | Qué ocurre si no se encuentran Variantes Personalizadas. Elija entre enviar la Variante Ganadora en su lugar, o finalizar la prueba y no enviar más mensajes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Análisis

Para conocer los resultados de su prueba A/B con una optimización, consulte [Análisis de pruebas multivariantes y A/B][2].

[1]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/
[2]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/