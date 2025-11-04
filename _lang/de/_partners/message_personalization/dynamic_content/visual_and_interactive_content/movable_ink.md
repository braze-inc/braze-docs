---
title: "Movable Ink"
article_title: Movable Ink
alias: "/partners/movable_ink/"
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Movable Ink, einer cloudbasierten Softwareplattform, die digitalen Marketern die Möglichkeit bietet, überzeugende und eindeutige visuelle Erlebnisse zu schaffen, die Kunden bewegen."
page_type: partner
search_tag: Partner

---

# Movable Ink

> [Movable Ink](https://www.movableink.com/) ist eine cloudbasierte Software-Plattform, die Marketern die Möglichkeit bietet, überzeugende und eindeutige visuelle Erlebnisse zu schaffen, die Kunden:in bewegen. Die Plattform von Movable Ink bietet wertvolle Anpassungsmöglichkeiten, die sich leicht in Ihre Kampagnen einfügen lassen. 

_Diese Integration wird von Movable Ink gepflegt._

## Über die Integration

Nutzen Sie die intelligenten Creative Features von Movable Ink, wie z.B. Polling, Countdown-Timer und Scratch-Off, um Ihre kreativen Möglichkeiten zu erweitern. Die Integration von Movable Ink und Braze ermöglicht einen umfassenderen Ansatz für dynamische datengestützte Nachrichten, die Nutzern:innen in Realtime Informationen über die Dinge liefern, die wichtig sind.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Movable Ink Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Movable Ink-Konto. |
| Datenquelle | Sie müssen eine Datenquelle mit Movable Ink verbinden. Dies kann über CSV, Website-Import oder API geschehen. Achten Sie darauf, dass Sie Daten mit einem einheitlichen Bezeichner zwischen Braze und Movable Ink übergeben (z.B. `external_id`).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

- Personalisierte Monats- oder End-to-End-Recaps.
- Personalisieren Sie dynamisch Bilder für E-Mail-, Push- oder Rich-Benachrichtigungen auf der Grundlage des letzten bekannten Verhaltens.<br>
	Zum Beispiel: 
	- Verwenden Sie eine Rich-Push-Benachrichtigung, um dynamisch einen Zeitplan von Ereignissen zu erstellen, indem Sie Daten aus APIs abrufen. 
	- Nutzen Sie den Countdown-Timer, um Nutzer:innen zu benachrichtigen, wenn ein großer Verkauf bevorsteht (z.B. Black Friday, Valentinstag oder Feiertagsangebote).
	- Nutzen Sie das Scratch Off Feature als unterhaltsame und interaktive Möglichkeit, Aktionscodes zu verteilen.

## Unterstützte Movable Ink-Funktionen

Intelligent Creative hat viele Angebote, die Nutzer:innen von Braze nutzen können. Die folgende Liste zeigt, welche Funktionen unterstützt werden. 

| Movable Ink-Fähigkeit | Feature | Rich-Push-Benachrichtigung | In-App Messaging / Content-Cards / E-Mail | Details |
| ---------------------- |---| ---------------------- | -------------------------------- | ------- |
| Kreativ-Optimierer | A/B-Inhalte anzeigen | ✗ | ✔ | |
|| Optimieren Sie | ✗ | ✔* | \* Must Use Branch's Deeplinking Lösung |
| Targeting-Regeln | Datum | ✔* | ✔ | \* Unterstützt, aber nicht empfohlen, da Push-Benachrichtigungen beim Empfang zwischengespeichert und nicht aktualisiert werden. |
|| Wochentag | ✔* | ✔ | \* Unterstützt, aber nicht empfohlen, da Push-Benachrichtigungen beim Empfang zwischengespeichert und nicht aktualisiert werden. |
|| Tageszeit | ✔* | ✔ | \* Unterstützt, aber nicht empfohlen, da Push-Benachrichtigungen beim Empfang zwischengespeichert und nicht aktualisiert werden. |
| Stories/Verhaltensweisen Aktivität | | ✔* | ✔* | \* Der eindeutige Nutzer:innen-Bezeichner für Braze muss mit dem Bezeichner Ihres ESP verknüpft sein. |
| Deeplinking innerhalb der App setzen | | ✔* | ✔* | \* Um Ihren Kund:innen ein optimiertes Erlebnis zu bieten, verwenden Sie entweder die etablierte Deeplinking-Lösung über Branch oder eine validierte Lösung mit dem Team von Movable Ink für Kundenerlebnisse. |
| Apps | Countdown-Timer | ✔* | ✔ | \* Unterstützt, aber nicht empfohlen, da Push-Benachrichtigungen beim Empfang zwischengespeichert und nicht aktualisiert werden. |
|| Abfrage | ✗ | ✔* | \* Nach der Abstimmung wird die App zu einer mobilen Landing Page |
|| Abrubbeln | ✔* | ✔* | \* Bei Klick verlassen Sie die App für das Scratch Off-Erlebnis |
|| Video | ✔* | ✔* | \* Nur animierte GIFs, <br>Für Android benötigt Braze [GIF-Unterstützung]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs/) bei der Implementierung |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration

