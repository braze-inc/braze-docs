---
nav_title: Segment Engage
article_title: Segment Engage
page_order: 3
alias: /partners/segment_personas/
alias: /partners/segment_engage/
alias: /partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_personas/

description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Segment, einer Plattform für Kundendaten, die Informationen sammelt und zwischen den Quellen in Ihrem Marketing-Stack weiterleitet."
page_type: partner
search_tag: Partner

---

# Segment Engage

> [Segment](https://segment.com) ist eine Plattform für Kundendaten, mit der Sie Ihre Kundendaten sammeln, bereinigen und aktivieren können. Dieser Referenzartikel gibt einen Überblick über die Verbindung zwischen [Braze und Segment Engage](https://segment.com/docs/destinations/braze/#Engage) und beschreibt die Anforderungen und Prozesse für die ordnungsgemäße Implementierung und Nutzung.

Mit der Integration von Braze und Segment können Sie [Engage](https://segment.com/docs/engage/), den integrierten Audience Builder von Segment, verwenden, um Nutzersegmente auf der Grundlage von Daten zu erstellen, die Sie bereits über verschiedene Quellen gesammelt haben. Diese Zielgruppen werden dann mit Braze als Kohorte synchronisiert oder im Benutzerprofil durch [benutzerdefinierte Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) oder [benutzerdefinierte Ereignisse]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) gekennzeichnet, die zur Erstellung von Braze-Segmenten für Kampagnen und Canvas-Retargeting verwendet werden können.

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Segment-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, ist ein [Segment-Konto](https://app.segment.com/login) erforderlich. |
| Ziel der Braze Cloud | Sie müssen [Braze]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) bereits [als Ziel]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) in Ihrer Segment-Integration [eingerichtet]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) haben.<br><br>Dazu gehört die Angabe des richtigen Braze-Rechenzentrums und des REST-API-Schlüssels in Ihren [Verbindungseinstellungen]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings). |
| Schlüssel für den Import von Lötdaten | Um Engage-Zielgruppen als Kohorten mit Braze zu synchronisieren, müssen Sie einen Datenimportschlüssel erstellen.<br><br>Der Kohortenimport befindet sich im Frühstadium. Wenden Sie sich an Ihren Braze Customer Success Manager, um Zugang zu dieser Funktion zu erhalten. |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Kohorten Zielortintegration

### Schritt 1: Publikum einbinden
1. Navigieren Sie in Segment zur Registerkarte **Zielgruppen** in Engage und klicken Sie auf **Neu**.
2. Schaffen Sie Ihr Publikum. Ein Blitz in der oberen Ecke der Seite zeigt an, ob das Publikum in Echtzeit aktualisiert wird.
3. Wählen Sie dann Braze als Ziel aus.
4. Zeigen Sie eine Vorschau Ihrer Zielgruppe an, indem Sie auf **Überprüfen & Erstellen** klicken. Standardmäßig fragt Segment alle historischen Daten ab, um den aktuellen Wert des berechneten Merkmals und der Zielgruppe festzulegen. Um diese Daten auszulassen, deaktivieren Sie die Option **Historisches Backfill**.

### Schritt 2: Erfassen Sie den Importschlüssel für Ihre Kohortendaten

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Segment**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

Hier finden Sie Ihren REST-Endpunkt und generieren Ihren Braze-Datenimportschlüssel. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen.

