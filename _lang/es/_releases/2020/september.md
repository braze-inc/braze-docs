---
nav_title: Septiembre
page_order: 4
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de septiembre de 2020."
---

# Septiembre

## Informe de embudo

El informe de embudo te ofrece un informe visual que te permite analizar los recorridos que realizan tus clientes tras recibir una [campaña]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/) o [Canvas]({{site.baseurl}}/user_guide/analytics/reporting/funnel_reports/).

## Guía de actualización a iOS 14

De acuerdo con los cambios anunciados en el nuevo iOS 14 de Apple, hay algunos cambios relacionados con Braze y elementos de acción necesarios para las integraciones del SDK de Braze para iOS. Para más información, echa un vistazo a esta [guía de actualización]({{site.baseurl}}/ios_14/).

## Cambios en IDFA e IDFV para iOS 14

En iOS 14, los usuarios deben decidir si quieren la adhesión voluntaria al seguimiento de anuncios y dejar que las aplicaciones y las redes publicitarias lean su IDFA cuando visiten una aplicación. Como resultado, la estrategia de Braze es utilizar en su lugar el "identificador para vendedores" (como IDFV) para que puedas seguir haciendo un seguimiento de los usuarios en diferentes dispositivos. Para más información, echa un vistazo a la [guía de actualización a iOS 14]({{site.baseurl}}/ios_14/).

## Validación del correo electrónico

Este nuevo proceso de validación de la sintaxis del correo electrónico es una mejora del existente en Braze. Se trata de una comprobación para verificar que los correos electrónicos actualizados o importados en Braze son correctos. Para más información, echa un vistazo a [estas directrices y notas]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/).

## Evento de usuario de contenedor aleatorio en Currents

El número de contenedor aleatorio (como RBN) se produce cada vez que se crea un nuevo usuario dentro de su espacio de trabajo. Durante este evento, a cada nuevo usuario se le asigna un número de contenedor aleatorio que puedes utilizar para crear segmentos de usuarios aleatorios distribuidos uniformemente. Utilízalo para agrupar una serie de valores de números de contenedor aleatorios y comparar el rendimiento de tus campañas y variantes de campaña. Para ver si este evento está disponible para ti, echa un vistazo al [glosario de eventos de comportamiento del cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) de Currents.

## Componentes de Canvas - ¡Próximamente!

Braze ha añadido cuatro nuevos componentes Canvas para ayudarte a aumentar la flexibilidad y funcionalidad de tus Canvas. Estos nuevos componentes incluyen: [Paso para la división de decisiones]({{site.baseurl}}/decision_split/), [paso para el retraso]({{site.baseurl}}/delay_step/), [pasos para la mensajería]({{site.baseurl}}/message_step/) y [sincronización de la audiencia con Facebook]({{site.baseurl}}/audience_sync_facebook/).
- **Pasos para la división de decisiones, retraso y mensajería en Canvas**<br>Las divisiones de decisiones pueden utilizarse para crear ramas de Canvas en función de si un usuario coincide con una consulta definida. Los pasos de retraso te permiten añadir un retraso independiente a tu Canvas sin necesidad de un mensaje correspondiente. Los pasos de mensajería te permiten añadir un mensaje independiente donde quieras en tu flujo de Canvas.
- **Sincronización de audiencias con Facebook**<br>Mediante la Sincronización de Audiencias Braze con Facebook, las marcas pueden optar por añadir los datos de sus propios usuarios desde su propia integración Braze a las Audiencias Personalizadas de Facebook para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más. Cualquier criterio que utilices normalmente para desencadenar un mensaje (push, correo electrónico, SMS, webhook, etc.) en un Canvas de Braze basado en tus datos de usuario puede utilizarse ahora para desencadenar un anuncio dirigido a ese usuario en Facebook a través de Públicos personalizados.

## Eventos recibidos de SMS entrantes

Se ha añadido un nuevo evento de interacción de mensajería a Currents. Este evento se produce cuando uno de tus usuarios envía un SMS a un número de teléfono de uno de tus grupos de suscripción a Braze SMS. Para más información, consulta nuestro [glosario de mensajería y eventos de interacción]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) de Currents.
