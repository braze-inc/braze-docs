---
nav_title: Juli
page_order: 6
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für Juli 2019."
---

# Juli 2019

{% alert update %}
Braze hat diesen Monat zwei (Sie haben richtig gelesen - **zwei**) Produktveröffentlichungen durchgeführt! Die neueste Version steht ganz oben, die frühere Version [beginnt weiter unten auf dieser Seite](#earlier-this-month)!
{% endalert %}

## SAML/SSO

[Single Sign-On]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/) (SSO) bietet Unternehmen eine sichere und zentralisierte Möglichkeit, den Zugriff auf das Braze-Dashboard zu kontrollieren. Kurz gesagt, ein einziger Satz von Anmeldedaten kann für den Zugriff auf verschiedene Anwendungen, einschließlich Braze, verwendet werden.

Zusätzlich zu [Google Sign-In mit OAuth 2.0-Unterstützung](https://developers.google.com/identity/protocols/OAuth2) wünschen sich Unternehmen SSO mit Security Assertion Markup Language (SAML) Unterstützung. Dies ermöglicht ihnen die nahtlose Integration mit großen Identitätsanbietern (IdPs), einschließlich [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/) und [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/), die die neuesten Branchenstandards (SAML 2.0) unterstützen.

Lötstützen:
- [OneLogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/)
- [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/entra/)
- [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/)

## Ereignis-API-Schlüssel anpassen zeigt

Wir haben die Partnerseite von Adjust aktualisiert, um diesen API-Schlüssel für Kunden zugänglich zu machen.

## Neue Partner

Einige neue Partner haben sich unserem Alloys-Programm angeschlossen und wurden zu unseren Docs hinzugefügt! Sagen Sie hallo zu:
- [FiveTran]({{site.baseurl}}/partners/fivetran/)
- [Talon.One]({{site.baseurl}}/partners/talonone/)
- [Voucherify]({{site.baseurl}}/partners/voucherify/)

## Verbesserung der Kampagnendetails

Erweiterte Kampagnendetails werden jetzt im Abschnitt ...warten Sie es ab...**Kampagnendetails** auf der **Kampagnenseite** angezeigt!

## Nur meine in Segmenten & Canvas anzeigen

Der Kontrollfilter "Nur meine anzeigen" auf der Seite **Kampagnen** hat sich als äußerst beliebt erwiesen. Aus diesem Grund fügen wir diese Option auch den Listen Canvas und Segment hinzu!

### Aufstiegsverhalten

Sie können jetzt festlegen, [wann ein Benutzer]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/) von einem Canvas-Schritt zum nächsten [wechselt]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/). Diese Optionen umfassen "Gesendete Nachricht" und "Gesamtes Publikum nach Verzögerung".

### In-App-Nachrichten in Canvas

[In-App-Nachrichten]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/) sind jetzt in Canvas verfügbar! Fügen Sie einen Canvas-Schritt hinzu und durchsuchen Sie die verfügbaren Kanäle, um eine In-App-Nachricht hinzuzufügen.

# Zu Beginn dieses Monats

## Benutzerprofilbild entfernen

Wir entfernen die Benutzerprofilbilder, die in den Benutzerprofilen und in der Benutzersuche von Braze angezeigt werden.

## Verbundene Inhalte in Inhaltskarten

Sie können jetzt Strings und Funktionen [von Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) in [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/overview/) verwenden.

Die Aufrufe von Connected Content an externe Server erfolgen, wenn eine Karte tatsächlich gesendet wird, und nicht, wenn die Karte vom Benutzer angesehen wird. Ähnlich wie bei E-Mails wird der dynamische Inhalt zum Zeitpunkt des Versands berechnet und festgelegt und nicht erst, wenn die Karte tatsächlich angesehen wird.

## Null "Antwort-an"-Adresse

Kunden können jetzt auf der Seite **E-Mail-Einstellungen** in Braze oder über die [API]({{site.baseurl}}/api/endpoints/messaging/#email-object-specification) einen Wert `null` für die "Antwort-an"-Adresse einer E-Mail-Nachricht festlegen.  Wenn Sie diese Option verwenden, werden die Antworten an die angegebene Absenderadresse gesendet.  Sie können das Adressfeld "Von" jetzt als `dan@emailaddress.com` personalisieren, und Ihre Kunden haben die Möglichkeit, Dan direkt zu antworten.

Um einen `null` Wert für die "Antwort-an"-Adresse einer E-Mail-Nachricht von Braze einzustellen, gehen Sie in der Navigation auf **Einstellungen verwalten** und dann auf die Registerkarte **E-Mail-Einstellungen**. Blättern Sie zum Abschnitt **Einstellungen für ausgehende E-Mails** und wählen Sie **"Antwort an" ausschließen und Antworten an "Von"** als Standardadresse **senden**.

## Vergleiche von Kampagnen

Schauen Sie sich [mehrere Kampagnen gleichzeitig]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/comparing_campaigns/) an [, um ihre relative Leistung zu vergleichen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/comparing_campaigns/), und zwar Seite an Seite in Braze - in einem einzigen Fenster!

## Vorlage Versand-ID in Nachrichten mit Liquid

{% alert note %}
Das Verhalten von `dispatch_id` unterscheidet sich zwischen Canvas und Kampagnen, da Braze Canvas-Schritte (mit Ausnahme von Eintrittsschritten, die geplant werden können) als ausgelöste Ereignisse behandelt, selbst wenn sie "geplant" sind. Erfahren Sie mehr über [`dispatch_id` Verhalten]({{site.baseurl}}/help/help_articles/data/dispatch_id/) in Canvases und Kampagnen.
{% endalert %}

Wenn Sie den Versand einer Nachricht aus der Nachricht heraus verfolgen wollen (z.B. in einer URL), können Sie in der Vorlage `dispatch_id`. Die Formatierung dafür finden Sie in unserer Liste der unterstützten Personalisierungs-Tags unter [Leinwandattribute]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

Dies verhält sich genau wie `api_id`, da `api_id` bei der Erstellung der Kampagne nicht verfügbar ist, wird es als Platzhalter eingefügt und in der Vorschau als `dispatch_id_for_unsent_campaign` angezeigt. Die ID wird generiert, bevor die Nachricht gesendet wird, und wird in die Sendezeit eingerechnet.

{% alert warning %}
Liquid Templating von `dispatch_id_for_unsent_campaign` funktioniert nicht mit In-App-Nachrichten, da In-App-Nachrichten keine `dispatch_id` haben.
{% endalert %}

## Die Einstellung "Nur meine anzeigen" bleibt bestehen

Der Filter "Nur meine anzeigen" auf dem Kampagnengitter bleibt immer aktiviert, wenn Sie die Seite **Kampagnen** besuchen.

## Aktualisierungen für A/B-Tests

Sie können einen einmaligen [A/B-Test]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/) mit bis zu acht Varianten (und optionaler Kontrolle) an einen vom Benutzer festgelegten Prozentsatz der Zielgruppe einer Kampagne senden und dann die beste Variante zu einem vorher festgelegten Zeitpunkt an die verbleibende Zielgruppe senden.
