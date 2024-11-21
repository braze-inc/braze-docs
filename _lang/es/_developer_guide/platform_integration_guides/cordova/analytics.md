---
nav_title: Análisis
article_title: Integración de análisis
page_order: 3
---

# Integración de análisis

> Aprende a integrar análisis para el SDK Braze de Cordova.

{% multi_lang_include cordova/prerequisites.md %}

## Registro de eventos personalizados

Para registrar eventos personalizados, utiliza el método `logCustomEvent()`. Para obtener instrucciones más detalladas, consulta las guías de [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events) e [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/) para registrar eventos personalizados.

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logCustomEvent("CUSTOM_EVENT_WITH_PROPERTIES", properties);
```

## Registrar compras

Para registrar las compras, utiliza el método `logPurchase()`. Para obtener instrucciones más detalladas, consulta las guías de [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/#logging-purchases) e [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/logging_purchases/) para registrar compras.

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% alert tip %}
Si quieres registrar las compras a nivel de pedido en lugar de a nivel de producto, puedes utilizar el nombre del pedido o la categoría del pedido como `product_id`. Consulta nuestra [especificación del objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para obtener más información.
{% endalert %}

## Configuración de atributos personalizados

Para establecer atributos personalizados, utiliza el método `setCustomUserAttribute()`. Para obtener instrucciones más detalladas, consulta las guías de [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) e [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/) sobre la configuración de atributos personalizados.

```javascript
BrazePlugin.setCustomUserAttribute("KEY", "VALUE");
```

## Configuración de los ID de usuario

Para configurar los ID de usuario, utiliza el método `changeUser()`. Para obtener instrucciones más detalladas, consulta las guías de [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) e [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/) para configurar los ID de usuario.

```javascript
BrazePlugin.changeUser("USER_ID");
```
