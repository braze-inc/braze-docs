---
title: "Bewegliche Tinte"
article_title: Bewegliche Tinte
alias: "/partners/movable_ink/"
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Movable Ink, einer cloudbasierten Softwareplattform, die digitalen Vermarktern eine Möglichkeit bietet, überzeugende und einzigartige visuelle Erlebnisse zu schaffen, die Kunden begeistern."
page_type: partner
search_tag: Partner

---

# Bewegliche Tinte

> [Movable Ink](https://www.movableink.com/) ist eine Cloud-basierte Software-Plattform, die digitalen Vermarktern eine Möglichkeit bietet, überzeugende und einzigartige visuelle Erlebnisse zu schaffen, die Kunden begeistern. Die Plattform von Movable Ink bietet wertvolle Anpassungsoptionen, die sich leicht in Ihre Kampagnen einfügen lassen. 

Nutzen Sie die intelligenten Kreativfunktionen von Movable Ink, wie z. B. Abfragen, Countdown-Timer und Rubbellose, um Ihre kreativen Möglichkeiten zu erweitern. Die Integration von Movable Ink und Braze ermöglicht einen umfassenderen Ansatz für dynamische, datengesteuerte Nachrichten, die den Nutzern Echtzeit-Elemente über die Dinge liefern, die wichtig sind.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Movable Ink Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Movable Ink-Konto. |
| Datenquelle | Sie müssen eine Datenquelle mit Movable Ink verbinden. Dies kann über CSV, Website-Import oder API erfolgen. Stellen Sie sicher, dass Sie Daten mit einem einheitlichen Bezeichner zwischen Braze und Movable Ink übergeben (zum Beispiel `external_id`).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

- Personalisierte Monats- oder Jahresrückblicke.
- Personalisieren Sie dynamisch Bilder für E-Mail-, Push- oder Rich Notifications auf der Grundlage des letzten bekannten Verhaltens.<br>
	Zum Beispiel: 
	- Verwenden Sie eine Rich-Push-Nachricht, um dynamisch einen Zeitplan für Ereignisse zu erstellen, indem Sie Daten aus der API abrufen. 
	- Verwenden Sie den Countdown-Timer, um Benutzer zu benachrichtigen, wenn ein großer Verkauf bevorsteht (z. B. Black Friday, Valentinstag oder Feiertagsangebote).
	- Nutzen Sie die Scratch Off-Funktion als unterhaltsame und interaktive Möglichkeit, Promotion-Codes zu verteilen.

## Unterstützte Movable Ink-Funktionen

Intelligent Creative hat viele Angebote, die Braze-Benutzer nutzen können. Die folgende Liste zeigt, welche Funktionen unterstützt werden. 

| Bewegliche Tinte ist möglich | Merkmal | Reichhaltige Push-Benachrichtigung | In-App-Nachrichten / Inhaltskarten / E-Mail | Details |
| ---------------------- |---| ---------------------- | -------------------------------- | ------- |
| Kreativ-Optimierer | Anzeige A/B Inhalt | ✗ | ✔ | |
|| Optimieren Sie | ✗ | ✔* | \* Muss Branch's Deeplinking Lösung verwenden |
| Targeting-Regeln | Datum | ✔* | ✔ | \* Unterstützt, aber nicht empfohlen, da Push-Benachrichtigungen beim Empfang zwischengespeichert werden und nicht aktualisiert werden. |
|| Wochentag | ✔* | ✔ | \* Unterstützt, aber nicht empfohlen, da Push-Benachrichtigungen beim Empfang zwischengespeichert werden und nicht aktualisiert werden. |
|| Tageszeit | ✔* | ✔ | \* Unterstützt, aber nicht empfohlen, da Push-Benachrichtigungen beim Empfang zwischengespeichert werden und nicht aktualisiert werden. |
| Geschichten/Verhaltensweisen Aktivität | | ✔* | ✔* | \* Die für Braze verwendete eindeutige Benutzerkennung muss mit der Kennung Ihres ESP verknüpft sein. |
| Deep Linking innerhalb der App | | ✔* | ✔* | \* Um Ihren Kunden ein optimiertes Erlebnis zu bieten, verwenden Sie entweder eine etablierte Deep Linking-Lösung über Branch oder eine validierte Lösung mit dem Client Experience-Team von Movable Ink. |
| Apps | Countdown-Timer | ✔* | ✔ | \* Unterstützt, aber nicht empfohlen, da Push-Benachrichtigungen beim Empfang zwischengespeichert werden und nicht aktualisiert werden. |
|| Abfrage | ✗ | ✔* | \* Nach der Abstimmung wird die App zu einer mobilen Landing Page |
|| Abkratzen | ✔* | ✔* | \* Bei Klick verlassen Sie die App für das Scratch Off Erlebnis |
|| Video | ✔* | ✔* | \* Nur animierte GIFs, <br>Für Android benötigt Braze [GIF-Unterstützung][GIFsupport] in der Implementierung |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integration

### Schritt 1: Erstellen Sie eine Datenquelle für Movable Ink

Kunden müssen eine Datenquelle erstellen, die entweder eine CSV-Datei, ein Website-Import oder eine API-Integration sein kann.

![Verschiedene Optionen für Datenquellen, die angezeigt werden: CSV-Upload, Website oder API-Integration.]({% image_buster /assets/img/movable_ink/movable_ink1.png %})

{% tabs local %}
{% tab CSV-Datenquelle %}
- **CSV-Datenquelle**: Jede Zeile muss mindestens eine Segmentspalte und eine Inhaltsspalte haben. Nachdem Sie Ihre CSV-Datei hochgeladen haben, wählen Sie aus, welche Spalten für die Suche nach dem Inhalt verwendet werden sollen. [Beispiel CSV-Datei]({% image_buster /assets/download_file/movable_ink_CSV.csv %})

![Die Felder, die angezeigt werden, wenn Sie "CSV" als Ihre Datenquelle auswählen.]({% image_buster /assets/img/movable_ink/movable_ink2.png %})
{% endtab %}
{% tab Website Datenquelle %}
- **Website Datenquelle**: Jede Zeile muss mindestens eine Segmentspalte und eine Inhaltsspalte haben. Nachdem Sie Ihre CSV-Datei hochgeladen haben, wählen Sie aus, welche Spalten für die Ausrichtung des Inhalts verwendet werden sollen.
  - Im Rahmen dieses Prozesses müssen Sie eine Karte erstellen:
    - Welche Felder als Segmente verwendet werden sollen
    - Welche Felder Sie als Datenfelder haben möchten, die dynamisch in der Kreation personalisiert werden können (z.B.: Benutzerattribute oder benutzerdefinierte Attribute wie Vorname, Nachname, Stadt usw.)

![Die Felder, die angezeigt werden, wenn Sie "Website" als Ihre Datenquelle auswählen.]({% image_buster /assets/img/movable_ink/movable_ink3.png %})
{% endtab %}
{% tab API-Integrationen %}
- **API-Integrationen**: Verwenden Sie die API Ihres Unternehmens, um Inhalte direkt aus einer API-Antwort zu erzeugen.

![Die Felder, die angezeigt werden, wenn Sie "API-Integration" als Ihre Datenquelle auswählen]({% image_buster /assets/img/movable_ink/movable_ink4.png %})
{% endtab %}
{% endtabs %}

### Schritt 2: Erstellen Sie eine Kampagne auf der Movable Ink-Plattform

Erstellen Sie auf dem Startbildschirm von Movable Ink eine Kampagne. Sie können wählen zwischen E-Mail aus HTML, E-Mail aus Bild oder einem Block, der in jedem Kanal verwendet werden kann, einschließlich Push, In-App-Nachricht und Content Cards (vorgeschlagen).
Wir empfehlen Ihnen auch, einen Blick auf die verschiedenen Inhaltsoptionen zu werfen, die über Blöcke verfügbar sind.

![Ein Bild davon, wie die Movable Ink-Plattform aussieht, wenn Sie eine neue Movable Ink-Kampagne erstellen.]({% image_buster /assets/img/movable_ink/movable_ink5.png %}){: style="max-width:70%"}

Movable Ink verfügt über einen einfachen Editor, mit dem Sie Elemente wie Text, Bilder usw. per Drag & Drop verschieben können. Wenn Sie Ihre Datenquelle ausgefüllt haben, können Sie mithilfe der Dateneigenschaften dynamisch ein Bild erzeugen. Darüber hinaus können Sie innerhalb dieses Flusses auch Fallbacks für Benutzer erstellen, wenn die Kampagne gesendet wird und ein Benutzer nicht den Personalisierungskriterien entspricht.

![Der Blockeditor von Movable Ink zeigt die verschiedenen anpassbaren Elemente.]({% image_buster /assets/img/movable_ink/create_campaign2.png %})

Bevor Sie Ihre Kampagne abschließen, sollten Sie eine Vorschau der dynamischen Bilder anzeigen und die Abfrageparameter testen, um zu sehen, wie die Bilder bei der Anzeige aussehen. Wenn Sie fertig sind, wird eine dynamische URL generiert, die dann in Braze! eingefügt werden kann.

Weitere Informationen zur Verwendung der Movable Ink Plattform finden Sie im [Movable Ink Support Center][support]

### Schritt 3: Erhalten Sie Movable Ink Inhalt URL

Um Movable Ink-Inhalte in Braze-Nachrichten einzubinden, müssen Sie die Quell-URL finden, die Movable Ink Ihnen zur Verfügung gestellt hat. 

Um die Quell-URL zu erhalten, müssen Sie den Inhalt im Movable Ink-Dashboard einrichten und dann von dort aus Ihren Inhalt fertigstellen und exportieren. Kopieren Sie auf der Seite **Finish** die Quell-URL(`img src`) aus dem Creative Tag.

![Die Seite, die erscheint, nachdem Sie Ihre Movable Ink-Kampagne abgeschlossen haben, hier finden Sie Ihre Inhalts-URL.]({% image_buster /assets/img/movable_ink/obtain_url.png %}){: style="max-width:80%;"}

Als nächstes fügen Sie in der Braze Platform die URL in das entsprechende Feld ein. Entsprechende Felder für Ihren Nachrichtenkanal finden Sie in Schritt 4. Ersetzen Sie schließlich alle Merge-Tags (z. B. {% raw %}```&mi_u=%%email%%```{% endraw %}) durch die entsprechende Liquid-Variable (z. B. {% raw %}```&mi_u={{${email_address}}}```{% endraw %}).

### Schritt 4: Erfahrung mit Braze

{% tabs local %}
{% tab E-Mail %}
Fügen Sie auf der Braze-Plattform Ihr kreatives Tag in den Text Ihrer E-Mail ein.![]({% image_buster /assets/img/movable_ink/web2.png %}){: style="max-width:90%"}<br><br>

{% endtab %}
{% tab Push-Benachrichtigung %}

1. In der Braze Plattform:
	- Android Push: Fügen Sie die URL in die Felder **Push-Symbol-Bild** und **Erweitertes Benachrichtigungsbild** ein.<br>![]({% image_buster /assets/img/movable_ink/android.png %}){: style="max-width:60%"}<br><br>
	- iOS Push: Fügen Sie die URL in das Feld **Medienlink** ein und geben Sie das Dateiformat an, das Sie verwenden.<br>![]({% image_buster /assets/img/movable_ink/ios.png %}){: style="max-width:60%"}<br><br>
	- Web-Push: Fügen Sie die URL in die Felder **Push-Symbol-Bild** und **Großes Benachrichtigungsbild** ein.<br>![]({% image_buster /assets/img/movable_ink/web.png %}){: style="max-width:60%"}<br><br>
2. Um sicherzustellen, dass Bilder nicht zwischengespeichert werden, stellen Sie der URL in der Nachricht leere Liquid-Tags voran: <br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}

