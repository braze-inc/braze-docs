---
nav_title: Audiencias de AppsFlyer
article_title: Audiencias de AppsFlyer
alias: /partners/appsflyer_audiences/
description: "Este artículo de referencia describe la asociación entre Braze y AppsFlyer Audiences, una función de la plataforma AppsFlyer que permite crear y conectar eficazmente segmentos de audiencia con redes asociadas."
page_type: partner
search_tag: Partner

---

# Audiencias de AppsFlyer

> Este artículo describe cómo importar cohortes de usuarios de AppsFlyer a Braze mediante la integración de [AppsFlyer Audiences](https://www.appsflyer.com/product/audiences/). Para más información sobre la integración de AppsFlyer y sus otras funcionalidades, como la atribución móvil, consulte el [artículo principal sobre AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/).

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta AppsFlyer | Se necesita una cuenta AppsFlyer para beneficiarse de esta asociación. |
| Aplicación para iOS o Android | Esta integración es compatible con aplicaciones iOS y Android. Dependiendo de su plataforma, es posible que se requieran fragmentos de código en su aplicación. Encontrará más detalles sobre estos requisitos en el paso 1 del proceso de integración. |
| SDK de AppsFlyer | Además del SDK de Braze necesario, debes instalar el [SDK de AppsFlyer](https://support.appsflyer.com/hc/en-us/articles/207032126-SDK-integration-overview). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración de la importación de datos

### Paso 1: Configurar el SDK de AppsFlyer

Para utilizar esta integración, debe pasar el ID externo Braze del usuario a AppsFlyer utilizando la función `setPartnerData()` del SDK de AppsFlyer:

#### Android 
```java
Map<String, Object> brazeData = new HashMap<>();
partnerData.put("external_user_id", "some-braze-external-id-value");
AppsFlyerLib.getInstance().setPartnerData("braze_int", brazeData);
```

#### iOS
```objc
NSDictionary *brazeInfo = @{
     @"external_user_id":@"some-braze-external-id-value"
};
[[AppsFlyerLib shared]  setPartnerDataWithPartnerId:@"braze_int" partnerInfo:brazeInfo];
```

### Paso 2: Obtener la clave de importación de datos Braze

En Braze, vaya a **Integraciones de socios** > **Socios tecnológicos** y seleccione **AppsFlyer**. 

Aquí encontrarás el punto final REST y generarás tu clave de importación de datos Braze. Una vez generada la clave, puede crear una nueva o invalidar una existente. La clave de importación de datos y el endpoint REST se utilizan en el siguiente paso cuando se configura un postback en el dashboard de AppsFlyer.<br><br>![La casilla "Importación de datos mediante importación de cohortes" en la página de tecnología de AppsFlyer. En este cuadro se te muestra la clave de importación de datos y el punto final REST.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_data_import_key.png %}){: style="max-width:90%;"}

### Paso 3: Configurar una conexión Braze en AppsFlyer Audiences

1. En [AppsFlyer Audiences](https://support.appsflyer.com/hc/en-us/articles/115002689186-Audiences-guide#managing-connections), vaya a la pestaña **Conexiones** y haga clic en **Añadir conexión de socio**.
2. Selecciona Braze como socio y dale un nombre a la conexión.
3. Proporciona la clave de importación de datos y el punto final REST de Braze.
4. Guarde la conexión, y estará disponible para vincularla a cualquier público nuevo o existente.

![Página de configuración de la conexión de socios de la plataforma de audiencias AppsFlyer. La parte inferior de las imágenes muestra que la casilla ID externo de Braze está marcada.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_braze_connection.png %}){: style="max-width:80%;"}

### Paso 4: Uso de cohortes de AppsFlyer Audiences en Braze

Una vez que se ha cargado un público de AppsFlyer en Braze, puede utilizarlo como filtro al definir segmentos en Braze seleccionando el filtro **Cohortes de AppsFlyer**.

![Filtro de atributos de usuario "Cohortes AppsFlyer" seleccionadas.]({% image_buster /assets/img/appsflyer_audiences/appsflyer_cohorts_as_filter.png %})

{% alert important %}
Sólo se añadirán o eliminarán de una cohorte los usuarios que ya existan en Braze. La importación de cohortes no creará nuevos usuarios en Braze.
{% endalert %}

## Coincidencia de usuarios

Los usuarios identificados pueden coincidir por su `external_id` o `alias`. Los usuarios anónimos pueden ser emparejados por su `device_id`. Los usuarios identificados que fueron creados originalmente como usuarios anónimos no pueden ser identificados por su `device_id`, y deben ser identificados por su `external_id` o `alias`.

