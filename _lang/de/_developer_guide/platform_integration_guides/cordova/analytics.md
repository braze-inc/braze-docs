---
nav_title: Analytics
article_title: Analytics-Integration
page_order: 3
---

# Analytics-Integration

> Erfahren Sie, wie Sie Analytics für das Cordova Braze SDK integrieren können.

{% multi_lang_include cordova/prerequisites.md %}

## Protokollierung benutzerdefinierter Ereignisse

Um angepasste Events zu protokollieren, verwenden Sie die Methode `logCustomEvent()`. Ausführlichere Anweisungen finden Sie in den Anleitungen für [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events) und [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/) zur Protokollierung angepasster Events.

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logCustomEvent("CUSTOM_EVENT_WITH_PROPERTIES", properties);
```

## Einkäufe protokollieren

Um Einkäufe zu protokollieren, verwenden Sie die Methode `logPurchase()`. Ausführlichere Anleitungen finden Sie in den Anleitungen für [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/#logging-purchases) und [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/logging_purchases/) zum Protokollieren von Käufen.

```javascript
var properties = {};
properties["KEY"] = "VALUE";
BrazePlugin.logPurchase("PRODUCT_ID", 10, "USD", 5, properties);
```

{% alert tip %}
Wenn Sie Einkäufe auf der Bestellebene statt auf der Produktebene protokollieren möchten, können Sie den Bestellnamen oder die Bestellkategorie als `product_id` verwenden. Weitere Informationen finden Sie in unserer [Spezifikation für Kaufobjekte]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions).
{% endalert %}

## Benutzerdefinierte Attribute einstellen

Um angepasste Attribute festzulegen, verwenden Sie die Methode `setCustomUserAttribute()`. Ausführlichere Anweisungen finden Sie in den Anleitungen für [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) und [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/) zum Einstellen angepasster Attribute.

```javascript
BrazePlugin.setCustomUserAttribute("KEY", "VALUE");
```

## Nutzer:innen IDs festlegen

Um Nutzer-IDs festzulegen, verwenden Sie die Methode `changeUser()`. Ausführlichere Anweisungen finden Sie in den Anleitungen für [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) und [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/) zum Einrichten von Nutzer:innen.

```javascript
BrazePlugin.changeUser("USER_ID");
```