### Schritt 1: Erstellen Sie eine Datenquelle für Movable Ink

Kunden müssen eine Datenquelle erstellen, bei der es sich um eine CSV-Datei, einen Website-Import oder eine API-Integration handeln kann.

![Es werden verschiedene Optionen für Datenquellen angezeigt: CSV-Upload, Website- oder API-Integration.]({% image_buster /assets/img/movable_ink/movable_ink1.png %})

{% tabs local %}
{% tab CSV Datenquelle %}
- **CSV-Datenquelle**: Jede Zeile muss mindestens eine Segmente- und eine Inhaltsspalte haben. Nachdem Sie Ihre CSV-Datei hochgeladen haben, wählen Sie aus, welche Spalten für das Targeting der Inhalte verwendet werden sollen. [Beispiel CSV-Datei]({% image_buster /assets/download_file/movable_ink_CSV.csv %})

![Die Felder, die angezeigt werden, wenn Sie "CSV" als Datenquelle auswählen.]({% image_buster /assets/img/movable_ink/movable_ink2.png %})
{% endtab %}
{% tab Website Datenquelle %}
- **Website Datenquelle**: Jede Zeile muss mindestens eine Segmente- und eine Inhaltsspalte haben. Nachdem Sie Ihre CSV-Datei hochgeladen haben, wählen Sie aus, welche Spalten für das Targeting der Inhalte verwendet werden sollen.
  - Im Rahmen dieses Prozesses müssen Sie eine Abbildung erstellen:
    - Welche Felder werden als Segmente verwendet?
    - Welche Felder Sie als Datenfelder haben möchten, die im Kreativbereich dynamisch personalisiert werden können (z.B.: Nutzerdaten oder angepasste Attribute wie Vorname, Nachname, Ort usw.)

![Die Felder, die angezeigt werden, wenn Sie "Website" als Datenquelle auswählen.]({% image_buster /assets/img/movable_ink/movable_ink3.png %})
{% endtab %}
{% tab API-Integrationen %}
- **API-Integrationen**: Nutzen Sie die API Ihres Unternehmens, um Inhalte direkt aus einer API-Antwort zu erzeugen.

![Die Felder, die angezeigt werden, wenn Sie "API Integration" als Ihre Datenquelle auswählen]({% image_buster /assets/img/movable_ink/movable_ink4.png %})
{% endtab %}
{% endtabs %}

### Schritt 2: Erstellen Sie eine Kampagne auf der Movable Ink Plattform

Erstellen Sie auf dem Startbildschirm von Movable Ink eine Kampagne. Sie können auswählen zwischen E-Mail aus HTML, E-Mail aus Bild oder einem Block, der in jedem Kanal verwendet werden kann, einschließlich Push, In-App-Nachricht und Content-Cards (vorgeschlagen).

Wir empfehlen Ihnen auch, einen Blick auf die verschiedenen Inhaltsoptionen zu werfen, die über Blöcke verfügbar sind.

![Ein Bild davon, wie die Movable Ink-Plattform aussieht, wenn Sie eine neue Kampagne für Movable Ink erstellen.]({% image_buster /assets/img/movable_ink/movable_ink5.png %}){: style="max-width:70%"}

