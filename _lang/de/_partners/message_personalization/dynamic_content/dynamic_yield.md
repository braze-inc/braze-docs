---
nav_title: Dynamic Yield
article_title: Dynamic Yield
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Dynamic Yield. Diese Partnerschaft ermöglicht es Ihnen, die Empfehlungs- und Segmentierungs-Engine von Dynamic Yield zu nutzen, um Experience Blocks zu erstellen, die in Braze-Nachrichten eingebettet werden können."
alias: /partners/dynamic_yield/
page_type: partner
search_tag: Partner

---

# Dynamic Yield

> [Dynamic Yield](https://www.dynamicyield.com/), ein Unternehmen von Mastercard, hilft Unternehmen aller Branchen, digitale Kundenerlebnisse zu liefern, die personalisiert, optimiert und synchronisiert sind. Mit dem [Experience OS](http://www.dynamicyield.com/experience-os) von Dynamic Yield können Vermarkter, Produktmanager, Entwickler und digitale Teams Inhalte, Produkte und Angebote algorithmisch auf jeden Kunden abstimmen, um den Umsatz zu steigern und die Kundenbindung zu erhöhen.

Die Partnerschaft zwischen Braze und Dynamic Yield ermöglicht es Ihnen, die Empfehlungs- und Segmentierungs-Engine von Dynamic Yield zu nutzen, um Experience Blocks zu erstellen, die in Braze-Nachrichten eingebettet werden können. Erfahrungsblöcke können aus:
- **Empfehlungsblöcke**: Stellen Sie Algorithmen und Filter ein, um die personalisierten Inhalte der Benutzer zu ermitteln, die beim Öffnen der E-Mail weitergegeben werden. 
- **Dynamische Inhaltsblöcke**: Richten Sie verschiedene Werbeaktionen und Nachrichten an verschiedene Benutzer. Das Targeting kann entweder auf Affinität oder auf Zielgruppe basieren. Dynamic Yield bestimmt, welches personalisierte Erlebnis beim Öffnen der E-Mail angezeigt werden soll. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Dynamisches Renditekonto | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein [Dynamic Yield-Konto](https://adm.dynamicyield.com/users/sign_in#/r/dashboard) erforderlich. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Einen Erlebnisblock erstellen

Um einen Erlebnisblock in Dynamic Yield zu erstellen, navigieren Sie zu **E-Mail > Erlebnis-E-Mails > Neu erstellen**.

Wählen Sie dann **Erlebnisblock erstellen**, um einen Block mit dynamischen Inhalten oder Empfehlungen zu entwerfen, der in eine Braze-E-Mail-Vorlage eingebettet wird.<br>![][8]

### Schritt 2: Entwerfen Sie Ihre Botschaften

Das folgende Bild zeigt eine von Grund auf neu erstellte E-Mail im Builder.<br>![][6]

1. Geben Sie einen Kampagnennamen, eine Notiz und Bezeichnungen für die Kampagne in den Überschriftenbereich ein.<br><br>
2. Fügen Sie einen Erfahrungsblock ein. Diese Blöcke umfassen:
  - [Empfehlungen](#configure-a-recommendations-block): Ein Widget, das den Benutzern vollständig personalisierte Empfehlungen bietet.
  - [Dynamischer Inhalt](#configure-a-dynamic-content-block): Richten Sie unterschiedliche Werbeaktionen und Botschaften an unterschiedliche Zielgruppen.<br><br>
3. Einstellungen aktualisieren:
  - Verwenden Sie die URL-Parameter, um Klicks in Ihrer Analysesoftware zu verfolgen (optional). Fügen Sie bei Bedarf Parameter zu den Standardanzeigen hinzu.
  - Wählen Sie ein Attributfenster, entweder sieben Tage (Standard) oder einen Tag.<br><br>
4. Speichern und beenden. Sie können jederzeit zurückkehren, um alle Elemente Ihrer E-Mail zu bearbeiten, bevor der Code generiert wird. Nachdem der Code generiert wurde, können Sie alles bearbeiten, was den [Code nicht beeinflusst](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZPXB6MH094J1MWS5N86FXH).

### Konfigurieren Sie einen Empfehlungsblock

Mit dem Empfehlungsblock können Sie Algorithmen und Filter festlegen, um personalisierte Inhalte für Benutzer zu erstellen, die beim Öffnen der E-Mail weitergegeben werden. 

1. Ziehen Sie einen Empfehlungsblock aus dem Bearbeitungsbereich in den Textkörper Ihrer E-Mail.<br><br>
2. Wählen Sie den gewünschten Algorithmus (Popularität, Benutzeraffinität, Ähnlichkeit und mehr). Je nach ausgewähltem Algorithmus werden zusätzliche Optionen angezeigt: 
  - Wenn Ihre Empfehlung auf der Beliebtheit basiert, können Sie die Ergebnisse mischen, um zu vermeiden, dass der Betrachter dieselbe Empfehlung aus verschiedenen E-Mails öffnet.
  - Andere Algorithmen, wie z.B. die Ähnlichkeitsanalyse, stützen sich auf den Kontext, um Empfehlungen auszusprechen, und verlangen, dass Sie die zu berücksichtigenden Objekte auswählen. Diese Elemente können im Builder hinzugefügt werden, oder [Sie fügen dem Einbettungscode ein Merge-Tag hinzu](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#advanced), um ihn dynamisch zu machen, z. B. um ähnliche Elemente in Versandbestätigungs-E-Mails einzufügen. <br><br>
3. Sie können Produkte ausschließen, die der Benutzer bereits gekauft hat, um zu vermeiden, dass diese Produkte empfohlen werden.<br><br>
4. Sie können eine [benutzerdefinierte Filterregel](https://support.dynamicyield.com/hc/en-us/articles/4404013832465-Experience-Email#h_01FAZP4ZWZX1JJ2SH61MB3HVXD) hinzufügen, um bestimmte Produkte an Slots zu binden, oder Produkte nach Produkteigenschaften ein- und ausschließen. Zeigen Sie z.B. keine Produkte mit einem Code von weniger als $5 oder nur Produkte aus der Kategorie Shorts.<br><br>
5. Zum Schluss konfigurieren Sie das Design des Empfehlungsblocks. Wählen Sie dazu eine Artikelvorlage aus, legen Sie die Anzahl der anzuzeigenden Artikel fest und bestimmen Sie, in wie vielen Zeilen. 

### Einen dynamischen Inhaltsblock konfigurieren
Verwenden Sie dynamische Inhalte, um verschiedene Werbeaktionen und Nachrichten an verschiedene Benutzer zu richten. Das Targeting kann entweder auf Affinität oder auf Zielgruppe basieren. Dynamic Yield bestimmt, welches personalisierte Erlebnis beim Öffnen der E-Mail angezeigt werden soll. 

1. Ziehen Sie einen dynamischen Inhaltsblock aus dem Bearbeitungsbereich in den Textkörper Ihrer E-Mail.<br><br> 
2. Wählen Sie eine Vorlage für die erste Variante. Sie können jetzt Design- und Inhaltsvariablen definieren. Speichern Sie die Variation, wenn Sie fertig sind. <br>![][4]<br><br> 
3. Legen Sie die Zielgruppe im Fensterbereich Dynamischer Inhalt fest.<br>![][5]<br><br> 
4. Fügen Sie eine weitere Variante hinzu, um eine andere spezielle Zielgruppe oder alle Nutzer anzusprechen. Wiederholen Sie den Vorgang nach Bedarf.<br><br> 
5. Legen Sie die Prioritäten für Ihre Variationen mithilfe der Pfeile nach oben und unten fest. <br><br> 
6. Die Prioritäten bestimmen, welche Variante angeboten wird, wenn ein Nutzer für mehr als ein Erlebnis in Frage kommt.

### Schritt 3: Integrieren Sie Ihre E-Mail mit Braze

Diese Integration ermöglicht es Ihnen, personalisierte Empfehlungs-Widgets und dynamische Inhalte von Dynamic Yield in Ihre Braze-E-Mail-Kampagnen einzubinden. Das Einbetten dieser Kampagnen in Braze-Kampagnen erfolgt über einen einfachen Einbettungscode, den Sie in den Braze-E-Mail-Editor einfügen.

1. Klicken Sie auf das Symbol ESP-Integration auf der Seite mit der Experience-E-Mail-Liste.<br><br> 
2. Geben Sie das entsprechende Token von Braze ein, das die CUID und die E-Mail-ID des Benutzers einfügt.<br>![][3]
  
Wenn Sie mit Ihrer E-Mail zufrieden sind, generieren Sie im nächsten Schritt den Code zum Einbetten in Braze.
1. Klicken Sie unter **Erlebnis-E-Mails** auf **Code generieren**.<br><br> 
2. Klicken Sie anschließend auf **In die Zwischenablage kopieren**.<br>![][1]<br><br> 
3. Fügen Sie den Code in Ihre Braze-E-Mail-Kampagne ein, und fahren Sie dann mit der Gestaltung, dem Testen und der Veröffentlichung Ihrer E-Mail-Kampagne fort.


[1]: {% image_buster /assets/img/dynamic_yield/dynamic_yield.png %}
[2]: {% image_buster /assets/img/dynamic_yield/dynamic_yield1.png %}
[3]: {% image_buster /assets/img/dynamic_yield/dynamic_yield2_new.png %}
[4]: {% image_buster /assets/img/dynamic_yield/dynamic_yield3.png %}
[5]: {% image_buster /assets/img/dynamic_yield/dynamic_yield4.png %}
[6]: {% image_buster /assets/img/dynamic_yield/dynamic_yield5.png %}
[7]: {% image_buster /assets/img/dynamic_yield/dynamic_yield6.png %}
[8]: {% image_buster /assets/img/dynamic_yield/dynamic_yield7.png %}
