---
nav_title: TikTok
article_title: Sincronización de la audiencia de Canvas con TikTok
alias: /tiktok_audience_sync/
description: "En este artículo de referencia se explica cómo utilizar Braze Audience Sync con TikTok para ofrecer anuncios basados en activadores de comportamiento, segmentación, etc."
Tool:
  - Canvas
page_order: 7

---

# Sincronización del público con TikTok

Con Braze Audience Sync to TikTok, las marcas pueden optar por añadir los datos de usuario de su propia integración Braze a TikTok Audiences para ofrecer anuncios basados en desencadenantes de comportamiento, segmentación y mucho más. Cualquier criterio que utilice normalmente para activar un mensaje (push, correo electrónico, SMS, webhook, etc.) en un Braze Canvas. 

**Entre los casos de uso más comunes para la Sincronización de Audiencias se incluyen**:

- Dirigirse a usuarios de alto valor a través de múltiples canales para impulsar las compras o la participación
- Reorientar a los usuarios menos receptivos a otros canales de marketing
- Creación de audiencias de supresión para evitar que los usuarios reciban anuncios cuando ya son consumidores fieles de su marca.
- Creación de Actalike Audiences para captar nuevos usuarios de forma más eficaz

Esta función permite a las marcas controlar qué datos específicos de origen se comparten con TikTok. En Braze, las integraciones con las que puedes y no puedes compartir tus datos de origen se tienen muy en cuenta. Para más información, consulte nuestra [política de privacidad](https://www.braze.com/privacy).

{% alert important %}
**Cláusula de exención de responsabilidad de Audience Sync Pro**<br>
Braze Audience Sync to TikTok es una integración de Audience Sync Pro. Para obtener más información sobre esta integración, póngase en contacto con su gestor de cuentas Braze.
{% endalert %}

## Requisitos previos

Debes asegurarte de que los siguientes elementos están creados, completados y/o aceptados antes de configurar tu Paso de Audiencia TikTok en Canvas.

| Requisito | Origin | Descripción |
| ----------- | ------ | ----------- |
| Cuenta de TikTok para Business Center | [TikTok](https://business.tiktok.com/) | Una herramienta centralizada para gestionar los activos TikTok de tu marca (como cuentas de anuncios, páginas, aplicaciones). |
| Cuenta publicitaria de TikTok | [TikTok](https://ads.tiktok.com/) | Una cuenta de anuncios TikTok activa vinculada a la cuenta Business Center de tu marca.<br><br>Asegúrese de que su administrador de TikTok Business Center le ha concedido permisos de administrador a las cuentas de anuncios de TikTok que planea utilizar con Braze. |
| Términos y políticas de TikToK | [TikTok](https://ads.tiktok.com/i18n/official/policy/terms) | Aceptas cumplir cualquiera de los términos, políticas, directrices y documentación requeridos por TikTok relacionados con tu uso de la Sincronización de Audiencia de Pinterest, incluidos los términos, políticas, directrices y documentación incorporados por referencia a los mismos, que pueden incluir: las Condiciones Comerciales del Servicio, las Condiciones de Publicidad, la Política de Privacidad, las Condiciones de Audiencia Personalizada, las Condiciones de Servicio del Desarrollador, el Acuerdo de Intercambio de Datos del Desarrollador, las Políticas de Publicidad, las Directrices de la Marca y las Directrices de la Comunidad. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integración 

### Paso 1: Conéctate a TikTok

En el salpicadero de Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **TikTok**. En Sincronizar audiencia de TikTok, selecciona **Conectar TikTok**.

![La página de la tecnología TikTok en Braze incluye una sección de resumen y otra de sincronización de la audiencia de TikTok con el botón de TikTok conectado.]({% image_buster /assets/img/tiktok/tiktok1.png %}){: style="max-width:75%;"}

A continuación, serás redirigido a la página de TikTok OAuth para autorizar Braze para la gestión de cuentas de anuncios y Audience Management. Una vez que hayas seleccionado **Confirmar**, se te redirigirá de nuevo a Braze para que selecciones las cuentas de anuncios de TikTok con las que deseas sincronizar. 

![]({% image_buster /assets/img/tiktok/tiktok2.png %}){: style="max-width:75%;"}

Una vez conectado correctamente, volverás a la página del socio. Aquí puede ver qué cuentas están conectadas y desconectar cuentas existentes.

![]({% image_buster /assets/img/tiktok/tiktok3.png %}){: style="max-width:75%;"}

Tu conexión TikTok se aplicará a nivel del grupo de aplicaciones Braze. Si tu administrador de TikTok te elimina de tu TikTok Business Center o del acceso a las cuentas TikTok conectadas, Braze detectará un token inválido. Como resultado, tus Canvases activos que utilicen componentes de TikTok Audience mostrarán errores, y Braze no podrá sincronizar usuarios.

### Paso 2: Añadir un componente TikTok Audience en Canvas Flow

Añada un componente a su lienzo y seleccione **Sincronización con el público**. 

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Paso 3: Configuración de la sincronización

Haga clic en el botón **Público personalizado** para abrir el editor de componentes.

Selecciona **TikTok** como socio de Sincronización de Audiencia deseado.

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

A continuación, selecciona la cuenta de anuncios de TikTok deseada. En el desplegable **Elegir una audiencia nueva o existente**, escribe el nombre de una audiencia nueva o existente.

![]({% image_buster /assets/img/tiktok/tiktok11.png %})

{% tabs %}
{% tab Crear una nueva audiencia %}

**Crear una nueva audiencia**<br>
Introduce un nombre para el nuevo público, selecciona **Añadir usuarios al público** y selecciona los campos que deseas sincronizar con TikTok. A continuación, guarde su público haciendo clic en el botón **Crear público** situado en la parte inferior del editor de pasos.

![]({% image_buster /assets/img/audience_sync/tiktok3.png %})

Los usuarios recibirán una notificación en la parte superior del editor de pasos si la audiencia se crea correctamente o si surgen errores durante este proceso. Los usuarios también pueden hacer referencia a este público para la eliminación de usuarios más adelante en el recorrido Canvas, ya que el público se creó en modo borrador.

![]({% image_buster /assets/img/audience_sync/tiktok2.png %})

Cuando lanzas un Canvas con una nueva audiencia, Braze sincroniza a los usuarios casi en tiempo real a medida que entran en el paso de audiencia.

{% endtab %}
{% tab Sincronización con un público existente %}

**Sincronización con un público existente**<br>
Braze también ofrece la posibilidad de añadir usuarios a las audiencias de TikTok existentes para garantizar que estas audiencias estén actualizadas. Para sincronizar con una audiencia existente, escribe el nombre de la audiencia existente en el desplegable y selecciona **Añadir a la audiencia**. A continuación, Braze añadirá usuarios casi en tiempo real a medida que entren en el paso TikTok Audience.

![Vista ampliada del paso en Canvas Audiencia personalizada. Aquí se seleccionan la cuenta publicitaria deseada y la audiencia existente.]({% image_buster /assets/img/audience_sync/tiktok.png %})

{% endtab %}
{% endtabs %}

### Paso 4: Lanzar Canvas
Una vez que haya configurado su componente TikTok Audience, ¡simplemente inicie el Canvas! Se creará una nueva audiencia, y los usuarios que fluyan a través del componente TikTok Audience pasarán a esta audiencia en TikTok. Si su Canvas contiene componentes subsiguientes, sus usuarios avanzarán al siguiente paso en su viaje de usuario.

Puedes ver la audiencia en TikTok entrando en tu **cuenta de Ads Manager** y seleccionando **Audiencias** en el desplegable de **Activos**. En la página **Audiencia**, puedes ver el tamaño de cada audiencia cuando alcance aproximadamente 1000.

![Página de TikTok que enumera las siguientes métricas para la audiencia dada.]({% image_buster /assets/img/tiktok/tiktok5.png %})

## Consideraciones sobre la sincronización de usuarios y el límite de velocidad

A medida que los usuarios alcanzan el paso de Sincronización de Audiencia, Braze sincronizará estos usuarios casi en tiempo real respetando los límites de velocidad de la API de Marketing de TikTok. Esto significa que Braze intentará procesar el mayor número de usuarios cada 5 segundos antes de enviarlos a TikTok.

El límite de velocidad de la API de Segmentación de TikTok establece no más de 50 consultas por segundo y 10k usuarios por solicitud. Si un cliente de Braze alcanza este límite de velocidad, el Canvas reintentará la sincronización durante un máximo de ~13 horas. Si la sincronización no es posible, estos usuarios aparecen en la lista de la métrica Users Errored.

## Comprender los análisis

La siguiente tabla incluye métricas y descripciones que le ayudarán a comprender mejor los análisis de su componente Audience Sync.

| Métrica | Descripción |
| ------ | ----------- |
| Has entrado | Número de usuarios que entraron en este componente para ser sincronizados con TikTok. |
| Continúa con el paso siguiente | Número de usuarios que avanzaron al siguiente componente si existe. Todos los usuarios avanzarán automáticamente si este es el último paso en la rama Canvas. |
| Usuarios sincronizados | Número de usuarios que se han sincronizado correctamente con TikTok. Ten en cuenta que esto no equivale a usuarios emparejados en TikTok. |
| Usuarios no sincronizados | Número de usuarios que no se han sincronizado debido a que faltan campos para coincidir. |
| Usuarios pendientes | Número de usuarios que actualmente están siendo procesados por Braze para sincronizar en TikTok. |
| Usuarios con errores | Número de usuarios que no se sincronizaron con TikTok debido a un error de la API tras unas 13 horas de reintentos. Las causas potenciales de errores pueden incluir un token de TikTok inválido o si la audiencia fue eliminada en TikTok. |
| Has salido de Canvas | Número de usuarios que han salido del Canvas. Esto ocurre cuando el último paso de un Canvas es un componente de sincronización de Audiencia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Recuerde que se producirá un retraso en los informes de las métricas de usuarios sincronizados y usuarios con errores debido a la descarga masiva y al reintento de 13 horas, respectivamente.
{% endalert %}

## Preguntas más frecuentes

### ¿Qué debo hacer si recibo un error de token no válido?

Puedes desconectar y volver a conectar tu cuenta de TikTok en la página de socios de TikTok. Asegúrate con tu administrador de TikTok Business Center que tienes los permisos apropiados para la cuenta de anuncios que deseas sincronizar.

### ¿Por qué no se puede iniciar mi Canvas?

Confirma que tu cuenta de TikTok se conecta correctamente a Braze en la página del socio de TikTok. A continuación, asegúrate de haber seleccionado una cuenta de publicidad, introducido un nombre para la nueva audiencia y seleccionado los campos que coincidan.

### ¿Cómo sé si los usuarios han coincidido después de pasar usuarios a TikTok?

TikTok no proporciona esta información para sus políticas de privacidad de datos.

### ¿Cuánto tardarán mis audiencias en poblar TikTok?

El tamaño de la audiencia se actualizará en 24-48 horas en la página de Audiencias en el Administrador de Anuncios de TikTok.

### ¿Cuál es el número máximo de audiencias que puedo tener en mi cuenta de anuncios de TikTok?

Puedes tener hasta 400 audiencias por cuenta de anuncios de TikTok.

### ¿Por qué el tamaño de mi audiencia o la tasa de coincidencias en TikTok es mayor que la de los usuarios sincronizados en Braze con Audience Sync?

Esto se debe a que en TikTok, un ID puede estar asociado a varios usuarios de TikTok. Esto ocurre con mayor frecuencia cuando los clientes utilizan ID de anuncios para móviles (IDFA de iOS y GAID de Android) porque un dispositivo puede tener varios usuarios de TikTok conectados. 

Además, TikTok también cuenta a los usuarios de Pangle como usuarios coincidentes, lo que en algunos casos puede dar lugar a una tasa de coincidencia elevada. Sin embargo, cuando utilizas la audiencia para la entrega de anuncios, es posible que el tamaño real de la audiencia entregable no sea tan alto como el tamaño del usuario emparejado, ya que depende de la ubicación y de otros factores que influyen.


