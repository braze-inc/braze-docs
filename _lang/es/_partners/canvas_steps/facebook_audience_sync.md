---
nav_title: Facebook
article_title: Sincronización de la audiencia de Canvas con Facebook
description: "En este artículo de referencia se explica cómo utilizar Braze Audience Sync con Facebook para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más."
page_order: 2
alias: "/audience_sync_facebook/"

Tool:
  - Canvas

---

# Sincronización de audiencias con Facebook

Mediante la Sincronización de audiencias de Braze con Facebook, las marcas pueden optar por añadir los datos de sus usuarios desde su propia integración de Braze a Públicos personalizados de Facebook para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más. Cualquier criterio que utilices normalmente para desencadenar un mensaje (push, correo electrónico, SMS o webhook) en un Canvas de Braze basado en tus datos de usuario puede utilizarse ahora para desencadenar un anuncio dirigido a ese usuario en Facebook mediante Audiencias personalizadas.

**Entre los casos de uso habituales para sincronizar audiencias personalizadas se incluyen**:

- Dirigirse a usuarios de alto valor a través de múltiples canales para impulsar las compras o la interacción.
- Reorientar a los usuarios menos receptivos a otros canales de marketing.
- Crear audiencias de supresión para evitar que los usuarios reciban anuncios cuando ya son consumidores fieles de tu marca.
- Crear audiencias similares para captar nuevos usuarios de forma más eficaz.

Esta característica permite a las marcas controlar qué datos propios específicos se comparten con Facebook. En Braze, se presta la máxima atención a las integraciones con las que puedes y no puedes compartir tus datos propios. Para más información, consulta nuestra [política de privacidad](https://www.braze.com/privacy).

## Requisitos previos

Tendrás que confirmar que tienes los siguientes elementos creados y completados antes de configurar tu paso de Facebook Audience en Canvas. 

| Requisito | Origin | Descripción |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook][1] | Una herramienta centralizada para administrar los activos de Facebook de tu marca (por ejemplo, cuentas de anuncios, páginas y aplicaciones). |
| Cuenta publicitaria de Facebook | [Facebook][2] | Una cuenta de anuncios de Facebook activa vinculada al administrador de la empresa de tu marca.<br><br>Asegúrate de que el administrador de tu empresa en Facebook te ha concedido permisos de "Gestionar campañas" o "Gestionar cuentas de anuncios" para las cuentas de anuncios de Facebook que piensas utilizar con Braze. Asegúrate también de que has aceptado los términos y condiciones de tu cuenta publicitaria. |
| Términos de los públicos personalizados de Facebook | [Facebook][3] | Acepta las Condiciones de públicos personalizados de Facebook para las cuentas de anuncios de Facebook que piensas utilizar con Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integración

### Paso 1: Conéctate a Facebook

En el panel de control de Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Facebook**. En Exportar audiencia de Facebook, selecciona **Conectar Facebook**.

{% alert note %}
Si utiliza la [navegación anterior]({{site.baseurl}}/navigation), encontrará a **los socios tecnológicos** en **Integraciones**.
{% endalert %}

![Página de tecnología de Facebook en Braze que incluye una sección de resumen y otra de exportación de la audiencia de Facebook con el botón de Facebook Conectado.][4]{: style="max-width:70%;"}

Aparecerá una ventana de diálogo de Facebook oAuth para autorizar a Braze a crear audiencias personalizadas en tus cuentas de anuncios de Facebook.

![El primer cuadro de diálogo de Facebook te pide "Conectarte como X", donde X es tu nombre de usuario de Facebook.][6]{: style="max-width:30%;"}  ![El segundo cuadro de diálogo de Facebook te pide permiso para administrar los anuncios de tus cuentas publicitarias.][5]{: style="max-width:40%;"}

Una vez que hayas vinculado Braze a tu cuenta de Facebook, podrás seleccionar las cuentas de anuncios que deseas sincronizar dentro de tu espacio de trabajo Braze. 

![Una lista de las cuentas de anuncios disponibles que puedes conectar a Facebook.][7]{: style="max-width:70%;"}

Una vez que te hayas conectado correctamente, volverás a la página del socio, donde podrás ver qué cuentas están conectadas y desconectar las cuentas existentes.

![Una versión actualizada de la página de socios tecnológicos de Facebook que muestra las cuentas de anuncios conectadas correctamente.][8]{: style="max-width:70%;"}

