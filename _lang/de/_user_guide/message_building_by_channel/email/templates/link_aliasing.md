---
nav_title: Link-Aliasing
article_title: Link Aliasing
alias: /link_aliasing/
page_order: 3
description: "Dieser Artikel beschreibt, wie Link-Aliasing funktioniert, und enthält Beispiele dafür, wie Ihre Links aussehen werden."
channel:
  - email

---

# [![Braze Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"} Link-Aliasing
# [![Braze Lernkurs]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"} Link-Aliasing
 
> Verwenden Sie Link-Aliasing, um wiedererkennbare, benutzergenerierte Namen zur Identifizierung von Links zu erstellen, die in E-Mail-Nachrichten von Braze gesendet werden. Diese Links sind für Segmentierungs-Retargeting, aktionsbasiertes Triggering und Link-Analysen verfügbar.

## Über Link-Aliasing

Mit Link-Aliasing können Sie benutzergenerierte Namen erstellen, um in E-Mails versandte Links zu identifizieren und zu verfolgen. Auf diese Weise können Sie diese erkennbaren Link-Aliase in Ihren E-Mails effizient nutzen, um das Engagement zu verfolgen und die Kampagnenleistung zu analysieren, ohne auf den vollständigen Link verweisen zu müssen.

Mit Link-Aliasing können Sie:

- **Sprechen Sie Nutzer erneut an, die auf bestimmte Links geklickt haben:** Identifizieren Sie Nutzer, die auf einen Link geklickt haben, und sprechen Sie sie an.
- **Aktionsbasierte Trigger erstellen:** Senden Sie eine E-Mail, wenn ein Benutzer auf einen Link klickt.
- **Metriken analysieren:** Vergleichen Sie, wie viele Benutzer auf Link A und Link B geklickt haben.

### Funktionsweise

Braze identifiziert Links in E-Mails eindeutig, indem es einen zusätzlichen Parameter namens `lid` (auch bekannt als Bezeichner des Links) an jede Link-URL anhängt. Dieser `lid`-Wert ermöglicht es Braze, die Interaktionen der Nutzer:innen mit dem Link zu tracken, zu überwachen und zu aggregieren, auch wenn die übrigen URL-Parameter unterschiedlich sein können. So erhalten Sie Einblicke in die Art und Weise, wie Nutzer mit den Inhalten Ihrer E-Mail-Kampagnen umgehen.

Die Bezeichner der Links werden auch aktualisiert, wenn eine E-Mail-Kampagne, ein Canvas mit einer Nachricht oder ein Content-Block dupliziert wird.

## Link-Alias erstellen

Um einen Link-Alias zu erstellen, gehen Sie folgendermaßen vor: 

1. Gehen Sie in Ihrer Kampagne oder Canvas-Komponente zu Ihrem E-Mail-Text.
2. Wählen Sie die Registerkarte **Linkverwaltung**.
3. Braze erstellt automatisch eindeutige Standard-Link-Aliase für jeden Ihrer Links.
4. Geben Sie dem Alias einen Namen. Aliase müssen pro E-Mail-Kampagnenvariante oder Canvas-Komponente eindeutig benannt sein. 

Sie können auch einen Alias festlegen, der verwendet wird, um einen bestimmten Link zu referenzieren, wenn es um Berichte oder Segmentierung geht. 

![Link Management Seite mit vier Link-Aliases.]({% image_buster /assets/img/link_aliasing_composer.png %})

{% alert note %}
Link Aliasing wird nur in `href`-Attributen innerhalb von HTML-Anker-Tags unterstützt, wo es sicher ist, einen Abfrageparameter anzuhängen. Am besten fügen Sie am Ende Ihres Links ein Fragezeichen (?) ein, damit Braze den Wert `lid` einfach anhängen kann. Wenn Sie den Wert `lid` nicht anhängen, erkennt Braze die URL nicht für Link-Aliasing.
{% endalert %}

## Verwaltung von Link-Aliasen

Um alle Ihre getrackten Link-Aliase anzuzeigen, gehen Sie wie folgt vor:

1. Gehen Sie zu **Einstellungen** > **E-Mail-Voreinstellungen** unter **Arbeitsbereichseinstellungen**.
2. Wählen Sie die Registerkarte **Link-Aliasing-Einstellungen**.

{% alert important %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/) verwenden, finden Sie diese Einstellungen unter **Einstellungen verwalten**.
{% endalert %}

Hier können Sie sortieren, suchen und das Tracking für Link-Aliase deaktivieren.

