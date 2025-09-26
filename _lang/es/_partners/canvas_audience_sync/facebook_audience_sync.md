---
nav_title: Facebook
article_title: Sincronización de la audiencia de Canvas con Facebook
description: "En este artículo de referencia se explica cómo utilizar Braze Audience Sync con Facebook para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más."
page_order: 2
alias: /audience_sync_facebook/

Tool:
  - Canvas

---

# Sincronización de audiencias con Facebook

> Con la Sincronización de audiencias de Braze con Facebook, puedes optar por añadir los datos de tus propios usuarios de tu integración de Braze a audiencias personalizadas de Facebook para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más.

Cualquier criterio que utilices normalmente para desencadenar un mensaje (push, correo electrónico, SMS o webhook) en un Canvas de Braze basado en tus datos de usuario puede utilizarse ahora para desencadenar un anuncio dirigido a ese usuario en Facebook utilizando audiencias personalizadas. Por ejemplo, cuando configures una Sincronización de audiencia con Facebook, podrás utilizar una amplia variedad de campos de origen, como correo electrónico, teléfono, nombre y apellidos.

**Entre los casos de uso habituales para sincronizar audiencias personalizadas se incluyen**:

- Dirigirse a usuarios de alto valor con múltiples canales para impulsar las compras o la interacción.
- Reorientar a los usuarios menos receptivos a otros canales de marketing.
- Crear audiencias de supresión para evitar que los usuarios reciban anuncios cuando ya son consumidores fieles de su marca.
- Crear audiencias similares para captar nuevos usuarios de forma más eficaz.

