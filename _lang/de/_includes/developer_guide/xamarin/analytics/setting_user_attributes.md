{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Nutzer:innen Attribute einstellen

Braze bietet Methoden für die Zuweisung von Attributen an Benutzer. Auf dem Dashboard können Sie Ihre Nutzer:innen nach diesen Attributen filtern und segmentieren.

### Standard-Nutzerattribute

Um Nutzer:innen-Attribute zu setzen, die von Braze automatisch gesammelt werden, können Sie die Setter-Methoden verwenden, die mit dem SDK geliefert werden. Sie können zum Beispiel den Vornamen des Nutzers:innen festlegen:

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

In den [Anleitungen zur Android-Integration]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android) finden Sie eine ausführliche Beschreibung der besten Praktiken und Schnittstellen für das Attribut Tracking.

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetCustomAttributeWithKey("custom_attribute_key", true);
```

In der [Anleitung zur Integration von iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift) finden Sie eine ausführliche Diskussion über bewährte Verfahren und Schnittstellen für das Attribut Tracking.

{% endtab %}
{% endtabs %}
