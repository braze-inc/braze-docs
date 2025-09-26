---
nav_title: Optimal
article_title: Optimal
page_order: 2
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Optimizely, die es Ihnen erlaubt, Ihre Segmente, Events und Currents Events von Braze mit der Optimizely Data Platform zu synchronisieren."
alias: /partners/optimizely/
page_type: partner
search_tag: Partner
---

# Optimal

> [Optimizely](https://www.optimizely.com/) ist eine führende Plattform für digitale Erlebnisse, die Experimentier- und Management-Tools für digitale Produkte und Kampagnen anbietet.

Die Integration von Braze und Optimizely ist eine bidirektionale Integration, die es Ihnen erlaubt:

- Synchronisieren Sie Ihre Braze Kundensegmente und Events mit der Optimizely Data Platform (ODP) über Nacht, um Optimizelys Kundenprofile, Berichte und Segmentierung zu bereichern.
- Senden Sie Braze-Currents-Ereignisse von Braze an das Berichtstool von Optimizely.
- Synchronisieren Sie ODP Kundendaten und Events mit Braze, um Ihre Kundendaten in Braze anzureichern und Messaging auf der Grundlage von Kundenevents in ODP zu triggern.

## Voraussetzungen

| Anforderung                     | Beschreibung |
|----------------------------------|-------------|
| Optimizely Daten Plattform Konto | Um die Vorteile dieser Partnerschaft nutzen zu können, benötigen Sie ein Optimizely Data Platform (ODP) Konto. |
| Braze REST API-Schlüssel               | Ein Braze REST API-Schlüssel mit den folgenden Berechtigungen: `users.track`,`users.export.segments`,`segments.list`,`campaigns.trigger.send`, und `canvas.trigger.send`. |
| Currents                         | Um Daten zurück in Optimizely zu exportieren, müssen Sie Braze-Currents für Ihr Konto einrichten lassen. |
| Optimizely URL und Token         | Diese erhalten Sie, indem Sie zu Ihrem Optimizely Dashboard navigieren und die Ingestion-URL und das Token kopieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Konfigurieren Sie die Integration

1. Wählen Sie im **App-Verzeichnis** von Optimizely Data Platform (ODP) die App **Braze** aus und wählen Sie dann **App installieren**.
2. Gehen Sie auf den Tab **Einstellungen**. Gehen Sie im Abschnitt **Autorisierung** wie folgt vor:
    1. Geben Sie den Braze **REST API-Schlüssel** ein.
    2. Wählen Sie die **URL Ihrer Braze-Instanz** aus.
    2. Wählen Sie **API-Schlüssel überprüfen**.
3. Gehen Sie in Braze zu **[Currents]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents/)**.
4. Wählen Sie **Neue Currents erstellen** > **Angepasste Currents exportieren**.
5. Konfigurieren Sie den Current mit dem Endpunkt und dem Token, die in ODP bereitgestellt werden. Dies ist erforderlich, um Braze-Ereignisse mit ODP zu synchronisieren. 

![Optimizely Autorisierung.]({% image_buster /assets/img/optimizely/image1_authorization.png %})

{:start="6"}
6\. Erweitern Sie in ODP den Abschnitt **Segmente** und wählen Sie bestimmte Segmente aus der Liste **Zu synchronisierende Segmente** aus, oder wählen Sie **Alle Kunden importieren**, um alle Segmente zu synchronisieren.
7\. Fügen Sie alle gewünschten [zusätzlichen Abbildungen von Feldern](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/29918568615949-Integrate-Braze%23h_01J6Z1P53JVDBFZ758Q78CK1QB&sa=D&source=editors&ust=1733948158380300&usg=AOvVaw3WSAND5ie3LCVuSxUlLanR) zwischen Braze und ODP hinzu.
8\. Wählen Sie **Speichern**.

![Optimally Braze Segmente synchronisieren.]({% image_buster /assets/img/optimizely/image2_syncsegment.png %})

{% alert tip %}
Sie müssen Segmente auswählen, um Braze Kundenprofile zu importieren. Wenn Sie keine Segmente auswählen, wird die Integration keine Kundenprofile importieren.
{% endalert %}

