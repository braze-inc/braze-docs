---
nav_title: Juli
page_order: 6
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für Juli 2019."
---

# Juli 2019

{% alert update %}
Braze hat in diesem Monat zwei (Sie haben richtig gelesen - **zwei**) Produkte veröffentlicht! Die neueste Version steht ganz oben, die frühere Version [beginnt weiter unten auf dieser Seite](#earlier-this-month)!
{% endalert %}

## SAML/SSO

[Single Sign-on]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/) (SSO) bietet Unternehmen eine sichere und zentralisierte Möglichkeit, den Zugriff auf das Braze-Dashboard zu kontrollieren. Kurz gesagt, ein einziger Satz Zugangsdaten kann für den Zugriff auf verschiedene Anwendungen, einschließlich Braze, verwendet werden.

Zusätzlich zu [Google Sign-In mit OAuth 2.0-Unterstützung](https://developers.google.com/identity/protocols/OAuth2) wünschen sich Unternehmen SSO mit Security Assertion Markup Language (SAML) Unterstützung. Dies ermöglicht ihnen die nahtlose Integration mit großen Identitätsanbietern (IdPs), einschließlich [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/) und [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/), die die neuesten Branchenstandards (SAML 2.0) unterstützen.

Braze unterstützt:
- [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)
- [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/)
- [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)

## Ereignis anpassen API-Schlüssel zeigt

Wir haben die Partnerseite von Adjust aktualisiert, um diesen API-Schlüssel für Kund:in zugänglich zu machen.

## Neue Partner

Einige neue Partner haben sich unserem Alloys-Programm angeschlossen und sind in unsere Docs aufgenommen worden! Sagen Sie hallo zu:
- [Fivetran]({{site.baseurl}}/partners/fivetran/)
- [Talon.One]({{site.baseurl}}/partners/talonone/)
- [Voucherify]({{site.baseurl}}/partners/voucherify/)

## Verbesserung der Details der Kampagne

Erweiterte Kampagnendetails werden jetzt im Abschnitt ... warten Sie es ab..**. Kampagnendetails** auf der **Kampagnenseite** angezeigt!

## Nur Minen in Segmenten & Canvas anzeigen

Der Filter "Nur meine anzeigen" auf der Seite **Kampagnen** hat sich als äußerst beliebt erwiesen. Deshalb fügen wir diese Option jetzt auch den Listen Canvas und Segmente hinzu!

### Verhalten bei Fortschritt

Sie können jetzt festlegen, [wann ein:e Nutzer:in]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) von einem Canvas-Schritt zum nächsten voranschreitet. Zu diesen Optionen gehören "Nachricht gesendet" und "Gesamte Zielgruppe nach Verzögerung".

### In-App-Nachrichten in Canvas

[In-App-Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/) sind jetzt in Canvas verfügbar! Fügen Sie einen Canvas-Schritt hinzu und durchsuchen Sie die verfügbaren Kanäle, um eine In-App-Nachricht hinzuzufügen.

# Zu Beginn dieses Monats

## Entfernen von Bildern aus Nutzerprofilen

Wir entfernen die in den Nutzerprofilen und Nutzersuchen von Braze angezeigten Bilder der Nutzerprofile.

## Connected-Content in Content-Cards

Sie können jetzt [Connected-Content-Strings]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) und -Funktionen in [Content-Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) verwenden.

Connected-Content-Aufrufe an externe Server erfolgen, wenn eine Karte tatsächlich gesendet wird, nicht wenn die Karte vom Nutzer:innen angesehen wird. Ähnlich wie bei E-Mails wird der dynamische Content zum Zeitpunkt des Versands berechnet und festgelegt, und nicht erst, wenn eine Karte tatsächlich angesehen wird.

## Null "Antwort-an"-Adresse

Kunden:in können jetzt einen `null` Wert für die "Antwort-an"-Adresse einer E-Mail-Nachricht über die Seite **E-Mail-Einstellungen** in Braze oder über die [API]({{site.baseurl}}/api/endpoints/messaging/#email-object-specification) festlegen.  Wenn Sie diese Option verwenden, werden die Antworten an die angegebene Absenderadresse gesendet.  Sie können das Adressfeld "Von" jetzt als `dan@emailaddress.com` anpassen, und Ihre Kund:in haben die Möglichkeit, direkt an Dan zu antworten.

Um einen `null` -Wert für die "Antwort-an"-Adresse einer E-Mail-Nachricht von Braze festzulegen, gehen Sie in der Navigation auf **Einstellungen verwalten** und dann auf den Tab **E-Mail-Einstellungen**. Blättern Sie zum Abschnitt **Einstellungen für ausgehende E-Mails** und wählen Sie **"Reply-To" ausschließen und Antworten an "Von" senden** als Standardadresse aus.

## Vergleiche der Kampagnen

Betrachten Sie [mehrere Kampagnen gleichzeitig, um ihre relative Performance zu vergleichen]({{site.baseurl}}/report_builder/), und zwar Seite an Seite in Braze - in einem einzigen Fenster!

## Template Versand ID in Nachrichten mit Liquid

{% alert note %}
Das Verhalten für `dispatch_id` unterscheidet sich zwischen Canvas und Kampagnen, da Braze Canvas-Schritte (mit Ausnahme von Eingangsschritten, die geplant werden können) als getriggerte Ereignisse behandelt, auch wenn sie "geplant" sind. Erfahren Sie mehr über [`dispatch_id` Verhalten]({{site.baseurl}}/help/help_articles/data/dispatch_id/) in Canvase und Kampagnen.
{% endalert %}

Wenn Sie den Versand einer Nachricht aus der Nachricht heraus verfolgen möchten (z.B. in einer URL), können Sie ein Template im `dispatch_id` verwenden. Die Formatierung dafür finden Sie in unserer Liste der unterstützten Tags für die Personalisierung unter [Canvas Attribute]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

Dies verhält sich genauso wie `api_id`, da `api_id` bei der Erstellung der Kampagne nicht verfügbar ist, wird es als Platzhalter eingefügt und in der Vorschau als `dispatch_id_for_unsent_campaign` angezeigt. Die ID wird generiert, bevor die Nachricht gesendet wird, und wird in die Sendezeit einbezogen.

{% alert warning %}
Das Liquid-Templating von `dispatch_id_for_unsent_campaign` funktioniert nicht mit In-App-Nachrichten, da In-App-Nachrichten keine `dispatch_id` haben.
{% endalert %}

## Die Einstellung "Nur meine anzeigen" bleibt bestehen

Der Filter "Nur meine anzeigen" auf dem Kampagnen-Raster bleibt jedes Mal aktiviert, wenn Sie die Seite **Kampagnen** besuchen.

## Updates für A/B-Tests

Sie können einen einmaligen [A/B-Test]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) mit bis zu acht Varianten (und optionaler Kontrolle) an einen vom Nutzer:innen festgelegten Prozentsatz der Zielgruppe einer Kampagne senden und dann die beste Variante zu einem vorher festgelegten Zeitpunkt an die verbleibende Zielgruppe senden.
