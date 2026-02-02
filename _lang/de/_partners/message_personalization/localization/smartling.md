---
nav_title: Smartling
article_title: Smartling
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Smartling, einer cloudbasierten Software für die Lokalisierung. Der Braze Connector unterstützt die Übersetzung von HTML-E-Mail-Vorlagen, Content-Blöcken, Canvase und Nachrichten für Kampagnen."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling](https://www.smartling.com/) ist eine End-to-End Cloud-Übersetzungsmanagement-Software für Kunden, die die Übersetzung von Websites, Anwendungen und Kundenerlebnissen automatisieren möchten.

_Diese Integration wird von Smartling gepflegt._

## Über die Integration

Der Braze Connector unterstützt Übersetzungen für Nachrichten in Kampagnen und Canvase (E-Mail-, Push- und In-App-Nachrichten), E-Mail-Templates und Content-Blöcke. In der folgenden Tabelle finden Sie Informationen zu den unterstützten Kanälen und Features, wenn Sie den neuen Konnektor mit Mehrsprachenunterstützung oder den Legacy-Workflow verwenden möchten.

| Kanal/Feature | Traditioneller Editor (ex. HTML) | Drag-and-Drop-Editor |
| --------------- | ----------------------------- | -------------------- |
| [E-Mail]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email) | ✅ | ✅ |
| [IAM]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message) | ✅ | ✅ |
| [Push]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push) | ✅ | k.A. |
| E-Mail-Template | Älterer Arbeitsablauf | Älterer Arbeitsablauf|
| Content-Blöcke |  ✅* |  ✅* |

