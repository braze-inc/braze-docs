---
nav_title: Verschachtelte angepasste Attribute
article_title: Verschachtelte angepasste Attribute
alias: "/nested_custom_attribute_support/"
page_order: 1
page_type: reference
description: "Dieser referenzierte Artikel behandelt die Verwendung verschachtelter angepasster Attribute als Datentyp für angepasste Attribute, einschließlich Einschränkungen und Anwendungsbeispielen."
---

# Verschachtelte angepasste Attribute

> Diese Seite behandelt verschachtelte angepasste Attribute, die es Ihnen ermöglichen, eine Reihe von Attributen als Eigenschaft eines anderen Attributs zu definieren. Mit anderen Worten: Wenn Sie ein angepasstes Attribut-Objekt definieren, können Sie eine Reihe von zusätzlichen Attributen für dieses Objekt festlegen.

{% multi_lang_include nested_attribute_objects/about_nested_attributes.md %}

{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## Beschränkungen

- Verschachtelte angepasste Attribute sind für angepasste Attribute gedacht, die über das Braze SDK oder die API gesendet werden. 
- Objekte haben eine maximale Größe von 100 KB.
- Schlüsselnamen und String-Werte dürfen maximal 255 Zeichen lang sein.
- Schlüsselnamen dürfen keine Leerzeichen enthalten.
- Punkte (`.`) und Dollarzeichen (`$`) sind keine unterstützten Zeichen in einer API-Nutzlast, wenn Sie versuchen, ein verschachteltes angepasstes Attribut an ein Nutzerprofil zu senden.
- Nicht alle Braze Partner unterstützen verschachtelte angepasste Attribute. Schauen Sie in der [Dokumentation des Partners]({{site.baseurl}}/partners/home) nach, ob bestimmte Partnerintegrationen dieses Feature unterstützen.
- Verschachtelte angepasste Attribute können nicht als Filter verwendet werden, wenn Sie eine Connected Audience API aufrufen.

## API Beispiel

{% tabs local %}
{% tab Create %}
Im Folgenden finden Sie ein Beispiel von `/users/track` mit einem Objekt "Meistgespielter Song". Um die Eigenschaften des Songs zu erfassen, senden wir eine API-Anfrage, die `most_played_song` als Objekt auflistet, zusammen mit einer Reihe von Objekteigenschaften.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab Update %}
Um ein bestehendes Objekt zu aktualisieren, senden Sie einen POST an `users/track` mit dem Parameter `_merge_objects` in der Anfrage. Dadurch wird Ihr Update mit den bestehenden Daten des Objekts zusammengeführt. Die tiefe Verschmelzung sorgt dafür, dass alle Ebenen eines Objekts in ein anderes Objekt verschmolzen werden und nicht nur die erste Ebene. In diesem Beispiel haben wir bereits ein `most_played_song` Objekt in Braze, und jetzt fügen wir ein neues Feld, `year_released`, zum `most_played_song` Objekt hinzu.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "most_played_song": {
          "year_released": 1960
      }
    }
  ]
}
```

Nachdem diese Anfrage eingegangen ist, sieht das angepasste Attribut-Objekt wie folgt aus:

```json
"most_played_song": {
  "song_name": "Solea",
  "artist_name" : "Miles Davis",
  "album_name": "Sketches of Spain",
  "year_released": 1960,
  "genre": "Jazz",
  "play_analytics": {
     "count": 1000,
     "top_10_listeners": true
  }
}
```

{% alert warning %}
Sie müssen `_merge_objects` auf `true` setzen, sonst werden Ihre Objekte überschrieben. `_merge_objects` ist standardmäßig `false`.
{% endalert %}

{% endtab %}
{% tab Delete %}
Um ein angepasstes Attribut-Objekt zu löschen, senden Sie einen POST an `users/track`, wobei das angepasste Attribut-Objekt auf `null` gesetzt ist.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": null
    }
  ]
}
```

{% alert note %}
Dieser Ansatz kann nicht verwendet werden, um einen verschachtelten Schlüssel innerhalb eines [Arrays von Objekten]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects) zu löschen.
{% endalert %}

{% endtab %}
{% endtabs %}

## SDK Beispiel

{% sdk_min_versions android:25.0.0 ios:6.1.0 web:4.7.0 %}

{% tabs local %}
{% tab Android SDK %}

**Erstellen**
```kotlin
val json = JSONObject()
    .put("song_name", "Solea")
    .put("artist_name", "Miles Davis")
    .put("album_name", "Sketches of Spain")
    .put("genre", "Jazz")
    .put(
        "play_analytics",
        JSONObject()
            .put("count", 1000)
            .put("top_10_listeners", true)
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json)
}
```

