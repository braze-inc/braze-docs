---
nav_title: Heap
article_title: "Heap-Analytik"
description: "Dieser Referenzartikel beschreibt, wie Sie Braze Currents zur automatischen Analyse von Engagement-Ereignissen mit Heap, einer Plattform für digitale Einblicke, verwenden können. Sie können Heap-Daten in Braze importieren, Benutzerkohorten erstellen und Braze-Daten in Heap exportieren, um Segmente zu erstellen."
page_type: partner
search_tag: Partner


---

# Heap-Analysen

> Dieser Artikel beschreibt, wie Sie automatisch Engagement-Ereignisse von Braze zur Analyse an Heap senden. Weitere Informationen zur Integration von Heap und seinen anderen Funktionen, wie z.B. die [Synchronisierung von Heap-Kohorten]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/#data-import-integration) mit Braze, finden Sie im [Hauptartikel zu Heap]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/).

## Integration des Datenexports

Verwenden Sie Braze Currents, um automatisch Engagement-Ereignisse (z. B. gesendete E-Mails, gesendete Push-Nachrichten) von Braze zur Analyse an Heap zu senden.

### Schritt 1: Heap-Anmeldeinformationen abrufen

Um diese Integration zu konfigurieren, benötigen Sie eine Webhook-Endpunkt-URL, die Sie von Ihrem Heap-Kundenbetreuer erhalten können.

### Schritt 2: Lötströme konfigurieren

Navigieren Sie in Braze zu **Partnerintegrationen** > **Datenexport**, klicken Sie auf **Neuen Strom erstellen** und wählen Sie **Heap-Export**. 

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Currents** unter **Integrationen**.
{% endalert %}

Geben Sie Ihrem Export einen Namen und gehen Sie dann auf die Seite **Aktuelle Details**. Geben Sie auf dieser Seite den Endpunkt und das optionale Träger-Token (falls vorhanden) ein.

Nachdem Sie die Anmeldedaten für Ihre Integration konfiguriert haben, markieren Sie alle Nachrichten, das Kundenverhalten und die Benutzerereignisse, die Sie in Heap exportieren möchten, und klicken Sie auf **Aktuell starten**.

![][5]{: style="max-width:90%;"}

[5]: {% image_buster /assets/img/heap/heap4.png %} 
