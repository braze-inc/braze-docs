---
nav_title: Lokalisierung
article_title: Lokalisierung
page_order: 7
description: "Dieser Artikel referenziert die Grundlagen der Lokalisierung, listet die Vorteile verschiedener Orchestrierungsansätze für Kampagnen und Canvase auf und zeigt verschiedene Möglichkeiten auf, wie Nutzer:innen die Personalisierung ihrer Nachrichten handhaben können."
tool:
    - Campaigns
    - Canvas
---

# Lokalisierung

> Für Unternehmen mit Kunden in vielen Ländern kann die frühzeitige Lokalisierung in Ihrer Braze-Journey Ihrem Unternehmen Zeit und Ressourcen sparen.

## Funktionsweise

Nachdem Sie [das Braze SDK integriert haben]({{site.baseurl}}/developer_guide/sdk_integration/), werden automatisch Lokalisierungsinformationen von Nutzer:innen-Geräten gesammelt. Das Gebietsschema enthält die Sprache und einen Bezeichner für die Region. Diese Informationen sind im Braze Segmentierungstool unter **Land** und **Sprache** verfügbar.

{% alert tip %}
Technische Details zum Empfang der Lokalisierung finden Sie in der offiziellen Dokumentation [für iOS](https://developer.apple.com/library/ios/documentation/MacOSX/Conceptual/BPInternational/LanguageandLocaleIDs/LanguageandLocaleIDs.html) und [Android](http://developer.android.com/reference/java/util/Locale.html).
{% endalert %}

## Übersetzungsmanagement

Ziehen Sie die folgenden Ansätze für die Verwaltung Ihrer Übersetzungen in Betracht.

{% tabs local %}
{% tab campaign %}
### Ein Template für alle

Bei diesem Ansatz wird die Lokalisierung mit [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) auf ein einzelnes Template in Braze angewendet. Nach dem Versand bietet das Dashboard aggregierte Kampagnen-Analysen. Das Engagement auf Benutzerebene kann mit benutzerdefinierten Segmenttrichtern gemessen werden, z. B. durch die Kombination von Filtern für **Land** und **empfangene Kampagne**.

| Vorteile | Überlegungen |
| --- | --- |
| \- Zentralisierter Ansatz<br>\- Schnellere E-Mail-Erstellung, E-Mail muss nicht mehrmals erstellt werden | \- Manuelle Berichterstellung<br>\- Der Kampagnenbericht zeigt aggregierte Metriken anstelle von Metriken pro Land<br>\- Sie müssen Liquid gründlich testen, um das erwartete Verhalten sicherzustellen<br>\- Je nachdem, wie Sie den Länderwert einlesen oder wie viele Länder Sie eingerichtet haben, könnte es schwierig sein, jedes Land zu testen.<br>\- Es ist schwieriger, Sendungen für bestimmte Zeiten in verschiedenen Zeitzonen zu planen.<br>\- Schwieriger zu verwenden, wenn Sie separate Inhalte pro Land senden möchten. |
| \--- | \--- | \--- |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Ein Template pro Land 

Dieser Ansatz trennt die Template-Erstellung in verschiedene Sende-Locales. Nach dem Versand meldet das Dashboard die Analytics für jedes Land separat, und alle nachgelagerten [Currents-Ereignisse]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) auf Nutzerebene werden ebenfalls mit einer bestimmten Kampagne verknüpft.

- Vorlagen profitieren von der Implementierung von [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags#tags) zu Wartungs- und Nachverfolgungszwecken.
- Kampagnen können die Konfigurationen von derselben [Braze-Vorlage]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media#about-templates-and-media) und von [Inhaltsblöcken]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) (z. B. [E-Mail-Vorlagen]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template), die Liquid enthalten) übernehmen.
- Bereits existierende Kampagnen und Templates können [dupliziert]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating/) werden, um eine schnellere Wertschöpfung zu ermöglichen.

| Vorteile | Überlegungen |
| --- | --- |
| \- Skalierbar für mehrere Standorte<br>\- Berichterstattung über den Umsatz pro Land innerhalb von Braze (z.B. pro Kampagne)<br>\- Flexibilität, wenn sich die Inhalte je nach Land drastisch unterscheiden | \- Erfordert strategische Strukturierung<br>\- Mehr Aufwand für den Aufbau (z. B. separate Kampagnen für jedes Land) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}

