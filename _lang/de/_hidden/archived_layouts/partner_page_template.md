---
nav_title: Partnerseite

page_order: 4

#Required
description: "Dies ist die Beschreibung der Google-Suche. Zeichen, die über 160 hinausgehen, werden abgeschnitten, fassen Sie sich kurz."
page_type: partner
tool:
  - Dashboard
  - Docs
  - Canvas
  - Campaigns
  - Segments
  - Templates
  - Media
  - Location
  - Currents
  - Reports

platform:
  - iOS
  - Android
  - Web
  - API

channel:
  - Content Cards
  - Email
  - News Feed
  - In-App Messages
  - Push
  - SMS
  - Webhooks
  
noindex: true
#ATTENTION: remove noindex and this alert from template

---

# [Name des Partners]

> Willkommen beim Template für die Partnerseite! Hier finden Sie alles, was Sie brauchen, um Ihre eigene Partnerseite zu erstellen. In diesem ersten Abschnitt sollten Sie den Partner im ersten Absatz in ein oder zwei Sätzen beschreiben. Fügen Sie außerdem einen Link zur Hauptseite des Partners hinzu.

Im zweiten Absatz sollten Sie die Beziehung zwischen Braze und diesem Partner untersuchen und erklären. Dieser Absatz sollte erklären, wie Braze und dieser Partner zusammenarbeiten, um die Bindung zwischen dem Braze Nutzer:innen und seinen Kund:innen zu festigen. Erläutern Sie die "Elevation", die eintritt, wenn ein Braze Nutzer:innen sich mit diesem Partner und seinen Diensten integriert oder sie nutzt.

## Anforderungen oder Voraussetzungen

In diesem Abschnitt erfahren Sie alles, was Sie für die Integration mit dem Partner und die Nutzung seiner Dienste benötigen. Am besten stellen Sie diese Informationen in einem kurzen Anweisungsabschnitt zu, in dem alle nichttechnischen wichtigen Details beschrieben werden, z.B. ob Ihre Integration zusätzlichen Sicherheitsprüfungen oder Genehmigungen unterliegt oder nicht. Dann sollten Sie ein Chart verwenden, um die technischen Anforderungen der Integration zu beschreiben.

{% alert important %}
Die folgenden Anforderungen sind typische Anforderungen, die Sie von Braze benötigen könnten. Wir empfehlen, die Attribute Titel, Herkunft, Links und Formulierungen zu verwenden, die in dem folgenden Chart aufgeführt sind. Passen Sie die Beschreibung so an, dass Sie wissen, wozu diese Anforderungen jeweils dienen.
{% endalert %}

| Anforderung | Herkunft | Zugang | Beschreibung |
|---|---|---|---|
|Braze Workspace REST API-Schlüssel | Braze Plattform | **Einstellungen** > **API-Schlüssel** Seite | Diese Beschreibung sollte Ihnen sagen, was Sie mit dem REST-API-Schlüssel für den Workspace tun sollen. |
|Braze API Endpunkt | Braze Plattform | Sehen Sie sich unsere [aufgelisteten Endpunkte]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) an oder öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/). | Beschreibung ausstehend. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## [Art der Integration] Integration

Hier können Sie die Integration in einzelne Schritte untergliedern. Schreiben Sie nicht einfach nur endlose Absätze - dies sind technische Dokumente, die von Marketern und Entwicklern gleichermaßen verwendet werden, um die Integration zum Laufen zu bringen. Ihr einziges Ziel in diesem Abschnitt ist es, eine beschreibende Dokumentation zu verfassen, die den Nutzer:innen von Braze hilft, ihre Arbeit zu erledigen. Mit 'Art der Integration' im Titel des Abschnitts geben wir an, ob es sich um eine Side-by-side-Integration, eine Server-zu-Server-Integration oder um den Standard handelt. So können Sie mehrere Integrationsabschnitte haben, wenn es mehr als eine Möglichkeit der Integration mit diesem Partner gibt.

Wenn es sich um eine Currents-Integration handelt, sollte sich diese Seite im Abschnitt Currents befinden, und es sollte eine entsprechende Navigationsseite erstellt werden, die zu diesem Standort in Currents weiterleitet.

### Schritt 1: Dies ist eine kurze Beschreibung von Schritt Eins

Gliedern Sie dies einfach auf und fügen Sie bei Bedarf Code hinzu. Denken Sie daran, dass Sie mehrere verschiedene Codes anbieten können - es ist nicht nötig, nur eine Art der Integration anzubieten.

### Schritt 2: Dieser Schritt beschreibt die Bilder

Sie haben die Möglichkeit, Bilder in Ihre Dokumentation aufzunehmen. Wir empfehlen Ihnen, dies zu tun, und zwar mit Bedacht.

### Schritt 3: Wie viele Schritte

Skizzieren Sie die Nutzung der Integration - vor allem, wenn es darum geht, Liquid in unseren Nachrichten-Editor einzufügen.

## Customization

Dies ist ein **optionaler** Abschnitt. Hier könnten Sie alle spezifischen Möglichkeiten zur Anpassung Ihrer Integration zwischen den beiden Partnern skizzieren.

## Diese Integration verwenden

Hier sollten Sie beschreiben, wie Sie die Integration nutzen können - lassen Sie Ihre Leser wissen, ob sie ein paar Buttons drücken müssen oder ob sie nach der Integration überhaupt nichts mehr tun müssen.

### Schritt 1: Dies ist eine kurze Beschreibung von Schritt Eins

Einfach eine typische Schritt-für-Schritt-Anleitung.

## Anwendungsfälle

Dies kann ein wichtiger Teil Ihrer Dokumentation sein. Dies ist zwar optional, aber es ist ein guter Ort, um typische oder sogar neuartige Anwendungsfälle für die Integration zu skizzieren. Dies kann als Mittel zum Verkauf oder Upselling der Beziehung genutzt werden - es liefert Kontext, Ideen und vor allem eine Möglichkeit, die Möglichkeiten der Integration zu visualisieren.