### Schritt 2: Datenfelder der Abbildung

Die Integration verfügt über Standard-Abbildungen von Datenfeldern zwischen Braze und ODP. Zum Beispiel wird das Feld **E-Mail** in Braze dem Feld **E-Mail zuletzt gesehen** in ODP zugeordnet.

![Optimieren und Braze Segmente abbilden.]({% image_buster /assets/img/optimizely/image3_emailmapfield.png %})

#### Abbildung zusätzlicher Felder (optional)

Wenn es in Braze zusätzliche Datenfelder gibt, die Sie in ODP abbilden möchten, gehen Sie in ODP wie folgt vor:

1. Wählen Sie im Abschnitt **Segmente** der App das Feld Braze aus der Dropdown- Liste **Felder für Nutzerdaten aus Braze** aus.
2. Wählen Sie das ODP-Feld aus der Dropdown- Liste **ODP-Kunden**:in aus.
3. Wählen Sie **Feldkarte speichern**.

![Optimizely Braze Segmente speichern Feldkarten]({% image_buster /assets/img/optimizely/image4_mapfields.png %})

#### Löschen Sie nicht benötigte Abbildungen von Feldern (optional)

Sie können auch alle Datenfeld-Abbildungen löschen, die nicht benötigt werden. Gehen Sie in ODP wie folgt vor:

1. Wählen Sie im Abschnitt **Segmente** der App die Abbildung des Feldes, das Sie löschen möchten, aus der Dropdown- Liste **Feldabbildung** aus.
2. Wählen Sie **Feldkarte löschen**.

![Optimizeely Braze Segmente löschen Feldkarten]({% image_buster /assets/img/optimizely/image5_deletephonefield.png %})

### Schritt 3: Synchronisieren Sie Daten von Optimizely Data Platform (ODP) mit Braze

Nachdem Sie die Integration konfiguriert haben, können Sie eine Aktivierung in ODP einrichten, um Ihre ODP Kundendaten mit Braze zu synchronisieren.

1. Gehen Sie zu **Aktivierung** > **Engage** und wählen Sie **Neue Kampagne erstellen**.
2. Wählen Sie **Verhalten**, um eine automatisierte, wiederkehrende Synchronisierung einzurichten.
3. Wählen Sie **Neu erstellen** und geben Sie dann einen Namen für Ihre Aktivierung ein, der die Daten repräsentiert, die Sie mit Braze synchronisieren (z.B. **Braze Data Sync**).
4. Im Abschnitt **Registrierung** können Sie Daten für Kunden synchronisieren, die einem Segment entsprechen, oder Daten für Kunden synchronisieren, die ein Ereignis triggern (z.B. wenn ODP registriert, dass ein Kunde eine E-Mail öffnet):
   - **Kunden, die einem Segment entsprechen:** Wählen Sie das gewünschte Segment aus und wählen Sie dann **Weiter**.<br><br>![Optimizely Segmente auswählen]({% image_buster /assets/img/optimizely/image6_segment.png %})
   - **Kunden:in, die ein Ereignis triggern:** Erweitern Sie die Dropdown- Liste **Filter** und wählen Sie das ODP-Ereignis aus, das als Auslöser für die Synchronisierung der Daten mit Braze dienen soll. Erweitern Sie dann die **Automatisierungsregeln** und passen Sie sie wie gewünscht an. <br><br>![Optimizely Ereignis triggern]({% image_buster /assets/img/optimizely/image7_trigger.png %})
5. Erweitern Sie **Touchpoints**, wählen Sie **Touchpoint 1** zur Bearbeitung aus und wählen Sie dann **Braze**.
6. Erweitern Sie den Abschnitt **Targeting**, und wählen Sie dann den **Bezeichner für das Ziel** aus.
7. Wählen Sie eine der folgenden Optionen für **Nutzer:innen hinzufügen** im Abschnitt **Konfigurieren** aus:
    - **Kampagne:** Fügen Sie Kunden:in zu einer bestimmten Kampagne in Braze hinzu. Nachdem Sie diese Option gewählt haben, müssen Sie die Braze Kampagne auswählen.
    - **Canvas:** Fügen Sie Kunden:in einem bestimmten Canvas in Braze hinzu. Nachdem Sie diese Option gewählt haben, müssen Sie das Braze-Canvas auswählen.
    - **Nur Profil Update:** Aktualisieren Sie nur das Kundenprofil von Braze.
