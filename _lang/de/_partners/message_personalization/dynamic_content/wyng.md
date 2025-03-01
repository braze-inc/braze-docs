---
nav_title: Wyng
article_title: Wyng
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Wyng, einer Zero-Party-Datenplattform, die die Erfassung, Nutzung und Integration von Kundenpräferenzen und -attributen über Micro-Experiences, Kundenpräferenzportale und eine API-Plattform erleichtert."
alias: /partners/wyng/
page_type: partner
search_tag: Partner
---

# Wyng

> Mit [Wyng][0] ist es ganz einfach, interaktive digitale Erlebnisse (d.h. Quiz, Präferenzzentren, Werbeaktionen) zu erstellen, die die Verbraucher im richtigen Moment ansprechen, Präferenzen und andere Daten von Null-Parteien sammeln und in Echtzeit personalisieren.

Die Integration von Braze und Wyng ermöglicht Ihnen die Nutzung von Zero-Party-Daten, die über Wyng-Erfahrungen gesammelt wurden, um Interaktionen in Braze Campaigns und Braze Canvas zu personalisieren. Wyng kann auch ein Präferenzzentrum einrichten, so dass Verbraucher die Daten und Präferenzen (einschließlich der Kommunikationspräferenzen) kontrollieren können, die sie mit Ihrer Marke teilen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Wyng-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Wyng-Konto. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Verbinden Sie die Braze-Integration

In Wyng gehen Sie zu [**Integrationen**][1] und wählen Sie die Registerkarte **Hinzufügen**. Fahren Sie dann mit dem Mauszeiger über **Braze** und klicken Sie auf **Verbinden** für die Integration.

![Die Braze-Partnerkachel in der Wyng-Plattform.][2]{: style="max-width:80%;"}

### Schritt 2: Konfigurieren Sie den Braze-Anschluss

1. In dem sich öffnenden Konfigurationsfenster geben Sie Ihren Braze REST API-Schlüssel an.
![Ein Bild der Eingabeaufforderung für die Anmeldeinformationen.][4]{: style="max-width:80%;"}<br><br>
2. Wählen Sie dann aus der Dropdown-Liste die Wyng-Kampagne aus, die Sie mit Braze teilen möchten.![Ein Bild des Braze-Connectors, das Sie auffordert, eine bestehende Wyng-Kampagne auszuwählen, die Sie mit Braze teilen möchten.][5]{: style="max-width:80%;"}<br><br>
3. Als nächstes müssen Sie Abonnements, Attribut- und Ereignisobjekte sowie benutzerdefinierte Ereignisse einrichten.<br><br>
- **Einrichtung von Abonnements (erforderlich)**<br>
Um Benutzer für Abonnementgruppen zu abonnieren, klicken Sie auf **Abonnement hinzufügen** und fügen den Namen und die ID Ihrer Abonnementgruppe hinzu. Um mehrere Gruppennamen und IDs hinzuzufügen, klicken Sie erneut auf die Schaltfläche **Abonnement hinzufügen**.<br>![Ein Bild, das Sie auffordert, den Namen und die ID einer Abonnementgruppe einzugeben.][8]{: style="max-width:80%;"}<br><br>
- **Einrichtung der Benutzerspur**<br>
Klicken Sie auf **Benutzerdefinierte Eigenschaft hinzufügen**, um Attribut- und Ereignisobjektpaare hinzuzufügen, die an den Endpunkt `/users/track` gesendet werden sollen. Verwenden Sie dies, um für jede Datentransaktion, die für die Integration gesendet wird, fest kodierte Attributwerte hinzuzufügen. Um mehrere Eigenschaften hinzuzufügen, klicken Sie erneut auf die Schaltfläche **Benutzerdefinierte Eigenschaft hinzufügen**.<br>![Ein Bild, das Sie auffordert, benutzerdefinierte Attribute hinzuzufügen.][9]{: style="max-width:80%;"}<br><br>
- **Benutzerdefiniertes Ereignis senden**<br>
Optional können Sie das **Senden von benutzerdefinierten Ereignissen** aktivieren. Falls aktiviert, sollten Sie den Ereignisnamen und die entsprechende App-ID angeben.<br>![Ein Bild, das Sie auffordert, bei Bedarf benutzerdefinierte Ereignisse zu senden.][10]{: style="max-width:80%;"}<br><br>
4. Schließlich müssen Sie die Wyng-Felder den Braze-API-Feldern zuordnen, je nach Ihrem Anwendungsfall. Klicken Sie auf **Feld auswählen**, um die zuzuordnenden Felder auszuwählen, und **speichern** Sie anschließend Ihre Integration. Nach dem Speichern finden Sie diese zugeordneten Felder unter **Integrationen > Verwalten**.
![Ein Beispiel für die verschiedenen Wyng-Felder, die Sie bestimmten Braze-Feldern zuordnen können.][11]{: style="max-width:80%;"}
![Eine Liste der verfügbaren Synchronisationsfelder.][12]{: style="max-width:80%;margin-top:2px"}

