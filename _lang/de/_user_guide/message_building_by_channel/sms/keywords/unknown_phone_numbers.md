---
nav_title: Umgang mit unbekannten Telefonnummern
article_title: Unbekannte SMS-Telefonnummern behandeln
page_order: 4
description: "In diesem Referenzartikel erfahren Sie, wie Braze unbekannte SMS-Telefonnummern von neuen Nutzer:innen verarbeitet."
page_type: reference
channel:
  - SMS
  
---

# Umgang mit unbekannten Rufnummern - neue Benutzer

> Nachdem Sie SMS mit Braze zum Laufen gebracht haben, werden Sie möglicherweise Nachrichten von unbekannten Benutzern erhalten. Die folgenden Schritte beschreiben, wie ein:e nicht identifizierte:r Nutzer:in und eine Nummer verarbeitet werden.

{% alert important %}
Sind Sie derzeit ein nicht-einheimischer SMS-Kunde? Wenn dies der Fall ist, lesen Sie den entsprechenden Artikel zum Umgang mit unbekannten Telefonnummern in der [Dokumentation zu nicht-nativen SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/).
{% endalert %}

## Opt-in/out und benutzerdefinierter Schlüsselwort-Workflow für unbekannte Nummern

Braze adressiert eine unbekannte Nummer automatisch auf eine von drei Arten:

1. Wenn ein Opt-in-Schlüsselwort eingegeben wird:
  * Braze erstellt ein anonymes Profil
  * Unser System legt das Telefon-Attribut fest
  * Abonniert die:den Nutzer:in die entsprechende Abo-Gruppe, je nachdem, welches Opt-in-Schlüsselwort von Braze empfangen wurde.<br><br>
2. Wenn ein Opt-out-Schlüsselwort eingegeben wird:
  * Braze erstellt ein anonymes Profil
  * Unser System legt das Telefon-Attribut fest
  * Meldet die:den Nutzer:in der entsprechenden Abo-Gruppe ab, je nachdem, welches Opt-out-Schlüsselwort von Braze empfangen wurde.<br><br>
3. Wenn ein anderes benutzerdefiniertes Schlüsselwort eingegeben wird:
  * Braze ignoriert die Textnachricht und tut nichts.

[ualink]: {{site.baseurl}}/api/objects_filters/user_alias_object/
[telink]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[uaolink]: {{site.baseurl}}/api/objects_filters/user_attributes_object/
[e.164]: https://en.wikipedia.org/wiki/E.164