---
nav_title: April
page_order: 9
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für April 2020."
---
# April 2020

## Movable Ink Partnerschaft

Movable Ink bietet Braze-Kunden die Möglichkeit, intelligente kreative Funktionen wie Countdown-Timer, Umfragen und Rubbellose in ihren Push-, In-App-Nachrichten- und Content-Card-Kampagnen zu verwenden. Movable Ink und Braze ermöglichen einen vielseitigeren Ansatz für dynamische, datengesteuerte Nachrichten, die den Nutzern in Echtzeit Informationen über die Dinge liefern, die wichtig sind.

[Integrieren Sie Movable Ink]({{site.baseurl}}/partners/channel_extensions/creative_and_personalization/intelligent_creative/movable_ink/) in Ihre Kampagnen!

## Intelligentes Timing

Wenn Sie eine Kampagne planen, können Sie [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) (früher Intelligent Delivery) verwenden, um Ihre Nachricht an jeden Benutzer zu dem Zeitpunkt zu übermitteln, zu dem Braze feststellt, dass eine Person sich am ehesten damit befassen wird.

Zu den Aktualisierungen dieser Funktion gehören:
- **Klärung der Ruhezeiten**: Die Funktionalität von Quiet Hours bleibt unverändert, aber die Benutzeroberfläche wurde zur Verdeutlichung angepasst.
- **Hinzufügung einer Vorschaukarte**: Sie können nun ein Diagramm erstellen, um zu sehen, wie viele Benutzer zu jeder Stunde des Tages mit Intelligent Timing Nachrichten erhalten werden und welcher Anteil der Benutzer über genügend Daten verfügt, um eine optimale Zeit zu berechnen.
- **Hinzufügung von Custom Fallback**: Sie können nun die Ortszeit wählen, zu der Sie den Benutzern eine Nachricht schicken, wenn sie nicht genügend Daten über ihr Engagement haben, um eine optimale Zeit zu berechnen.

## Facebook Zielgruppen-Export

Braze bietet Ihnen die Möglichkeit, Ihre Benutzer manuell von der Braze-Segment-Seite zu exportieren, um Facebook Custom Audiences zu erstellen. Dies ist ein einmaliger, statischer Audience-Export und erstellt nur neue [Facebook Custom Audiences]({{site.baseurl}}/partners/facebook/).

Derzeit ist ein neuer Braze Facebook Audience Export-Prozess für alle Cluster verfügbar, der den Prozess mit einfachen Integrationsschritten rationalisiert. Sie müssen keine OAuth Redirect URIs mehr auf die Whitelist setzen, um benutzerdefinierte Zielgruppen zu senden, oder in den Facebook App-Einstellungen herumspielen, um die Integration vorzunehmen.

{% alert important %}
Beachten Sie, dass alle Kunden, die derzeit Facebook Custom Audiences verwenden, ihre Braze-Segmente mit diesen neuen Schritten neu integrieren müssen.
{% endalert%}


## Aktualisierungen der API für Inhaltsblöcke und E-Mail-Vorlagen

Die [template/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) und [content_block/list]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) API-Endpunkte wurden aktualisiert und enthalten nun ein neues `tags` Feld. In diesem Feld werden alle Tags, die auf den aktuellen Block oder die E-Mail-Vorlage zutreffen, als Array aufgelistet.

## Personalisierte Absenderadresse

Wenn Sie eine E-Mail-Nachricht in Braze erstellen, können Sie jetzt die Absenderadresse der Nachricht im Abschnitt **Sendeinfo** der E-Mail-Komposition personalisieren. Sie können alle von uns unterstützten [Personalisierungs-Tags]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) verwenden

![Personalisierte Absenderadresse][0]{: style="max-width:80%"}

[0]: {% image_buster /assets/img/personalized-from-name.png %}
