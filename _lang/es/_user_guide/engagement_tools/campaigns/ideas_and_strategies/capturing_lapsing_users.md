---
nav_title: Capturar usuarios rezagados
article_title: Capturar usuarios rezagados
page_order: 1
page_type: tutorial
description: "En este artículo de instrucciones se aborda el problema de los usuarios que abandonan y cómo utilizar eficazmente las campañas Braze para reactivar a esos usuarios."
tool:
  - Segments
  - Campaigns

---

# Capturar usuarios rezagados

> Si tu audiencia está disminuyendo, es crucial que intentes atraerla de nuevo. Con Braze, puedes configurar campañas de reactivación de la interacción recurrentes y automatizadas para captar a los usuarios rezagados. Puedes elegir el plazo de reactivación de la interacción y la recurrencia que mejor se adapten a tu aplicación, pero para demostrarlo, empezaremos con un plan de reactivación de 14 días.

Para obtener más información sobre la segmentación de usuarios, consulte nuestro [curso Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuración de campañas.

## Paso 1: Segmentar usuarios

En primer lugar, crearemos un segmento para dirigirnos a los usuarios que no han utilizado tu aplicación en las últimas dos semanas, utilizando los siguientes filtros:

- **Usó la aplicación por última vez** hace más de 2 semanas
- **Usó la aplicación por última vez** hace menos de 3 semanas

![]({% image_buster /assets/img_archive/2weeklapse1.png %}){: style="max-width:70%;"}

Nombra el segmento con algo memorable, como "Usuarios caducados - 2 semanas". Como estamos configurando la campaña para que se repita semanalmente, queremos asegurarnos de que hay al menos una semana de usuarios capturados en el segmento. Por eso hemos seleccionado usuarios que utilizaron la aplicación por última vez hace entre dos y tres semanas.

## Paso 2: Crear una campaña

A continuación, haz clic en **Crear campaña** y elige el tipo de campaña que enviaremos a este segmento. en este ejemplo, crearemos una nueva [campaña push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message).

![]({% image_buster /assets/img_archive/2weeklapse2.png %}){: style="max-width:70%;"}

Llamaremos a la campaña "Mensaje a usuarios rezagados - 2 semanas" y a continuación crearemos el contenido de nuestro mensaje. En este ejemplo, sólo nos dirigiremos a los usuarios de iOS, pero puedes utilizar Braze para las notificaciones push de Android e iOS. 

Cuanto más cerca de la última vez que un usuario estuvo en la aplicación, más importante es que sea actual y relevante. Cuando se envía un mensaje a un usuario después de dos semanas sin usar la aplicación, es importante presentar contenido relevante y destacar las ventajas de usarla.

![]({% image_buster /assets/img_archive/2weeklapse3.png %}){: style="max-width:70%;"}

A continuación, crearemos una programación recurrente para enviar nuestro mensaje semanal los jueves a las 17:45 utilizando la [entrega según la zona horaria local]({{site.baseurl}}/help/faqs/#what-does-local-time-zone-delivery-offer) en **las Opciones de programación en función de la hora**. Le recomendamos que observe su gráfico de sesiones para dirigirse a los usuarios justo antes de los periodos de mayor uso. De este modo, intentará volver a captar la atención de los usuarios cuando sea más probable que utilicen la aplicación. Puedes modificarlo más adelante y poner a prueba tu hipótesis inicial.

![]({% image_buster /assets/img_archive/2weeklapse4.png %}){: style="max-width:70%;"}

## Paso 3: Lanzar la campaña

Ahora, ya está listo para enviar la campaña. Confirme la configuración en la última página del compositor y haga clic en **¡Lanzar campaña**!

