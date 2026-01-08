---
nav_title: E-Mail-Stil
article_title: E-Mail-Styling
page_order: 2
page_type: reference
description: "In diesem Artikel finden Sie eine Übersicht über die besten Methoden zur Gestaltung von E-Mail-Kampagnen, die Sie bei der Erstellung Ihrer Kampagnen berücksichtigen sollten."
channel: email

---

# E-Mail-Stil

## Adressenstil

Die **Betreffzeile** ist eines der ersten Dinge, die der Empfänger sieht, wenn er Ihre Nachricht erhält. Wenn Sie sich auf 6 bis 10 Wörter beschränken, erzielen Sie die höchsten Öffnungsraten. 

Es gibt auch verschiedene Ansätze für eine gute Betreffzeile, von einer Frage, um das Interesse des Lesers zu wecken, über eine direktere Formulierung bis hin zu einer personalisierten Betreffzeile, um Ihre Kunden anzusprechen. Bleiben Sie nicht bei einer einzigen Betreffzeile, sondern nutzen Sie [A/B-Tests]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#what-are-multivariate-and-ab-testing/), um neue Betreffzeilen auszuprobieren und ihre Wirksamkeit zu messen. Die Betreffzeilen sollten nicht länger als 35 Zeichen sein, damit sie auf dem Handy richtig angezeigt werden.

Im Feld „Von“ sollte klar ersichtlich sein, wer der oder die Absender:in ist. Versuchen Sie nicht, den Namen einer Person oder eine ungewöhnliche Abkürzung zu verwenden. Verwenden Sie stattdessen einen wiedererkennbaren Namen wie Ihren Markennamen. Wenn die Verwendung des Namens einer Person zu den Methoden Ihrer Marke zur Personalisierung von E-Mails passt, bleiben Sie konsequent, um eine Beziehung zu dem Empfänger aufzubauen. Der Name "Von" sollte nicht länger als 25 Zeichen sein, damit er auf dem Handy richtig angezeigt wird.

### Adressen, auf die keine Antwort erfolgt

E-Mail-Adressen, auf die keine Antwort erfolgt, sind aus mehreren Gründen nicht zu empfehlen, da sie Ihre Leser aus dem Konzept bringen. Viele Empfänger antworten auf die E-Mail, um sich abzumelden. Wenn sie das nicht dürfen, ist die nächste Maßnahme meist die Kennzeichnung der E-Mail als Spam.

Abwesenheitsantworten können tatsächlich wertvolle Informationen liefern, die Öffnungsrate erhöhen und Spam-Meldungen verringern (indem diejenigen entfernt werden, die keine E-Mails erhalten möchten). Auf einer persönlichen Ebene kann eine Nicht-Antwort auf die Empfänger unpersönlich wirken und sie davon abhalten, weitere E-Mails von Ihrem Unternehmen zu erhalten.

## Preheader-Text

Der Text in der Kopfzeile einer E-Mail vermittelt auf effiziente Weise das Hauptthema der Nachricht, um das Interesse des Lesers zu wecken und ihn zum Öffnen der Nachricht zu bewegen. Preheader-Text wird auch häufig von Marketern für E-Mails verwendet, um zusätzliche Informationen über den Content einer E-Mail bereitzustellen. Ein Preheader ist der Vorschautext, der unmittelbar nach einem E-Mail-Betreff angezeigt wird. Im folgenden Beispiel lautet der Preheader `- Brand. New. Lounge Shorts`.

