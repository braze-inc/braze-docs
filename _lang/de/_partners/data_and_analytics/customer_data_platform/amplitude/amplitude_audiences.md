---
nav_title: Amplitude
article_title: Amplitude
page_order: 0
alias: /partners/amplitude_recommend/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Amplitude, einer Analytics-Plattform für Produkte und Business-Intelligence."
page_type: partner
tool: Currents
search_tag: Partner

---

# [![Braze-Lernkurs] ({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/amplitude-integration-with-braze){: style="float:right;width:120px;border:0;" class="noimgborder"}Amplitude

> [Amplitude](https://amplitude.com/) ist eine Plattform für Produkt-Analytik und Business-Intelligence.

Die bidirektionale Integration von Braze und Amplitude ermöglicht es Ihnen, [Ihre Amplitude-Kohorten]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import/), Benutzermerkmale und Ereignisse in Braze zu importieren und Segmente zu erstellen, die Nutzer:innen in zukünftigen Kampagnen oder Canvase ansprechen können. Sie können Braze-Currents auch nutzen, um [Ihre Braze-Ereignisse nach Amplitude zu exportieren]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_for_currents/#data-export-integration) und so tiefere Analysen Ihrer Produkt- und Marketingdaten durchzuführen.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Amplitude Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Amplitude-Konto](https://amplitude.com/). |
| Currents | Um Daten zurück nach Amplitude zu exportieren, müssen Sie [Braze-Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) für Ihr Konto eingerichtet haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

## Wählen Sie eine Integration 

Amplitude und Braze bieten zwei verschiedene Methoden zur Integration. Lesen Sie die folgende Dokumentation, um zu entscheiden, welche Methoden für Ihre Bedürfnisse geeignet sind:

- Braze Event Streaming: Eine Integration, die es Ihnen erlaubt, rohe Amplitude-Ereignisdaten direkt an Braze weiterzuleiten.
- [Kohortenimport]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_cohort_import/): Eine Integration, die es Ihnen erlaubt, Kohorten von Amplitude an Braze weiterzuleiten.

## Braze Event Streaming

### Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit allen Berechtigungen.<br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][1]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Bezeichner der App Braze | Der Bezeichner für die App, die Amplitude-Ereignisse empfangen soll. Diese finden Sie im **Braze-Dashboard > Entwicklungskonsole > Einstellungen.** |

### Amplitude einrichten

1. Navigieren Sie in Amplitude zu **Daten-Ziele** und suchen Sie nach "Braze - Event Stream".
2. Geben Sie einen Namen für die Synchronisierung ein und klicken Sie dann auf **Synchronisierung erstellen**.
3. Klicken Sie auf **Bearbeiten** und geben Sie den Endpunkt der Braze REST API, den REST API-Schlüssel und den Bezeichner der Braze App an.
4. Verwenden Sie den Filter Ereignisse senden, um die zu sendenden Ereignisse auszuwählen. Sie können alle Ereignisse senden, aber Amplitude empfiehlt, die wichtigsten auszuwählen. 
5. Wenn Sie fertig sind, aktivieren Sie das Ziel und speichern. 

Weitere Informationen zu dieser Integration finden Sie unter [Braze Event Streaming](https://www.docs.developers.amplitude.com/data/destinations/braze/).

## Synchronisierung von Nutzer:innen und Berechnungen

Verwenden Sie Audiences, um Nutzer:innen Eigenschaften und Berechnungen als angepasste Attribute an Braze zu senden. Sie können die Eigenschaften von Nutzern:innen, die in den letzten 90 Tagen aktiv waren, synchronisieren.

Wenn die Eigenschaft eines Nutzers oder eine Berechnung aktualisiert wird, aktualisiert Amplitude ein angepasstes Attribut in Braze mit demselben Namen wie die Eigenschaft oder Berechnung des Nutzers.

Durch die Synchronisierung von Benutzereigenschaften und Berechnungen werden neue Nutzer:innen für Bezeichner erstellt, die noch nicht in Braze existieren. Berechnungen und Nutzer:innen können nur über Bezeichner synchronisiert werden. Ein Bezeichner für Nutzer:innen kann einer der folgenden sein:
- Externe ID
- Braze-ID
- Nutzer:in alias
- E-Mail-Adresse

Lesen Sie die Dokumentation von Amplitude, um mehr über die [Synchronisierung von Eigenschaften, Empfehlungen und Kohorten mit Zielen von Drittanbietern](https://help.amplitude.com/hc/en-us/articles/360060055531) zu erfahren.

#### Synchronisieren von Nutzer:innen Eigenschaften und Berechnungen

Wählen Sie in Amplitude Zielgruppen **> Sync erstellen**.

![]({% image_buster /assets/img/amplitude11.png %})

Wählen Sie als nächstes, ob Sie eine Nutzer:in, eine Berechnung, eine Kohorte oder eine Empfehlung synchronisieren möchten. 

{% tabs %}
{% tab Synchronisierung der Nutzer:in-Eigenschaften %}

Wählen Sie **Benutzer:innen** und dann die zu synchronisierende Eigenschaft des Nutzers aus.

![]({% image_buster /assets/img/amplitude7.png %})

Wählen Sie als nächstes ein Ziel aus, mit dem Sie Ihre Nutzer:innen Eigenschaften synchronisieren möchten.

![]({% image_buster /assets/img/amplitude8.png %})

Legen Sie schließlich die Häufigkeit Ihrer Synchronisierung fest.

![Definieren Sie Ihre Kadenz als einmalige oder geplante Synchronisierung.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% tab Synchronisierung der Berechnungen %}

Wählen Sie **Berechnung** und dann die gewünschte zu synchronisierende Berechnung aus

![]({% image_buster /assets/img/amplitude10.png %})

Wählen Sie dann ein Ziel aus, mit dem Sie Ihre Berechnungen synchronisieren möchten.

![]({% image_buster /assets/img/amplitude8.png %})

Legen Sie schließlich die Häufigkeit Ihrer Synchronisierung fest.

![Definieren Sie Ihre Kadenz als einmalige oder geplante Synchronisierung.]({% image_buster /assets/img/amplitude9.png %})

{% endtab %}
{% endtabs %}

## Amplitude Nutzerprofil API Endpunkte

Einige der gängigen Amplitude API Endpunkte, die mit Connected-Content verwendet werden können, finden Sie in unserer speziellen [Amplitude API Dokumentation]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/amplitude/amplitude_user_profile_api/).