{% tab canvas %}
### Eine Reise für alle

Bei diesem Ansatz wird die Lokalisierung innerhalb von [Canvas Journeys]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/the_basics/#building-the-customer-journey) und Liquid durchgeführt, um Nachrichten für jeden Nutzer:innen zu definieren. 

Nachdem ein Canvas versendet wurde, bietet das Dashboard aggregierte [Canvas-Analysen]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/), während das Engagement auf Benutzerebene über benutzerdefinierte [Segmenttrichter]({{site.baseurl}}/user_guide/engagement_tools/segments/measuring_segment_size/) gemessen werden kann, z. B. durch Kombination von [**Land**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#country) und [**Empfangener Canvas-Schritt**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#received-canvas-step) Filter.

| Vorteile | Überlegungen |
| --- | --- |
| \- Zentralisierter Ansatz<br>\- Schnellere E-Mail-Erstellung – E-Mail muss nicht mehrmals erstellt werden | \- Manuelle Berichterstellung<br>\- Der Canvas-Bericht zeigt aggregierte Metriken anstelle von Metriken pro Land<br>\- Sie müssen Liquid gründlich testen, um das erwartete Verhalten sicherzustellen<br>\- Je nachdem, wie Sie den Länderwert einlesen oder wie viele Länder Sie eingerichtet haben, könnte es schwierig sein, jedes Land zu testen.<br>\- Es ist schwieriger, Sendungen für bestimmte Zeiten in verschiedenen Zeitzonen zu planen.<br>\- Schwieriger zu verwenden, wenn Sie separate Inhalte pro Land senden möchten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Eine Reise pro Land

Bei diesem Ansatz bietet der [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) Journey Builder die Flexibilität, Nutzer:innen über mehrere [Canvas-Komponenten]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) zu erstellen. Diese Komponenten können auf der Ebene der Komponenten und der gesamten Journey [dupliziert]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/duplicating) werden.

Die Lokalisierung kann mit den folgenden Methoden durchgeführt werden:

- Getrennte Canvase pro Land, um sicherzustellen, dass die komplexen Nutzer:innen mit Hilfe von Zielgruppen-Filtern am oberen Ende des Funnels definiert werden.
- Maßgeschneiderte User Journeys pro Land, die Implementierung von [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) zur intuitiven Segmentierung von Nutzern in großem Maßstab für jede Journey durch die Erstellung separater Nachrichten-Threads für jedes Land in einem einzigen Canvas

Nach dem Versand bietet das Dashboard dynamische Analytics pro Land und innerhalb der [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents#access-currents) Events auf Nutzerebene, die auf dem aktuellen Standort des Kunden basieren.

| Vorteile | Überlegungen |
| --- | --- |
| \- Berichterstattung über den Umsatz pro Land innerhalb von Braze (z. B. pro Canvas, Variante oder Schritt)<br>\- Flexibilität, wenn sich die Inhalte je nach Land drastisch unterscheiden<br>\- Kann in Zukunft weitere Kanäle als Teil der Journey hinzufügen | \- Erfordert strategische Strukturierung<br>\- Mehr Aufwand für die Erstellung (z. B. separate Nachrichtenschritte für jedes Land)<br>\- Canvas kann groß und schwer lesbar werden, wenn Sie benutzerdefinierte, komplexe Reisen für jedes Land in einem einzigen Canvas haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

## Versenden von übersetzten Nachrichten

Um personalisierte Nachrichten auf der Grundlage der Sprache oder des Gebietsschemas eines Nutzers zu versenden, verwenden Sie eine der folgenden Methoden:

{% tabs local %}
{% tab Manually %}
Sie können Ihre Inhalte manuell in den Textkörper Ihrer Nachricht einfügen und [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) verwenden, um dem Empfänger: [in]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) der richtigen Sprache anzuzeigen. Um dies zu tun:

1. Verfassen Sie Ihre Nachricht und wählen Sie dann **Sprache** aus, um Liquid bedingte Logik für jede der von Ihnen ausgewählten Sprachen zu generieren.
2. Sie können die folgende Liquid-Vorlage verwenden, um Ihre Nachricht zu verfassen. Für jedes Feld mit Templates sollten Sie die Variationen nach dem in Klammern gesetzten Segment des Templates eingeben. Die Variation sollte dem Sprachcode entsprechen, auf den in den Klammern davor verwiesen wird.
    {% raw %}
    ```liquid
    {% if ${language} == 'en' %}
    This is a message in English from Braze!
    {% elsif ${language} == 'es' %}
    Este es un mensaje en español de Braze !
    {% elsif ${language} == 'zh' %}
    这是一条来自Braze的中文消息。
    {% else %}
    This is a message from Braze! This will go to anyone who does not match the other specified languages!
    {% endif %}
    ```
    {% endraw %}
