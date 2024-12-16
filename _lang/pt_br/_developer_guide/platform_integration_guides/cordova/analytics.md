---
nav_title: Análise de dados
article_title: Integração da análise de dados
page_order: 3
---

# Integração da análise de dados

> Saiba como integrar a análise de dados ao Cordova Braze SDK.

{% multi_lang_include cordova/prerequisites.md %}

## Registro de eventos personalizados

Para registrar eventos personalizados, use o método `logCustomEvent()`. Para obter instruções mais detalhadas, consulte os guias do [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events) e [do iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/) para registro de eventos personalizados.

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logCustomEvent("CUSTOM_EVENT_WITH_PROPERTIES", properties);
```

## Registro de compras

Para registrar compras, use o método `logPurchase()`. Para obter instruções mais detalhadas, consulte os guias do [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/#logging-purchases) e [do iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/logging_purchases/) para registro de compras.

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% alert tip %}
Se quiser registrar as compras no nível do pedido em vez de no nível do produto, poderá usar o nome do pedido ou a categoria do pedido como `product_id`. Consulte nossa [especificação de objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para saber mais.
{% endalert %}

## Definição de atributos personalizados

Para definir atributos personalizados, use o método `setCustomUserAttribute()`. Para obter instruções mais detalhadas, consulte os guias [do Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) e [do iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/) sobre a configuração de atributos personalizados.

```javascript
BrazePlugin.setCustomUserAttribute("KEY", "VALUE");
```

## Definição de IDs de usuário

Para definir IDs de usuário, use o método `changeUser()`. Para obter instruções mais detalhadas, consulte os guias do [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) e [do iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/) para definir IDs de usuário.

```javascript
BrazePlugin.changeUser("USER_ID");
```
