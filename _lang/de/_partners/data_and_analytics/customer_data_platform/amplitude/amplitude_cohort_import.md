---
nav_title: Amplitude
article_title: Amplitude Kohorte Import
description: "Dieser referenzierte Artikel beschreibt die Kohortenimport-Funktionalität von Amplitude, einer Analytics-Plattform für Produkte und Business-Intelligence."
page_type: partner
search_tag: Partner
---

# Amplitude Kohortenimport

> Dieser Artikel beschreibt, wie Sie Nutzer:in-Kohorten von [Amplitude](https://amplitude.com/) nach Braze importieren können. Weitere Informationen zur Integration von Amplitude und seinen anderen Funktionen finden Sie im [Hauptartikel zu Amplitude]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_audiences/).

## Integration von Datenimporten

Jede Integration, die Sie einrichten, wird auf das Datenpunktvolumen Ihres Kontos angerechnet.

### Schritt 1: Holen Sie sich den Datenimport-Schlüssel für Braze

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Amplitude** aus. Hier finden Sie den REST-Endpunkt und generieren Ihren Datenimport-Schlüssel für Braze. 

Nach der Generierung können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimport-Schlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im Dashboard von Amplitude einrichten.<br><br>![]({% image_buster /assets/img/amplitude3.png %})

### Schritt 2: Einrichten der Braze Integration in Amplitude

Navigieren Sie in Amplitude zu **Quellen & Ziele** > **[Projektname]** > **Ziele** > Braze. Geben Sie in der daraufhin angezeigten Aufforderung den Datenimport-Schlüssel und den REST-Endpunkt von Braze an und klicken Sie auf **Speichern**.

![]({% image_buster /assets/img/amplitude.png %})

### Schritt 3: Exportieren einer Amplitude Kohorte nach Braze

Um Nutzer:innen aus Amplitude nach Braze zu exportieren, erstellen Sie zunächst eine [Kohorte](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts) von Nutzern:innen, die Sie exportieren möchten. Amplitude kann Kohorten mit den folgenden Bezeichnern mit Braze synchronisieren:
- Nutzer-Alias
- Geräte-ID
- Nutzer:innen ID (Externe ID)

Amplitude unterstützt mehrere Eigenschaften für die Abbildung von Bezeichnern in Prioritätsreihenfolge. Sie können eine Abbildung von primären, sekundären und tertiären Bezeichnern konfigurieren. Wenn einem Nutzer:innen bei der Synchronisierung die Primärdatei fehlt, verwendet Amplitude die nächste verfügbare Datei. Dies verbessert die Synchronisierungsabdeckung, reduziert die Zahl der ausgelassenen Nutzer:in und bezieht mehr anonyme und teilweise identifizierte Nutzer:innen in Ihre Synchronisierung ein. 

Sobald Sie eine Kohorte erstellt haben, klicken Sie auf **Synchronisieren mit...**, um diese Nutzer:innen nach Braze zu exportieren.

{% alert important %}
Nur Nutzer:innen, die bereits in Braze existieren, werden einer Kohorte hinzugefügt oder aus ihr entfernt. Kohortenimport wird keine neuen Nutzer:innen in Braze erstellen.
{% endalert %}

#### Sync-Kadenz festlegen

Kohorten-Synchronisationen können als einmalige Synchronisation, als täglicher oder stündlicher Zeitplan oder sogar als Realtime-Synchronisation, die jede Minute aktualisiert, eingestellt werden. 

Jede Integration, die Sie einrichten, protokolliert Datenpunkte. Wenn Sie Fragen zu den Datenpunkten von Braze haben, kann Ihr Braze-Konto Manager:in diese Fragen beantworten.

### Schritt 4: Segmentierung der Nutzer:innen in Braze

Um in Braze ein Segment dieser Nutzer:innen zu erstellen, navigieren Sie zu **Segmente** unter **Engagement**, benennen Sie Ihr Segment und wählen Sie **Amplitude Kohorten** als Filter aus. Als nächstes verwenden Sie die Option "enthält" und wählen die Kohorte, die Sie in Amplitude erstellt haben. 

![Im Braze Segment Builder ist der Filter "amplitude_cohorts" auf "includes_value" und "Amplitude Kohorte Test" eingestellt.]({% image_buster /assets/img/amplitude2.png %})

Nach dem Speichern können Sie dieses Segment bei der Erstellung von Canvas oder Kampagnen im Schritt Targeting Nutzer:innen referenzieren.

## Nutzer:innen-Abgleich

Identifizierte Nutzer:innen können entweder über ihre `external_id` oder `alias` abgeglichen werden. Anonyme Nutzer:innen können über ihre `device_id` gefunden werden. Identifizierte Nutzer:innen, die ursprünglich als anonyme Nutzer:innen angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder `alias` identifiziert werden.
