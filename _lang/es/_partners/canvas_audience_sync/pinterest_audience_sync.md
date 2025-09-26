---
nav_title: Pinterest
article_title: Sincronización de la audiencia de Canvas con Pinterest
description: "Este artículo de referencia explica cómo utilizar Braze Audience Sync en Pinterest para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más."
page_order: 5
alias: "/audience_sync_pinterest/"

Tool:
  - Canvas

---

# Sincronización de audiencia con Pinterest

Mediante la Sincronización de Audiencias Braze con Pinterest, las marcas pueden optar por añadir datos de usuarios de su propia integración Braze a las Audiencias de Pinterest para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más. Cualquier criterio que utilices normalmente para desencadenar un mensaje (push, correo electrónico, SMS, webhook, etc.) en un Canvas de Braze basado en tus datos de usuario puede utilizarse ahora para desencadenar un anuncio dirigido a ese usuario en tus Audiencias de Pinterest.

**Entre los casos de uso habituales de la sincronización de audiencias se incluyen:**

- Dirigirse a usuarios de alto valor a través de múltiples canales para impulsar las compras o la interacción
- Reorientar a los usuarios menos receptivos a otros canales de marketing
- Creación de audiencias de supresión para evitar que los usuarios reciban anuncios cuando ya son consumidores fieles de su marca.
- Crear Audiencias Actalike para captar nuevos usuarios de forma más eficaz

