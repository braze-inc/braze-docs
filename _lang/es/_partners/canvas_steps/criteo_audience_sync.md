---
nav_title: Criteo
article_title: Sincronización del público de Canvas con Criteo
description: "Este artículo de referencia explica cómo utilizar Braze Audience Sync con Criteo para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más."
page_order: 1
alias: "/audience_sync_criteo/"

Tool:
  - Canvas
---

# Sincronización de audiencias con Criteo

Con Braze Audience Sync to Criteo, las marcas pueden optar por añadir los datos de usuario de su propia integración Braze a las listas de clientes de Criteo para ofrecer anuncios basados en activadores de comportamiento, segmentación y mucho más. Cualquier criterio que utilice normalmente para activar un mensaje (push, correo electrónico, SMS, webhook, etc.) en un Braze Canvas basado en sus datos de usuario puede utilizarse ahora para activar un anuncio dirigido a ese usuario en sus listas de clientes de Criteo.

**Entre los casos de uso más comunes para la sincronización de audiencias se incluyen:**

- Dirigirse a usuarios de alto valor a través de múltiples canales para impulsar las compras o el compromiso
- Reorientar a los usuarios menos receptivos a otros canales de marketing
- Creación de audiencias de supresión para evitar que los usuarios reciban anuncios cuando ya son consumidores fieles de su marca.
- Creación de audiencias similares para captar nuevos usuarios de forma más eficaz

