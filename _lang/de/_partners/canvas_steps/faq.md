---
nav_title: FAQs
article_title: Zielgruppe Sync FAQ
description: "Dieser Artikel enthält Antworten auf häufig gestellte Fragen zu Audience Sync."
page_order: 80
Tool:
  - Canvas

---

# Häufig gestellte Fragen

> Dieser Artikel enthält Antworten auf einige häufig gestellte Fragen zu Audience Sync.

### Wie lange dauert es, bis meine Zielgruppen in meinem Audience Sync Partner Dashboard angezeigt werden?

Wie lange es dauert, eine Zielgruppe zu bevölkern, hängt von dem jeweiligen Partner ab. Alle Netzwerke werden die Anfragen von Braze verarbeiten und versuchen, Nutzer:innen zu finden. Dieser Vorgang kann in der Regel zwischen 6 und 48 Stunden dauern.

Sie können die spezifische Zeitspanne im Abschnitt Fehlerbehebung in der Dokumentation für jeden Audience Sync Partner überprüfen.

### Welche Art von First-Party-Daten kann ich in meiner Audience Sync verwenden?

Die spezifischen Felder, die für jeden Partner verwendet werden, können je nach den Anforderungen des Partners variieren. 

Wenn Sie beispielsweise eine Audience-Synchronisierung mit Facebook konfigurieren, können Sie eine Vielzahl von First-Party-Feldern wie E-Mail, Telefon, Vorname und Nachname verwenden, während Sie bei Snapchat nur E-Mail, Telefon oder die ID des mobilen Werbers auswählen können. 

Bitte beachten Sie, dass die Nutzer:innen-Felder, die Sie für die Synchronisierung auswählen können, mit den Braze Standard-Attributen und den IDs für mobile Werbung korrelieren. Sie müssen sicherstellen, dass Sie diese Daten in geeigneter Weise über unsere SDKs oder APIs weitergeben. 

### Was passiert, wenn meine Daten verarbeitet werden, um sie an die einzelnen Audience Sync Partner zu senden?

Die Daten, die Sie zum Senden an Ihr Audience Sync Ziel auswählen, werden normalisiert. Jeder Partner kann aufgrund seiner API-Anforderungen unterschiedliche Spezifikationen für die Normalisierung von Daten haben. Bitte prüfen Sie daher jeden partnerspezifischen Endpunkt für weitere Details.

Darüber hinaus hackt Braze alle Daten, bevor wir Nutzer:innen mit unseren Audience Sync Partnern synchronisieren, um sicherzustellen, dass alle PII mit SHA256 gehasht werden.

### Warum kann ich für einige Partner mehrere Bezeichner in einem Schritt auswählen, für andere aber nur einen Bezeichner?

Dies wird von den Methoden der Partnerintegration bestimmt und nicht von Braze kontrolliert. Bei einigen Partnern (z.B. Meta) ist es zulässig, mehrere Bezeichner zu synchronisieren, während bei anderen Partnern (z.B. Google) immer nur ein einziger Bezeichner mit einem Nutzer:innen synchronisiert werden kann.

### Wie kann ich meine Integration erneut verbinden?

Wenn der vorherige Nutzer:innen, der die Integration verbunden hat, nicht mehr in Ihrem Unternehmen tätig ist, müssen Sie die Integration mit dem neuen Nutzer:innen aktualisieren. Wählen Sie dazu **Bestätigen** aus. Beachten Sie, dass dadurch aktive Canvase unterbrochen werden können.

Der Benutzer, der die Verbindung wiederherstellt, muss sowohl Lese- als auch Schreibzugriff auf alle Zielgruppen haben, damit die Nutzer:innen erfolgreich mit den Partnern synchronisiert werden können. Vergewissern Sie sich, dass der Nutzer:innen, der die Integration wiederherstellt, Zugriff auf die gleichen Anzeigenkonten und Zielgruppen hat. Es sollte nicht nötig sein, bestehende Canvas-Schritte zu bearbeiten. 

### Was sind die häufigsten Fehler, die bei der Erstellung und Verwaltung meiner Zielgruppen-Synchronisationen auftreten können?

- **Ungültiges Token**<br>
  - Typische Ursachen sind, dass Sie Ihr Passwort für die Anmeldung bei einem bestimmten Anzeigennetzwerk geändert haben oder dass Ihre Zugangsdaten abgelaufen sind.
  - Um dieses Problem zu beheben, gehen Sie einfach auf die betreffende Partnerseite, um Ihr Konto zu trennen und erneut zu verbinden.
- **Zielgruppe zu klein**<br>
  - Dieser Fehler tritt in der Regel auf, wenn Sie einen Audience Sync-Schritt erstellt haben, der Nutzer:innen aus Ihren Zielgruppen entfernt. Wenn die Größe Ihrer Zielgruppe gegen Null geht, kann das Netzwerk feststellen, dass die Zielgruppe zu klein ist, um bedient zu werden. 
  - Um dieses Problem zu lösen, stellen Sie sicher, dass Sie eine Strategie für die Audience Sync in Betracht ziehen, die regelmäßig Nutzer:innen hinzufügt und entfernt, ohne dass die Zielgruppengröße dadurch völlig erschöpft wird.
- **Zielgruppe gibt es nicht**<br>
  - Dieser Fehler tritt auf, weil der Schritt Audience Sync eine Zielgruppe verwendet, die nicht existiert. Dies kann auch getriggert werden, wenn Sie nicht über die erforderliche Berechtigung zum Zugriff auf die Zielgruppe verfügen. 
  - Um dieses Problem zu beheben, fügen Sie eine aktive Zielgruppe in Ihrer Audience Sync-Konfiguration hinzu oder erstellen Sie eine neue Zielgruppe.
- **Versuch eines Zugriffs auf ein Anzeigenkonto**<br>
  - Dieser Fehler tritt auf, wenn Sie keine Berechtigungen für das von Ihnen ausgewählte Anzeigenkonto und/oder die Zielgruppe haben.
  - Um dieses Problem zu lösen, arbeiten Sie mit den Admins Ihres Anzeigenkontos zusammen, um den richtigen Zugang und die richtigen Berechtigungen zu erhalten. 
- **Ungültige Einstellungen**<br>
  - Dieser Fehler triggert, wenn Sie kein bestimmtes Audience Sync-Ziel in Canvas konfiguriert haben, einschließlich der übereinstimmenden Felder für Anzeigenkonten, Zielgruppen oder Nutzer:innen. 
  - Um dieses Problem zu beheben, schließen Sie die Konfiguration der einzelnen Partner vor dem Start ab.
- **Nutzungsbedingungen**<br>
  - Bei einigen Zielgruppen, wie z.B. Facebook, ist es für die Nutzung des Features Audience Sync erforderlich, dass das Werbenetzwerk bestimmte Dienste akzeptiert. Dieser Fehler wird ausgelöst, wenn Sie die entsprechenden Bedingungen nicht akzeptiert haben. 
  - Um dieses Problem zu lösen, stellen Sie sicher, dass Sie die Bedingungen jedes Partners akzeptiert haben. Speziell für Facebook lesen Sie bitte die [Facebook-Fehlerbehebung]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync/#troubleshooting). 
