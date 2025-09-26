---
nav_title: Segment Engage
article_title: Segment Engage
page_order: 3
alias: /partners/segment_personas/
alias: /partners/segment_engage/
alias: /partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_personas/

description: "Este artículo de referencia describe la asociación entre Braze y Segment, una plataforma de datos de clientes que recopila y redirige información entre fuentes de tu stack de marketing."
page_type: partner
search_tag: Partner

---

# Segment Engage

> [Segment](https://segment.com) es una plataforma de datos de clientes que te ayuda a recopilar, limpiar y activar los datos de tus clientes. Este artículo de referencia ofrece un resumen de la conexión entre [Braze y Segment Engage](https://segment.com/docs/destinations/braze/#Engage), además de describir los requisitos y procesos para una implementación y uso adecuados.

La integración de Braze y Segment te permite utilizar [Engage](https://segment.com/docs/engage/), el creador de audiencias integrado de Segment, para crear segmentos de usuarios basados en datos que ya hayas recopilado de diversas fuentes. A continuación, estas audiencias se sincronizarán con Braze como una cohorte, o se denotarán en el perfil de usuario mediante [atributos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) o [eventos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) que pueden utilizarse para crear segmentos Braze que se utilizarán en la reorientación de campañas y Canvas.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta de Segment | Se necesita una [cuenta de Segment](https://app.segment.com/login) para beneficiarse de esta asociación. |
| Destino en la nube Braze | Ya debes haber configurado [Braze como destino]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) en tu integración de Segment.<br><br>Esto incluye proporcionar el centro de datos Braze y la clave de API REST correctos en tu [configuración de conexión]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings). |
| Clave de importación de datos Braze | Para sincronizar audiencias de Engage con Braze como cohortes, debes generar una clave de importación de datos.<br><br>La importación de cohortes está en acceso temprano; ponte en contacto con tu administrador del éxito del cliente de Braze para acceder a esta característica. |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cohortes Integración en el destino

### Paso 1: Crea una audiencia interactiva
1. En Segment, ve a la pestaña **Audiencias** de Engage y haz clic en **Nuevo**.
2. Crea tu audiencia. Un rayo en la esquina superior de la página indicará si la audiencia se actualiza en tiempo real.
3. A continuación, selecciona Braze como destino.
4. Obtén una vista previa de tu audiencia haciendo clic en **Revisar y crear**. Por defecto, Segment consulta todos los datos históricos para establecer el valor actual del rasgo computado y la audiencia. Para omitir estos datos, desmarca **Relleno histórico**.

### Paso 2: Captura tu clave de importación de datos de cohortes

En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Segmento**.

Aquí encontrarás tu punto final REST y generarás tu clave de importación de datos Braze. Una vez generada la clave, puedes crear una nueva o invalidar una existente.

