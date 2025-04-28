---
nav_title: Nachrichten abbrechen
article_title: Abbrechen von Liquid Messages
page_order: 7
description: "Dieser Referenzartikel behandelt den Abbruch von Liquid-Nachrichten und einige Anwendungsbeispiele."

---

# Nachrichten abbrechen

> Optional können Sie Liquid-Nachrichten innerhalb von Bedingungen abbrechen. In diesem Referenzartikel finden Sie einige Beispiele dafür, wie diese Funktion in Marketingkampagnen eingesetzt werden kann.

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

![Fehlerprotokoll in der Entwicklungskonsole mit der Abbruchmeldung "Sprache war null".][26]

## Abfrage für abgebrochene Nachrichten

Sie können den [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) oder Ihr eigenes Data Warehouse, sofern es mit Braze verbunden ist, verwenden, um nach bestimmten Abbruchmeldungen zu suchen, die ausgelöst werden, wenn die Liquid-Logik den Abbruch einer Meldung verursacht.

[15]: {% image_buster /assets/img_archive/liquid_abort.png %}
[26]: {% image_buster /assets/img_archive/developer_console.png %}
[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:\#accounting-for-null-attribute-values