8. (Optional) Wählen Sie die **Anzahl der zusätzlichen Felder** aus, die Sie mit Braze synchronisieren möchten (bis zu 20).  
    Wählen Sie dann für die Dropdown- Liste und das Eingabefeld jedes zusätzlichen Feldes das Folgende aus:
    - Wählen Sie in jeder Dropdown- Liste **Feld #** das Braze-Feld aus, das Sie auffüllen möchten. 
    - Geben Sie in jedes entsprechende **Feld # Wert** das ODP-Feld ein, das Sie an das ausgewählte Braze-Feld senden möchten. Wenn Sie z.B. **Firmenname** aus der Dropdown- Liste **Feldnummer** ausgewählt haben, geben Sie `{{customer.company_name}}` für den entsprechenden **Feldnummerwert** ein.
9. Wählen Sie **Speichern** und wählen Sie dann Ihren Aktivierungsnamen im Breadcrumb-Pfad aus.
10. Wählen Sie **Startzeit und Zeitplan** im Abschnitt **Touchpoints** aus, wenn Sie für die Anmeldung **Kunden, die einem Segment entsprechen** ausgewählt haben.
11. Nehmen Sie die folgenden Einstellungen vor:
    - **Wiederkehrend oder fortlaufend:** Wählen Sie **Wiederkehrend**.
    - **Startdatum:** Geben Sie das Datum ein, an dem Sie die Daten an Braze senden möchten.
    - **Ende:** Standardmäßig ist **Nie** eingestellt. Wenn Sie die Synchronisierung der Daten von Braze an einem bestimmten Datum beenden möchten, legen Sie dies hier fest.
    - **Wiederholungen:** Stellen Sie auf **Täglich**.
    - **Wiederholen Sie alle** \- Setzen Sie auf **1 Tag**.
    - **Zeitplan:** Geben Sie den Zeitpunkt ein, zu dem Sie die Daten an Braze senden möchten.
    - **Zeitzone:** Wählen Sie die Zeitzone aus, in der Sie diese Daten senden möchten.
12. Wählen Sie **Anwenden**, **Speichern** und dann **Live gehen**. Ihre Synchronisierung beginnt an dem von Ihnen festgelegten Startdatum und -zeitpunkt (oder wenn das triggernde Ereignis eintritt).

## Fehlersuche

### Ereignisse inspizieren

Um zu überprüfen, ob die Daten ordnungsgemäß von ODP mit Braze synchronisiert werden, können Sie Ereignisse in ODP überprüfen.

1. Gehen Sie in ODP zu **Kontoeinstellungen** > **Ereignisinspektor**.
2. Wählen Sie **Inspektor starten**.
3. Wenn Daten im Inspektor verfügbar sind, wird neben **Aktualisieren** eine Zahl angezeigt. Wählen Sie aus, um die Daten anzuzeigen.
4. Die Rohdaten, die ODP und Braze hin und her senden, werden angezeigt. Wählen Sie **Details anzeigen**, um die formatierte Version dieser Rohdaten zu sehen.
5. Datenfelder, die von Braze zurück an ODP gesendet werden, beginnen mit `_braze`.

### Aktivitätsprotokolle prüfen

Jede Synchronisierung von Daten wird auch im [ODP-Aktivitätsprotokoll](https://www.google.com/url?q=https://support.optimizely.com/hc/en-us/articles/4407268804365-Use-the-Activity-Log&sa=D&source=editors&ust=1733948158385124&usg=AOvVaw2tMOxzcTKfL0-oYLT4IMpP) festgehalten:

1. Gehen Sie zu **Kontoeinstellungen** > **Aktivitätsprotokoll**.
2. Filtern Sie die Kategorien nach **Braze**.
3. Wählen Sie **Details** auswählen, um eine formatierte Ansicht der Protokolldetails, einschließlich der Anzahl der Treffer, zu erhalten.