Esta característica permite a las marcas controlar qué datos propios específicos se comparten con Facebook. En Braze, se presta la máxima atención a las integraciones con las que puedes y no puedes compartir tus datos propios. Para más información, consulte nuestra [política de privacidad](https://www.braze.com/privacy).

## Consideraciones sobre la sincronización de usuarios y el límite de velocidad
 
A medida que los usuarios lleguen al paso Sincronización de audiencia, Braze sincronizará a estos usuarios casi en tiempo real, respetando al mismo tiempo los límites de tasa de la API de marketing de Facebook. Lo que esto significa en la práctica es que Braze intentará procesar por lotes el mayor número de usuarios cada 5 segundos antes de enviarlos a Facebook. 

El límite de velocidad de la API de marketing de Facebook establece un máximo de ~190.000 solicitudes de API para cada cuenta publicitaria en un periodo de tiempo de una hora. Si un cliente Braze alcanza este límite de velocidad, Braze Canvas reintentará la sincronización durante un máximo de ~13 horas. Si la sincronización no es posible, estos usuarios aparecen en la métrica Usuarios erróneos.

## Requisitos previos

Tendrás que confirmar que tienes los siguientes elementos creados y completados antes de configurar tu paso en Canvas de Facebook Audience. 

| Requisito | Origin | Descripción |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook](https://www.facebook.com/business/help/113163272211510) | Una herramienta centralizada para administrar los activos de Facebook de tu marca (por ejemplo, cuentas de anuncios, páginas y aplicaciones). |
| Cuenta publicitaria de Facebook | [Facebook](https://www.facebook.com/business/help/910137316041095) | Una cuenta de anuncios de Facebook activa vinculada al administrador de la empresa de tu marca.<br><br>Asegúrate de que el administrador de tu empresa en Facebook te ha concedido permisos de "Gestionar campañas" o "Gestionar cuentas de anuncios" para las cuentas de anuncios de Facebook que piensas utilizar con Braze. Asegúrate también de que has aceptado los términos y condiciones de tu cuenta publicitaria. |
| Términos de los públicos personalizados de Facebook | [Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php) | Acepta las Condiciones de públicos personalizados de Facebook para las cuentas de anuncios de Facebook que piensas utilizar con Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integración

### Paso 1: Conéctate a Facebook

En el panel de control de Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Facebook**. En Exportar audiencia de Facebook, selecciona **Conectar Facebook**.

![Página de tecnología de Facebook en Braze que incluye una sección de resumen y otra de exportación de la audiencia de Facebook con el botón de Facebook Conectado.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:85%;"}

Aparecerá una ventana de diálogo de Facebook oAuth para autorizar a Braze a crear audiencias personalizadas en tus cuentas de anuncios de Facebook.

![El primer cuadro de diálogo de Facebook que solicita "Conectarse como X", donde X es tu nombre de usuario de Facebook.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![El segundo cuadro de diálogo de Facebook que solicita permiso para administrar los anuncios de tus cuentas publicitarias.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

Después de vincular Braze a tu cuenta de Facebook, selecciona las cuentas de anuncios que deseas sincronizar dentro de tu espacio de trabajo Braze. Cuando estés conectado, volverás a la página del socio, donde podrás ver qué cuentas están conectadas y desconectar las cuentas existentes.

![Una versión actualizada de la página de socios tecnológicos de Facebook que muestra las cuentas de anuncios conectadas correctamente.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:85%;"}

Tu conexión a Facebook se aplica a nivel del espacio de trabajo Braze. Si tu administrador de Facebook te elimina de tu administrador de empresas de Facebook o del acceso a las cuentas de Facebook conectadas, Braze detectará un token no válido. Como resultado, tus Canvas activos que utilicen componentes de Facebook Audience mostrarán errores, y Braze no podrá sincronizar usuarios. 

{% alert important %}
Para los clientes que hayan pasado previamente por el proceso de revisión de la aplicación de Facebook para la [gestión de anuncios](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) y [el acceso estándar a la gestión de anuncios](https://developers.facebook.com/docs/marketing-api/access#standard), tu token de usuario del sistema seguirá siendo válido para el componente Facebook Audience. No podrás editar ni revocar el token de usuario del sistema de Facebook a través de la página del socio de Facebook. En su lugar, puedes conectar tu cuenta de Facebook para sustituir tu token de usuario del sistema de Facebook dentro de tu espacio de trabajo Braze. 

<br><br>La configuración de Facebook oAuth también se aplicará a las [exportaciones de Facebook mediante Segmentos]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites).
{% endalert %}

### Paso 2: Aceptar las condiciones de servicio de las audiencias personalizadas

Antes de crear tu Canvas, debes aceptar las siguientes condiciones de servicio de Facebook en los siguientes enlaces:

- **Lista de clientes Audiencias personalizadas Términos para tu cuenta personal:** `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- **Herramientas de Facebook para empresas Condiciones de tu cuenta de empresa:** `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

![Un ejemplo de los términos a aceptar para las audiencias personalizadas de la lista de clientes.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos.png %}){: style="max-width:85%;"}
![Un ejemplo de las condiciones que debes aceptar para las herramientas de empresa de Facebook.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos2.png %}){: style="max-width:85%;"}

Consulta la [sección de preguntas frecuentes](#terms) para obtener más información sobre la auditoría de tu cuenta de Facebook al realizar la integración.

### Paso 3: Añadir un componente de Facebook Audience en Canvas Flow

Añade un componente en tu Canvas y selecciona **Facebook Audience**.

![Una lista de componentes para añadir al Canvas.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![El componente de Sincronización de Audiencias.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Paso 4: Configuración de la sincronización

Selecciona el botón **Audiencia personalizada** para abrir el editor de componentes. A continuación, selecciona **Facebook** como socio de Sincronización de audiencias.

!["Configurar la sincronización de la audiencia" con opciones para elegir un socio.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Selecciona la cuenta de anuncios de Facebook deseada. En el desplegable **Elegir una audiencia nueva o existente**, escribe el nombre de una audiencia nueva o existente. 

{% tabs %}
{% tab Crear una nueva audiencia %}

1. Introduce un nombre para la nueva audiencia personalizada.
2. Selecciona **Añadir usuarios a la audiencia** y elige los campos que deseas sincronizar con Facebook. 
3. A continuación, selecciona **Crear audiencia** para guardar tu audiencia.

![Configuración de la sincronización de una audiencia con la información de correo electrónico, teléfono, nombre y apellidos para que coincida.]({% image_buster /assets/img/audience_sync/fb_sync.png %})

Se te notificará en la parte superior del editor de pasos si la audiencia se ha creado correctamente o si se produce un error durante este proceso. También puedes hacer referencia a esta audiencia para eliminar usuarios más adelante en el recorrido Canvas, porque la audiencia se creó en modo borrador.

Cuando lances un Canvas con una nueva audiencia, Braze creará la nueva audiencia personalizada al lanzar el Canvas y posteriormente sincronizará a los usuarios casi en tiempo real cuando entren en el paso en Canvas Sincronización de audiencia.

{% endtab %}
{% tab Sincronización con un público existente %}

Braze ofrece la posibilidad de añadir o eliminar usuarios de las audiencias personalizadas de Facebook existentes para confirmar que estas audiencias están actualizadas. Para sincronizar con una audiencia existente, haz lo siguiente:

1. Escribe el nombre de la audiencia existente en el desplegable.
2. Elige si quieres **Añadir a la audiencia** o **Eliminar de la audiencia**. 
3. Braze añadirá o eliminará usuarios casi en tiempo real cuando entren en el paso de Facebook Audience. 

![Configuración de la sincronización de la audiencia para eliminar la información de correo electrónico, teléfono, nombre y apellidos.]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
Facebook prohíbe eliminar usuarios de audiencias personalizadas cuando el tamaño de la audiencia es demasiado bajo (normalmente menos de 1.000 usuarios). Como resultado, Braze no podrá sincronizar usuarios para una eliminación del paso Sincronización de audiencia hasta que la audiencia alcance el tamaño de audiencia adecuado.
{% endalert %}

{% endtab %}
{% endtabs %}

### Paso 5: Lanzar Canvas

Después de configurar tu componente Facebook Audience, ¡es hora de lanzar el Canvas! Se creará la nueva audiencia personalizada, y los usuarios que pasen por el paso de Facebook Audience pasarán a esta audiencia personalizada en Facebook. Si tu Canvas contiene pasos posteriores, tus usuarios avanzarán al siguiente paso en su viaje de usuario.

La pestaña **Historial** de la audiencia personalizada en el administrador de audiencias de Facebook reflejará el número de usuarios enviados a la audiencia desde Braze. Si un usuario vuelve a entrar en el paso, se le enviará de nuevo a Facebook.

![Detalles de la audiencia y la pestaña Historial de una determinada audiencia de Facebook que incluye una tabla Historial de la audiencia con columnas para la actividad, los detalles de la actividad, los elementos modificados y la fecha y la hora.]({% image_buster /assets/img/fb_audience_sync/audience_history.png %}){: style="max-width:80%;"}

## Comprender los análisis

La siguiente tabla incluye métricas y descripciones que le ayudarán a comprender mejor los análisis de su componente Audience Sync.

| Métrica | Descripción |
| --- | --- |
| El usuario ha entrado | Número de usuarios que entraron en este componente para ser sincronizados con Facebook. |
| Continúa con el paso siguiente | Cuántos usuarios avanzaron al siguiente componente, si lo hay. Todos los usuarios avanzarán automáticamente si este es el último paso en la rama Canvas. |
| Usuarios sincronizados | Número de usuarios que se han sincronizado correctamente con Facebook. |
| Usuarios no sincronizados | Número de usuarios que no se han sincronizado debido a que faltan campos para coincidir. Los campos se emparejan utilizando un operador "OR", lo que significa que mientras un usuario tenga uno de los campos en Facebook, Facebook emparejará al usuario aunque no haya coincidencia en todos los demás campos. |
| Usuarios pendientes | Número de usuarios que están siendo procesados por Braze para sincronizarse con Facebook. |
| Usuarios con errores | Número de usuarios que no se sincronizaron con Facebook debido a un error de la API tras unas 13 horas de reintentos. Las posibles causas de error pueden ser un token de Facebook no válido o que se haya eliminado la audiencia personalizada en Facebook. |
| Has salido de Canvas | Número de usuarios que han salido del Canvas. Esto ocurre cuando el último paso en Canvas es un paso de Facebook. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Habrá un retraso en los informes de métricas de usuarios sincronizados y usuarios con errores debido al procesamiento interno.
{% endalert %}

## Preguntas más frecuentes

### ¿Cuánto tardan mis audiencias en aparecer en mi panel de socios de Audience Sync?

El tiempo que se tarda en poblar una audiencia depende del socio concreto. Todas las redes procesarán las solicitudes de Braze e intentarán emparejar a los usuarios. Las audiencias personalizadas pueden tardar hasta 24 horas en actualizarse.

### ¿Qué debo hacer si recibo un error de token no válido?

Sólo tienes que desconectar y volver a conectar tu cuenta de Facebook en la página del socio de Facebook. Confirma con el administrador de tu empresa de Facebook que tienes los permisos adecuados para la cuenta publicitaria con la que deseas sincronizar.

### ¿Por qué no se puede iniciar mi Canvas?

- Asegúrate de que tu token de usuario del sistema está autenticado y tiene acceso a las cuentas de anuncios deseadas en Facebook Business Manager.
- Asegúrate de haber seleccionado una cuenta de publicidad, introducido un nombre para la nueva audiencia personalizada y seleccionado los campos que coincidan.
- Puede que hayas alcanzado el límite de 500 audiencias personalizadas en Facebook. Ve al administrador de audiencias de Facebook para eliminar algunas innecesarias antes de crear nuevas audiencias personalizadas utilizando Canvas.

### ¿Cómo sé si los usuarios se han emparejado después de pasarlos a Facebook?

Facebook no facilita esta información por motivos de privacidad.

### ¿Soporta Braze audiencias personalizadas basadas en valores?

En este momento, Braze no admite audiencias personalizadas basadas en valores. Si estás interesado en sincronizar este tipo de audiencias personalizadas, envía [tus comentarios sobre el producto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

### ¿Braze hace hash de los datos antes de enviarlos a los socios de Audience Sync?

Una vez normalizados los datos del correo electrónico, Braze los procesa con SHA256.

**IDFA/AAID/phone:** Braze hashes con SHA256. Los tipos de audiencia a los que nos dirigimos son siempre uno de los siguientes:

- IDFA_SHA256
- AAID_SHA256
- EMAIL_SHA256
- PHONE_SHA256\.

En cuanto a la frecuencia, Braze sólo recopilará la información de identificación personal (PII) del usuario cuando éste entre en el paso de Sincronización de audiencias en el recorrido del usuario para prepararse para la sincronización.

### ¿Cómo resuelvo un problema con la sincronización de una audiencia personalizada similar basada en valores?

En este momento, Braze no admite audiencias personalizadas similares basadas en valores. Si intentas sincronizar con esta audiencia, pueden producirse errores en el paso Sincronizar audiencia. Para solucionarlo, sigue estos pasos:

1. Ve al panel del administrador de anuncios de Facebook y selecciona **Audiencias**.
2. Selecciona **Crear audiencia** > **Audiencia personalizada**.
3. Selecciona **Lista de clientes**.
4. Sube tu CSV o lista sin la columna **Valor**. Selecciona **No, continuar con una lista de clientes que no incluya el valor del cliente**.
5. Termina de crear tu audiencia personalizada.
6. En Braze, actualiza el paso Sincronizar audiencia de Facebook con la audiencia personalizada que has creado.

### He recibido un correo electrónico relacionado con las condiciones del servicio de audiencia personalizada de Facebook. ¿Qué debo hacer para resolverlo?

Para utilizar la Sincronización de audiencias con Facebook, debes aceptar estas condiciones de servicio. 

- Si tu cuenta publicitaria está directamente asociada a tu cuenta personal de Facebook, puedes aceptar las condiciones del servicio desde tu cuenta personal aquí: `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- Si tu cuenta publicitaria está vinculada a la cuenta del administrador de empresas de tu empresa, tienes que aceptar las condiciones del servicio en tu cuenta del administrador de empresas de Facebook aquí: `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

Después de aceptar las condiciones de servicio de tu audiencia personalizada de Facebook, haz lo siguiente:

1. Actualiza tu token de acceso a Facebook con Braze desconectando y volviendo a conectar tu cuenta de Facebook.
2. Vuelve a habilitar el paso de sincronización con la audiencia de Facebook editando y actualizando tu Canvas.

A continuación, Braze puede sincronizar a los usuarios en cuanto lleguen al paso Sincronizar audiencia de Facebook.

## Solución de problemas

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 40%;
}
table th:nth-child(2) {
    width: 40%;
}
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>Error</th>
      <th>Descripción</th>
      <th>Pasos para resolver</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Token no válido</b></td>
      <td>Las causas típicas son que el usuario que conectó la integración cambie su contraseña, que caduquen las credenciales, etc.</td>
      <td>Ve a <b>Integraciones de socios</b> > <b>Facebook</b> y desconecta y vuelve a conectar tu cuenta. Consulta <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>esta sección de solución de problemas</a> para conocer los pasos adicionales para auditar tu cuenta de Facebook.</td>
    </tr>
    <tr>
      <td><b>Tamaño de la audiencia demasiado bajo</b></td>
      <td>Este error puede producirse si has creado un paso de Sincronización de audiencias que elimina usuarios de tus audiencias. Si el tamaño de tu audiencia se aproxima a cero, la red puede señalar que el tamaño de la audiencia es demasiado pequeño para servir.</td>
      <td> Utiliza una estrategia de Sincronización de Audiencias que añada y elimine usuarios con regularidad, cuando no agote por completo el tamaño de la audiencia.</td>
    </tr>
    <tr>
      <td><b>La audiencia no existe</b></td>
      <td>El paso Sincronizar audiencia utiliza una audiencia que no existe o que ha sido eliminada. Esto también puede desencadenarse si ya no tienes el permiso necesario para acceder a la audiencia.</td>
      <td>Haz que un administrador compruebe en la plataforma del socio si la audiencia sigue existiendo. <br><br>Si existe, confirma si el usuario que conectó la integración tiene permiso para la audiencia. Si no es así, el usuario debe tener acceso a esa audiencia. <br><br>Si la audiencia se eliminó intencionadamente, añade una audiencia activa y crea una nueva audiencia en el paso.</td>
    </tr>
    <tr>
      <td><b>Intento de acceso a la cuenta publicitaria</b></td>
      <td>No tienes permisos para la cuenta publicitaria o la audiencia que has seleccionado.</td>
      <td>Trabaja con los administradores de tu cuenta publicitaria para obtener el acceso y los permisos adecuados.</td>
    </tr>
    <tr>
      <td><b>Condiciones del servicio no aceptadas</b></td>
      <td>Para algunos destinos de Sincronización de Audiencias, como Facebook, la red publicitaria exige aceptar unas condiciones de servicio específicas para utilizar la característica de Sincronización de Audiencias. Este error se desencadenará si no has aceptado las condiciones adecuadas. Como resultado, es posible que también hayas recibido un correo electrónico con este asunto de Braze: "Tus credenciales de autorización para Facebook no son válidas".</td>
      <td>Comprueba que has aceptado las condiciones exigidas por Facebook.</td>
    </tr>
    <tr>
      <td><b>Todos los usuarios se equivocan</b></td>
      <td>Si todos los usuarios están dando error en un paso a pesar de confirmar que estos usuarios tienen valores para los campos seleccionados en el paso, esto podría indicar un problema con tu cuenta de Facebook.</td>
      <td>Sigue los pasos de <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>esta sección de solución de problemas</a> para comprobar si tu cuenta tiene algún problema.
      </td>
    </tr>
    <tr>
      <td><b>No ha conseguido crear audiencia</b></td>
      <td>En la página de socios tecnológicos de Facebook, aparece "Conectado", pero hay un error en el paso de sincronización de audiencias de Facebook al sincronizar una audiencia: "Error al crear la audiencia 'nombre de la audiencia'". Ha fallado la autorización de tu cuenta de Facebook. Visita la página de socios tecnológicos para volver a conectar tu cuenta.</td>
      <td>Sigue los pasos de <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>esta sección de solución de problemas</a> para comprobar si tu cuenta tiene algún problema.
      </td>
    </tr>
  </tbody>
</table>

### Audita tu cuenta de Facebook

Si experimentas problemas adicionales con tu integración, consulta las siguientes secciones y pasos para auditar tu cuenta de Facebook. 

#### Revisar los permisos de la cuenta

1. Revisa [la documentación de Facebook](https://www.facebook.com/business/help/186007118118684?id=829106167281625) sobre cómo gestionar estos permisos en su plataforma. Para el Administrador de empresas de Facebook, necesitas al menos una función de **administrador** o de **empleado** administrador de empresas con acceso a las cuentas de anuncios necesarias.
2. Como **empleado**, confirma que el administrador te concede todos los permisos de **Gestionar cuenta de anuncios** para cada cuenta de anuncios para crear una audiencia o sincronizar usuarios con la audiencia. 
3. Una vez concedido, deberás desconectar y volver a conectar tu cuenta.

#### Acepta las condiciones del servicio {#terms}

Aceptar las Condiciones de servicio (CDS) pendientes de Facebook. Facebook requerirá periódicamente que tú (el usuario) y el administrador de la empresa aprueben de nuevo sus condiciones de servicio.

1. El usuario conectado debe aceptar todas las condiciones de servicio de cada una de sus cuentas publicitarias:
- Condiciones de servicio de la audiencia personalizada para tu cuenta personal de Facebook:
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`

![Una cuenta con todos los permisos de control para administrar una cuenta publicitaria.]({% image_buster /assets/img/fb_audience_sync/ad_account_permission.png %}){: style="max-width:70%;"}

Para encontrar tu cuenta y tu ID de empresa, sigue estos pasos:

1. Ve a tu [cuenta de administrador de anuncios de Facebook](https://adsmanager.facebook.com/).
2. Confirma que estás utilizando la cuenta publicitaria correcta verificándola en el menú desplegable.
3. En la URL, busca el ID de cuenta después de `act=` y el ID de empresa después de `business_id=`

![La URL con el ID de la cuenta y el ID de la empresa resaltados.]({% image_buster /assets/img/fb_audience_sync/fb_businessid_url.png %}){: style="max-width:90%;"}

{:start="4"}

4. Lee y selecciona **Aceptar** para las Condiciones de la audiencia personalizada. Te recomendamos que confirmes para qué cuenta se están firmando las condiciones de servicio utilizando el desplegable de la parte superior de las condiciones.

![El desplegable que muestra la cuenta que está firmando las condiciones de servicio.]({% image_buster /assets/img/fb_audience_sync/confirm_accept_tos.png %}){: style="max-width:90%;"}

{:start="5"}
5\. Debes seleccionar **Aceptar** para las condiciones del servicio. Después, verás este mensaje: "Has aceptado estas condiciones de servicio en nombre de Braze".
6\. Actualiza tu token de acceso a Facebook con Braze desconectando y volviendo a conectar tu cuenta de Facebook.
7\. Vuelve a habilitar el paso de sincronización con la audiencia de Facebook editando y actualizando tu Canvas. Braze podrá sincronizar a los usuarios en cuanto lleguen al Paso de Facebook Audience.
8\. Si el problema persiste, prueba a utilizar otro usuario con permisos de administrador para aceptar manualmente las condiciones a través del Administrador de anuncios.

#### Completa las tareas pendientes 

Comprueba si tienes alguna tarea pendiente con Facebook que pudiera estar bloqueándote el uso de los servicios de Facebook Ads:

1. [Accede al administrador de anuncios de Facebook](https://adsmanager.facebook.com/).
2. Selecciona la cuenta publicitaria con la que tienes problemas.
3. En la navegación, selecciona el **resumen de** tu **cuenta**. <br> ![La navegación con el resumen de cuenta seleccionado.]({% image_buster /assets/img/fb_audience_sync/ads_manager_accouint_overview.png %})
4. Comprueba si hay alguna alerta que deba ser atendida. <br> ![Una cuenta con una tarjeta de crédito caducada.]({% image_buster /assets/img/fb_audience_sync/resolve_alerts.png %})

{:start="5"}

5. Comprueba si hay alguna tarea de configuración que deba completarse. <br> ![Una cuenta con una configuración de cuenta parcialmente completada.]({% image_buster /assets/img/fb_audience_sync/confirm_tasks.png %})

#### Conectar con otro usuario

Como otro paso de solución de problemas, recomendamos que otro usuario administrador intente conectar su cuenta haciendo lo siguiente:

1. Desconecta la integración de corriente.
2. Un usuario independiente con permisos de administrador conecta su cuenta de usuario de Facebook.

