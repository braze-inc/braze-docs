---
nav_title: Amplitude
article_title: Amplitude
page_order: 0
alias: /partners/amplitude_recommend/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Amplitude, einer Plattform für Produktanalyse und Business Intelligence."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Braze Learning Kurs]](https://learning.braze.com/amplitude-integration-with-braze) ( [{% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude

> [Amplitude](https://amplitude.com/) ist eine Plattform für Produktanalytik und Business Intelligence.

Die bidirektionale Integration von Braze und Amplitude ermöglicht es Ihnen, [Ihre Amplitude-Kohorten]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/amplitude/), Benutzermerkmale und Ereignisse in Braze [zu importieren]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/amplitude/) und Segmente zu erstellen, die Benutzer in zukünftigen Kampagnen oder Canvases ansprechen können. Sie können Braze Currents auch dazu nutzen, [Ihre Braze-Ereignisse nach Amplitude zu exportieren]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/#data-export-integration), um Ihre Produkt- und Marketingdaten genauer zu analysieren.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Amplitude Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Amplitude-Konto](https://amplitude.com/). |
| Currents | Damit Sie Daten zurück nach Amplitude exportieren können, müssen Sie [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Wählen Sie eine Integration 

Amplitude und Braze bieten zwei verschiedene Integrationsmethoden. Lesen Sie die folgende Dokumentation, um zu entscheiden, welche Methoden für Ihre Bedürfnisse geeignet sind:

- Braze Event Streaming: Eine Integration, mit der Sie rohe Amplitude-Ereignisdaten direkt an Braze weiterleiten können.
- [Kohortenimport]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/amplitude/): Eine Integration, mit der Sie Amplitude-Kohorten an Braze weiterleiten können.

## Braze Event Streaming

### Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit allen Berechtigungen.<br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][1]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Braze App Kennung | Der Bezeichner für die App, die Amplitude-Ereignisse empfangen soll. Diese finden Sie im **Braze Dashboard > Entwicklerkonsole > Einstellungen**. |

### Amplitude einstellen

1. Navigieren Sie in Amplitude zu **Datenzielen** und suchen Sie dann nach "Braze - Event Stream".
2. Geben Sie einen Sync-Namen ein und klicken Sie dann auf **Sync erstellen**.
3. Klicken Sie auf **Bearbeiten** und geben Sie den REST-API-Endpunkt von Braze, den REST-API-Schlüssel und die Kennung der Braze-App an.
4. Verwenden Sie den Filter Ereignisse senden, um die zu sendenden Ereignisse auszuwählen. Sie können alle Ereignisse senden, aber Amplitude empfiehlt, die wichtigsten auszuwählen. 
5. Wenn Sie fertig sind, aktivieren Sie das Ziel und speichern Sie. 

Weitere Informationen zu dieser Integration finden Sie unter [Braze Event Streaming](https://www.docs.developers.amplitude.com/data/destinations/braze/).

## Synchronisierung von Benutzermerkmalen und Berechnungen

Verwenden Sie Audiences, um Benutzereigenschaften und Berechnungen als benutzerdefinierte Attribute an Braze zu senden. Sie können Benutzereigenschaften oder berechnete Eigenschaften von Benutzern, die in den letzten 90 Tagen aktiv waren, synchronisieren.

Wenn die Eigenschaft eines Benutzers oder eine Berechnung aktualisiert wird, aktualisiert Amplitude ein benutzerdefiniertes Attribut in Braze mit demselben Namen wie die Benutzereigenschaft oder die Berechnung.

Durch die Synchronisierung von Benutzermerkmalen und Berechnungen werden neue Benutzer für Benutzer-IDs erstellt, die noch nicht in Braze existieren. Berechnungen und Benutzereigenschaften können nur über die Benutzer-ID synchronisiert werden.

Lesen Sie die Dokumentation von Amplitude, um mehr über die [Synchronisierung von Eigenschaften, Empfehlungen und Kohorten mit Zielen von Drittanbietern](https://help.amplitude.com/hc/en-us/articles/360060055531) zu erfahren.

#### Wie Sie Benutzereigenschaften und Berechnungen synchronisieren

Wählen Sie in Amplitude Audiences **Syncs > Sync erstellen**.

![]({% image_buster /assets/img/amplitude11.png %})

Wählen Sie als nächstes, ob Sie eine Benutzereigenschaft, eine Berechnung, eine Kohorte oder eine Empfehlung synchronisieren möchten. 

{% tabs %}
{% tab Synchronisieren von Benutzereigentum %}

Wählen Sie **Benutzereigenschaft** und dann die gewünschte zu synchronisierende Benutzereigenschaft.

![]({% image_buster /assets/img/amplitude7.png %})

Wählen Sie dann ein Ziel aus, mit dem Sie Ihre Benutzereigenschaften synchronisieren möchten.

![]({% image_buster /assets/img/amplitude8.png %})

Legen Sie schließlich die Häufigkeit Ihrer Synchronisierung fest.

![Definieren Sie Ihre Kadenz als einmalige Synchronisierung oder als geplante Synchronisierung.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% tab Synchronisationsberechnung %}

Wählen Sie **Berechnung** und dann die gewünschte zu synchronisierende Berechnung.

![]({% image_buster /assets/img/amplitude10.png %})

Wählen Sie dann ein Ziel aus, mit dem Sie Ihre Berechnungen synchronisieren möchten.

![]({% image_buster /assets/img/amplitude8.png %})

Legen Sie schließlich die Häufigkeit Ihrer Synchronisierung fest.

![Definieren Sie Ihre Kadenz als einmalige Synchronisierung oder als geplante Synchronisierung.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% endtabs %}

## Amplitude Benutzerprofil API Endpunkte

Einige der gängigen Amplitude-API-Endpunkte, die mit Connected Content verwendet werden können, finden Sie in unserer speziellen [Amplitude-API-Dokumentation]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_user_profile_api/).
