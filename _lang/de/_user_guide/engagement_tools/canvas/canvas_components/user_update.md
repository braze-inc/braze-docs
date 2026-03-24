---
nav_title: "Update für Nutzer:innen"
article_title: Nutzeraktualisierung 
alias: "/user_update/"
page_order: 12
page_type: reference
description: "Dieser Referenzartikel behandelt die Komponente Nutzer:in Update und wie Sie sie in Ihren Canvase verwenden können."
tool: Canvas
---

# Nutzeraktualisierung 

> Mit der Komponente „Benutzer-Update“ können Sie die Attribute, Ereignisse und Käufe eines Nutzers in einem JSON-Editor aktualisieren, sodass keine sensiblen Informationen wie API-Schlüssel angegeben werden müssen.

## Wie diese Komponente funktioniert

![Ein Benutzeraktualisierungsschritt namens „Loyalität aktualisieren”, der das Attribut „Ist Premium-Mitglied” auf „wahr” aktualisiert.]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Wenn Sie diese Komponente in Ihrem Canvas verwenden, werden Updates nicht auf das Rate-Limit von `/users/track` für Anfragen pro Minute angerechnet. Stattdessen werden diese Updates gebündelt, damit Braze sie effizienter verarbeiten kann als ein Braze-to-Braze-Webhook. Bitte beachten Sie, dass diese Komponente keine [Datenpunkte]({{site.baseurl}}/user_guide/data/data_points/) protokolliert, wenn sie zum Update nicht abrechnungsfähiger Datenpunkte (wie Abo-Gruppen) verwendet wird.

Nachdem die Nutzer:innen den Schritt „Benutzer-Update“ aufgerufen haben und die Verarbeitung abgeschlossen ist, werden sie zum nächsten Schritt vorangebracht. Dies bedeutet, dass alle nachfolgenden Nachrichten, die auf diesen Updates der Nutzer:innen basieren, zum Zeitpunkt der Ausführung des nächsten Schritts auf dem neuesten Stand sind.

## Erstellen eines Nutzerupdates

Ziehen Sie die Komponente aus der Seitenleiste per Drag-and-Drop oder wählen Sie den<i class="fas fa-plus-circle"></i>Plus-Button am unteren Rand der Variante oder des Schritts und wählen Sie **„Benutzer-Update**“. 

Es gibt drei zulässige Optionen, mit denen Sie vorhandene Informationen zum Nutzerprofil aktualisieren, neue Informationen hinzufügen oder Informationen zum Nutzerprofil entfernen können. Insgesamt können die User Update-Schritte in einem Workspace bis zu 200.000 Nutzerprofile pro Minute aktualisieren.

{% alert tip %}
Sie können die mit dieser Komponente vorgenommenen Änderungen auch testen, indem Sie nach einem Nutzer:innen suchen und die Änderung auf ihn anwenden. Dadurch wird der Benutzer aktualisiert.
{% endalert %}

## Benutzerdefinierte Attribute aktualisieren

Um ein angepasstes Attribut zu aktualisieren oder zu entfernen, wählen Sie bitte einen Attributnamen aus Ihrer Attributliste aus und geben Sie den Wert ein.

![Benutzeraktualisierungsschritt, der die beiden Attribute „Treueprogramm-Mitglied” und „Kundenbindungs-Programm” auf „wahr” aktualisiert.]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

## Anpassen von Attributen entfernen

Um ein angepasstes Attribut zu entfernen, wählen Sie einen Attributnamen aus der Dropdown-Liste aus. Sie können zum [erweiterten JSON-Editor](#advanced-json-editor) wechseln, um weitere Bearbeitungen vorzunehmen. 

![Schritt zum Update der Nutzer:innen, der das Attribut „Treue-Mitglied” entfernt.]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### Steigende und fallende Werte

Der Schritt „Benutzer-Update“ kann einen Wert des Attributs erhöhen oder verringern. Markieren Sie das Attribut, wählen Sie **Erhöhen um** oder **Verringern um** und geben Sie eine Zahl ein. 

#### Wöchentliche Fortschritte verfolgen

Indem Sie ein angepasstes Attribut erhöhen, das ein Event verfolgt, können Sie die Anzahl der Kurse verfolgen, die ein:e Nutzer:in in einer Woche belegt hat. Mit dieser Komponente können Sie die Klassenanzahl zu Beginn der Woche zurücksetzen und das Tracking neu beginnen. 

![Update-Schritt für Nutzer:innen, der das Attribut"class_count"um eins erhöht.]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### Aktualisieren eines Arrays von Objekten

Ein [Array von Objekten]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) ist ein datenreiches benutzerdefiniertes Attribut, das im Nutzerprofil eines Nutzers gespeichert ist. Sie können damit einen Verlauf der Interaktionen der Nutzer:innen mit Ihrer Marke erstellen und Segmente auf der Grundlage eines berechneten Feldes erstellen, wie beispielsweise Kaufhistorie oder Lifetime-Value.

