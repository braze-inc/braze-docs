---
nav_title: Verschachtelte Objekte
article_title: Verschachtelte Objekte in benutzerdefinierten Ereignissen
page_order: 1
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie verschachtelte JSON-Daten als Eigenschaften von benutzerdefinierten Ereignissen und Käufen senden und wie Sie diese verschachtelten Objekte in Ihren Nachrichten verwenden können."
---

# Verschachtelte Objekte in angepassten Events

> Auf dieser Seite erfahren Sie, wie Sie verschachtelte JSON-Daten als Eigenschaften von angepassten Events und Käufen senden und wie Sie diese verschachtelten Objekte in Ihren Nachrichten verwenden können.

Sie können verschachtelte Objekte - Objekte, die sich innerhalb eines anderen Objekts befinden - verwenden, um verschachtelte JSON-Daten als Eigenschaften von benutzerdefinierten Ereignissen und Käufen zu senden. Diese verschachtelten Daten können als Template für personalisierte Informationen in Nachrichten, zum Triggern von Nachrichtensendungen und zur Segmentierung von Nutzer:innen verwendet werden.

## Beschränkungen

- Verschachtelte Daten werden sowohl für [angepasste Events]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) als auch für [Kauf-Events]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/) unterstützt, jedoch nicht für andere Event-Typen.
- Objekte mit Event-Eigenschaften, die Array- oder Objektwerte enthalten, können eine Nutzlast für Event-Eigenschaften von bis zu 100 KB haben.
- Schemata für Event-Eigenschaften können nicht für Kauf-Events erstellt werden.
- Die Schemata für Event-Eigenschaften werden durch Stichproben angepasster Events aus den letzten 24 Stunden generiert.

### Minimale SDK-Versionen

Die folgenden SDK-Versionen unterstützen verschachtelte Objekte:

{% sdk_min_versions swift:5.0.0 android:1.0.0 web:3.3.0 %}

## Schritt 1: Ein Schema generieren

Sie können auf die verschachtelten Daten in Ihrem angepassten Event zugreifen, indem Sie für jedes Event ein Schema mit verschachtelten Event-Eigenschaften erstellen. Um ein Schema zu erstellen:

1. Gehen Sie zu **Dateneinstellungen** > Angepasste Events.
2. Wählen Sie **Eigenschaften verwalten** für die Ereignisse mit verschachtelten Eigenschaften.
3. Wählen Sie den Button <i class="fas fa-arrows-rotate"></i>, um das Schema zu erstellen. Um das Schema anzuzeigen, wählen Sie den Button <i class="fas fa-plus"></i> plus.

![]({% image_buster /assets/img_archive/schema_generation_example.png %}){: style="max-width:80%;"}

Wenn in Zukunft neue Eigenschaften gesendet werden, sind sie erst dann im Schema enthalten, wenn es neu generiert wird. Schemas können alle 24 Stunden neu generiert werden.

## Schritt 2: Verwenden Sie das verschachtelte Objekt

Sie können die verschachtelten Daten bei der Segmentierung und Personalisierung referenzieren. Beachten Sie, dass ein Schema nicht erforderlich ist. Beispiele für die Verwendung finden Sie in den folgenden Abschnitten:

