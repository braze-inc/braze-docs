---
nav_title: Julio
page_order: 6
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de julio de 2019."
---

# Julio de 2019

{% alert update %}
Braze ha tenido dos (has leído bien, **dos)** ciclos de lanzamiento de productos este mes. La última versión está anotada en la parte superior, ¡la anterior [empieza más abajo en esta página](#earlier-this-month)!
{% endalert %}

## SAML/SSO

[El inicio de sesión único]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/) (SSO) proporciona a las empresas una forma segura y centralizada de controlar el acceso al panel Braze. En resumen, se puede utilizar un único conjunto de credenciales para acceder a diferentes aplicaciones, incluida Braze.

Además de la compatibilidad de [Google Sign-In con OAuth 2.0](https://developers.google.com/identity/protocols/OAuth2), a las empresas les gustaría que SSO fuera compatible con Security Assertion Markup Language (SAML). Esto les habilita para integrarse fácilmente con grandes proveedores de identidad (IdP), como [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/) y [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/), que admiten los últimos estándares del sector (SAML 2.0).

Soportes de Braze:
- [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)
- [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/)
- [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)

## Se muestra la clave de API de evento de Adjust

Hemos actualizado la página del socio de Adjust para que los clientes puedan acceder a esta clave de API.

## Nuevos socios

¡Algunos socios nuevos se unieron a nuestro programa Alloys y se agregaron a nuestra documentación! Saluda a
- [Fivetran]({{site.baseurl}}/partners/fivetran/)
- [Talon.One]({{site.baseurl}}/partners/talonone/)
- [Voucherify]({{site.baseurl}}/partners/voucherify/)

## Mejora de los detalles de la campaña

Los detalles ampliados de la campaña se muestran ahora en la sección ... espera...**¡Detalles de la campaña** de la Página de **Campaña**!

## Mostrar sólo mina en segmentos y Canvas

El filtro "Mostrar sólo la mía" de la página de **campañas** ha demostrado ser muy popular. Como resultado, ¡también vamos a añadir esta opción a las listas de Canvas y Segmento!

### Comportamiento de avance

Ahora puedes elegir [cuándo un usuario avanza]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) de un paso en Canvas al siguiente. Estas opciones incluyen "Mensaje enviado" y "Toda la audiencia tras el retraso".

### Mensajes dentro de la aplicación en Canvas

¡[Los mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/) ya están disponibles en Canvas! Añade un paso en Canvas y explora los canales disponibles para añadir un mensaje dentro de la aplicación.

# A principios de este mes

## Eliminación de la imagen del perfil de usuario

Estamos eliminando las fotos de perfil de usuario que aparecen en los perfiles de usuario de Braze y en las búsquedas de usuarios.

## Contenido conectado en tarjetas de contenido

Ahora puedes utilizar cadenas y funciones de [Contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) en las [tarjetas de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/).

Las llamadas de Contenido conectado a servidores externos se producirán cuando se envíe realmente una tarjeta, no cuando el usuario vea la tarjeta. Al igual que en el correo electrónico, el contenido dinámico se calculará y determinará en el momento del envío, y no cuando se visualice realmente una tarjeta.

## Dirección "responder a" nula

Ahora los clientes pueden establecer un valor `null` para la dirección "responder a" de un mensaje de correo electrónico desde la página **Configuración de correo electrónico** en Braze o utilizando la [API]({{site.baseurl}}/api/endpoints/messaging/#email-object-specification).  Si se utiliza, las respuestas se enviarán a la dirección "De" indicada.  Ahora puedes personalizar el campo de dirección "De" como `dan@emailaddress.com`, y tus clientes podrán responder directamente a Dan.

Para establecer un valor `null` para la dirección "responder a" de un mensaje electrónico de Braze, ve a **Administrar configuración** en la navegación y, a continuación, a la pestaña **Configuración de correo electrónico**. Desplázate hasta la sección **Configuración del correo electrónico saliente** y selecciona **Excluir "Responder a" y enviar las respuestas a "De"** como dirección predeterminada.

## Comparaciones de campañas

Mira [varias campañas a la vez para comparar su rendimiento relativo]({{site.baseurl}}/report_builder/), una al lado de la otra en Braze, ¡en una sola ventana!

## Plantilla del ID de envío en mensajes con Liquid

{% alert note %}
El comportamiento para `dispatch_id` difiere entre Canvas y las campañas porque Braze trata los pasos en Canvas (excepto los pasos de entrada, que pueden programarse) como eventos desencadenados, incluso cuando están "programados". Más información sobre [el comportamiento de`dispatch_id` ]({{site.baseurl}}/help/help_articles/data/dispatch_id/) en Lienzos y campañas.
{% endalert %}

Si quieres hacer un seguimiento del envío de un mensaje desde dentro del mensaje (en una URL, por ejemplo), puedes utilizar la plantilla `dispatch_id`. Puedes encontrar el formato para ello en nuestra lista de etiquetas de personalización compatibles, en [Atributos de Canvas]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

Esto se comporta igual que `api_id`, en el sentido de que como `api_id` no está disponible en el momento de crear la campaña, se incluye en la plantilla como marcador de posición y se previsualizará como `dispatch_id_for_unsent_campaign`. El ID se genera antes de enviar el mensaje, y se incluirá en la hora de envío.

{% alert warning %}
La plantilla Liquid de `dispatch_id_for_unsent_campaign` no funciona con los mensajes dentro de la aplicación, ya que los mensajes dentro de la aplicación no tienen `dispatch_id`.
{% endalert %}

## La configuración "Mostrar sólo la mía" persiste

El filtro "Mostrar sólo las mías" de la parrilla de campañas permanecerá activado siempre que visites la página **Campañas**.

## Actualizaciones de las pruebas A/B

Puedes enviar una única [prueba A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) con hasta ocho variantes (y un control opcional) a un porcentaje especificado por el usuario de la audiencia de una campaña, y luego enviar la mejor variante a la audiencia restante a una hora programada previamente.
