---
nav_title: Facebook
article_title: Exportación de audiencias de Facebook
alias: /partners/facebook/
description: "Este artículo de referencia describe la asociación entre Braze y Facebook, una plataforma social líder para que las marcas lleguen a sus clientes y se relacionen con ellos."
page_type: partner
search_tag: Partner

---

# Exportación de audiencias de Facebook

> La integración de Braze y Facebook te permite exportar manualmente tus segmentos de Braze a Facebook para crear públicos personalizados de Facebook. Se trata de una exportación de público única y estática, y sólo creará nuevos públicos personalizados de Facebook.

Los casos de uso más comunes para exportar públicos personalizados de Facebook incluyen
- Reorientar a los usuarios en puntos específicos de su ciclo de vida
- Creación de listas de exclusión
- Creación de [audiencias similares][4] para captar nuevos usuarios de forma más eficaz
<br><br>

{% alert note %}
La exportación de público de Facebook utiliza el **token de acceso de usuario** para autorizar las solicitudes.<br><br>
Si utiliza esta función junto con la función [Sincronización de público con Facebook]({{site.baseurl}}/audience_sync_facebook/), Braze utilizará por defecto el **token de usuario del sistema** más fiable que ya ha generado para autorizar las solicitudes.
{% endalert %}

{% alert note %}
Si estás participando en las pruebas de las cuentas de Meta Work en versión beta, asegúrate de desconectar y volver a conectar tu cuenta a la [página asociada de Facebook]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#step-1-connect-to-facebook).
{% endalert %}

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| [Facebook Business Manager][1] | Una herramienta centralizada para gestionar los activos de Facebook de tu marca (por ejemplo, cuentas de anuncios, páginas, aplicaciones). |
| [Cuenta publicitaria en Facebook][2] | Una cuenta de anuncios de Facebook activa vinculada al administrador de empresas de tu marca que quieras utilizar con los públicos personalizados de Braze.<br><br>Asegúrate de que el administrador de tu empresa en Facebook te ha concedido permisos de administrador para las cuentas de anuncios de Facebook que piensas utilizar con Braze, y de que has aceptado los términos y condiciones de tu cuenta de anuncios. De lo contrario, no podrás acceder a ninguna cuenta de anuncios de Facebook dentro de Braze. |
| [Términos de los públicos personalizados de Facebook][3]| Debes aceptar las Condiciones de públicos personalizados de Facebook para las cuentas de anuncios de Facebook que pienses utilizar con Braze.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Conéctate a Facebook

1. En el panel de control de Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Facebook**. 

{% alert note %}
Si utiliza la [navegación anterior]({{site.baseurl}}/navigation), encontrará a **los socios tecnológicos** en **Integraciones**.
{% endalert %}

{: start="2"}
2\. En el módulo Exportar audiencia de Facebook, selecciona **Conectar Facebook**. <br><br>![Página de socios tecnológicos de Facebook en la plataforma Braze.][6]{: style="max-width:70%;"}

{: start="3"}
3\. En la ventana de diálogo oAuth de Facebook, autoriza a Braze a crear Públicos personalizados en tus cuentas de anuncios de Facebook. <br><br>![El primer cuadro de diálogo de Facebook te pide "Conectarte como X", donde X es tu nombre de usuario de Facebook.][8]{: style="max-width:30%;"}  ![El segundo cuadro de diálogo de Facebook que solicita permiso para gestionar los anuncios de tus cuentas publicitarias.][7]{: style="max-width:40%;"}

{: start="4"}
4\. Una vez que Braze esté vinculado a tu cuenta de Facebook, selecciona las cuentas de anuncios que deseas sincronizar en tu espacio de trabajo Braze. <br><br>![Una lista de las cuentas de anuncios disponibles que puedes conectar a Facebook.][9]{: style="max-width:70%;"}<br><br> Después de conectarse, volverá a la página de socios, donde podrá ver qué cuentas están conectadas y desconectar las existentes. <br><br> ![Una versión actualizada de la página de socios tecnológicos de Facebook que muestra las cuentas de anuncios conectadas correctamente.][10]{: style="max-width:70%;"}<br>
<br> Tu conexión a Facebook se aplica a nivel del espacio de trabajo Braze. Si tu administrador de Facebook te elimina de tu Facebook Business Manager o del acceso a las cuentas de Facebook conectadas, Braze detectará un token no válido. Como resultado, tus Canvases activos que utilicen pasos de audiencia de Facebook mostrarán errores y Braze no podrá sincronizar usuarios. 