Tu conexión a Facebook se aplicará a nivel del espacio de trabajo Braze. Si tu administrador de Facebook te elimina de tu administrador de empresas de Facebook o del acceso a las cuentas de Facebook conectadas, Braze detectará un token no válido. Como resultado, tus Canvas activos que utilicen componentes de Facebook Audience mostrarán errores, y Braze no podrá sincronizar usuarios. 

{% alert important %}
Para los clientes que hayan pasado previamente por el proceso de revisión de la aplicación de Facebook para la [gestión de anuncios](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) y [el acceso estándar a la gestión de anuncios](https://developers.facebook.com/docs/marketing-api/access#standard), tu token de usuario del sistema seguirá siendo válido para el componente Facebook Audience. No podrás editar ni revocar el token de usuario del sistema de Facebook a través de la página del socio de Facebook. En su lugar, puedes conectar tu cuenta de Facebook para sustituir tu token de usuario del sistema de Facebook dentro de tu espacio de trabajo Braze. 

<br><br>La configuración de Facebook oAuth también se aplicará a las [exportaciones de Facebook a través de Segmentos]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites).
{% endalert %}

### Paso 2: Aceptar las condiciones de servicio de las audiencias personalizadas

Antes de crear tu Canvas, debes aceptar las condiciones de servicio de las audiencias personalizadas de Facebook. Tus condiciones de servicio se encuentran en el siguiente enlace:
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<your_ad_account_id>`

### Paso 3: Añadir un componente de Facebook Audience en Canvas Flow

Añade un componente en tu Canvas y selecciona **Facebook Audience**.

![][18]{: style="max-width:35%;"} ![][20]{: style="max-width:28%;"}

### Paso 4: Configuración de la sincronización

Haz clic en el botón **Audiencia personalizada** para abrir el editor de componentes.

Selecciona **Facebook** como el socio de Audience Sync.

![][19]{: style="max-width:80%;"}

Selecciona la cuenta de anuncios de Facebook deseada. En el desplegable **Elegir una audiencia nueva o existente**, escribe el nombre de una audiencia nueva o existente. 

{% tabs %}
{% tab Crear una nueva audiencia %}
**Crear una nueva audiencia**<br>
Introduce un nombre para la nueva audiencia personalizada, selecciona **Añadir usuarios a la audiencia** y selecciona los campos que deseas sincronizar con Facebook. A continuación, guarda tu audiencia haciendo clic en el botón **Crear audiencia** situado en la parte inferior del editor de pasos.

![]({% image_buster /assets/img/audience_sync/fb_sync.png %})

A continuación, guarda tu audiencia haciendo clic en el botón Crear audiencia situado en la parte inferior del editor de pasos. Se notificará a los usuarios en la parte superior del editor de pasos si la audiencia se ha creado correctamente o si surgen errores durante este proceso. Los usuarios también pueden hacer referencia a este público para la eliminación de usuarios más adelante en el recorrido Canvas, ya que el público se creó en modo borrador.

![]({% image_buster /assets/img/audience_sync/fb_sync2.png %})

Cuando lances un Canvas con una nueva audiencia, Braze creará la nueva audiencia personalizada al lanzar el Canvas y, posteriormente, sincronizará a los usuarios casi en tiempo real cuando entren en el paso en Canvas de sincronización de audiencias.

{% endtab %}
{% tab Sincronización con un público existente %}
**Sincronización con una audiencia existente**<br>
Braze también ofrece la posibilidad de añadir o eliminar usuarios de las audiencias personalizadas de Facebook existentes para confirmar que estas audiencias están actualizadas. Para sincronizar con una audiencia existente, escribe el nombre de la audiencia existente en el desplegable y elige si quieres **Añadir a la audiencia** o **Eliminar de la audiencia**. A continuación, Braze añadirá o eliminará usuarios casi en tiempo real a medida que entren en el paso de Facebook Audience. 

![]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

Es importante tener en cuenta que Facebook prohíbe eliminar usuarios de audiencias personalizadas cuando el tamaño de la audiencia es demasiado bajo (normalmente menos de 1000). Como resultado, Braze no podrá sincronizar usuarios para un paso Eliminar de la audiencia hasta que la audiencia alcance el tamaño de audiencia adecuado.

{% endtab %}
{% endtabs %}

### Paso 5: Lanzar Canvas

Una vez que hayas configurado tu componente Facebook Audience, ¡simplemente lanza el Canvas! Se creará la nueva audiencia personalizada, y los usuarios que pasen por el componente Facebook Audience pasarán a esta audiencia personalizada en Facebook. Si tu Canvas contiene componentes posteriores, tus usuarios avanzarán al siguiente paso en su viaje de usuario.

La pestaña **Historial** de la audiencia personalizada en el administrador de audiencias de Facebook reflejará el número de usuarios enviados a la audiencia desde Braze. Si un usuario vuelve a entrar en el paso, se le enviará de nuevo a Facebook.

![Detalles de la audiencia y la pestaña Historial de una determinada audiencia de Facebook, que incluye una tabla Historial de la audiencia con columnas para la actividad, los detalles de la actividad, los elementos modificados y la fecha y hora.][9]{: style="max-width:80%;"}

## Migración a cuentas de trabajo Meta

A partir de julio de 2023, Meta lanzará las cuentas de trabajo Meta a un pequeño grupo de empresas interesadas en adoptar este nuevo tipo de cuenta. Si tienes una cuenta de empresa integrada con Braze, asegúrate de desconectarte y volver a conectarte a la [página del socio de Facebook]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync#step-1-connect-to-facebook) con tu cuenta de empresa para conservar esta implementación y no interrumpir ningún Canvas activo.

## Consideraciones sobre la sincronización de usuarios y el límite de velocidad
 
A medida que los usuarios alcancen el Paso de sincronización de audiencia, Braze sincronizará a estos usuarios casi en tiempo real, respetando al mismo tiempo los límites de tasa de la API de marketing de Facebook. Lo que esto significa en la práctica es que Braze intentará procesar por lotes el mayor número de usuarios cada 5 segundos antes de enviarlos a Facebook. 

El límite de velocidad de la API de marketing de Facebook establece no más de unas 190.000 solicitudes de API por cada cuenta de anuncios en un periodo de tiempo de 1 hora. Si un cliente Braze alcanza este límite de velocidad, Braze Canvas reintentará la sincronización durante un máximo de ~13 horas. Si la sincronización no es posible, estos usuarios aparecen en la métrica Usuarios erróneos.

## Comprender los análisis

La siguiente tabla incluye métricas y descripciones que le ayudarán a comprender mejor los análisis de su componente Audience Sync.

| Métrica | Descripción |
| --- | --- |
| El usuario ha entrado | Número de usuarios que entraron en este componente para ser sincronizados con Facebook. |
| Continúa con el paso siguiente | Cuántos usuarios avanzaron al siguiente componente, si lo hay. Todos los usuarios avanzarán automáticamente si este es el último paso en la rama Canvas. |
| Usuarios sincronizados | Número de usuarios que se han sincronizado correctamente con Facebook. |
| Usuarios no sincronizados | Número de usuarios que no se han sincronizado debido a que faltan campos para coincidir. |
| Usuarios pendientes | Número de usuarios que están siendo procesados por Braze para sincronizarse con Facebook. |
| Usuarios con errores | Número de usuarios que no se sincronizaron con Facebook debido a un error de la API tras unas 13 horas de reintentos. Las posibles causas de error pueden ser un token de Facebook no válido o que se haya eliminado la audiencia personalizada en Facebook. |
| Has salido de Canvas | Número de usuarios que han salido del Canvas. Esto ocurre cuando el último paso en Canvas es un paso de Facebook. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Recuerde que se producirá un retraso en los informes de las métricas de usuarios sincronizados y usuarios con errores debido a la descarga masiva y al reintento de 13 horas, respectivamente.
{% endalert %}   

## Solución de problemas

{% details ¿Qué debo hacer si recibo un error de token no válido? %}
Sólo tienes que desconectar y volver a conectar tu cuenta de Facebook en la página del socio de Facebook. Confirma con tu administrador de empresas de Facebook que tienes los permisos adecuados para la cuenta publicitaria con la que deseas sincronizar.
{% enddetails %}

{% details ¿Por qué no se puede iniciar mi Canvas? %}
- Asegúrate de que tu token de usuario del sistema está autenticado y tiene acceso a las cuentas de anuncios deseadas en Facebook Business Manager.
- Asegúrate de haber seleccionado una cuenta de publicidad, introducido un nombre para la nueva audiencia personalizada y seleccionado los campos que coincidan.
- Puede que hayas alcanzado el límite de 500 audiencias personalizadas en Facebook. Entra en el administrador de audiencias de Facebook para eliminar las que no necesites antes de crear nuevas audiencias personalizadas con Canvas.
{% enddetails %}

{% details ¿Cómo sé si los usuarios se han emparejado después de pasarlos a Facebook? %}
Facebook no facilita esta información por motivos de privacidad.
{% enddetails %}

{% details ¿Admite Braze audiencias personalizadas basadas en valores? %}
En este momento, Braze no admite audiencias personalizadas basadas en valores. Si estás interesado en sincronizar este tipo de audiencias personalizadas, envía [tus comentarios sobre el producto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% enddetails %}

{% details ¿Cómo resuelvo un problema con la sincronización de una audiencia personalizada similar basada en valores? %}

En este momento, Braze no supone audiencias personalizadas basadas en el valor. Si intentas sincronizar con esta audiencia, pueden producirse errores en el paso Sincronizar audiencia. Para solucionarlo, sigue estos pasos:

1. Ve al panel del administrador de anuncios de Facebook y selecciona **Audiencias**.
2. Selecciona **Crear audiencia** > **Audiencia personalizada**.
3. Selecciona **Lista de clientes**.
4. Sube tu CSV o lista sin la columna **Valor**. Selecciona **No, continuar con una lista de clientes que no incluya el valor del cliente**.
5. Termina de crear tu audiencia personalizada.
6. En Braze, actualiza el paso Sincronizar audiencia de Facebook con la audiencia personalizada que has creado.
{% enddetails %}

{% details He recibido un correo electrónico relacionado con las condiciones del servicio de audiencia personalizada de Facebook. ¿Qué debo hacer para resolverlo? %}
Para utilizar la Sincronización de audiencias con Facebook, debes aceptar estas condiciones de servicio. 

- Si tu cuenta publicitaria está directamente asociada a tu cuenta personal de Facebook, puedes aceptar las Condiciones de servicio desde tu cuenta personal aquí: `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=ACCOUNT_ID`.
- Si tu cuenta publicitaria está vinculada a la cuenta de administrador de empresas de tu empresa, tienes que aceptar las condiciones de servicio desde tu cuenta de administrador de empresas aquí: `https://business.facebook.com/customaudiences/value_based/tos.php?act=ACCOUNT_ID&business_id=BUSINESS_ID`.