Esta característica permite a las marcas controlar qué datos propios específicos se comparten con Pinterest. En Braze, se presta la máxima atención a las integraciones con las que puedes y no puedes compartir tus datos propios. Para más información, consulte nuestra [política de privacidad](https://www.braze.com/privacy).

{% alert important %}
**Exención de responsabilidad de Audience Sync Pro**<br>
Braze Audience Sync to Pinterest es una integración de Audience Sync Pro. Para más información sobre esta integración, ponte en contacto con tu director de cuentas Braze.
{% endalert %}

## Requisitos previos 
Debes asegurarte de que los siguientes elementos están creados, completados y/o aceptados antes de configurar tu paso de audiencia de Pinterest en Canvas.

| Requisito | Origin | Descripción |
| --- | --- | --- |
| Pinterest Business Hub | [Pinterest](https://www.pinterest.com/business/hub/) | Una herramienta centralizada para administrar los activos de Pinterest de tu marca (como cuentas de anuncios, páginas, aplicaciones). |
| Cuenta publicitaria de Pinterest | [Pinterest](https://ads.pinterest.com/) | Una cuenta publicitaria de Pinterest activa vinculada al Pinterest Business Hub de tu marca.<br><br>Asegúrate de que tu administrador de Pinterest Business Hub te ha concedido permisos de administrador para las cuentas de anuncios de Pinterest que piensas utilizar con Braze. |
| Condiciones y políticas de Pinterest | Pinterest | Aceptas cumplir cualquiera de los términos, políticas, directrices y documentación exigidos por Pinterest en relación con tu uso de la Sincronización de audiencias de Pinterest, incluidos los términos, políticas, directrices y documentación incorporados por referencia a los mismos, que pueden incluir: las Condiciones del servicio, las Condiciones del servicio para empresas, la Política de privacidad, las Condiciones del servicio para desarrolladores y API, las Condiciones de datos de anuncios, las Directrices publicitarias, el Acuerdo de servicios publicitarios, las Directrices comunitarias y las Directrices de la marca. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integración 

### Paso 1: Conéctate a Pinterest

En el panel de Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Pinterest**. En Sincronizar audiencia de Pinterest, selecciona **Conectar Pinterest**.

![Página de tecnología de Pinterest en Braze que incluye una sección de resumen y otra de sincronización de la audiencia de Pinterest con el botón de Pinterest conectado.]({% image_buster /assets/img/pinterest/pinterest1.png %}){: style="max-width:80%;"}

A continuación, se te redirigirá a la página OAuth de Pinterest para que autorices a Braze para la gestión de cuentas publicitarias y la gestión de audiencias.

Tras seleccionar **Confirmar**, se te redirigirá de nuevo a Braze para que selecciones las cuentas de anuncios de Pinterest que deseas sincronizar. 

![Una lista de las cuentas de anuncios disponibles que puedes conectar a Pinterest.]({% image_buster /assets/img/pinterest/pinterest2.png %}){: style="max-width:80%;"}

Cuando te hayas conectado correctamente, volverás a la página del socio, donde podrás ver qué cuentas están conectadas y desconectar las cuentas existentes.

![Una versión actualizada de la página de socios tecnológicos de Pinterest que muestra las cuentas de anuncios conectadas correctamente.]({% image_buster /assets/img/pinterest/pinterest3.png %}){: style="max-width:80%;"}

Tu conexión a Pinterest se aplicará a nivel del espacio de trabajo Braze. Si tu administrador de Pinterest te elimina de tu Pinterest Business Hub o del acceso a las cuentas de Pinterest conectadas, Braze detectará un token no válido. Como resultado, tus Canvas activos que utilicen componentes de Audiencia de Pinterest mostrarán errores, y Braze no podrá sincronizar usuarios.

### Paso 2: Añadir un paso de sincronización de audiencia con Pinterest

Añada un componente a su lienzo y seleccione **Sincronización con el público**.

![]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Paso 3: Configuración de la sincronización

Haz clic en el botón **Audiencia personalizada** para abrir el editor de componentes.

Selecciona **Pinterest** como socio de Sincronización de Audiencias deseado.

![]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

A continuación, selecciona la cuenta de anuncios de Pinterest que desees. En el **desplegable Elegir una audiencia nueva o existente**, escribe el nombre de una audiencia nueva o existente.

{% tabs %}
{% tab Crear una nueva audiencia %}

**Crear una nueva audiencia**<br>
Introduce un nombre para la nueva audiencia, selecciona **Añadir usuarios a la audiencia** y selecciona los campos que deseas sincronizar con Pinterest. A continuación, guarda tu audiencia haciendo clic en el botón **Crear audiencia** situado en la parte inferior del editor de pasos.

![Vista ampliada del paso en Canvas Audiencia personalizada. Aquí se selecciona la cuenta publicitaria deseada y se crea una nueva audiencia.]({% image_buster /assets/img/audience_sync/pinterest_sync.png %})

Los usuarios recibirán una notificación en la parte superior del editor de pasos si la audiencia se crea correctamente o si surgen errores durante este proceso. Los usuarios también pueden hacer referencia a este público para la eliminación de usuarios más adelante en el recorrido Canvas, ya que el público se creó en modo borrador.

![Una alerta que aparece después de crear una nueva audiencia en el componente Canvas.]({% image_buster /assets/img/audience_sync/pinterest_sync3.png %})

Cuando lanzas un Canvas con una nueva audiencia, Braze sincroniza a los usuarios casi en tiempo real cuando entran en el paso en Canvas de Sincronización de Audiencia.
{% endtab %}
{% tab Sincronización con un público existente %}
**Sincronización con una audiencia existente**<br>
Braze también ofrece la posibilidad de añadir usuarios a las audiencias de Pinterest existentes para garantizar que estas audiencias están actualizadas. Para sincronizar con una audiencia existente, escribe el nombre de la audiencia existente en el desplegable y añádela a la audiencia. A continuación, Braze añadirá usuarios casi en tiempo real cuando entren en el paso Sincronización de audiencias.

![Vista ampliada del paso en Canvas Audiencia personalizada. Aquí se seleccionan la cuenta publicitaria deseada y el público existente.]({% image_buster /assets/img/audience_sync/pinterest_sync2.png %})

{% endtab %}
{% endtabs %}

### Paso 4: Lanzar Canvas

Una vez que hayas configurado la sincronización de tu audiencia con Pinterest, ¡lanza el Canvas! Se creará la nueva audiencia, y los usuarios que pasen por el paso Sincronización de audiencias pasarán a esta audiencia en Pinterest. Si tu Canvas contiene componentes posteriores, tus usuarios avanzarán al siguiente paso en su viaje de usuario.

Puedes ver la audiencia en Pinterest entrando en tu cuenta de administrador de anuncios y seleccionando Audiencias en el desplegable Anuncios. En la página Audiencia, puedes ver el tamaño de cada audiencia cuando alcance ~100.

![Detalles de la audiencia de una determinada audiencia de Pinterest que incluye el nombre de la audiencia, el ID de la audiencia, el tipo de audiencia y el tamaño de la audiencia.]({% image_buster /assets/img/pinterest/pinterest11.png %})

## Consideraciones sobre la sincronización de usuarios y el límite de velocidad

A medida que los usuarios lleguen al paso Sincronización de audiencia, Braze sincronizará a estos usuarios casi en tiempo real respetando los límites de tasa de la API de marketing de Pinterest. En la práctica, Braze intentará procesar por lotes el mayor número de usuarios cada 5 segundos antes de enviarlos a Pinterest.

El límite de velocidad de la API de segmentos de Pinterest establece no más de siete consultas por segundo por usuario y 1.900 usuarios por solicitud. Si un cliente Braze alcanza este límite de velocidad, Braze Canvas reintentará la sincronización durante un máximo de ~13 horas. Si la sincronización no es posible, estos usuarios aparecen en la lista de la métrica Users Errored.

## Comprender los análisis

La siguiente tabla incluye métricas y descripciones que le ayudarán a comprender mejor los análisis de su componente Audience Sync.

| Métrica | Descripción |
| --- | --- |
| El usuario ha entrado | Número de usuarios que entraron en este componente para ser sincronizados con Pinterest. |
| Continúa con el paso siguiente | ¿Cuántos usuarios avanzaron al siguiente componente, si lo hay? Todos los usuarios avanzarán automáticamente si éste es el último paso en Canvas. |
| Usuarios sincronizados | Número de usuarios que se han sincronizado correctamente con Pinterest. |
| Usuarios no sincronizados | Número de usuarios que no se han sincronizado debido a que faltan campos para coincidir. |
| Usuarios pendientes | Número de usuarios que Braze está procesando actualmente para sincronizar en Pinterest. |
| Usuarios con errores | Número de usuarios que no se sincronizaron con Pinterest debido a un error de la API tras unas 13 horas de reintentos. Las causas potenciales de los errores pueden incluir un token de Pinterest no válido o si la audiencia fue eliminada en Pinterest. |
| Has salido de Canvas | Número de usuarios que han salido del Canvas. Esto ocurre cuando el último paso de un Canvas es un componente de Sincronización de Audiencias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Recuerda que habrá un retraso en los informes de los usuarios sincronizados y de las métricas con errores debido a la descarga masiva y al reintento de 13 horas, respectivamente.
{% endalert %}   

## Preguntas más frecuentes

### ¿Cuánto tardarán mis audiencias en poblar Pinterest?

El tamaño de la audiencia se actualizará en 24-48 horas en la página **Audiencias** del administrador de anuncios de Pinterest.

### ¿Cómo sé si los usuarios han coincidido después de pasar usuarios a Pinterest?

Pinterest no proporciona esta información para sus propias políticas de privacidad de datos.

### ¿Qué debo hacer si recibo un error de token no válido?

Confirma con tu administrador de Pinterest Business Hub que tienes los permisos adecuados para la cuenta de anuncios que deseas sincronizar. También puedes desconectar y volver a conectar tu cuenta de Pinterest en la página del socio de Pinterest. 

### ¿Por qué no se puede iniciar mi Canvas?

Asegúrate de que tu cuenta de Pinterest se conecta correctamente a Braze en la página del socio de Pinterest. Asegúrate de haber seleccionado una cuenta de publicidad, introducido un nombre para la nueva audiencia y seleccionado los campos que coincidan.

### ¿Por qué no puedo seleccionar mi cuenta de anuncios para mi paso de Sincronización de Audiencias?

Comprueba que tu token se generó con los permisos de cuenta correctos. Ten en cuenta que si tienes demasiadas audiencias en tu cuenta de anuncios de Pinterest, el menú desplegable para seleccionar tu cuenta de anuncios puede agotarse. En este caso, te recomendamos que reduzcas la cantidad de audiencias de tu cuenta publicitaria.

