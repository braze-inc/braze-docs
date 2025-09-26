---
nav_title: Snapchat
article_title: Sincronización de la audiencia de Canvas con Snapchat
description: "Este artículo de referencia explica cómo utilizar el componente Braze Audience Sync en Snapchat para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más."
page_order: 6
alias: "/audience_sync_snapchat/"

Tool:
  - Canvas

---

# Sincronización de la audiencia con Snapchat

Con Braze Audience Sync to Snapchat, las marcas pueden añadir datos de usuarios de su integración Braze a las listas de clientes de Snapchat para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más. Cualquier criterio que normalmente utilizarías para desencadenar un mensaje (push, correo electrónico, SMS, webhook, etc.) en un Canvas de Braze basado en tus datos de usuario, ahora se puede utilizar para desencadenar un anuncio dirigido a ese usuario en tus listas de clientes de Snapchat.

**Entre los casos de uso habituales de la sincronización de audiencias se incluyen:**

- Dirigirse a usuarios de alto valor a través de múltiples canales para impulsar las compras o la interacción
- Reorientar a los usuarios menos receptivos a otros canales de marketing
- Crear audiencias de supresión para evitar que los usuarios reciban anuncios cuando ya son consumidores fieles a tu marca.
- Crear audiencias similares para captar nuevos usuarios de forma más eficaz

