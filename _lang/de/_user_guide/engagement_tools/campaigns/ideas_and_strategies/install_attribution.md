---
nav_title: Verstehen von Benutzerinstallationen
article_title: Verstehen von Benutzerinstallationen 
page_order: 7
page_type: reference
description: "Dieser Referenzartikel beschreibt Nutzer:innen (Install-Attribution Tracking) und verschiedene Möglichkeiten, diese Informationen in Ihrer Kampagne anzuwenden."
tool:
  - Campaigns
  - Segments
---

# Verstehen der Benutzerinstallationen

> Install-Attribution Tracking ist eine großartige Möglichkeit, Ihre erste Beziehung zu Ihren Nutzer:innen zu verbessern. Wenn Sie wissen, wie, wo und - was noch wichtiger ist - warum ein Benutzer Ihre App installiert, können Sie besser verstehen, wer Ihr Benutzer ist und wie Sie ihm Ihre App vorstellen sollten. 

Braze bietet zwar kein Tracking der Installationsattribution, aber wir können uns in [Dienste]({{site.baseurl}}/partners/message_orchestration/attribution) wie Branch und AppsFlyer integrieren, um Ihnen nahtlos Installationsdaten zur Verfügung zu stellen.

## Segmentieren Sie Ihre Benutzer

Sobald ein Benutzer Ihre App installiert hat, können Sie damit beginnen, ihn auf der Grundlage der folgenden [Filter für die Installationsattribution][2] zu segmentieren. Eine Reise-App könnte zum Beispiel Nutzer, die über eine Anzeige zu Strandurlaubsangeboten gekommen sind, dem Segment "Strandliebhaber" hinzufügen. In ähnlicher Weise könnte eine Musik-App die Nutzer auf der Grundlage des Musikgenres segmentieren, das in der Werbung angezeigt wird, die zur Installation geführt hat.

## Bewährte Praktiken

### Personalisiertes Onboarding

Da Sie nun mehr Informationen über Ihre Nutzer:innen haben, können Sie deren Onboarding-Prozess personalisieren. Das kann so einfach sein wie das Ändern der Bilder in Ihren Nachrichten, um sie an die Vorlieben der Nutzer:innen anzupassen, oder so komplex wie das Erstellen eines eindeutigen Nutzer-Onboardings für jede Anzeige, die zu einer Installation führen kann. Um eine umfassende Abfolge von Nachrichten zu skalieren, die das Verhalten der Nutzer:innen berücksichtigen kann, lesen Sie unsere Dokumentation zu [Canvas][5].

### Referenzdaten aus der Anzeige

Benutzer können durch ein Werbeangebot oder eine Werbeaktion zu Ihrer App gelockt werden. Die Verwendung von Installationsattributionsdaten ermöglicht es Ihnen, Kampagnen mit Rabattcodes oder Angeboten nur an die Benutzer zu senden, die aufgrund dieser Werbeaktionen installiert haben. Wenn Ihre Anzeige Informationen über ein bestimmtes Produkt enthält (z. B. einen bestimmten Film in einer Video-App oder einen Verkauf in einer E-Commerce-App), können Sie auf ähnliche Weise Kampagnen senden, die Nutzer auf die richtige Seite Ihrer App leiten.

## Werbemaßnahmen auswerten

Daten zur Install-Attribution können bei der Bewertung der Effektivität verschiedener Marketingkampagnen von großem Nutzen sein. Wenn Sie sich ansehen, welche Anzeigen und Kampagnen zu den meisten Installationen führen und welche zurückbleiben, können Sie Ihre Ressourcen auf die überzeugendsten Anzeigen konzentrieren.

[2]: {{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#install-attribution
[3]: {% image_buster /assets/img_archive/install_onboarding.png %}
[5]: {{site.baseurl}}/developer_guide/rest_api/messaging/#canvas