3. Testen Sie Ihre Nachricht vor dem Versenden, indem Sie die ID oder E-Mail eines Benutzers eingeben, um zu prüfen, wie eine Nachricht je nach Sprache für eine bestimmte Person aussehen würde. 

{% alert tip %}
Wir empfehlen immer, eine Erklärung {% raw %}`{% else %}`{% endraw %} in Ihre Nachricht aufzunehmen. Während die meisten Nutzer:innen Nachrichten in ihrer eigenen Sprache sehen, ist der Text auch für diejenigen sichtbar, die:
- Sie haben keine Sprache ausgewählt
- Sie haben eine Sprache, die Braze nicht unterstützt
- Haben Sie ein Gerät, bei dem die Sprache nicht nachweisbar ist
{% endalert %}
{% endtab %}

{% tab Content Blocks %}
Braze [Content Blocks]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks) sind wiederverwendbare Inhaltsblöcke. Wenn ein Block geändert wird, ändern sich alle Referenzen auf diesen Block. Zum Beispiel werden Aktualisierungen eines E-Mail-Header- oder Footer in allen E-Mails oder Übersetzungen übernommen. Diese Blöcke können auch über die REST API [erstellt]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/#create-content-block) und [aktualisiert]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) werden, und Nutzer:innen können Übersetzungen programmatisch hochladen. 

Beim Erstellen einer Kampagne im Dashboard können Content-Blöcke mit dem Tag {% raw %}`{{content_blocks.${name_of_content_block}}}`{% endraw %} referenziert werden. Diese Blöcke können alle Übersetzungen enthalten, die in einer bedingten Logik für jede Sprache untergebracht sind, wie in Option 1 gezeigt, oder es kann ein separater Block für jede Sprache verwendet werden.

Content-Blöcke können auch als Übersetzungsverwaltungsprozess verwendet werden, bei dem zu übersetzenden Content in einem Content-Block gespeichert, abgerufen, übersetzt und dann aktualisiert werden:
1. Erstellen Sie im Dashboard manuell einen Content-Block mit dem Tag „Übersetzungsbedarf“.
2. Ihr Dienst führt über den [Endpunkt`/content_blocks/list` ]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) einen nächtlichen Abruf aller Content-Blöcke durch.
3. Ihr Dienst holt über den [Endpunkt`/content_blocks/info` ]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_see_email_content_blocks_information/) Details zu jedem Content-Block ab, um zu sehen, welche Blöcke mit Tags für die Übersetzung versehen sind.
4. Ihr Übersetzungsdienst übersetzt den Textkörper aller Inhaltsblöcke, die eine Übersetzung benötigen.
5. Ihr Dienst greift auf den [Endpunkt`/content_block/update` ]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/) zu, um übersetzten Content zu aktualisieren und das Tag auf „Übersetzung abgeschlossen“ zu setzen.
{% endtab %}

{% tab Catalogs %}
[Kataloge]({{site.baseurl}}/user_guide/data/activation/catalogs/) ermöglichen Ihnen den Zugriff auf Daten aus importierten JSON-Objekten über API und CSV-Dateien, um Ihre Nachrichten anzureichern, ähnlich wie bei benutzerdefinierten Attributen oder benutzerdefinierten Ereigniseigenschaften über Liquid. Zum Beispiel:

{% subtabs local %}
{% subtab API %}

Erstellen Sie einen Katalog über den folgenden API-Aufruf:
```json
curl --location --request POST 'https://your_api_endpoint/catalogs' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "catalogs": [
   {
     "name": "translations",
     "description": "My localization samples",
     "fields": [
       {
         "name": "id",
         "type": "string"
       },
       {
         "name": "context",
         "type": "string"
       },
       {
         "name": "language",
         "type": "string"
       },
       {
         "name": "body",
         "type": "string"
       }
     ]
   }
 ]
}'
```

Fügen Sie Artikel über den folgenden API-Aufruf hinzu:

