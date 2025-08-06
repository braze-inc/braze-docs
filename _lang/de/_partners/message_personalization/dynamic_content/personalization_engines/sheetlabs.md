---
nav_title: Sheetlabs
article_title: Sheetlabs
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Sheetlabs, einem Dienst, mit dem Sie Ihre Kampagnen mit Daten aus Tabellenkalkulationen personalisieren können."
alias: /partners/sheetlabs/
page_type: partner
search_tag: Partner
---

# Sheetlabs

> [Sheetlabs](https://sheetlabs.com/) ist eine Plattform, die es Ihnen erlaubt, Tabellenkalkulationen in leistungsstarke, gut dokumentierte APIs zu verwandeln. Sie können Daten aus Google Sheets oder Excel importieren, sie in eine API umwandeln und diese API dann in anderen Anwendungen wie Braze verwenden.
_Diese Integration wird von Sheetlabs gepflegt._

## Über die Integration

Die Integration von Sheetlabs und Braze erlaubt es Ihnen, [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/) zu nutzen, um Sheetlabs APIs in Ihre Kampagnen für Braze einzubinden. Diese Funktion wird in der Regel verwendet, um eine Brücke zwischen einem Google Spreadsheet (das direkt vom Marketing Team aktualisiert wird) und Braze Templates zu schlagen. So können Sie mit Braze Templates mehr erreichen, z. B. Übersetzungen oder größere Mengen angepasster Attribute.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Sheetlabs Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Sheetlabs-Konto](https://sheetlabs.com/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Die Integration von Braze und Sheetlabs lässt die folgenden Anwendungsfälle zu:

1. **Trennung des Marketer-Zugriffs vom Zugriff auf die Kampagnen von Braze**: Einige Teams möchten vermeiden, dass alle Mitarbeiter Zugriff auf die direkte Konfiguration von Braze-Templates und -Inhalten haben. Stattdessen wollen sie, dass ihre Mitarbeiter Marketing-Inhalte in einer Tabellenkalkulation aktualisieren. Sheetlabs bildet die Brücke zwischen Tabellenkalkulationen und Braze und kann in Realtime aktualisiert werden.
2. **Übersetzungen**: Braze Templates unterstützen von Haus aus keine Übersetzungen. Wenn Sie mehrere Sprachen unterstützen möchten, müssen Sie mehrere Templates erstellen. Wenn Sie Sheetlabs in Verbindung mit Braze verwenden, können Sie ein einziges Braze Template verwenden, das in mehrere Sprachen übersetzt ist.
3. **Erweitern Sie angepasste Attribute**: Braze bietet eine bestimmte Anzahl angepasster Attribute, die konfiguriert werden können. Wenn Sie Sheetlabs in Verbindung mit Braze verwenden, können Sie über diese anfängliche Zuteilung hinaus weitere angepasste Attribute hinzufügen.

Weitere Informationen zu diesen Anwendungsfällen finden Sie bei [Sheetlabs](https://app.sheetlabs.com/docs/producers/braze/).

## Integration

### Schritt 1: Importieren Sie Ihre Tabellenkalkulation in Sheetlabs

Laden Sie in Sheetlabs eine Excel-Tabelle hoch, oder verknüpfen Sie Ihr Google-Konto und importieren Sie ein Google Sheet. 

- Um eine Excel-Tabelle zu importieren, klicken Sie in der Menüleiste auf **Datentabellen** und dann auf **Aus CSV/Excel importieren**.
- Um aus Google Sheets zu importieren, klicken Sie in der Menüleiste auf **Datentabellen** und dann auf **Aus Google importieren**. Sie müssen dann Ihre Zugangsdaten für Google angeben und das Blatt importieren.

Sie können sich auch dafür entscheiden, Ihr Google Sheet synchron zu halten. Das bedeutet, dass Sheetlabs automatisch die neuesten Daten aus Ihrem Google Sheet abruft, wenn sich diese ändern.

Vergewissern Sie sich, dass Sie die Nutzer:innen ID von Braze in Ihre Kalkulationstabelle aufnehmen oder etwas anderes, das Sie später als Nachschlagewerk verwenden können.

### Schritt 2: Erstellen Sie eine API in Sheetlabs

Als nächstes gehen Sie in Sheetlabs zu **APIs > API erstellen** und geben Ihrer API einen Namen. Wahrscheinlich möchten Sie Abfragen über ein Nachschlagefeld aus Ihrer Kalkulationstabelle zulassen, z.B. die Nutzer:in von Braze.

Jetzt sollten Sie in der Lage sein, über einen Link wie diesen auf Ihre API zuzugreifen:<br> [`https://sheetlabs.com/ACME/email1_translations?country=en`](https://sheetlabs.com/ACME/email1_translations?country=en).

### Schritt 3: Verwenden Sie die API in Braze Connected-Content

Da Ihre API nun zugänglich ist, können Sie sie in Ihren Connected-Content-Aufrufen verwenden. Hier sehen Sie ein Beispiel dafür, wie eine Vorlage für Übersetzungen aussehen könnte:

{% raw %}
```js
{% connected_content https://sheetlabs.com/ACME/email1_translations?country={{${country}}} :save translations %}

{{translations[0].greeting}} {{${first_name}}},

{{translations[0].message_body}}
```
{% endraw %}
{% alert tip %}
Weitere Beispiele und Hinweise zur Integration mit Sheetlabs finden Sie in der [Sheetlabs Dokumentation](https://app.sheetlabs.com/docs/producers/braze/).
{% endalert %}