Mit der Option **„Erweiterter JSON-Editor**“ können Sie JSON einfügen, um Artikel zu diesem Objekt-Array hinzuzufügen oder daraus zu entfernen.

#### Anwendungsfälle: Aktualisieren der Wunschliste eines Benutzers

Verfolgen Sie die Wunschliste einer Nutzer:in, um anhand der gespeicherten Artikel eine Segmentierung oder Personalisierung vorzunehmen.

1. Erstellen Sie ein angepasstes Attribut, das ein Array von Objekten ist, beispielsweise `wishlist`. Jedes Objekt kann Felder wie `product_id`, `product_name`, und enthalten`added_at`.
2. Wählen Sie im Schritt „Update für Nutzer:innen“ **die Option „Erweiterter JSON-Editor“** aus. Verwenden Sie anschließend im Abschnitt **„Compose“** den`$add`Operator, um einen Artikel anzuhängen, oder den`$remove`Operator, um einen Artikel anhand seines Werts zu entfernen.

Im Folgenden finden Sie ein Beispiel für das Hinzufügen eines Artikels zur Wunschliste:

{% raw %}
```json
{
  "attributes": [
    {
      "wishlist": {
        "$add": [
          {
            "product_id": "SKU-123",
            "product_name": "Wireless Headphones",
            "added_at": "{{$isoTimestamp}}"
          }
        ]
      }
    }
  ]
}
```
{% endraw %}

Um einen Artikel zu entfernen, verwenden`"wishlist": { "$remove": [ { "product_id": "SKU-123", ... } ] }`Sie bitte dieselbe Objektstruktur, damit Braze ihn zuordnen und entfernen kann.

#### Anwendungsfälle: Berechnen der Gesamtsumme des Warenkorbs

Verfolgen Sie, wann ein Benutzer Artikel in seinem Einkaufswagen hat, wann er neue Artikel hinzufügt oder Artikel entfernt, und wie hoch der Gesamtwert des Warenkorbs ist. 

1. Erstellen Sie ein angepasstes Array von Objekten mit dem Namen `shopping_cart`. Das folgende Beispiel zeigt, wie dieses Attribut aussehen kann. Jeder Artikel verfügt über eine eindeutige `product_id`Kennung, die zusätzliche Daten in einem eigenen verschachtelten Objekt-Array enthält, darunter `price`.

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": number,
         "shipping": number,
         "items_in_cart": number,
         "product_id": array,
         "gift": boolean,
         "discount_code": "enum",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

{:start="2"}
2\. Erstellen Sie ein [benutzerdefiniertes Ereignis]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) namens `add_item_to_cart`, das protokolliert wird, wenn ein Benutzer einen Artikel in den Warenkorb legt.
3\. Erstellen Sie eine Canvas, die sich an Nutzer:innen richtet, die dieses angepasste Event ausführen. Wenn nun ein:e Nutzer:in einen Artikel in seinen Warenkorb legt, wird dieses Canvas getriggert. Sie können dann gezielt Nachrichten an diese Benutzer senden und ihnen Gutscheincodes anbieten, wenn sie einen bestimmten Betrag ausgegeben haben, ihren Einkaufswagen eine bestimmte Zeit lang nicht benutzt haben oder alles andere, was zu Ihrem Anwendungsfall passt. 

Das Attribut `shopping_cart` enthält die Summe vieler benutzerdefinierter Ereignisse: die Gesamtkosten aller Artikel, die Gesamtzahl der Artikel im Einkaufswagen, ob der Einkaufswagen ein Geschenk enthält, und so weiter. Dies kann etwa wie folgt aussehen:

{% raw %}
```javascript
{
  "attributes": [
    {
      "shopping_cart": [
       {
         "total_cart_value": 22.99,
         "shipping": 4.99,
         "items_in_cart": 2,
         "product_id": ["1001", "1002"],
         "gift": true,
         "discount_code": "flashsale1000",
         "timestamp": {"$time" : "{{$isoTimestamp}}"},
       }
      ]
    }
  ]
}
```
{% endraw %}

## Eigenschaft des Canvas-Entrys als Attribut festlegen

Mit dem Schritt Nutzer:innen aktualisieren können Sie eine `canvas_entry_property` persistent machen. Angenommen, Sie haben ein Ereignis, das ausgelöst wird, wenn ein Artikel in den Warenkorb gelegt wird. Sie können die ID des zuletzt in den Warenkorb gelegten Artikels speichern und diese für eine Remarketing-Kampagne verwenden. Verwenden Sie die Personalisierungsfunktion, um eine Eigenschaft eines Canvas-Eintrags abzurufen und sie in einem Attribut zu speichern.