{% alert important %}
Para los clientes que hayan pasado previamente por el proceso de revisión de la aplicación de Facebook para [Gestión de anuncios](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) y [Acceso estándar a Gestión de anuncios](https://developers.facebook.com/docs/marketing-api/access#standard), su token de usuario del sistema seguirá siendo válido para el paso de audiencia de Facebook. No podrás editar ni revocar el token de usuario del sistema de Facebook a través de la página de socio de Facebook. En su lugar, puedes conectar tu cuenta de Facebook para sustituir tu token de usuario del sistema de Facebook dentro de tu espacio de trabajo Braze. 

<br><br>La nueva configuración de Facebook oAuth también se aplicará a las [exportaciones de Facebook a través de segmentos]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites).
{% endalert %}

### Paso 2: Exporta tus usuarios a Facebook

En Braze, se puede acceder a la exportación de público de Facebook a través de la página **Segmentos**. 

1. En la página **Segmentos**, selecciona el segmento que deseas exportar.
2. Selecciona **Datos de usuario** y, a continuación, **Exportar como audiencia de Facebook**. <br><br>![La sección "Detalles del segmento" de un segmento con "Datos de usuario" seleccionados para mostrar un desplegable de opciones que incluye "Exportar como audiencia de Facebook".][11]

{: start="3"}
3\. Si aún no has activado Facebook en Braze, se te pedirá que vayas a la página de socios tecnológicos de Facebook en el panel. Si ya has activado Facebook a través de **Socios tecnológicos** > **Facebook**, podrás seleccionar tu cuenta de anuncios de Facebook y los campos de usuario para exportar. <br><br> Hay tres posibles campos de usuario que puede exportar:
- Identificador para anunciantes (IDFA) del dispositivo
- Número de teléfono 
- Correo electrónico

{% alert note %}
Sólo puede seleccionar un campo de usuario en una única exportación. Si elige más de un tipo de datos, Braze creará un público personalizado distinto para cada uno.
{% endalert %}

{: start="4"}
4\. Después de seleccionar el campo del usuario, selecciona **Exportar segmento**. Al igual que las exportaciones CSV, recibirás un correo electrónico cuando el segmento haya terminado de exportarse a Facebook.
5\. Ver el público personalizado en el [Facebook Ads Manager][13].

{% alert important %}
Por motivos de privacidad de los usuarios, Facebook no te permite ver:

- Los usuarios exactos que se han añadido correctamente a un público personalizado. [Más información.](https://www.facebook.com/business/help/112061095610075)
- El tamaño de la audiencia personalizada. [Más información.](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923)
{% endalert %}

#### Configuración de la exportación de público

Al crear audiencias de Facebook, es posible que desees incluir o excluir a determinados usuarios en función de sus preferencias y para cumplir con las leyes de privacidad, como el derecho de "No vender ni compartir" en virtud de la [CCPA](https://oag.ca.gov/privacy/ccpa). Los vendedores deben implementar los filtros pertinentes para la elegibilidad de los usuarios dentro de sus criterios de entrada en Canvas. A continuación enumeramos algunas opciones. 

- Si has recopilado el [IDFA de iOS a través del SDK de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), podrás utilizar el filtro **Ads Tracking Enabled**. Selecciona el valor como `true` para enviar sólo a los usuarios a los destinos de Audience Sync en los que hayan optado por la adhesión voluntaria. 

![][16]{: style="max-width:75%;"}

- Si está recopilando opt ins, opt outs, `Do Not Sell Or Share`, u otros atributos personalizados relevantes, debe incluirlos dentro de sus criterios de entrada de Canvas como un filtro: 

![Un Canvas con un público de entrada "opted_in_marketing" es igual a "true".][15]{: style="max-width:75%;"}


#### Audiencias similares

Una vez que hayas exportado correctamente un segmento como público de Facebook, puedes crear grupos adicionales utilizando [públicos similares][4] de Facebook. Esta función examina los datos demográficos, los intereses y otros atributos de la audiencia elegida y crea una nueva audiencia de personas con atributos similares.

[1]: https://www.facebook.com/business/help/113163272211510?id=180505742745347
[2]: https://www.facebook.com/business/help/910137316041095?id=420299598837059
[3]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[4]: https://www.facebook.com/business/help/164749007013531?id=401668390442328
[6]: {% image_buster /assets/img/fb/afb_1.png %}
[7]: {% image_buster /assets/img/fb/afb_2.png %}
[8]: {% image_buster /assets/img/fb/afb_3.png %}
[9]: {% image_buster /assets/img/fb/afb_4.png %}
[10]: {% image_buster /assets/img/fb/afb_5.png %}
[11]: {% image_buster /assets/img/fb/afb_6.png %}
[13]: https://www.facebook.com/ads/manager/audiences/manage/
[15]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
