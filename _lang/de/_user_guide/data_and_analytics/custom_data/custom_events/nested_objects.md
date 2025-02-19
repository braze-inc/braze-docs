---
nav_title: Verschachtelte Objekte
article_title: Verschachtelte Objekte in benutzerdefinierten Ereignissen
page_order: 1
page_type: reference
description: "Dieser Artikel beschreibt, wie Sie verschachtelte JSON-Daten als Eigenschaften von benutzerdefinierten Ereignissen und Käufen senden und wie Sie diese verschachtelten Objekte in Ihren Nachrichten verwenden können."
---

# Verschachtelte Objekte in benutzerdefinierten Ereignissen

> Dieser Artikel beschreibt, wie Sie verschachtelte JSON-Daten als Eigenschaften von benutzerdefinierten Ereignissen und Käufen senden und wie Sie diese verschachtelten Objekte in Ihren Nachrichten verwenden können.

Sie können verschachtelte Objekte - Objekte, die sich innerhalb eines anderen Objekts befinden - verwenden, um verschachtelte JSON-Daten als Eigenschaften von benutzerdefinierten Ereignissen und Käufen zu senden. Diese verschachtelten Daten können zur Erstellung von Vorlagen für personalisierte Informationen in Nachrichten, zum Auslösen von Nachrichtensendungen und zur Segmentierung verwendet werden.

## Beschränkungen

- Verschachtelte Daten werden sowohl für [angepasste Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) als auch für [Kauf-Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/) unterstützt, jedoch nicht für andere Event-Typen.
- Objekte mit Event-Eigenschaften, die Array- oder Objektwerte enthalten, können eine Nutzlast für Event-Eigenschaften von bis zu 100 KB haben.
- Schemata für Event-Eigenschaften können nicht für Kauf-Events erstellt werden.
- Die Schemata für Event-Eigenschaften werden durch Stichproben angepasster Events aus den letzten 24 Stunden generiert.

### Minimale SDK-Versionen

Die folgenden SDK-Versionen unterstützen verschachtelte Objekte:

{% sdk_min_versions swift:5.0.0 android:1.0.0 web:3.3.0 %}

## Schritt 1: Ein Schema generieren

Um auf die verschachtelten Daten in Ihrem angepassten Event zuzugreifen, erstellen Sie ein Schema für jedes Event mit verschachtelten Event-Eigenschaften. Um ein Schema zu erstellen, gehen Sie folgendermaßen vor:

1. Gehen Sie zu **Dateneinstellungen** > **Benutzerdefinierte Ereignisse**.
2. Wählen Sie **Eigenschaften verwalten** für die Ereignisse mit verschachtelten Eigenschaften.
3. Wählen Sie den Button <i class="fas fa-arrows-rotate"></i> aus, um das Schema zu erstellen. Um das Schema anzuzeigen, wählen Sie den Plus-Button <i class="fas fa-plus"></i> aus.

![][6]{: style="max-width:80%;"}

## Schritt 2: Verwenden Sie das verschachtelte Objekt

Nachdem Sie ein Schema erstellt haben, können Sie bei der Segmentierung und Personalisierung auf die verschachtelten Daten verweisen. Beispiele für die Verwendung finden Sie in den folgenden Abschnitten:

