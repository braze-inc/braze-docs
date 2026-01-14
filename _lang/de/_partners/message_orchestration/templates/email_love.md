---
nav_title: "E-Mail Liebe"
article_title: E-Mail Liebe
description: "Lernen Sie die Integration von Braze mit Email Love, einem Figma-Plugin, mit dem Sie responsive und barrierefreie HTML-E-Mails direkt aus Figma entwerfen und exportieren können."
alias: /partners/email_love/
page_type: partner
search_tag: Partner

---

# E-Mail Liebe

> [Email Love](https://emaillove.com/) ist ein Figma-Plugin, mit dem Sie responsive und barrierefreie HTML-E-Mails direkt aus Figma heraus entwerfen und exportieren können. Das Feature Export to Braze von Email Love verwendet die Braze API, um Ihre E-Mail Templates nahtlos auf Braze hochzuladen.

## Voraussetzungen

| Anforderung            | Beschreibung                                                      |
|------------------------|------------------------------------------------------------------|
| **E-Mail Liebeskonto** | Um diese Partnerschaft nutzen zu können, benötigen Sie ein E-Mail Love-Konto. |
| **Braze REST API-Schlüssel** | Ein Braze REST API-Schlüssel mit vollständig aktivierter `Templates` Berechtigung. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation}

## Verwendung von E-Mail Love mit Braze

### Schritt 1: Starten Sie das Plugin

Um Ihr Template für E-Mails zu gestalten, müssen Sie zunächst das Plugin laden. Ausführlichere Anweisungen finden Sie in der Dokumentation von Email Love zum [Hochladen Ihrer E-Mails auf Braze](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm).

### Schritt 2: Erstellen Sie Ihren ersten Rahmen

Wählen Sie im Plugin den Button **[+ Keine Vorlage ausgewählt]**, um einen neuen Rahmen für Ihr E-Mail-Design zu erstellen.

### Schritt 3: Gestalten Sie das Template mit den vorgefertigten Komponenten von Email Love

Wählen Sie den von Ihnen erstellten Rahmen aus und fügen Sie Komponenten (Kopfzeilen, Content-Blöcke, CTAs und Fußzeilen) aus der Bibliothek **des** Plugins hinzu, um Ihre E-Mail zu strukturieren.

![Die vorgefertigten Komponenten von E-Mail Love.]({% image_buster /assets/img/email_love/emaillove1_content.png %})

### Schritt 4: Anpassen der Komponenten

Ändern Sie die Komponenten mit den Figma-Werkzeugen, um Text, Bilder, Farben und Layout-Elemente anzupassen, damit das Design des Templates mit Ihrer Marke übereinstimmt. Wenn Sie eine Fußzeilenkomponente hinzufügen, wird beim Exportieren automatisch ein Link zum Abmelden von Braze eingefügt.

![Anpassen von Komponenten in Figma.]({% image_buster /assets/img/email_love/emaillove2_components.png %})

### Schritt 5: Exportieren Sie Ihr Template für E-Mails nach Braze

1. Wenn Sie fertig sind, wählen Sie den Rahmen aus, den Sie exportieren möchten. Beachten Sie, dass Sie eine E-Mail Love-Fußzeile verwenden müssen, die einen Abmeldelink enthält, damit der Export funktioniert.
2. Wählen Sie den Button **Exportieren** im Plugin und wählen Sie **Braze** aus dem Dropdown-Menü.
3. Kopieren Sie Ihren API-Schlüssel und fügen Sie ihn in das Feld **Braze API-Schlüssel** innerhalb des Plugins Email Love Figma ein.
4. Wählen Sie den Button **API-Schlüssel festlegen**.
5. Wählen Sie **Instanz-ID ändern** und wählen Sie dann Ihre Braze-Instanz ID aus.

![Exportieren eines Templates nach Braze aus dem Plugin Email Love.]({% image_buster /assets/img/email_love/emaillove3_exportbraze.png %}){: style="max-width:50%;"}

### Schritt 6: Bearbeiten Sie Ihre E-Mail in Braze

Gehen Sie in Braze zu **Templates** > **Vorlagen bearbeiten** > **Nachricht bearbeiten**. Im Template-Editor können Sie entweder Ihre E-Mail im HTML-Format bearbeiten oder den **Rich-Text-Editor** auf dem Tab **Klassisch** verwenden.

## Unterstützung und Fehlerbehebung

Ausführlichere Anweisungen finden Sie in der Dokumentation von Email Love zum [Exportieren eines E-Mail-Entwurfs](https://help.emaillove.com/exporting-an-email-design/6rcR6LPWq6BoYseKZf41nS/uploading-your-email-to-braze-/3ZcmGaGz6a8azeZQxWgKzm). Wenn Sie zusätzliche Unterstützung benötigen, wenden Sie sich an das Email Love Team.
