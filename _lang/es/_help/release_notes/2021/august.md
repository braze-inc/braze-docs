---
nav_title: Agosto
page_order: 4
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de agosto de 2021."
---

# Agosto de 2021

## Sincronización de audiencias de Google

La integración de Braze [de sincronización de audiencia con Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/) permite a las marcas ampliar el alcance de sus recorridos de clientes multicanal a Google Search, Google Shopping, Gmail, YouTube y Google Display. Utilizando tus datos de clientes propios, puedes entregar de forma segura anuncios basados en desencadenantes dinámicos de comportamiento, segmentación y mucho más. Cualquier criterio que utilices normalmente para desencadenar un mensaje (por ejemplo, push, correo electrónico, SMS, etc.) como parte de un Canvas de Braze puede utilizarse para desencadenar un anuncio dirigido a ese usuario a través de Customer Match de Google.

## Guía de buenas prácticas para la integración de SDK de iOS

Esta [guía del SDK de integración de iOS]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift#swift_integrating-the-swift-sdk) opcional te lleva paso a paso por las mejores prácticas de configuración a la hora de integrar por primera vez el SDK de iOS y sus componentes principales en tu aplicación. Esta guía te ayudará a crear un archivo de ayuda `BrazeManager.swift` que desacoplará cualquier dependencia del SDK Braze para iOS del resto de tu código de producción, dando como resultado un `import AppboyUI` en toda tu aplicación. Este enfoque limita los problemas que surgen de un exceso de importaciones del SDK, lo que facilita el seguimiento, la depuración y la modificación del código. 

## Compras predictivas

Las compras predictivas proporcionan a los especialistas en marketing una potente herramienta para identificar y enviar mensajes a los usuarios en función de su probabilidad de realizar una compra. Cuando creas una predicción de compra, Braze entrena un modelo de aprendizaje automático mediante [árboles de decisión potenciados por gradiente](https://en.wikipedia.org/wiki/Gradient_boosting) para aprender de la actividad de compra anterior y predecir la actividad de compra futura. Visita nuestro documento [Compras predictivas]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events/) para saber más. 

## Editor de arrastrar y soltar

Con Braze Email, puedes crear mensajes de correo electrónico completamente personalizados en campañas o Canvas utilizando nuestra nueva [experiencia de edición arrastrar y soltar]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/). Ahora los usuarios pueden arrastrar bloques de editor a sus correos electrónicos, lo que permite una personalización más intuitiva. 

## Importación de alias de usuarios

Para dirigirte a usuarios que no tienen un `external_id`, puedes [importar una lista de usuarios con alias de usuario]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#import-with-user-alias). Un alias sirve como identificador único alternativo del usuario. Puede ser útil si intentas dirigirte a usuarios anónimos que no se han registrado ni creado una cuenta en tu aplicación. 

## Guía de actualización a iOS 15

Esta [guía de actualización a iOS 15]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/) describe los cambios introducidos en iOS 15 (WWDC21) y los pasos de actualización necesarios para tu integración de SDK de Braze iOS.

## Guía de actualización a Android 12

Esta [guía de actualización a Android 12]({{site.baseurl}}/developer_guide/platforms/android/android_13/) describe los cambios relevantes introducidos en Android 12 (2021) y los pasos de actualización necesarios para tu integración de SDK de Android Braze.

## A2P 10DLC

A2P 10DLC hace referencia a un sistema de Estados Unidos que permite a las empresas enviar mensajería del tipo Aplicación a Persona (A2P) a través de un número de teléfono estándar de código largo de 10 dígitos (10DLC). Los códigos largos de 10 dígitos se han diseñado tradicionalmente para el tráfico de Persona a Persona (P2P), por lo que las empresas se ven constreñidas por un rendimiento limitado y un mayor filtrado. Este servicio ayuda a aliviar esos problemas, mejorando la capacidad de entrega de mensajes en general, permitiendo a las marcas enviar mensajes a escala, incluyendo enlaces y llamadas a la acción, y ayudando a proteger aún más a los consumidores de mensajes no deseados. 

Todos los clientes que actualmente tengan y/o utilicen códigos largos de EE.UU. para enviar a clientes de EE.UU. deben registrar sus códigos largos para 10DLC. Para saber más sobre los detalles del 10DLC y por qué es necesario, visita nuestro [artículo dedicado al 10DLC]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/10dlc/).

## Restablecimiento de autenticación de dos factores

Los usuarios que tengan problemas para iniciar sesión mediante la autenticación de dos factores pueden ponerse en contacto con los administradores de su empresa para [restablecer la autenticación de dos factores]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#user-authetication-reset).

## Nuevas asociaciones Braze

### Hightouch - Automatización del flujo de trabajo

La integración de Braze y [Hightouch]({{site.baseurl}}/partners/data_and_analytics/reverse_etl/hightouch/) te permite crear mejores campañas en Braze con datos de clientes actualizados de tu almacén de datos. Quieres proporcionar interacciones relevantes y oportunas a tus clientes, y hacerlo depende en gran medida de que los datos de tu cuenta Braze sean precisos y estén actualizados. Al sincronizar automáticamente los datos de clientes de tu almacén de datos con Braze, ya no tienes que preocuparte por la coherencia de los datos, y puedes centrarte en crear experiencias del cliente de primera clase.

### Transcend - Privacidad de datos y cumplimiento

La asociación entre Braze y [Transcend]({{site.baseurl}}/partners/ecommerce/payments/transcend/) ayuda a los usuarios a automatizar las peticiones de privacidad mediante la orquestación de datos en docenas de sistemas de datos. En última instancia, esto ayuda a los equipos a cumplir normativas como el RGPD y la CCPA, y pone a las personas al mando cuando se trata de sus datos.

### Tinyclues - Importación de cohortes

[Tinyclues]({{site.baseurl}}/partners/data_and_analytics/cohort_import/tinyclues/) es una característica de creación de audiencia que ofrece la capacidad de aumentar el número de campañas y los ingresos sin perjudicar la experiencia del cliente, y análisis para seguir el rendimiento de las campañas de CRM tanto online como offline. Juntas, la integración de Braze y Tinyclues ofrece a los usuarios un camino hacia una mejor planificación y estrategia de CRM, permitiendo a los usuarios enviar más campañas de segmentación, encontrar nuevas oportunidades de productos y elevar los ingresos mediante una interfaz de usuario increíblemente fácil de usar.

### optilyz - Correo directo

[optilyz]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/optilyz/) es una plataforma de automatización del correo directo que te permite realizar campañas de correo directo más centradas en el cliente, sostenibles y rentables. optilyz es utilizada por cientos de empresas de toda Europa y te habilita para integrar cartas, postales y autoenvíos en tu marketing de canales cruzados y automatizar y personalizar mejor las campañas. Utiliza la integración de Optilyz y Braze webhook para enviar correo directo a tus clientes.