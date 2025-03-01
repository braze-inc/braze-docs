---
nav_title: Analytics
article_title: Analytics für Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 4
description: "Dieser Artikel behandelt die iOS-, Android- und FireOS-Analytics für die Xamarin-Plattform."

---
 
# Xamarin Analytics

> Lernen Sie, wie Sie Analysen für die Xamarin-Plattform erstellen und überprüfen können.

## Sitzungs-Tracking

Das Braze SDK meldet Sitzungsdaten, die vom Braze Dashboard verwendet werden, um das Benutzerengagement und andere Analysen zu berechnen, die für das Verständnis Ihrer Benutzer wichtig sind. Auf der Grundlage der folgenden Sitzungssemantik generiert unser SDK Datenpunkte für "Sitzungsbeginn" und "Sitzungsende", die die Sitzungsdauer und die Anzahl der Sitzungen berücksichtigen, die im Braze-Dashboard angezeigt werden.

Um eine Nutzer-ID festzulegen oder eine Sitzung zu starten, verwenden Sie die Methode `ChangeUser`, die einen Parameter für die Nutzer-ID benötigt.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).ChangeUser("user_id");
```

In der [Anleitung zur Android Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) erfahren Sie, wann und wie Sie eine Nutzer:innen ID festlegen und ändern können.

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.ChangeUser("user_id");
```

In den [Anleitungen zur Integration von iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/) finden Sie eine ausführliche Beschreibung, wann und wie Sie eine Nutzer:innen ID festlegen und ändern können.

{% endtab %}
{% endtabs %}

## Protokollierung benutzerdefinierter Ereignisse

Sie können angepasste Events in Braze unter `LogCustomEvent` aufzeichnen, um mehr über das Nutzungsverhalten Ihrer App zu erfahren und Ihre Nutzer:innen nach ihren Aktionen im Dashboard zu segmentieren.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).LogCustomEvent("event_name");
```

In den [Anleitungen zur Android-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/) finden Sie eine ausführliche Beschreibung der besten Praktiken und Schnittstellen für das Event-Tracking.

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.LogCustomEvent("event_name");
```

In der [Anleitung zur Integration von iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/) finden Sie eine ausführliche Diskussion über bewährte Methoden und Schnittstellen für das Event-Tracking.

{% endtab %}
{% endtabs %}

## Einkäufe protokollieren

Erfassen Sie In-App-Käufe mit `LogPurchase`, um Ihre Einnahmen im Zeitverlauf und über verschiedene Einnahmequellen hinweg zu verfolgen und Ihre Nutzer nach ihrem Lifetime-Value zu segmentieren.

Braze unterstützt Einkäufe in mehreren Währungen. Einkäufe, die Sie in einer anderen Währung als dem USD melden, werden im Dashboard in USD auf der Grundlage des Wechselkurses an dem Tag, an dem sie gemeldet wurden, angezeigt.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).LogPurchase("product_id", "USD", new Java.Math.BigDecimal(3.50));
```

In der [Anleitung zur Android-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/) finden Sie eine ausführliche Beschreibung der besten Praktiken und Schnittstellen für das Umsatz-Tracking.

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.LogPurchase("product_id", "USD", 3.50);
```

In der [Anleitung zur Integration von iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/logging_purchases/) finden Sie eine ausführliche Beschreibung der besten Praktiken und Schnittstellen für das Umsatz-Tracking.

{% endtab %}
{% endtabs %}

### Käufe auf der Ebene der Bestellung protokollieren

Wenn Sie Einkäufe auf der Bestellebene statt auf der Produktebene protokollieren möchten, können Sie den Bestellnamen oder die Bestellkategorie als `product_id` verwenden. Weitere Informationen finden Sie in unserer [Spezifikation für Kaufobjekte]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions). 

### Reservierte Tasten

Die folgenden Schlüssel sind reserviert und können **nicht** als Kauf-Details verwendet werden:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

## Benutzerdefinierte Attribute protokollieren

Braze bietet Methoden für die Zuweisung von Attributen an Benutzer. Auf dem Dashboard können Sie Ihre Nutzer:innen nach diesen Attributen filtern und segmentieren.

### Standard-Benutzerattribute

Um Nutzer automatisch von Braze gesammelte Attribute zuzuweisen, können Sie Setter-Methoden im SDK verwenden. Sie können zum Beispiel den Vornamen des Nutzers:innen festlegen:

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).CurrentUser.SetFirstName("first_name");
```

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetFirstName("first_name");
```

{% endtab %}
{% endtabs %}

Die folgenden Attribute werden unterstützt:

- Vorname
- Nachname
- Geschlecht
- Geburtsdatum
- Heimatstadt
- Land
- Telefonnummer
- E-Mail

### Angepasste Benutzerattribute

Zusätzlich zu den vordefinierten Methoden für Standard-Benutzerattribute bietet Braze auch angepasste Attribute unter `SetCustomUserAttribute`, um Daten aus Ihren Anwendungen zu tracken.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).CurrentUser.SetCustomUserAttribute("custom_attribute_key", true);
```

In den [Anleitungen zur Android-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) finden Sie eine ausführliche Beschreibung der besten Praktiken und Schnittstellen für das Attribut Tracking.

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetCustomAttributeWithKey("custom_attribute_key", true);
```

In der [Anleitung zur Integration von iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/) finden Sie eine ausführliche Diskussion über bewährte Verfahren und Schnittstellen für das Attribut Tracking.

{% endtab %}
{% endtabs %}

## Standort-Tracking

Ein Beispiel für die Protokollierung und das Tracking von Analytics finden Sie in unseren Beispielanwendungen [Android MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/MainActivity.cs) und [iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp/MainPage.xaml.cs).

{% tabs %}
{% tab android %}
Weitere Informationen finden Sie in der [Anleitung zur Integration von Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/).
{% endtab %}

{% tab ios %}
Um lokales Tracking zu unterstützen, siehe [iOS: Verwendung des Standorts im Hintergrund](http://developer.xamarin.com/guides/cross-platform/application_fundamentals/backgrounding/part_4_ios_backgrounding_walkthroughs/location_walkthrough/) und die [Anleitung zur iOS Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/locations_and_geofences/).
{% endtab %}
{% endtabs %}

