---
nav_title: Übersicht
article_title: Übersicht
description: "In diesem Referenzartikel erfahren Sie, wie Sie Braze Audience Sync für Facebook verwenden, um Anzeigen auf der Grundlage von verhaltensbezogenen Auslösern, Segmentierung und mehr zu schalten."
page_order: 0
Tool:
  - Canvas

---

# Übersicht Audience Sync

> Mit der Funktion Braze Audience Sync können Sie die Reichweite Ihrer Kampagnen auf viele der wichtigsten sozialen und Werbetechnologien ausdehnen. Mit [Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas) können Marken dynamisch und sicher First-Party-Nutzerdaten mit dem Werbe-Ökosystem synchronisieren, um die Marketing- und Betriebseffizienz zu steigern.

## Anwendungsfälle

- Ansprechen von hochwertigen Nutzern über eigene und bezahlte Kanäle, um zusätzliche Käufe oder Engagement zu fördern.
- Erstellen Sie Lookalike Audiences für Ihre hochwertigen Nutzer, um die Kosten für die Akquisition neuer Nutzer und die Konversionen zu optimieren.
- Retargeting von Nutzern mit Anzeigen, die auf andere Marketingkanäle weniger gut reagieren.
- Erstellen von Unterdrückungszielgruppen, um zu verhindern, dass Nutzer Werbung erhalten, wenn sie bereits treue Kunden Ihrer Marke sind.

## Verfügbarkeit von Funktionen

Alle Braze-Kunden haben ab sofort Zugang zu Audience Sync to Google und Facebook. Um weitere Audience Sync-Ziele wie TikTok, Pinterest, Snapchat oder Criteo freizuschalten, müssen Sie Audience Sync Pro erwerben. Kontaktieren Sie Ihren Braze-Kundenbetreuer für weitere Informationen.

## Wie es funktioniert

Um Audience Sync mit Google oder Facebook zu verwenden, verbinden Sie Ihr Anzeigenkonto, indem Sie auf der Seite **Technologiepartner** nach dem Partner suchen.

![][3]{: style="max-width:35%;"} ![][4]{: style="max-width:35%;"}

Nachdem Sie Ihr Anzeigenkonto verbunden haben, können Sie ein Canvas mit einem Audience Sync-Schritt erstellen.

![][22]{: style="max-width:75%;"}

Wählen Sie dann den Partner aus, mit dem Sie die Audiences synchronisieren möchten.

![][19]{: style="max-width:85%;"}

Für jeden Partner müssen Sie im Rahmen Ihres Audience Sync-Schrittes Folgendes konfigurieren: 
- Anzeigenkonto
- Zielgruppe 
- Aktion zum Hinzufügen oder Entfernen von Benutzern 
- Passende Felder 

Beachten Sie, dass Braze die Benutzer synchronisiert, sobald sie den Schritt Audience Sync in Ihrem Canvas eingeben. 

Für jedes Audience Sync-Ziel kann der Partner unterschiedliche Anforderungen an die Felder haben, die wir senden können. Weitere Einzelheiten finden Sie in der Dokumentation des jeweiligen Partners. 

### Audience Sync Pro

Um einen Audience Sync Pro-Partner wie TikTok, Pinterest, Snapchat oder Criteo zu nutzen, können Sie Ihre Partner auf der Grundlage Ihrer Audience Sync Pro-Kaufkontingente im Abschnitt **Audience Sync Pro** auf der Seite **Technologiepartner** auswählen.

![][5]{: style="max-width:75%;"}

Wählen Sie zunächst die Partner aus, die Sie verwenden möchten, indem Sie Partner auswählen wählen. Mit jedem Kauf von Audience Sync Pro erhalten Sie 3 zugewiesene Audience Sync Pro-Ziele, die in jedem Ihrer Arbeitsbereiche auf Ihrem Dashboard verfügbar sind.

![][6]{: style="max-width:65%;"}

Nachdem Sie Ihre Audience Sync Pro-Ziele ausgewählt haben, verbinden Sie Ihr ausgewähltes Partner-Anzeigenkonto, indem Sie auf die Partner-Kachel klicken.

![][7]{: style="max-width:70%;"}

![][9]{: style="max-width:70%;"}

Zum Schluss erstellen Sie Ihren Audience Sync-Schritt in Canvas mit diesem Audience Sync Pro-Ziel.

## Überlegungen zum Datenschutz

{% alert important %}
Diese Dokumentation ist nicht als Rechtsberatung gedacht und darf auch nicht als solche angesehen werden. Die Verwendung von Audience Sync unterliegt bestimmten rechtlichen Anforderungen. Um sicherzustellen, dass Sie es in Übereinstimmung mit allen geltenden Gesetzen verwenden, sollten Sie sich von Ihrem Rechtsberater beraten lassen.
{% endalert %}

Wenn Sie Zielgruppen für das Ad Tracking aufbauen, möchten Sie vielleicht bestimmte Nutzer auf der Grundlage ihrer Präferenzen ein- oder ausschließen und Datenschutzgesetze einhalten, wie z. B. das Recht "Nicht verkaufen oder weitergeben" gemäß [CCPA](https://oag.ca.gov/privacy/ccpa). Vermarkter sollten die entsprechenden Filter für die Eignung der Nutzer in ihre Canvas-Eingabekriterien integrieren. Nachfolgend finden Sie einige Optionen.

Wenn Sie die [iOS IDFA über das Braze SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection) gesammelt haben, können Sie den Filter "Ads Tracking Enabled" verwenden. Wählen Sie den Wert `true`, um Benutzer nur an Audience Sync-Ziele zu senden, für die sie sich angemeldet haben.

![][2]

Wenn Sie `opt-ins`, `opt-outs`, `Do Not Sell Or Share` oder andere relevante benutzerdefinierte Attribute sammeln, sollten Sie diese als Filter in Ihre Canvas-Eingabekriterien aufnehmen:

![Ein Canvas mit einem Eintrag Publikum von "opted_in_marketing" ist gleich "true".][1]

Wenn Sie mehr darüber erfahren möchten, wie Sie diese Datenschutzgesetze innerhalb der Braze-Plattform einhalten können, lesen Sie bitte den Abschnitt [Technische Unterstützung zum Datenschutz]({{site.baseurl}}/dp-technical-assistance/).

[1]: {% image_buster /assets/img/audience_sync/audience_sync.png %}
[2]: {% image_buster /assets/img/audience_sync/audience_sync2.png %}
[3]: {% image_buster /assets/img/audience_sync/facebook_partner.png %}
[4]: {% image_buster /assets/img/audience_sync/google_ads_partner.png %}
[5]: {% image_buster /assets/img/audience_sync/audience_sync_pro1.png %}
[6]: {% image_buster /assets/img/audience_sync/audience_sync_pro2.png %}
[7]: {% image_buster /assets/img/audience_sync/audience_sync_pro3a.png %}
[8]: {% image_buster /assets/img/audience_sync/audience_sync_pro3b.png %}
[9]: {% image_buster /assets/img/audience_sync/audience_sync_pro4.png %}
[18]: {% image_buster /assets/img/audience_sync/audience_sync3.png %}
[19]: {% image_buster /assets/img/audience_sync/audience_sync4.png %}
[20]: {% image_buster /assets/img/audience_sync/audience_sync5.png %}
[21]: {% image_buster /assets/img/audience_sync/audience_sync6.png %}
[22]: {% image_buster /assets/img/audience_sync/audience_sync7.png %}