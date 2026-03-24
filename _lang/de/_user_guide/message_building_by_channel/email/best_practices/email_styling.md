---
nav_title: E-Mail-Styling
article_title: E-Mail-Styling
page_order: 2
page_type: reference
description: "In diesem Artikel finden Sie eine Übersicht über Best Practices für das E-Mail-Styling, die Sie bei der Erstellung Ihrer E-Mail-Kampagnen als Referenz nutzen können."
channel: email

---

# E-Mail-Styling

## Adress-Styling

Die **Betreffzeile** ist eines der ersten Dinge, die Empfänger:innen sehen, wenn sie Ihre Nachricht erhalten. Wenn Sie sich auf 6 bis 10 Wörter beschränken, erzielen Sie die höchsten Öffnungsraten. 

Es gibt auch verschiedene Ansätze für eine gute Betreffzeile – von einer Frage, um das Interesse der Leser:innen zu wecken, über eine direktere Formulierung bis hin zur Personalisierung, um Ihre Kundschaft gezielt anzusprechen. Bleiben Sie nicht bei einer einzigen Betreffzeile, sondern nutzen Sie [A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#what-are-multivariate-and-ab-testing/), um neue Betreffzeilen auszuprobieren und ihre Wirksamkeit zu messen. Die Betreffzeilen sollten nicht länger als 35 Zeichen sein, damit sie auf Mobilgeräten richtig angezeigt werden.

Im Feld „Von" sollte klar ersichtlich sein, wer der Sender ist. Verwenden Sie möglichst nicht den Namen einer Person oder eine ungewöhnliche Abkürzung. Verwenden Sie stattdessen einen wiedererkennbaren Namen wie Ihren Markennamen. Wenn die Verwendung eines Personennamens zu den Personalisierungsmethoden Ihrer Marke für E-Mails passt, bleiben Sie konsequent, um eine Beziehung zu den Empfänger:innen aufzubauen. Der „Von"-Name sollte nicht länger als 25 Zeichen sein, damit er auf Mobilgeräten richtig angezeigt wird.

### No-Reply-Adressen

No-Reply-E-Mail-Adressen werden aus mehreren Gründen generell nicht empfohlen, da sie Ihre Leser:innen abschrecken. Viele Empfänger:innen antworten auf die E-Mail, um sich abzumelden. Wenn ihnen das nicht möglich ist, besteht die nächste Maßnahme meist darin, die E-Mail als Spam zu markieren.

Abwesenheitsantworten können tatsächlich wertvolle Informationen liefern, die Öffnungsrate erhöhen und Spam-Berichte verringern (indem diejenigen entfernt werden, die keine E-Mails erhalten möchten). Auf persönlicher Ebene kann eine No-Reply-Adresse auf Empfänger:innen unpersönlich wirken und sie davon abhalten, weitere E-Mails von Ihrem Unternehmen zu erhalten.

## Preheader-Text

Der Preheader-Text in einer E-Mail vermittelt auf effiziente Weise das Hauptthema der Nachricht, um das Interesse der Leser:innen zu wecken und zum Öffnen zu animieren. Preheader-Text wird auch häufig von E-Mail-Marketern verwendet, um zusätzliche Informationen über den Inhalt einer E-Mail bereitzustellen. Ein Preheader ist der Vorschautext, der unmittelbar nach der Betreffzeile einer E-Mail angezeigt wird. Im folgenden Beispiel lautet der Preheader `- Brand. New. Lounge Shorts`.

![Preheader-Text in einem Gmail-Posteingang mit dem Text „Brand. New. Lounge Shorts".]({% image_buster /assets/img_archive/preheader_example.png %})

Die Länge des sichtbaren Preheader-Textes hängt vom E-Mail-Client der Nutzer:innen und von der Länge der Betreffzeile der E-Mail ab. Im Allgemeinen empfehlen wir, dass E-Mail-Preheader zwischen 50 und 100 Zeichen lang sind.

{% alert note %}
Der Preheader kann Liquid im E-Mail-Text referenzieren, und der E-Mail-Text kann Liquid im Preheader referenzieren. Dies liegt daran, dass der Preheader-Text Teil des E-Mail-Textes ist, wenn Sie Nachrichten an Empfänger:innen senden.
{% endalert %}

Im Folgenden finden Sie einige Best Practices, die Sie beim Schreiben Ihrer Preheader beachten sollten:

1. Handlungsaufforderungen kommen ins Spiel, nachdem die Leser:innen Ihre E-Mail geöffnet haben.
  - Weisen Sie Ihren Leser:innen die richtige Richtung – ob sie nun ein Abonnement abschließen, ein Produkt kaufen oder Ihre Website besuchen sollen.
  - Verwenden Sie starke Worte, damit die Leser:innen genau wissen, worum Sie sie bitten. Achten Sie jedoch darauf, dass der Text die Markenstimme Ihres Unternehmens widerspiegelt und dass jede Handlungsaufforderung einen gewissen Nutzen für die Verbraucher:innen aufweist.
  - Der Preheader sollte nicht länger als 85 Zeichen sein und eine beschreibende Handlungsaufforderung enthalten, die die Betreffzeile unterstützt.

2. E-Mails und Landingpages, auf die Sie Ihre Nutzer:innen weiterleiten, sollten für Mobilgeräte optimiert sein:
  - Keine Interstitial-Fenster
  - Große Formularfelder
  - Einfache Navigation
  - Großer Text
  - Großzügiger Weißraum
  - Kurzer, prägnanter Fließtext
  - Klare Handlungsaufforderungen

### Preheader-Zeichenbegrenzungen

  |   Mobiler E-Mail-Client  |  Limit  |
  |:----------------------:|:-------:|
  | iOS Outlook            | 74      |
  | Android nativ         | 43      |
  | Android Gmail          | 24      |
  | iOS nativ             | 82      |
  | iOS Gmail              | 30      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }

  |  Desktop-E-Mail-Client  |  Limit  |
  |:----------------------:|:-------:|
  | Apple Mail             | 33      |
  | Outlook '13            | 38      |
  | Outlook for Mac '15   | 53      |
  | Outlook '16            | 50      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }


  |  Webmail-E-Mail-Client  |  Limit  |
  |:----------------------:|:-------:|
  | AOL Mail               | 81      |
  | Gmail                  | 119     |
  | Outlook.com            | 49      |
  | Office 365             | 40      |
  | Mail.ru                | 64      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## E-Mail-Größe

Achten Sie darauf, die Größe Ihrer E-Mails zu begrenzen. E-Mail-Texte, die größer als 102&nbsp;KB sind, belasten nicht nur die Braze-Server extrem, sondern werden auch von Gmail und anderen E-Mail-Clients abgeschnitten. Versuchen Sie, die Größe Ihrer E-Mail unter 25&nbsp;KB für reinen Text oder 60&nbsp;KB mit Bildern zu halten. Wir empfehlen Ihnen dringend, unseren Bild-Uploader zu verwenden, um Bilder zu hosten und diese Bilder über `href` zu referenzieren.

|   Nur Text   | Text mit Bildern |     E-Mail-Breite    |
|:-------------:|:----------------:|:------------------:|
| Maximal 25&nbsp;KB |   Maximal 60&nbsp;KB   | Maximal 600 Pixel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Um Ihre E-Mail-Kampagne oder Ihr Template zu speichern, stellen Sie sicher, dass der E-Mail-Text 400&nbsp;KB nicht überschreitet.
{% endalert %}

## Textlänge

In der folgenden Tabelle finden Sie die empfohlenen Textlängen.

| Textspezifikationen | Empfohlene Eigenschaften |
| --- | --- |
| Länge der Betreffzeile | Maximal 35 Zeichen (für optimale Anzeige auf Mobilgeräten) (6 bis 10 Wörter) |
| Länge des Absendernamens | Maximal 25 Zeichen (für optimale Anzeige auf Mobilgeräten) |
| Preheader-Länge | Maximal 85 Zeichen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Bildgröße

In der folgenden Tabelle finden Sie die empfohlenen Bildgrößen. Kleinere, qualitativ hochwertige Bilder werden schneller geladen. Verwenden Sie also das kleinstmögliche Asset, um die gewünschte Ausgabe zu erzielen.

|     Größe    | Breite des Kopfzeilenbildes |  Breite des Inhaltsbildes  |   Dateitypen  |
|:-----------:|:------------------:|:------------------:|:-------------:|
| Maximal 5&nbsp;MB | Maximal 600 Pixel | Maximal 480 Pixel | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Deeplinking

Bei Push-Benachrichtigungen und In-App-Nachrichten führt ein [Deeplink]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) Nutzer:innen direkt zu einem bestimmten Ziel innerhalb einer App. Deeplinks setzen jedoch voraus, dass die App installiert ist, und E-Mails bieten keine Möglichkeit festzustellen, ob Empfänger:innen die App haben. Das bedeutet, dass Deeplinks in E-Mails zu Fehlern bei Empfänger:innen führen können, die die App nicht installiert haben.

Verwenden Sie stattdessen [Universal Links und App Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links), die als Standard-URLs funktionieren. Sie können sie so konfigurieren, dass sie die App öffnen oder Nutzer:innen zu einer bestimmten Seite weiterleiten. Sie können auch zum App Store umleiten oder auf eine Webseite zurückfallen, wenn die App nicht installiert ist.