{% endtab %}
{% tab In-App-Nachricht %}

1. Fügen Sie auf der Braze-Plattform die URL in das Feld **Rich Notification Media** ein.![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. Geben Sie eine eindeutige URL an, um das Zwischenspeichern zu verhindern. Um sicherzustellen, dass die Echtzeitbilder von Movable Ink funktionieren und nicht durch das Zwischenspeichern beeinträchtigt werden, fügen Sie mit Liquid einen Zeitstempel an das Ende der URL des Movable Ink-Bildes an.

Verwenden Sie dazu die folgende Syntax und ersetzen Sie die Bild-URL nach Bedarf:
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
Diese Vorlage nimmt die aktuelle Zeit (in Sekunden), hängt sie an das Ende der Registerkarte "Movable Ink image" (als Abfrageparameter) an und gibt dann das Endergebnis aus. Sie können eine Vorschau mit der Registerkarte **Test** anzeigen - dies bewertet den Code und zeigt eine Vorschau an.

**3\.** Und schließlich sollten Sie die Mitgliedschaft in einem Segment neu bewerten. Aktivieren Sie dazu die Option `Re-evaluate audience membership and liquid at send-time`, die sich im Schritt **Zielgruppen** einer Kampagne befindet. Wenn diese Option nicht verfügbar ist, wenden Sie sich an Ihren Customer Success Manager oder den Braze-Support. Mit dieser Option werden die Braze SDKs angewiesen, die Kampagne mit einer eindeutigen URL jedes Mal neu anzufordern, wenn eine In-App-Nachricht ausgelöst wird.

{% endtab %}
{% tab Inhalt Karte %}

1. Fügen Sie auf der Braze-Plattform die URL in das Feld **Rich Notification Media** ein.![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. Für Mobiltelefone: Die Bilder der Content Cards auf iOS und Android werden beim Empfang zwischengespeichert und nicht aktualisiert. 
  - Als Abhilfe planen Sie Ihre Kampagne als tägliche, wöchentliche oder monatliche wiederkehrende Nachricht mit einem entsprechenden Ablaufdatum, damit die Inhaltskarte neu geplant wird. Zum Beispiel sollte eine Inhaltskarte, die einmal am Tag aktualisiert werden soll, als täglicher geplanter Versand mit einem Ablaufdatum von 1 Tag eingestellt werden.
3. Um sicherzustellen, dass die Echtzeit-Bilder von Movable Ink funktionieren und nicht durch das Zwischenspeichern beeinträchtigt werden, wenn die Content Card neu generiert wird, verwenden Sie Liquid, um einen Zeitstempel an das Ende der Movable Ink-Bild-URL anzuhängen.

Verwenden Sie dazu die folgende Syntax und ersetzen Sie die Bild-URL nach Bedarf:
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
Diese Vorlage nimmt die aktuelle Zeit (in Sekunden), hängt sie an das Ende der Registerkarte "Movable Ink image" (als Abfrageparameter) an und gibt dann das Endergebnis aus. Sie können eine Vorschau auf der Registerkarte **Test** anzeigen, die den Code auswertet und eine Vorschau anzeigt.

{% endtab %}
{% endtabs %}

## Fehlersuche

### Werden dynamische Bilder nicht korrekt angezeigt? Mit welchem Kanal haben Sie Schwierigkeiten?
- **Schieben**: Stellen Sie sicher, dass Sie eine leere Logik vor Ihrer Movable Ink Bild-URL haben: <br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}
- **In-App-Nachrichten und Inhaltskarten**: Achten Sie darauf, dass die Bild-URL für jeden Abdruck eindeutig ist. Dies kann durch Anhängen der entsprechenden Flüssigkeit geschehen, so dass jede URL anders ist. Siehe [Anweisungen für In-App- und Inhaltskarten-Nachrichten][Anweisungen]. 
- **Bild wird nicht geladen**: Stellen Sie sicher, dass Sie alle "Merge-Tags" durch die entsprechenden Liquid-Felder im Braze Dashboard ersetzen. Zum Beispiel: {% raw %}```https://mi-msg.com/p/rp/image.png?mi_u=%%email%%```{% endraw %} mit {% raw %}```https://mi-msg.com/p/rp/image.png?mi_u={{${email_address}}}```{% endraw %}.

### Haben Sie Probleme mit der Anzeige von GIFs auf Android?
- Android erfordert GIF-Unterstützung bei der Implementierung. Folgen Sie dem Android [In-App-Nachrichtenanpassung][GIFsupport] Artikel, wenn Sie dies noch nicht eingerichtet haben.

[1]: https://www.movableink.com/
[Datenquelle]: ({% image_buster /assets/img/movable_ink/movable_ink1.png %})
[Unterstützung]: https://support.movableink.com/
[GIFsupport]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs/
[Anleitung]: {{site.baseurl}}/partners/message_personalization/dynamic_content/movable_ink/#step-4-braze-experience
[1]: ({% image_buster /assets/img/movable_ink/android.png %})
[2]: ({% image_buster /assets/img/movable_ink/ios.png %})
[3]: ({% image_buster /assets/img/movable_ink/web.png %})