![Benutzeraktualisierungsschritt, der das Attribut"most_recent_cart_item"mit einer ID für einen Artikel aktualisiert.]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

### Personalisierung

Um die Eigenschaft des Trigger-Events für ein Canvas als Attribut zu speichern, verwenden Sie das Personalisierungsmodal, um die Eigenschaft des Canvas-Entrys zu extrahieren und zu speichern. Nutzer:innen Update unterstützt außerdem die folgenden Features zur Personalisierung:

* [Connected-Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) 
* [Content-Blöcke]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/)
* [Entry-Eigenschaften]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/)
* Liquid-Logik (einschließlich [Abbruch von Nachrichten]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/))
* Mehrere Attribut- oder Ereignisaktualisierungen pro Objekt

{% alert warning %}
Wir empfehlen eine vorsichtige Verwendung der Personalisierung von Connected-Content Liquid in Nutzerupdates, da für diesen Schritttyp ein Rate-Limit von 200.000 Anfragen pro Minute gilt. Dieses Ratenlimit hat Vorrang vor dem Canvas-Ratenlimit.
{% endalert %}

## Erweiterter JSON-Editor

Fügen Sie dem JSON-Editor ein Attribut, ein Ereignis oder ein Kauf-JSON-Objekt mit bis zu 65.536 Zeichen hinzu. Der Status des [globalen Abonnements]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) und der [Abonnementgruppe]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) eines Benutzers kann ebenfalls festgelegt werden.

![]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

Mit dem JSON-Editor können Sie auf dem Tab **„Vorschau und Test“** auch eine Vorschau anzeigen und überprüfen, ob das Nutzerprofil mit Ihren Änderungen aktualisiert wurde. Sie können entweder einen zufälligen Nutzer auswählen oder nach einem bestimmten Nutzer:innen suchen. Nachdem Sie einen Test an eine:n Nutzer:in gesendet haben, sehen Sie sich das Nutzerprofil über den generierten Link an.

![]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### Überlegungen

Bei der Verwendung des JSON-Editors müssen Sie keine sensiblen Daten wie Ihren API-Schlüssel angeben, da diese automatisch von der Plattform bereitgestellt werden. Die folgenden Felder sollten nicht in den JSON-Editor aufgenommen werden:
* Externe Benutzer-ID
* API-Schlüssel
* Braze-Cluster-URL
* Felder für den Import von Push-Token

{% alert important %}
Canvas-Eigenschaften (wie die Tags `canvas_id`,`canvas_name`  und`canvas_variant_name`  Liquid-Tags) werden in Benutzereinrichtungsschritten nicht unterstützt.
{% endalert %}

{% raw %}
### Benutzerdefinierte Ereignisse protokollieren

Mit dem JSON-Editor können Sie auch angepasste Events protokollieren. Bitte beachten Sie, dass hierfür ein Zeitstempel im ISO-Format erforderlich ist, sodass zu Beginn eine Zeit und ein Datum mit Liquid zugewiesen werden müssen. Betrachten Sie dieses Beispiel, in dem ein Event mit einer Uhrzeit protokolliert wird.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "name": "logged_user_event",
      "time": "{{timestamp}}"
    }
  ]
}
```

Dieses nächste Beispiel verknüpft ein Event mit einer bestimmten App, indem es ein angepasstes Event mit optionalen Eigenschaften und die `app_id` verwendet.

```
{% assign timestamp = 'now' | date: "%Y-%m-%dT%H:%M:%SZ" %}
{
  "events": [
    {
      "app_id": "insert_app_id",
      "name": "rented_movie",
      "time": "{{timestamp}}",
      "properties": {
        "release": {
          "studio": "FilmStudio",
          "year": "2022"
        },
        "cast": [
          {
            "name": "Actor1"
          },
          {
            "name": "Actor2"
          }
        ]
      }
    }
  ]
}
```

### Abonnementstatus bearbeiten

Im JSON-Editor können Sie auch den Status des Abos einer Nutzer:in bearbeiten. Das folgende Beispiel zeigt, dass der Status des Abos einer Nutzerin oder eines Nutzers  auf `opted_in` aktualisiert wurde. 

```
{
  "attributes": [
    {
      "email_subscribe": "opted_in"
    }
  ]
}
```

### Abonnementgruppen aktualisieren 

Sie können mit diesem Canvas-Schritt auch Abonnementgruppen aktualisieren. Das folgende Beispiel veranschaulicht, wie eine oder mehrere Abo-Gruppen aktualisiert werden können.

```
{
  "attributes": [
    {
      "subscription_groups": [
        {
          "subscription_group_id": "subscription_group_identifier_1",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_2",
          "subscription_state": "subscribed"
        },
        {
          "subscription_group_id": "subscription_group_identifier_3",
          "subscription_state": "subscribed"
        }
      ]
    }
  ]
}
```
{% endraw %}