Movable Ink verfügt über einen einfachen Editor, mit dem Sie Elemente wie Text oder Bilder per Drag-and-Drop verschieben können. Wenn Sie Ihre Datenquelle aufgefüllt haben, können Sie mit Hilfe der Eigenschaften der Daten dynamisch ein Bild erzeugen. Darüber hinaus können Sie innerhalb dieses Flusses auch Fallbacks für Nutzer:innen erstellen, wenn die Kampagne gesendet wird und ein Nutzer nicht den Kriterien der Personalisierung entspricht.

![Der Movable Ink Block-Editor zeigt die verschiedenen anpassbaren Elemente.]({% image_buster /assets/img/movable_ink/create_campaign2.png %})

Bevor Sie Ihre Kampagne abschließen, sollten Sie eine Vorschau der dynamischen Bilder anzeigen und die Abfrageparameter testen, um zu sehen, wie die Bilder bei der Anzeige aussehen werden. Wenn Sie fertig sind, wird eine dynamische URL generiert, die Sie in Braze! einfügen können.

Weitere Informationen zur Verwendung der Movable Ink Plattform finden Sie im [Movable Ink Support Center](https://support.movableink.com/).

### Schritt 3: Movable Ink Content-URL abrufen

Um Movable Ink-Inhalte in Nachrichten von Braze einzubinden, müssen Sie den Standort der Quell-URL finden, die Movable Ink Ihnen mitgeteilt hat. 

Um die Quell-URL zu erhalten, müssen Sie den Inhalt im Movable Ink Dashboard einrichten und dann von dort aus Ihren Inhalt fertigstellen und exportieren. Kopieren Sie auf der Seite **Finish** die Quell-URL(`img src`) aus dem Creative Tag.

![Die Seite, die erscheint, nachdem Sie Ihre Movable Ink Kampagne abgeschlossen haben, hier finden Sie Ihre Inhalts-URL.]({% image_buster /assets/img/movable_ink/obtain_url.png %}){: style="max-width:80%;"}

Als nächstes fügen Sie in der Braze Platform die URL in das entsprechende Feld ein. Entsprechende Felder für Ihren Messaging-Kanal finden Sie in Schritt 4. Ersetzen Sie schließlich alle Merge-Tags (z. B. {% raw %}```&mi_u=%%email%%```{% endraw %}) durch die entsprechende Liquid-Variable (z. B. {% raw %}```&mi_u={{${email_address}}}```{% endraw %}).

### Schritt 4: Braze Erfahrung

{% tabs local %}
{% tab E-Mail %}
Fügen Sie auf der Braze-Plattform Ihren kreativen Tag in den Text Ihrer E-Mail ein.![]({% image_buster /assets/img/movable_ink/web2.png %}){: style="max-width:90%"}<br><br>

{% endtab %}
{% tab Push-Benachrichtigung %}

1. In der Braze Plattform:
	- Android Push: Fügen Sie die URL in die Felder **Push-Symbolbild** und **Erweitertes Bild der Benachrichtigung** ein.<br>![]({% image_buster /assets/img/movable_ink/android.png %}){: style="max-width:60%"}<br><br>
	- iOS Push: Fügen Sie die URL in das Feld **Medienlink** ein und geben Sie das Dateiformat an, das Sie verwenden.<br>![]({% image_buster /assets/img/movable_ink/ios.png %}){: style="max-width:60%"}<br><br>
	- Internet-Push: Fügen Sie die URL in die Felder **Push-Symbol-Bild** und **Großes Bild der Benachrichtigung** ein.<br>![]({% image_buster /assets/img/movable_ink/web.png %}){: style="max-width:60%"}<br><br>
2. Um sicherzustellen, dass die Bilder nicht zwischengespeichert werden, stellen Sie der URL in der Nachricht leere Liquid-Tags voran: <br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}

{% endtab %}
{% tab In-App-Nachricht %}

