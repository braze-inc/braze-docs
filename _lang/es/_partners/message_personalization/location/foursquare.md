---
nav_title: Foursquare
article_title: Foursquare
alias: /partners/foursquare/
description: "Este artículo de referencia describe la asociación entre Braze y Foursquare, una plataforma de datos de ubicación, que permite desencadenar eventos en tiempo real basados en la ubicación."
page_type: partner
search_tag: Partner

---

# Foursquare

{% multi_lang_include video.html id="G2ZoJqZGqrU" align="right" %}

> [Foursquare](https://foursquare.com/) es una plataforma de datos de ubicación que proporciona orientación de datos de ubicación en tus campañas de Braze. Utiliza el SDK Pilgrim de Foursquare en aplicaciones iOS y Android para desencadenar eventos en tiempo real basados en la ubicación, lo que te permitirá aprovechar las potentes capacidades de orientación geográfica de Foursquare para enviar mensajes relevantes y personalizados con Braze.

_Esta integración está mantenida por Foursquare._

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta Foursquare | Se necesita una cuenta de Foursquare para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el dashboard de Braze desde **Configuración** > **Claves API**. |
| Espacio de trabajo Braze e ID de aplicación | El espacio de trabajo Braze y los ID de aplicación se encuentran en la [consola para desarrolladores]({{site.baseurl}}/api/api_key/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integración

Para integrar las dos plataformas, debes integrar los dos SDK y mapear los campos de usuario coincidentes. Tras integrar el SDK de Pilgrim, recibirás eventos de ubicación en el dispositivo o en un webhook. 

### Paso 1: Mapear campos de ID de usuario

Para mapear correctamente los campos entre los dos SDK, establece el mismo ID de usuario en ambos sistemas utilizando el método [`changeUser` ]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/#setting-user-ids) en el SDK de Braze y el método `setUserId` de [`PilgrimUserInfo`](https://developer.foursquare.com/docs/pilgrim-sdk/advanced-setup-guide#custom-user-data) en el SDK Pilgrim.

### Paso 2: Configurar la consola Pilgrim
![Una imagen de la consola Pilgrim pidiendo el ID de grupo, el ID de la aplicación Android y el ID de la aplicación iOS.]({% image_buster /assets/img_archive/pilgrim-dev-console.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Encuentra el espacio de trabajo y los ID de la aplicación en la consola para desarrolladores Braze. A continuación, introduce tu clave de API REST de Braze y los ID de aplicación en la Consola Foursquare Pilgrim.

Una vez que hayas configurado la Consola Pilgrim, el SDK Pilgrim registrará los eventos de ubicación y los reenviará a Braze, permitiéndote reorientar y segmentar a los clientes cualificados. Consulta el [sitio web del desarrollador de Foursquare](https://developer.foursquare.com/) para obtener más información.

{% alert important %}
El SDK de Pilgrim requiere que habilites los servicios de ubicación.
{% endalert %}

## Desencadenar mensajes

Una vez configurada la integración, puedes crear una campaña o Canvas que actúe a partir de los eventos de ubicación generados por el SDK de Pilgrim. Esta ruta de integración es ideal para la mensajería en tiempo real justo después de que los usuarios entren en un lugar de interés o para la comunicación de seguimiento diferida después de que se hayan ido, como una nota de agradecimiento o un recordatorio.

Para enviar una campaña que enviará mensajes en función de una ubicación establecida:
- Crea una campaña Braze o Canvas que envíe con **entrega basada en acciones**
- Para desencadenar, utiliza un evento personalizado de `arrival` con un filtro de propiedades de evento para `locationType`, como se muestra en la siguiente captura de pantalla.

![Una campaña basada en acciones en el paso de entrega que muestra la "llegada" seleccionada como la opción "realizar evento personalizado", donde "locationType" es igual a "home".]({% image_buster /assets/img_archive/action-based-campaign.png %})

## Reorientación

Para reorientar a tus usuarios, utiliza el SDK Pilgrim para establecer un atributo personalizado `last_location` en los perfiles de usuario de tus usuarios Braze. A continuación, puedes utilizar la comparación `matches regex` para reorientar a los usuarios que fueron a una ubicación concreta en el mundo real, por ejemplo, segmentando a todos los usuarios que estuvieron recientemente en una pizzería.

![Una campaña basada en acciones en el paso de usuarios objetivo que muestra que "last_location" es igual a "Restaurante de Pizza".]({% image_buster /assets/img_archive/last-location-segment.png %})

También puedes segmentar en Braze a los usuarios que visitaron un tipo concreto de local basándote en `primaryCategoryId` de Foursquare en una ventana de tiempo determinada. Para aprovechar este punto de datos para tus casos de uso de reorientación, registra `primaryCategoryId` como una propiedad del evento durante tu proceso de segmentación de la audiencia. Para identificar a los usuarios y las propiedades utilizadas por la API de Foursquare y el SDK de Pilgrim, consulta el [sitio del desarrollador de Foursquare](https://developer.foursquare.com/).