**Aktualisieren**
```kotlin
val json = JSONObject()
    .put("year_released", 1960)

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json, true)
}
```

**Löschen**
```kotlin
braze.getCurrentUser { user ->
    user.unsetCustomUserAttribute("most_played_song")
}
```

{% endtab %}
{% tab Swift SDK %}

**Erstellen**
```swift
let json: [String: Any?] = [
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": [
    "count": 1000,
    "top_10_listeners": true,
  ],
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json)
```

**Aktualisieren**
```swift
let json: [String: Any?] = [
  "year_released": 1960
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json, merge: true)
```

**Löschen**
```swift
braze.user.unsetCustomAttribute(key: "most_played_song")
```

{% endtab %}
{% tab Web SDK %}

**Erstellen**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": {
    "count": 1000,
    "top_10_listeners": true
  }
};
braze.getUser().setCustomUserAttribute("most_played_song", json);
```

**Aktualisieren**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "year_released": 1960
};
braze.getUser().setCustomUserAttribute("most_played_song", json, true);

```

**Löschen**
```javascript
import * as braze from "@braze/web-sdk";
braze.getUser().setCustomUserAttribute("most_played_song", null);
```

{% endtab %}
{% endtabs %}

## Erfassen von Daten als Objekteigenschaften

Um Datumsangaben als Objekteigenschaften zu erfassen, müssen Sie den Schlüssel `$time` verwenden. Im folgenden Beispiel wird ein Objekt "Wichtige Daten" verwendet, um die Eigenschaften des Objekts zu erfassen, `birthday` und `wedding_anniversary`. Der Wert für diese Daten ist ein Objekt mit dem Schlüssel `$time`, der kein Nullwert sein darf.

{% alert note %}
Wenn Sie anfangs keine Daten als Objekteigenschaften erfasst haben, empfehlen wir, diese Daten unter Verwendung des Schlüssels `$time` für alle Nutzer:innen erneut zu senden. Andernfalls kann dies bei Verwendung des Attributs `$time` zu unvollständigen Segmenten führen. Wenn jedoch der Wert für `$time` in einem verschachtelten angepassten Attribut nicht korrekt formatiert ist, wird das gesamte verschachtelte angepasste Attribut nicht aktualisiert.
{% endalert %}

```json
{
  "attributes": [ 
    {
      "external_id": "time_with_nca_test",
      "important_dates": {
        "birthday": {"$time" : "1980-01-01"},
        "wedding_anniversary": {"$time" : "2020-05-28"}
      }
    }
  ]
}
```

{% alert note %}
Wenn bei verschachtelten angepassten Attributen das Jahr kleiner als 0 oder größer als 3000 ist, speichert Braze diese Werte nicht für den Nutzer:in.
{% endalert %}

## Liquid-Templates

Das folgende Liquid Template-Beispiel zeigt, wie Sie die angepassten Attribut-Objekteigenschaften referenzieren, die aus der vorangegangenen API-Anfrage gespeichert wurden, und sie in Ihren Nachrichten verwenden.

Verwenden Sie den Tag für die Personalisierung `custom_attribute` und die Punktnotation, um auf Eigenschaften eines Objekts zuzugreifen. Geben Sie den Namen des Objekts an (und die Position im Array, wenn Sie auf ein Array von Objekten verweisen), gefolgt von einem Punkt, gefolgt vom Namen der Eigenschaft.

{% raw %}
`{{custom_attribute.${most_played_song}[0].artist_name}}` - "Miles Davis"
<br> `{{custom_attribute.${most_played_song}[0].song_name}}` - "Solea"
<br> `{{custom_attribute.${most_played_song}[0].play_analytics.count}}` - "1000"
{% endraw %}

![Mit Liquid können Sie ein Template für den Namen eines Liedes und die Anzahl, wie oft ein Hörer dieses Lied gespielt hat, in eine Nachricht einfügen]({% image_buster /assets/img_archive/nca_liquid_2.png %})

## Segmentierung