1. Fügen Sie auf der Braze-Plattform die URL in das Feld **Rich-Benachrichtigung Media** ein.![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. Geben Sie eine eindeutige URL an, um das Zwischenspeichern zu verhindern. Um sicherzustellen, dass die Realtime-Bilder von Movable Ink funktionieren und nicht durch das Caching beeinträchtigt werden, verwenden Sie Liquid, um einen Zeitstempel an das Ende der URL des Movable Ink-Bildes anzuhängen.

Verwenden Sie dazu die folgende Syntax und ersetzen Sie die Bild-URL nach Bedarf:
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
Dieses Template nimmt die aktuelle Zeit (in Sekunden), hängt sie an das Ende des Movable Ink Bild Tabs an (als Abfrageparameter) und gibt dann das Endergebnis aus. Mit dem Tab **Test** können Sie eine Vorschau anzeigen. Der Code wird dann ausgewertet und eine Vorschau angezeigt.

**3\.** Schließlich sollten Sie die Mitgliedschaft in den Segmenten neu bewerten. Aktivieren Sie dazu die Option `Re-evaluate audience membership and liquid at send-time`, die sich im Schritt **Targeting Zielgruppen** einer Kampagne befindet. Wenn diese Option nicht verfügbar ist, wenden Sie sich an Ihren Customer-Success-Manager oder den Braze-Support. Diese Option weist Braze SDKs an, die Kampagne mit einer eindeutigen URL jedes Mal neu anzufragen, wenn eine In-App-Nachricht getriggert wird.

{% endtab %}
{% tab Content-Card %}

1. Fügen Sie auf der Braze-Plattform die URL in das Feld **Rich-Benachrichtigung Media** ein.![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. Für Mobiltelefone: Content-Cards-Bilder auf iOS und Android werden beim Empfang zwischengespeichert und nicht aktualisiert. 
  - Als Abhilfe können Sie Ihre Kampagne als täglich, wöchentlich oder monatlich wiederkehrende Nachricht mit einem entsprechenden Ablaufdatum planen, so dass die Content-Card erneut in den Zeitplan aufgenommen wird. Eine Content-Card, die einmal am Tag aktualisiert werden soll, sollte beispielsweise als täglicher Zeitplan mit einem Ablaufdatum von 1 Tag festgelegt werden.
3. Um sicherzustellen, dass die Realtime-Bilder von Movable Ink funktionieren und nicht durch das Zwischenspeichern beeinträchtigt werden, wenn die Content-Card neu getemplated wird, verwenden Sie Liquid, um einen Zeitstempel an das Ende der Movable Ink-Bild-URL anzuhängen.

Verwenden Sie dazu die folgende Syntax und ersetzen Sie die Bild-URL nach Bedarf:
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
Dieses Template nimmt die aktuelle Zeit (in Sekunden), hängt sie an das Ende des Movable Ink Bild Tabs an (als Abfrageparameter) und gibt dann das Endergebnis aus. Sie können eine Vorschau mit dem Tab **Test** anzeigen, der den Code auswertet und eine Vorschau anzeigt.

{% endtab %}
{% endtabs %}

## Fehlersuche

### Dynamische Bilder werden nicht korrekt angezeigt? Mit welchem Kanal haben Sie Probleme?
- **Push**: Achten Sie darauf, dass vor Ihrer Movable Ink Bild-URL eine leere Logik steht: <br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}
- **In-App-Nachrichten und Content-Cards**: Achten Sie darauf, dass die Bild-URL für jede Impression eindeutig ist. Dies kann durch Anhängen des entsprechenden Liquids geschehen, so dass jede URL anders ist. Siehe [Anweisungen für In-App-Nachrichten und Content-Card-Nachrichten]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink/#step-4-braze-experience). 
- **Bild wird nicht geladen**: Achten Sie darauf, dass Sie alle "Merge Tags" durch die entsprechenden Liquid-Felder im Braze-Dashboard ersetzen. Zum Beispiel: {% raw %}```https://mi-msg.com/p/rp/image.png?mi_u=%%email%%```{% endraw %} mit {% raw %}```https://mi-msg.com/p/rp/image.png?mi_u={{${email_address}}}```{% endraw %}.

### Haben Sie Probleme mit der Anzeige von GIFs auf Android?
- Android erfordert GIF-Unterstützung bei der Implementierung. Folgen Sie dem Artikel zur [Anpassung von In-App-Nachrichten]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs/) für Android, wenn Sie dies noch nicht eingerichtet haben.


[1]: https://www.movableink.com/
[Datenquelle]: ({% image_buster /assets/img/movable_ink/movable_ink1.png %})
[1]: ({% image_buster /assets/img/movable_ink/android.png %})
[2]: ({% image_buster /assets/img/movable_ink/ios.png %})
[3]: ({% image_buster /assets/img/movable_ink/web.png %})