- [API-Anfragetext](#api-request-body)
- [Liquid-Templates](#liquid-templating)
- [Triggern von Nachrichten](#message-triggering)
- [Segmentierung](#segmentation)
- [Personalisierung](#personalization)

### Körper der API-Anfrage

{% tabs %}
{% tab Musik Beispiel %}

Im Folgenden finden Sie ein `/users/track`-Beispiel mit einem angepassten Event „Erstellte Playliste“. Nachdem eine Wiedergabeliste erstellt wurde, senden wir zur Erfassung der Eigenschaften der Wiedergabeliste eine API-Anfrage, die "Songs" als Eigenschaft und ein Array mit den verschachtelten Eigenschaften der Songs enthält.

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
{% tab Restaurant Beispiel%}

Im Folgenden finden Sie ein `/users/track`-Beispiel mit einem angepassten Event „Bestellt“. Nachdem eine Bestellung abgeschlossen wurde, senden wir zur Erfassung der Eigenschaften dieser Bestellung eine API-Anfrage, die "r_details" als Eigenschaft und die verschachtelten Eigenschaften dieser Bestellung auflistet.

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

### Liquid-Templates

Die folgenden Beispiele für Liquid Templating zeigen, wie Sie auf die verschachtelten Eigenschaften verweisen, die in der vorangegangenen API-Anfrage gespeichert wurden, und wie Sie diese in Ihren Liquid-Nachrichten verwenden. Verwenden Sie Liquid und die Punktnotation, um die verschachtelten Daten zu durchsuchen und den spezifischen Knoten zu finden, den Sie in Ihre Nachrichten aufnehmen möchten.

{% tabs %}
{% tab Musik Beispiel %}
Templates in Liquid in einer Nachricht, die durch das Event „Erstellte Playliste“ ausgelöst wird:

{% raw %}
`{{event_properties.${songs}[0].album.name}}`: „Vergessen Sie es“<br>
`{{event_properties.${songs}[1].title}}`: "Während meine Gitarre sanft weint"
{% endraw %}

{% endtab %}
{% tab Restaurant Beispiel %}
Templates in Liquid in einer Nachricht, die durch das Event „Bestellt“ ausgelöst wird:

{% raw %}
`{{event_properties.${r_details}.location.city}}`: "Montclair"
{% endraw %}

{% endtab %}
{% endtabs %}

### Triggern von Nachrichten

Um diese Eigenschaften zum Auslösen einer Kampagne zu verwenden, wählen Sie Ihr benutzerdefiniertes Ereignis oder Ihren Kauf und fügen einen Filter für **verschachtelte Eigenschaften** hinzu. Beachten Sie, dass das Auslösen von Nachrichten für In-App-Nachrichten noch nicht unterstützt wird, aber verschachtelte Eigenschaften in der Liquid-Personalisierung in den Nachrichten werden trotzdem angezeigt.

{% tabs %}
{% tab Musik Beispiel %}

Auslösen einer Kampagne mit verschachtelten Eigenschaften durch das Ereignis "Erstellte Wiedergabeliste":

![Ein Nutzer:innen, der eine verschachtelte Eigenschaft für die Filterung von Eigenschaften eines angepassten Events auswählt.]({% image_buster /assets/img/nested_object2.png %})

Die triggernde Bedingung `songs[].album.yearReleased` „ist“ „1968“ passt auf ein Event, bei dem einer der Titel ein Album hat, das 1968 veröffentlicht wurde. Wir verwenden die Klammerschreibweise `[]` für das Durchlaufen von Arrays und stimmen überein, wenn **ein** Element in dem durchlaufenen Array mit der Ereigniseigenschaft übereinstimmt.

{% alert important %}
Der Filter **ist nicht gleich** passt nur, wenn keine der Eigenschaften in Ihrem Array dem angegebenen Wert entspricht. <br><br>Nehmen wir zum Beispiel an, Canvas A hat den Filter für die verschachtelten Eigenschaften des angepassten Events **ist gleich** „Smartwatch“, und Canvas B hat den Filter für die verschachtelten Eigenschaften des angepassten Events **gleich** „simphone“. Wenn Sie „smartwatch“ und „simphone“ in Ihren Eigenschaften haben, werden beide Canvase ausgelöst. Wenn Sie jedoch „simphone“ oder „sim only“ in irgendeiner Eigenschaft haben, wird keiner der Canvas ausgelöst.
{% endalert %}

{% endtab %}
{% tab Restaurant Beispiel %}

Auslösen einer Kampagne mit verschachtelten Eigenschaften aus dem Ereignis "Bestellt":

![Ein:e Nutzer:in, der den Eigenschaftsfilter r_details.name hinzufügt, ist McDonalds für eine nutzerdefinierte Veranstaltung.]({% image_buster /assets/img/nested_object1.png %})

`r_details.name`: "Mcdonalds"<br>
`r_details.location.city`: "Montclair"
{% endtab %}
{% endtabs %}

{% alert note %}
Wenn Ihre Eigenschaft die Zeichen `[]` oder `.` enthält, müssen Sie diese in doppelte Anführungszeichen setzen. Zum Beispiel passt `"songs[].album".yearReleased` auf ein Event mit der literalen Eigenschaft `"songs[].album"`.
{% endalert %}

### Segmentierung

Um Nutzer:innen auf der Grundlage verschachtelter Event-Eigenschaften zu segmentieren, müssen Sie [Segment-Erweiterungen]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/) verwenden. Nachdem Sie ein Schema erstellt haben, wird der Explorer für verschachtelte Objekte im Bereich Segmentierung angezeigt. 

![][4]

Die Segmentierung verwendet die gleiche Notation wie die Triggerung (siehe [Triggerung von Nachrichten](#message-triggering)).

### Personalisierung

Wählen Sie im Modal **Personalisierung hinzufügen** als Personalisierungstyp **Erweiterte Event-Eigenschaften** aus. Dies lässt die Möglichkeit zu, verschachtelte Event-Eigenschaften hinzuzufügen, nachdem ein Schema erstellt wurde.

![][5]{: style="max-width:70%;"}

## Häufig gestellte Fragen

### Werden durch die Verwendung verschachtelter Objekte zusätzliche Datenpunkte verbraucht?

Die Art und Weise, wie wir Datenpunkte abrechnen, ändert sich durch die Hinzufügung dieser Funktion nicht. Bei der Segmentierung auf der Grundlage verschachtelter Objekte werden Segmenterweiterungen verwendet, die keine zusätzliche Verwendung von Datenpunkten mit sich bringen.

### Wie viele verschachtelte Daten können gesendet werden?

Wenn eine oder mehrere der Eigenschaften des Ereignisses verschachtelte Daten enthalten, beträgt die maximale Nutzlast für alle kombinierten Eigenschaften eines Ereignisses 100 KB. Jede Anfrage, die diese Größenbeschränkung überschreitet, wird abgelehnt.

[4]: {% image_buster /assets/img_archive/nested_event_properties_segmentation.png %}
[5]: {% image_buster /assets/img_archive/nested_event_properties_personalization.png %}
[6]: {% image_buster /assets/img_archive/schema_generation_example.png %}