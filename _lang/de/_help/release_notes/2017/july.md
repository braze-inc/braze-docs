---
nav_title: Juli
page_order: 6
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für Juli 2017."
---

# Juli 2017

## Große Bilder in Web Push

Wir haben Unterstützung für große Bilder für Web-Push auf Chrome für Windows und Android hinzugefügt, so dass Sie reichhaltige, ansprechende Kundenerlebnisse schaffen können. Erfahren Sie mehr über [Web Push][58].

## Aktualisierungen der E-Mail-Felder

Sie können jetzt E-Mails für eine bestimmte Gruppe von Absenderadressen sperren, um sicherzustellen, dass Sie nicht versehentlich eine falsche Adresse eingeben. Das E-Mail-Formular wird mit den in den letzten 6 Monaten verwendeten Adressen vorausgefüllt, um den Prozess zu vereinfachen. Weitere Informationen finden Sie unter [E-Mail-Best Practices][57].

## Aktualisierungen der API für Kampagnendetails

Der Endpunkt `/campaign/details` liefert jetzt Informationen über seine Nachrichten, so dass Sie über die API den Betreff, den HTML-Textkörper, die Absenderadresse und die Antwort-Felder abrufen können. Erfahren Sie mehr über [Braze APIs][56].

## Aktualisierungen für Liquid Templating

Wir haben die Möglichkeit hinzugefügt, Variantenattribute in Canvases und Kampagnen zu erstellen. In Canvas können Sie nun sowohl die API-ID der Variante als auch den Namen der Variante als Vorlage verwenden, und in Kampagnen können Sie nun die `message_api_id` und `message_name` einer Nachricht als Vorlage verwenden. Beide Aktualisierungen ermöglichen eine größere Flexibilität bei der Nachrichtenübermittlung, so dass Sie personalisierte Kampagnen erstellen können. Erfahren Sie mehr über [personalisierte Nachrichten][55].

## Neuer HTML-E-Mail-Editor

Mit einem Vollbild-HTML-Editor, der eine Live-Vorschau, Personalisierung über Liquid und einen verbesserten Vollbild-Texteditor mit Zeilennummern und Syntaxhervorhebung ermöglicht, können Sie jetzt ganz einfach E-Mails schreiben und testen. Erfahren Sie mehr über das [Verfassen von E-Mails][54].

## Aktualisierungen der Vorschauen

Sie können jetzt dem Bildschirmfenster folgen, wenn Sie in der Nachrichtenvorschau in Kampagnen und Canvases nach unten scrollen, um sicherzustellen, dass Sie die Änderungen immer im Blick haben. Erfahren Sie mehr über [Vorschauen und Tests][53].

## Neuer Filter für Segmentzugehörigkeit

Wir haben den [Filter Segmentzugehörigkeit][52] hinzugefügt, mit dem Sie Nutzer auf der Grundlage ihrer Mitgliedschaft in einem Ihrer bestehenden Segmente ansprechen können. Außerdem haben wir die Möglichkeit hinzugefügt, in Segmentfiltern sowohl die "Und"- als auch die "Oder"-Logik zu verwenden, sowie die Möglichkeit, Segmente ineinander zu verschachteln. Diese Aktualisierungen ermöglichen es Ihnen, maßgeschneiderte Nachrichten an Ihre Kunden mit größerer Präzision zu versenden. 

## Update auf Android Vorschau

Wir haben die [Android-Vorschau][51] aktualisiert, um neuere Versionen von Android seit Android N zu berücksichtigen.


[51]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#step-5-preview-message
[52]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#targeting-filters
[53]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#step-6-preview-message
[54]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template
[55]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[56]: {{site.baseurl}}/developer_guide/rest_api/basics/#what-is-a-rest-api
[57]: {{site.baseurl}}/help/troubleshooting_guide/troubleshooting_guide/#email
[58]: {{site.baseurl}}/user_guide/message_building_by_channel/push/web
[98]:{{site.baseurl}}/user_guide/onboarding/platform_administrative_features/#authentication-rules