Sie können Segmente auf der Grundlage von verschachtelten angepassten Attributen erstellen, um Ihre Nutzer:innen weiter zu targetieren. Dazu filtern Sie Ihr Segment auf der Grundlage des angepassten Attributsobjekts und geben dann den Pfad zu dem Namen Ihrer Eigenschaft und dem zugehörigen Wert an, nach dem Sie segmentieren möchten. Wenn Sie sich nicht sicher sind, wie dieser Pfad aussieht, können Sie [ein Schema erstellen](#generate-schema) und den verschachtelten Objekt-Explorer verwenden, damit Braze diesen Pfad für Sie ausfüllt.

Nachdem Sie einen Pfad zu Ihrer Eigenschaft hinzugefügt haben, wählen Sie **Validieren**, um zu überprüfen, ob der Wert im Feld Pfad gültig ist.

Filter basierend auf einem angepassten Attribut für den meistgespielten Titel, wenn ein Hörer einen Titel mehr als eine bestimmte Anzahl von Malen gespielt hat]({% image_buster /assets/img_archive/nca_segmentation_2.png %})

Um mit verschachtelten angepassten Attributen zu segmentieren, wählen Sie den Filter **Verschachtelte angepasste Attribute**, um ein Dropdown-Menü anzuzeigen, aus dem Sie ein bestimmtes verschachteltes angepasstes Attribut auswählen können.

![]({% image_buster /assets/img_archive/nested_custom_attributes.png %}){: style="max-width:70%;"}

Bei der Segmentierung mit verschachtelten angepassten Attributen haben Sie Zugriff auf einen neuen Vergleicher, der nach Datentyp gruppiert ist. Da `play_analytics.count` zum Beispiel eine Zahl ist, können Sie einen Komparator unter der Kategorie **Zahl** auswählen.

![Ein Nutzer:innen wählt einen Operator auf der Grundlage des Datentyps für das verschachtelte angepasste Attribut]({% image_buster /assets/img_archive/nca_comparator.png %})

### Filter für Zeitdatenarten

Wenn Sie ein verschachteltes angepasstes Attribut filtern, können Sie beim Vergleich des Datumswertes mit Operatoren unter den Kategorien **Tag des Jahres** oder **Zeit** filtern. 

Wenn Sie einen Operator unter der Kategorie **Tag des Jahres** auswählen, werden nur der Monat und der Tag zum Vergleich herangezogen und nicht der vollständige Zeitstempel des verschachtelten Wertes des angepassten Attributs. Wenn Sie einen Operator unter der Kategorie **Zeit** auswählen, wird der vollständige Zeitstempel einschließlich des Jahres verglichen.

### Multikriterielle Segmentierung

Verwenden Sie die **Segmentierung nach mehreren Kriterien**, um ein Segment zu erstellen, das mehreren Kriterien innerhalb eines einzigen Objekts entspricht. Dadurch wird der Nutzer:innen in das Segment aufgenommen, wenn er mindestens ein Objekt-Array besitzt, das alle angegebenen Kriterien erfüllt. Zum Beispiel passen Nutzer:innen nur dann in dieses Segment, wenn ihr Schlüssel nicht leer ist und wenn ihre Nummer größer als 0 ist.

Sie können auch das Feature **Liquid für Segmente kopieren** verwenden, um einen Liquid Code für dieses Segment zu erzeugen und diesen in einer Nachricht zu verwenden. Nehmen wir zum Beispiel an, Sie haben ein Array von Kontoobjekten und ein Segment, das auf Kund:innen mit aktiven steuerpflichtigen Konten abzielt. Wenn Sie Ihre Kund:in dazu bringen möchten, einen Beitrag zu einem ihrer aktiven und steuerpflichtigen Konten zu leisten, müssen Sie eine Nachricht erstellen, um sie anzustacheln. 

![Ein Beispielsegment mit ausgewähltem Kontrollkästchen für die Multikriterien-Segmentierung.]({% image_buster /assets/img_archive/nca_multi_criteria.png %})

Wenn Sie **Liquid für Segmente** auswählen, generiert Braze automatisch Liquid-Code, der ein Objekt-Array zurückgibt, das nur aktive und steuerpflichtige Konten enthält.

{% raw %}

```
{% assign segmented_nested_objects = '' | split: '' %}
{% assign obj_array = {{custom_attribute.${accounts}}} %}
{% for obj in obj_array %}
  {% if obj["account_type"] == 'taxable' and obj["active"] == true %}
    {% assign segmented_nested_objects = obj_array | slice: forloop.index0 | concat: segmented_nested_objects | reverse %}
  {% endif %}
{% endfor %}
```

Von hier aus können Sie `segmented_nested_objects` nutzen und Ihre Nachricht personalisieren. In diesem Beispiel wollen wir ein Ziel aus dem ersten aktiven Steuerkonto nehmen und es personalisieren:

```
Get to your {{segmented_nested_objects[0].goal}} goal faster, make a deposit using our new fast deposit feature!
```

{% endraw %}

Dies gibt die folgende Nachricht an Ihre Kund:in zurück: "Erreichen Sie Ihr Rentenziel schneller, indem Sie eine Einzahlung mit unserem neuen Feature für schnelle Einzahlungen vornehmen!"

### Erzeugen Sie ein Schema mit Hilfe des verschachtelten Objekt-Explorers {#generate-schema}

Sie können ein Schema für Ihre Objekte erstellen, um Segmente zu filtern, ohne sich verschachtelte Objektpfade merken zu müssen. Führen Sie dazu die folgenden Schritte aus.

#### Schritt 1: Ein Schema generieren

Nehmen wir für dieses Beispiel an, dass wir ein Objekt-Array `accounts` haben, das wir gerade an Braze gesendet haben:

```json
"accounts": [
  {"type": "taxable",
  "balance": 22500,
  "active": true},
  {"type": "non-taxable",
  "balance": 0,
  "active": true},
 ]
```

Gehen Sie im Braze-Dashboard zu **Dateneinstellungen** > Angepasste Attribute.

Suchen Sie nach Ihrem Objekt oder Objekt-Array. Wählen Sie in der Spalte **Attributname** die Option **Schema generieren** aus.

![]({% image_buster /assets/img_archive/nca_generate_schema.png %})

{% alert tip %}
Je nachdem, wie viele Daten Sie uns geschickt haben, kann es ein paar Minuten dauern, bis Ihr Schema erstellt ist.
{% endalert %}

Nachdem das Schema generiert wurde, erscheint anstelle des Buttons **Schema generieren** ein neuer Button <i class="fas fa-plus"></i> plus. Sie können darauf klicken, um zu sehen, was Braze über dieses verschachtelte angepasste Attribut weiß. 

Während der Schemaerstellung betrachtet Braze die zuvor gesendeten Daten und erstellt eine ideale Darstellung Ihrer Daten für dieses Attribut. Braze analysiert auch einen Datentyp für Ihre verschachtelten Werte und fügt ihn hinzu. Dazu werden die früheren Daten, die für das jeweilige verschachtelte Attribut an Braze gesendet wurden, abgerufen.

Für unser Objekt-Array `accounts` können Sie sehen, dass es innerhalb des Objekt-Arrays ein Objekt gibt, das Folgendes enthält:

- Ein boolescher Typ mit einem Schlüssel von `active` (unabhängig davon, ob das Konto aktiv ist oder nicht)
- Ein Zahlentyp mit dem Schlüssel `balance` (Saldobetrag auf dem Konto)
- Ein String-Typ mit einem Schlüssel von `type` (nicht steuerpflichtiges oder steuerpflichtiges Konto)

![]({% image_buster /assets/img_archive/nca_schema.png %}){: style="max-width:50%" }

Nachdem wir nun die Daten analysiert und eine Darstellung erstellt haben, können wir ein Segment erstellen.

#### Schritt 2: Segmente erstellen

Lassen Sie uns Kunden:in ansprechen, die einen Kontostand von weniger als 100 haben, damit wir ihnen eine Nachricht schicken können, die sie zu einer Einzahlung auffordert.

Erstellen Sie ein Segment und fügen Sie den Filter `Nested Custom Attribute` hinzu. Suchen Sie dann nach Ihrem Objekt oder Objekt-Array und wählen Sie es aus. Hier haben wir das Objekt-Array `accounts` hinzugefügt. 

![]({% image_buster /assets/img_archive/nca_segment_schema.png %})

Wählen Sie den <i class="fas fa-plus"></i> plus Button im Pfadfeld aus. Daraufhin wird eine Darstellung Ihres Objekts oder Objekt-Arrays angezeigt. Sie können jeden der aufgelisteten Artikel auswählen und Braze fügt sie für Sie in das Pfadfeld ein. In diesem Beispiel müssen wir den Saldo ermitteln. Wählen Sie die Waage aus und der Pfad (in diesem Fall `[].balance`) wird automatisch in das Pfadfeld eingefügt.

![]({% image_buster /assets/img_archive/nca_segment_schema2.png %}){: style="max-width:70%" }

Sie können **Validieren** auswählen, um zu überprüfen, ob der Inhalt des Pfadfelds gültig ist, und dann den Rest des Filters nach Bedarf erstellen. Hier haben wir festgelegt, dass der Saldo weniger als 100 betragen soll.