\*Referenzieren Sie auf [Verwalten von Übersetzungen für Content-Blöcke](#managing-translations-for-content-blocks) für weitere Informationen.

### Älterer Arbeitsablauf

Je nach Anwendungsfall verwalten Sie Übersetzungen für Content-Blöcke entweder mit dem alten oder dem aktualisierten Übersetzungsworkflow. 

In dem aktualisierten Arbeitsablauf, der die Mehrsprachenunterstützung von Braze und die Lokalisierung in Nachrichten nutzt, werden dem Content-Block Übersetzungstags hinzugefügt. Smartling führt die Übersetzungen jedoch auf der Ebene der Nachrichten aus. Der Inhalt wird nur dann übersetzt, wenn der Inhalt in einer Kampagne oder einem Canvas enthalten ist und das Zielgebietsschema festgelegt ist. Weitere Informationen finden Sie unter [Verwalten von Übersetzungen für Content-Blöcke](#managing-translations-for-content-blocks).

Für E-Mail Templates wird nur der Legacy-Workflow unterstützt. Weitere Informationen finden Sie unter [Verwalten von Übersetzungen mit dem Legacy-Workflow](#managing-translations-using-the-legacy-workflow).

## Voraussetzungen

| Anforderung                   | Beschreibung                                                                                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Klugscheißer-Konto             | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Smartling-Konto](https://dashboard.smartling.com/).                                                          |
| Smartling Übersetzungsprojekt | Um Ihr Braze-Konto mit Smartling zu verbinden, müssen Sie sich zunächst anmelden und [ein Übersetzungsprojekt erstellen](https://help.smartling.com/hc/en-us/articles/115003074093). |
| Braze REST API-Schlüssel            | Ein Braze REST API-Schlüssel mit den folgenden Berechtigungen: <br>- campaigns.translations.get<br>- campaigns.translations.update<br>- campaigns.list<br>- campaigns.details<br>- canvas.translations.get<br>- canvas.translations.update<br>- campaigns.details<br>- templates.email.create<br>- templates.email.update<br>- templates.email.list<br>- templates.email.info<br>- templates.translations.get<br>- templates.translations.update<br>- content_blocks.info<br>- content_blocks.list<br>- content_blocks.create<br>- content_blocks.update<br><br> Dieser kann im Braze-Dashboard unter **Einstellungen > API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt           | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab.             |
| Braze Multi-Spracheinstellungen | [Vollständige Mehrspracheneinstellungen in Braze]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Mehrsprachige Einstellungen in Braze einrichten

Sehen Sie sich [die mehrsprachige Setup-Anleitung von Braze]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) an, um Lokalisierungen in Braze einzurichten.

### Schritt 2: Richten Sie das Braze-Projekt in Smartling TMS ein

Einzelheiten zur Konfiguration des Konnektors finden Sie in der [Dokumentation von Smartling](https://help.smartling.com/hc/en-us/articles/13248549217435).

### Braze mit Smartling verbinden

1. Erstellen Sie in Ihrem [Smartling-Konto](https://dashboard.smartling.com/) einen [Braze Konnektor-Projekttyp](https://help.smartling.com/hc/en-us/articles/115003074093).

![Lötverbindung in Smartling.]({% image_buster /assets/img/smartling/image1_Connecting_Braze_to_Smartling.png %})

{: start="2"}
2\. Wählen Sie in diesem Projekt **Einstellungen** > **Braze-Einstellungen** > **Mit Braze verbinden**.
3\. Füllen Sie die erforderlichen Felder aus, wie API-URL und API-Schlüssel. Wenn die Testverbindung erfolgreich ist, speichern Sie die Verbindung. Wenn der Test nicht erfolgreich ist, überprüfen Sie, ob Sie die richtige API-URL und den richtigen API-Schlüssel eingegeben haben.

![Braze-Verbindung in den Smartling API-Einstellungen.]({% image_buster /assets/img/smartling/image2_API.png %})

{: start="4"}
4\. Fügen Sie zusätzliche Projektsprachen hinzu.

![Braze-Verbindung in Smartling Project Languages.]({% image_buster /assets/img/smartling/image3_project_languages.png %})

{: start="5"}
5\. Überprüfen Sie in den Braze-Einstellungen, ob die Werte in der Spalte **Zielsprache (Braze)** mit den in den Braze-Mehrspracheneinstellungen konfigurierten Gebietsschemata übereinstimmen. Die Benennungskonvention der Lokalisierung muss genau übereinstimmen.

![Braze-Verbindung in Smartling Language Confirmation.]({% image_buster /assets/img/smartling/image4_language_confirmation.png %})

### Schritt 3: Fügen Sie Ihrer Nachricht auf Braze Tags für die Übersetzung hinzu

Sehen Sie sich [die Anleitung von Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/?tab%3Dhtml%2520editor#prerequisites) an, wie Sie Ihren Nachrichten Tags für die Übersetzung hinzufügen können:

- [E-Mail]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email)
- [Push]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push)
- [In-App-Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message)

Hier sehen Sie ein Beispiel für eine HTML E-Mail Kampagne mit Übersetzungstags.

![Braze E-Mail mit Übersetzungstags.]({% image_buster /assets/img/smartling/image5_translation_tags.png %})

Sie müssen die Nachricht als Entwurf speichern, bevor Sie Lokalisierungen auswählen können.

### Schritt 4: Verwalten von Übersetzungen in Smartling

Nachdem Sie den Konnektor von Braze angeschlossen und eingerichtet haben, finden Sie Braze-Inhalte auf dem Tab Braze in Ihrem Smartling-Projekt. Weitere Informationen finden Sie in der [Dokumentation zu Smartling](https://help.smartling.com/hc/en-us/articles/13248577069979).

Smartling bietet fortschrittliche Features zum Suchen und Auswählen von Inhalten nach:
- Schlüsselwort-Suche
- Braze Content-Typ
- Braze-Tagging

1. In diesem Beispiel wurde die E-Mail Kampagne für das neue Jahr in [Schritt 3](#step-3-add-translation-tags-to-your-braze-message) erstellt.

![Braze E-Mail mit Übersetzungstags.]({% image_buster /assets/img/smartling/image6_ny_promotion.png %})

{: start="2"}
2\. Nachdem Sie die Kampagne gefunden haben, die Sie übersetzen möchten, wählen Sie den Ordner aus, wählen Sie die Varianten und wählen Sie **Übersetzung anfragen**.

![Anfrage für Übersetzungen.]({% image_buster /assets/img/smartling/image7_request_translation.png %})

{: start="3"}
3\. Erstellen Sie einen neuen Auftrag für die Übersetzung.

![Erstellen Sie einen neuen Auftrag für die Übersetzung.]({% image_buster /assets/img/smartling/image8_request_translation.png %})

{: start="4"}
4\. Nachdem der Auftrag genehmigt wurde, bearbeiten Sie jede Übersetzung im CAT-Tool.

![Übersetzung CAT-Tool.]({% image_buster /assets/img/smartling/image9_translation_job.png %})

{: start="5"}
5\. Nachdem Sie die Übersetzungen fertiggestellt haben, speichern Sie Ihre Übersetzung und senden sie an Braze.

![Übersetzung an Braze senden.]({% image_buster /assets/img/smartling/image10_translations.png %})

### Schritt 5: Vorschau auf die Nachricht als mehrsprachiger Nutzer:in in Braze

Zeigen Sie in Braze eine Vorschau Ihrer Kampagne als mehrsprachiger Nutzer:in an, um zu überprüfen, ob die Übersetzungen korrekt angewendet werden.

![Mehrsprachige Vorschau für Nutzer:innen.]({% image_buster /assets/img/smartling/image11_preview.png %})

## Übersetzungen für Content-Blöcke verwalten

Content-Blöcke werden in Braze unter der Rubrik **Templates & Media** verwaltet.

### Übersetzung als Teil der Nachrichtenkomponente gespeichert

Übersetzungs-Tags gehören in den Content-Block. Smartling führt die Übersetzungen jedoch auf der Ebene der Nachrichten aus; der Inhalt wird nur dann übersetzt, wenn er in einer Kampagne oder einem Canvas enthalten ist und das Zielgebietsschema festgelegt ist.

### Überlegungen

- Übersetzungs-Tags müssen sowohl bei HTML- als auch bei Drag-and-Drop-Editoren für Content-Blöcke manuell in den Content-Block eingefügt werden.
- Die Lokalisierung wird auf der Ebene der Nachrichten ausgewählt, nicht auf den Content-Blöcken selbst.
- Für Canvas empfehlen wir die Verwendung von Zeilen, um Content-Blöcke in Ihre Nachricht einzufügen, anstatt sie manuell mit einem Liquid-Tag hinzuzufügen. Wenn Sie einen Content-Block aus der Vorschau in eine E-Mail ziehen, wird eine lokale Kopie erstellt. Alle Änderungen am "übergeordneten" Content-Block werden nicht auf andere Kampagnen übertragen, die diesen Block verwenden.
- Wenn Sie einen Liquid-Tag für den Content-Block verwenden, sollten Sie mindestens einen Tag für die Übersetzung direkt in den Text der E-Mail einfügen. Durch das manuelle Hinzufügen des Tags für die Übersetzung können Sie die Gebietsschemata aus dem Dropdown-Menü für mehrere Sprachen auswählen. Smartling übernimmt die Übersetzungstags für den Content-Block. Sie können einen `comment` Tag hinzufügen, damit der Text für den Nutzer:in nicht sichtbar ist.

## Verwalten von Übersetzungen mit dem Legacy-Workflow

Wenn Sie es vorziehen, Übersetzungen direkt in einem Content-Block oder einer E-Mail-Vorlage zu verwalten, lesen Sie die Anweisungen in der [Dokumentation von Smartling.](https://help.smartling.com/hc/en-us/articles/13248577069979-Translating-with-the-Braze-Connector) Diese Methode verwendet ein Sprachattribut und Liquid if/else-Logik, um Text in verschiedenen Sprachen anzuzeigen.

## Häufig gestellte Fragen

### Werden Übersetzungstags für den Drag-and-Drop-Editor unterstützt?

Für den Drag-and-Drop-Editor (E-Mail, Content-Block, In-App-Nachricht) müssen Sie Übersetzungs-Tags manuell als Liquid-Tags hinzufügen.

### Wie übersetzt man Text innerhalb eines Liquid-Tags?

Smartling erkennt Liquid-Tags und macht sie zu nicht editierbaren Variablen im Composer. Jeder andere Text innerhalb des Liquid-Tags, wie z.B. Standard-Text oder Filter wie join, wird in Smartling ebenfalls nicht editierbar. Entfernen Sie jedoch den Liquid-Tag in Smartling und erstellen Sie den Liquid-Tag mit dem übersetzten Standardtext neu. Beim Speichern der Übersetzung erscheint eine Warnung.
