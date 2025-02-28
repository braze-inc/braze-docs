---
nav_title: Sheetlabs
article_title: Sheetlabs
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Sheetlabs, einem Service, mit dem Sie Ihre Marketingkampagnen mit Daten aus Tabellenkalkulationen personalisieren können."
alias: /partners/sheetlabs/
page_type: partner
search_tag: Partner

---

# Sheetlabs

> [Sheetlabs][1] ist eine Plattform, mit der Sie Tabellenkalkulationen in leistungsstarke, gut dokumentierte APIs verwandeln können. Sie können Daten aus Google Sheets oder Excel importieren, sie in eine API umwandeln und diese API dann in anderen Anwendungen, wie z.B. Braze, verwenden.

Die Integration von Sheetlabs und Braze ermöglicht es Ihnen, [Connected Content][2] zu nutzen, um Sheetlabs APIs in Ihre Braze-Marketingkampagnen einzubinden. Diese Funktion wird häufig verwendet, um eine Brücke zwischen einem Google Spreadsheet (das direkt vom Marketingteam aktualisiert wird) und Braze-Vorlagen zu schlagen. So können Sie mit Braze-Vorlagen mehr erreichen, z. B. Übersetzungen oder größere Sätze von benutzerdefinierten Attributen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Sheetlabs Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Sheetlabs-Konto][1]. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Mit der Integration von Braze und Sheetlabs können Sie die folgenden Anwendungsfälle realisieren:

1. **Trennen Sie den Zugriff des Vermarkters vom Zugriff auf Braze-Kampagnen**: Einige Teams möchten vermeiden, dass alle Mitarbeiter Zugriff auf die direkte Konfiguration von Braze-Vorlagen und -Inhalten haben. Stattdessen wollen sie, dass die Mitarbeiter Marketinginhalte in einer Tabelle aktualisieren. Sheetlabs bildet die Brücke zwischen Tabellenkalkulationen und Braze und kann in Echtzeit aktualisiert werden.
2. **Übersetzungen**: Braze-Vorlagen unterstützen von Haus aus keine Übersetzungen. Wenn Sie mehrere Sprachen unterstützen möchten, müssen Sie mehrere Vorlagen erstellen. Durch die Verwendung von Sheetlabs in Verbindung mit Braze können Sie eine einzige Braze-Vorlage verwenden, die in mehrere Sprachen übersetzt ist.
3. **Erweitern von benutzerdefinierten Attributen**: Braze bietet eine bestimmte Anzahl von benutzerdefinierten Attributen, die konfiguriert werden können. Wenn Sie Sheetlabs in Verbindung mit Braze verwenden, können Sie über diese anfängliche Zuteilung hinaus weitere benutzerdefinierte Attribute hinzufügen.

Weitere Informationen zu diesen Anwendungsfällen finden Sie bei [Sheetlabs][3].

## Integration

### Schritt 1: Importieren Sie Ihre Tabellenkalkulation in Sheetlabs

Laden Sie in Sheetlabs eine Excel-Tabelle hoch, oder verknüpfen Sie Ihr Google-Konto und importieren Sie ein Google Sheet. 

- Um eine Excel-Tabelle zu importieren, klicken Sie in der Menüleiste auf **Datentabellen** und dann auf **Aus CSV/Excel importieren**.
- Um aus Google Sheets zu importieren, klicken Sie in der Menüleiste auf **Datentabellen** und dann auf **Aus Google importieren**. Sie müssen dann Ihre Google-Anmeldedaten eingeben und das Blatt importieren.

Sie können sich auch dafür entscheiden, Ihr Google Sheet zu synchronisieren. Das bedeutet, dass Sheetlabs automatisch die neuesten Daten aus Ihrem Google Sheet abruft, wenn sich diese ändern.

Vergewissern Sie sich, dass Sie die Braze-Benutzer-ID in Ihre Kalkulationstabelle aufnehmen oder etwas anderes, das Sie später als Nachschlagewerk verwenden können.

### Schritt 2: Erstellen Sie eine API in Sheetlabs

Als nächstes gehen Sie in Sheetlabs zu **APIs > API erstellen** und geben Ihrer API einen Namen. Sie werden wahrscheinlich Abfragen über ein Nachschlagefeld aus Ihrer Kalkulationstabelle zulassen wollen, wie z.B. die Braze-Benutzer-ID.

Jetzt sollten Sie in der Lage sein, mit einem Link wie diesem auf Ihre API zuzugreifen:<br> [`https://sheetlabs.com/ACME/email1_translations?country=en`][4].

### Schritt 3: Verwenden Sie die API in Braze Connected Content

Nun, da Ihre API zugänglich ist, können Sie sie in Ihren Aufrufen für Connected Content verwenden. Hier sehen Sie ein Beispiel dafür, wie eine Übersetzungsvorlage aussehen könnte:

{% raw %}
```js
{% connected_content https://sheetlabs.com/ACME/email1_translations?country={{${country}}} :save translations %}

{{translations[0].greeting}} {{${first_name}}},

{{translations[0].message_body}}
```
{% endraw %}

{% alert tip %}
Weitere Beispiele und Hinweise zur Integration mit Sheetlabs finden Sie in der [Sheetlabs-Dokumentation](https://app.sheetlabs.com/docs/producers/braze/).
{% endalert %}


[1]: https://sheetlabs.com/
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[3]: https://app.sheetlabs.com/docs/producers/braze/
[4]: https://sheetlabs.com/ACME/email1_translations?country=en