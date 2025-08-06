---
nav_title: LinkedIn
article_title: Sincronización de la audiencia de Canvas con LinkedIn
alias: /linkedin_audience_sync/
description: "Este artículo de referencia explicará cómo utilizar Braze Audience Sync con LinkedIn para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más."
Tool:
  - Canvas
page_order: 4

---

# Sincronización de audiencia con LinkedIn

Mediante la Sincronización de la audiencia Braze con LinkedIn, las marcas pueden añadir datos de usuarios de su integración Braze a las listas de clientes de LinkedIn para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más. Cualquier criterio que utilices normalmente para desencadenar un mensaje (push, correo electrónico, SMS, webhook, etc.) en un Canvas de Braze basado en tus datos de usuario puede ahora desencadenar un anuncio para ese usuario en tus listas de clientes de LinkedIn.

**Entre los casos de uso habituales de la Sincronización de audiencias se incluyen**:

- Dirigirse a usuarios de alto valor a través de múltiples canales para impulsar las compras o la participación
- Reorientar a los usuarios menos receptivos a otros canales de marketing
- Crear audiencias de supresión para evitar que los usuarios reciban anuncios cuando ya son consumidores fieles a tu marca.

Esta característica permite a las marcas controlar qué datos propios específicos se comparten con LinkedIn. En Braze, se presta la máxima atención a las integraciones con las que puedes y no puedes compartir tus datos propios. Para más información, consulte nuestra [política de privacidad](https://www.braze.com/privacy).

{% alert important %}
La Sincronización de audiencias con LinkedIn está actualmente en fase beta. Ponte en contacto con tu director de cuentas de Braze si quieres participar en la beta.
{% endalert %}

## Requisitos previos

Debes asegurarte de que tienes los siguientes elementos creados, completados o aceptados antes de configurar tu paso de Sincronización con la audiencia de LinkedIn en Canvas.

| Requisito | Origin | Descripción |
| --- | --- | --- |
| Cuenta publicitaria en LinkedIn | [LinkedIn](https://www.linkedin.com/campaignmanager) | Una cuenta publicitaria activa en LinkedIn vinculada a tu marca.<br><br>Asegúrate de que has aceptado las condiciones pertinentes de LinkedIn para acceder a esa cuenta y utilizarla, y de que tu administrador de LinkedIn te ha concedido los permisos adecuados para gestionar Audiencias. |
| Términos y políticas de LinkedIn | LinkedIn | Aceptas cumplir cualquiera de los términos, políticas, directrices y documentación requeridos por LinkedIn en relación con tu uso de la Sincronización de audiencias de LinkedIn, incluidos los términos, políticas, directrices y documentación incorporados por referencia a los mismos, que pueden incluir los de LinkedIn: Condiciones de los servicios, Acuerdo de anuncios, Acuerdo de procesamiento de datos y Directrices de la comunidad profesional. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integración

### Paso 1: Conéctate a LinkedIn

En el panel de Braze, ve a **Socios tecnológicos** y selecciona **LinkedIn**. En la sección **Sincronizar audiencia de LinkedIn**, selecciona **Conectar LinkedIn**.

![La página de tecnología de LinkedIn en Braze incluye una sección de resumen y otra de sincronización con la audiencia de LinkedIn con el botón de LinkedIn conectado.]({% image_buster /assets/img/linkedin/linkedin3.png %}){: style="max-width:75%;"}

A continuación, se te redirigirá a la página LinkedIn OAuth para que autorices a Braze los permisos relacionados con tu integración de Sincronización de audiencia. Cuando hayas seleccionado **Confirmar**, se te redirigirá de nuevo a Braze para que selecciones las cuentas de anuncios de LinkedIn con las que deseas sincronizar. 

![Se selecciona "Braze Self Service" como cuenta publicitaria a conectar.]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

Una vez que te hayas conectado correctamente, volverás a la página del socio, donde podrás ver qué cuentas están conectadas y desconectar las cuentas existentes.

![Una cuenta de LinkedIn conectada correctamente.]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

Tu conexión a LinkedIn se aplicará a nivel del espacio de trabajo Braze. Si tu administrador de LinkedIn te elimina de tu cuenta publicitaria de LinkedIn, Braze detectará un token no válido. Como resultado, tus Lienzos activos utilizando LinkedIn mostrarán errores, y Braze no podrá sincronizar usuarios.

### Paso 2: Configura tus criterios de entrada en Canvas

Al crear audiencias para el seguimiento de anuncios, es posible que desees incluir o excluir a determinados usuarios en función de sus preferencias, y para cumplir con las leyes de privacidad, como el derecho de "No vender ni compartir" en virtud de la [CCPA](https://oag.ca.gov/privacy/ccpa). Los vendedores deben implementar los filtros pertinentes para la elegibilidad de los usuarios dentro de sus criterios de entrada en Canvas. A continuación enumeramos algunas opciones. 

Si has recopilado el [IDFA de iOS a través del SDK de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overviewother_sdk_customizations/#optional-idfa-collection), podrás utilizar el filtro **Ads Tracking Enabled**. Selecciona el valor como `true` para enviar sólo a los usuarios a los destinos de Audience Sync en los que hayan optado por la adhesión voluntaria. 

![Una audiencia de entrada con el filtro "El seguimiento de anuncios habilitado es verdadero".]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

Si estás recopilando `opt-ins`, `opt-outs`, `Do Not Sell Or Share`, o cualquier otro atributo personalizado relevante, debes incluirlos dentro de tus criterios de entrada en Canvas como filtro:

![Un Canvas con una audiencia de entrada de "opted_in_marketing" igual a "true".]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

Para saber más sobre cómo cumplir estas leyes de Protección de Datos dentro de la plataforma Braze, consulta la [Asistencia Técnica sobre Protección de Datos]({{site.baseurl}}/dp-technical-assistance/).

### Paso 3: Añadir un paso de sincronización de audiencia con LinkedIn

Añade un componente en tu Canvas y selecciona Sincronizar audiencia. Haga clic en el botón **Público personalizado** para abrir el editor de componentes.

![El editor Canvas con la lista de componentes disponibles.]({% image_buster /assets/img/linkedin/linkedin2.png %}){: style="max-width:35%;"} ![El componente de Sincronización de Audiencias seleccionado.]({% image_buster /assets/img/linkedin/linkedin1.png %}){: style="max-width:29%;"}

### Paso 4: Configuración de la sincronización

Selecciona **LinkedIn** como socio de Sincronización de audiencia deseado.

![Los detalles de "Configurar la sincronización de la audiencia" con los múltiples socios a elegir.]({% image_buster /assets/img/linkedin/linkedin.png %}){: style="max-width:70%;"}

A continuación, selecciona la cuenta de anuncios de LinkedIn que desees. En el desplegable **Elegir una audiencia nueva o existente**, escribe el nombre de una audiencia nueva o existente.

![Sincronización de la audiencia con LinkedIn con Braze seleccionada como cuenta publicitaria.]({% image_buster /assets/img/linkedin/linkedin20.png %})

{% tabs %}
{% tab Crear una nueva audiencia %}

**Crear una nueva audiencia**<br>
Introduce un nombre para la nueva audiencia, selecciona **Añadir usuarios a la audiencia** y selecciona los campos que deseas sincronizar con LinkedIn. Para esta integración, actualmente admitimos lo siguiente: 
- Correo electrónico
- Nombre y apellidos
- Android GAID

A continuación, guarda tu audiencia haciendo clic en el botón **Crear audiencia** situado en la parte inferior del editor de pasos.

![Un ejemplo de audiencia de "clientes potenciales" con la cuenta de anuncios Braze seleccionada, la audiencia de "clientes potenciales", la acción para añadir usuarios a la audiencia y el correo electrónico, el GAID de Android y el nombre y apellidos como campos que deben coincidir.]({% image_buster /assets/img/linkedin/linkedin10.png %})

Los usuarios recibirán una notificación en la parte superior del editor de pasos si la audiencia se crea correctamente o si surgen errores durante este proceso. Los usuarios también pueden hacer referencia a este público para la eliminación de usuarios más adelante en el recorrido Canvas, ya que el público se creó en modo borrador.

![Confirmación de que se ha creado la audiencia de "clientes potenciales".]({% image_buster /assets/img/linkedin/linkedin9.png %})

Cuando lanzas un Canvas con una nueva audiencia, Braze sincroniza a los usuarios casi en tiempo real a medida que entran en el componente Sincronización de Audiencias.

{% endtab %}
{% tab Sincronización con un público existente %}

**Sincronízate con una audiencia existente**<br>
Braze también ofrece la posibilidad de añadir usuarios a las audiencias existentes de LinkedIn para confirmar que dichas audiencias están actualizadas. Para sincronizar con una audiencia existente, escribe el nombre de la audiencia existente en el desplegable y selecciona **Añadir a la audiencia**. A continuación, Braze añadirá usuarios casi en tiempo real a medida que entren en el componente Audience Sync.

![Vista ampliada del paso en Canvas Audiencia personalizada. Aquí se seleccionan la cuenta publicitaria deseada y la audiencia existente.]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### Paso 5: Lanzar Canvas

Una vez que hayas configurado la Sincronización de tu Audiencia con LinkedIn, ¡simplemente lanza el Canvas! Se creará la nueva audiencia, y los usuarios que pasen por el paso Sincronizar audiencia pasarán a esta audiencia en LinkedIn. Si tu Canvas contiene componentes posteriores, tus usuarios avanzarán al siguiente paso en su viaje de usuario.

Puedes ver la audiencia en LinkedIn entrando en tu cuenta de publicidad y seleccionando **Audiencias** en la sección **Activos** de la navegación. En la página **Audiencias**, puedes ver el tamaño de cada audiencia después de alcanzar más de 300 miembros.

![Página de LinkedIn que enumera las siguientes métricas para la audiencia dada.]({% image_buster /assets/img/linkedin/linkedin8.png %})

## Consideraciones sobre la sincronización de usuarios y el límite de velocidad

A medida que los usuarios alcancen el Paso de sincronización de audiencia, Braze sincronizará a estos usuarios casi en tiempo real respetando los límites de velocidad de la API de LinkedIn. En la práctica, Braze intentará procesar por lotes el mayor número de usuarios cada 5 segundos antes de enviarlos a LinkedIn.

El límite de velocidad de la API de LinkedIn establece no más de diez consultas por segundo y 100.000 usuarios por solicitud. Si un cliente de Braze alcanza este límite de velocidad, Braze the Canvas reintentará la sincronización durante unas 13 horas. Si la sincronización no es posible, estos usuarios aparecen en la lista de la métrica Users Errored.

## Comprender los análisis

La tabla siguiente incluye métricas y descripciones que te ayudarán a comprender mejor los análisis de tu componente Audience Sync.

| MÉTRICA | DESCRIPCIÓN |
| ------ | ----------- | 
| El usuario ha entrado | Número de usuarios que entraron en este componente para ser sincronizados con LinkedIn. |
| Continúa con el paso siguiente | ¿Cuántos usuarios avanzaron al siguiente componente, si lo hay? Todos los usuarios avanzarán automáticamente si éste es el último paso en Canvas. |
| Usuarios sincronizados | Número de usuarios que se han sincronizado correctamente con LinkedIn. |
| Usuarios no sincronizados | Número de usuarios que no se han sincronizado debido a que faltan campos para coincidir. |
| Usuarios pendientes | Número de usuarios que Braze está procesando actualmente para sincronizarlos con LinkedIn. |
| Usuarios con errores | Número de usuarios que no se sincronizaron con LinkedIn debido a un error de la API tras unas 13 horas de reintentos. Las causas potenciales de los errores pueden incluir un token de LinkedIn no válido o si la audiencia fue eliminada en LinkedIn. |
| Has salido de Canvas | Número de usuarios que han salido del Canvas. Esto ocurre cuando el último paso de un Canvas es un componente de Sincronización de Audiencias. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
Recuerde que se producirá un retraso en los informes de las métricas de usuarios sincronizados y usuarios con errores debido a la descarga masiva y al reintento de 13 horas, respectivamente.
{% endalert %}

{% alert important %}
LinkedIn proporciona métricas adicionales sobre las tasas de coincidencia dentro de su plataforma. Para revisar la coincidencia de tu Sincronización de Audiencia específica, selecciona las métricas del paso Sincronización de Audiencia para ir a la página **Detalles del paso en Canvas**.
<br><br>
Selecciona el socio como **LinkedIn**, tu cuenta de publicidad y la audiencia para ver el tamaño de la audiencia y la tasa de coincidencia de LinkedIn.

![Un ejemplo de métrica de pasos de Audience Sync con 10.000 usuarios introducidos.]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## Preguntas más frecuentes

### ¿Cuánto tardarán en poblarse los tamaños de audiencia en LinkedIn?

Hay un retraso de hasta 48 horas para ver las audiencias dentro de tu cuenta de LinkedIn.

### ¿Cuál es el tamaño mínimo de audiencia para que LinkedIn lo incluya en tu cuenta publicitaria?

La audiencia debe incluir al menos 300 miembros para poblar el tamaño de la audiencia dentro de tu cuenta de LinkedIn.

### ¿Qué debo hacer si recibo un error de token no válido?

Puedes desconectar y volver a conectar tu cuenta de LinkedIn en la página del socio de LinkedIn. Confirma con tu administrador de LinkedIn que tienes los permisos adecuados para la cuenta de publicidad con la que deseas sincronizar.

### ¿Por qué no se puede iniciar mi Canvas?

Confirma que tu cuenta publicitaria de LinkedIn se ha conectado correctamente a Braze en la página del socio de LinkedIn. A continuación, asegúrate de haber seleccionado una cuenta de publicidad, introducido un nombre para la nueva audiencia y seleccionado los campos que coincidan.

### ¿Cómo sé si los usuarios se han emparejado después de pasar los usuarios a LinkedIn?

LinkedIn proporciona información sobre las tasas de coincidencia en su panel. Puedes consultarlo en LinkedIn, en la sección **Audiencias**. Puedes revisar la tasa de coincidencia de tu audiencia de LinkedIn en los detalles del paso en Canvas de tu paso Sincronización de audiencia.

### ¿A cuántas audiencias puede dar soporte LinkedIn?

Actualmente, no hay límite en el número de audiencias en tu cuenta de anuncios de LinkedIn.

### ¿Por qué un segmento está atascado en estado CONSTRUIDO y no se actualiza?

Un segmento se considera no utilizado y se establece en ARCHIVADO después de que no se utilice de forma continuada durante 30 días en un borrador o en una campaña activa. Por ello, un segmento puede aparecer "atascado" en CONSTRUCCIÓN cuando se transmiten actualizaciones a un segmento ARCHIVADO, empujándolo así al estado de CONSTRUCCIÓN, y justo antes de que se archive de nuevo, se transmiten nuevas actualizaciones al segmento no utilizado.


