---
nav_title: mParticle von Rokt
article_title: mParticle von Rokt
alias: /partners/mparticle/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und mParticle, einer Customer Data Platform, die Informationen zwischen Quellen in Ihrem Marketing Stack sammelt und weiterleitet."
page_type: partner
search_tag: Partner

---

# mParticle von Rokt

{% multi_lang_include video.html id="Njhqwd36gZM" align="right" %}

> Mit der Kundendatenplattform von mParticle können Sie mehr aus Ihren Daten machen. Anspruchsvolle Marketer nutzen mParticle zur Orchestrierung von Daten in ihrem gesamten Growth Stack, um in den entscheidenden Momenten der Customer Journey zu gewinnen.

Die Integration von Braze und mParticle erlaubt es Ihnen, den Informationsfluss zwischen den beiden Systemen nahtlos zu steuern:
- Synchronisieren Sie die Zielgruppen von mParticle mit Braze für die Segmentierung von Kampagnen und Canvas.
- Teilen Sie Daten zwischen den beiden Plattformen. Dies kann über die mParticle Kit Integration und die Server-zu-Server Integration erfolgen.
- [Senden Sie die Interaktion von Braze-Nutzern:innen über Currents an mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents/) und machen Sie sie im gesamten Growth Stack nutzbar. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| mParticle Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [mParticle-Konto](https://app.mparticle.com/login). |
| Braze-Instanz | Ihre Braze-Instanz finden Sie auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics/#endpoints) (z. B. `US-01` oder `US-02`). |
| Braze App Bezeichner Schlüssel | Ihr Bezeichner für die App. <br><br>Diese finden Sie im **Braze Dashboard > Einstellungen verwalten > API-Schlüssel**. |
| Workspace REST API-Schlüssel | (Server-zu-Server) Ein Braze REST API-Schlüssel<br><br>Dieser kann über das **Braze-Dashboard > Entwicklungskonsole > API-Einstellungen > API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Zielgruppen

Nutzen Sie die Partnerschaft zwischen Braze und mParticle, um Ihre Integration zu konfigurieren und mParticle Zielgruppen für das Retargeting direkt in Braze zu importieren, so dass ein vollständiger Kreislauf von Daten von einem System zum anderen entsteht. Jede Integration, die Sie einrichten, wird auf das Datenpunktvolumen Ihres Kontos angerechnet.

#### Zielgruppen weiterleiten

mParticle bietet drei Möglichkeiten, Attribute für die Kohortenzugehörigkeit festzulegen, die über die Konfigurationseinstellung "[Segmente senden als](#send_settings)" gesteuert werden. In den folgenden Abschnitten finden Sie Informationen zur Verarbeitung der einzelnen Optionen:

- [Einzelnes String-Attribut](#string)
- [Einzelne Attribute des Arrays](#array)
- [Ein Attribut pro Segment](#per-segment)
- [Sowohl ein einzelnes Attribut für ein Array als auch ein einzelnes Attribut für einen String](#both-1)
- [Sowohl einzelne Attribute als auch ein Attribut pro Segment](#both-2)
- [Sowohl einzelne String Attribute als auch ein Attribut pro Segment](#both-3)
- [Einzelne Array-Attribute, einzelne String-Attribute und ein Attribut pro Segment](#multi)

##### Einzelnes String-Attribut {#string}

mParticle erstellt ein einzelnes angepasstes Attribut namens `SegmentMembership`. Der Wert dieses Attributs ist ein String mit durch Komma getrennten mParticle Zielgruppen IDs, die dem Nutzer:in entsprechen. Diese Zielgruppen IDs finden Sie im mParticle Dashboard unter **Zielgruppen**.

Wenn zum Beispiel eine mParticle Zielgruppe "Ibiza-Träumer" eine Zielgruppen-ID von "11036" hat, können Sie diese Nutzer:innen mit dem Filter `SegmentMembership` - `matches regex` - `11036` segmentieren.

Obwohl dies die Standardoption in mParticle ist, entscheiden sich die meisten Nutzer:innen von Braze dafür, bei der Erstellung von Segmenten in Braze [einzelne Array-Attribute](#array) für die Filterung zu verwenden.

{% alert important %}
Diese Lösung ist nicht empfehlenswert, wenn Sie mehr als ein paar Zielgruppen haben, da angepasste Attribute bis zu 255 Zeichen lang sein können. Sie werden also nicht in der Lage sein, mit dieser Methode Dutzende oder Hunderte von Zielgruppen in einem Nutzerprofil zu speichern. Wenn Sie eine große Anzahl von Kohorten pro Nutzer:innen haben, empfehlen wir dringend die Konfiguration "ein Attribut pro Segment".
{% endalert %}

![mParticle Segmente Mitgliedschaft]({% image_buster /assets/img_archive/mparticle1.png %})

##### Einzelne Attribute des Arrays {#array}

mParticle erstellt in Braze für jeden Nutzer:in ein einzelnes angepasstes Attribut, das `SegmentMembershipArray` heißt. Der Wert dieses Attributs ist ein Array von mParticle Zielgruppen IDs, die mit dem Nutzer:innen übereinstimmen.

Wenn ein Nutzer:innen beispielsweise Mitglied von drei mParticle Zielgruppen mit den IDs "13053", "13052" und "13051" ist, können Sie Nutzer:innen, die einer dieser Zielgruppen entsprechen, mit dem Filter `SegmentMembershipArray` - `includes value` - `13051` segmentieren.

{% alert note %}
Braze Array Attribute haben eine maximale Länge von 25. Wenn einer Ihrer Nutzer:innen Mitglied in mehr als 25 Zielgruppen ist, werden die Mitgliedsdaten von Braze gekürzt. Um dies zu umgehen, wenden Sie sich an Ihre Braze Vertretung, um den Schwellenwert für die maximale Array-Länge zu erhöhen.
{% endalert %}

##### Ein Attribut pro Segment {#per-segment}

mParticle erstellt für jede Zielgruppe, zu der ein Nutzer:in gehört, ein angepasstes Attribut mit Booleschen Werten. Wenn eine mParticle Zielgruppe zum Beispiel "Mögliche Pariser" heißt, können Sie diese Nutzer:innen mit dem Filter `In Possible Parisians` - `equals` - `true` segmentieren.

![mParticle angepasstes Attribut]({% image_buster /assets/img_archive/mparticle2.png %})

##### Sowohl ein einzelnes Attribut für ein Array als auch ein einzelnes Attribut für einen String {#both-1}

mParticle sendet Attribute, die sowohl durch ein einzelnes Array-Attribut als auch durch ein einzelnes String-Attribut beschrieben werden.

##### Sowohl einzelne Attribute als auch ein Attribut pro Segment {#both-2}

mParticle sendet Attribute, die sowohl durch ein einzelnes Array-Attribut als auch durch ein Attribut pro Segment beschrieben werden.

##### Sowohl einzelne String Attribute als auch ein Attribut pro Segment {#both-3}

mParticle sendet Attribute, die sowohl durch ein einzelnes String-Attribut als auch durch ein Attribut pro Segment beschrieben werden.

##### Einzelne Array-Attribute, einzelne String-Attribute und ein Attribut pro Segment {#multi}

mParticle sendet Attribute, die durch ein einzelnes Array-Attribut, ein einzelnes String-Attribut und ein Attribut pro Segment beschrieben werden.

#### Schritt 1: Erstellen Sie eine Zielgruppe in mParticle {#send_settings}

So erstellen Sie eine Zielgruppe in mParticle:

1. Navigieren Sie zu **Zielgruppen** > **Einzelner Workspace** > **\+ Neue Zielgruppe**.
2. Um Braze als Ausgabe für Ihre Zielgruppe zu verbinden, müssen Sie die folgenden Felder angeben:

| Feldname               | Beschreibung                                                                                                                                                                   |
| ------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| API-Schlüssel                  | Zu finden im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**.<br><br>Wenn Sie die ältere Navigation verwenden, finden Sie API-Schlüssel unter **Entwickler**:in > **API-Einstellungen**. |
| API-Schlüssel des Betriebssystems | Wählen Sie aus, zu welchem Betriebssystem Ihr Braze API-Schlüssel gehört. Diese Auswahl schränkt die Arten von Push-Token ein, die bei einem Update der Zielgruppe weitergeleitet werden.                          |
| Segmente senden als         | Die Methode zum Senden von Zielgruppen an Braze. Siehe den Abschnitt [Zielgruppen weiterleiten](#forwarding-audiences) für weitere Informationen.                                                          |
| Workspace REST API-Schlüssel   | REST API-Schlüssel von Braze mit vollen Rechten. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden.                                                        |
| Externer Identitätstyp   | Der mParticle Nutzer:in-Typ, der als externe ID an Braze weitergeleitet werden soll. Wir empfehlen, dies auf dem Standardwert Kunden ID zu belassen.                                          |
| Typ der E-Mail-Identität      | Der Typ der mParticle Nutzer:in, der als E-Mail an Braze weitergeleitet werden soll.                                                                                                            |
| Braze-Instanz           | Geben Sie an, an welchen Cluster Ihre Braze-Daten weitergeleitet werden sollen.                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="3"}
3\. Und schließlich: **Speichern Sie** Ihre Zielgruppe.

Sie sollten die Synchronisierung der Zielgruppen mit Braze innerhalb weniger Minuten sehen. Die Mitgliedschaft in den Zielgruppen wird nur für Nutzer:in mit `external_ids` aktualisiert (d.h. nicht für anonyme Nutzer:innen). Weitere Informationen zur Erstellung von Braze mParticle-Zielgruppen finden Sie in der mParticle-Dokumentation unter [Konfigurationseinstellungen](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings).

#### Schritt 2: Segmentierung der Nutzer:innen in Braze

Um in Braze ein Segment für diese Nutzer:innen zu erstellen, navigieren Sie zu **Segmente** unter **Engagement** und benennen Sie Ihr Segment. Im Folgenden finden Sie zwei Beispiele für Segmente, abhängig von der Option, die Sie für **Segmente senden als** ausgewählt haben. Weitere Einzelheiten zu den einzelnen Optionen finden Sie unter [Weiterleitung von Zielgruppen](#forwarding-audiences.)

- **Einzelnes Attribut eines Arrays:** Wählen Sie `SegmentMembershipArray` als Ihren Filter aus. Verwenden Sie als nächstes die Option "enthält Wert" und geben Sie die gewünschte Zielgruppen-ID ein. ![mParticle Segmente-Filter "SegmentMembershipArray" als "enthält Wert" und Zielgruppen-ID eingestellt..]({% image_buster /assets/img_archive/mparticle5.png %})<br><br>
- **Ein Attribut pro Segment:** Wählen Sie Ihr angepasstes Attribut als Filter aus. Verwenden Sie dann die Option "gleich" und wählen Sie die entsprechende Logik. ![mParticle Segmente Filter "in möglichen Parisern" als "gleich" und "wahr" eingestellt.]({% image_buster /assets/img_archive/mparticle3.png %})

Einmal gespeichert, können Sie dieses Segment bei der Erstellung von Canvas oder Kampagnen im Schritt Targeting Nutzer:innen referenzieren.

#### Deaktivieren und Löschen von Verbindungen

Da mParticle die Segmente in Braze nicht direkt verwaltet, werden die Segmente nicht gelöscht, wenn die entsprechende mParticle-Zielgruppenverbindung gelöscht oder deaktiviert wird. In diesem Fall wird mParticle die Attribute der Nutzer:innen in Braze nicht aktualisieren, um die Zielgruppe von jedem Nutzer zu entfernen.

Um die Zielgruppe eines Braze-Nutzers vor dem Löschen zu entfernen, passen Sie die Zielgruppen-Filter so an, dass die Zielgruppengröße vor dem Löschen einer Zielgruppe auf 0 gesetzt wird. Nachdem die Berechnung der Zielgruppe abgeschlossen ist und 0 Nutzer:innen ergibt, löschen Sie die Zielgruppe. Dann wird die Mitgliedschaft der Zielgruppe in Braze auf `false` für die Option Einzelattribut aktualisiert oder die ID der Zielgruppe wird aus dem Array-Format entfernt.

## Abbildung der Daten

Wenn Sie Ihre mobilen und Web-Apps über mParticle mit Braze verbinden möchten, können Sie die Daten mithilfe der [Embedded Kit Integration](#embedded-kit-integration) in Braze abbilden. Sie können auch die [Server-zu-Server-API-Integration](#server-api-integration) verwenden, um serverseitige Daten an Braze weiterzuleiten.

Unabhängig davon, welchen Ansatz Sie wählen, müssen Sie Braze als Ausgabe einrichten:

### Konfigurieren Sie Ihre Braze-Ausgabeeinstellungen

Navigieren Sie in mParticle zu **Setup > Outputs > Add Outputs** und wählen Sie **Braze**, um die Konfiguration des Braze-Kits zu öffnen. **Speichern Sie**, wenn Sie fertig sind.

| Name der Einstellung | Beschreibung |
| ------------ | ----------- |
| Braze App Bezeichner Schlüssel | Ihren Braze App-Bezeichner-Schlüssel finden Sie im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**. Beachten Sie, dass die API-Schlüssel für jede Plattform (iOS, Android und Internet) unterschiedlich sind. |
| Externer Identitätstyp | Der mParticle Nutzer:in-Typ, der als externe ID an Braze weitergeleitet werden soll. Wir empfehlen, dies auf dem Standardwert zu belassen, Customer ID |
| Typ der E-Mail-Identität | Der Typ der mParticle Nutzer:in, der als E-Mail an Braze weitergeleitet werden soll. Wir empfehlen, dies auf dem Standardwert E-Mail zu belassen, |
| Braze-Instanz | Der Cluster, an den Ihre Braze-Daten weitergeleitet werden; dies sollte derselbe Cluster sein, auf dem sich Ihr Dashboard befindet. |
| Enablement der Weiterleitung von Ereignisströmen | (Server-zu-Server) Wenn diese Option aktiviert ist, werden alle Ereignisse in Realtime weitergeleitet. Wenn nicht, werden alle Ereignisse als Ganzes weitergeleitet. Wenn Sie die Weiterleitung von Ereignisströmen aktivieren, stellen Sie sicher, dass die Daten, die Sie an Braze weiterleiten, die [Rate-Limits]({{site.baseurl}}/api/api_limits/) einhalten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img_archive/configure_settings.png %})

### Integration von Embedded Kits

Das mParticle und Braze SDK wird durch die Integration des Embedded Kits in Ihrer Anwendung vorhanden sein. Im Gegensatz zu einer direkten Braze-Integration kümmert sich mParticle jedoch um den Aufruf der meisten SDK-Methoden von Braze für Sie. Die mParticle Methoden, die Sie zum Tracking von Nutzerdaten verwenden, werden automatisch auf die Braze SDK Methoden abgebildet. 

Diese Abbildungen des SDK von mParticle für [Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy), [iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy) und [Internet](https://github.com/Appboy/integration-appboy) sind Open Source und können auf der [GitHub-Seite von mParticle](https://github.com/mparticle-integrations) gefunden werden. 

Die SDK-Integration des Embedded Kit erlaubt es Ihnen, unsere gesamte Suite an Features zu nutzen (Push, In-App-Nachrichten und alle relevanten Messaging Analytics Tracking).

{% alert note %}
Für Content-Cards und angepasste In-App-Nachrichten-Integrationen rufen Sie die Braze SDK-Methoden direkt auf.
{% endalert %}

#### Schritt 1: Integration der mParticle SDKs

Integrieren Sie die entsprechenden mParticle SDKs in Ihre App, je nach den Anforderungen Ihrer Plattform:

* [mParticle für Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle für iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle für das Internet](https://docs.mparticle.com/developers/sdk/web/getting-started/)

#### Schritt 2: Vollständige Integration des Braze Event-Kits von mParticle

Während das Braze SDK für diese mParticle-Integration nicht direkt in Ihre Website oder App eingebunden werden muss, muss das folgende mParticle Appboy Kit installiert werden, um Daten von Ihrer App an Braze weiterzuleiten.

Der [Leitfaden zur Integration des Braze Event-Kits](https://docs.mparticle.com/integrations/braze/event/#kit-integration) von mParticle führt Sie durch angepasste Anweisungen zur Abstimmung von mParticle und Braze auf Ihre Nachrichten (Push, Standort-Tracking usw.).

#### Schritt 3: Verbindungseinstellungen für Ihren Braze-Ausgang

Navigieren Sie in mParticle zu **Verbindungen > Verbinden > [Ihre gewünschte Plattform] > Ausgang verbinden**, um Braze als Ausgang hinzuzufügen. **Speichern Sie**, wenn Sie fertig sind.

![]({% image_buster /assets/img_archive/mParticle_event_config.png %})

Nicht alle Verbindungseinstellungen gelten für alle Plattformen und Integrationsarten. Eine Aufschlüsselung der Verbindungseinstellungen und der Plattformen, für die sie gelten, finden Sie in der [Dokumentation von mParticle.](https://docs.mparticle.com/integrations/braze/event/#connection-settings)

### Server API Integration

Dies ist ein Add-On, mit dem Sie Ihre Backend-Daten an Braze weiterleiten können, wenn Sie die serverseitigen SDKs von mParticle verwenden (z.B. Ruby, Python, etc.). Um diese Server-zu-Server-Integration mit Braze einzurichten, folgen Sie der [Dokumentation von mParticle.](https://docs.mparticle.com/guides/platform-guide/connections/)

{% alert important %}
Die Server-zu-Server Integration unterstützt keine UI Features von Braze wie In-App-Nachrichten, Content-Cards oder Push-Benachrichtigungen. Es gibt auch automatisch erfasste Daten, wie z.B. Felder auf Geräteebene, die mit dieser Methode nicht verfügbar sind. 

Ziehen Sie eine Side-by-side-Integration in Betracht, wenn Sie diese Features nutzen möchten.

Damit serverseitige Daten an Braze weitergeleitet werden können, müssen sie ein `external_id` enthalten; anonyme Nutzer:innen werden nicht weitergeleitet.
{% endalert %}

#### Verbindungseinstellungen für Ihren Braze-Ausgang

Navigieren Sie in mParticle zu **Verbindungen > Verbinden > [Ihre gewünschte Plattform] > Ausgang verbinden**, um Braze als Ausgang hinzuzufügen. **Speichern Sie**, wenn Sie fertig sind. 

![]({% image_buster /assets/img_archive/mParticle_connections.png %})

Nicht alle Verbindungseinstellungen gelten für alle Plattformen und Integrationsarten. Eine Aufschlüsselung der Verbindungseinstellungen und der Plattformen, für die sie gelten, finden Sie in der [Dokumentation von mParticle.](https://docs.mparticle.com/integrations/braze/event/#connection-settings)

Bevor Sie "Angereicherte Benutzerattribute" oder "Angereicherte Benutzeridentitäten" aktivieren, empfehlen wir Ihnen, die [Mehrkosten für Datenpunkte](#potential-data-point-overages) zu prüfen, um sicherzustellen, dass Sie wissen, wie sich diese Einstellungen auf die Datenpunkt-Nutzung auswirken.

### Details zur Abbildung der Daten

#### Daten-Typen
Nicht alle Datentypen werden von beiden Plattformen unterstützt.
- [Angepasste Event-Eigenschaften]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) unterstützen String-, numerische, boolesche oder Datumsobjekte. Es unterstützt keine Arrays oder verschachtelte Objekte.
- [Angepasste Attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) unterstützen Strings, Zahlen, Boolesche Werte, Datumsobjekte und Arrays, aber keine Objekte oder verschachtelte Objekte. 

{% alert note %}
Braze unterstützt keine Zeitstempel vor Jahr 0 oder nach Jahr 3000 in angepassten Attributen des Typs `Time`. Braze nimmt diese Werte auf, wenn sie von mParticle gesendet werden, aber der Wert wird als String gespeichert.
{% endalert %}

#### Abbildung der Daten

| mParticle Datentyp | Braze Daten Typ | Beschreibung |
| ------------------- | --------------- | ----------- |
| Nutzer:in-Attribute (reserviert) | Standard Attribut | Der reservierte Nutzer:in-Schlüssel von mParticle ( `$FirstName` ) wird beispielsweise dem Standard-Attributfeld für Braze ( `first_name` ) zugeordnet. |
| Attribute der Nutzer:innen (andere) | Angepasstes Attribut | Alle an mParticle übergebenen Nutzer:innen-Attribute, die nicht unter die reservierten Attribute fallen, werden in Braze als angepasstes Attribut protokolliert.<br><br>Nutzer:innen-Attribute unterstützen Strings, Zahlen, Boolesche Werte, Datumsangaben und Arrays, aber keine Objekte oder verschachtelte Objekte. |
| Angepasstes Event | Angepasstes Event | Die angepassten Events von mParticle werden von Braze als angepasste Events erkannt. Event-Attribute werden als angepasste Event-Eigenschaften weitergeleitet.<br><br>Event-Attribute, die als Event-Eigenschaften an Braze übergeben werden, unterstützen String-, numerische, boolesche oder Datums-Objekte, aber keine Arrays oder verschachtelte Objekte. |
| Kauf-Event für den Handel | Kauf-Event | Kauf-Events werden auf Braze Kauf-Events abgebildet. <br><br>Schalten Sie den Einstellungswert für Bundle-Commerce-Ereignisdaten um, um Käufe auf Bestell- oder Produktebene zu protokollieren. Wenn zum Beispiel `false` ein einzelnes eingehendes Ereignis mit zwei eindeutigen Produkten, Aktionen oder Impressionen zu mindestens zwei ausgehenden Braze-Ereignissen führen würde. Bei der Einstellung `true` würde dies zu einem einzigen ausgehenden Ereignis mit einem verschachtelten Array von Produkten, Aktionen bzw. Impressionen führen.<br><br>Weitere Informationen zu den zusätzlichen Handelsfeldern, die protokolliert werden, finden Sie in [der Dokumentation von mParticle.](https://docs.mparticle.com/integrations/braze/event/#purchase-events) <br><br>Wenn Sie "bundle commerce event data" als `false` Produkt-Attribute einstellen, die als Kauf-Event-Eigenschaften an Braze übergeben werden, unterstützen Sie String-, numerische, boolesche oder Datums-Objekte, aber keine Arrays oder verschachtelten Objekte.|
| Alle anderen kommerziellen Ereignisse | Angepasstes Event | Alle anderen Commerce Events werden auf angepasste Events abgebildet. <br><br>Schalten Sie den Einstellungswert für Bundle-Commerce-Ereignisdaten um, um Käufe auf Bestell- oder Produktebene zu protokollieren. Wenn zum Beispiel `false` ein einzelnes eingehendes Ereignis mit zwei eindeutigen Produkten, Aktionen oder Impressionen zu mindestens zwei ausgehenden Braze-Ereignissen führen würde. Bei der Einstellung `true` würde dies zu einem einzigen ausgehenden Ereignis mit einem verschachtelten Array von Produkten, Aktionen bzw. Impressionen führen.<br><br>Zusätzlich zu bestimmten Standard-Commerce-Werten werden Produkt-Attribute als Event-Eigenschaften von Braze protokolliert. Weitere Informationen zu den zusätzlichen Handelsfeldern, die protokolliert werden, finden Sie in [der Dokumentation von mParticle](https://docs.mparticle.com/integrations/braze/event/#other-commerce-events)<br><br>Wenn Sie "bundle commerce event data" als `false` Produkt-Attribute einstellen, die als Event-Eigenschaften an Braze übergeben werden, unterstützen Sie String-, numerische, boolesche oder Datums-Objekte, aber keine Arrays oder verschachtelten Objekte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Abbildung der Nutzer:in
Für jeden mParticle-Ausgang können Sie den externen Identitätstyp auswählen, der an Braze als `external_id` gesendet werden soll. Der Standardwert ist die ID der Kund:in, Sie können aber auch eine andere ID, wie z.B. `MPID`, als `external_id` an Braze senden. Beachten Sie, dass die Wahl eines anderen Bezeichners als der Kund:in ID einen Einfluss darauf haben kann, wie Daten in Braze gesendet werden. 

Die Abbildung der MPID auf Ihre Braze `external_id` hat zum Beispiel folgende Auswirkungen:
- Aufgrund der Art der Zuweisung der MPID wird allen Nutzer:innen bei Sitzungsbeginn eine `external_id` zugewiesen.
- Die Einrichtung von Currents kann aufgrund der unterschiedlichen Datentypen zwischen MPID und `external_id` eine zusätzliche Abbildung erfordern.

### Weiterleitung von Anfragen zur Löschung von Daten (Anfragen von Betroffenen)

Leiten Sie Anfragen zur Löschung von Daten an Braze weiter, indem Sie die Ausgabe von Anfragen zu Daten an Braze konfigurieren. Um Löschanfragen an Braze weiterzuleiten, folgen Sie der [Dokumentation von mParticle.](https://docs.mparticle.com/integrations/braze/forwarding-dsr/)

## Mögliche Mehrkosten für Datenpunkte

### Angereicherte Attribute für Nutzer:innen

#### Enablement der Anreicherung von Nutzer:innen-Attributen/-Identitäten (nur Server-zu-Server) {#enriched}

Braze empfiehlt, in den mParticle-Verbindungseinstellungen die Option **Angereicherte Nutzer:innen-Attribute einbeziehen** zu deaktivieren. Wenn diese Funktion aktiviert ist, leitet mParticle bei jedem protokollierten Event alle verfügbaren Nutzerattribute (wie Standardattribute, angepasste Attribute und berechnete Attribute) aus dem vorhandenen Profil an Braze weiter. Dies führt zu einem hohen Verbrauch an Datenpunkten, da mParticle Braze bei jedem Aufruf die gleichen unveränderten Attribute sendet.

Wenn ein Nutzer:innen z.B. bei seiner ersten Sitzung Vorname, Nachname und Telefonnummer angibt und sich später für einen Newsletter anmeldet, indem er dieselben Informationen zusätzlich zu seiner E-Mail hinzufügt, wird ein Newsletter-Registrierungsereignis ausgelöst:
- Wenn diese Option aktiviert ist (Standard), fallen fünf Datenpunkte an. (Registrierungsereignis, E-Mail Adresse, Vorname, Nachname und Telefonnummer)
- Wenn Sie diese Option deaktivieren, fallen zwei Datenpunkte an (Registrierungsereignis und E-Mail Adresse)

{% alert note %}
Wenn Sie diese Einstellung deaktivieren, wird nicht auf sich ändernde Daten geprüft. Sie verhindert jedoch, dass die Integration alle Attribute im Profil des Nutzers sendet, die nicht in der ursprünglichen eingehenden Charge empfangen oder explizit als Attribut für das Ereignis festgelegt wurden. Es ist wichtig, dass Sie trotzdem sicherstellen, dass nur Deltas an Braze weitergegeben werden.
{% endalert %}

#### Überlegungen zur Deaktivierung von angereicherten Nutzer:innen-Attributen

Bei der Deaktivierung der Option **Angereicherte Nutzer:innen Attribute einbeziehen** gibt es einige Dinge zu beachten:
1. Die Server-zu-Server Integration verwendet die mParticle events API, um Ereignisse an Braze zu senden. Jede Anfrage wird durch ein Ereignis ausgelöst. Wenn ein Benutzerattribut geändert wird, wie z.B. das Update einer E-Mail-Adresse, aber nicht mit einem bestimmten Event verbunden ist (z.B. ein angepasstes Event zur Profil-Aktualisierung), wird der neue Wert nur als "angereichertes Attribut" in der Payload des nächsten vom Benutzer getriggerten Events an eine Ausgabe wie Braze weitergegeben. Wenn **Include Enriched User Attributes** ausgeschaltet ist, wird dieser neue Attributwert, der nicht mit einem bestimmten Ereignis verknüpft ist, nicht an Braze weitergegeben.
  - Um dieses Problem zu lösen, empfehlen wir Ihnen, ein separates Ereignis "Nutzer:innen aktualisiert" zu erstellen, das nur die spezifischen Nutzer:innen-Attribute, die aktualisiert wurden, an Braze sendet. Beachten Sie, dass Sie bei diesem Ansatz zwar immer noch einen zusätzlichen Datenpunkt für das Ereignis "Update der Nutzer:innen-Attribute" protokollieren, der Verbrauch an Datenpunkten jedoch weitaus geringer ist als das Senden aller Nutzer:innen-Attribute bei jedem Anruf, bei dem das Feature aktiviert ist.
2. Berechnete Attribute werden als angereicherte Nutzer:innen-Attribute an Braze weitergegeben. Wenn also "Angereicherte Nutzer:innen-Attribute" deaktiviert ist, werden diese nicht mehr an Braze weitergegeben. Um berechnete Attribute an Braze weiterzuleiten, wenn "Angereicherte Nutzer:innen"-Attribute ausgeschaltet sind, könnte ein [berechneter Attribut-Feed](https://docs.mparticle.com/guides/platform-guide/calculated-attributes/using-calculated-attributes/#forward-calculated-attributes-in-the-calculated-attributes-feed) helfen, ohne alle Attribute zu pushen. Der Feed gibt ein Update an Braze weiter, wenn sich ein berechnetes Attribut ändert. 

### Senden von unnötigen oder doppelten Daten an Braze
Braze zählt jedes Mal einen Datenpunkt, wenn ein Attribut an Braze übergeben wird, auch wenn der Wert unverändert ist. Aus diesem Grund empfiehlt Braze, nur Daten weiterzuleiten, die für Aktionen innerhalb von Braze benötigt werden, und sicherzustellen, dass nur Deltas von Attributen weitergegeben werden.