```json
curl --location --request POST 'https://your_api_endpoint/catalogs/translations/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
 "items": [
   {
     "id": "1",
     "context": "1",
     "language": "en",
     "body": "Hey"
   },
   {
     "id": "2",
     "context": "1",
     "language": "es",
     "body": "Hola"
   },
   {
     "id": "3",
     "context": "1",
     "language": "pt",
     "body": "Oi"
   },
   {
     "id": "4",
     "context": "1",
     "language": "de",
     "body": "Hallo"
   }
 ]
}'
```
{% endsubtab%}
{% subtab CSV %}
Erstellen Sie eine CSV-Datei im folgenden Format:

| id | context | Sprache | body |
| --- | --- | --- |
| (1 %) | (1 %) | en | Hallo |
| (2 %) | (1 %) | es | Hola |
| 3 | (1 %) | pt | Oi |
| (4 %) | (1 %) | de | Hallo |
| (5 %) | (2 %) | en | Hallo |
| 6 | (2 %) | es | Hola |
| (7 %) | (2 %) | pt | Oi |
| (8 %) | (2 %) | de | Hallo |
| (9 %) | 3 | en | Hallo |
| (10 %) | 3 | es | Hola |
| (11 %) | 3 | pt | Oi |
| (12 %) | 3 | de | Hallo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}
{% endsubtab %}
{% endsubtabs %}

Auf diese Katalogeintragungen kann mit Hilfe der unten gezeigten [Personalisierung]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog/#using-catalogs-in-a-message) oder mit Hilfe von [Auswahlen]({{site.baseurl}}/user_guide/data/activation/catalogs/selections), mit denen Sie Datengruppen erstellen können, Bezug genommen werden. 

{% raw %}
```liquid
{% catalog_items translations 1 %}
{{items[0].body}} 
//returns “Hey”
```
{% endraw %}
{% endtab %}

{% tab Locale messages %}
Fügen Sie Ihrer Nachricht Lokalisierungen hinzu und verwenden Sie diese, um Nutzer:innen in verschiedenen Sprachen innerhalb einer einzigen Kampagne oder eines Canvas für die E-Mail- oder Push-Kanäle anzusprechen. Eine vollständige Anleitung finden Sie unter [Lokalisierung in E-Mail Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/) oder [Lokalisierung in Push-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/push/using_locales/).

{% alert important %}
Diese Funktion befindet sich derzeit in der Early Access-Phase. Wenden Sie sich an Ihren Braze-Account Manager, wenn Sie sich für die Teilnahme am Early Access interessieren.
{% endalert %}
{% endtab %}

