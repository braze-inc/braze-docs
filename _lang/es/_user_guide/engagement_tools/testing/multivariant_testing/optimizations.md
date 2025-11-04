---
nav_title: Optimizaciones
article_title: Optimizar las pruebas A/B con variantes ganadoras o personalizadas
page_order: 1
page_type: reference
description: "Aprende a utilizar la Variante Ganadora o la Variante Personalizada al crear pruebas multivariantes y A/B."
---

# Optimizar las pruebas A/B con variantes ganadoras o personalizadas

Al [crear una prueba A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/) para campañas de correo electrónico, push, webhook, SMS y WhatsApp programadas para enviar una vez, puedes seleccionar una optimización. Hay dos opciones de optimización: **Variante ganadora** y **variante personalizada**.

\![Opciones de optimización enumeradas en la sección Pruebas A/B al elegir tu audiencia objetivo. Hay tres opciones: Sin optimización, Variante ganadora y Variante personalizada. Se selecciona la variante de personalización.]({% image_buster /assets/img_archive/ab_personalized_variant.png %})

Ambas opciones funcionan enviando una prueba inicial a un porcentaje de tu segmento objetivo. Una vez finalizada la prueba, a los usuarios restantes de tu audiencia se les envía la variante con mejor rendimiento (Variante Ganadora) o la variante con la que es más probable que interactúen (Variante Personalizada).

{% alert tip %}
Las optimizaciones se encuentran en el paso **Audiencias objetivo** de la creación de campaña, en **Pruebas A/B**.
{% endalert %}

## Variante ganadora

Enviar la variante ganadora es similar a una prueba A/B estándar. Los usuarios de este grupo recibirán la variante ganadora cuando finalice la prueba inicial.

1. Selecciona Variante **ganadora** y, a continuación, especifica qué porcentaje de la audiencia de tu campaña debe asignarse al grupo Variante ganadora.
2. Configura las siguientes configuraciones adicionales.

| Campo | Descripción |
| --- | --- | 
| Determinar la variante ganadora | La métrica que hay que optimizar. Elige entre *Unique Opens* o *Clics* para correo electrónico, *Aperturas* para push, o *Tasa de conversión primaria* para todos los canales. Seleccionar *Aperturas* o *Clics* para determinar el ganador no afecta a lo que elijas para los eventos de conversión de la campaña. <br><br>Ten en cuenta que si utilizas un grupo de control, los usuarios del grupo de control no pueden realizar *Aperturas* ni *Clics*, por lo que el rendimiento del grupo de control está garantizado `0`. Como resultado, el grupo de control no puede ganar la prueba A/B. Sin embargo, es posible que quieras utilizar un grupo de control para hacer un seguimiento de otras métricas para los usuarios que no reciben un mensaje. |
| Hora de envío de la variante ganadora | La fecha y hora de envío de la variante ganadora. |
| Si no se puede determinar una variante ganadora | Qué ocurre si ninguna variante gana por un margen estadísticamente significativo. Elige entre enviar de todos modos la variante con mejor rendimiento, o finalizar la prueba y no enviar más mensajes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Variante personalizada

Utiliza variantes personalizadas para enviar a cada usuario de tu segmento objetivo la variante con la que es más probable que interactúe.

Para determinar la mejor variante para cada usuario, Braze enviará una prueba inicial a una parte de tu audiencia objetivo para buscar asociaciones entre las características del usuario y las preferencias de mensajes. En función de cómo respondan los usuarios a cada variante en la prueba inicial, estas características se utilizan para determinar qué usuarios restantes obtendrán cada variante. Si no se encuentran asociaciones y no se pueden realizar personalizaciones, la variante ganadora se envía automáticamente a los usuarios restantes. Para saber más sobre cómo se determinan las variantes personalizadas, consulta los [análisis de las pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#personalized-variant).

1. Selecciona Variante **personalizada** y, a continuación, especifica qué porcentaje de la audiencia de tu campaña debe asignarse al grupo Variante personalizada.
2. Configura las siguientes configuraciones adicionales.

| Campo | Descripción |
| --- | --- | 
| Determinar variante personalizada | La métrica que hay que optimizar. Elige entre *Unique Opens* o *Clics* para correo electrónico, *Aperturas* para push, o *Tasa de conversión primaria* para todos los canales. Seleccionar *Aperturas* o *Clics* para determinar el ganador no afecta a lo que elijas para los eventos de conversión de la campaña. <br><br>Ten en cuenta que si utilizas un grupo de control, los usuarios del grupo de control no pueden realizar *Aperturas* ni *Clics*, por lo que el rendimiento del grupo de control está garantizado `0`. Como resultado, el grupo de control no puede ganar la prueba A/B. Sin embargo, es posible que quieras utilizar un grupo de control para hacer un seguimiento de otras métricas para los usuarios que no reciben un mensaje. |
| Hora de envío de la variante personalizada | La fecha y hora de envío de la variante personalizada. |
| Si no se puede determinar una variante personalizada | Qué ocurre si no se encuentran variantes personalizadas. Elige entre enviar la variante ganadora en su lugar, o finalizar la prueba y no enviar más mensajes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Análisis

Para conocer los resultados de tu prueba A/B con una optimización, consulta [Análisis de pruebas multivariantes y A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/).