### Schritt 3: Testen Sie Ihre Integration

Testen Sie in Wyng das Absenden des Formulars in Ihrer Wyng-Kampagne. Sie können ihn auch in der Vorschaukampagne einreichen, wenn Sie der Hauptproduktionskampagne keinen Datensatz hinzufügen möchten. Sie sollten eine erfolgreiche Transaktion im Dashboard **Integration** sehen.

## Mit dieser Integration

Sobald der Datenkonnektor eingerichtet ist, können alle in Wyng erstellten und zu Braze hinzugefügten Felder wie jedes andere Datenfeld verwendet werden, um Kampagnen auszulösen, Zielgruppen zu segmentieren oder personalisierte Inhalte zu liefern.

Die Anwendungen sind breit gefächert, und spezifische Fragen können Sie an [contact@wyng.com][13] oder an Ihren jeweiligen Kundenbetreuer richten.

## Fehlersuche

### Fehlgeschlagene Einreichung

Im Falle einer fehlgeschlagenen Übertragung klicken Sie beim Senden von Daten an Braze auf den Link **Protokoll anzeigen**, um die fehlgeschlagene Übertragung und die zugehörige Fehlermeldung zu überprüfen.

![Der Link "Protokoll anzeigen" befindet sich unter der Überschrift Aktionen.][14]{: style="max-width:80%;"}

Auf der Protokollseite werden die fehlgeschlagene Übermittlung, die Anzahl der Wiederholungsversuche, die Daten der Übermittlung, der Fehler und ein Link zum erneuten Übermitteln der Übermittlung angezeigt.

![Ein Beispiel dafür, was eine fehlgeschlagene Übermittlung anzeigt.][15]{: style="max-width:80%;"}

Im Abschnitt **Fehler anzeigen** werden der Fehlercode und einige zusätzliche Informationen über die Fehlerursache angezeigt. Sie können dann den Fehlercode mit Braze abgleichen, um die Ursache zu ermitteln.

![Ein Beispiel für ein Fehlerprotokoll, das auf der Wyng-Plattform angezeigt wird.][16]{: style="max-width:80%;"}

Wenn Sie weitere Fragen haben, wenden Sie sich bitte an den Wyng-Support ([support@wyng.com][13]), um Hilfe zu erhalten.

[0]: https://wyng.com/
[1]: https://wyng.com/dashboard/integrations/
[2]: {% image_buster /assets/img/wyng/2.png %}
[3]: {% image_buster /assets/img/wyng/3.png %}
[4]: {% image_buster /assets/img/wyng/4.png %}
[5]: {% image_buster /assets/img/wyng/5.png %}
[6]: {% image_buster /assets/img/wyng/6.png %}
[7]: {{site.baseurl}}/api/basics/
[8]: {% image_buster /assets/img/wyng/8.png %}
[9]: {% image_buster /assets/img/wyng/9.png %}
[10]: {% image_buster /assets/img/wyng/10.png %}
[11]: {% image_buster /assets/img/wyng/11.png %}
[12]: {% image_buster /assets/img/wyng/12.png %}
[13]: mailto:contact@wyng.com
[14]: {% image_buster /assets/img/wyng/14.png %}
[15]: {% image_buster /assets/img/wyng/15.jpg %}
[16]: {% image_buster /assets/img/wyng/16.jpg %}