Después de aceptar las condiciones de servicio de tu audiencia personalizada de Facebook, haz lo siguiente:
1. Actualiza tu token de acceso a Facebook con Braze desconectando y volviendo a conectar tu cuenta de Facebook.
2. Vuelve a habilitar el paso de sincronización con la audiencia de Facebook editando y actualizando tu Canvas.
Braze podrá sincronizar a los usuarios en cuanto lleguen al Paso de Facebook Audience.
{% enddetails %}


[0]: https://www.braze.com/privacy
[1]: https://www.facebook.com/business/help/113163272211510
[2]: https://www.facebook.com/business/help/910137316041095
[3]: https://www.facebook.com/ads/manage/customaudiences/tos.php
[4]: {% image_buster /assets/img/fb/afb_1.png %}
[5]: {% image_buster /assets/img/fb/afb_2.png %}
[6]: {% image_buster /assets/img/fb/afb_3.png %}
[7]: {% image_buster /assets/img/fb/afb_4.png %}
[8]: {% image_buster /assets/img/fb/afb_5.png %}
[9]: {% image_buster /assets/img/fb_audience_sync/audience_history.png %}
[10]: {% image_buster /assets/img/fb_audience_sync/analytics_example.jpg %}
[11]: {% image_buster /assets/img/fb_audience_sync/add_step.png %}
[12]: {% image_buster /assets/img/fb_audience_sync/add_audience.png %}
[13]: {% image_buster /assets/img/fb_audience_sync/create_audience.png %}
[14]: {% image_buster /assets/img/fb_audience_sync/new_audience.png %}
[15]: {% image_buster /assets/img/tiktok/tiktok13.png %}
[16]: {% image_buster /assets/img/tiktok/tiktok16.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/fb_sync.png %}
[22]: {% image_buster /assets/img/audience_sync/fb_sync2.png %}
[23]: {% image_buster /assets/img/audience_sync/fb_sync3.png %}
