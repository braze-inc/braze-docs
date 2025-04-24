---
nav_title: Odicci
article_title: Odicci
description: "Schritt-für-Schritt-Anleitung zur Integration von Odicci mit Braze für personalisierte Kampagnen im Marketing"
alias: /partners/odicci/
page_type: partner
search_tag: Partner
---

# Integration von Odicci mit Braze

> Erfahren Sie, wie Sie Braze in [Odicci](https://www.odicci.com/) integrieren können, eine Plattform, die es Unternehmen ermöglicht, Kunden durch loyale Omnichannel-Erlebnisse zu gewinnen, zu engagieren und zu binden.

{% alert tip %}
Weitere Ressourcen und FAQs finden Sie im [Odicci Help Center](https://help.odicci.com).
{% endalert %}

## Anwendungsfälle

Sie können die Odicci-Plattform mit Braze verbinden, um nahtlos Daten auszutauschen und Kampagnen zu verwalten. Dies beinhaltet:

- Automatische Übermittlung der in Odicci gesammelten Daten der Zielgruppe an Braze.
- Triggern von personalisierten Marketing Kampagnen auf der Grundlage von Nutzer:innen-Interaktionen.
- Abbildung der Felder zwischen Odicci und Braze, um eine genaue Synchronisierung der Daten zu gewährleisten.

## Beispiel

Ein Marketer nutzt die spielerischen Erlebnisse von Odicci, um E-Mail-Adressen für eine Marketing-Kampagne zu sammeln.

1. Ein Kunde schließt ein Spiel in Odicci ab und gibt dabei seine E-Mail Adresse an.
2. Odicci synchronisiert diese Daten automatisch mit Braze.
3. Braze triggert eine personalisierte "Danke"-E-Mail und enthält einen Rabattcode.

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung             | Beschreibung                                                               |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Ein Bericht von Odicci            | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Odicci-Konto mit Zugriff auf den Bereich **Integrationen**.|
| Braze REST API-Schlüssel        | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.track` und 'campaigns.list'. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration von Odicci

### Schritt 1: Aktivieren Sie die Integration in Odicci

1. Melden Sie sich bei Ihrem Odicci Konto an.
2. Navigieren Sie zum Bereich **Einstellungen > Integrationen**.
3. Suchen Sie die **Braze** Integration und klicken Sie auf **Verbinden**.

   ![Connect Braze Integration]({% image_buster /assets/img/odicci/braze_connect.png %})

4. Geben Sie Ihren Braze REST API-Schlüssel in das vorgesehene Feld ein.
5. Speichern Sie die Einstellungen, um die Integration auf Kontoebene zu aktivieren.

### Schritt 2: Beziehen Sie Ihren Braze REST API-Schlüssel

1. Melden Sie sich bei Ihrem Braze-Konto an.
2. Gehen Sie zu **Entwicklungskonsole > REST API-Schlüssel.**
3. Erstellen Sie einen neuen API-Schlüssel oder kopieren Sie einen vorhandenen Schlüssel mit der Berechtigung `users.track`.

### Schritt 3: Aktivieren Sie die Integration auf der Erfahrungsebene

1. Erstellen oder öffnen Sie eine **Experience** in Odicci Studio.
2. Navigieren Sie zu **Studio > Einstellungen > Integrationen.**
3. Suchen Sie das Kontrollkästchen **Braze** und markieren Sie es, um die Integration für das Erlebnis zu aktivieren.
4. Speichern Sie Ihre Änderungen.

### Schritt 4: Abbildung Felder

1. Nachdem Sie die Integration aktiviert haben, bleiben Sie im Bereich **Studio > Einstellungen > Integrationen**.
2. Ordnen Sie die Felder aus Ihrer Odicci-Erfahrung (e.g., `Email`, `Name`) den entsprechenden Feldern in Braze zu.
3. Speichern Sie Ihre Konfiguration.

   ![Konfiguration der Abbildung von Feldern]({% image_buster /assets/img/odicci/braze_field_mapping.png %})

### Schritt 5: Testen Sie die Integration

1. Führen Sie die Erfahrung in Odicci aus, um Daten zu sammeln.
2. Überprüfen Sie, ob die Daten korrekt mit Braze synchronisiert werden, indem Sie das Braze-Dashboard oder die Datenprotokolle überprüfen.
3. Stellen Sie sicher, dass die abgebildeten Felder in Braze korrekt ausgefüllt sind.

## Fehlersuche

Wenn Sie Probleme mit der Integration haben, sollten Sie die folgenden Lösungen in Betracht ziehen. Für weitere Unterstützung wenden Sie sich bitte an den [Odicci Support](https://help.odicci.com).

### API-Schlüssel nicht gültig

Überprüfen Sie Ihren Braze API-Schlüssel und stellen Sie sicher, dass er über die erforderlichen Berechtigungen verfügt. Geben Sie dann den API-Schlüssel in den Einstellungen für die Integration von Odicci erneut ein.

### Daten werden nicht synchronisiert

Überprüfen Sie, ob die Felder im Abschnitt **Abbildung der Felder** korrekt konfiguriert sind. Stellen Sie dann sicher, dass der API-Schlüssel über die Berechtigung für Nutzerdatenimporte verfügt.

### Kampagne nicht triggernd

Überprüfen Sie die Einstellungen der Braze Kampagne, um sicherzustellen, dass die richtige Zielgruppe oder die richtigen Triggerbedingungen eingestellt sind.