![Tracking Link-Aliasing-Seite, die zwei Link-Aliase mit den Namen "TechPartners" und "Hilfe" zeigt, die mit einer Kampagne mit dem Namen "Email_Survey".]({% image_buster /assets/img/tracked_aliases.png %})

{% alert tip %}
Verwenden Sie die Endpunkte [Listenlink-Alias für Kampagnen]({{site.baseurl}}/get_campaign_link_alias/) und [Listenlink-Alias für Canvas]({{site.baseurl}}/get_canvas_link_alias/), um den Satz `alias` in jeder Nachrichtenvariante in einer Kampagne oder einer E-Mail-spezifischen Canvas-Komponente zu extrahieren.
{% endalert %}

Braze empfiehlt, die Links in der E-Mail zu bewerten, Link-Templates hinzuzufügen und eine Benennungskonvention zu erstellen, die für die Segmentierung und die Berichterstattung geeignet ist. Dies hilft Ihnen, den Überblick über alle Links zu behalten.

Wenn das Link-Aliasing aktiviert ist, werden Nachrichten, Inhaltsblöcke und Linkvorlagen nicht geändert. Alle vorhandenen Nachrichten, die Linkvorlagen oder Inhaltsblöcke verwenden, bleiben unverändert. Wenn Sie jedoch eine Nachricht aktualisieren, wird die Link-Alias-Markierung auf alle Links angewendet, so dass Sie die Linkvorlagen erneut anwenden müssen, damit die Links sichtbar sind.

## Wie Links mit Link-Aliasing aktualisiert werden

In den folgenden Tabellen finden Sie Beispiele für Links in einem E-Mail-Text, Link-Aliasing-Ergebnisse und Erklärungen dazu, wie der ursprüngliche Link mit Link-Aliasing aktualisiert wird.

### Permalink

**Logik:** Braze fügt ein Fragezeichen (?) ein und fügt den ersten Abfrageparameter in die URL ein.

| Link im E-Mail-Text    | Link mit Aliasing                     |
|-----------------------|----------------------------------------|
| https://www.braze.com | https://www.braze.com?lid=slfdldtqdhdk |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link mit weiteren Abfrageparametern

**Logik:** Braze erkennt andere Abfrageparameter und fügt `lid=` an das Ende der URL an.

| Link im E-Mail-Text                                            | Link mit Aliasing                                                             |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| https://www.braze.com?utm_campaign=retention&utm_source=email | https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### HTML-Link

**Logik:** Braze erkennt, dass ein Link eine URL ist und bereits ein Fragezeichen (?) enthält. Daher wird der Abfrageparameter `lid` nach dem Fragezeichen angefügt.

| Link im E-Mail-Text                                                | Link mit Aliasing                                                                |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link mit Anker

