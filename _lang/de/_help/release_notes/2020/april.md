---
nav_title: April
page_order: 9
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für April 2020."
---
# April 2020

## Movable Ink Partnerschaft

Movable Ink bietet Braze-Kunden die Möglichkeit, intelligente kreative Features wie Countdown-Timer, Umfragen und Rubbellose in ihren Push-, In-App-Nachrichten- und Content-Card-Kampagnen zu verwenden. Movable Ink und Braze ermöglichen einen umfassenderen Ansatz für dynamische datengestützte Nachrichten, die Nutzer:innen mit Echtzeit-Elementen über die Dinge versorgen, die wichtig sind.

Beginnen Sie mit der [Integration von Movable Ink]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink/) in Ihre Kampagnen!

## Intelligentes Timing

Wenn Sie eine Kampagne planen, können Sie [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) (früher Intelligent Delivery) verwenden, um Ihre Nachricht jedem Nutzer:innen zu dem Zeitpunkt zuzustellen, zu dem Braze feststellt, dass die Wahrscheinlichkeit eines Engagements am größten ist.

Zu den Updates für dieses Feature gehören:
- **Klärung der Ruhezeiten**: Die Funktionalität der Ruhezeiten bleibt gleich, aber das UI wurde zur Verdeutlichung angepasst.
- **Hinzufügung eines Preview Charts**: Sie können jetzt ein Chart erstellen, um zu sehen, wie viele Nutzer:innen zu jeder Stunde des Tages mit Intelligent Timing Nachrichten erhalten werden und welcher Anteil der Nutzer:innen über genügend Daten verfügt, um eine optimale Zeit zu berechnen.
- **Hinzufügen eines angepassten Fallbacks**: Sie können nun die Ortszeit wählen, zu der Sie Nutzern:innen eine Nachricht schicken, wenn diese nicht genügend Daten über ihr Engagement haben, um eine optimale Zeit zu berechnen.

## Facebook Audience exportieren

Braze bietet Ihnen die Möglichkeit, Ihre Nutzer:innen von der Seite Segmente von Braze manuell zu exportieren, um angepasste Zielgruppen auf Facebook zu erstellen. Dies ist ein einmaliger, statischer Zielgruppenexport und erstellt nur neue [Facebook Custom Audiences]({{site.baseurl}}/partners/facebook/).

Derzeit ist ein neuer Braze Facebook Audience Exportprozess für alle Cluster verfügbar, der den Prozess mit einfachen Integrationsschritten rationalisiert. Sie müssen keine OAuth Redirect URIs mehr auf die Whitelist setzen, um angepasste Zielgruppen zu senden, oder in den Facebook App-Einstellungen herumspielen, um die Integration durchzuführen.

{% alert important %}
Beachten Sie, dass alle Clients, die derzeit Facebook Custom Audiences verwenden, ihre Braze Segmente mit diesen neuen Schritten neu integrieren müssen.
{% endalert%}


## Content-Block und E-Mail Template API Updates

Die [template/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/) und [content_block/list]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/get_list_email_content_blocks/) API Endpunkte wurden aktualisiert und enthalten nun ein neues `tags` Feld. Dieses Feld listet als Array alle Tags auf, die auf den aktuellen Block oder das E-Mail Template zutreffen.

## Personalisierte Absenderadresse

Wenn Sie in Braze eine E-Mail-Nachricht erstellen, können Sie jetzt die Absenderadresse der Nachricht im Abschnitt **Sendeinfo** der E-Mail-Komposition personalisieren. Sie können jeden unserer unterstützten [Tags für die Personalisierung]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) verwenden

![Personalisierte Absenderadresse]({% image_buster /assets/img/personalized-from-name.png %}){: style="max-width:80%"}