{% tab Braze partners %}
Viele Partner von Braze bieten Lösungen zur Lokalisierung an, darunter [Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex/#about-transifex) und [Crowdin](https://crowdin.com/). In der Regel nutzen die Benutzer die Plattform zusammen mit einem internen Team und einem Übersetzungsbüro. Diese Übersetzungen werden dann dort hochgeladen und sind dann über die REST API zugänglich. Diese Dienste nutzen häufig auch [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), was es Nutzern:innen erlaubt, die Übersetzungen über APIs abzurufen.

Die folgenden Connected Content-Aufrufe rufen beispielsweise Transifex und Crowdin auf, um eine Übersetzung zu holen. Dabei wird {% raw %}`{{${language}}}`{% endraw %} genutzt, um die richtige Übersetzung für einen bestimmten Benutzer zu ermitteln. Diese Übersetzung wird dann in dem JSON-Block „Strings“ gespeichert und referenziert.

{% subtabs local %}
{% subtab Transifex example %}
{% raw %}
```liquid
{% connected_content https://www.transifex.com/api/2/project/example/resource/example/translation/{{${language}}}/strings :basic_auth semc :save strings %}
{{strings[0].translation}}
```
{% endraw %}
{% endsubtab %}
{% subtab Crowdin example %}
{% raw %}
```liquid
{% connected_content https://api.crowdin.com/api/project/braze-test/export-file?key=you_api_key&language={{${language}}}&file=test.json&export_translated_only=1 :save response %}
{{response.value_1}}
```
{% endraw %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Spreadsheets %}
Hosten Sie die Übersetzungen in einer Tabelle und verwenden Sie dann eine der folgenden Methoden, um Ihre Nachricht in der entsprechenden Sprache zu versenden.

{% subtabs local %}
{% subtab Connected Content %}
Sie können mit einem Übersetzungsbüro zusammenarbeiten, um Übersetzungen in einem Google Spreadsheet zu speichern und diese Inhalte dann mit [Braze Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) abzufragen. Wenn Sie eine Nachricht senden, wird die entsprechende Übersetzung für jeden Nutzer:innen auf der Grundlage seiner ausgewählten Sprache in Ihre Kampagne übernommen. 

{% alert note %}
Die Google-Tabellen-API hat ein Limit von 500 Anfragen pro 100 Sekunden pro Projekt. Connected-Content-Aufrufe können zwischengespeichert werden, aber diese Lösung ist für eine Kampagne mit hohem Datenverkehr nicht skalierbar.
{% endalert %}
{% endsubtab %}

{% subtab JSON API via SheetDB %}
Diese Option bietet eine alternative Methode zur Transformation von Google-Tabellen in JSON-Objekte, die über Connected-Content abgefragt werden. Indem Sie eine Tabellenkalkulation über SheetDB in eine JSON-API umwandeln, können Sie je nach Häufigkeit der API-Aufrufe aus [mehreren Abonnementstufen](https://sheetdb.io/pricing) wählen.

Die Struktur der Tabellenkalkulation folgt den Schritten in Option 4, aber SheetDB bietet auch [zusätzliche Filter](https://docs.sheetdb.io/#sheetdb-api) zur Abfrage der Objekte.

Einige Benutzer ziehen es vielleicht vor, SheetDB mit weniger Liquid- und Connected Block-Abhängigkeiten zu implementieren, indem sie die [SheetDB-Suchmethode](https://docs.sheetdb.io/#get-search-in-document) in GET-Anfrageaufrufen implementieren, um die JSON-Objekte auf der Grundlage von {% raw %}`{{${language}}}`{% endraw %} Liquid-Tag zu filtern und automatisch die Ergebnisse für eine einzelne Sprache zurückzugeben, anstatt große bedingte Blöcke zu erstellen.

#### Schritt 1: Google-Tabelle formatieren

Erstellen Sie zunächst die Google-Tabelle so, dass die Sprachen unterschiedliche Objekte sind:

| Sprache | Titel1 | Text1 | Titel2 | Text2 |
| de | Hey | 1 | Hey2 | 5 |
| es | Hola | 2 | Hola2 | 6 |
| pt | Oi | 3 | Oi2 | 7 |
| de | Hallo | 4 | Hallo2 | 8 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 .reset-td-br-5 role="presentation"}

#### Schritt 2: Sprach-Liquid-Tag in einem Connected-Content-Aufruf verwenden

Als nächstes implementieren Sie den {% raw %}`{{${language}}}`{% endraw %}-Liquid-Tag innerhalb eines Connected-Content-Aufrufs. Beachten Sie, dass SheetDB die `sheet_id` bei der Erstellung des Arbeitsblatts automatisch generiert.

{% raw %}
```liquid
{% connected_content https://sheetdb.io/api/v1/[sheet_id]/search?language={{${language}}} :save result%}
```
{% endraw %}

#### Schritt 3: Template für Ihre Nachrichten

Und schließlich verwenden Sie Liquid für das Template Ihrer Nachrichten:

{% raw %}
```liquid
{{result[0].title1}} //returns “Hey”
{{result[0].title2}} //returns “Hey2”
```
{% endraw %}

##### Überlegungen

- Das Feld {% raw %}`{{${language}}}`{% endraw %} muss für alle Benutzer definiert werden, andernfalls muss ein Liquid-Bedingungsblock als Fallback-Handler für Benutzer ohne eine Sprache bereitgestellt werden.
- Die Datenmodellierung in Google Sheets muss einer anderen sprachgesteuerten Vertikale folgen, als dies bei Nachrichtenobjekten der Fall ist.
- SheetDB bietet ein begrenztes kostenloses Konto und mehrere kostenpflichtige Optionen, die Sie je nach Ihrer Kampagnenstrategie in Betracht ziehen sollten. 
- Aufrufe von Connected Content können zwischengespeichert werden. Wir empfehlen, die voraussichtliche Kadenz der API-Aufrufe zu messen und einen alternativen Ansatz zu untersuchen, bei dem der Haupt-Endpunkt von SheetDB aufgerufen wird, anstatt die Suchmethode zu verwenden.
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
