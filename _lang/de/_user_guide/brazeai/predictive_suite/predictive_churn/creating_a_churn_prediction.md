---
nav_title: Erstellen Sie eine Prognose für die Abwanderung
article_title: Erstellen Sie eine Prognose für die Abwanderung
description: "Dieser Artikel beschreibt, wie Sie im Braze-Dashboard eine Prognose zur Abwanderung erstellen."
page_order: 1.1

---

# Erstellen Sie eine Prognose für die Abwanderung

> Erfahren Sie, wie Sie im Braze-Dashboard eine Prognose zur Abwanderung erstellen können.

## Schritt 1: Erstellen Sie eine neue Vorhersage

Gehen Sie in Braze zu **Analytics** > **Predictive Churn**.

Eine Prognose ist eine Instanz eines trainierten Modells des maschinellen Lernens und aller Parameter und Daten, die es verwendet. Auf dieser Seite sehen Sie eine Liste aktueller aktiver Vorhersagen zusammen mit einigen grundlegenden Informationen über sie. Hier können Sie Vorhersagen umbenennen, archivieren und neue erstellen. Archivierte Vorhersagen sind inaktiv und aktualisieren die Bewertungen der Benutzer nicht. 

Um eine neue Vorhersage zu erstellen, wählen Sie **Vorhersage erstellen** und wählen eine neue **Churn-Vorhersage**.

{% alert note %}
Es gibt eine Obergrenze von fünf gleichzeitig aktiven Prognosen zur Abwanderung. Vor dem Erwerb von Predictive Churn ist die Anzahl der aktiven Vorschau-Prognosen für die voraussichtliche Abwanderung auf eine begrenzt. Eine Abwanderungsvorhersage in der Vorschau aktualisiert die Ergebnisse nicht regelmäßig und ermöglicht es Ihnen nicht, Benutzer auf der Grundlage der Vorhersage anzusprechen. Kontaktieren Sie Ihren Kundenbetreuer für weitere Informationen.
{% endalert %}

Auf der Seite **Grundlagen** geben Sie Ihrer neuen Vorhersage einen eindeutigen Namen. Sie können auch eine optionale Beschreibung eingeben, um sich Notizen zu dieser speziellen Vorhersage zu machen.

Bitte wählen Sie **„Weiter“,** um zum nächsten Schritt zu gelangen. Alternativ können Sie **„Jetzt erstellen“** auswählen, um alle Standard-Einstellungen zu verwenden und zum letzten Schritt der Erstellung zu gelangen. Sie haben die Möglichkeit, die Einstellungen zu überprüfen, bevor Sie den Erstellungsprozess starten. Sie können zu jedem Schritt zurückkehren, indem Sie ihn im Fortschrittsbalken auswählen.

## Schritt 2: Definieren Sie abwandern

Verwenden Sie im Bereich **Abwanderungsdefinition** die bereitgestellten Filter, um festzulegen, wie Sie die Benutzerabwanderung für Ihr Unternehmen definieren. Mit anderen Worten: Was muss ein:e Nutzer:in in welchem Zeitraum tun, damit Sie sie:ihn als abgewandert betrachten?

Denken Sie daran, dass Sie nicht erklären müssen, welche Verhaltensweisen dem Abwandern vorausgehen, sondern nur, was eine:n Nutzer:in zu einer abgewanderten Nutzerin oder einem abgewanderten Nutzer macht. Stellen Sie sich das so vor, dass ein:e Nutzer:in etwas abwandern kann, das sie:er entweder einmal tut (`do`) oder nicht mehr tut (`do not`). Sie könnten zum Beispiel Nutzer:innen, die Ihre App seit 7 Tagen nicht mehr geöffnet haben, als abgewandert betrachten. Sie können die Deinstallation oder angepasste Events wie die Abmeldung, die Deaktivierung eines Kontos oder andere in Betracht ziehen, um eine:n Nutzer:in abwandern zu lassen. 

#### Abwanderungsfenster

Das Abwanderungsfenster ist der Zeitraum, in dem die Aktivität einer Nutzer:in die Kriterien für das Abwandern erfüllt. Sie können es je nach verfügbaren Daten für bis zu 60 Tage einstellen. Dieses Fenster dient dazu, historische Daten abzurufen, um Ihre Prognose zu trainieren. Sobald die Prognose erstellt ist, können Sie feststellen, ob ausreichend Daten für genaue Ergebnisse vorhanden waren.

