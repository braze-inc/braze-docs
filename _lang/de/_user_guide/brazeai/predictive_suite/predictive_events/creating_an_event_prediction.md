---
nav_title: Erstellen einer Event-Prognose
article_title: Erstellen einer Event-Prognose
page_order: 1
description: "In diesem Artikel erfahren Sie, wie Sie im Braze-Dashboard eine Event-Prognose erstellen."

---

# Erstellen einer Event-Prognose

> Eine Prognose ist eine Instanz eines trainierten Modells des maschinellen Lernens und aller Parameter und Daten, die es verwendet. Um mehr über prognostizierte Events zu erfahren, lesen Sie die [Übersicht über prognostizierte Events]({{site.baseurl}}/user_guide/brazeai/predictive_suite/predictive_events).

Gehen Sie in Braze zu **Analytics** > **Prädiktive Ereignisse**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Vorhersagen** unter **Engagement**.
{% endalert %}

Auf dieser Seite sehen Sie eine Liste aktueller aktiver Ereignisprognosen und einige grundlegende Informationen über sie. Hier können Sie Vorhersagen umbenennen, archivieren und neue erstellen. Archivierte Vorhersagen sind inaktiv und aktualisieren die Bewertungen der Benutzer nicht.

## Schritt 1: Erstellen Sie eine neue Vorhersage

1. Wählen Sie **Vorhersage erstellen** und wählen Sie eine neue **Ereignisvorhersage**.

{% alert note %}
Es gibt ein Limit von fünf gleichzeitig aktiven Vorhersagen. Vor dem Kauf von prognostizierten Events ist die Grenze bei einer aktiven Vorschauprognose. Eine Vorschauvorhersage aktualisiert nicht regelmäßig die Bewertungen oder die Zielnutzer auf der Grundlage der Ergebnisse der Vorhersage. Kontaktieren Sie Ihren Kundenbetreuer für weitere Informationen.
{% endalert %}

{: start="2"}
2\. Geben Sie Ihrer Vorhersage einen eindeutigen Namen. Sie können auch eine Beschreibung eingeben, um relevante Notizen zu speichern.

![][1]

{: start="3"}
3\. Klicken Sie auf **Weiter**, um zum nächsten Schritt zu gelangen. <br><br>Optional können Sie auf **Jetzt erstellen** klicken, um alle Standardeinstellungen zu verwenden und zum letzten Schritt der Erstellung überzugehen. Sie haben die Möglichkeit, die Einstellungen zu überprüfen, bevor Sie mit dem Erstellungsprozess beginnen. Außerdem können Sie später zu jedem Schritt zurückkehren, indem Sie ihn in der oberen Leiste anklicken.

## Schritt 2: Legen Sie das Tracking von Events fest {#event-tracking}

Geben Sie an, ob die Ereignisse Ihrer Benutzer in Braze als [Kaufereignisse]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/) oder als [benutzerdefinierte Ereignisse]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) gespeichert werden.

Hier sehen Sie, ob die ausgewählte Methode genügend Daten für Braze liefert, um ein Modell des maschinellen Lernens zu erstellen. Wenn die Anforderung nicht erfüllt ist, versuchen Sie, die andere Protokollierungsmethode auszuwählen, wenn diese auch von Ihrer Anwendung verwendet wird. Wenn dies nicht der Fall ist, ist Braze leider nicht in der Lage, mit der Menge der verfügbaren Daten eine Vorhersage zu erstellen. Wenn Sie glauben, dass Sie diesen Fehler fälschlicherweise sehen, wenden Sie sich an Ihren Customer-Success-Manager.

#### Event-Fenster

Das Event-Fenster ist der Zeitrahmen, in dem Sie prognostizieren möchten, ob ein:e Nutzer:in das Event durchführen wird. Es kann bis zu 60 Tage eingestellt werden. In diesem Fenster können Sie historische Daten abfragen, um die Prognose zu trainieren. Nachdem die Vorhersage erstellt wurde und die Benutzer Bewertungen erhalten haben, zeigt die Wahrscheinlichkeitsbewertung an, wie wahrscheinlich es ist, dass ein Benutzer das Ereignis innerhalb der durch das Ereignisfenster festgelegten Anzahl von Tagen ausführt.

### Schritt 3: Filtern Sie Ihre Prognosen-Zielgruppen (optional) {#audience}

Ihre Zielgruppe für die Vorhersage ist die Gruppe von Nutzern, deren Wahrscheinlichkeitswert Sie vorhersagen möchten. Falls gewünscht, können Sie eine Prognose für Ihre gesamte Nutzerpopulation durchführen. Lassen Sie dazu die Standardoption **Alle Benutzer** ausgewählt.

Das Modell erzielt in der Regel eine bessere Performance, wenn Sie die Nutzer:innen, die Sie bewerten möchten, anhand einiger Kriterien filtern. Wählen Sie dazu **Meine eigene Vorhersagezielgruppe definieren** und wählen Sie Ihre Zielgruppenfilter. Sie könnten sich zum Beispiel auf Nutzer konzentrieren, die Ihre App seit mindestens 30 Tagen nutzen, indem Sie den Filter "Erste Nutzung der App" auf 30 Tage setzen.