Esta función ofrece a las marcas la opción de controlar qué datos específicos de origen se comparten con Criteo. En Braze, las integraciones con las que puedes y no puedes compartir tus datos de origen se tienen muy en cuenta. Para más información, consulte nuestra [política de privacidad](https://www.braze.com/privacy).

{% alert important %}
**Cláusula de exención de responsabilidad de Audience Sync Pro**<br>
Braze Audience Sync to Criteo es una integración de Audience Sync Pro. Para obtener más información sobre esta integración, póngase en contacto con su gestor de cuentas Braze. <br> 
{% endalert %}

## Requisitos previos 

Tendrás que asegurarte de que tienes los siguientes elementos creados y/o completados antes de configurar tu Sincronización de Audiencia con Criteo.

| Requisito | Origin | Descripción |
| --- | --- | --- |
| Cuenta publicitaria Criteo | [Criteo](https://marketing.criteo.com/) | Una cuenta de anuncios Criteo activa vinculada a su marca.<br><br>Asegúrate de que tu administrador de Criteo te ha concedido los permisos adecuados para acceder a Audiencias. |
| [Directrices publicitarias de Criteo](https://www.criteo.com/advertising-guidelines/)<br>y<br>[Directrices de seguridad de la marca Criteo](https://www.criteo.com/wp-content/uploads/2017/11/Criteo-Brand-Safety-Guidelines-UK-March-2016.pdf) | Criteo | Como cliente activo de Criteo, debes asegurarte de que puedes cumplir las Directrices de Publicidad y Seguridad de Marca de Criteo antes de lanzar cualquier campaña de Criteo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integración 

### Paso 1: Conectar con Criteo

En el panel de control de Braze, vaya a **Integraciones de socios** > **Socios tecnológicos** y seleccione **Criteo**. En Exportar audiencia de Criteo, selecciona **Conectar Criteo**.

{% alert note %}
Si utiliza la [navegación anterior]({{site.baseurl}}/navigation), encontrará a **los socios tecnológicos** en **Integraciones**.
{% endalert %}

![Página de tecnología Criteo en Braze que incluye una sección de Resumen y otra de Criteo con el botón Criteo Conectado.][5]{: style="max-width:80%;"}

Aparecerá una página Criteo oAuth para autorizar a Braze los permisos relacionados con su integración Audience Sync.

Una vez que haya seleccionado confirmar, se le redirigirá de nuevo a Braze para que seleccione las cuentas de anuncios de Criteo con las que desea sincronizar. 

![Una lista de las cuentas de anuncios disponibles que puedes conectar a Criteo.][7]{: style="max-width:80%;"}

Una vez que se haya conectado correctamente, volverá a la página de socios, donde podrá ver qué cuentas están conectadas y desconectar las cuentas existentes.

![Una versión actualizada de la página de socios tecnológicos de Criteo que muestra las cuentas de anuncios conectadas correctamente.][4]{: style="max-width:80%;"}

Tu conexión con Criteo se aplicará a nivel del espacio de trabajo Braze. Si tu administrador de Criteo te elimina de tu cuenta de anuncios de Criteo, Braze detectará un token no válido. Como resultado, tus Canvases activos usando Criteo mostrarán errores, y Braze no podrá sincronizar usuarios.

### Paso 2: Configure sus criterios de entrada en Canvas

Al crear audiencias para el seguimiento de anuncios, es posible que desee incluir o excluir a determinados usuarios en función de sus preferencias, y con el fin de cumplir con las leyes de privacidad, como el derecho de "No vender ni compartir" en virtud de la [CCPA](https://oag.ca.gov/privacy/ccpa). Los vendedores deben implementar los filtros pertinentes para la elegibilidad de los usuarios dentro de sus criterios de entrada en Canvas. A continuación enumeramos algunas opciones.

Si has recopilado el [IDFA de iOS a través del SDK de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), podrás utilizar el filtro Seguimiento de anuncios habilitado. Seleccione el valor como verdadero para enviar únicamente a los usuarios a los destinos de Audience Sync en los que hayan optado por participar.

![][11]

Si está recopilando `opt-ins`, `opt-outs`, `Do Not Sell Or Share` o cualquier otro atributo personalizado relevante, debe incluirlos en los criterios de entrada de Canvas como filtro:

![][12]

Para obtener más información sobre cómo cumplir estas leyes de Protección de Datos dentro de la plataforma Braze, consulte la [Asistencia Técnica sobre Protección de Datos]({{site.baseurl}}/dp-technical-assistance/).

### Paso 3: Añadir un paso de sincronización de audiencia con Criteo

Añada un componente a su lienzo y seleccione **Sincronización con el público**.

![Flujo de trabajo de los pasos anteriores para añadir un componente de Audiencia de Criteo en el Flujo de Canvas.][9]{: style="max-width:35%;"} ![Flujo de trabajo de los pasos anteriores para añadir un componente de Audiencia de Criteo en el Flujo de Canvas.][10]{: style="max-width:28%;"}

### Paso 4: Configuración de la sincronización

Haga clic en el botón **Público personalizado** para abrir el editor de componentes.

Selecciona **Criteo** como socio de Audience Sync deseado. 

![][6]

A continuación, seleccione la cuenta de anuncios de Criteo que desee. En el menú desplegable **Elegir un público nuevo o existente**, escriba el nombre de un público nuevo o existente.

{% tabs %}
{% tab Crear una nueva audiencia %}
**Crear una nueva audiencia**<br>
Introduzca un nombre para el nuevo público, seleccione **Añadir usuarios al público** y seleccione los campos que desea sincronizar con Criteo. A continuación, guarde su público haciendo clic en el botón **Crear público** situado en la parte inferior del editor de pasos.

![Vista ampliada del paso en Canvas Audiencia personalizada. Aquí se selecciona la cuenta publicitaria deseada y se crea una nueva audiencia.]({% image_buster /assets/img/criteo/criteo3.png %})

Los usuarios recibirán una notificación en la parte superior del editor de pasos si la audiencia se crea correctamente o si surgen errores durante este proceso. Los usuarios también pueden hacer referencia a este público para la eliminación de usuarios más adelante en el recorrido Canvas, ya que el público se creó en modo borrador.

![Una alerta que aparece después de crear un nuevo público en el componente Canvas.]({% image_buster /assets/img/criteo/criteo1.png %})

Al lanzar un Canvas con un público nuevo, Braze sincroniza los usuarios casi en tiempo real a medida que entran en el componente Sincronización de público.
{% endtab %}
{% tab Sincronización con un público existente %}
**Sincronización con un público existente**<br>
Braze también ofrece la posibilidad de añadir usuarios a las audiencias existentes de Criteo para garantizar que estas audiencias están actualizadas. Para sincronizar con una audiencia existente, escribe el nombre de la audiencia existente en el desplegable y **Añadir a la audiencia**. A continuación, Braze añadirá usuarios casi en tiempo real cuando entren en el componente de sincronización de audiencias.

![Vista ampliada del paso en Canvas Audiencia personalizada. Aquí se seleccionan la cuenta publicitaria deseada y el público existente.]({% image_buster /assets/img/criteo/criteo8.png %})

{% endtab %}
{% endtabs %}

### Paso 5: Lanzar Canvas

Una vez que hayas configurado la Sincronización de tu audiencia con Criteo, ¡simplemente inicia el Canvas! Se creará la nueva audiencia, y los usuarios que fluyan a través del paso Sincronización de Audiencias pasarán a esta audiencia en Criteo. Si su Canvas contiene componentes posteriores, sus usuarios avanzarán al siguiente paso en su recorrido de usuario.

Puede ver la audiencia en Criteo accediendo a su cuenta de administrador de anuncios y seleccionando Segmentos en la **Biblioteca de Audiencias** de la navegación. En la página **Segmentos**, puedes ver el tamaño de cada audiencia cuando alcance ~1.000.

![La biblioteca de audiencias muestra el segmento, el ID, la fuente, el tipo, el tamaño, el uso actual y la última actualización.][0]

## Sincronización de usuarios y consideraciones sobre el límite de velocidad

A medida que los usuarios alcanzan el paso de Sincronización de Audiencia, Braze sincronizará estos usuarios casi en tiempo real respetando también los límites de velocidad de la API de Criteo. Lo que esto significa en la práctica es que Braze intentará procesar por lotes el mayor número de usuarios cada 5 segundos antes de enviarlos a Snapchat.

El límite de velocidad de la API de Criteo establece no más de 250 solicitudes por minuto. Si un cliente de Braze alcanza este límite de velocidad, Braze the Canvas volverá a intentar la sincronización durante un máximo de ~13 horas. Si la sincronización no es posible, estos usuarios aparecen en la lista de la métrica Users Errored. 

## Comprender los análisis

La siguiente tabla incluye métricas y descripciones que le ayudarán a comprender mejor los análisis de su componente Audience Sync.

| Métrica | Descripción |
| --- | --- |
| Has entrado | Número de usuarios que entraron en este componente para ser sincronizados con Criteo. |
| Continúa con el paso siguiente | Cuántos usuarios avanzaron al siguiente componente, si lo hay. Todos los usuarios avanzarán automáticamente si este es el último paso en la rama Canvas. |
| Usuarios sincronizados | Número de usuarios que se han sincronizado correctamente con Criteo. |
| Usuarios no sincronizados | Número de usuarios que no se han sincronizado debido a que faltan campos para coincidir. |
| Usuarios pendientes | Número de usuarios procesados actualmente por Braze para sincronizar en Criteo. |
| Usuarios con errores | Número de usuarios que no se sincronizaron con Criteo debido a un error de la API tras unas 13 horas de reintentos. Las causas potenciales de los errores pueden incluir un token Criteo inválido o si la audiencia fue eliminada en Criteo. |
| Has salido de Canvas | Número de usuarios que han salido del Canvas. Esto ocurre cuando el último paso de un Canvas es un componente de Sincronización de Audiencias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Recuerde que se producirá un retraso en los informes de las métricas de usuarios sincronizados y usuarios con errores debido a la descarga masiva y al reintento de 13 horas, respectivamente.
{% endalert %}

## Solución de problemas

{% details ¿Qué debo hacer si recibo un error de token no válido? %}
Sólo tienes que desconectar y volver a conectar tu cuenta de Criteo en la página del socio de Criteo. Asegúrese con su administrador de Criteo de que dispone de los permisos adecuados para la cuenta publicitaria con la que desea sincronizar.
{% enddetails %}

{% details ¿Por qué no se puede iniciar mi Canvas? %}
Asegúrese de que su cuenta de anuncios de Criteo se ha conectado correctamente a Braze en la página de socios de Criteo.

Asegúrese de haber seleccionado una cuenta publicitaria, introducido un nombre para el nuevo público y seleccionado los campos que coincidan
{% enddetails %}

{% details ¿Cómo sé si los usuarios han coincidido después de pasar los usuarios a Criteo? %}
Criteo no proporciona esta información para sus propias políticas de privacidad de datos.
{% enddetails %}

{% details ¿A cuántas audiencias puede dar soporte Criteo? %}
En este momento, sólo puedes tener 1000 audiencias en tu cuenta de Criteo. 

Si superas este límite, Braze te notificará que no podemos crear nuevas audiencias. 

Deberá acceder a su cuenta de anuncios de Criteo y eliminar las audiencias que ya no utilice.
{% enddetails %} 

[0]: {% image_buster /assets/img/criteo/criteo.png %}
[1]: {% image_buster /assets/img/criteo/criteo1.png %}
[2]: {% image_buster /assets/img/criteo/criteo2.png %}
[3]: {% image_buster /assets/img/criteo/criteo3.png %}
[4]: {% image_buster /assets/img/criteo/criteo4.png %}
[5]: {% image_buster /assets/img/criteo/criteo5.png %}
[6]: {% image_buster /assets/img/criteo/criteo6.png %}
[7]: {% image_buster /assets/img/criteo/criteo7.png %}
[8]: {% image_buster /assets/img/criteo/criteo8.png %}
[9]: {% image_buster /assets/img/criteo/criteo9.png %}
[10]: {% image_buster /assets/img/criteo/criteo10.png %}
[11]: {% image_buster /assets/img/criteo/criteo11.png %}
[12]: {% image_buster /assets/img/criteo/criteo12.png %}
