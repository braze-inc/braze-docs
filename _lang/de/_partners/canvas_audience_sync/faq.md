---
nav_title: FAQs
article_title: Zielgruppe Sync FAQ
alias: /partners/audience_sync_faq/
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

Wenn der vorherige Nutzer:innen, der die Integration verbunden hat, nicht mehr in Ihrem Unternehmen tätig ist, müssen Sie die Integration mit dem neuen Nutzer:innen aktualisieren, indem Sie **Konto ändern** auswählen. Wählen Sie dann **Bestätigen** und stellen Sie eine Verbindung mit dem neuen Nutzer:innen her. Wir empfehlen, die Nutzer:innen zu wechseln, wenn keine aktiven Synchronisierungen stattfinden, z.B. vor einem geplanten Eingang von Nutzer:innen in einen Canvas, da eine Synchronisierung während des Übergangs vom vorherigen Nutzer zu einem neuen Nutzer aktive Canvase unterbrechen kann. Wir empfehlen, die Nutzer:innen zu wechseln, wenn keine aktiven Synchronisierungen stattfinden, z. B. vor einem geplanten Eingang von Nutzer:innen in einen Canvas.

Der Benutzer, der die Verbindung wiederherstellt, muss sowohl Lese- als auch Schreibzugriff auf alle Zielgruppen haben, damit die Nutzer:innen erfolgreich mit den Partnern synchronisiert werden können. Vergewissern Sie sich, dass der Nutzer:innen, der die Integration wiederherstellt, Zugriff auf die gleichen Anzeigenkonten und Zielgruppen hat. Sie brauchen keine bestehenden Canvas-Schritte zu bearbeiten. 

### Was sind häufige Fehler, die bei der Erstellung und Verwaltung meiner Zielgruppen-Synchronisationen auftreten können?

| Fehler | Grund | Lösung |
| --- | --- | --- |
| Ungültiges Token | Dies kann der Fall sein, wenn Sie Ihr Passwort für die Anmeldung bei einem bestimmten Anzeigennetzwerk geändert haben oder wenn Ihre Zugangsdaten abgelaufen sind. | Gehen Sie auf die jeweilige Partnerseite, um Ihr Konto zu trennen und wieder zu verbinden. |
| Zielgruppe zu klein | Dies kann vorkommen, wenn Sie einen Audience Sync-Schritt erstellt haben, der Nutzer:innen aus Ihren Zielgruppen entfernt. Wenn die Größe Ihrer Zielgruppe gegen Null geht, kann das Netzwerk feststellen, dass die Zielgruppe zu klein ist, um bedient zu werden. | Vergewissern Sie sich, dass Sie eine Strategie zur Synchronisierung der Zielgruppe in Erwägung ziehen, bei der regelmäßig Nutzer:innen hinzugefügt und entfernt werden, ohne dass die Zielgruppe vollständig erschöpft wird. |
| Zielgruppe gibt es nicht | Der Schritt Audience Sync verwendet eine Zielgruppe, die nicht existiert. Dies kann auch getriggert werden, wenn Sie nicht über die erforderliche Berechtigung zum Zugriff auf die Zielgruppe verfügen. | Fügen Sie eine aktive Zielgruppe in Ihrer Audience Sync-Konfiguration hinzu oder erstellen Sie eine neue Zielgruppe. |
| Versuch eines Zugriffs auf ein Anzeigenkonto | Dieser Fehler tritt auf, wenn Sie keine Berechtigung für das Anzeigenkonto, eine von Ihnen ausgewählte Zielgruppe oder beides haben. | Arbeiten Sie mit den Administratoren Ihres Anzeigenkontos zusammen, um den richtigen Zugang und die richtigen Berechtigungen zu erhalten. |
| Ungültige Einstellungen | Dies kann vorkommen, wenn Sie kein bestimmtes Audience Sync-Ziel in Canvas konfiguriert haben, einschließlich der entsprechenden Felder für Anzeigenkonten, Zielgruppen oder Nutzer:innen. | Vervollständigen Sie die Konfiguration der einzelnen Partner, bevor Sie sie starten. |
| Nutzungsbedingungen | Bei einigen Zielgruppen, wie z.B. Facebook, ist es für die Nutzung des Features Audience Sync erforderlich, dass das Werbenetzwerk bestimmte Dienste akzeptiert. Dieser Fehler wird ausgelöst, wenn Sie die entsprechenden Bedingungen nicht akzeptiert haben. | Bestätigen Sie, dass Sie die erforderlichen Bedingungen jedes Partners akzeptiert haben. Speziell für Facebook lesen Sie bitte die [Facebook-Fehlerbehebung]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync/#troubleshooting). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