Die Definition der Zielgruppe für die Vorhersage wird auch zur Abfrage historischer Daten verwendet, damit das maschinelle Lernmodell aus der Vergangenheit lernen kann. Ähnlich wie auf der vorherigen Seite wird die Menge der von diesen Filtern gelieferten Daten zusammen mit der Anforderung angezeigt. Wenn Sie die gewünschte Zielgruppe angeben und das Minimum nicht erreichen, versuchen Sie, einen breiteren Filter anzugeben oder die Option **Alle Benutzer** zu verwenden.

{% alert note %}
Die prognostizierte Zielgruppe darf 100 Millionen Nutzer nicht überschreiten.
{% endalert %}

Wenn das Event-Fenster 14 Tage oder weniger beträgt, kann das Zeitfenster für Filter, die mit "Zuletzt..." beginnen, wie z. B. "Zuletzt verwendete App" und "Zuletzt getätigter Kauf", **das im [Event-Tracking](#event-tracking) angegebene Event-Fenster nicht überschreiten**. Wenn zum Beispiel das Event-Fenster auf 14 Tage eingestellt ist, kann das Zeitfenster für die Filter "Zuletzt..." 14 Tage nicht überschreiten.

#### Alle-Filter-Modus

Um sofort eine neue Prognose erstellen zu können, wird nur eine Teilmenge der Segmentierungsfilter von Braze unterstützt. Im Alle-Filter-Modus können Sie alle Braze-Filter verwenden, benötigen aber ein Event-Fenster, um die Prognose zu erstellen. 

Wenn zum Beispiel das Event-Fenster auf 14 Tage eingestellt ist, dauert es 14 Tage, um die Nutzerdaten zu sammeln und die Prognose zu erstellen, wenn Sie Filter verwenden, die nur im Alle-Filter-Modus unterstützt werden. Außerdem sind einige Schätzungen über die Zuschauerzahlen im Modus Vollständiger Filter nicht verfügbar.

### Schritt 4: Wählen Sie den Aktualisierungszeitplan

Das Modell für maschinelles Lernen, das beim Ausfüllen dieser Seite erstellt wird, wird nach einem Zeitplan, den Sie hier auswählen, verwendet, um neue Scores für die Wahrscheinlichkeit der Nutzer, das Ereignis durchzuführen, zu generieren (Likelihood Score). Wählen Sie die **maximale Häufigkeit der Aktualisierungen**, die Sie für sinnvoll halten. Wenn Sie zum Beispiel Käufe vorhersagen und eine wöchentliche Werbeaktion planen, stellen Sie die Aktualisierungshäufigkeit auf **Wöchentlich** an einem Tag und zu einer Uhrzeit Ihrer Wahl ein.

{% alert note %}
Die Vorschau und die Demo-Vorhersage aktualisieren die Wahrscheinlichkeitswerte der Benutzer nicht.
{% endalert %}

### Schritt 5: Prognose erstellen

Überprüfen Sie, ob Ihre Angaben korrekt sind, und wählen Sie **Prognose erstellen**. Sie können Ihre Änderungen auch in Entwurfsform speichern, indem Sie **Als Entwurf speichern** wählen, um zu dieser Seite zurückzukehren und das Modell später zu erstellen. 

Nachdem Sie auf **Vorhersage erstellen** geklickt haben, beginnt der Prozess zur Erstellung des Modells. Dies kann je nach Datenvolumen zwischen 30 Minuten und einigen Stunden dauern. Für diese Prognose sehen Sie eine Seite, auf der erklärt wird, dass das Training für die Dauer der Modellerstellung im Gange ist.

Wenn Sie fertig sind, wechselt die Seite automatisch in die Analyseansicht und Sie erhalten eine E-Mail, die Sie darüber informiert, dass die Vorhersage und die Ergebnisse fertig sind. Im Falle eines Fehlers kehrt die Seite in den Bearbeitungsmodus zurück und gibt eine Erklärung, was falsch gelaufen ist.

Die Vorhersage wird alle **zwei Wochen** automatisch neu erstellt ("trainiert"), um sie auf dem neuesten Stand der verfügbaren Daten zu halten. Beachten Sie, dass dies ein anderer Prozess ist als die Erstellung der Nutzerwahrscheinlichkeits-Scores, die das Ergebnis der Prognose sind. Letzteres hängt von der Häufigkeit der Updates ab, die Sie in Schritt 4 gewählt haben.

## Archivierte Vorhersagen

Bei archivierten Vorhersagen werden die Benutzerbewertungen nicht mehr aktualisiert. Alle archivierten Prognosen, die nicht archiviert sind, aktualisieren die Nutzer:innen weiterhin nach einem festgelegten Zeitplan. Archivierte Vorhersagen werden nie gelöscht und bleiben in der Liste.

[1]: {% image_buster /assets/img/purchasePrediction/purchases_step1.png %}

