---
nav_title: RudderStack
article_title: RudderStack
description: "Este artículo describe la asociación entre Braze y RudderStack, una infraestructura de datos de clientes de código abierto que ofrece una integración perfecta de Braze para sus aplicaciones Android, iOS y web. Con RudderStack, puede enviar los datos de los eventos de sus clientes dentro de la aplicación directamente a Braze para su análisis contextual."
page_type: partner
search_tag: Partner

---

# RudderStack

> [Rudderstack](https://rudderstack.com/) es una infraestructura de datos de clientes de código abierto para recopilar y enrutar datos de eventos de clientes a tu almacén de datos preferido y a docenas de otros proveedores de análisis, como Braze. Está preparado para la empresa y ofrece un sólido marco de transformación para procesar tus datos de eventos sobre la marcha.

La integración de Braze y Rudderstack ofrece una integración de SDK nativa para tus aplicaciones Android, iOS y Web, y una integración de servidor a servidor desde tus servicios backend.

## Requisitos previos

| Requisito | Descripción |
| --- | --- |
| Cuenta RudderStack | Se requiere una [cuenta Rudderstack](https://app.rudderstack.com/) para beneficiarse de esta asociación. |
| Fuente configurada | Un [Origin](https://www.rudderstack.com/docs/dashboard-guides/sources/) es esencialmente el origen de cualquier dato enviado a Rudderstack, como sitios web, aplicaciones móviles o servidores backend. Es necesario configurar la fuente antes de configurar Braze como destino en RudderStack. |
| Clave REST API de Braze | Una clave de API REST de Braze con permisos `users.track`, `users.identify`, `users.delete` y `users.alias.new`.<br><br>Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Clave de la aplicación Braze | Para obtener la clave de tu aplicación en el panel de control de Braze, ve a **Ajustes** > **Ajustes de la aplicación** > **Identificación** y busca el nombre de tu aplicación. Guarda la cadena de identificadores asociada.
| Centro de datos | Tu centro de datos se alinea con tu [instancia de]({{site.baseurl}}/api/basics/#endpoints) panel de Braze.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integración

### Paso 1: Añadir una fuente

Para empezar a enviar datos a Braze, primero debe asegurarse de que se ha configurado una fuente en su aplicación RudderStack. Visita [Rudderstack](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#getting-started) para saber cómo configurar tu origen de datos.

### Paso 2: Configurar destino

Ahora que su fuente de datos está configurada, en el panel de RudderStack, seleccione **AÑADIR DESTINO** en **Destinos**. En la lista de destinos disponibles, seleccione **Braze** y haga clic en **Siguiente**.

En el destino Braze, proporciona la clave de la aplicación, la clave de API REST de Braze, el clúster de datos y la opción de SDK nativo (sólo en modo dispositivo). La opción SDK nativo utilizará el SDK nativo de Braze para enviar eventos si está alternada. 

![]({% image_buster /assets/img/RudderStack/braze_settings.png %}){: style="max-width:70%;margin-bottom:15px;border:none;"}

### Paso 3: Elija el tipo de integración

Puede elegir integrar las bibliotecas web y nativas del lado del cliente de RudderStack con Braze utilizando uno de los siguientes enfoques:

- [Lado a lado / modo dispositivo](#device-mode)**:** RudderStack enviará los datos de eventos a Braze directamente desde su cliente (navegador o aplicación móvil).
- [Servidor a servidor / modo nube](#cloud-mode)**:** El SDK de Braze envía los datos de los eventos directamente a Rudderstack, que los transforma y enruta a Braze.
- [Modo híbrido](#hybrid-mode)**:** Utiliza el modo híbrido para enviar eventos autogenerados y generados por el usuario de iOS y Android a Braze utilizando una única conexión.

{% alert note %}
Más información sobre los [modos de conexión](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/) de RudderStack y las ventajas de cada uno.
{% endalert %}

#### Integración lado a lado (modo dispositivo) {#device-mode}

Con este modo, puedes enviar tus eventos a Braze utilizando el SDK de Braze configurado en tu sitio web o aplicación móvil.

Configura los mapeados al SDK de Rudderstack para tu plataforma en el repositorio Braze de GitHub, como se describe en [métodos compatibles](#supported-methods):

- [Android](https://github.com/rudderlabs/rudder-integration-braze-android)
- [iOS](https://github.com/rudderlabs/rudder-integration-braze-ios/tree/master)
- [Swift](https://github.com/rudderlabs/rudder-integration-braze-swift)
- [Web](https://github.com/rudderlabs/rudder-sdk-js/tree/production/src/integrations/Braze)
- [React Native](https://github.com/rudderlabs/rudder-sdk-react-native/tree/develop/libs/rudder-integration-braze-react-native)
- [Flutter](https://github.com/rudderlabs/rudder-sdk-flutter/tree/develop/packages/integrations/rudder_integration_braze_flutter)

Para completar la integración del modo dispositivo, consulte las instrucciones detalladas de RudderStack para [añadir Braze a su proyecto](https://rudderstack.com/docs/destinations/marketing/braze/#adding-device-mode-integration).

#### Integración de servidor a servidor (modo nube) {#cloud-mode}

En este modo, el SDK envía los datos del evento directamente al servidor Rudderstack. A continuación, RudderStack transforma estos datos y los encamina al destino deseado. Esta transformación se realiza en el backend de RudderStack mediante el módulo transformador de RudderStack.

Para habilitar la integración, tendrá que asignar los métodos RudderStack a Braze, como se describe en [métodos compatibles](#supported-methods).

{% alert note %}
Los SDK del lado del servidor de Rudderstack (Java, Python, Node.js, Go, Ruby) sólo admiten el modo nube. Esto se debe a que sus SDK del lado del servidor funcionan en el backend de Rudderstack y no pueden cargar ningún SDK específico de Braze.
{% endalert %}

{% alert important %}
La integración de servidor a servidor no es compatible con las funciones de Braze UI, como las notificaciones push o la mensajería dentro de la aplicación. Sin embargo, estas funciones son compatibles con la integración del modo dispositivo.
{% endalert %}

#### Modo híbrido {#hybrid-mode}

Utiliza el modo híbrido para enviar todos los eventos a Braze desde tus fuentes iOS y Android. 

Cuando eliges el modo híbrido para enviar eventos a Braze, Rudderstack:
1. Inicializa el SDK Braze.
2. Envía todos los eventos generados por el usuario (identificar, rastrear, página, pantalla y grupo) a Braze sólo a través del modo nube y bloquea su envío a través del modo dispositivo.
3. Envía los eventos autogenerados (mensajes in-app, notificaciones push que requieren el SDK Braze) a través del modo dispositivo.

Para [enviar eventos a través del modo híbrido](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-events-in-hybrid-mode), utilice la opción de modo híbrido mientras conecta su fuente al destino Braze. A continuación, añade la integración Braze a tu proyecto.

## Paso 4: Configurar ajustes adicionales

Tras completar la configuración inicial, configure los siguientes ajustes para recibir correctamente sus datos en Braze:

- **Habilitar grupos de suscripción en llamada de grupo**: Habilite esta configuración para enviar el estado del grupo de suscripción en sus eventos de grupo. Para más información, consulta [Grupo](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#group).
- **Operación Utilizar atributos personalizados**: Active esta opción si desea utilizar la funcionalidad [de atributos personalizados anidados]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) en Braze para crear segmentos y personalizar sus mensajes utilizando un objeto de atributo personalizado. Para más información, consulta [Enviar rasgos de usuario como atributos personalizados anidados](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#send-user-traits-as-nested-custom-attributes).
- **Seguimiento de eventos para usuarios anónimos**: Active esta opción para realizar un seguimiento de la actividad anónima del usuario y enviar esta información a Braze.

### Configuración del modo de dispositivo

La siguiente configuración sólo es aplicable si envías eventos a Braze a través del [modo dispositivo](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/#device-mode):

- **Filtrado de eventos del lado del cliente**: Esta configuración te permite especificar qué eventos deben bloquearse o permitirse en Braze. Para obtener más información sobre esta configuración, consulte [Filtrado de eventos en el lado del cliente](https://www.rudderstack.com/docs/sources/event-streams/sdks/event-filtering/).
- **Deduplicar rasgos**: Habilita esta configuración para deduplicar los rasgos del usuario en la llamada a [`identify`](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#identify).
- **Mostrar registros de Braze**: Esta configuración sólo es aplicable cuando se utiliza el [SDK de JavaScript](https://www.rudderstack.com/docs/sources/event-streams/sdks/rudderstack-javascript-sdk/) como fuente. Actívala para mostrar los registros de Braze a tus usuarios.
- **Categorías de cookies de OneTrust**: Esta configuración le permite asociar los grupos de consentimiento de cookies de [OneTrust](https://www.rudderstack.com/docs/sources/event-streams/sdks/onetrust/javascript/) a Braze.

## Métodos admitidos

Braze admite los métodos Rudderstack identificar, seguimiento, pantalla, página, grupo y alias.

{% tabs %}
{% tab Identificador %}

El [método `identify`](https://rudderstack.com/docs/destinations/marketing/braze/#identify) RudderStack asocia a los usuarios con sus acciones. RudderStack captura un ID de usuario único y rasgos opcionales asociados a ese usuario, como nombre, correo electrónico, dirección IP, etc.

**Gestión de deltas para identificar llamadas**<br>
Si envías eventos a Braze a través del modo dispositivo, puedes ahorrar costes deduplicando tus llamadas a `identify`. Para ello, habilita la configuración del panel Deduplicar rasgos. RudderStack envía entonces sólo los atributos (traits) cambiados o modificados a Braze.

**Eliminar un usuario**<br>
Puede eliminar un usuario en Braze utilizando la [regulación Supresión con Borrado](https://www.rudderstack.com/docs/api/data-regulation-api/#adding-a-suppression-with-delete-regulation) de la [API de Regulación de Datos](https://www.rudderstack.com/docs/api/data-regulation-api/) de RudderStack.

{% endtab %}
{% tab Seguimiento %}

El [método`track` ](https://rudderstack.com/docs/destinations/marketing/braze/#track) de RudderStack captura todas las actividades del usuario y las propiedades asociadas a dichas actividades.

**Pedido realizado**<br>
Al utilizar [la API de comercio electrónico de Rudderstack](https://www.rudderstack.com/docs/event-spec/ecommerce-events-spec/) para llamar al método de seguimiento de un evento con el nombre `Order Completed`, RudderStack envía los productos incluidos en ese evento a Braze como [`purchases`]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).

{% endtab %}
{% tab Pantalla %}

El [método`screen` ](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#screen) de RudderStack le permite registrar las vistas de pantalla móvil de sus usuarios con cualquier información adicional sobre la pantalla vista.

{% endtab %}
{% tab Página %}

El [método`page` ](https://rudderstack.com/docs/destinations/marketing/braze/#page) de Rudderstack te permite registrar las páginas vistas de tu sitio web. También captura cualquier otra información relevante sobre esa página.

{% endtab %}
{% tab Grupo %}

El [método`group` ](https://rudderstack.com/docs/destinations/marketing/braze/#group) de RudderStack permite asociar un usuario a un grupo.

**Estado del grupo de suscripción**<br>
Para actualizar el estado del grupo de suscripción, active el ajuste "Habilitar grupos de suscripción en llamada de grupo" en el panel de RudderStack y envíe el estado del grupo de suscripción en la llamada de grupo.

{% endtab %}
{% tab Alias %}

El [método`alias` ](https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#alias) de RudderStack permite fusionar diferentes identidades de un usuario conocido. Ten en cuenta que Rudderstack sólo admite la llamada de alias para Braze en modo nube.

{% endtab %}
{% endtabs %}

## Enviar rasgos de usuario como atributos personalizados anidados

Puede enviar los rasgos de usuario a Braze como atributos personalizados anidados y realizar operaciones de adición, actualización y eliminación en ellos. Para ello, habilita el ajuste "Utilizar atributos personalizados Panel de operaciones" en Rudderstack mientras configuras el destino Braze. Esta función sólo está disponible en modo nube.

Puede enviar los rasgos de usuario como atributos personalizados anidados en sus eventos `identify` con el siguiente formato:
```javascript
rudderanalytics.identify("1hKOmRA4GRlm", {
  "cars": {
    "add": [{
      "age": 27,
      "id": 1,
      "name": "Alex Keener"
    }],
    "update": [{
        "age": 30,
        "id": 2,
        "identifier": "id",
        "name": "Rowan"
      },
      {
        "age": 27,
        "id": 1,
        "identifier": "id",
        "name": "Mike"
      }
    ]
  },
  "country": "USA",
  "email": "alex@example.com",
  "firstName": "Alex",
  "gender": "M",
  "pets": [{
      "breed": "beagle",
      "id": 1,
      "name": "Scooby",
      "type": "dog"
    },
    {
      "breed": "calico",
      "id": 2,
      "name": "Garfield",
      "type": "cat"
    }
  ]
})
```

Para enviar los rasgos de usuario como atributos de usuario personalizados a través de las llamadas `track`, `page`, o `screen`, pase `traits` como campo contextual en el evento:
```javascript
rudderanalytics.track("Product Viewed", {
    revenue: 8.99,
    currency: "USD",
 },{
  "traits": {
    "cars": {
      "add": [{
        "age": 27,
        "id": 1,
        "name": "Alex Keener"
      }],
      "update": [{
          "age": 30,
          "id": 2,
          "identifier": "id",
          "name": "Mike"
        },
        {
          "age": 27,
          "id": 1,
          "identifier": "id",
          "name": "Rowan"
        }
      ]
    },
    "city": "Disney",
    "country": "USA",
    "email": "alexa@example.com",
    "firstName": "Alexa",
    "gender": "woman",
    "pets": [{
        "breed": "beagle",
        "id": 1,
        "name": "Scooby",
        "type": "dog"
      },
      {
        "breed": "calico",
        "id": 2,
        "name": "Garfield",
        "type": "cat"
      }
    ]
  }
});
```

{% alert note %}
Para las operaciones de actualización y eliminación, `identifier` es una clave necesaria. Si las operaciones add, update o remove no están presentes en el array anidado, RudderStack utiliza por defecto la operación create para crear las propiedades. Consulte [Matriz de objetos]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) para obtener más información sobre el envío de atributos personalizados anidados.
{% endalert %}