**Logik:** Braze erwartet, dass die URL eine Standardstruktur verwendet, bei der Anker (#) nach einem Fragezeichen (?) vorhanden sind. Da Braze von links nach rechts liest, werden das Fragezeichen und der Wert `lid` vor dem Anker angehängt.

| Link im E-Mail-Text                               | Link mit Aliasing                                                |
|--------------------------------------------------|-------------------------------------------------------------------|
| https://www.braze.com#bookmark1?utm_source=email | https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link mit Anker- und Erfassungs-Tag

**Logik:** Wenn Sie Link Aliasing mit URLs verwenden, die Anker (#) enthalten, erwartet Braze, dass der Anker nach den Abfrageparametern platziert wird. Das bedeutet, dass der Wert `lid` vor dem Anker angehängt werden muss, damit er richtig verfolgt werden kann. Da Braze die URL von links nach rechts liest, sollten das Fragezeichen (?) und `lid` vor dem Anker stehen.

| Link im E-Mail-Text                                                                        | Link mit Aliasing                                                                                           |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| {%raw%}`<a href="https://www.braze.com/promotions#special-offer">Check out our special offer!</a>`{%endraw%}  | {%raw%}`<a href="https://www.braze.com/promotions#special-offer?lid={{link_alias}}">Check out our special offer!</a>` {%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Link-Aliase tracken

Wählen Sie auf der Registerkarte **Linkverwaltung** aus, welche Aliase für die Segmentierung "verfolgt" werden und in den Segmentierungsfiltern vorhanden sein sollen. Beachten Sie, dass verfolgte Aliase nur der Segmentierung dienen und keinen Einfluss darauf haben, dass Ihr Link zu Berichtszwecken getrackt wird.

{% alert tip %}
Um Metriken für die Link-Interaktion zu verfolgen, stellen Sie sicher, dass Ihr Link entweder mit HTTP oder HTTPS beginnt. Um das Tracking von Klicks für bestimmte Links zu deaktivieren, referenzieren Sie auf [Universal Links und App Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/#turning-off-click-tracking-on-a-link-to-link-basis).
{% endalert %}

Mit Braze können Sie eine unbegrenzte Anzahl von Links zum Nachverfolgen auswählen. Allerdings können Sie nur die zuletzt geöffneten Links nachverfolgen. Die Benutzerprofile enthalten die 100 zuletzt angeklickten Links. Wenn Sie beispielsweise 500 Links verfolgen und ein Nutzer auf alle 500 klickt, können Sie ein Retargeting durchführen oder Segmente erstellen, die auf den 100 zuletzt angeklickten Links basieren.

{% tabs local %}
{% tab Drag-And-Drop Editor %}

![Link Management Tab des Drag-and-Drop-Editors für E-Mails.]({% image_buster /assets/img/link_management_dnd.png %})

{% endtab %}
{% tab HTML editor %}

![Tab Link Management des HTML-Editors für E-Mails.]({% image_buster /assets/img/link_management_html.png %})

{% endtab %}
{% endtabs %}

{% alert note %}
Braze verfolgt nur bis zu den letzten 100 angeklickten Link-Aliasen auf Profilebene.
{% endalert %}

### Aktionsbasierte Filter
 
Sie können aktionsbasierte Nachrichten erstellen, die auf einen beliebigen Link (mit oder ohne Tracking) abzielen, oder Nutzer:innen anhand eines Klicks auf einen Alias in einer beliebigen E-Mail-Kampagne oder Canvas-Komponente retargeten.

![Aktionsbasierte Optionen zum Targeting von Nutzern:in, die auf einen Alias in einer Canvas-Komponente geklickt oder mit einer Kampagne interagiert haben.]({% image_buster /assets/img/link_aliasing_action_based_filters.png %})

### Segmentierungsfilter

Wenn Sie in Braze einen Link-Alias in Ihrer E-Mail haben und ein Benutzer darauf klickt, wird das Ereignis im Profil des Benutzers mit dem Alias aufgezeichnet.

Wenn Sie den Segmentierungsfilter "Geklickter Alias in einer beliebigen Kampagne oder einem beliebigen Canvas-Schritt" verwenden und später beschließen, diesen Link-Alias umzubenennen, werden die vorherigen Klickdaten im Benutzerprofil **nicht** aktualisiert, d.h. er wird weiterhin als der vorherige Link-Alias angezeigt. Wenn Sie also Nutzer:innen auf der Grundlage des neuen Link-Alias zusammenstellen, werden die Daten des vorherigen Link-Alias nicht berücksichtigt.

Wenn Sie den Segmentierungsfilter "Alias in Kampagne angeklickt" oder "Alias in Canvas angeklickt" verwenden, werden Ihre Benutzer danach gefiltert, ob sie einen bestimmten Alias in einer bestimmten Kampagne oder einem Canvas angeklickt haben. Wenn mehrere Benutzer dieselbe E-Mail-Adresse verwenden und der Alias-Link angeklickt wird, werden die Benutzerprofile aller anderen Benutzer, die dieselbe E-Mail-Adresse verwenden, aktualisiert. 

Die folgenden Filter für die Segmentierung gelten für Klick-Events, die zum Zeitpunkt der Verarbeitung des Events getrackt werden. Das bedeutet, dass nicht getrackte Links vorhandene Daten nicht löschen und dass das Tracking eines Links die Daten nicht wieder auffüllt. Weitere Einzelheiten finden Sie unter [Segmentierungsfilter]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).

#### Tracking für Links aufheben

Wenn Sie das Tracking eines Links aufheben, werden vorhandene Segmente mit dem Filter nicht erneut dem nicht getrackten Alias zugewiesen. Die alten Daten bleiben in den Nutzerprofilen erhalten, bis sie durch neuere Daten ersetzt werden. 

Das Tracking von Links in archivierten Nachrichten wird automatisch aufgehoben. Wenn archivierte Nachrichten jedoch nicht archiviert werden, müssen die Links erneut getrackt werden. Wenn Link-Aliase verfolgt werden, werden die Link-Berichte anhand des Alias indexiert und nicht anhand von Top-Level-Domänen oder vollständigen URLs.

![Analytics Tab für Kampagnen, der drei Link-Aliases und deren Gesamtklicks anzeigt.]({% image_buster /assets/img/link_aliasing_click_table.png %})

### Event „E-Mail Klicks“

Wenn Sie Ihre Engagement-Daten mit Currents exportieren, wird ein E-Mail-Klick-Event etwas anders aussehen, wenn Sie Link Aliasing aktiviert haben. Wenn das Link Aliasing aktiviert ist, verfügt es über zwei zusätzliche Felder für das [Event „E-Mail-Klicks“]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-clicks-events/): `link_id` und `link_alias`.

```json
// Email Click: users.messages.email.Click
{
  "id": (string) unique ID of this event,
  "user_id": (string) Braze user ID of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) ID of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) ID of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) ID of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the URL that was clicked (Email Click events only),
  "user_agent": (string) description of the user's system and browser for the event (Email Click and Open events only),
  "ip_pool": (string) IP pool used for message sending,
  "link_id": (string) unique value generated by Braze for the URL,
  "link_alias": (string) alias name set when the message was sent
}
```

{% alert update %}
Das Verhalten für `dispatch_id` unterscheidet sich zwischen Canvas und Kampagnen, da Braze Canvas-Schritte (mit Ausnahme von Event-Schritten, die geplant werden können) als getriggerte Events behandelt, selbst wenn sie „geplant“ sind. Erfahren Sie mehr über [`dispatch_id` Verhalten]({{site.baseurl}}/help/help_articles/data/dispatch_id/) in Canvas und Kampagnen.

_Update im August 2019 vermerkt._
{% endalert %}

## Link Aliasing in Content-Blöcken

Bei neuen Inhaltsblöcken werden die Links geändert, wobei Braze jedem Link gegebenenfalls eine `lid={{placeholder}}` anhängt. Dieser Platzhalterwert wird aufgelöst, wenn er in eine E-Mail-Nachrichtenvariante eingefügt wird.

Um die Links in bestehenden Inhaltsblöcken zu ändern, die erstellt wurden, bevor Braze das Link-Aliasing aktiviert hat, duplizieren Sie die bestehenden Inhaltsblöcke und ändern dann die Links in den duplizierten Inhaltsblöcken.

Wenn ein Inhaltsblock ohne einen `lid` Wert in eine neue Nachricht eingefügt wird, werden die Links aus diesem Inhaltsblock nicht mit einem Alias verfolgt. Wenn ein neuer Content-Block in eine „alte“ Nachrichtenvariante eingefügt wird, werden die Links dieser Nachrichtenvariante durch Link Aliasing erkannt. Links aus dem Inhaltsblock werden ebenfalls erkannt. Allerdings können „alte“ Content-Blöcke keine „neuen“ Content-Blöcke verschachteln.

{% alert tip %}
Für Content-Blöcke empfiehlt Braze die Erstellung von Kopien bestehender Content-Blöcke zur Verwendung in neuen Nachrichten. Dies kann durch Massenvervielfältigung erfolgen, um Szenarien zu vermeiden, in denen Sie auf einen Content-Block verweisen, der in einer neuen Nachricht nicht für Link Aliasing aktiviert wurde.
{% endalert %}

## Link-Aliasing für von Liquid generierte URLs

Für URLs, die von Liquid generiert werden, z.B. `assign` Anweisungen im HTML oder von einem Content-Block, müssen Sie ein Fragezeichen (`?`) an den Liquid-Tag anfügen. Dies erlaubt Braze das Anhängen von Abfrageparametern (`lid = somevalue`), so dass Link-Aliasing richtig funktionieren kann. Wenn Sie nicht angeben, wo die Abfrageparameter angehängt werden sollen, erkennt Link-Aliasing diese URLs nicht und die Link-Templates können nicht angewendet werden.

### Beispiel

Sehen Sie sich dieses Link-Aliasing-Beispiel für die empfohlene Formatierung des Links an:

{% raw %}
```liquid
{% assign link1 = "https://www.braze1.com" %}

<a href="{{link1}}?">Click Here</a>
```
{% endraw %}

Wenn der Link Parameter enthält, die ein Fragezeichen (`?`) enthalten, können Sie dieses im Anker-Tag durch ein kaufmännisches Und (`&`) ersetzen, wie in diesem Beispiel:

{% raw %}
```liquid
{% assign link_with_params = "https://www.braze1.com?param_1&param_2" %}

<a href="{{link_with_params}}&">Click Here</a>
```
{% endraw %}


