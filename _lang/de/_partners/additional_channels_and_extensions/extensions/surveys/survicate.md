---
nav_title: Survicate
article_title: Survicate
description: "Dieser referenzierende Artikel beschreibt die Partnerschaft zwischen Braze und Survicate, einer Plattform für Kundenfeedback, die Ihnen hilft, Insights von Kund:innen über mehrere Kanäle und während der gesamten Customer Journey zu sammeln, zu analysieren und zu nutzen."
alias: /partners/survicate/
page_type: partner
search_tag: Partner

---

# Survicate

> [Survicate](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter) ist eine Plattform für Kundenfeedback, die Insights von Kund:in über mehrere Kanäle und über die gesamte Customer Journey hinweg sammelt, analysiert und auswertet. [Sehen Sie sich eine kurze Demo an](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter)

_Diese Integration wird von Survicate gepflegt._

## Über die Integration

Verwenden Sie die native Integration von Survicate und Braze, um Antworten auf E-Mail-, In-App-, Mobil- oder Web-Umfragen mit Kundenprofilen von Braze zu synchronisieren. Umfragen werden automatisch mit Braze Nutzerprofilen als angepasste Attribute oder Events synchronisiert. Insights zu Echtzeit-Feedback erleichtern das Tracking und die Analyse von Feedback zusammen mit Kundendaten sowie die Erstellung von Targeting-Follow-ups und hyper-personalisierten Segmenten. 

## Anwendungsfälle

Braze und Survicate arbeiten zusammen, um eine Reihe von Feedback-Anwendungsfällen abzudecken und Ihnen dabei zu helfen, umsetzbare Insights der Nutzer:innen zu sammeln und das Kundenerlebnis zu verbessern:

- Verbessern Sie die Beantwortungsquoten von Umfragen mit eingebetteten Umfragen, die über einen Posteingang beantwortet werden können. 
- Sammeln Sie Insights in kritischen Phasen der Customer Journey über Braze In-App-Nachrichten. 
- Verwenden Sie in Survicate gespeichertes Feedback, um intelligentere Segmente in Braze zu erstellen. 
- Automatisieren Sie Folgekampagnen auf der Grundlage des Feedbacks von Kund:innen. 
- Nutzen Sie Insights von Kund:in, um personalisierte Workflows zu triggern. 
- Erreichen Sie eine breitere Zielgruppe mit automatisch übersetzten Umfragen.
- Senden Sie Ereignisse an Braze Kontaktprofile, wenn jemand auf Ihre Umfrage antwortet

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Survicate Konto | Sie benötigen ein Survicate-Konto, um diese Integration zu aktivieren. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit der Berechtigung `users.track`. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **APIs und Bezeichner** erstellt werden. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Die wichtigsten Features der Integration

Die Integration von Survicate und Braze bietet eine Realtime-Datensynchronisation, so dass die aktuellsten Informationen aus Survicate-Umfragen sofort in Braze verfügbar sind. Auf der Grundlage der Antworten auf Umfragen können Sie diese Daten nutzen, um zeitnahe, personalisierte Maßnahmen zu ergreifen.

- **Senden Sie Umfragen an Braze als angepasste Attribute für Nutzer:innen**: Reichern Sie die Nutzerprofile von Braze mit Daten aus Umfragen an.
- **Triggern Sie angepasste Events in Braze**: Nutzen Sie Ereignisse, die auf den Antworten auf Umfragen basieren, um bestimmte Gruppen zu targeting oder Folgekampagnen zu initiieren.
- **Erstellen Sie detaillierte Segmente**: Erstellen Sie Segmente in Braze anhand von Daten aus Survicate-Umfragen, um Ihre Reichweite weiter zu personalisieren.

## Integration

### Erstellen Sie Ihre Umfragen in Survicate

#### Betten Sie Ihre Umfrage in eine E-Mail ein oder erstellen Sie eine Umfrage, die Sie über einen Link teilen können. 

1.  Klicken Sie in Survicate auf **\+ Neue Umfrage erstellen**, wählen Sie eine beliebige Erstellungsmethode (eine Vorlage, die Erstellung einer KI-Umfrage oder das Hinzufügen eigener Fragen) und den Umfragetyp E-Mail oder Freigegebener Link:
![Braze wird im Ersteller der Umfrage ausgewählt.]({% image_buster /assets/img/survicate/survicate_1.gif %})

{: start="2"}
2\. Wählen Sie auf dem Tab Konfigurieren der Umfrage **Braze** als das Tool aus, mit dem Sie die Befragten identifizieren möchten:
![Braze wird auf dem Tab Konfigurieren der Umfrage ausgewählt.]({% image_buster /assets/img/survicate/survicate_2.png %})

