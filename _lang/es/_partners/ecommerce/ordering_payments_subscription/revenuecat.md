---
nav_title: RevenueCat
article_title: RevenueCat
description: "La integración de RevenueCat y Braze le permite sincronizar automáticamente los eventos del ciclo de vida de compra y suscripción de sus clientes en todas las plataformas. Esto le permite crear campañas que reaccionan a la etapa del ciclo de vida de suscripción de sus clientes, como la participación con los clientes que optaron por salir durante su prueba gratuita o el envío de recordatorios a los clientes con problemas de facturación."
alias: /partners/revenuecat/
page_type: partner
search_tag: Partner

---

# RevenueCat

> [RevenueCat](https://www.revenuecat.com/) es la única fuente de información sobre el estado de tu suscripción en iOS, Android y Web. Tanto si está creando una nueva aplicación como si ya tiene millones de suscriptores, puede utilizar RevenueCat para crear compras dentro de la aplicación multiplataforma, gestionar sus productos y suscriptores y analizar sus datos, sin necesidad de código de servidor.

_Esta integración está mantenida por RevenueCat._

## Sobre la integración

La integración de RevenueCat y Braze le permite sincronizar automáticamente los eventos del ciclo de vida de compra y suscripción de sus clientes en todas las plataformas. Esto le permite crear campañas que reaccionan a la etapa del ciclo de vida de suscripción de sus clientes, como la participación con los clientes que optaron por salir durante su prueba gratuita o el envío de recordatorios a los clientes con problemas de facturación.

## Requisitos previos

Como mínimo, tendrá que habilitar la integración desde el panel de RevenueCat para conectar RevenueCat a Braze. Si está utilizando el SDK de Braze, puede utilizar los SDK de RevenueCat y Braze juntos para mejorar la integración asegurándose de que se está utilizando el mismo identificador de cliente en ambos sistemas.

| Requisito | Descripción |
|---|---|
| Cuenta y aplicación RevenueCat | Se necesita una [cuenta RevenueCat](https://app.revenuecat.com/login) para beneficiarse de esta asociación. También debe tener una aplicación RevenueCat configurada. |
| SDK RevenueCat | Además del SDK de Braze necesario, recomendamos instalar el [SDK de Reven](https://docs.revenuecat.com/docs/configuring-sdk) ueCat para proporcionar alias de usuario a RevenueCat. |
| instancia de Braze | Puedes obtener tu instancia de Braze a través de tu administrador de incorporación a Braze o en la [página de resumen de la API]({{site.baseurl}}/api/basics/#endpoints).<br><br>RevenueCat requiere que la instancia de Braze envíe desde el servidor al punto final REST Braze correcto. |
| Clave REST API de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Clave REST API de prueba Braze (opcional) | Se puede utilizar una clave API de prueba para las compras de prueba y de producción si desea que estas solicitudes se envíen a instancias Braze independientes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Ejemplos 

- Active una campaña de incorporación que destaque sus funciones premium cuando un cliente inicie una prueba gratuita.
- Enviar un recordatorio para actualizar la información de facturación cuando se recibe un evento de "Problema de facturación".
- Envíe una encuesta de opinión después de que un cliente cancele una prueba gratuita. 

## Integración

### Paso 1: Establecer identidad de usuario Braze

En el SDK de Braze, puede configurar el ID de usuario de Braze para que coincida con el ID de usuario de la aplicación RevenueCat, lo que garantiza que los eventos enviados desde Braze y RevenueCat se puedan sincronizar con el mismo usuario.

Configure el Braze SDK con el mismo ID de usuario de la aplicación que RevenueCat o utilice el método Braze SDK `.changeUser()`.

{% tabs local %}
{% tab swift %}
```swift
// Configure Purchases SDK
Purchases.configure(withAPIKey: "public_sdk_key", appUserID: "my_app_user_id")

// Change user in Braze SDK
Appboy.sharedInstance()?.changeUser("my_app_user_id")

// Optional User Alias Object attributes
Purchases.shared.setAttributes(["$brazeAliasName" : "name", 
                             "$brazeAliasLabel" : "label"])
```
{% endtab %}
{% tab objetivo-c %}
```objc
// Configure Purchases SDK
[RCPurchases configureWithAPIKey:@"public_sdk_key" appUserID:@"my_app_user_id"];

// Change user in Braze SDK
[[Appboy sharedInstance] changeUser:@"my_app_user_id"];

// Optional User Alias Object attributes
[[RCPurchases sharedPurchases] setAttributes:@{
    @"$brazeAliasName": @"name",
    @"$brazeAliasLabel": @"label"
}];
```
{% endtab %}
{% tab java %}
```java
// Configure Purchases SDK
Purchases.configure(this, "public_sdk_key", "my_app_user_id");

// Change user in Braze SDK
Braze.getInstance(context).changeUser(my_app_user_id);

// Optional User Alias Object attributes
Map<String, String> attributes = new HashMap<String, String>();
attributes.put("$brazeAliasName", "name");
attributes.put("$brazeAliasLabel", "label");

Purchases.getSharedInstance().setAttributes(attributes);
```
{% endtab %}
{% endtabs %}

#### Enviar objeto alias de usuario a Braze (opcional) 

Si desea enviar un identificador de usuario único alternativo distinto del identificador de usuario de la aplicación RevenueCat, actualice los usuarios con los siguientes datos como atributos de suscriptor de RevenueCat.

| Clave | Descripción |
|---|---|
| `$brazeAliasName` | El Braze `alias_name` en el [objeto alias de usuario]({{site.baseurl}}/api/objects_filters/user_alias_object/) |
| `$brazeAliasLabel` | El Braze `alias_label` en el [objeto alias de usuario]({{site.baseurl}}/api/objects_filters/user_alias_object/) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ambos atributos son necesarios para que el [objeto alias de usuario]({{site.baseurl}}/api/objects_filters/user_alias_object/) se envíe junto con los datos del evento. Estas propiedades pueden configurarse manualmente, como cualquier otro [atributo del suscriptor de RevenueCat](https://docs.revenuecat.com/docs/subscriber-attributes). En el primer paso se muestran fragmentos de código de ejemplo.

### Paso 2: Enviar eventos RevenueCat a Braze

Después de configurar el SDK de compras de RevenueCat y el SDK de Braze para que tengan la misma identidad de usuario, puede activar la integración y configurar los nombres de los eventos desde el panel de RevenueCat.

1. Navegue hasta su proyecto en el panel de control de RevenueCat y busque la tarjeta **Integraciones** en el menú de la izquierda. Selecciona **\+ Nuevo**.
2. A continuación, seleccione **Braze** entre las integraciones disponibles y añada su instancia de Braze y su clave de API REST de Braze. 
3. Introduzca los nombres de eventos que RevenueCat enviará o elija los nombres de eventos por defecto. Encontrará más información sobre los eventos disponibles en [el paso 3](#configure-event-names).
4. Seleccione si desea que RevenueCat informe de los ingresos (después del corte de la tienda de aplicaciones) o de los ingresos (ventas brutas).

![Configuración de Braze en RevenueCat con campos para la instancia de Braze, el identificador de la clave de API y el identificador del sandbox.]({% image_buster /assets/img/revenuecat/braze_settings_in_revenuecat.png %})

### Paso 3: Configurar los nombres de los eventos {#configure-event-names}

Introduzca los nombres de eventos que RevenueCat enviará o seleccione entre los nombres de eventos por defecto seleccionando **Usar Nombres de Eventos por Defecto**. Los eventos que RevenueCat admite enviar se describen en el siguiente cuadro.

| Evento | Descripción |
|---|---|
| Compra inicial | La primera compra de un producto de suscripción con renovación automática que no contenga una prueba gratuita. |
| Prueba iniciada | El inicio de una prueba gratuita de un producto de suscripción con renovación automática. |
| Prueba convertida | Cuando un producto de suscripción con renovación automática pasa de un periodo de prueba gratuito a un periodo normal de pago. |
| Prueba cancelada | Cuando un usuario desactiva las renovaciones de un producto de suscripción con renovación automática durante un periodo de prueba gratuito. |
| Renovación | Cuando se renueva un producto de suscripción autorrenovable, o un usuario vuelve a comprar el producto de suscripción autorrenovable tras un lapso en su suscripción. |
| Anulación | Cuando un usuario desactiva las renovaciones de un producto de suscripción de renovación automática durante el periodo de pago normal. |
| Compra sin suscripción | La compra de cualquier producto que no sea una suscripción de renovación automática. |
| Caducidad | Cuando caduca una suscripción. |
| Problema de facturación | Cuando ha habido un problema al intentar cobrar al usuario. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para los eventos que incluyan ingresos, RevenueCat registrará automáticamente este importe junto con el evento en Braze, como las conversiones de prueba y las renovaciones.

## Mediante esta integración

Después de configurar los ajustes de Braze en RevenueCat, los eventos comenzarán a fluir automáticamente de RevenueCat a Braze sin ninguna otra acción por su parte.

## Personalización

### Añadir una clave de API de sandbox para Pruebas

Si sólo proporcionas una clave de API REST de Braze a RevenueCat, sólo se enviarán los eventos de producción. Si también quieres enviar eventos de prueba de sandbox, [crea otra clave de API REST Braze]({{site.baseurl}}/api/basics/#app-group-rest-api-keys) y añádela a tu configuración Braze en RevenueCat.


