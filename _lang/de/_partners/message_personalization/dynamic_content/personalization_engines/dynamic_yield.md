---
nav_title: Dynamic Yield
article_title: Dynamic Yield
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Dynamic Yield. Diese Partnerschaft erlaubt es Ihnen, die Empfehlungs- und Segmentierungs-Engine von Dynamic Yield zu nutzen, um Experience Blocks zu erstellen, die in Nachrichten von Braze eingebettet werden können."
alias: /partners/dynamic_yield/
page_type: partner
search_tag: Partner

---

# Dynamic Yield

> [Dynamic Yield](https://www.dynamicyield.com/), ein Unternehmen von Mastercard, unterstützt Unternehmen aller Branchen bei der Bereitstellung digitaler Kundenerlebnisse, die personalisiert, optimiert und synchronisiert sind. Mit dem [Experience OS](http://www.dynamicyield.com/experience-os) von Dynamic Yield können Marketer, Produktmanager, Entwickler und digitale Teams Inhalte, Produkte und Angebote algorithmisch an jeden Kunden anpassen, um den Umsatz zu steigern und die Kundenbindung zu erhöhen.

_Diese Integration wird von Dynamic Yield gepflegt._

## Über die Integration

Die Partnerschaft von Braze und Dynamic Yield erlaubt es Ihnen, die Empfehlungs- und Segmentierungs-Engine von Dynamic Yield zu nutzen, um Experience Blocks zu erstellen, die in Nachrichten von Braze eingebettet werden können. Erfahrungsblöcke können aus:
- **Empfehlungsblöcke**: Legen Sie Algorithmen und Filter fest, um Nutzer:innen personalisierte Inhalte zu liefern, die beim Öffnen der E-Mail weitergegeben werden. 
- **Dynamische Content-Blöcke**: Targeting verschiedener Aktionen und Nachrichten für verschiedene Nutzer:innen. Das Targeting kann entweder auf Affinität oder auf Zielgruppe basieren. Der dynamische Ertrag bestimmt, welches personalisierte Erlebnis bei der Öffnung der E-Mail angezeigt werden soll. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Dynamisches Renditekonto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [dynamisches Renditekonto](https://adm.dynamicyield.com/users/sign_in#/r/dashboard). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Einen Erlebnisblock erstellen

Um einen Experience Block in Dynamic Yield zu erstellen, navigieren Sie zu **E-Mail > Experience Emails > Neu erstellen**.

Als nächstes wählen Sie **Erlebnisblock erstellen**, um einen Block mit dynamischen Inhalten oder Empfehlungen zu entwerfen, der in ein Braze E-Mail Template eingebettet werden soll.<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield7.png %})

### Schritt 2: Entwerfen Sie Ihre Messaging-Nachrichten

Das folgende Bild zeigt eine E-Mail von Grund auf im Builder.<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield5.png %})