### Schritt 3: Verbinden Sie die Braze Cohorts Ziel
Folgen Sie den [Anweisungen von Segment](https://segment.com/docs/connections/destinations/catalog/actions-braze-cohorts/#getting-started) zur Einrichtung der Kohorten-Destination, um Ihre Engage-Zielgruppen als Kohorten mit Braze zu synchronisieren.

### Schritt 4: Erstellen Sie ein Braze-Segment aus der Engage-Zielgruppe
Navigieren Sie in Braze zu **Segmente**, erstellen Sie ein neues Segment und wählen Sie **Segmentkohorten** als Filter. Von hier aus können Sie wählen, welche Segmentkohorte Sie einbeziehen möchten. Nachdem das Kohortensegment Segment erstellt wurde, können Sie es bei der Erstellung einer Kampagne oder eines Canvas als Zielgruppenfilter auswählen.

![][1]

## Integration des Cloud-Modus

### Schritt 1: Erstellen Sie ein Segment mit berechneten Merkmalen oder einer Zielgruppe

1. Navigieren Sie in Segment zur Registerkarte **Computed Traits** oder **Audiences** in **Engage** und klicken Sie auf **Neu**.
2. Schaffen Sie Ihre berechnete Eigenschaft oder Ihr Publikum. Ein Blitz in der oberen Ecke der Seite zeigt an, ob die Berechnung in Echtzeit aktualisiert wird.
3. Wählen Sie als nächstes **Braze** als Ihr Ziel aus. 
4. Zeigen Sie eine Vorschau Ihrer Zielgruppe an, indem Sie auf **Überprüfen & Erstellen** klicken. Standardmäßig fragt Segment alle historischen Daten ab, um den aktuellen Wert des berechneten Merkmals und der Zielgruppe festzulegen. Um diese Daten auszulassen, deaktivieren Sie die Option **Historisches Backfill**.
5. Passen Sie in den Einstellungen für die berechnete Eigenschaft oder die Zielgruppe die Verbindungseinstellungen an, je nachdem, wie Sie Ihre Daten an Braze senden möchten.

#### Berechnete Eigenschaften und Zielgruppen

Die [berechneten Merkmale](https://segment.com/docs/engage/audiences/computed-traits/) und [Zielgruppen](https://segment.com/docs/Engage/audiences/) können als benutzerdefinierte Attribute oder benutzerdefinierte Ereignisse an Braze gesendet werden.
- Traits und Audiences, die über den Aufruf `identify` gesendet werden, erscheinen in Braze als benutzerdefinierte Attribute.
- Traits und Audiences, die über den Aufruf `track` gesendet werden, erscheinen in Braze als benutzerdefinierte Ereignisse.

Sie können wählen, welche Methode Sie verwenden möchten (oder Sie verwenden beide), wenn Sie die berechnete Eigenschaft mit dem Braze-Ziel verbinden.

{% tabs %}
{% tab Identifizieren Sie %}

Sie können berechnete Traits und Audiences als `identify` Aufrufe an Braze senden, um benutzerdefinierte Attribute in Braze zu erstellen. 

Wenn Sie zum Beispiel eine von Engage berechnete Eigenschaft für "Zuletzt angesehenes Produkt" haben, finden Sie `last_product_viewed_item` im Braze-Profil des Benutzers unter **Benutzerdefinierte Attribute**. Wenn es sich stattdessen um eine Engage-Zielgruppe handeln würde, würden Sie Ihre Zielgruppe unter **Benutzerdefinierte Attribute** als `true` aufgeführt finden.

| Berechnetes Merkmal | Publikum |
| -------------- | --------- |
| ![Der Abschnitt für benutzerdefinierte Attribute in einem Benutzerprofil führt "last_product_viewed_item" als "Pullover" auf.]({% image_buster /assets/img/segment/last_viewed-id-braze.png %}) | ![Im Abschnitt für benutzerdefinierte Attribute in einem Benutzerprofil wird "dormant_shopper" als "true" aufgeführt.]({% image_buster /assets/img/segment/dormant-identify-braze.png %}) |

{% endtab %}
{% tab Spur %}

Sie können berechnete Eigenschaften und Zielgruppen als `track` Aufrufe an Braze senden, um benutzerdefinierte Ereignisse in Braze zu erstellen. 

Um das vorherige Beispiel fortzusetzen: Wenn ein Benutzer eine berechnete Eigenschaft für "Zuletzt angesehenes Produkt" hat, wird diese auf den Braze-Profilen der Benutzer als `Trait Computed` mit der entsprechenden Anzahl und dem letzten Zeitstempel unter **Benutzerdefinierte Ereignisse** angezeigt. Wenn es sich stattdessen um eine Engage-Zielgruppe handeln würde, würden Sie Ihre Zielgruppe, die Anzahl und den letzten Zeitstempel unter **Benutzerdefinierte Attribute** als `true` aufgeführt finden.

| Berechnetes Merkmal | Publikum |
| -------------- | --------- |
| ![Der Abschnitt für benutzerdefinierte Ereignisse in einem Benutzerprofil listet "Trait Computed" "1" Mal auf, wobei das letzte Mal "vor 20 Stunden" war.]({% image_buster /assets/img/segment/last_viewed-track-braze.png %}) | ![Der Abschnitt für benutzerdefinierte Attribute innerhalb eines Benutzerprofils listet die Zeit "Audience Entered" "1" auf, wobei der letzte Zeitpunkt "9\. März um 1:45 Uhr" ist.]({% image_buster /assets/img/segment/dormant-track-braze.png %}) |

{% endtab %}
{% endtabs %}

### Schritt 2: Segmentierte Benutzer in Braze

Um in Braze ein Segment dieser Benutzer zu erstellen, navigieren Sie zu **Segmente** unter **Engagement**, erstellen ein neues Segment und benennen Ihr Segment. Als nächstes, je nachdem, welchen Anruf Sie verwendet haben:
- **Identifizieren Sie sich**: Wählen Sie **benutzerdefiniertes Attribut** als Filter und suchen Sie Ihr benutzerdefiniertes Attribut. Verwenden Sie dann die Option "matches regex" (Eigenschaft) oder die Option "equals" (Publikum) und geben Sie die entsprechende Variable ein.
- **Titel**: Wählen Sie **benutzerdefiniertes Ereignis** als Filter und suchen Sie Ihr benutzerdefiniertes Ereignis. Verwenden Sie dann die Option "mehr als", "weniger als" oder "genau" und geben Sie den gewünschten Wert ein. Dies hängt davon ab, wie Sie Ihr Segment definieren möchten.

Sobald Sie es gespeichert haben, können Sie dieses Segment bei der Erstellung von Canvas oder Kampagnen im Schritt "Benutzer ansprechen" verwenden.

## Synchronisationszeit

Obwohl die Standardeinstellung für die Verbindung zwischen Braze und Segment Engage `Realtime` ist, gibt es einige Filter, die die Persona von der Synchronisierung in Echtzeit ausschließen, einschließlich einiger zeitbasierter Filter, die die Größe Ihrer Zielgruppe zum Zeitpunkt des Nachrichtenversands einschränken.

## Segment-Debugger-Tests

Das Dashboard von Segment bietet eine "Debugger"-Funktion, mit der Kunden testen können, ob die Daten von einer "Quelle" wie erwartet an ein "Ziel" übertragen werden.

Diese Funktion stellt eine Verbindung zum Braze [`/users/track` Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) her, was bedeutet, dass sie nur für identifizierte Benutzer verwendet werden kann (Benutzer, die bereits eine Benutzer-ID für ihr Braze-Benutzerprofil haben).

Dies funktioniert nicht für eine nebeneinander liegende Braze-Integration. Es werden keine Serverdaten übertragen, wenn Sie nicht die richtigen Braze REST API-Informationen eingegeben haben.

[1]: {% image_buster /assets/img/segment/segment3.png %}