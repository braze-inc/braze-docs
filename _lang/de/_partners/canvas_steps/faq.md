---
nav_title: FAQs
article_title: Audience Sync FAQ
description: "Dieser Artikel enthält Antworten auf häufig gestellte Fragen zu Audience Sync."
page_order: 80
Tool:
  - Canvas

---

# Häufig gestellte Fragen

> Dieser Artikel enthält Antworten auf einige häufig gestellte Fragen zu Audience Sync.

### Wie lange dauert es, bis meine Zielgruppen in meinem Audience Sync-Partner-Dashboard angezeigt werden? 

Wie lange es dauert, ein Publikum zu bevölkern, hängt von dem jeweiligen Partner ab.

Alle Netzwerke werden die Anfragen von Braze verarbeiten und versuchen, die Benutzer zu vergleichen. Dieser Vorgang kann in der Regel zwischen 6 und 48 Stunden dauern.

Sie können den spezifischen Zeitbereich im Abschnitt Fehlerbehebung in der Dokumentation für jeden Audience Sync-Partner überprüfen. 

### Welche Art von Erstanbieterdaten kann ich in meinem Audience Sync verwenden?

Die spezifischen Felder, die für jeden Partner verwendet werden, können je nach den Anforderungen des Partners variieren. 

Wenn Sie z.B. eine Audience Sync mit Facebook konfigurieren, können Sie eine Vielzahl von First-Party-Feldern wie E-Mail, Telefon, Vorname und Nachname verwenden, wohingegen Sie bei Snapchat nur E-Mail, Telefon oder die mobile Werbe-ID auswählen können. 

Es ist wichtig zu wissen, dass die Benutzerfelder, die Sie für die Synchronisierung auswählen können, mit den Standardattributen von Braze und den IDs für mobile Werbung übereinstimmen. Sie müssen sicherstellen, dass Sie diese Daten in geeigneter Weise über unsere SDKs oder APIs weitergeben. 

### Was geschieht, wenn meine Daten verarbeitet werden, um sie an die einzelnen Audience Sync-Partner zu senden?

Die Daten, die Sie zum Senden an Ihr Audience Sync-Ziel auswählen, werden normalisiert. Jeder Partner kann je nach seinen API-Anforderungen unterschiedliche Spezifikationen für die Datennormalisierung haben. Bitte prüfen Sie daher jeden partnerspezifischen Endpunkt für weitere Details.

Darüber hinaus hackt Braze alle Daten, bevor wir sie mit unseren Audience Sync-Partnern synchronisieren, um sicherzustellen, dass alle PII mit SHA256 gehasht werden.

### Was sind die häufigsten Fehler, die beim Erstellen und Verwalten meiner Audience Syncs auftreten können?

- **Ungültiges Token**<br>
  - Typische Ursachen sind, dass Sie Ihr Passwort für die Anmeldung bei einem bestimmten Werbenetzwerk geändert haben oder dass Ihre Anmeldedaten abgelaufen sind.
  - Um dieses Problem zu beheben, gehen Sie einfach auf die betreffende Partnerseite, um Ihr Konto zu trennen und erneut zu verbinden.
- **Publikumsgröße zu gering**<br>
  - Dieser Fehler tritt in der Regel auf, wenn Sie einen Audience Sync-Schritt erstellt haben, der Benutzer aus Ihren Audiences entfernt. Wenn die Größe Ihres Publikums gegen Null geht, kann das Netzwerk feststellen, dass das Publikum zu klein ist, um bedient zu werden. 
  - Um dieses Problem zu lösen, stellen Sie sicher, dass Sie eine Audience-Sync-Strategie in Erwägung ziehen, die regelmäßig Nutzer hinzufügt und entfernt, ohne dass die Größe der Audience völlig erschöpft wird.
- **Das Publikum existiert nicht**<br>
  - Dieser Fehler tritt auf, weil der Schritt Audience Sync eine Audience verwendet, die nicht existiert. Dies kann auch ausgelöst werden, wenn Sie nicht über die erforderliche Berechtigung zum Zugriff auf die Zielgruppe verfügen. 
  - Um dieses Problem zu beheben, fügen Sie eine aktive Zielgruppe in Ihrer Audience Sync-Konfiguration hinzu oder erstellen Sie eine neue Zielgruppe.
- **Versuch eines Zugriffs auf ein Anzeigenkonto**<br>
  - Dieser Fehler tritt auf, wenn Sie keine Berechtigungen für das von Ihnen ausgewählte Anzeigenkonto und/oder die Zielgruppe haben.
  - Um dieses Problem zu lösen, arbeiten Sie mit den Admins Ihres Anzeigenkontos zusammen, um den richtigen Zugang und die richtigen Berechtigungen zu erhalten. 
- **Ungültige Einstellungen**<br>
  - Dieser Fehler wird ausgelöst, wenn Sie kein bestimmtes Audience Sync-Ziel in Canvas konfiguriert haben, einschließlich der abzugleichenden Anzeigenkonten, Zielgruppen oder Benutzerfelder. 
  - Um dieses Problem zu beheben, schließen Sie die Konfiguration jedes Partners ab, bevor Sie ihn starten.
- **Nutzungsbedingungen**<br>
  - Bei einigen Audience Sync-Zielen, wie z.B. Facebook, ist es erforderlich, dass das Werbenetzwerk bestimmte Nutzungsbedingungen akzeptiert, um die Audience Sync-Funktion zu nutzen. Dieser Fehler wird ausgelöst, wenn Sie die entsprechenden Bedingungen nicht akzeptiert haben. 
  - Um dieses Problem zu lösen, stellen Sie sicher, dass Sie die erforderlichen Bedingungen jedes Partners akzeptiert haben. Speziell für Facebook lesen Sie bitte die [Facebook-Fehlerbehebung](https://www.braze.com/docs/partners/canvas_steps/facebook_audience_sync/#troubleshooting). 
