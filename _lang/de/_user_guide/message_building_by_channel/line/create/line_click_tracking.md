---
nav_title: LINE click tracking
article_title: LINE Click Tracking
page_order: 2
description: "Auf dieser Seite erfahren Sie, wie Sie das Tracking von Klicks in Ihren LINE Nachrichten aktivieren, verkürzte Links testen, Ihre angepasste Domain in verfolgten Links verwenden und vieles mehr."
page_type: reference
alias: /line/click_tracking/
channel:
 - LINE
---

# LINE click tracking

> Auf dieser Seite erfahren Sie, wie Sie das Tracking von Klicks in Ihren LINE Nachrichten aktivieren, verkürzte Links testen, Ihre angepasste Domain in verfolgten Links verwenden und vieles mehr.


Wenn das LINE-Klick-Tracking aktiviert ist, verkürzt Braze automatisch Ihre URLs, fügt Tracking-Mechanismen hinzu und zeichnet Klicks in Realtime auf. Während LINE Ihnen aggregierte Klickdaten bietet, liefert Braze granulare Nutzer:innen-Daten, die zeitnah und umsetzbar sind. Mit diesen Daten können Sie gezieltere Segmentierungs- und Retargeting-Strategien entwickeln, z. B. die Segmentierung von Nutzern auf der Grundlage ihres Klickverhaltens und das Auslösen von Nachrichten als Reaktion auf bestimmte Klicks.

LINE Click Tracking kann für text-, rich- und kartenbasierte Nachrichten verwendet werden. Es unterstützt Links in Buttons und Bildbereichen, die eine URL als Klick-Aktion haben. Sie können URLs auch mit Liquid und angepassten Domains anpassen.

## Funktionsweise

Sie können die Einstellungen für das Tracking von LINE-Klicks auf dem Tab **Einstellungen** verwalten, während Sie eine Nachricht verfassen. Wenn diese Funktion aktiviert ist, werden URLs unter Verwendung der Standard Braze Domain (`https://brz.ai`) oder der angepassten Domain, die für die Abo-Gruppe angegeben wurde, verkürzt und für den Nutzer:innen personalisiert.

Alle URLs, die mit `http://` oder `https://` beginnen, werden gekürzt. Sie können bis zu 25 URLs in einer Nachricht verwenden. Verkürzte URLs, die Liquid Personalisierung (wie Tracking auf Nutzerebene oder UTM-Parameter) enthalten, sind zwei Monate lang gültig.

## Klick Tracking einrichten

### Textnachrichten

So richten Sie das Tracking von Klicks für eine Textnachricht ein:

1. Ziehen Sie eine **Textnachricht** in den Composer und fügen Sie eine URL in das Textfeld ein.