{: start="3"}
3\. Nachdem Sie Ihre Umfrage eingerichtet haben, gehen Sie auf den Tab Teilen und entscheiden Sie, wie Sie Ihre Umfrage per E-Mail versenden möchten. Es gibt zwei Möglichkeiten: Sie können Ihre **Umfrage als Link** versenden oder **die erste Frage in die E-Mail einbetten**, so dass die Befragten direkt in der E-Mail mit der Beantwortung der Umfrage beginnen.

{% details Survey link option %}

1. Über den Button Umfragelink kopieren können Sie einen Link zu Ihrer Umfrage erstellen:

![Über den Button Umfragelink kopieren können Sie einen Link zu Ihrer Umfrage erstellen.]({% image_buster /assets/img/survicate/survicate_3.png %})

{: start="2"}
2\. Blenden Sie den Link zur Umfrage hinter einem CTA Button oder einem Hyperlink in Ihrer Braze E-Mail aus.

![Blenden Sie den Link zur Umfrage hinter einem CTA Button oder einem Hyperlink in Ihrer Braze E-Mail aus.]({% image_buster /assets/img/survicate/survicate_4.png %})

{% enddetails %}

{% details Email embed option %}

Zeigen Sie die erste Frage direkt im Textkörper der E-Mail an, um die Umfrage aus der E-Mail heraus zu starten. Die Befragten werden dann auf eine Landing Page weitergeleitet, um den Rest der Umfrage auszuführen.

1. Klicken Sie auf **E-Mail-Code abrufen** und **kopieren Sie** dann **den HTML-Code**:

![E-Mail Code erhalten]({% image_buster /assets/img/survicate/survicate_5.gif %})

{: start="2"}
2\. Gehen Sie zu der Kampagne von Braze, die Sie für die Umfrage verwenden möchten, klicken Sie auf **E-Mail-Text bearbeiten** und fügen Sie einen HTML-Block zu Ihrem Template hinzu:

![HTML-Block Code abrufen]({% image_buster /assets/img/survicate/survicate_6.png %})

{: start="3"}
3\. Ersetzen Sie den Code durch den Code, den Sie aus Ihrer Survicate Umfrage kopiert haben. Sie sehen dann die erste Frage der Umfrage in der Vorlage:

![Ersetzen Sie den Code mit dem Code, den Sie aus Ihrer Survicate Umfrage kopiert haben]({% image_buster /assets/img/survicate/survicate_7.png %})

{: start="4"}
4\. Legen Sie den Zeitplan für die E-Mail fest, wählen Sie Ihre Zielgruppe, und schon ist Ihre Kampagne versandfertig.

{% enddetails %}

### Braze In-App Nachrichten Umfrage

1. Klicken Sie auf **\+ Neue Umfrage erstellen**, wählen Sie eine beliebige Erstellungsmethode (eine Vorlage, die Erstellung von KI-Umfragen oder das Hinzufügen eigener Fragen) und wählen Sie dann Umfragen auf der Plattform und den Umfragetyp Braze In-App-Nachricht:

![Klicken Sie auf + Neue Umfrage erstellen, wählen Sie eine beliebige Erstellungsmethode]({% image_buster /assets/img/survicate/survicate_8.gif %})

{: start="2"}
2\. Starten Sie Ihre Braze In-App-Nachricht-Umfrage, indem Sie zu Ihrem Braze-Konto navigieren und dann zu **Messaging > Kampagnen > Kampagne erstellen > In-App-Nachricht:**
![Starten Sie Ihre Braze In-App Nachrichten Umfrage]({% image_buster /assets/img/survicate/survicate_9.gif %})

### Starten Sie Ihre Braze In-App Messenger Umfrage über den traditionellen Editor

1. Wenn Sie den traditionellen Editor verwenden, wählen Sie unter Nachrichtentyp die Option **Angepasster Code**:

![Wählen Sie Angepasster Code]({% image_buster /assets/img/survicate/survicate_10.gif %})

{: start="2"}
2\. Fügen Sie dann den Code aus dem Tab Start Ihrer Umfrage in das HTML-Feld ein:

![Fügen Sie den Code aus dem Tab Start Ihrer Umfrage in das HTML-Feld ein]({% image_buster /assets/img/survicate/survicate_11.gif %})

{% alert note %}
Braze zeigt In-App-Nachrichten standardmäßig in einem Iframe an, während der Hintergrund der App blockiert ist. Um eine Interaktion mit Ihrer App zuzulassen, während Umfragen von Survicate erscheinen, müssen Sie:<br><br>