![]({% image_buster /assets/img_archive/nca_segment_schema_3.png %})

Das war's! Sie haben soeben ein Segment mit einem verschachtelten angepassten Attribut erstellt, ohne dass Sie wissen müssen, wie die Daten strukturiert sind. Der verschachtelte Objekt-Explorer in Braze generierte eine visuelle Darstellung Ihrer Daten und ließ Sie genau das auswählen, was Sie für die Erstellung eines Segments benötigten.

### Triggern von Änderungen an angepassten Attributen

Sie können triggern, wenn sich ein verschachteltes Objekt mit angepassten Attributen ändert. Diese Option ist für Änderungen an Objekt-Arrays nicht verfügbar. Wenn Sie keine Option zum Anzeigen des Pfad-Explorers sehen, überprüfen Sie, ob Sie ein Schema erstellt haben. 

![]({% image_buster /assets/img_archive/nca_triggered_changes2.png %})

In der folgenden aktionsbasierten Kampagne können Sie beispielsweise eine neue Aktion für **Angepasste Attribute ändern** hinzufügen, um Nutzer:innen zu triggern, die ihre Präferenzen für die Vertretung in der Nachbarschaft geändert haben. 

![]({% image_buster /assets/img_archive/nca_triggered_changes.png %})

### Personalisierung

Mit dem Modal **Personalisierung hinzufügen** können Sie auch verschachtelte angepasste Attribute in Ihre Nachrichten einfügen. Wählen Sie als Personalisierungstyp **verschachtelte angepasste Attribute** aus. Als nächstes wählen Sie das Top-Level-Attribut und den Schlüssel des Attributs aus. 

In dem untenstehenden Modal zur Personalisierung wird beispielsweise das angepasste Attribut einer lokalen Vertretung in der Nachbarschaft auf der Grundlage der Präferenzen eines Nutzers eingefügt.

![]({% image_buster /assets/img_archive/nca_personalization.png %}){: style="max-width:70%" }

{% alert tip %}
Prüfen Sie, ob ein Schema generiert wurde, wenn Sie die Option zum Einfügen verschachtelter angepasster Attribute nicht sehen.
{% endalert %}

### Schemata neu generieren {#regenerate-schema}

Nachdem ein Schema erstellt wurde, kann es einmal alle 24 Stunden neu generiert werden. Dieser Abschnitt beschreibt, wie Sie Ihr Schema neu generieren können. Ausführlichere Informationen zu Schemas finden Sie im Abschnitt über die [Erstellung eines Schemas](#generate-schema) in diesem Artikel.

So regenerieren Sie das Schema für Ihr verschachteltes angepasstes Attribut:

1. Gehen Sie zu **Dateneinstellungen** > Angepasste Attribute.
2. Suchen Sie nach Ihrem verschachtelten angepassten Attribut.
3. Wählen Sie in der Spalte **Attributname** für Ihr Attribut <i class="fas fa-plus"></i> aus, um das Schema zu verwalten.
4. Es wird ein Modal angezeigt. Wählen Sie **Schema neu generieren**.

Die Option zum Regenerieren des Schemas wird deaktiviert, wenn seit der letzten Regenerierung des Schemas weniger als 24 Stunden vergangen sind. Bei einer Neugenerierung des Schemas werden nur neue Objekte erkannt und keine Objekte gelöscht, die bereits im Schema vorhanden sind.

{% alert important %}
Um das Schema für ein Objekt-Array mit einem bestehenden Objekt zurückzusetzen, müssen Sie ein neues angepasstes Attribut erstellen. Die Schema-Neugenerierung löscht keine bestehenden Objekte.
{% endalert %}

Wenn die Daten nach der Neugenerierung des Schemas nicht wie erwartet angezeigt werden, wird das Attribut möglicherweise nicht oft genug aufgenommen. Nutzerdaten werden anhand früherer Daten, die für das angegebene verschachtelte Attribut an Braze gesendet wurden, abgefragt. Wenn das Attribut nicht ausreichend erfasst wird, wird es nicht in das Schema aufgenommen.

## Datenpunkte

Jeder Schlüssel, der gesendet wird, verbraucht einen Datenpunkt. Zum Beispiel zählt dieses Objekt, das im Nutzerprofil initialisiert wurde, sieben (7) Datenpunkte:

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "year_released": 1960,
        "genre": "Jazz",
        "play_analytics": {
          "count": 1000,
          "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% alert note %}
Das Update eines angepassten Attributs auf `null` verbraucht ebenfalls einen Datenpunkt.
{% endalert %}

