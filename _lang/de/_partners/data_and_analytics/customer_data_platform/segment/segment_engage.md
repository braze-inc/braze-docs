---
nav_title: Segmente Engagieren
article_title: Segmente Engagieren
page_order: 3
alias: /partners/segment_personas/
alias: /partners/segment_engage/
alias: /partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_personas/

description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Segment, einer Customer Data Platform, die Informationen sammelt und zwischen den Quellen in Ihrem Marketing Stack weiterleitet."
page_type: partner
search_tag: Partner

---

# Segmente Engagieren

> [Segmente](https://segment.com) ist eine Customer Data Platform (CDP), mit der Sie Ihre Kundendaten sammeln, bereinigen und aktivieren können. Dieser referenzierte Artikel gibt eine Übersicht über die Verbindung zwischen [Braze und Segment Engage](https://segment.com/docs/destinations/braze/#Engage) und beschreibt die Anforderungen und Prozesse für die ordnungsgemäße Implementierung und Nutzung.

Die Integration von Braze und Segment erlaubt es Ihnen, mit [Engage](https://segment.com/docs/engage/), dem integrierten Audience-Builder von Segment, Segmente von Nutzer:innen auf der Grundlage von Daten zu erstellen, die Sie bereits über verschiedene Quellen gesammelt haben. Diese Zielgruppen werden dann mit Braze als Kohorte synchronisiert oder auf dem Kundenprofil durch [angepasste Attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) oder [angepasste Events]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) gekennzeichnet, die zur Erstellung von Braze-Segmenten für das Retargeting in Kampagnen und Canvas verwendet werden können.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Segmente Konto | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein [Segment-Konto](https://app.segment.com/login) erforderlich. |
| Braze Cloud Ziel | Sie müssen bereits in Ihrer Segment-Integration [Braze als Zie eingerichtet]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) haben.<br><br>Dazu gehört die Angabe des richtigen Braze Datenzentrums und des REST API-Schlüssels in Ihren [Verbindungseinstellungen]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings). |
| Braze Datenimport-Schlüssel | Um die Zielgruppen von Engage als Kohorten mit Braze zu synchronisieren, müssen Sie einen Datenimport-Schlüssel erstellen.<br><br>Der Kohortenimport befindet sich im Frühstadium. Wenden Sie sich an Ihren Customer-Success-Manager:in, um Zugriff auf dieses Feature zu erhalten. |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Kohorten Ziel-Integration

### Schritt 1: Erstellen Sie eine Zielgruppe für Engage
1. Gehen Sie in Segmente auf den Tab **Zielgruppen** in Engage und klicken Sie auf **Neu**.
2. Schaffen Sie Ihre Zielgruppe. Ein Blitz in der oberen Ecke der Seite zeigt an, ob die Zielgruppe in Realtime aktualisiert wird.
3. Wählen Sie dann Braze als Ihr Ziel aus.
4. Machen Sie eine Vorschau Ihrer Zielgruppe, indem Sie auf **Überprüfen & Erstellen** klicken. Standardmäßig fragt Segmente alle historischen Daten ab, um den aktuellen Wert des berechneten Merkmals und der Zielgruppe festzulegen. Um diese Daten auszulassen, deaktivieren Sie die Option **Historisches Backfill**.

### Schritt 2: Erfassen Sie den Datenimport-Schlüssel für Ihre Kohorte

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Segmentierung**.

Hier finden Sie Ihren REST-Endpunkt und generieren Ihren Datenimport-Schlüssel für Braze. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen.