### Paso 3: Conecta el destino Cohortes de Braze
Sigue [las instrucciones de Segment](https://segment.com/docs/connections/destinations/catalog/actions-braze-cohorts/#getting-started) sobre la configuración del destino Cohortes para sincronizar tus audiencias de Engage como cohortes con Braze.

### Paso 4: Crea un segmento Braze a partir de la audiencia Engage
En Braze, ve a **Segmentos**, crea un nuevo segmento y selecciona **Cohortes de segmentos** como filtro. Desde aquí, puedes elegir qué cohorte de Segment deseas incluir. Una vez creado el segmento de cohorte de Segment, puedes seleccionarlo como filtro de audiencia al crear una campaña o Canvas.

![]({% image_buster /assets/img/segment/segment3.png %})

## Integración del Modo Nube

### Paso 1: Crear un rasgo computado de Segment o audiencia

1. En Segment, ve a la pestaña **Rasgos computados** o **Audiencias** en **Engage**, y haz clic en **Nuevo**.
2. Crea tu rasgo computarizado o audiencia. Un rayo en la esquina superior de la página indicará si el cálculo se actualiza en tiempo real.
3. A continuación, selecciona **Braze** como destino. 
4. Obtén una vista previa de tu audiencia haciendo clic en **Revisar y crear**. Por defecto, Segment consulta todos los datos históricos para establecer el valor actual del rasgo computado y la audiencia. Para omitir estos datos, desmarca **Relleno histórico**.
5. En la configuración de rasgo computado o audiencia, ajusta la configuración de conexión en función de cómo quieras que se envíen tus datos a Braze.

#### Rasgos computados y audiencias

[Los rasgos](https://segment.com/docs/engage/audiences/computed-traits/) y [audiencias computados](https://segment.com/docs/Engage/audiences/) pueden enviarse a Braze como atributos personalizados o eventos personalizados.
- Los rasgos y audiencias enviados mediante la llamada `identify` aparecerán en Braze como atributos personalizados.
- Los rasgos y audiencias enviados mediante la llamada `track` aparecerán en Braze como eventos personalizados.

Puedes elegir qué método utilizar (o utilizar ambos) cuando conectes el rasgo computado al destino Braze.

{% tabs %}
{% tab Identificar %}

Puedes enviar rasgos y audiencias computados a Braze como llamadas a `identify` para crear atributos personalizados en Braze. 

Por ejemplo, si tienes un atributo computado en Engage para "Último producto visto", encontrarás `last_product_viewed_item` en el perfil de usuario de Braze, en **Atributos personalizados**. Si, en cambio, se tratara de una audiencia de Engage, encontrarías a tu audiencia en **Atributos personalizados** configurados como `true`.

| Rasgo computado | Audiencias |
| -------------- | --------- |
| ![La sección de atributos personalizados dentro de un perfil de usuario lista "last_product_viewed_item" como "Sweater".]({% image_buster /assets/img/segment/last_viewed-id-braze.png %}) | ![La sección de atributos personalizados dentro de un perfil de usuario lista "dormant_shopper" como "true".]({% image_buster /assets/img/segment/dormant-identify-braze.png %}) |

{% endtab %}
{% tab Seguimiento %}

Puedes enviar rasgos computados y audiencias a Braze como llamadas a `track` para crear eventos personalizados en Braze. 

Siguiendo con el ejemplo anterior, si un usuario tiene un rasgo computado para "Último producto visto", aparecerá en los perfiles Braze de los usuarios como `Trait Computed` con el recuento correspondiente y la marca de tiempo más reciente en **Eventos personalizados**. Si, en cambio, se tratara de una audiencia de Engage, encontrarías la audiencia, el recuento y la fecha y hora más recientes en **Atributos personalizados** configurados como `true`.

| Rasgo computado | Audiencias |
| -------------- | --------- |
| ![La sección de eventos personalizados dentro de un perfil de usuario enumera "Rasgo computado" "1" vez, siendo la última vez "hace 20 horas".]({% image_buster /assets/img/segment/last_viewed-track-braze.png %}) | ![La sección de atributos personalizados dentro de un perfil de usuario muestra la hora "Audiencia introducida" "1", siendo la última hora "9 de marzo a la 1:45".]({% image_buster /assets/img/segment/dormant-track-braze.png %}) |

{% endtab %}
{% endtabs %}

### Paso 2: Segmentar usuarios en Braze

En Braze, para crear un segmento de estos usuarios, ve a **Segmentos** en **Interacción**, crea un nuevo segmento y dale un nombre a tu segmento. A continuación, en función de la llamada que hayas utilizado:
- **Identifica**: Selecciona **atributo personalizado** como filtro y localiza tu atributo personalizado. A continuación, utiliza la opción "coincide con regex" (rasgo) o la opción "es igual a" (audiencia) e introduce la variable adecuada.
- **Realiza un seguimiento**: Selecciona **evento personalizado** como filtro y localiza tu evento personalizado. A continuación, utiliza la opción "más que", "menos que" o "exactamente", e introduce el valor que desees. Esto dependerá de cómo quieras definir tu segmento.

Una vez guardado, puedes hacer referencia a este segmento durante la creación de Canvas o de la campaña en el paso de segmentación de usuarios.

## Tiempo de sincronización

Aunque la configuración predeterminada para la conexión de Braze a Segment Engage es `Realtime`, hay algunos filtros que descalificarán a la persona para la sincronización en tiempo real, incluidos algunos filtros basados en el tiempo que restringen el tamaño de tu audiencia en el momento del envío del mensaje.

## Prueba del depurador de Segment

El panel de Segment proporciona una característica de "Depurador" que permite a los clientes probar si los datos de un "Origen" se transfieren a un "Destino" como se esperaba.

Esta característica se conecta al [punto final `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze , lo que significa que solo puede utilizarse para usuarios identificados (usuarios que ya tienen un ID de usuario para su perfil de usuario Braze).

Esto no funcionará para una integración en paralelo con Braze. No se transmitirá ningún dato del servidor si no has introducido la información correcta de la API REST de Braze.