Esta característica permite a los usuarios controlar qué datos propios específicos se comparten con Snapchat. En Braze, se presta la máxima atención a las integraciones con las que puedes y no puedes compartir tus datos propios. Para más información, consulte nuestra [política de privacidad](https://www.braze.com/privacy).

{% alert important %}
**Exención de responsabilidad de Audience Sync Pro**<br>
Braze Audience Sync to Snapchat es una integración de Audience Sync Pro. Para más información sobre esta integración, ponte en contacto con tu director de cuentas Braze.
{% endalert %}

## Requisitos previos 

Debes asegurarte de que los siguientes elementos están creados, completados y/o aceptados antes de configurar tu paso de audiencia de Snapchat en Canvas.

| Requisito | Origin | Descripción |
| --- | --- | --- |
| Administrador de negocios de Snapchat | Snapchat | Una herramienta centralizada para administrar los activos de Snapchat de tu marca (como cuentas de anuncios, páginas, aplicaciones). |
| Cuenta publicitaria de Snapchat | Snapchat | Una cuenta de anuncios de Snapchat activa vinculada al administrador de negocios de Snapchat de tu marca.<br><br>Asegúrate de que tu administrador de Snapchat Business Manager te ha concedido permisos de administrador para las cuentas de anuncios de Snapchat que piensas utilizar con Braze. |
| Términos y políticas de Snapchat | [Snapchat](https://www.snap.com/en-US/policies) | Acepta cumplir cualquiera de los términos, políticas, directrices y documentación requeridos por Snapchat relacionados con tu uso de la Sincronización de audiencias de Snapchat, incluidos los términos, políticas, directrices y documentación incorporados por referencia a los mismos, que pueden incluir: las Condiciones de servicio, las Condiciones de servicio para empresas, las Condiciones para desarrolladores, la Sincronización de audiencias, las Políticas de publicidad, la Política de contenido comercial, las Directrices de la comunidad y la Responsabilidad del proveedor. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integración 

### Paso 1: Conéctate a Snapchat

En el panel de Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Snapchat**. En Sincronizar audiencia de Snapchat, selecciona **Conectar Snapchat**.

![Página de tecnología de Snapchat en Braze que incluye una sección de resumen y otra de sincronización de la audiencia de Snapchat con el botón de Snapchat conectado.]({% image_buster /assets/img/snapchat/snapchat1.png %}){: style="max-width:80%;"}

A continuación, se te redirigirá a la página OAuth de Snapchat para que autorices a Braze los permisos relacionados con tu integración de Audience Sync.

Una vez que hayas seleccionado confirmar, se te redirigirá de nuevo a Braze para que selecciones las cuentas de anuncios de Snapchat que deseas sincronizar. 

![Una lista de las cuentas de anuncios disponibles que puedes conectar a Snapchat.]({% image_buster /assets/img/snapchat/snapchat2.png %}){: style="max-width:80%;"}

Una vez conectado correctamente, volverás a la página del socio, donde podrás ver qué cuentas están conectadas y desconectar las cuentas existentes.

![Una versión actualizada de la página de socios tecnológicos de Snapchat que muestra las cuentas de anuncios conectadas correctamente.]({% image_buster /assets/img/snapchat/snapchat3.png %}){: style="max-width:80%;"}

Tu conexión a Snapchat se aplicará a nivel del espacio de trabajo Braze. Si tu administrador de Snapchat te elimina de tu Business Manager de Snapchat o del acceso a las cuentas publicitarias de Snapchat conectadas, Braze detectará un token no válido. Como resultado, tus Lienzos activos que utilicen Snapchat mostrarán errores y Braze no podrá sincronizar usuarios.

### Paso 2: Añade un paso de sincronización de audiencia con Snapchat

Añada un componente a su lienzo y seleccione **Sincronización con el público**.

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Paso 3: Configuración de la sincronización

Haga clic en el botón **Público personalizado** para abrir el editor de componentes.

Selecciona **TikTok** como socio de Sincronización de Audiencia deseado.

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

A continuación, selecciona la cuenta de anuncios de Snapchat que desees. En el desplegable **Elegir una audiencia nueva o existente**, escribe el nombre de una audiencia nueva o existente.

{% tabs %}
{% tab Crear una nueva audiencia %}

**Crear una nueva audiencia**<br>
Introduce un nombre para la nueva audiencia, selecciona **Añadir usuarios a la audiencia** y selecciona los campos que deseas sincronizar con Snapchat. A continuación, guarda tu audiencia haciendo clic en el botón **Crear audiencia** situado en la parte inferior del editor de pasos.

![Vista ampliada del paso en Canvas Audiencia personalizada. Aquí se selecciona la cuenta publicitaria deseada y se crea una nueva audiencia.]({% image_buster /assets/img/audience_sync/snapchat3.png %})

Los usuarios recibirán una notificación en la parte superior del editor de pasos si la audiencia se crea correctamente o si surgen errores durante este proceso. Los usuarios también pueden hacer referencia a este público para la eliminación de usuarios más adelante en el recorrido Canvas, ya que el público se creó en modo borrador.

![Una alerta que aparece después de crear una nueva audiencia en el componente Canvas.]({% image_buster /assets/img/audience_sync/snapchat2.png %})

Cuando lanzas un Canvas con una nueva audiencia, Braze sincroniza a los usuarios casi en tiempo real a medida que entran en el componente Audience Sync.

{% endtab %}
{% tab Sincronización con un público existente %}
**Sincronización con una audiencia existente**<br>
Braze también ofrece la posibilidad de añadir usuarios a las audiencias de Snapchat existentes para garantizar que estas audiencias estén actualizadas. Para sincronizar con una audiencia existente, escribe el nombre de la audiencia existente en el desplegable y **Añadir a la audiencia**. A continuación, Braze añadirá usuarios casi en tiempo real a medida que entren en el componente Audience Sync.

![Vista ampliada del paso en Canvas Audiencia personalizada. Aquí se seleccionan la cuenta publicitaria deseada y el público existente.]({% image_buster /assets/img/audience_sync/snapchat.png %})

{% endtab %}
{% endtabs %}

### Paso 4: Lanzar Canvas

Una vez que hayas configurado la sincronización de tu audiencia con Snapchat, ¡lanza el Canvas! Se creará una nueva audiencia, y los usuarios que pasen por el paso Sincronizar audiencia pasarán a esta audiencia en Snapchat. Si tu Canvas contiene componentes posteriores, tus usuarios avanzarán al siguiente paso en su viaje de usuario.

Puedes ver la audiencia en Snapchat entrando en tu cuenta de administrador de anuncios y seleccionando **Audiencias** en la sección Activos de la navegación. En la página **Audiencias**, puedes ver el tamaño de cada audiencia cuando alcance ~1.000.

![Detalles de la audiencia de una determinada audiencia de Snapchat que incluye el nombre de la audiencia, el tipo de audiencia, el tamaño de la audiencia y la retención de la audiencia en días.]({% image_buster /assets/img/snapchat/snapchat7.png %})

## Consideraciones sobre la sincronización de usuarios y el límite de velocidad

Cuando los usuarios lleguen al paso Sincronización de audiencia, Braze sincronizará a estos usuarios casi en tiempo real, respetando los límites de velocidad de la API de Snapchat. En la práctica, Braze intentará procesar por lotes el mayor número de usuarios cada 5 segundos antes de enviarlos a Snapchat.

El límite de velocidad de la API de Snapchat establece no más de diez consultas por segundo y 100.000 usuarios por solicitud. Si un cliente Braze alcanza este límite de velocidad, Braze Canvas reintentará la sincronización durante un máximo de ~13 horas. Si la sincronización no es posible, estos usuarios aparecen en la lista de la métrica Users Errored.

### Comprender los análisis

La siguiente tabla incluye métricas y descripciones que le ayudarán a comprender mejor los análisis de su componente Audience Sync.

| Métrica | Descripción |
| --- | --- |
| El usuario ha entrado | Número de usuarios que entraron en este componente para ser sincronizados con Snapchat. |
| Continúa con el paso siguiente | ¿Cuántos usuarios avanzaron al siguiente componente, si lo hay? Todos los usuarios avanzarán automáticamente si éste es el último paso en Canvas. |
| Usuarios sincronizados | Número de usuarios que se han sincronizado correctamente con Snapchat. |
| Usuarios no sincronizados | Número de usuarios que no se han sincronizado debido a que faltan campos para coincidir. |
| Usuarios pendientes | Número de usuarios que están siendo procesados actualmente por Braze para sincronizarse en Snapchat. |
| Usuarios con errores | Número de usuarios que no se sincronizaron con Snapchat debido a un error de la API tras unas 13 horas de reintentos. Las causas potenciales de los errores pueden incluir un token de Snapchat no válido o si se ha eliminado la audiencia en Snapchat. |
| Has salido de Canvas | Número de usuarios que han salido del Canvas. Esto ocurre cuando el último paso de un Canvas es un componente de Sincronización de Audiencias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Recuerda que habrá un retraso en los informes de los usuarios sincronizados y de las métricas con errores debido a la descarga masiva y al reintento de 13 horas, respectivamente.
{% endalert %}   

## Preguntas más frecuentes

### ¿Cuántas audiencias puede soportar Snapchat?

En este momento, solo puedes tener 1000 audiencias en tu cuenta de Snapchat. 

Si superas este límite, Braze te notificará que no podemos crear nuevas audiencias. Tendrás que eliminar las audiencias que ya no utilices en tu cuenta de anuncios de Snapchat.

### ¿Cómo sé si los usuarios se han emparejado después de pasar usuarios a Snapchat?

Snapchat no proporciona esta información para sus políticas de privacidad de datos.

### ¿Qué debo hacer si recibo un error de token no válido?

Puedes desconectar y volver a conectar tu cuenta de Snapchat en la página del socio de Snapchat. Confirma con tu administrador de Snapchat Business Manager que tienes los permisos adecuados para la cuenta publicitaria con la que deseas sincronizar.

### ¿Por qué no se puede iniciar mi Canvas?

Asegúrate de que tu cuenta de anuncios de Snapchat se conecta correctamente a Braze en la página del socio de Snapchat. Comprueba que has seleccionado una cuenta de publicidad, introducido un nombre para la nueva audiencia y seleccionado los campos que coinciden.


