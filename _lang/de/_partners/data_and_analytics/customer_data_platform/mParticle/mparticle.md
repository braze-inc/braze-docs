---
nav_title: mParticle von Rokt
article_title: mParticle von Rokt
alias: /partners/mparticle/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und mParticle, einer Customer Data Platform, die Informationen zwischen Quellen in Ihrem Marketing Stack sammelt und weiterleitet."
page_type: partner
search_tag: Partner

---

# mParticle von Rokt

{% multi_lang_include video.html id="Njhqwd36gZM" align="right" %}

> Mit der Customer Data Platform von mParticle können Sie mehr aus Ihren Daten machen. Anspruchsvolle Marketer nutzen mParticle zur Orchestrierung von Daten in ihrem gesamten Growth Stack, um in den entscheidenden Momenten der Customer Journey zu überzeugen.

Die Integration von Braze und mParticle erlaubt es Ihnen, den Informationsfluss zwischen den beiden Systemen nahtlos zu steuern:
- Synchronisieren Sie mParticle-Zielgruppen mit Braze für die Segmentierung von Kampagnen und Canvas.
- Teilen Sie Daten zwischen den beiden Plattformen. Dies kann über die mParticle-Kit-Integration und die Server-zu-Server-Integration erfolgen.
- [Senden Sie Braze-Nutzerinteraktionen über Currents an mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle_for_currents/) und machen Sie sie im gesamten Growth Stack nutzbar. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| mParticle-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [mParticle-Konto](https://app.mparticle.com/login). |
| Braze-Instanz | Ihre Braze-Instanz finden Sie auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics/#endpoints) (z. B. `US-01` oder `US-02`). |
| Braze-App-Bezeichner-Schlüssel | Ihr App-Bezeichner-Schlüssel. <br><br>Diesen finden Sie unter **Einstellungen verwalten** > **API-Schlüssel** im Braze-Dashboard. |
| Workspace-REST-API-Schlüssel | (Server-zu-Server) Ein Braze-REST-API-Schlüssel<br><br>Dieser kann unter **Entwicklungskonsole** > **API-Einstellungen** > **API-Schlüssel** im Braze-Dashboard erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Zielgruppen

Nutzen Sie die Partnerschaft zwischen Braze und mParticle, um Ihre Integration zu konfigurieren und mParticle-Zielgruppen für das Retargeting direkt in Braze zu importieren, sodass ein vollständiger Datenkreislauf von einem System zum anderen entsteht. 

Jede Integration, die Sie einrichten, protokolliert Datenpunkte. Wenn Sie Fragen zu den Besonderheiten der Braze-Datenpunkte haben, kann Ihr Braze Account Manager diese beantworten.

#### Zielgruppen weiterleiten

mParticle bietet drei Möglichkeiten, Attribute für die Kohortenzugehörigkeit festzulegen, die über die Konfigurationseinstellung „[Segmente senden als](#send_settings)" gesteuert werden. In den folgenden Abschnitten finden Sie Informationen zur Verarbeitung der einzelnen Optionen:

- [Einzelnes String-Attribut](#string)
- [Einzelnes Array-Attribut](#array)
- [Ein Attribut pro Segment](#per-segment)
- [Sowohl einzelnes Array-Attribut als auch einzelnes String-Attribut](#both-1)
- [Sowohl einzelnes Array-Attribut als auch ein Attribut pro Segment](#both-2)
- [Sowohl einzelnes String-Attribut als auch ein Attribut pro Segment](#both-3)
- [Einzelnes Array-Attribut, einzelnes String-Attribut und ein Attribut pro Segment](#multi)

##### Einzelnes String-Attribut {#string}

mParticle erstellt ein einzelnes angepasstes Attribut namens `SegmentMembership`. Der Wert dieses Attributs ist ein String mit durch Komma getrennten mParticle-Zielgruppen-IDs, die dem/der Nutzer:in entsprechen. Diese Zielgruppen-IDs finden Sie im mParticle-Dashboard unter **Audiences**.

Wenn zum Beispiel eine mParticle-Zielgruppe „Ibiza dreamers" die Zielgruppen-ID „11036" hat, können Sie diese Nutzer:innen mit dem Filter `SegmentMembership` — `matches regex` — `11036` segmentieren.

Obwohl dies die Standardoption in mParticle ist, entscheiden sich die meisten Unternehmensnutzer:innen dafür, bei der Erstellung von Segmenten in Braze [einzelne Array-Attribute](#array) für ein besseres Filtererlebnis zu verwenden.

{% alert important %}
Diese Lösung ist nicht empfehlenswert, wenn Sie mehr als ein paar Zielgruppen haben, da angepasste Attribute bis zu 255 Zeichen lang sein können. Sie werden also nicht in der Lage sein, mit dieser Methode Dutzende oder Hunderte von Zielgruppen in einem Nutzerprofil zu speichern. Wenn Sie eine große Anzahl von Kohorten pro Nutzer:in haben, empfehlen wir dringend die Konfiguration „ein Attribut pro Segment".
{% endalert %}

![mParticle Segment-Mitgliedschaft]({% image_buster /assets/img_archive/mparticle1.png %})

##### Einzelnes Array-Attribut {#array}

mParticle erstellt in Braze für jede:n Nutzer:in ein einzelnes angepasstes Array-Attribut namens `SegmentMembershipArray`. Der Wert dieses Attributs ist ein Array von mParticle-Zielgruppen-IDs, die mit dem/der Nutzer:in übereinstimmen.

Wenn ein:e Nutzer:in beispielsweise Mitglied von drei mParticle-Zielgruppen mit den IDs „13053", „13052" und „13051" ist, können Sie Nutzer:innen, die einer dieser Zielgruppen entsprechen, mit dem Filter `SegmentMembershipArray` — `includes value` — `13051` segmentieren.

{% alert note %}
Braze-Array-Attribute haben eine maximale Länge von 25. Wenn eine:r Ihrer Nutzer:innen Mitglied in mehr als 25 Zielgruppen ist, werden die Mitgliedschaftsinformationen von Braze gekürzt. Um dies zu umgehen, wenden Sie sich an Ihre Braze-Vertretung, um den Schwellenwert für die maximale Array-Länge zu erhöhen.
{% endalert %}

##### Ein Attribut pro Segment {#per-segment}

mParticle erstellt für jede Zielgruppe, zu der ein:e Nutzer:in gehört, ein angepasstes Attribut vom Typ Boolescher Wert. Wenn eine mParticle-Zielgruppe zum Beispiel „Possible Parisians" heißt, können Sie diese Nutzer:innen mit dem Filter `In Possible Parisians` — `equals` — `true` segmentieren.

![mParticle angepasstes Attribut]({% image_buster /assets/img_archive/mparticle2.png %})

##### Sowohl einzelnes Array-Attribut als auch einzelnes String-Attribut {#both-1}

mParticle sendet Attribute wie sowohl für das einzelne Array-Attribut als auch für das einzelne String-Attribut beschrieben.

##### Sowohl einzelnes Array-Attribut als auch ein Attribut pro Segment {#both-2}

mParticle sendet Attribute wie sowohl für das einzelne Array-Attribut als auch für ein Attribut pro Segment beschrieben.

##### Sowohl einzelnes String-Attribut als auch ein Attribut pro Segment {#both-3}

mParticle sendet Attribute wie sowohl für das einzelne String-Attribut als auch für ein Attribut pro Segment beschrieben.

##### Einzelnes Array-Attribut, einzelnes String-Attribut und ein Attribut pro Segment {#multi}

mParticle sendet Attribute wie für das einzelne Array-Attribut, das einzelne String-Attribut und ein Attribut pro Segment beschrieben.

#### 1. Schritt: Erstellen Sie eine Zielgruppe in mParticle {#send_settings}

So erstellen Sie eine Zielgruppe in mParticle:

1. Navigieren Sie zu **Audiences** > **Single Workspace** > **+ New Audience**.
2. Um Braze als Ausgabe für Ihre Zielgruppe zu verbinden, müssen Sie die folgenden Felder angeben:

| Feldname               | Beschreibung                                                                                                                                                                   |
| ------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| API-Schlüssel                  | Zu finden im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**.<br><br>Wenn Sie die ältere Navigation verwenden, finden Sie API-Schlüssel unter **Entwicklungskonsole** > **API-Einstellungen**. |
| API-Schlüssel-Betriebssystem | Wählen Sie aus, zu welchem Betriebssystem Ihr Braze-API-Schlüssel gehört. Diese Auswahl schränkt die Arten von Push-Token ein, die bei einem Update der Zielgruppe weitergeleitet werden.                          |
| Segmente senden als         | Die Methode zum Senden von Zielgruppen an Braze. Siehe den Abschnitt [Zielgruppen weiterleiten](#forwarding-audiences) für weitere Informationen.                                                          |
| Workspace-REST-API-Schlüssel   | Braze-REST-API-Schlüssel mit vollen Berechtigungen. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden.                                                        |
| Externer Identitätstyp   | Der mParticle-Nutzeridentitätstyp, der als externe ID an Braze weitergeleitet werden soll. Wir empfehlen, dies auf dem Standardwert Customer ID zu belassen.                                          |
| E-Mail-Identitätstyp      | Der mParticle-Nutzeridentitätstyp, der als E-Mail an Braze weitergeleitet werden soll.                                                                                                            |
| Braze-Instanz           | Geben Sie an, an welchen Cluster Ihre Braze-Daten weitergeleitet werden sollen.                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="3"}
3. Abschließend **speichern** Sie Ihre Zielgruppe.

Die Synchronisierung der Zielgruppen mit Braze sollte innerhalb weniger Minuten beginnen. Die Zielgruppenmitgliedschaft wird nur für Nutzer:innen mit `external_ids` aktualisiert (d. h. nicht für anonyme Nutzer:innen). Weitere Informationen zur Erstellung von Braze-mParticle-Zielgruppen finden Sie in der mParticle-Dokumentation unter [Konfigurationseinstellungen](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings).

#### 2. Schritt: Segmentierung der Nutzer:innen in Braze

Um in Braze ein Segment für diese Nutzer:innen zu erstellen, navigieren Sie zu **Segmente** unter **Engagement** und benennen Sie Ihr Segment. Im Folgenden finden Sie zwei Beispiele für Segmente, abhängig von der Option, die Sie für **Segmente senden als** ausgewählt haben. Weitere Einzelheiten zu den einzelnen Optionen finden Sie unter [Zielgruppen weiterleiten](#forwarding-audiences).

- **Einzelnes Array-Attribut:** Wählen Sie `SegmentMembershipArray` als Ihren Filter aus. Verwenden Sie als Nächstes die Option „includes value" und geben Sie die gewünschte Zielgruppen-ID ein. ![mParticle-Segment-Filter „SegmentMembershipArray" als „includes value" und Zielgruppen-ID eingestellt.]({% image_buster /assets/img_archive/mparticle5.png %})<br><br>
- **Ein Attribut pro Segment:** Wählen Sie Ihr angepasstes Attribut als Filter aus. Verwenden Sie dann die Option „equals" und wählen Sie die entsprechende Logik. ![mParticle-Segment-Filter „in possible parisians" als „equals" und „true" eingestellt.]({% image_buster /assets/img_archive/mparticle3.png %})

Einmal gespeichert, können Sie dieses Segment bei der Erstellung von Canvas oder Kampagnen im Schritt zum Targeting der Nutzer:innen referenzieren.

#### Deaktivieren und Löschen von Verbindungen

Da mParticle die Segmente in Braze nicht direkt verwaltet, werden die Segmente nicht gelöscht, wenn die entsprechende mParticle-Zielgruppenverbindung gelöscht oder deaktiviert wird. In diesem Fall aktualisiert mParticle die Zielgruppen-Nutzerattribute in Braze nicht, um die Zielgruppe von den jeweiligen Nutzer:innen zu entfernen.

Um die Zielgruppe von einem/einer Braze-Nutzer:in vor dem Löschen zu entfernen, passen Sie die Zielgruppen-Filter so an, dass die Zielgruppengröße auf 0 gesetzt wird, bevor Sie die Zielgruppe löschen. Nachdem die Berechnung der Zielgruppe abgeschlossen ist und 0 Nutzer:innen ergibt, löschen Sie die Zielgruppe. Dann wird die Zielgruppenmitgliedschaft in Braze auf `false` für die Einzelattribut-Option aktualisiert oder die Zielgruppen-ID aus dem Array-Format entfernt.

## Daten-Mapping

Wenn Sie Ihre mobilen und Web-Apps über mParticle mit Braze verbinden möchten, können Sie die Daten mithilfe der [Embedded-Kit-Integration](#embedded-kit-integration) an Braze übertragen. Sie können auch die [Server-zu-Server-API-Integration](#server-api-integration) verwenden, um serverseitige Daten an Braze weiterzuleiten.

Unabhängig davon, welchen Ansatz Sie wählen, müssen Sie Braze als Ausgabe einrichten:

### Konfigurieren Sie Ihre Braze-Ausgabeeinstellungen

Navigieren Sie in mParticle zu **Setup > Outputs > Add Outputs** und wählen Sie **Braze**, um die Braze-Kit-Konfiguration zu öffnen. **Speichern** Sie, wenn Sie fertig sind.

| Name der Einstellung | Beschreibung |
| ------------ | ----------- |
| Braze-App-Bezeichner-Schlüssel | Ihren Braze-App-Bezeichner-Schlüssel finden Sie im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**. Beachten Sie, dass die API-Schlüssel für jede Plattform (iOS, Android und Web) unterschiedlich sind. |
| Externer Identitätstyp | Der mParticle-Nutzeridentitätstyp, der als externe ID an Braze weitergeleitet werden soll. Wir empfehlen, dies auf dem Standardwert Customer ID zu belassen. |
| E-Mail-Identitätstyp | Der mParticle-Nutzeridentitätstyp, der als E-Mail an Braze weitergeleitet werden soll. Wir empfehlen, dies auf dem Standardwert E-Mail zu belassen. |
| Braze-Instanz | Der Cluster, an den Ihre Braze-Daten weitergeleitet werden; dies sollte derselbe Cluster sein, auf dem sich Ihr Dashboard befindet. |
| Event-Stream-Weiterleitung aktivieren | (Server-zu-Server) Wenn diese Option aktiviert ist, werden alle Events in Realtime weitergeleitet. Andernfalls werden alle Events gebündelt weitergeleitet. Wenn Sie die Event-Stream-Weiterleitung aktivieren, stellen Sie sicher, dass die Daten, die Sie an Braze weiterleiten, die [Rate-Limits]({{site.baseurl}}/api/api_limits/) einhalten. |
{: .reset-td-br-1 .reset-td-br_2 role="presentation" }

![]({% image_buster /assets/img_archive/configure_settings.png %})

### Embedded-Kit-Integration

Die SDKs von mParticle und Braze werden durch die Embedded-Kit-Integration in Ihrer Anwendung vorhanden sein. Im Gegensatz zu einer direkten Braze-Integration kümmert sich mParticle jedoch um den Aufruf der meisten Braze-SDK-Methoden für Sie. Die mParticle-Methoden, die Sie zum Tracking von Nutzerdaten verwenden, werden automatisch auf die Braze-SDK-Methoden abgebildet. 

Diese Abbildungen des mParticle-SDK für [Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy), [iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy) und [Web](https://github.com/mparticle-integrations/mparticle-javascript-integration-braze) sind Open Source und können auf der [GitHub-Seite von mParticle](https://github.com/mparticle-integrations) eingesehen werden. 

Die Embedded-Kit-SDK-Integration erlaubt es Ihnen, unsere gesamte Suite an Features zu nutzen (Push, In-App-Nachrichten und alle relevanten Messaging-Analytics-Trackings).

{% alert note %}
Für Content-Cards und angepasste In-App-Nachrichten-Integrationen rufen Sie die Braze-SDK-Methoden direkt auf.
{% endalert %}

#### 1. Schritt: Integration der mParticle-SDKs

Integrieren Sie die entsprechenden mParticle-SDKs in Ihre App, je nach den Anforderungen Ihrer Plattform:

* [mParticle für Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle für iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle für Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

#### 2. Schritt: Vollständige Integration des Braze-Event-Kits von mParticle

Während das Braze SDK für diese mParticle-Integration nicht direkt in Ihre Website oder App eingebunden werden muss, muss das folgende mParticle Appboy Kit installiert werden, um Daten von Ihrer App an Braze weiterzuleiten.

Der [Leitfaden zur Integration des Braze-Event-Kits](https://docs.mparticle.com/integrations/braze/event/#kit-integration) von mParticle führt Sie durch angepasste Anweisungen zur Abstimmung von mParticle und Braze auf Ihre Messaging-Anforderungen (Push, Standort-Tracking usw.).

#### 3. Schritt: Verbindungseinstellungen für Ihre Braze-Ausgabe

Navigieren Sie in mParticle zu **Connections** > **Connect** > **[Ihre gewünschte Plattform]** > **Connect Output**, um Braze als Ausgabe hinzuzufügen. Wählen Sie dann **Save**.

![]({% image_buster /assets/img_archive/mParticle_event_config.png %})

Nicht alle Verbindungseinstellungen gelten für alle Plattformen und Integrationsarten. Eine Aufschlüsselung der Verbindungseinstellungen und der Plattformen, für die sie gelten, finden Sie in der [Dokumentation von mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

### Server-API-Integration

Dies ist ein Add-On, mit dem Sie Ihre Backend-Daten an Braze weiterleiten können, wenn Sie die serverseitigen SDKs von mParticle verwenden (z. B. Ruby, Python usw.). Um diese Server-zu-Server-Integration mit Braze einzurichten, folgen Sie der [Dokumentation von mParticle](https://docs.mparticle.com/guides/platform-guide/connections/).

{% alert important %}
Die Server-zu-Server-Integration unterstützt keine Features der Braze-UI, wie In-App-Nachrichten, Content-Cards oder Push-Benachrichtigungen. Es gibt auch automatisch erfasste Daten, wie z. B. Felder auf Geräteebene, die mit dieser Methode nicht verfügbar sind. 

Ziehen Sie eine Side-by-side-Integration in Betracht, wenn Sie diese Features nutzen möchten.

Damit serverseitige Daten an Braze weitergeleitet werden können, müssen sie eine `external_id` enthalten; anonyme Nutzer:innen werden nicht weitergeleitet.
{% endalert %}

#### Verbindungseinstellungen für Ihre Braze-Ausgabe

Navigieren Sie in mParticle zu **Connections > Connect > [Ihre gewünschte Plattform] > Connect Output**, um Braze als Ausgabe hinzuzufügen. **Speichern** Sie, wenn Sie fertig sind. 

![]({% image_buster /assets/img_archive/mParticle_connections.png %})

Nicht alle Verbindungseinstellungen gelten für alle Plattformen und Integrationsarten. Eine Aufschlüsselung der Verbindungseinstellungen und der Plattformen, für die sie gelten, finden Sie in der [Dokumentation von mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

Bevor Sie „Angereicherte Nutzerattribute" oder „Angereicherte Nutzeridentitäten" aktivieren, empfehlen wir Ihnen, den Abschnitt [Mögliche Mehrkosten für Datenpunkte](#potential-data-point-overages) zu lesen, um sicherzustellen, dass Sie wissen, wie sich diese Einstellungen auf die Datenpunkt-Nutzung auswirken.

### Details zum Daten-Mapping

#### Datentypen
Nicht alle Datentypen werden von beiden Plattformen unterstützt.
- [Angepasste Event-Eigenschaften]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) unterstützen String-, numerische, boolesche oder Datumsobjekte. Arrays oder verschachtelte Objekte werden nicht unterstützt.
- [Angepasste Attribute]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) unterstützen Strings, Zahlen, Boolesche Werte, Datumsobjekte und Arrays, aber keine Objekte oder verschachtelte Objekte. 

{% alert note %}
Braze unterstützt keine Zeitstempel vor dem Jahr 0 oder nach dem Jahr 3000 in angepassten Attributen des Typs `Time`. Braze nimmt diese Werte auf, wenn sie von mParticle gesendet werden, aber der Wert wird als String gespeichert.
{% endalert %}

#### Daten-Mapping

| mParticle-Datentyp | Braze-Datentyp | Beschreibung |
| ------------------- | --------------- | ----------- |
| Nutzerattribute (reserviert) | Standard-Attribut | Der reservierte Nutzerattribut-Schlüssel `$FirstName` von mParticle wird beispielsweise dem Standard-Attributfeld `first_name` in Braze zugeordnet. |
| Nutzerattribute (andere) | Angepasstes Attribut | Alle an mParticle übergebenen Nutzerattribute, die nicht unter die reservierten Nutzerattribut-Schlüssel fallen, werden in Braze als angepasstes Attribut protokolliert.<br><br>Nutzerattribute unterstützen Strings, Zahlen, Boolesche Werte, Datumsangaben und Arrays, aber keine Objekte oder verschachtelte Objekte. |
| Angepasstes Event | Angepasstes Event | Die angepassten Events von mParticle werden von Braze als angepasste Events erkannt. Event-Attribute werden als angepasste Event-Eigenschaften weitergeleitet.<br><br>Event-Attribute, die als Event-Eigenschaften an Braze übergeben werden, unterstützen String-, numerische, boolesche oder Datumsobjekte, aber keine Arrays oder verschachtelte Objekte. |
| Kauf-Commerce-Event | Kauf-Event | Kauf-Commerce-Events werden auf Braze-Kauf-Events abgebildet. <br><br>Schalten Sie den Einstellungswert für gebündelte Commerce-Event-Daten um, um Käufe auf Bestell- oder Produktebene zu protokollieren. Wenn zum Beispiel `false`, würde ein einzelnes eingehendes Event mit zwei eindeutigen Produkten, Aktionen oder Impressionen zu mindestens zwei ausgehenden Braze-Events führen. Bei der Einstellung `true` würde dies zu einem einzigen ausgehenden Event mit einem verschachtelten Array von Produkten, Aktionen bzw. Impressionen führen.<br><br>Weitere Informationen zu den zusätzlichen Commerce-Feldern, die protokolliert werden, finden Sie in der [Dokumentation von mParticle](https://docs.mparticle.com/integrations/braze/event/#purchase-events). <br><br>Wenn Sie „bundle commerce event data" auf `false` setzen, unterstützen Produktattribute, die als Kauf-Event-Eigenschaften an Braze übergeben werden, String-, numerische, boolesche oder Datumsobjekte, aber keine Arrays oder verschachtelte Objekte.|
| Alle anderen Commerce-Events | Angepasstes Event | Alle anderen Commerce-Events werden auf angepasste Events abgebildet. <br><br>Schalten Sie den Einstellungswert für gebündelte Commerce-Event-Daten um, um Käufe auf Bestell- oder Produktebene zu protokollieren. Wenn zum Beispiel `false`, würde ein einzelnes eingehendes Event mit zwei eindeutigen Produkten, Aktionen oder Impressionen zu mindestens zwei ausgehenden Braze-Events führen. Bei der Einstellung `true` würde dies zu einem einzigen ausgehenden Event mit einem verschachtelten Array von Produkten, Aktionen bzw. Impressionen führen.<br><br>Zusätzlich zu bestimmten Standard-Commerce-Werten werden Produktattribute als Braze-Event-Eigenschaften protokolliert. Weitere Informationen zu den zusätzlichen Commerce-Feldern, die protokolliert werden, finden Sie in der [Dokumentation von mParticle](https://docs.mparticle.com/integrations/braze/event/#other-commerce-events)<br><br>Wenn Sie „bundle commerce event data" auf `false` setzen, unterstützen Produktattribute, die als Event-Eigenschaften an Braze übergeben werden, String-, numerische, boolesche oder Datumsobjekte, aber keine Arrays oder verschachtelte Objekte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Nutzeridentitäts-Mapping
Für jede mParticle-Ausgabe können Sie den externen Identitätstyp auswählen, der an Braze als `external_id` gesendet werden soll. Der Standardwert ist die Customer ID, Sie können aber auch eine andere ID, wie z. B. `MPID`, als `external_id` an Braze senden. Beachten Sie, dass die Wahl eines anderen Bezeichners als der Customer ID einen Einfluss darauf haben kann, wie Daten in Braze gesendet werden. 

Das Mapping der MPID auf Ihre Braze-`external_id` hat zum Beispiel folgende Auswirkungen:
- Aufgrund der Art der MPID-Zuweisung wird allen Nutzer:innen bei Sitzungsbeginn eine `external_id` zugewiesen.
- Die Einrichtung von Currents kann aufgrund der unterschiedlichen Datentypen zwischen MPID und `external_id` ein zusätzliches Mapping erfordern.

### Weiterleitung von Löschanfragen (Anfragen betroffener Personen)

Leiten Sie Löschanfragen an Braze weiter, indem Sie eine Ausgabe für Anfragen betroffener Personen an Braze konfigurieren. Um Löschanfragen an Braze weiterzuleiten, folgen Sie der [Dokumentation von mParticle](https://docs.mparticle.com/integrations/braze/forwarding-dsr/).

## Mögliche Mehrkosten für Datenpunkte

### Angereicherte Nutzerattribute

#### Aktivierung der Anreicherung von Nutzerattributen/-identitäten (nur Server-zu-Server) {#enriched}

Braze empfiehlt, in den mParticle-Verbindungseinstellungen die Option **Angereicherte Nutzerattribute einbeziehen** zu deaktivieren. Wenn diese Funktion aktiviert ist, leitet mParticle bei jedem protokollierten Event alle verfügbaren Nutzerattribute (wie Standard-Attribute, angepasste Attribute und berechnete Attribute) aus dem vorhandenen Profil an Braze weiter. Dies führt zu einem hohen Verbrauch an Datenpunkten, da mParticle bei jedem Aufruf die gleichen unveränderten Attribute an Braze sendet.

Wenn ein:e Nutzer:in beispielsweise bei der ersten Sitzung Vorname, Nachname und Telefonnummer angibt und sich später für einen Newsletter anmeldet und dieselben Informationen sowie eine E-Mail hinzufügt, wird ein Newsletter-Registrierungs-Event getriggert:
- Wenn diese Option aktiviert ist (Standard), fallen fünf Datenpunkte an. (Registrierungs-Event, E-Mail-Adresse, Vorname, Nachname und Telefonnummer)
- Wenn diese Option deaktiviert ist, fallen zwei Datenpunkte an (Registrierungs-Event und E-Mail-Adresse)

{% alert note %}
Wenn Sie diese Einstellung deaktivieren, wird nicht auf sich ändernde Daten geprüft. Sie verhindert jedoch, dass die Integration alle Nutzerattribute im Profil sendet, die nicht im ursprünglichen eingehenden Batch empfangen oder explizit als Attribut für das Event festgelegt wurden. Es ist wichtig, dass Sie trotzdem sicherstellen, dass nur Deltas an Braze weitergegeben werden.
{% endalert %}

#### Überlegungen zur Deaktivierung von angereicherten Nutzerattributen

Bei der Deaktivierung der Option **Angereicherte Nutzerattribute einbeziehen** gibt es einige Dinge zu beachten:
1. Die Server-zu-Server-Integration verwendet die mParticle Events API, um Events an Braze zu senden. Jede Anfrage wird durch ein Event ausgelöst. Wenn ein Nutzerattribut geändert wird, wie z. B. das Update einer E-Mail-Adresse, aber nicht mit einem bestimmten Event verbunden ist (z. B. ein angepasstes Event zur Profilaktualisierung), wird der neue Wert nur als „angereichertes Attribut" in der Payload des nächsten vom/von der Nutzer:in getriggerten Events an eine Ausgabe wie Braze weitergegeben. Wenn **Angereicherte Nutzerattribute einbeziehen** ausgeschaltet ist, wird dieser neue Attributwert, der nicht mit einem bestimmten Event verknüpft ist, nicht an Braze weitergegeben.
  - Um dieses Problem zu lösen, empfehlen wir, ein separates Event „Nutzerattribut aktualisiert" zu erstellen, das nur die spezifischen Nutzerattribute, die aktualisiert wurden, an Braze sendet. Beachten Sie, dass Sie bei diesem Ansatz zwar immer noch einen zusätzlichen Datenpunkt für das Event „Nutzerattribut aktualisiert" protokollieren, die Datenpunkt-Nutzung aber weitaus geringer ist als das Senden aller Nutzerattribute bei jedem Aufruf mit aktiviertem Feature.
2. Berechnete Attribute werden als angereicherte Nutzerattribute an Braze weitergegeben. Wenn also „Angereicherte Nutzerattribute" deaktiviert ist, werden diese nicht mehr an Braze weitergegeben. Um berechnete Attribute an Braze weiterzuleiten, wenn „Angereicherte Nutzerattribute" ausgeschaltet sind, könnte ein [Feed für berechnete Attribute](https://docs.mparticle.com/guides/platform-guide/calculated-attributes/using-calculated-attributes/#forward-calculated-attributes-in-the-calculated-attributes-feed) helfen, ohne alle Attribute zu pushen. Der Feed gibt ein Update an Braze weiter, wenn sich ein berechnetes Attribut ändert. 

## Fehlerbehebung

### Fehlerbehebung bei iOS-Push-Benachrichtigungen mit dem Braze-Event-Kit

Wenn Push-Benachrichtigungen bei Verwendung des Braze-Event-Kits (Embedded-Kit-Integration) unter iOS nicht funktionieren, prüfen Sie Folgendes:
1. **Push-Token-Weiterleitung:** Bestätigen Sie, dass mParticle Push-Token an Braze weiterleitet. Überprüfen Sie in Ihrem mParticle-Dashboard, ob die Braze-Kit-Verbindung Push aktiviert hat und ob die korrekte Apple-Push-Berechtigung im Braze-Dashboard konfiguriert ist.
2. **Reihenfolge der Kit-Initialisierung:** Das Braze-Kit muss initialisiert werden, bevor Ihre App Push-Berechtigungen anfordert. Wenn Push-Berechtigungen angefordert werden, bevor das Kit aktiv ist, wird das Push-Token möglicherweise nicht an Braze weitergeleitet. Stellen Sie sicher, dass das mParticle SDK früh im Lebenszyklus Ihrer App gestartet wird.
3. **Method Swizzling:** Das mParticle Apple Kit verwendet Method Swizzling, um Push-Token automatisch weiterzuleiten und Push-Benachrichtigungs-Events zu verarbeiten. Wenn Sie Swizzling deaktiviert haben oder ein anderes SDK interferiert, erreichen Push-Token möglicherweise Braze nicht. Überprüfen Sie, ob Swizzling in Ihrer mParticle-Konfiguration aktiviert ist.
4. **Manuelle Token-Verarbeitung:** Wenn Sie Push-Token manuell verwalten (z. B. durch Implementierung von `application:didRegisterForRemoteNotificationsWithDeviceToken:`), stellen Sie sicher, dass Sie das Token an mParticle übergeben, indem Sie es der Push-Benachrichtigungs-Token-Eigenschaft zuweisen, zum Beispiel: `MParticle.sharedInstance().pushNotificationToken = deviceToken`. Das Kit leitet es dann an Braze weiter.
5. **Umgebungsabweichung:** Bestätigen Sie, dass die APNs-Berechtigungsumgebung (Entwicklung vs. Produktion) mit dem Build Ihrer App übereinstimmt. Weitere Details finden Sie unter [iOS-Push-Fehlerbehebung]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/ios/).

### Senden von unnötigen oder doppelten Daten an Braze
Braze zählt jedes Mal einen Datenpunkt, wenn ein Attribut an Braze übergeben wird, auch wenn der Wert unverändert ist. Aus diesem Grund empfiehlt Braze, nur Daten weiterzuleiten, die für Aktionen innerhalb von Braze benötigt werden, und sicherzustellen, dass nur Deltas von Attributen weitergegeben werden.