- Fügen Sie `opts.useBrazeIframeClipper = true` zu Ihrem Survicate-Braze Snippet hinzu.
- Installieren Sie das [Paket](https://www.npmjs.com/package/@survicate/braze-bridge-npm) `@survicate/braze-bridge-npm` in der Datei, in der Sie Braze initialisieren und die Funktion `initBrazeBridge` verwenden.

Ein Beispiel-Snippet und eine React-Implementierung finden Sie [auf der Website der Entwickler:in von Survicate.](https://developers.survicate.com/javascript/installation/#braze)
{% endalert %}

{: start="3"}
3\. Richten Sie in Ihrer Braze Kampagne die Schritte Targeting und Zuweisen ein. Wenn Sie fertig sind, ist Ihre Kampagne startbereit. Im Schritt Überprüfung können Sie sehen, wie die Kampagne aussieht. Die Umfrage erscheint auf Ihrer Website an der Stelle, die im Survicate Panel angegeben ist, wie oben beschrieben.

### Enablement der Integration von Braze

1. Um die Integration von Braze zu aktivieren, gehen Sie zu **Integrationen**, suchen Sie nach "Braze" und wählen Sie es aus.

![Braze auswählen]({% image_buster /assets/img/survicate/survicate_12.gif %})

{: start="2"}
2\. Klicken Sie auf **Verbinden**, um die Autorisierung einzurichten.

3. Geben Sie den API-Schlüssel Ihres Braze-Kontos für den Workspace und die URL der Braze-Instanz ein:

![Geben Sie den API-Schlüssel Ihres Braze-Kontos für den Workspace und die URL der Braze-Instanz ein]({% image_buster /assets/img/survicate/survicate_13.png %})

{% alert important %}
Um Survicate mit Braze zu verbinden, muss der API-Schlüssel von Braze über die Berechtigung `users.track` verfügen.
{% endalert %}

### Verbinden Sie Ihre Umfragen mit Braze

Jetzt, da die Braze Integration verbunden ist, können Sie individuelle Einstellungen für jede Umfrage vornehmen. Gehen Sie zu Ihrer Umfrage, wählen Sie den Tab **Verbinden** und wählen Sie **Braze** aus der Liste der verfügbaren Integrationen.

![Gehen Sie zu Ihrer Umfrage, wählen Sie den Tab Verbinden und wählen Sie Braze]({% image_buster /assets/img/survicate/survicate_14.png %})

### Senden von Antworten an Braze als angepasste Attribute

Richten Sie Umfrageantworten so ein, dass sie als angepasste Attribute in Braze einfließen, wodurch Ihre Nutzerprofile in Braze mit gesammelten Daten angereichert werden.

1. Auf dem Tab Einstellungen der Braze Integration sehen Sie den Abschnitt **Felder aktualisieren**.

![Wählen Sie den Abschnitt Felder aktualisieren]({% image_buster /assets/img/survicate/survicate_15.png %})

{: start="2"}
2\. Wählen Sie die Frage aus, deren Felder Sie aktualisieren möchten. Um eine Überflutung Ihrer Nutzer:innen-Profile mit Daten zu vermeiden, können Sie Antworten nur auf ausgewählte Fragen senden.

![Wählen Sie die Frage aus, deren Felder Sie aktualisieren möchten]({% image_buster /assets/img/survicate/survicate_16.png %})

{% alert note %}
Ranking- und Matrixfragen werden von dieser Braze Integration nicht unterstützt.
{% endalert %}

{: start="3"}
3\. Fügen Sie den Namen des angepassten Attributs, das Sie aktualisieren möchten, unter dem Feld **Nutzer**: **innen** ein:

![Fügen Sie den Namen des angepassten Attributs, das Sie aktualisieren möchten, unter dem Feld Nutzer:in hinzu.]({% image_buster /assets/img/survicate/survicate_17.png %})

Standardmäßig sendet Survicate den Inhalt einer Umfrageantwort als Attributwert. Sie können die Beschriftung ändern, um sie kürzer zu machen oder an Ihre Datenstruktur anzupassen, indem Sie auf **Abbildung bearbeiten** klicken, um diese Werte zu ändern:

![Umfrage-Antwort als Attribut-Wert]({% image_buster /assets/img/survicate/survicate_18.png %})

![Klicken Sie auf Abbildung bearbeiten, um diese Werte zu ändern.]({% image_buster /assets/img/survicate/survicate_19.png %})

{% alert note %}
Für NPS sendet Survicate Abbildungen, die auf der Antwortgruppe der NPS®-Frage basieren. Wenn Sie jedoch numerische Werte empfangen möchten, können Sie die Option Antworten als 0-10 Werte senden aktivieren.
{% endalert %}

![Survicate sendet Werte, die auf der Grundlage der Antwortgruppe abgebildet werden]({% image_buster /assets/img/survicate/survicate_20.png %})

{: start="4"}
4\. Verbinden Sie weitere Fragen mit Ihrer Integration, indem Sie auf **\+ Neu hinzufügen** klicken und die gleichen Schritte ausführen.

![Verbinden Sie weitere Fragen mit Ihrer Integration]({% image_buster /assets/img/survicate/survicate_21.png %})

### Senden von Ereignissen an die Profile von Braze-Kontakten

Abgesehen von den vorherigen Einstellungen kann Survicate jedes Mal, wenn ein Befragter eine Umfrage beantwortet, ein angepasstes Event in Braze namens `survicate-question-answered` senden.
Im Panel Survicate können Sie unter Antworten als angepasste Attribute senden wählen, ob Sie das Event für alle Fragen, für die im Tab Felder aktualisieren ausgewählten Fragen oder gar nicht senden möchten:

![Sie können wählen, ob Sie das Ereignis für alle Fragen senden möchten]({% image_buster /assets/img/survicate/survicate_22.png %})

Wenn Sie sich für das Senden der Ereignisse entscheiden, können Sie in den Profilen der Nutzer:innen sehen, wie oft sie auf Umfragen von Survicate geantwortet haben und wann sie zuletzt geantwortet haben:

![Antworten ]({% image_buster /assets/img/survicate/survicate_23.png %})

Das Event enthält Event-Eigenschaften mit der Antwort auf die Frage und Informationen über die Umfrage, die Frage und den Befragten. Sie können dieses Ereignis verwenden, um Segmente zu erstellen. Erstellen Sie zum Beispiel ein Segment von Nutzer:innen, die nach einem bestimmten Datum oder einer bestimmten Anzahl von Umfragen geantwortet haben:

![Das Event enthält Event-Eigenschaften mit der Antwort]({% image_buster /assets/img/survicate/survicate_24.png %})

Sie können diese Daten auch verwenden, wenn Sie eine Kampagne in Braze erstellen.

![Sie können diese Daten auch beim Erstellen einer Kampagne in Braze verwenden]({% image_buster /assets/img/survicate/survicate_25.png %})

### Testen Sie die Integration

Wenn Sie Ihre Umfrage fertiggestellt und die Integration eingerichtet haben, können Sie sie testen, ohne Survicate zu verlassen. Klicken Sie dazu auf den Button Integration testen neben einem Attribut, Tag oder einer neuen Kontakteinrichtung, die Sie erstellt haben. Survicate erstellt einen Testkontakt (`braze-test@survicate.com`) in Ihrem Braze-Konto. Das Profil des Kontakts enthält aktualisierte Felder gemäß der Einrichtung.

![Klicken Sie auf den Button Integration testen]({% image_buster /assets/img/survicate/survicate_26.png %})

In Braze sehen Sie Beispieldaten aus den abgebildeten Feldern im Survicate Dummy-Kontakt:

![Beispieldaten aus den abgebildeten Feldern im Survicate Dummy Contact]({% image_buster /assets/img/survicate/survicate_27.png %})

### Analyse der Ergebnisse Ihrer Umfrage

Nachdem Sie die Antworten in Ihrer Braze Umfrage gesammelt haben, ist es an der Zeit, das Feedback und die Insights Ihrer Befragten zu analysieren. Mit Survicate können Sie ganz einfach Ergebnisse, Statistiken und Trends überprüfen, um weitere Maßnahmen zu ergreifen.

### Feedback in Survicate

Nachdem Ihre Umfrage mit der Erfassung von Antworten begonnen hat, sehen Sie diese sofort im Tab Analysieren der Umfrage.

![Antworten im Tab Analysieren]({% image_buster /assets/img/survicate/survicate_28.png %})

Der Tab Analysieren zeigt Ihnen die Gesamtergebnisse mit Statistiken und Daten über die Zeit sowie die einzelnen Umfragen, um die einzelnen Umfragen im Detail zu betrachten.

### Feedback in Braze

Wenn Sie Benutzerfelder mit Umfrageantworten aktualisieren oder Antworten als angepasste Events senden, können Sie sehen, dass die Daten der Umfrage in Realtime synchronisiert werden. Gehen Sie in Braze zu einem bestimmten Kontakt, der auf Ihre Umfrage geantwortet hat. In der Hauptansicht des Kontakts sehen Sie sowohl die response-basierten Daten als auch die Ereignisse.

![Umfragedaten in Realtime synchronisiert]({% image_buster /assets/img/survicate/survicate_29.png %}) 