- [Körper der API-Anfrage](#api-request-body)
- [Liquid-Templates](#liquid-templating)
- [Auslösen von Nachrichten](#message-triggering)
- [Segmentierung](#segmentation)
- [Personalisierung](#personalization)

### Körper der API-Anfrage

{% tabs %}
{% tab Music Example %}

Im Folgenden finden Sie ein `/users/track` Beispiel mit einem angepassten Event "Created Playlist". Nachdem eine Wiedergabeliste erstellt wurde, erfassen Sie die Eigenschaften der Wiedergabeliste durch Senden:
- Eine API-Anfrage, die "Songs" als Eigenschaft auflistet
- Ein Array mit den verschachtelten Eigenschaften der Songs

```
...
"properties": {
  "songs": [
    {
      "title": "Smells Like Teen Spirit",
      "artist": "Nirvana",
      "album": {
        "name": "Nevermind",
        "yearReleased": "1991"
      }
    },
    {
      "title": "While My Guitar Gently Weeps",
      "artist": "the Beatles",
      "album": {
        "name": "The Beatles",
        "yearReleased": "1968"
      }
    }
  ]
}
...
```
{% endtab %}
{% tab Restaurant Example%}

Im Folgenden finden Sie ein `/users/track` Beispiel mit einem angepassten Event "Bestellt". Nachdem ein Auftrag abgeschlossen wurde, erfassen Sie die Eigenschaften dieses Auftrags, indem Sie ihn senden:
- Eine API-Anfrage, die "r_details" als Eigenschaft auflistet
- Die verschachtelten Eigenschaften dieser Reihenfolge

```
...
"properties": {
  "r_details": {
    "name": "McDonalds",
    "identifier": "12345678",
    "location" : {
      "city": "Montclair",
      "state": "NJ"
    }
  }
}
...
```
{% endtab %}
{% endtabs %}

{% alert note %}
Wenn bei verschachtelten Event-Eigenschaften das Jahr kleiner als 0 oder größer als 3000 ist, speichert Braze diese Werte nicht beim Nutzer:in.
{% endalert %}

### Liquid-Templates

Im Folgenden wird gezeigt, wie Sie ein Liquid Template erstellen, das die verschachtelten Eigenschaften referenziert, die in der [vorherigen API-Anfrage](#api-request-body) angefordert wurden.

{% tabs %}
{% tab Music Example %}
Templating in Liquid in einer Nachricht, die durch das Ereignis "Created Playlist" getriggert wird:

{% raw %}
`{{event_properties.${songs}[0].album.name}}`: "Vergessen Sie's"<br>
`{{event_properties.${songs}[1].title}}`: "Während meine Gitarre sanft weint"
{% endraw %}

{% endtab %}
{% tab Restaurant Example %}
Templating in Liquid in einer Nachricht, die durch das Ereignis "Bestellt" ausgelöst wird:

{% raw %}
`{{event_properties.${r_details}.location.city}}`: "Montclair"
{% endraw %}

{% endtab %}
{% endtabs %}

### Auslösen von Nachrichten

Um diese Eigenschaften zum Triggern einer Kampagne zu verwenden, wählen Sie Ihr angepasstes Event oder Ihren Kauf aus und fügen dann einen Filter für **verschachtelte Eigenschaften** hinzu. Beachten Sie, dass das Auslösen von Nachrichten für In-App-Nachrichten noch nicht unterstützt wird, aber verschachtelte Eigenschaften in der Liquid-Personalisierung in den Nachrichten werden trotzdem angezeigt.

{% tabs %}
{% tab Music Example %}

Auslösen einer Kampagne mit verschachtelten Eigenschaften durch das Ereignis "Erstellte Wiedergabeliste":

![Ein Nutzer:in wählt eine verschachtelte Eigenschaft für Eigenschaftsfilter auf einem angepassten Event.]({% image_buster /assets/img/nested_object2.png %})

Die triggernde Bedingung `songs[].album.yearReleased` "ist" "1968" passt auf ein Ereignis, bei dem einer der Titel ein Album hat, das 1968 veröffentlicht wurde. Wir verwenden die Klammerschreibweise `[]` für das Durchlaufen von Arrays und stimmen überein, wenn **ein** Element in dem durchlaufenen Array mit der Ereigniseigenschaft übereinstimmt.

{% alert important %}
Der Filter " **Nicht gleich"** passt nur, wenn keine der Eigenschaften in Ihrem Array dem angegebenen Wert entspricht. <br><br>Nehmen wir zum Beispiel an, Canvas A hat den Filter für die verschachtelten Eigenschaften des angepassten Events **gleich** "Smartwatch", und Canvas B hat den Filter für die verschachtelten Eigenschaften des angepassten Events **gleich** "simphone". Wenn Sie "smartwatch" und "simphone" in Ihren Eigenschaften haben, werden beide Canvase getriggert. Wenn Sie jedoch "simphone" oder "sim only" in einer Eigenschaft haben, wird keiner der beiden Canvas triggern.
{% endalert %}

{% endtab %}
{% tab Restaurant Example %}

Auslösen einer Kampagne mit verschachtelten Eigenschaften aus dem Ereignis "Bestellt":

![Ein Nutzer:in, der die Eigenschaft Filter r_details.name hinzufügt, ist McDonalds für ein angepasstes Event.]({% image_buster /assets/img/nested_object1.png %})

`r_details.name`: "Mcdonalds"<br>
`r_details.location.city`: "Montclair"
{% endtab %}
{% endtabs %}

{% alert note %}
Wenn Ihre Eigenschaft die Zeichen `[]` oder `.` enthält, müssen Sie diese in doppelte Anführungszeichen setzen. Zum Beispiel passt `"songs[].album".yearReleased` auf ein Ereignis mit der literalen Eigenschaft `"songs[].album"`.
{% endalert %}

### Segmentierung

Um Nutzer:innen auf der Grundlage verschachtelter Event-Eigenschaften zu segmentieren, müssen Sie [Segment-Erweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) verwenden. Nachdem Sie ein Schema erstellt haben, wird der Explorer für verschachtelte Objekte im Bereich Segmentierung angezeigt. 

![]({% image_buster /assets/img_archive/nested_event_properties_segmentation.png %})

Die Segmentierung verwendet die gleiche Notation wie die Triggerung (siehe [Triggerung von Nachrichten](#message-triggering)).

Um Segment-Erweiterungen zu bearbeiten oder zu erstellen, benötigen Sie die Berechtigung "Segmente bearbeiten".

### Personalisierung

Wählen Sie im Modal " **Personalisierung hinzufügen"** als Personalisierungstyp **"Erweiterte Event-Eigenschaften** " aus. Dies lässt die Möglichkeit zu, verschachtelte Event-Eigenschaften hinzuzufügen, nachdem ein Schema erstellt wurde.

![]({% image_buster /assets/img_archive/nested_event_properties_personalization.png %}){: style="max-width:70%;"}

## Häufig gestellte Fragen

### Werden bei verschachtelten Objekten zusätzliche Datenpunkte aufgezeichnet?

Die Art und Weise, wie wir Datenpunkte protokollieren, ändert sich durch das Hinzufügen dieser Funktion nicht. Bei der Segmentierung auf der Grundlage verschachtelter Objekte werden Segment-Erweiterungen verwendet, die keine zusätzlichen Datenpunkte benötigen.

### Wie viele verschachtelte Daten können gesendet werden?

Wenn eine oder mehrere der Eigenschaften des Ereignisses verschachtelte Daten enthalten, beträgt die maximale Nutzlast für alle kombinierten Eigenschaften eines Ereignisses 100 KB. Jede Anfrage, die diese Größenbeschränkung überschreitet, wird abgelehnt.

