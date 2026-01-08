---
nav_title: "Nutzer:in-Update"
article_title: Nutzeraktualisierung 
alias: "/user_update/"
page_order: 6
page_type: reference
description: "Dieser Referenzartikel behandelt die Komponente Nutzer:in Update und wie Sie sie in Ihren Canvase verwenden können."
tool: Canvas
---

# Nutzeraktualisierung 

> Mit der Komponente User Update können Sie die Attribute, Events und Käufe einer Nutzerin oder eines Nutzers in einem JSON-Composer aktualisieren, so dass Sie keine sensiblen Informationen wie API-Schlüssel eingeben müssen.

## Wie diese Komponente funktioniert

![Ein Nutzer:innen-Update-Schritt namens "Loyalität aktualisieren", der ein Attribut "Ist Premium-Mitglied" auf "wahr" aktualisiert.]({% image_buster /assets/img_archive/canvas_user_update_step.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

Wenn Sie diese Komponente in Ihrem Canvas verwenden, werden Updates nicht auf das Rate-Limit von `/users/track` für Anfragen pro Minute angerechnet. Stattdessen werden diese Updates gebündelt, damit Braze sie effizienter verarbeiten kann als ein Braze-to-Braze-Webhook. Beachten Sie, dass diese Komponente keine [Datenpunkte]({{site.baseurl}}/user_guide/data/data_points/) protokolliert, wenn sie zum Update nicht abrechenbarer Datenpunkte (wie Abo-Gruppen) verwendet wird.

Die Benutzer gelangen erst dann zu den nächsten Canvas-Schritten, wenn die entsprechenden Benutzeraktualisierungen abgeschlossen sind. Das bedeutet, dass alle nachfolgenden Messaging-Nachrichten, die sich auf diese Nutzer:innen-Updates stützen, auf dem neuesten Stand sind, wenn der nächste Schritt ausgeführt wird.

## Erstellen eines Nutzerupdates

Ziehen Sie die Komponente aus der Seitenleiste, oder klicken Sie auf die Plus-Schaltfläche <i class="fas fa-plus-circle"></i> am unteren Rand der Variante oder des Schritts und wählen Sie **Benutzeraktualisierung**. 

Es gibt drei Optionen, mit denen Sie bestehende Benutzerprofilinformationen aktualisieren, neue hinzufügen oder entfernen können. Insgesamt können die User Update-Schritte in einem Workspace bis zu 200.000 Nutzerprofile pro Minute aktualisieren.

{% alert tip %}
Sie können die mit dieser Komponente vorgenommenen Änderungen auch testen, indem Sie nach einem Nutzer:innen suchen und die Änderung auf ihn anwenden. Dadurch wird der Benutzer aktualisiert.
{% endalert %}

### Benutzerdefinierte Attribute aktualisieren

Um ein benutzerdefiniertes Attribut hinzuzufügen oder zu aktualisieren, wählen Sie einen Attributnamen aus Ihrer Attributliste und geben den Schlüsselwert ein.

![Nutzer:in Update-Schritt, der die beiden Attribute "Loyalitätsmitglied" und "Loyalitätsprogramm" auf "wahr" aktualisiert.]({% image_buster /assets/img_archive/canvas_user_update_update.png %}){: style="max-width:90%;"}

### Anpassen von Attributen entfernen

Um ein angepasstes Attribut zu entfernen, wählen Sie einen Attributnamen aus der Dropdown-Liste aus. Sie können zum [erweiterten JSON-Composer](#advanced-json-composer) wechseln, um ihn weiter zu bearbeiten. 

![Nutzer:in Update-Schritt, der ein Attribut "Loyalty Member" entfernt.]({% image_buster /assets/img_archive/canvas_user_update_remove.png %}){: style="max-width:90%;"}

### Steigende und fallende Werte

Der Schritt der Benutzeraktualisierung kann einen Attributwert erhöhen oder verringern. Markieren Sie das Attribut, wählen Sie **Erhöhen um** oder **Verringern um** und geben Sie eine Zahl ein. 

#### Wöchentliche Fortschritte verfolgen

Indem Sie ein angepasstes Attribut erhöhen, das ein Event verfolgt, können Sie die Anzahl der Kurse verfolgen, die ein:e Nutzer:in in einer Woche belegt hat. Mit dieser Komponente können Sie die Klassenanzahl zu Beginn der Woche zurücksetzen und das Tracking neu beginnen. 

![Nutzer:in Update-Schritt, der das Attribut "class_count" um eins erhöht.]({% image_buster /assets/img_archive/canvas_user_update_increment.png %}){: style="max-width:90%;"}

### Aktualisieren eines Arrays von Objekten

Ein [Array von Objekten]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects/) ist ein benutzerdefiniertes Attribut, das im Profil eines Benutzers gespeichert ist und viele Daten enthält. So können Sie eine Historie der Interaktionen des Benutzers mit Ihrer Marke erstellen. Damit können Sie Segmente erstellen, die auf einem angepassten Attribut basieren, das ein berechnetes Feld ist, wie z. B. der Kaufverlauf oder der Lifetime-Value.

Der Schritt Benutzeraktualisierung kann diesem Array von Objekten Attribute hinzufügen oder entfernen. Um ein Array zu aktualisieren, wählen Sie den Namen des Array-Attributs aus Ihrer Liste der Attribute aus und geben den Schlüsselwert ein.

#### Anwendungsfall: Aktualisieren der Wunschliste eines Benutzers

Das Hinzufügen oder Entfernen eines Artikels zu einem Array aktualisiert die Wunschliste des Benutzers.

![Nutzer:in Update-Schritt, der einen Artikel "sunblock" zum Attribut "items_in_wishlist".]({% image_buster /assets/img_archive/canvas_user_update_wishlist.png %}){: style="max-width:90%;"}

#### Anwendungsfälle: Berechnen der Gesamtsumme des Warenkorbs

Verfolgen Sie, wann ein Benutzer Artikel in seinem Einkaufswagen hat, wann er neue Artikel hinzufügt oder Artikel entfernt, und wie hoch der Gesamtwert des Warenkorbs ist. 

1. Erstellen Sie ein benutzerdefiniertes Array von Objekten namens `shopping_cart`. Das folgende Beispiel zeigt, wie dieses Attribut aussehen kann. Jeder Artikel hat eine eindeutige `product_id`, die komplexere Daten in ihrem eigenen verschachtelten Array von Objekten enthält, einschließlich `price`.

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
3\. Erstellen Sie mit diesem benutzerdefinierten Ereignis ein Canvas mit einer Zielgruppe von Benutzern. Wenn nun ein:e Nutzer:in einen Artikel in seinen Warenkorb legt, wird dieses Canvas getriggert. Sie können dann gezielt Nachrichten an diese Benutzer senden und ihnen Gutscheincodes anbieten, wenn sie einen bestimmten Betrag ausgegeben haben, ihren Einkaufswagen eine bestimmte Zeit lang nicht benutzt haben oder alles andere, was zu Ihrem Anwendungsfall passt. 

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
         "product_id": ["1001", "1002"]
         "gift": yes,
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

![Nutzer:innen Update Schritt, der das Attribut "most_recent_cart_item" mit einer Artikel ID aktualisiert.]({% image_buster /assets/img_archive/canvas_user_update_cep.png %}){: style="max-width:90%;"}

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

## Erweiterter JSON-Composer

Fügen Sie dem JSON-Composer ein Attribut, ein Event oder ein JSON-Kauf-Objekt mit bis zu 65.536 Zeichen hinzu. Der Status des [globalen Abonnements]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states) und der [Abonnementgruppe]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) eines Benutzers kann ebenfalls festgelegt werden.