![Preheader-Text in einem Posteingang von Google Mail mit dem Text "Marke. Neu. Lounge Shorts“.]({% image_buster /assets/img_archive/preheader_example.png %})

Die Länge des sichtbaren Textes in der Kopfzeile hängt vom E-Mail-Client des Benutzers und von der Länge der Betreffzeile der E-Mail ab. Im Allgemeinen empfehlen wir, dass E-Mail-Preheader zwischen 50 und 100 Zeichen lang sind.

Im Folgenden finden Sie einige Best Practices, die Sie beim Schreiben Ihrer Preheader beachten sollten:

1. Aktionsaufrufe kommen ins Spiel, nachdem die Leser Ihre E-Mail geöffnet haben.
  - Weisen Sie Ihren Lesern die richtige Richtung, ob sie nun ein Abonnement abschließen, ein Produkt kaufen oder Ihre Website besuchen sollen.
  - Verwenden Sie starke Worte, damit der Leser genau weiß, worum Sie ihn bitten. Achten Sie jedoch darauf, dass der Text die Stimme der Marke Ihres Unternehmens widerspiegelt und dass jeder Aufruf zum Handeln einen gewissen Nutzen für den Verbraucher hat.
  - Der Preheader sollte nicht länger als 85 Zeichen sein und eine Art beschreibende Aufforderung zum Handeln enthalten, die die Betreffzeile unterstützt.

2. E-Mails und Landing Sites, auf die Sie Ihre Nutzer leiten, sollten für Mobilgeräte optimiert sein:
  - Keine Zwischenablagefelder
  - Große Form-Felder
  - Einfache Navigation
  - Großer Text
  - Großzügiges Leerzeichen
  - Kurze, prägnante Textpassagen
  - Klare Aufforderungen zum Handeln

### Preheader-Zeichenbegrenzungen

  |   Mobiler E-Mail-Client  |  Limit  |
  |:----------------------:|:-------:|
  | iOS Outlook            | 74      |
  | Android nativ         | 43      |
  | Android Gmail          | 24      |
  | iOS Nativ             | 82      |
  | iOS Google Mail              | 30      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }

  |  Desktop-E-Mail-Client  |  Limit  |
  |:----------------------:|:-------:|
  | Apple Mail             | 33      |
  | Outlook '13            | 38      |
  | Outlook for Mac '15   | 53      |
  | Outlook '16            | (50 %)      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }


  |  Webmail E-Mail Client  |  Limit  |
  |:----------------------:|:-------:|
  | AOL Mail               | 81      |
  | Gmail                  | 119     |
  | Outlook.com            | 49      |
  | Office 365             | 40      |
  | Mail.ru                | 64      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## E-Mail Größe

Achten Sie darauf, die Größe Ihrer E-Mails zu begrenzen. E-Mails, die größer als 102 KB sind, belasten nicht nur die Server von Braze extrem, sondern werden auch von Gmail und anderen Clients abgeschnitten. Versuchen Sie, die Größe Ihrer E-Mail unter 25 KB für reinen Text oder 60 KB mit Bildern zu beschränken. Wir empfehlen Ihnen dringend, unseren Bild-Uploader zu verwenden, um Bilder hochzuladen und auf diese Bilder mit der Adresse `href` zu verweisen.

|   Nur Text   | Text mit Bildern |     E-Mail Breite    |
|:-------------:|:----------------:|:------------------:|
| Maximal 25 KB |   Maximal 60 KB   | Maximal 600 Pixel |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Textlänge

In der folgenden Tabelle finden Sie die empfohlenen Textlängen.

| Text Spezifikationen | Empfohlene Eigenschaften |
| --- | --- |
| Länge der Betreffzeile | Maximal 35 Zeichen (für optimale Anzeige auf dem Handy) (6 bis 10 Wörter) |
| Länge des Absendernamens | Maximal 25 Zeichen (für eine optimale Anzeige auf dem Handy) |
| Preheader Länge | Maximal 85 Zeichen |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Bildgröße

In der folgenden Tabelle finden Sie die empfohlenen Bildgrößen. Kleinere, qualitativ hochwertige Bilder werden schneller geladen, verwenden Sie also das kleinstmögliche Asset, um den gewünschten Output zu erzielen.

|     Größe    | Breite des Kopfzeilenbildes |  Körperbild Breite  |   Dateitypen  |
|:-----------:|:------------------:|:------------------:|:-------------:|
| Maximal 5 MB | Maximal 600 Pixel | Maximal 480 Pixel | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Deeplinking

Ein hoher Prozentsatz der E-Mails wird auf mobilen Geräten gelesen. Die Verwendung von [Deeplinking]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) ist eine hervorragende Methode, um mit diesen mobilen E-Mail-Empfänger:innen in Kontakt zu treten. Bei Push-Benachrichtigungen und In-App-Nachrichten führt ein Deep Link den Nutzer direkt zu einem bestimmten Ziel innerhalb einer App. 

E-Mails bieten jedoch keine Klarheit darüber, ob die Empfänger:innen die App installiert haben. Die Vermeidung von Deeplinks hilft also, Fehlermeldungen für diese Empfänger:in zu vermeiden, die nicht über die App verfügen.