### Schritt 3: Verbinden Sie die Braze Kohorten Ziel
Folgen Sie den [Anweisungen von Segment](https://segment.com/docs/connections/destinations/catalog/actions-braze-cohorts/#getting-started) zur Einrichtung der Kohorten-Zielgruppen, um Ihre Engage Zielgruppen als Kohorten mit Braze zu synchronisieren.

### Schritt 4: Erstellen Sie ein Braze Segment aus der Engage Zielgruppe
Navigieren Sie in Braze zu **Segmente**, erstellen Sie ein neues Segment und wählen Sie **Segmente Kohorten** als Filter. Von hier aus können Sie wählen, welche Segmente der Kohorte Sie einbeziehen möchten. Nachdem das Segment Kohorte erstellt wurde, können Sie es als Zielgruppen-Filter auswählen, wenn Sie eine Kampagne oder ein Canvas erstellen.

![]({% image_buster /assets/img/segment/segment3.png %})

## Integration des Cloud-Modus

### Schritt 1: Erstellen Sie eine Segmente berechnete Eigenschaft oder Zielgruppe

1. Gehen Sie in Segmente auf den Tab **Berechnete Merkmale** oder **Zielgruppen** in **Engage** und klicken Sie auf **Neu**.
2. Erstellen Sie Ihre rechnerische Eigenschaft oder Zielgruppe. Ein Blitz in der oberen Ecke der Seite zeigt an, ob die Berechnung in Realtime aktualisiert wird.
3. Wählen Sie dann **Braze** als Ihr Ziel aus. 
4. Machen Sie eine Vorschau Ihrer Zielgruppe, indem Sie auf **Überprüfen & Erstellen** klicken. Standardmäßig fragt Segmente alle historischen Daten ab, um den aktuellen Wert des berechneten Merkmals und der Zielgruppe festzulegen. Um diese Daten auszulassen, deaktivieren Sie die Option **Historisches Backfill**.
5. Passen Sie in den Einstellungen für berechnete Merkmale oder Zielgruppen die Verbindungseinstellungen an, je nachdem, wie Sie Ihre Daten an Braze senden möchten.

#### Berechnete Merkmale und Zielgruppen

[Berechnete Attribute](https://segment.com/docs/engage/audiences/computed-traits/) und [Zielgruppen](https://segment.com/docs/Engage/audiences/) können als angepasste Attribute oder angepasste Events an Braze gesendet werden.
- Merkmale und Zielgruppen, die über den Aufruf `identify` gesendet werden, erscheinen in Braze als angepasste Attribute.
- Traits und Zielgruppen, die über den Aufruf `track` gesendet werden, erscheinen in Braze als angepasste Events.

Sie können wählen, welche Methode Sie verwenden möchten (oder Sie verwenden beide), wenn Sie die berechnete Spur mit dem Braze-Ziel verbinden.

{% tabs %}
{% tab Identifizieren %}

Sie können berechnete Attribute und Zielgruppen als `identify` -Aufrufe an Braze senden, um angepasste Attribute in Braze zu erstellen. 

Wenn Sie z.B. ein von Engage berechnetes Attribut für "Zuletzt gesehener Artikel" haben, finden Sie `last_product_viewed_item` im Profil des Nutzers:in unter **Angepasste Attribute**. Wäre dies stattdessen eine Engage-Zielgruppe, würden Sie Ihre Zielgruppe unter **Angepasste Attribute** als `true` aufgeführt finden.

| Berechnetes Merkmal | Zielgruppen |
| -------------- | --------- |
| ![Der Abschnitt für angepasste Attribute in einem Nutzerprofil listet "last_product_viewed_item" als "Pullover" auf.]({% image_buster /assets/img/segment/last_viewed-id-braze.png %}) | ![Im Abschnitt für angepasste Attribute in einem Nutzerprofil wird "dormant_shopper" als "true" aufgeführt.]({% image_buster /assets/img/segment/dormant-identify-braze.png %}) |

{% endtab %}
{% tab Tracking %}

Sie können berechnete Merkmale und Zielgruppen als `track` Aufrufe an Braze senden, um angepasste Events in Braze zu erstellen. 

Um das vorherige Beispiel fortzusetzen: Wenn ein Nutzer eine berechnete Eigenschaft für "Zuletzt gesehener Artikel" hat, erscheint diese auf den Profilen der Nutzer:innen in Braze als `Trait Computed` mit der entsprechenden Anzahl und dem letzten Zeitstempel unter **Angepasste Events**. Wäre dies stattdessen eine Engage-Zielgruppe, würden Sie Ihre Zielgruppe, die Anzahl und den letzten Zeitstempel unter **Angepasste Attribute** als `true` finden.

| Berechnetes Merkmal | Zielgruppen |
| -------------- | --------- |
| ![Der Abschnitt für angepasste Events innerhalb eines Nutzerprofils listet "Trait Computed" "1" Zeit auf, wobei der letzte Zeitpunkt "vor 20 Stunden" liegt.]({% image_buster /assets/img/segment/last_viewed-track-braze.png %}) | ![Der Abschnitt für angepasste Attribute innerhalb eines Nutzerprofils listet die Zeit "Zielgruppe eingegeben" "1" auf, wobei die letzte Zeit "9\. März um 1:45 Uhr" ist.]({% image_buster /assets/img/segment/dormant-track-braze.png %}) |

{% endtab %}
{% endtabs %}

### Schritt 2: Segmentierung der Nutzer:innen in Braze

Um in Braze ein Segment dieser Nutzer:innen zu erstellen, navigieren Sie zu **Segmente** unter **Engagement**, erstellen ein neues Segment und benennen Ihr Segment. Als nächstes, je nachdem, welchen Anruf Sie verwendet haben:
- **Bezeichner**: Wählen Sie **angepasstes Attribut** als Filter und suchen Sie Ihr angepasstes Attribut. Verwenden Sie dann die Option "matches regex" (Eigenschaft) oder die Option "equals" (Zielgruppe) und geben Sie die entsprechende Variable ein.
- **Tracking**: Wählen Sie als Filter **angepasste Events** aus und suchen Sie nach Ihrem angepassten Event. Verwenden Sie dann die Option "mehr als", "weniger als" oder "genau" und geben Sie den gewünschten Wert ein. Dies hängt davon ab, wie Sie Ihr Segment definieren möchten.

Einmal gespeichert, können Sie dieses Segment bei der Erstellung von Canvas oder Kampagnen im Schritt Targeting Nutzer:innen referenzieren.

## Synchronisationszeit

Obwohl die Standardeinstellung für die Verbindung von Braze zu Segment Engage `Realtime` ist, gibt es einige Filter, die die Persona von der Synchronisierung in Realtime ausschließen, einschließlich einiger zeitbasierter Filter, die die Größe Ihrer Zielgruppe zum Zeitpunkt des Versands der Nachricht einschränken.

## Testen von Segmenten mit dem Debugger

Das Dashboard von Segmente bietet ein "Debugger"-Feature, mit dem Kunden testen können, ob die Daten von einer "Quelle" wie erwartet an ein "Ziel" übertragen werden.

Dieses Feature stellt eine Verbindung zum [`/users/track` Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) von Braze  her, d.h. es kann nur für identifizierte Nutzer:innen verwendet werden (Nutzer:innen, die bereits eine ID für ihr Braze Nutzerprofil haben).

Dies funktioniert nicht bei einer Side-by-side-Integration von Braze. Es werden keine Daten des Servers übertragen, wenn Sie nicht die richtigen Braze REST API-Informationen eingegeben haben.

