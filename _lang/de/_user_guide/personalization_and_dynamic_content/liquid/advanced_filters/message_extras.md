---
nav_title: Tag für Nachrichten-Extras
article_title: "Tag \"Nachrichten-Extras\""
page_order: 1
description: "Dieser Artikel erklärt, wie Sie das Liquid-Tag \"Nachrichten-Extras\" verwenden und die Syntax überprüfen können."
alias: "/message_extras_tag/"
---

# Liquid-Tag "Nachrichten-Extras"

> Verwenden Sie das Liquid-Tag `message_extras`, um Ihre Versandereignisse mit dynamischen Daten aus Connected-Content, Katalogen, angepassten Attributen (z.B. Sprache oder Land), Canvas-Entry-Eigenschaften oder anderen Datenquellen zu versehen.

Das Liquid-Tag `message_extras` hängt Schlüssel-Wert-Paare an das entsprechende Sendeereignis in Currents und Snowflake Data Sharing an. 

Um dynamische oder zusätzliche Daten zurück an Versandereignisse in Currents oder Snowflake Data Sharing zu senden, fügen Sie den entsprechenden Liquid-Tag in Ihre Nachricht ein. 

Hier ist ein Beispiel für das Standard-Liquid-Tag-Format für `message_extras`:

{% raw %}
```liquid
{% message_extras :key test :value 123 %}
```
{% endraw %}

Sie können die Tags nach Bedarf zu Ihren Schlüssel-Wert-Paaren im Nachrichtentext hinzufügen. Die Länge aller Schlüssel und Werte sollte jedoch 1 KB nicht überschreiten. In Currents und Snowflake Data Sharing sehen Sie ein neues Ereignisfeld namens `message_extras` für Ihre Versandereignisse. Dies erzeugt eine serialisierte JSON-Zeichenfolge in einem Feld.

## Unterstützte Kanäle

Das Tag `message_extras` wird für alle Nachrichtentypen mit Sendeereignis und für Impression-Ereignisse bei In-App-Nachricht unterstützt. Für die Verwendung von `message_extras` mit In-App-Nachrichten müssen bestimmte [Mindest-SDK-Versionen](#iam-sdk) erfüllt sein.

## So verwenden Sie das Tag `message_extras` 

1. Geben Sie in den Nachrichtentext für den Kanal das Liquid-Tag `message_extras` ein. Oder Sie verwenden das Modal **Personalisierung hinzufügen** und wählen die Option **Nachrichten-Extras** als Personalisierungstyp aus. 

![Das Modal "Personalisierung hinzufügen" mit ausgewählten Nachrichten-Extras als Personalisierungstyp.]({% image_buster /assets/img_archive/message_extras1.png %}){: style="max-width:35%;"}

{: start="2"}

2. Geben Sie das [Schlüssel-Wert-Paar]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) für jedes `message_extras`-Tag ein. 

![Ein Beispiel für Schlüssel-Wert-Paare für das Tag Nachrichten-Extras. Das Titelfeld lautet "Ihre neuen Favoriten". Die Nachricht enthält Schlüssel-Wert-Paare für das Tag Nachrichten-Extras und den folgenden Satz: "Wir freuen uns, Ihnen eine Auswahl an neuen und spannenden Produkten anbieten zu können, die mit Sicherheit zu Ihren neuen Lieblingsprodukten werden."]({% image_buster /assets/img_archive/message_extras2.png %}){: style="max-width:70%;"}

{: start="3"}

3. Wenn Ihre Kampagne oder Ihr Canvas versendet wurde, hängt Braze die dynamischen Daten zum Sendezeitpunkt an das Feld `message_extras` der Sendeereignisse in Currents oder Snowflake Data Sharing an.

## Überprüfung der Syntax

Alle anderen Eingaben, die nicht dem oben beschriebenen Tag-Standard entsprechen, werden möglicherweise nicht an Currents oder Snowflake weitergeleitet. Vermeiden Sie in Ihrer Syntax bzw. Formatierung:

- Nicht vorhandene, leere oder falsch eingegebene Begrenzungszeichen
- Doppelte Schlüssel (Braze sendet standardmäßig das Schlüssel-Wert-Paar, das zuerst gefunden wird)
- Zusätzlicher Text, bevor Schlüssel oder Werte definiert werden
- Schlüssel und Werte in falscher Reihenfolge 
  - {% raw %}Zum Beispiel, ```{% message_extras :value 123 :key test %}```{% endraw %}

## Senden von Aktionscode-Informationen an Currents

{% multi_lang_include shopify.md section='Liquid promotion codes with Currents' %}

## Überlegungen

- Wenn Ihre Schlüsselwerte 1 KB überschreiten, werden sie abgeschnitten. 
- Leerzeichen werden bei der Zeichenzählung berücksichtigt. Beachten Sie, dass Braze Leerzeichen an Anfang und Ende weglässt.
- Das resultierende JSON gibt nur String-Werte aus.
- Sie können Liquid-Variablen als Schlüssel oder Wert einschließen, aber keine anderen Liquid-Tags in `message_extras` verwenden.
  - Sie könnten zum Beispiel das folgende Liquid verwenden: {% raw %}```{% assign value = '123' %} {% assign key = 'test' %} {% message_extras :key {{key}} :value {{value}} %}```{% endraw %}

## Häufig gestellte Fragen

#### Wie kann ich das Feld message_extras in den Sendeereignissen mit meinen Engagement-Ereignissen wie Öffnungen und Klicks verknüpfen? 

Es wird eine `dispatch_id` generiert und in Ihren Sendeereignissen bereitgestellt. Diese kann als eindeutiger Bezeichner verwendet werden, um bestimmte Klicks, Zugriffe oder Zustellungsereignisse zuzuordnen. Sie können dieses Feld in Currents oder Snowflake verwenden und abfragen. Erfahren Sie mehr über [`dispatch_id` Verhalten]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

#### Kann ich message_extras mit In-App-Nachrichten verwenden? {#iam-sdk}

Ja, Sie können `message_extras` in Ihren In-App-Nachrichten verwenden, solange auf den Nutzergeräten mindestens folgende SDK-Versionen vorhanden sind:

{% sdk_min_versions web:5.2.0 android:30.4.0 swift:8.4.0 %}