1. Geben Sie einen Kampagnennamen, eine Notiz und Bezeichnungen für die Kampagne in den Kopfbereich ein.<br><br>
2. Fügen Sie einen Erfahrungsblock ein. Diese Blöcke umfassen:
  - [Empfehlungen](#configure-a-recommendations-block): Ein Widget, das den Nutzer:innen vollständig personalisierte Empfehlungen bietet.
  - [Dynamische Inhalte](#configure-a-dynamic-content-block): Targeting verschiedener Aktionen und Nachrichten für verschiedene Zielgruppen.<br><br>
3. Einstellungen aktualisieren:
  - Verwenden Sie die URL-Parameter zum Tracking von Klicks in Ihrer Analytics-Software (optional). Fügen Sie bei Bedarf Parameter zu den Standard-Anzeigen hinzu.
  - Wählen Sie ein Attribut-Fenster aus, entweder sieben Tage (Standard) oder einen Tag.<br><br>
4. Speichern und beenden. Sie können jederzeit zurückkehren, um alle Elemente Ihrer E-Mail zu bearbeiten, bevor der Code generiert wird. Nachdem der Code generiert wurde, können Sie alles bearbeiten, was [sich nicht auf den Code auswirkt](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZPXB6MH094J1MWS5N86FXH).

### Konfigurieren Sie einen Empfehlungsblock

Mit dem Empfehlungsblock können Sie Algorithmen und Filter für die personalisierten Inhalte der Nutzer:innen festlegen, die beim Öffnen der E-Mail weitergegeben werden. 

1. Ziehen Sie einen Empfehlungsblock aus dem Bearbeitungsbereich in den Textkörper Ihrer E-Mail.<br><br>
2. Wählen Sie den gewünschten Algorithmus aus (Popularität, Nutzer:innen-Affinität, Ähnlichkeit und mehr). Je nach ausgewähltem Algorithmus werden zusätzliche Optionen angezeigt: 
  - Wenn Ihre Empfehlung auf der Popularität basiert, können Sie die Ergebnisse mischen, um zu vermeiden, dass der Betrachter dieselbe Empfehlung von verschiedenen E-Mails erhält, die er geöffnet hat.
  - Andere Algorithmen, wie z.B. die Ähnlichkeitsanalyse, stützen sich auf den Kontext, um Empfehlungen auszusprechen, die voraussetzen, dass Sie Artikel auswählen, die aufgenommen werden sollen. Diese Artikel können im Builder hinzugefügt werden, oder [Sie fügen dem eingebetteten Code einen Tag hinzu](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#advanced), um ihn dynamisch zu machen, z.B. um ähnliche Artikel in Versandbestätigungs-E-Mails einzufügen. <br><br>
3. Sie können Produkte ausschließen, die der Nutzer:innen bereits gekauft hat, um diese Produkte nicht zu empfehlen.<br><br>
4. Sie können eine [angepasste Filterregel](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZP4ZWZX1JJ2SH61MB3HVXD) hinzufügen, um bestimmte Produkte an Steckplätze zu binden, oder Produkte nach Produkteigenschaften ein- und ausschließen. Zeigen Sie z.B. keine Produkte mit einem Code von weniger als $5 oder nur Produkte aus der Kategorie Shorts.<br><br>
5. Zum Schluss konfigurieren Sie das Design des Empfehlungsblocks. Wählen Sie dazu ein Template für Artikel aus, legen Sie die Anzahl der anzuzeigenden Artikel fest und bestimmen Sie, in wie vielen Zeilen. 

### Konfigurieren Sie einen dynamischen Content-Block
Verwenden Sie Dynamic Content, um unterschiedliche Aktionen und Nachrichten an verschiedene Nutzer:innen zu richten. Das Targeting kann entweder auf Affinität oder auf Zielgruppe basieren. Der dynamische Ertrag bestimmt, welches personalisierte Erlebnis bei der Öffnung der E-Mail angezeigt werden soll. 

1. Ziehen Sie einen Dynamic Content-Block aus dem Bearbeitungsbereich in den Textkörper Ihrer E-Mail.<br><br> 
2. Wählen Sie ein Template für die erste Variante aus. Sie können jetzt Design- und Inhaltsvariablen definieren. Speichern Sie die Variation, wenn Sie fertig sind. <br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield3.png %})<br><br> 
3. Legen Sie die Zielgruppe im Bereich Dynamischer Content fest.<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield4.png %})<br><br> 
4. Fügen Sie eine weitere Variante hinzu, um eine andere spezifische Zielgruppe oder alle Nutzer:innen anzusprechen. Wiederholen Sie den Vorgang nach Bedarf.<br><br> 
5. Legen Sie die Prioritäten für Ihre Variationen mithilfe der Pfeile nach oben und unten fest. <br><br> 
6. Die Prioritäten bestimmen, welche Variante angeboten wird, wenn ein Nutzer:innen für mehr als ein Erlebnis in Frage kommt.

### Schritt 3: Integrieren Sie Ihre E-Mail mit Braze

Diese Integration erlaubt es Ihnen, personalisierte Empfehlungs-Widgets und dynamischen Content von Dynamic Yield in Ihre Kampagnen von Braze zu integrieren. Das Einbetten dieser Kampagnen in Braze-Kampagnen erfolgt über einen einfachen Einbettungscode, den Sie in den E-Mail-Editor von Braze einfügen.

1. Klicken Sie auf das Symbol ESP Integration auf der Seite Experience E-Mail-Liste.<br><br> 
2. Geben Sie das entsprechende Token von Braze ein, das die CUID und die E-Mail ID der Nutzer:innen einfügt.<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield2_new.png %})
  
Wenn Sie mit Ihrer E-Mail zufrieden sind, generieren Sie im nächsten Schritt den Code zum Einbetten in Braze.
1. Klicken Sie in **Erlebnis-E-Mails** auf **Code generieren**.<br><br> 
2. Klicken Sie anschließend auf **In die Zwischenablage kopieren**.<br>![]({% image_buster /assets/img/dynamic_yield/dynamic_yield.png %})<br><br> 
3. Fügen Sie den Code in Ihre Braze E-Mail-Kampagne ein, und fahren Sie dann mit dem Entwerfen, Testen und Veröffentlichen Ihrer E-Mail-Kampagne fort.


