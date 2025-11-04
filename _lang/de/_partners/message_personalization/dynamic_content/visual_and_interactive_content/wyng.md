---
nav_title: Wyng
article_title: Wyng
description: "Dieser Artikel referenziert die Partnerschaft zwischen Braze und Wyng, einer Zero-Party-Datenplattform, die die Erfassung, Nutzung und Integration von Kundenpräferenzen und Attributen über Micro-Experiences, Kundenpräferenzportale und eine API-Plattform erleichtert."
alias: /partners/wyng/
page_type: partner
search_tag: Partner
---

# Wyng

> [Wyng](https://wyng.com/) macht es Ihnen leicht, interaktive digitale Erlebnisse (d.h. Quiz, Präferenzzentren, Aktionen) zu erstellen, die Verbraucher:in den richtigen Momenten einbinden, Präferenzen und andere Zero-Party-Daten erfassen und in Realtime personalisieren.

_Diese Integration wird von Wyng gepflegt._

## Über die Integration

Die Integration von Braze und Wyng erlaubt es Ihnen, Zero-Party-Daten, die über Wyng-Erfahrungen gewonnen wurden, zu nutzen, um Interaktionen in Braze-Kampagnen und Braze-Canvas zu personalisieren. Wyng kann auch ein Präferenzzentrum betreiben, so dass Verbraucher:in die Lage versetzt werden, die Daten und Präferenzen (einschließlich der Kommunikationspräferenzen) zu kontrollieren, die sie mit Ihrer Marke teilen.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Wyng-Konto | Um diese Partnerschaft nutzen zu können, benötigen Sie ein Wyng-Konto. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.track` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Verbinden Sie die Braze Integration

Gehen Sie in Wyng zu [**Integrationen**](https://wyng.com/dashboard/integrations/) und wählen Sie den Tab **Hinzufügen**. Bewegen Sie dann den Mauszeiger über **Braze** und klicken Sie auf **Verbinden** für die Integration.

![Die Braze Partner-Kachel in der Wyng Plattform.]({% image_buster /assets/img/wyng/2.png %}){: style="max-width:80%;"}

### Schritt 2: Konfigurieren Sie den Braze-Konnektor

1. Geben Sie in dem sich öffnenden Konfigurationsfenster Ihren Braze REST API-Schlüssel an.
![Ein Bild, das zeigt, wie die Eingabeaufforderung für die Zugangsdaten aussieht.]({% image_buster /assets/img/wyng/4.png %}){: style="max-width:80%;"}<br><br>
2. Wählen Sie dann aus der Dropdown-Liste die Wyng-Kampagne aus, die Sie mit Braze teilen möchten.![Ein Bild des Konnektors von Braze, der Sie auffordert, eine bestehende Wyng-Kampagne auszuwählen, die Sie mit Braze teilen möchten.]({% image_buster /assets/img/wyng/5.png %}){: style="max-width:80%;"}<br><br>
3. Als nächstes müssen Sie Abonnements, Attribute und Ereignisobjekte sowie angepasste Events einrichten.<br><br>
- **Einrichtung von Abos (erforderlich)**<br>
Um Nutzer:innen für Abo-Gruppen zu abonnieren, klicken Sie auf **Abonnement hinzufügen** und fügen Sie den Namen und die ID Ihrer Abo-Gruppe hinzu. Um mehrere Gruppennamen und IDs hinzuzufügen, klicken Sie erneut auf den Button **Abonnement hinzufügen**.<br>![Ein Bild, das Sie auffordert, den Namen und die ID einer Abo-Gruppe einzugeben.]({% image_buster /assets/img/wyng/8.png %}){: style="max-width:80%;"}<br><br>
- **Nutzer:innen Tracking einrichten**<br>
Klicken Sie auf **Angepasste Eigenschaft hinzufügen**, um Attribut- und Ereignisobjektpaare hinzuzufügen, die an den Endpunkt `/users/track` gesendet werden sollen. Verwenden Sie diese Option, um fest kodierte Attributwerte für jede Datentransaktion hinzuzufügen, die für die Integration gesendet wird. Um mehrere Eigenschaften hinzuzufügen, klicken Sie erneut auf den Button **Angepasste Eigenschaft hinzufügen**.<br>![Ein Bild, das Sie auffordert, angepasste Attribute Eigenschaften hinzuzufügen.]({% image_buster /assets/img/wyng/9.png %}){: style="max-width:80%;"}<br><br>
- **Angepasstes Event senden**<br>
Optional können Sie das **Senden von angepassten Events** aktivieren. Falls aktiviert, sollten Sie den Ereignisnamen und die entsprechende App ID angeben.<br>![Ein Bild, das Sie auffordert, angepasste Events zu senden, falls erforderlich.]({% image_buster /assets/img/wyng/10.png %}){: style="max-width:80%;"}<br><br>
4. Schließlich müssen Sie die Wyng-Felder auf der Grundlage Ihres Anwendungsfalls den Braze API-Feldern zuordnen. Klicken Sie auf **Feld auswählen**, um die Felder auszuwählen, die Sie abbilden möchten, und **speichern Sie** anschließend Ihre Integration. Wenn Sie diese Abbildungen gespeichert haben, finden Sie diese Felder unter **Integrationen > Verwalten.**
![Ein Beispiel für die verschiedenen Wyng-Felder, die Sie bestimmten Braze-Feldern zuordnen können.]({% image_buster /assets/img/wyng/11.png %}){: style="max-width:80%;"}
![Eine Liste der verfügbaren Synchronisationsfelder.]({% image_buster /assets/img/wyng/12.png %}){: style="max-width:80%;margin-top:2px"}

### Schritt 3: Testen Sie Ihre Integration

Testen Sie in Wyng, ob Sie das Formular in Ihrer Kampagne in Wyng abschicken können. Sie können es auch in der Vorschau-Kampagne einreichen, wenn Sie der Hauptproduktionskampagne keinen Datensatz hinzufügen möchten. Sie sollten im Dashboard **Integration** eine erfolgreiche Transaktion sehen.

## Verwendung dieser Integration

Sobald der Konnektor eingerichtet ist, können alle in Wyng erstellten und zu Braze hinzugefügten Felder wie jedes andere Datenfeld verwendet werden, um Kampagnen zu triggern, Zielgruppen zu segmentieren oder personalisierte Inhalte einzuspeisen.

Die Anwendungen sind breit gefächert, und spezifische Fragen können Sie an [contact@wyng.com](mailto:contact@wyng.com) oder an Ihren spezifischen Account Manager:in richten.

## Fehlersuche

### Einreichung fehlgeschlagen

Im Falle einer fehlgeschlagenen Übermittlung klicken Sie beim Senden von Daten an Braze auf den Link **Protokoll anzeigen**, um die fehlgeschlagene Übermittlung und die zugehörige Fehlermeldung zu überprüfen.

![Der Link "Protokoll anzeigen" befindet sich unter der Überschrift Aktionen.]({% image_buster /assets/img/wyng/14.png %}){: style="max-width:80%;"}

Auf der Protokollseite werden die fehlgeschlagene Übermittlung, die Anzahl der Wiederholungsversuche, die Daten der Übermittlung, der Fehler und ein Link zum erneuten Push der Übermittlung angezeigt.

![Ein Beispiel dafür, was eine fehlgeschlagene Übermittlung anzeigt.]({% image_buster /assets/img/wyng/15.jpg %}){: style="max-width:80%;"}

Im Bereich **Fehler anzeigen** werden der Fehlercode und einige zusätzliche Informationen über die Fehlerursache angezeigt. Sie können dann den Fehlercode mit Braze referenzieren, um die Ursache zu ermitteln.

![Ein Beispiel für ein Fehlerprotokoll auf der Wyng Plattform.]({% image_buster /assets/img/wyng/16.jpg %}){: style="max-width:80%;"}

Sollten Sie weitere Fragen haben, wenden Sie sich bitte an den Wyng-Support ([support@wyng.com](mailto:contact@wyng.com)), um Hilfe zu erhalten.


