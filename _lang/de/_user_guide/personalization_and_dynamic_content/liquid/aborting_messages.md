---
nav_title: Nachrichten abbrechen
article_title: Abbrechen von Liquid Messages
page_order: 7
description: "Dieser Referenzartikel behandelt den Abbruch von Liquid-Nachrichten und einige Anwendungsbeispiele."

---

# Nachrichten abbrechen

> Optionally, you can use the `abort_message("optional reason for aborting")` Liquid message tag within conditionals to prevent sending a message to a user. In diesem Referenzartikel finden Sie einige Beispiele dafür, wie diese Funktion in Marketingkampagnen eingesetzt werden kann.

{% alert note %}
Wenn ein Nachrichtenschritt in einem Canvas abgebrochen wird, verlässt die:der Nutzer:in den Canvas **nicht** und **fährt** mit dem nächsten Schritt fort.
{% endalert %}

## Nachricht abbrechen, wenn "Anzahl der besuchten Spiele" = 0

Nehmen wir zum Beispiel an, Sie möchten keine Nachricht an Kunden senden, die nicht an einem Spiel teilgenommen haben:

{% raw %}
```liquid
{% if custom_attribute.${Number_Game_Attended} == 1 %}
Loved the game? Get 10% off your second one with code SAVE10.
{% elsif custom_attribute.${Number_Game Attended} > 1 %}
Love the games? Get 10% off your next one with code SAVE10.
{% else %}
{% abort_message() %}
{% endif %}
```
{% endraw %}

Diese Nachricht wird nur an Kunden gesendet, von denen bekannt ist, dass sie ein Spiel besucht haben.

## Nachricht nur an englischsprachige Kunden

Sie können nur englischsprachige Kunden benachrichtigen, indem Sie eine "if"-Anweisung erstellen, die passt, wenn die Sprache eines Kunden Englisch ist, und eine "else"-Anweisung, die die Nachricht für jeden abbricht, der kein Englisch spricht oder keine Sprache in seinem Profil hat.

{% raw %}
```liquid

{% if ${language} == 'en' %}
Send this message in English!
{% else %}
{% abort_message() %}
{% endif %}
```

Standardmäßig protokolliert Braze eine allgemeine Fehlermeldung in Ihrem Message Activity Log:

```text
{% abort_message %} called
```

Sie können die abgebrochene Nachricht auch in Ihrem Nachrichten-Aktivitätsprotokoll protokollieren lassen, indem Sie innerhalb der Klammern einen String einfügen:

```liquid
{% abort_message('language was nil') %}
```
{% endraw %}

![Nachrichten-Fehlerprotokoll in der Entwickler:in der Entwicklungskonsole mit der Abbruchnachricht "language was nil".]({% image_buster /assets/img_archive/developer_console.png %})

## Abfrage für abgebrochene Nachrichten

Sie können den [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) oder Ihr eigenes Data Warehouse, sofern es mit Braze verbunden ist, verwenden, um nach bestimmten Abbruchmeldungen zu suchen, die ausgelöst werden, wenn die Liquid-Logik den Abbruch einer Meldung verursacht.

## Considerations

The `abort_message()` Liquid message tag prevents messages from sending to users, meaning the message won't display on user profiles, and won't count toward deliveries or frequency capping.
