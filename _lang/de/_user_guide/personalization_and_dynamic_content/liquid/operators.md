---
nav_title: Operatoren
article_title: Liquid-Operatoren
page_order: 2
description: "Auf dieser Referenzseite finden Sie die von Liquid unterstützten Operatoren sowie entsprechende Beispiele."

---

# Operatoren

> Liquid unterstützt viele [Operatoren][25] für bedingte Anweisungen. Auf dieser Seite finden Sie die von Liquid unterstützten Operatoren und Anwendungsbeispiele, wie Sie sie in Ihren Nachrichten verwenden können.

Diese Tabelle enthält die unterstützten Operatoren. Beachten Sie, dass Klammern in Liquid ungültig sind und verhindern, dass Tags funktionieren.

|   Syntax| Beschreibung|
|---------|-----------|
| ==  | ist gleich        |
| !=  | ist nicht gleich|
|  >  | größer als  |
| <   | weniger als     |
| >=| größer als oder gleich|
| <= | kleiner als oder gleich |
| oder | Bedingung A oder Bedingung B|
| und | Bedingung A und Bedingung B|
| enthält | prüft, ob ein String oder ein String-Array einen String enthält|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Hier einige Anwendungsbeipiele für diese Operatoren in Kampagnen:

### Nachricht mit einem ganzzahligen benutzerdefinierten Attribut auswählen

{% raw %}
```liquid
{% if {{custom_attribute.${total_spend}}} >0 %}
Thanks for purchasing! Here's another 10% off!
{% else %}
Buy now! Would 5% off convince you?
{% endif %}
```
{% endraw %}

![][13]{: width="100%"}

Wenn in diesem Beispiel das angepasste Attribut "Gesamtausgaben" eines Kunden größer als `0` ist, erhält er folgende Nachricht:

```
Thanks for purchasing! Here's another 10% off!
```
Wenn das benutzerdefinierte Attribut "Gesamtausgaben" eines Kunden nicht existiert oder gleich `0` ist, erhalten Sie die folgende Meldung:

```
Buy now! Would 5% off convince you?
```

### Nachricht mit einem benutzerdefinierten String-Attribut auswählen

{% raw %}

```liquid
{% if {{custom_attribute.${Game}}} == 'Game1' %}
You played our Game! We're so happy!
{% elsif{{custom_attribute.${Game}}} == 'Game2' %}
You played our other Game! Woop!{% else %}
Hey! Get in here and play this Game!
{% endif %}
```
{% endraw %}

![][14]

In diesem Beispiel erhalten Sie folgende Nachricht, wenn Sie ein bestimmtes Spiel gespielt haben:

```
You played our Game! We're so happy!
```

Wenn Sie ein anderes angegebenes Spiel gespielt haben:

```
You played our other Game! Woop!
```

Wenn Sie noch keine Spiele gespielt haben oder das benutzerdefinierte Attribut in Ihrem Profil nicht vorhanden ist, erhalten Sie die folgende Meldung:

```
Hey! Get in here and play this Game!
```

### Nachricht standortabhängig abbrechen

Sie können eine Nachricht aufgrund von so gut wie allem abbrechen. Das folgende Beispiel zeigt, wie Sie eine Nachricht abbrechen können, wenn jemand nicht in einem bestimmten Gebiet wohnt und damit nicht für die Aktion, Anzeige bzw. Zustellung infrage kommt.

{% raw %}
```liquid
{% if {{${time_zone.$}}} =='America/Los_Angeles' %}
Stream now!
{% else %}
{% abort_message () %}
{% endif %}
```
{% endraw %}

![][26]

Sie können Nachrichten auch auf Grundlage verbundener Inhalte [abbrechen][1].


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[13]: {% image_buster /assets/img/liquid-if-totalspend.png %}
[14]: {% image_buster /assets/img/liquid-if-elsif-games.png %}
[25]: https://docs.shopify.com/themes/liquid/basics/operators
[26]: {% image_buster /assets/img/abort-if.png %}
