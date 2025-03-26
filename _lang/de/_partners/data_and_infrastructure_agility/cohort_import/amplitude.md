---
nav_title: Amplitude
article_title: Amplitude Kohorte Import
description: "Dieser Referenzartikel beschreibt die Kohortenimportfunktion von Amplitude, einer Plattform für Produktanalyse und Business Intelligence."
page_type: partner
search_tag: Partner
---

# Amplitude Kohorte importieren

> Dieser Artikel beschreibt, wie Sie Benutzerkohorten aus [Amplitude](https://amplitude.com/) in Braze importieren. Weitere Informationen zur Integration von Amplitude und seinen anderen Funktionen finden Sie im [Hauptartikel zu Amplitude]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_audiences/).

## Integration von Datenimporten

Jede Integration, die Sie einrichten, wird auf das Datenpunktvolumen Ihres Kontos angerechnet.

### Schritt 1: Holen Sie sich den Braze-Datenimportschlüssel

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Amplitude**. Hier finden Sie den REST-Endpunkt und generieren Ihren Braze-Datenimportschlüssel. 

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

Nach der Generierung können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimportschlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im Dashboard von Amplitude einrichten.<br><br>![]({% image_buster /assets/img/amplitude3.png %})

### Schritt 2: Einrichten der Braze-Integration in Amplitude

Navigieren Sie in Amplitude zu **Quellen & Ziele** > **[Projektname]** > **Ziele** > **Braze**. Geben Sie in der daraufhin angezeigten Aufforderung den Braze-Datenimportschlüssel und den REST-Endpunkt an und klicken Sie auf **Speichern**.

![]({% image_buster /assets/img/amplitude.png %})

### Schritt 3: Exportieren einer Amplitudenkohorte nach Braze

Um Benutzer von Amplitude nach Braze zu exportieren, erstellen Sie zunächst eine [Kohorte](https://help.amplitude.com/hc/en-us/articles/231881448-Behavioral-Cohorts) von Benutzern, die Sie exportieren möchten. Amplitude kann Kohorten mit den folgenden Identifikatoren mit Braze synchronisieren:
- Nutzer-Alias
- Geräte-ID
- Benutzer-ID (Externe ID)

Sobald Sie eine Kohorte erstellt haben, klicken Sie auf **Synchronisieren mit...**, um diese Benutzer nach Braze zu exportieren.

#### Sync-Kadenz festlegen

Kohortensynchronisierungen können als einmalige Synchronisierung, als tägliche oder stündliche Synchronisierung oder sogar als Echtzeitsynchronisierung, die jede Minute aktualisiert wird, eingestellt werden. Stellen Sie sicher, dass Sie eine Option wählen, die für Ihre geschäftlichen Anforderungen sinnvoll ist, und achten Sie gleichzeitig auf den Verbrauch von [Datenpunkten]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/).

### Schritt 4: Segmentierte Benutzer in Braze

Um in Braze ein Segment dieser Benutzer zu erstellen, navigieren Sie zu **Segmente** unter **Engagement**, benennen Sie Ihr Segment und wählen Sie **Amplitude Cohorts** als Filter. Als nächstes verwenden Sie die Option "enthält" und wählen die Kohorte, die Sie in Amplitude erstellt haben. 

![Im Braze Segment Builder wird der Filter "amplitude_cohorts" auf "includes_value" und "Amplitude cohort test" gesetzt.]({% image_buster /assets/img/amplitude2.png %})

Nach dem Speichern können Sie dieses Segment bei der Erstellung von Canvas oder Kampagnen im Schritt Nutzer ansprechen verwenden.

## Benutzerabgleich

Identifizierte Benutzer können entweder über ihre `external_id` oder `alias` abgeglichen werden. Anonyme Benutzer können über ihre `device_id` abgeglichen werden. Identifizierte Benutzer, die ursprünglich als anonyme Benutzer angelegt wurden, können nicht über ihre `device_id` identifiziert werden, sondern müssen über ihre `external_id` oder `alias` identifiziert werden.