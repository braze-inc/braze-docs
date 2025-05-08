---
nav_title: Resumen
article_title: Resumen
description: "En este artículo de referencia se explica cómo utilizar Braze Audience Sync con Facebook para enviar anuncios basados en desencadenantes de comportamiento, segmentación, etc."
page_order: 0
Tool:
  - Canvas

---

# Resumen de la sincronización de la audiencia

> La característica Braze Audience Sync te ayuda a ampliar el alcance de tus campañas a muchas de las principales tecnologías sociales y publicitarias. A través de [Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas), las marcas pueden sincronizar de forma dinámica y segura datos de usuarios de primera mano en el ecosistema publicitario para impulsar el marketing y la eficiencia operativa.

## Casos prácticos

- Dirigirse a usuarios de alto valor a través de canales propios y de pago para aumentar las compras o la participación.
- Creación de audiencias similares de sus usuarios de alto valor para optimizar los costes de adquisición de nuevos usuarios y las conversiones.
- Reorientar a los usuarios con anuncios que son menos receptivos a otros canales de marketing.
- Crear audiencias de supresión para evitar que los usuarios reciban anuncios cuando ya son consumidores fieles de su marca.

## Disponibilidad de características

Todos los clientes de Braze tendrán acceso inmediato a la Sincronización de Audiencias con Google y Facebook. Para desbloquear destinos adicionales de Audience Sync, como TikTok, Pinterest, Snapchat o Criteo, tendrás que comprar Audience Sync Pro. Póngase en contacto con su gestor de cuentas Braze para obtener más información.

## Cómo funciona

Para utilizar Audience Sync con Google o Facebook, conecta tu cuenta de anuncios buscando al socio en la página de **socios tecnológicos**.

![][3]{: style="max-width:35%;"} ![][4]{: style="max-width:35%;"}

Después de conectar tu cuenta de anuncios, puedes crear un Canvas con un paso de Sincronización de Audiencia.

![][22]{: style="max-width:75%;"}

A continuación, selecciona el socio para sincronizar audiencias.

![][19]{: style="max-width:85%;"}

Para cada socio, tendrás que configurar lo siguiente como parte del paso de sincronización de audiencias: 
- Cuenta publicitaria
- Audiencia 
- Acción de añadir o eliminar usuarios 
- Campos que deben coincidir 

Tenga en cuenta que Braze sincronizará a los usuarios en cuanto entren en el paso Sincronización de público dentro de su Canvas. 

Para cada destino de la Sincronización de Audiencias, el socio puede tener diferentes requisitos sobre los campos que podemos enviar. Consulta la documentación específica del socio para más detalles. 

### Audience Sync Pro

Para utilizar un socio de Audience Sync Pro, como TikTok, Pinterest, Snapchat o Criteo, podrás seleccionar tus socios en función de tus asignaciones de compra de Audience Sync Pro en la sección **Audience Sync Pro** de la página de **socios tecnológicos**.

![][5]{: style="max-width:75%;"}

Primero, selecciona los socios que pretendes utilizar seleccionando Seleccionar socios. Cada compra de Audience Sync Pro te proporcionará 3 destinos asignados de Audience Sync Pro, que estarán disponibles en cada uno de tus espacios de trabajo dentro de tu panel.

![][6]{: style="max-width:65%;"}

Después de seleccionar tus destinos de Audience Sync Pro, conecta la cuenta de publicidad de tu socio seleccionado haciendo clic en el mosaico de socios.

![][7]{: style="max-width:70%;"}

![][9]{: style="max-width:70%;"}

Por último, crea tu paso en Canvas para la Sincronización de Audiencias utilizando este destino de Audience Sync Pro.

## Consideraciones sobre la privacidad de los datos

{% alert important %}
Esta documentación no pretende ofrecer asesoramiento jurídico ni puede considerarse como tal. El uso de Audience Sync está sujeto a requisitos legales específicos. Para asegurarse de que lo utiliza de conformidad con la legislación vigente, consulte a su asesor jurídico.
{% endalert %}

Al crear audiencias para el seguimiento de anuncios, es posible que desee incluir o excluir a determinados usuarios en función de sus preferencias y para cumplir con las leyes de privacidad, como el derecho de "No vender ni compartir" en virtud de la [CCPA](https://oag.ca.gov/privacy/ccpa). Los vendedores deben implementar los filtros pertinentes para la elegibilidad de los usuarios dentro de sus criterios de entrada en Canvas. A continuación enumeramos algunas opciones.

Si has recogido el [IDFA de iOS a través del SDK de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), podrás utilizar el filtro "Seguimiento de anuncios habilitado". Selecciona el valor como `true` para enviar sólo a los usuarios a los destinos de Audience Sync en los que hayan optado por la adhesión voluntaria.

![][2]

Si está recopilando `opt-ins`, `opt-outs`, `Do Not Sell Or Share`, o cualquier otro atributo personalizado relevante, debe incluirlos dentro de sus criterios de entrada de Canvas como un filtro:

![Un Canvas con un público de entrada "opted_in_marketing" es igual a "true".][1]

Para obtener más información sobre cómo cumplir estas leyes de Protección de Datos dentro de la plataforma Braze, consulte la [Asistencia Técnica sobre Protección de Datos]({{site.baseurl}}/dp-technical-assistance/).

[1]: {% image_buster /assets/img/audience_sync/audience_sync.png %}
[2]: {% image_buster /assets/img/audience_sync/audience_sync2.png %}
[3]: {% image_buster /assets/img/audience_sync/facebook_partner.png %}
[4]: {% image_buster /assets/img/audience_sync/google_ads_partner.png %}
[5]: {% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}
[6]: {% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}
[7]: {% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}
[8]: {% image_buster /assets/img/audience_sync/audience_sync_pro3b.png %}
[9]: {% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/audience_sync6.png %}
[22]: {% image_buster /assets/img/audience_sync/audience_sync7.png %}