![LINE Nachrichten-Editor mit einer Textnachricht, die eine lange URL enthält: https://braze.com/docs/user_guide/message_building_by_channel/line/create/]({% image_buster /assets/img/line/click_tracking_text_message.png %})

{: start="2"}
2\. Gehen Sie auf den Tab **Einstellungen** und bestätigen Sie, dass **Click Tracking** aktiviert ist. Das Tracking von Klicks ist standardmäßig für alle neuen Nachrichten aktiviert.

{% alert note %}
Auf dem Tab **Einstellungen** oder **Vorschau & Test** können Sie eine Vorschau des verkürzten Links sehen. Der vollständige Link wird im Composer angezeigt, während Sie Ihre Nachricht erstellen.
{% endalert %}

![LINE Nachrichten-Editor Tab "Einstellungen" mit " mit eingeschaltetem "Click Tracking" und einer Vorschau Textnachricht mit einer verkürzten URL: https://olaf.brz.ai/p/9rcfdqdD]({% image_buster /assets/img/line/click_tracking_settings.png %})

### Rich-Nachrichten

So richten Sie das Click Tracking für eine Rich Message ein:

1. Ziehen Sie eine **Rich Nachricht** in den Composer und wählen Sie ein Template aus.
2. Wählen Sie die **URI** für das **Klickverhalten** für den entsprechenden antippbaren Bereich aus.
3. Geben Sie eine URL in das Feld **URL öffnen** ein.

![LINE Nachrichten-Editor mit einer Rich Nachricht mit zwei antippbaren Bereichen, die jeweils eine URL haben.]({% image_buster /assets/img/line/rich_message_click_tracking.png %})

{: start="4"}
4\. Gehen Sie auf den Tab **Einstellungen** und bestätigen Sie, dass **Click Tracking** aktiviert ist. Das Tracking von Klicks ist standardmäßig für alle neuen Nachrichten aktiviert.

### Kartenbasierte Nachrichten

So richten Sie das Tracking von Klicks für eine kartenbasierte Nachricht ein:

1. Ziehen Sie eine **kartenbasierte Nachricht** in den Composer.
2. Wählen Sie die **URI** für das **Klickverhalten** für die entsprechenden Karten- oder Button-Bereiche aus.

![LINE Nachrichten-Editor mit einer kartenbasierten Nachricht mit zwei Buttons, die jeweils eine URL enthalten.]({% image_buster /assets/img/line/card_based_message_click_tracking.png %})

{: start="3"}
3\. Gehen Sie auf den Tab **Einstellungen** und bestätigen Sie, dass **Click Tracking** aktiviert ist. Das Tracking von Klicks ist standardmäßig für alle neuen Nachrichten aktiviert.

{% alert note %}
URLs in den Feldern **Titel** oder **Beschreibung** werden nicht gekürzt, da diese Felder in LINE nicht anklickbar sind.
{% endalert %}

## Angepasste Domains

Das LINE Tracking von Klicks erlaubt es Ihnen, Ihre eigene Domain zu verwenden, um das Erscheinungsbild Ihrer verkürzten URLs zu personalisieren und so ein einheitliches Markenimage zu vermitteln. Weitere Informationen finden Sie unter [Angepasste Domains]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains).

## Flüssige Personalisierung in URLs

Sie können Ihre URL direkt im Braze Composer dynamisch aufbauen, so dass Sie dynamische UTM-Parameter zu Ihren URLs hinzufügen oder Benutzern einzigartige Links senden können (z. B. die Weiterleitung zu einem abgebrochenen Warenkorb oder zu einem bestimmten Produkt, das wieder auf Lager ist).
URLs können durch die Verwendung beliebiger unterstützter Tags zur Personalisierung in Liquid dynamisch generiert werden.

{% raw %}
```
https://example.com/?campaign_utm={{campaign.${api_id}}}&user_attribute={{custom_attribute.${attribute1}}}
```
{% endraw %}

Sie können auch angepasste Liquid-Variablen kürzen, wie im folgenden Beispiel gezeigt:

{% raw %}
```liquid
{% assign url_var = {{event_properties.${url_slug}}} %}
https://example.com/{{url_var}}
```
{% endraw %}

## Kürzen Sie URLs, die von Liquid-Variablen gerendert werden

Braze verkürzt URLs, die von Liquid gerendert werden, auch solche, die in API-triggernden Eigenschaften enthalten sind. Wenn {% raw %}`{{api_trigger_properties.${url_value}}}`{% endraw %} beispielsweise eine gültige URL darstellt, kürzen und tracken wir diese URL, bevor wir die LINE Nachricht senden.

## Testen

Bevor Sie Ihre Kampagne oder Ihr Canvas einführen, sollten Sie Ihre Nachricht zunächst in einer Vorschau testen. Gehen Sie dazu auf den Tab **Test**, um eine Vorschau anzuzeigen und eine LINE Nachricht an Inhaltstestgruppen oder einen einzelnen Nutzer:innen zu senden.

Diese Vorschau wird mit der entsprechenden Personalisierung und der verkürzten URL aktualisiert. 

{% alert important %}
Wenn ein Entwurf innerhalb eines aktiven Canvas erstellt wird, wird keine verkürzte URL generiert. Die eigentliche verkürzte URL wird generiert, wenn der Canvas-Entwurf aktiviert wird.
{% endalert %}

## Berichterstattung

Die Tabelle LINE Performance enthält die Spalte **Gesamtklicks**, die die Anzahl der Klickereignisse pro Variante und die zugehörige Klickrate anzeigt. Weitere Einzelheiten zu den LINE Metriken finden Sie unter [LINE Nachrichten Performance]({{site.baseurl}}/user_guide/message_building_by_channel/line/reporting).

![Performance für einen LINE Canvas-Schritt.]({% image_buster /assets/img/line/line_step_performance.png %}){: style="max-width:30%;"}

Die Daten der Klicks werden automatisch im Analytics Dashboard angezeigt. 

![LINE performance analytics Dashboard.]({% image_buster /assets/img/line/line_performance.png %})

## Nutzer-Retargeting

Sie können Nutzer:innen, die auf eine URL in einer LINE Nachricht geklickt haben, mit den folgenden Segmentierungsfiltern und Triggern retargeten:

- Aktionsbasierte Auslöser
    - mit Kampagne interagieren
    - Interagieren Sie mit Step

![LINE aktionsbasierte Zustellung triggern.]({% image_buster /assets/img/line/line_action_based.png %})

- Segmentierungsfilter
    - Kampagne angeklickt/geöffnet
    - Geklickte/geöffnete Kampagne oder Canvas mit Tag 
    - Schritt angeklickt/geöffnet

![Filtergruppe, die alle drei Segmentierungsfilter anzeigt: "Angeklickte/geöffnete Kampagne", "Angeklickte/geöffnete Kampagne oder Canvas mit Tag" und "Angeklickter/geöffneter Schritt".]({% image_buster /assets/img/line/line_segmentation_filters.png %})

## Häufig gestellte Fragen

### Sind die Links, die ich beim Testversand erhalte, echte URLs?

Ja, beim Testversand werden echte URLs generiert. Die genaue URL, die in einer gestarteten Kampagne gesendet wird, kann sich jedoch von der URL unterscheiden, die in einem Testversand gesendet wurde.

### Kann ich UTM-Parameter zu einer URL hinzufügen, bevor sie gekürzt wird?

Ja, es können sowohl statische als auch dynamische Parameter hinzugefügt werden.

### Wie lange bleiben verkürzte URLs gültig?

Personalisierte URLs sind ab dem Zeitpunkt der URL-Registrierung zwei Monate lang gültig.

### Muss das Braze SDK installiert werden, um URLs zu verkürzen?

Nein, Click Tracking funktioniert ohne SDK-Integration.

### Kann ich wissen, welche einzelnen Benutzer auf eine URL klicken?

Ja Wenn das Tracking von Klicks aktiviert ist, können Sie Nutzer:innen, die auf URLs geklickt haben, mit den [Retargeting-Filtern von LINE](#retargeting-users) erneut ansprechen.

### Funktioniert das Click Tracking mit Deeplinks oder universellen Links?

Click Tracking funktioniert nicht mit Deeplinks. Sie können universelle Links von Anbietern wie Branch oder Appsflyer kürzen, aber Braze ist nicht in der Lage, Fehler zu beheben, die dabei auftreten können (z.B. wenn die Attribution unterbrochen wird oder die Weiterleitung fehlschlägt).

### Zählen Vorschauen in der LINE App als Klicks?

Nein, sie tragen nicht zur Klickrate für LINE Nachrichten bei.