![]({% image_buster /assets/img_archive/canvas_user_update_composer.png %}){: style="max-width:90%;"}

Mit dem erweiterten Composer können Sie auch eine Vorschau anzeigen und testen, ob das Nutzerprofil mit den Änderungen aktualisiert wird, indem Sie den Tab **Vorschau und Test** verwenden. Sie können entweder einen zufälligen Nutzer auswählen oder nach einem bestimmten Nutzer:innen suchen. Nachdem Sie einen Test an eine:n Nutzer:in gesendet haben, sehen Sie sich das Nutzerprofil über den generierten Link an.

![]({% image_buster /assets/img_archive/canvas_user_update_test_preview.png %}){: style="max-width:90%;"}

### Überlegungen

Sie müssen bei der Verwendung des JSON-Composers keine sensiblen Daten wie Ihren API-Schlüssel angeben, da dieser automatisch von der Plattform bereitgestellt wird. Daher werden die folgenden Felder nicht benötigt und sollten im JSON-Composer nicht verwendet werden:
* Externe Benutzer-ID
* API-Schlüssel
* Braze-Cluster-URL
* Felder für den Import von Push-Token

{% raw %}
### Benutzerdefinierte Ereignisse protokollieren

Mit dem JSON-Composer können Sie auch angepasste Events protokollieren. Beachten Sie, dass hierfür ein Zeitstempel im ISO-Format erforderlich ist. Sie müssen also eine Zeit und ein Datum mit Liquid am Anfang angeben. Betrachten Sie dieses Beispiel, in dem ein Event mit einer Uhrzeit protokolliert wird.

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

Innerhalb des JSON-Composers können Sie auch den Abo-Status der Nutzer:innen bearbeiten. Das folgende Beispiel zeigt, dass der Status des Abos einer Nutzerin oder eines Nutzers  auf `opted_in` aktualisiert wurde. 

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

Sie können mit diesem Canvas-Schritt auch Abonnementgruppen aktualisieren. Das folgende Beispiel zeigt eine Aktualisierung der Abonnementgruppen. Sie können eine oder mehrere Aktualisierungen von Abonnementgruppen durchführen.

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