Nachdem die Prognose erstellt wurde und die Nutzer:innen ihre Bewertungen erhalten haben, zeigt der _Churn-Risiko-Score_ an, wie wahrscheinlich es ist, dass eine Nutzer:in innerhalb des von Ihnen im Churn-Fenster festgelegten Zeitraums abwandert. 

Hier ein Beispiel für eine einfache Definition auf der Grundlage der verstrichenen Sitzungen der letzten 7 Tage.

![Abwanderungsdefinition: Ein:e Nutzer:in gilt als abgewandert, wenn sie:er innerhalb von 7 Tagen keine Sitzung beginnt]({% image_buster /assets/img/churn/churn1.png %})

Für diesen Fall wählen wir `do not` und `start a session` aus. Sie können andere Filter mit `AND` und `OR` nach Belieben kombinieren, um die von Ihnen gewünschte Definition zu erstellen. Interessieren Sie sich für einige mögliche Definitionen des Abwanderns, die Sie berücksichtigen sollten? Im folgenden Abschnitt über die [Definition von Abwanderung](#sample-definitions) finden Sie einige Anregungen.

{% alert note %}
Für nehmen `do`wir an, dass aktive Nutzer:innen die von Ihnen für diese Zeile angegebene Aktion nicht durchgeführt haben, bevor sie abgewandert sind. Diese Aktion führt zu Abwanderung. <br><br>Für betrachten`do not` wir aktive Nutzer:innen als diejenigen, die diese Aktion in den Tagen zuvor durchgeführt haben und dann damit aufgehört haben. <br><br>**Beispiel:** Wenn Abwanderung als „hat in den letzten 60 Tagen keinen Kauf getätigt” definiert wird, betrachten wir diejenigen als aktive:e Nutzer:innen, die in den letzten 60 Tagen einen Kauf getätigt haben. Daher wird jeder, der in den letzten 60 Tagen keinen Kauf getätigt hat, nicht als aktive:r Nutzer:in betrachtet. Dies bedeutet, dass eine anhand dieser Abwanderungsdefinition erstellte Abwanderungszielgruppe nur Nutzer:innen umfasst, die in den letzten 60 Tagen einen Kauf getätigt haben. Dies kann dazu führen, dass die resultierende Zielgruppe für die voraussichtliche Abwanderung deutlich kleiner erscheint als die ursprüngliche Population – die meisten Nutzer:innen in einem Workspace könnten bereits die Definition für Abwanderung erfüllen und daher in der Prognose zur voraussichtlichen Abwanderung nicht aktiv sein.
{% endalert %}

Unterhalb der Definition sehen Sie Schätzungen darüber, wie viele Nutzer:innen (die in der Vergangenheit abgewandert sind und die nach Ihrer Definition nicht abgewandert sind) verfügbar sind. Sie sehen auch die erforderlichen Mindestwerte. Braze muss über diese Mindestanzahl von Nutzer:innen in den historischen Daten verfügen, damit die Prognosen über genügend Daten verfügen, um daraus zu lernen.

## Schritt 3: Filtern Sie Ihre Prognosen-Zielgruppen

Ihre Prognosegruppe ist die Gruppe der Nutzer:innen, für die Sie das Abwanderungsrisiko prognostizieren möchten. Die Zielgruppe der Prognosen definiert die Gruppe der Nutzer:innen, die das Modell des maschinellen Lernens betrachtet, um aus der Vergangenheit zu lernen. Standardmäßig ist diese Option auf **„Alle Nutzer:innen“** eingestellt, was bedeutet, dass diese Prognose Abwanderungsrisikowerte für alle Ihre aktiven Nutzer:innen erstellt (Informationen dazu, wer für ein Abwanderungsmodell als aktiv gilt, finden Sie im vorherigen Hinweis).

Je nach Anwendungsfall können Sie Filter verwenden, um die Nutzer:innen anzugeben, die Sie für das Modell bewerten möchten. Wählen Sie dazu **Meine eigene Vorhersagezielgruppe definieren** und wählen Sie Ihre Zielgruppenfilter. Wenn Sie beispielsweise eine Mitfahr-App mit Fahrern und Fahrgästen in Ihrer Nutzerbasis betreiben und ein Churn-Modell für Fahrgäste erstellen, sollten Sie Ihre Prognosegruppe auf Fahrgäste beschränken. Bitte beachten Sie, dass es in vielen Anwendungsfällen nicht erforderlich ist, eine bestimmte Zielgruppe für die Prognosen auszuwählen. Wenn Ihr Anwendungsfall beispielsweise darin besteht, eine Zielgruppe aus Nutzern in der EU-Region zusammenzustellen, bei denen die Wahrscheinlichkeit des Abwanderns am höchsten ist, können Sie Ihr Modell auf alle Nutzer:innen anwenden und dann einfach einen Filter für die EU-Region in das Segment der Kampagne einfügen.

Braze zeigt Ihnen die geschätzte Größe Ihrer Prognose-Zielgruppe an. Wenn Sie Ihre gewünschte Zielgruppe angeben und die Mindestanforderungen für die Ausführung des Modells nicht erfüllen, versuchen Sie bitte, einen breiteren Filter anzugeben, oder verwenden Sie die Option **„Alle Nutzer:innen**“. Bitte beachten Sie, dass die Größe Ihrer Gruppe „Alle Nutzer:innen” nicht statisch ist und von Modell zu Modell variiert, da sie Ihre Definition der Nutzer:innen, die abwandern, berücksichtigt. Angenommen, die Definition für Abwanderung lautet, dass innerhalb von 30 Tagen **kein** Kauf getätigt wurde. In diesem Fall wendet Braze das Modell auf Nutzer:innen an, die in den letzten 30 Tagen einen Kauf getätigt **haben** (und prognostiziert die Wahrscheinlichkeit, dass sie in den nächsten 30 Tagen **keinen** Kauf tätigen werden). Diese Nutzer:innen werden dann in der Metrik „Alle Nutzer:innen” berücksichtigt.

{% alert note %}
Die prognostizierte Zielgruppe darf 100 Millionen Nutzer nicht überschreiten.
{% endalert %}

Wenn das Vorhersagefenster 14 Tage oder weniger beträgt, **darf** das Zeitfenster für Filter, die mit „Zuletzt ...” beginnen, wie „Zuletzt verwendete App” und „Zuletzt getätigter Kauf”, **das** in der Churn-Definition **angegebene Churn-Fenster nicht überschreiten**. Wenn Ihre Churn-Definition beispielsweise ein Zeitfenster von 14 Tagen hat, darf das Zeitfenster für die Filter "Letzte..." 14 Tage nicht überschreiten. 

Das Abwanderungsfenster wird anhand der Anzahl der Tage seit dem letzten Ausführen des Modells berechnet. Wenn das Abwanderungsfenster also 15 Tage beträgt und das Modell zuletzt am 1\. Dezember ausgeführt wurde, analysiert das Modell den Zeitraum vom 16\. bis zum 30\. November, um die Nutzeraktivität für die Zielgruppenberechtigung und das Training zu erfassen.

#### Alle-Filter-Modus

Um umgehend eine neue Prognose zu erstellen, wird nur eine Teilmenge der Braze-Filter für die Segmentierung unterstützt. Im Alle-Filter-Modus können Sie alle Braze-Filter verwenden, jedoch ist ein Churn-Fenster erforderlich, um die Prognose zu erstellen. Wenn das Abwanderungsfenster beispielsweise auf 15 Tage eingestellt ist, dauert es 15 Tage, um die Nutzerdaten zu sammeln und die Prognose zu erstellen, wenn Sie Filter verwenden, die nur im Alle-Filter-Modus unterstützt werden. Außerdem sind einige Schätzungen über die Zuschauerzahlen im Modus Vollständiger Filter nicht verfügbar.

Eine Beispielliste mit Definitionen für die Vorhersagezielgruppe finden Sie im folgenden Abschnitt über [Beispieldefinitionen für Abwanderung](#sample-definitions).

![]({% image_buster /assets/img/churn/churn5.png %})

Genau wie auf der vorherigen Seite sehen Sie im unteren Bereich die geschätzte Anzahl der historischen Nutzer, die sich aus der Definition der Abwanderung und der Definition der Vorhersagezielgruppe ergibt. Diese Schätzungen müssen die angegebenen Mindestanforderungen erfüllen, um eine Prognose erstellen zu können.

## Schritt 4: Wählen Sie die Update-Häufigkeit für die Prognose der Abwanderung

Das maschinelle Lernen generiert Ereigniswahrscheinlichkeitswerte für Nutzer:innen, und diese Werte werden auf Grundlage des hier ausgewählten Zeitplans aktualisiert. Sie können Nutzer:innen anhand ihres Ereigniswahrscheinlichkeitswerts gezielt ansprechen. 

Wählen Sie die **maximale Häufigkeit der Aktualisierungen**, die Sie für sinnvoll halten. Wenn Sie z. B. eine wöchentliche Werbeaktion versenden möchten, um zu verhindern, dass Benutzer abwandern, stellen Sie die Aktualisierungshäufigkeit auf **Wöchentlich** an einem Tag und zu einer Uhrzeit Ihrer Wahl ein. 

![Der Zeitplan für das Update der Prognosen ist auf täglich um 17 Uhr eingestellt.]({% image_buster /assets/img/churn/churn2.png %})

{% alert note %}
Die Vorschau und die Demo-Prognose werden das Abwanderungsrisiko der Nutzer:innen niemals aktualisieren. Darüber hinaus erfordern tägliche Updates für Vorhersagen einen zusätzlichen Kauf im Vergleich zu wöchentlichen oder monatlichen Updates mit Predictive Churn. Um diese Funktionalität zu erwerben, wenden Sie sich an Ihren Account Manager.
{% endalert %}

## Schritt 5: Prognose erstellen

Überprüfen Sie, ob Ihre Angaben korrekt sind, und wählen Sie **Prognose erstellen**. Sie können Ihre Änderungen auch in Entwurfsform speichern, indem Sie **Als Entwurf speichern** wählen, um zu dieser Seite zurückzukehren und das Modell später zu erstellen. Nachdem Sie **„Prognose erstellen“** ausgewählt haben, beginnt der Prozess zur Generierung des Modells. Dies kann je nach Datenvolumen zwischen 30 Minuten und einigen Stunden dauern. Für diese Prognose wird eine Seite angezeigt, auf der erläutert wird, dass während des Modellbildungsprozesses das Modell trainiert wird. Das Braze-Modell berücksichtigt angepasste Events, Kauf-Events, Kampagneninteraktionsereignisse und Sitzungsdaten.

Nach Abschluss des Vorgangs wechselt die Seite automatisch zur Analytics-Ansicht, und Sie erhalten eine E-Mail, die Sie darüber informiert, dass die Prognose und die Ergebnisse verfügbar sind. Im Falle eines Fehlers kehrt die Seite in den Bearbeitungsmodus zurück und gibt eine Erklärung, was schief gelaufen ist.

Die Vorhersage wird alle **zwei Wochen automatisch** neu aufgebaut ("retrainiert"), um sie auf der Grundlage der neuesten verfügbaren Daten auf dem neuesten Stand zu halten. Beachten Sie, dass dies ein anderer Prozess ist als die Erstellung der _Churn Risk Scores_ der Benutzer, die das Ergebnis der Vorhersage sind. Letzteres hängt von der Häufigkeit der Updates ab, die Sie in Schritt 4 gewählt haben.

## Definitionen für voraussichtliche Abwanderung und Prognosen der Zielgruppe {#sample-definitions}

**Beispiele für Churn-Definitionen**<br>
- "Innerhalb von 7 Tagen ein angepasstes Event 'Abo-Kündigung' durchführen"<br>
- "Machen Sie innerhalb von 30 Tagen ein angepasstes Event 'Probezeit abgelaufen'"<br>
- "Innerhalb von 1 Tag deinstallieren." <br>
- "Innerhalb von 14 Tagen keinen Kauf tätigen." <br>

Für die von uns skizzierten Definitionen der Abwanderung gibt es möglicherweise auch entsprechende Definitionen für Prognosen der Zielgruppen:<br>
- **Sie haben das Abonnement vor mehr als 2 Wochen begonnen ODER Sie haben das Abonnement vor weniger als zwei Wochen begonnen**<br>Vielleicht möchten Sie in diesem Fall 2 Prognosen erstellen und neuen Abonnent:innen dann andere Nachrichten schicken als längerfristigen Abonnent:innen. Sie könnten dies auch als "Erster getätigter Kauf vor mehr als 30 Tagen" definieren.<br>
- **Deinstallationsprogramme**<br>Sie könnten sich auf Kunden konzentrieren, die in der jüngsten Vergangenheit etwas gekauft oder die App erst kürzlich genutzt haben.<br>
- **Diejenigen, die Gefahr laufen, nicht zu kaufen, als Definition von Abwandern**<br>Sie möchten sich möglicherweise auf Kunden konzentrieren, die kürzlich Ihre App besucht, darin gesucht oder mit ihr interagiert haben. Vielleicht kann die richtige Rabattaktion die Abwanderung dieser engagierten Gruppe verhindern.

## Archivierte Vorhersagen

Bei archivierten Vorhersagen werden die Benutzerbewertungen nicht mehr aktualisiert. Alle archivierten Prognosen, die nicht archiviert sind, aktualisieren die Nutzer:innen weiterhin nach einem festgelegten Zeitplan. Archivierte Vorhersagen werden nie gelöscht und bleiben in der Liste.


