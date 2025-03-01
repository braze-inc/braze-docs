---
nav_title: mTeilchen
article_title: mTeilchen
alias: /partners/mparticle/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und mParticle, einer Plattform für Kundendaten, die Informationen sammelt und zwischen den Quellen in Ihrem Marketing-Stack weiterleitet."
page_type: partner
search_tag: Partner

---

# mTeilchen

{% multi_lang_include video.html id="Njhqwd36gZM" align="right" %}

> Die Kundendatenplattform von mParticle ermöglicht es Ihnen, mehr aus Ihren Daten zu machen. Anspruchsvolle Vermarkter nutzen mParticle, um Daten über ihren gesamten Wachstumsstapel zu orchestrieren und so in den entscheidenden Momenten der Customer Journey zu gewinnen.

Die Integration von Braze und mParticle ermöglicht Ihnen die nahtlose Steuerung des Informationsflusses zwischen den beiden Systemen:
- Synchronisieren Sie mParticle Audiences mit Braze für die Segmentierung von Braze-Kampagnen und Canvas.
- Teilen Sie Daten zwischen den beiden Plattformen. Dies kann über die mParticle-Kit-Integration und die Server-zu-Server-Integration erfolgen.
- [Senden Sie die Interaktionen von Braze-Benutzern über Currents an mParticle]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/) und machen Sie sie für das gesamte Wachstumsprogramm nutzbar. 

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| mParticle Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [mParticle-Konto](https://app.mparticle.com/login). |
| Hartlöt-Instanz | Ihre Braze-Instanz finden Sie auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics/#endpoints). (Zum Beispiel: US-01, US-02, etc.) |
| Braze App Identifizierungsschlüssel | Der Schlüssel zu Ihrer App-Kennung. <br><br>Diesen finden Sie im **Braze Dashboard > Einstellungen verwalten > API-Schlüssel**. |
| Arbeitsbereich REST API Schlüssel | (Server-zu-Server) Ein Braze REST API-Schlüssel<br><br>Dieser kann im **Braze Dashboard > Entwicklerkonsole > API-Einstellungen > API-Schlüssel** erstellt werden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Publikum

Nutzen Sie die Partnerschaft zwischen Braze und mParticle, um Ihre Integration zu konfigurieren und mParticle-Zielgruppen für das Retargeting direkt in Braze zu importieren, so dass ein vollständiger Kreislauf von Daten von einem System zum anderen entsteht. Jede Integration, die Sie einrichten, wird auf das Datenpunktvolumen Ihres Kontos angerechnet.

#### Weiterleitung von Zielgruppen

mParticle bietet drei Möglichkeiten, die Attribute für die Kohortenzugehörigkeit festzulegen, die über die Konfigurationseinstellung "[Segmente senden als](#send_settings)" gesteuert werden. In den folgenden Abschnitten erfahren Sie, wie die einzelnen Optionen verarbeitet werden:

- [Einzelnes String-Attribut](#string)
- [Einzelnes Array-Attribut](#array)
- [Ein Attribut pro Segment](#per-segment)
- [Sowohl einzelnes Array-Attribut als auch einzelnes String-Attribut](#both-1)
- [Sowohl einzelnes Array-Attribut als auch ein Attribut pro Segment](#both-2)
- [Sowohl einzelnes String-Attribut als auch ein Attribut pro Segment](#both-3)
- [Einzelne Array-Attribute, einzelne String-Attribute und ein Attribut pro Segment](#multi)

##### Einzelnes String-Attribut {#string}

mParticle erstellt ein einzelnes benutzerdefiniertes Attribut namens `SegmentMembership`. Der Wert dieses Attributs ist eine Zeichenkette mit durch Komma getrennten mParticle Audience IDs, die dem Benutzer entsprechen. Diese Audience IDs finden Sie im mParticle Dashboard unter **Audiences**.

Wenn zum Beispiel eine mParticle Audience "Ibiza-Träumer" die Audience-ID "11036" hat, können Sie diese Benutzer mit dem Filter `SegmentMembership` - `matches regex` - `11036` segmentieren.

Obwohl dies die Standardoption in mParticle ist, entscheiden sich die meisten Braze-Benutzer für die Verwendung [einzelner Array-Attribute](#array), um die Filterung bei der Erstellung von Segmenten in Braze zu erleichtern.

{% alert important %}
Diese Lösung wird nicht empfohlen, wenn Sie mehr als ein paar Zielgruppen haben, da benutzerdefinierte Attribute bis zu 255 Zeichen lang sein können. Sie können also mit dieser Methode nicht Dutzende oder Hunderte von Zielgruppen in einem Benutzerprofil speichern. Wenn Sie eine große Anzahl von Kohorten pro Benutzer haben, empfehlen wir dringend die Konfiguration "ein Attribut pro Segment".
{% endalert %}

![mParticle Segment Mitgliedschaft][6]

##### Einzelnes Array-Attribut {#array}

mParticle erstellt für jeden Benutzer ein einzelnes benutzerdefiniertes Array-Attribut in Braze, das `SegmentMembershipArray` heißt. Der Wert dieses Attributs ist ein Array von mParticle Audience IDs, die dem Benutzer entsprechen.

Wenn ein Benutzer beispielsweise Mitglied von drei mParticle Audiences mit den Audience-IDs "13053", "13052" und "13051" ist, können Sie mit dem Filter `SegmentMembershipArray` - `includes value` - `13051` nach Benutzern segmentieren, die einer dieser Audiences entsprechen.

{% alert note %}
Braze-Array-Attribute haben eine maximale Länge von 25. Wenn einer Ihrer Benutzer Mitglied in mehr als 25 Zielgruppen ist, werden die Mitgliederinformationen von Braze gekürzt. Um dieses Problem zu umgehen, wenden Sie sich an Ihren Braze-Vertreter, um die maximale Array-Länge zu erhöhen.
{% endalert %}

##### Ein Attribut pro Segment {#per-segment}

mParticle erstellt für jede Zielgruppe, zu der ein Benutzer gehört, ein benutzerdefiniertes boolesches Attribut. Wenn eine mParticle-Zielgruppe zum Beispiel "Mögliche Pariser" heißt, können Sie diese Nutzer mit dem Filter `In Possible Parisians` - `equals` - `true` segmentieren.

![mParticle benutzerdefiniertes Attribut][7]

##### Sowohl einzelnes Array-Attribut als auch einzelnes String-Attribut {#both-1}

mParticle sendet Attribute, die sowohl durch ein einzelnes Array-Attribut als auch durch ein einzelnes String-Attribut beschrieben werden.

##### Sowohl einzelnes Array-Attribut als auch ein Attribut pro Segment {#both-2}

mParticle sendet Attribute, die sowohl durch ein einzelnes Array-Attribut als auch durch ein Attribut pro Segment beschrieben werden.

##### Sowohl einzelnes String-Attribut als auch ein Attribut pro Segment {#both-3}

mParticle sendet Attribute, die sowohl durch ein einzelnes String-Attribut als auch durch ein Attribut pro Segment beschrieben werden.

##### Einzelne Array-Attribute, einzelne String-Attribute und ein Attribut pro Segment {#multi}

mParticle sendet Attribute, wie durch ein einzelnes Array-Attribut, ein einzelnes String-Attribut und ein Attribut pro Segment beschrieben.

#### Schritt 1: Erstellen Sie ein Publikum in mParticle {#send_settings}

So erstellen Sie ein Publikum in mParticle:

1. Navigieren Sie zu **Zielgruppen** > **Einzelner Arbeitsbereich** > **\+ Neue Zielgruppe**.
2. Um Braze als Ausgabe für Ihr Publikum zu verbinden, müssen Sie die folgenden Felder ausfüllen:

| Feldname               | Beschreibung                                                                                                                                                                   |
| ------------------------ | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| API-Schlüssel                  | Zu finden im Braze Dashboard unter **Einstellungen** > **API-Schlüssel**.<br><br>Wenn Sie die ältere Navigation verwenden, finden Sie die API-Schlüssel unter **Entwicklerkonsole** > **API-Einstellungen**. |
| API-Schlüssel Betriebssystem | Wählen Sie aus, zu welchem Betriebssystem Ihr Braze API-Schlüssel gehört. Diese Auswahl schränkt die Arten von Push-Tokens ein, die bei einer Audience-Aktualisierung weitergeleitet werden.                          |
| Segmente senden als         | Die Methode zum Senden von Audiences an Braze. Weitere Informationen finden Sie im Abschnitt [Weiterleitung von Audienzen](#forwarding-audiences).                                                          |
| Arbeitsbereich REST API Schlüssel   | Braze REST API-Schlüssel mit vollen Rechten. Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden.                                                        |
| Externer Identitätstyp   | Der mParticle-Benutzeridentitätstyp, der als externe ID an Braze weitergeleitet werden soll. Wir empfehlen, den Standardwert Kunden-ID beizubehalten.                                          |
| E-Mail-Identitätstyp      | Der mParticle-Benutzeridentitätstyp, der als E-Mail an Braze weitergeleitet werden soll.                                                                                                            |
| Hartlöt-Instanz           | Geben Sie an, an welchen Cluster Ihre Braze-Daten weitergeleitet werden sollen.                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="3"}
3\. Und schließlich: **Sichern Sie** Ihr Publikum.

Sie sollten innerhalb weniger Minuten die Synchronisierung der Audiences mit Braze sehen. Die Publikumsmitgliedschaft wird nur für Benutzer mit `external_ids` aktualisiert (d.h. nicht für anonyme Benutzer). Weitere Informationen zur Erstellung von Braze mParticle Audiences finden Sie in der mParticle-Dokumentation zu den [Konfigurationseinstellungen](https://docs.mparticle.com/integrations/braze/audience/#configuration-settings).

#### Schritt 2: Segmentierte Benutzer in Braze

Um in Braze ein Segment für diese Benutzer zu erstellen, navigieren Sie zu **Segmente** unter **Engagement** und benennen Sie Ihr Segment. Im Folgenden finden Sie zwei Beispiele für Segmente, je nachdem, welche Option Sie für **Segmente senden als** gewählt haben. Weitere Einzelheiten zu den einzelnen Optionen finden Sie unter [Weiterleitung von Hörern](#forwarding-audiences.)

- **Einzelnes Array-Attribut:** Wählen Sie `SegmentMembershipArray` als Ihren Filter. Verwenden Sie als nächstes die Option "enthält Wert" und geben Sie die gewünschte Zielgruppen-ID ein. ![mParticle Segmentfilter "SegmentMembershipArray" als "enthält Wert" und Zielgruppen-ID eingestellt.][11]<br><br>
- **Ein Attribut pro Segment:** Wählen Sie Ihr benutzerdefiniertes Attribut als Filter. Verwenden Sie als nächstes die Option "gleich" und wählen Sie die entsprechende Logik. ![mParticle segment filter "in possible parisians" set as "equals" and "true".][8]

Sobald Sie es gespeichert haben, können Sie dieses Segment bei der Erstellung von Canvas oder Kampagnen im Schritt "Benutzer ansprechen" verwenden.

#### Deaktivieren und Löschen von Verbindungen

Da mParticle die Segmente nicht direkt in Braze verwaltet, werden die Segmente nicht gelöscht, wenn die entsprechende mParticle Audience-Verbindung gelöscht oder deaktiviert wird. In diesem Fall aktualisiert mParticle die Benutzerattribute der Audience in Braze nicht, um die Audience von jedem Benutzer zu entfernen.

Um die Audience eines Braze-Benutzers vor dem Löschen zu entfernen, passen Sie die Audience-Filter so an, dass die Audience-Größe auf 0 gesetzt wird, bevor Sie eine Audience löschen. Nachdem die Berechnung der Zielgruppe abgeschlossen ist und 0 Benutzer ergibt, löschen Sie die Zielgruppe. Dann wird die Audience-Mitgliedschaft in Braze auf `false` für die Option Einzelattribut aktualisiert oder die Audience-ID wird aus dem Array-Format entfernt.

## Datenzuordnung

Wenn Sie Ihre mobilen und Web-Apps über mParticle mit Braze verbinden möchten, können Sie die Daten mithilfe der [Embedded Kit-Integration](#embedded-kit-integration) auf Braze abbilden. Sie können auch die [Server-zu-Server-API-Integration](#server-api-integration) verwenden, um serverseitige Daten an Braze weiterzuleiten.

Unabhängig davon, welchen Ansatz Sie wählen, müssen Sie Braze als Ausgabe einrichten:

### Konfigurieren Sie Ihre Braze-Ausgabeeinstellungen

Navigieren Sie in mParticle zu **Setup > Outputs > Add Outputs** und wählen Sie **Braze**, um die Konfiguration des Braze-Kits zu öffnen. **Speichern Sie**, wenn Sie fertig sind.

| Name der Einstellung | Beschreibung |
| ------------ | ----------- |
| Braze App Identifizierungsschlüssel | Ihren Braze-App-Kennungsschlüssel finden Sie im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel**. Beachten Sie, dass die API-Schlüssel für jede Plattform (iOS, Android und Web) unterschiedlich sind. |
| Externer Identitätstyp | Der mParticle-Benutzeridentitätstyp, der als externe ID an Braze weitergeleitet werden soll. Wir empfehlen, dies auf dem Standardwert Kunden-ID zu belassen. |
| E-Mail-Identitätstyp | Der mParticle-Benutzeridentitätstyp, der als E-Mail an Braze weitergeleitet werden soll. Wir empfehlen, dies auf dem Standardwert E-Mail zu belassen, |
| Hartlöt-Instanz | Der Cluster, an den Ihre Braze-Daten weitergeleitet werden; dies sollte derselbe Cluster sein, auf dem sich Ihr Dashboard befindet. |
| Aktivieren Sie die Weiterleitung von Ereignisströmen | (Server-zu-Server) Wenn aktiviert, werden alle Ereignisse in Echtzeit weitergeleitet. Wenn nicht, werden alle Ereignisse als Ganzes weitergeleitet. Wenn Sie sich dafür entscheiden, die Weiterleitung von Ereignisströmen zu aktivieren, stellen Sie sicher, dass die Daten, die Sie an Braze weitergeben, die [Geschwindigkeitsgrenzen]({{site.baseurl}}/api/basics/#api-limits) einhalten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][10]

### Integration von Embedded Kits

Das mParticle- und Braze-SDK wird durch die Integration des Embedded Kits in Ihrer Anwendung vorhanden sein. Im Gegensatz zu einer direkten Braze-Integration übernimmt mParticle jedoch den Aufruf der meisten Braze-SDK-Methoden für Sie. Die mParticle-Methoden, die Sie zum Verfolgen von Benutzerdaten verwenden, werden automatisch auf die SDK-Methoden von Braze abgebildet. 

Diese Mappings des SDK von mParticle für [Android](https://github.com/mparticle-integrations/mparticle-android-integration-appboy), [iOS](https://github.com/mparticle-integrations/mparticle-apple-integration-appboy) und [Web](https://github.com/Appboy/integration-appboy) sind Open Source und können auf der [GitHub-Seite von mParticle](https://github.com/mparticle-integrations) gefunden werden. 

Mit der Integration des Embedded Kit SDK können Sie alle Vorteile unserer Funktionen nutzen (Push, In-App-Nachrichten und alle relevanten Nachrichtenanalysen).

{% alert note %}
Für Content Cards und benutzerdefinierte In-App-Nachrichtenintegrationen rufen Sie die Braze SDK-Methoden direkt auf.
{% endalert %}

#### Schritt 1: Integrieren Sie die mParticle SDKs

Integrieren Sie die entsprechenden mParticle SDKs in Ihre App, je nach den Anforderungen Ihrer Plattform:

* [mParticle für Android](https://docs.mparticle.com/developers/sdk/android/getting-started/)
* [mParticle für iOS](https://docs.mparticle.com/developers/sdk/ios/getting-started/)
* [mParticle für das Web](https://docs.mparticle.com/developers/sdk/web/getting-started/)

#### Schritt 2: Vollständige Integration des Braze Event-Kits von mParticle

Während das Braze SDK für diese mParticle-Integration nicht direkt in Ihre Website oder App eingebunden werden muss, muss das folgende mParticle Appboy Kit installiert werden, um Daten von Ihrer App an Braze weiterzuleiten.

Der [Leitfaden zur Integration des Braze-Event-Kits](https://docs.mparticle.com/integrations/braze/event/#kit-integration) von mParticle führt Sie durch die Anweisungen zur Anpassung von mParticle und Braze an Ihre Anforderungen (Push, Location Tracking usw.).

#### Schritt 3: Verbindungseinstellungen für Ihren Braze-Ausgang

Navigieren Sie in mParticle zu **Verbindungen > Verbinden > [Ihre gewünschte Plattform] > Ausgang verbinden**, um Braze als Ausgang hinzuzufügen. **Speichern Sie**, wenn Sie fertig sind.

![][3]

Nicht alle Verbindungseinstellungen gelten für alle Plattformen und Integrationstypen. Eine Aufschlüsselung der Verbindungseinstellungen und der Plattformen, für die sie gelten, finden Sie in [der Dokumentation von mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

### Server-API-Integration

Dies ist ein Add-on, mit dem Sie Ihre Backend-Daten an Braze weiterleiten können, wenn Sie die serverseitigen SDKs von mParticle verwenden (z. B. Ruby, Python usw.). Um diese Server-zu-Server-Integration mit Braze einzurichten, folgen Sie der [Dokumentation von mParticle](https://docs.mparticle.com/guides/platform-guide/connections/).

{% alert important %}
Die Server-zu-Server-Integration unterstützt keine Braze UI-Funktionen wie In-App-Nachrichten, Content Cards oder Push-Benachrichtigungen. Es gibt auch automatisch erfasste Daten, wie z.B. Felder auf Geräteebene, die mit dieser Methode nicht verfügbar sind. 

Ziehen Sie eine Side-by-Side-Integration in Betracht, wenn Sie diese Funktionen nutzen möchten.

Damit serverseitige Daten an Braze weitergeleitet werden können, müssen sie ein `external_id` enthalten; anonyme Benutzer werden nicht weitergeleitet.
{% endalert %}

#### Verbindungseinstellungen für Ihren Braze-Ausgang

Navigieren Sie in mParticle zu **Verbindungen > Verbinden > [Ihre gewünschte Plattform] > Ausgang verbinden**, um Braze als Ausgang hinzuzufügen. **Speichern Sie**, wenn Sie fertig sind. 

![][4]

Nicht alle Verbindungseinstellungen gelten für alle Plattformen und Integrationstypen. Eine Aufschlüsselung der Verbindungseinstellungen und der Plattformen, für die sie gelten, finden Sie in [der Dokumentation von mParticle](https://docs.mparticle.com/integrations/braze/event/#connection-settings).

Bevor Sie "Angereicherte Benutzerattribute" oder "Angereicherte Benutzeridentitäten" aktivieren, empfehlen wir Ihnen, die [Datenpunktüberschreitung](#potential-data-point-overages) zu überprüfen, um sicherzustellen, dass Sie wissen, wie sich diese Einstellungen auf die Datenpunktnutzung auswirken.

### Details zur Datenzuordnung

#### Datentypen
Nicht alle Datentypen werden von beiden Plattformen unterstützt.
- [Benutzerdefinierte Ereigniseigenschaften]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/) unterstützen String-, numerische, boolesche oder Datumsobjekte. Es unterstützt keine Arrays oder verschachtelte Objekte.
- [Benutzerdefinierte Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) unterstützen Strings, Zahlen, Boolesche Werte, Datumsobjekte und Arrays, aber keine Objekte oder verschachtelte Objekte. 

{% alert note %}
Braze unterstützt keine Zeitstempel vor Jahr 0 oder nach Jahr 3000 in benutzerdefinierten Attributen vom Typ `Time`. Braze nimmt diese Werte auf, wenn sie von mParticle gesendet werden, aber der Wert wird als String gespeichert.
{% endalert %}

#### Datenzuordnung

| mParticle Datentyp | Datenart Hartlöten | Beschreibung |
| ------------------- | --------------- | ----------- |
| Benutzerattribute (reserviert) | Standard-Attribut | Der reservierte Benutzerattributschlüssel von mParticle ( `$FirstName` ) wird zum Beispiel dem Standardattributfeld für Braze ( `first_name` ) zugeordnet. |
| Benutzerattribute (Sonstiges) | Angepasstes Attribut | Alle an mParticle übergebenen Benutzerattribute, die nicht in die reservierten Benutzerattributschlüssel fallen, werden in Braze als benutzerdefiniertes Attribut protokolliert.<br><br>Benutzerattribute unterstützen Strings, Zahlen, Boolesche Werte, Daten und Arrays, aber keine Objekte oder verschachtelte Objekte. |
| Angepasstes Event | Angepasstes Event | mParticle-Ereignisse werden von Braze als benutzerdefinierte Ereignisse erkannt. Ereignisattribute werden als benutzerdefinierte Ereigniseigenschaften weitergeleitet.<br><br>Ereignisattribute, die als Ereigniseigenschaften an Braze übergeben werden, unterstützen String-, numerische, boolesche oder Datumsobjekte, aber keine Arrays oder verschachtelte Objekte. |
| Handelsereignis kaufen | Ereignis kaufen | Kauf-Commerce-Ereignisse werden mit Braze-Kaufereignissen verknüpft. <br><br>Schalten Sie den Einstellungswert für Bundle-Commerce-Ereignisdaten um, um Einkäufe auf Bestell- oder Produktebene zu protokollieren. Wenn `false` beispielsweise ein einzelnes eingehendes Ereignis mit zwei einzigartigen Produkten, Werbeaktionen oder Impressionen zu mindestens zwei ausgehenden Braze-Ereignissen führt. Bei der Einstellung `true` würde dies zu einem einzigen ausgehenden Ereignis mit einem verschachtelten Array für Produkte, Aktionen bzw. Impressionen führen.<br><br>Weitere Informationen zu den zusätzlichen Handelsfeldern, die protokolliert werden, finden Sie in [der Dokumentation von mParticle](https://docs.mparticle.com/integrations/braze/event/#purchase-events). <br><br>Wenn Sie "bundle commerce event data" als `false` Produktattribute festlegen, die als Kaufereigniseigenschaften an Braze übergeben werden, unterstützen Sie String-, numerische, boolesche oder Datumsobjekte, aber keine Arrays oder verschachtelte Objekte.|
| Alle anderen kommerziellen Ereignisse | Angepasstes Event | Alle anderen Handelsereignisse werden auf benutzerdefinierte Ereignisse abgebildet. <br><br>Schalten Sie den Einstellungswert für Bundle-Commerce-Ereignisdaten um, um Einkäufe auf Bestell- oder Produktebene zu protokollieren. Wenn `false` beispielsweise ein einzelnes eingehendes Ereignis mit zwei einzigartigen Produkten, Werbeaktionen oder Impressionen zu mindestens zwei ausgehenden Braze-Ereignissen führt. Bei der Einstellung `true` würde dies zu einem einzigen ausgehenden Ereignis mit einem verschachtelten Array für Produkte, Aktionen bzw. Impressionen führen.<br><br>Zusätzlich zu bestimmten Standard-Commerce-Werten werden Produktattribute als Braze-Ereigniseigenschaften protokolliert. Weitere Informationen zu den zusätzlichen Handelsfeldern, die protokolliert werden, finden Sie in [der Dokumentation von mParticle](https://docs.mparticle.com/integrations/braze/event/#other-commerce-events)<br><br>Wenn Sie "bundle commerce event data" als `false` Produktattribute einstellen, die als Ereigniseigenschaften an Braze übergeben werden, unterstützen Sie String-, numerische, boolesche oder Datumsobjekte, aber keine Arrays oder verschachtelte Objekte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Zuordnung von Benutzeridentitäten
Für jede mParticle-Ausgabe können Sie den externen Identitätstyp auswählen, der als `external_id` an Braze gesendet werden soll. Der Standardwert ist zwar die Kunden-ID, aber Sie können auch eine andere ID zuordnen, z. B. `MPID`, um sie als `external_id` an Braze zu senden. Beachten Sie, dass die Wahl einer anderen Kennung als der Kunden-ID die Art und Weise beeinflussen kann, wie Daten in Braze gesendet werden. 

Die Zuordnung von MPID zu Ihrem Braze `external_id` hat beispielsweise folgende Auswirkungen:
- Aufgrund der Art der Zuweisung der MPID wird allen Benutzern beim Start der Sitzung eine `external_id` zugewiesen.
- Die aktuelle Einrichtung kann aufgrund der unterschiedlichen Datentypen zwischen MPID und `external_id` zusätzliche Zuordnungen erfordern.

### Weiterleitung von Anträgen auf Löschung (Anträge der betroffenen Person)

Leiten Sie Löschanfragen an Braze weiter, indem Sie die Ausgabe von Löschanfragen für Betroffene an Braze konfigurieren. Um Löschanfragen an Braze weiterzuleiten, folgen Sie der [Dokumentation von mParticle](https://docs.mparticle.com/integrations/braze/forwarding-dsr/).

## Mögliche Überschreitungen der Datenpunkte

### Angereicherte Benutzerattribute

#### Aktivieren der Anreicherung von Benutzerattributen/identitäten (nur Server-zu-Server) {#enriched}

Braze empfiehlt, in den mParticle-Verbindungseinstellungen die Option **Angereicherte Benutzerattribute einbeziehen** zu deaktivieren. Wenn diese Option aktiviert ist, leitet mParticle bei jedem protokollierten Ereignis alle verfügbaren Benutzerattribute (wie Standardattribute, benutzerdefinierte Attribute und berechnete Attribute) aus dem vorhandenen Profil an Braze weiter. Dies führt zu einem hohen Verbrauch an Datenpunkten, da mParticle Braze bei jedem Aufruf die gleichen unveränderten Attribute sendet.

Wenn ein Benutzer beispielsweise bei seiner ersten Sitzung Vorname, Nachname und Telefonnummer angibt und sich später für einen Newsletter anmeldet, indem er dieselben Informationen zusätzlich zu seiner E-Mail-Adresse hinzufügt, wird ein Newsletter-Anmeldungsereignis ausgelöst:
- Wenn Sie diese Option aktivieren (Standardeinstellung), werden fünf Datenpunkte erfasst. (Anmeldungsereignis, E-Mail-Adresse, Vorname, Nachname und Telefonnummer)
- Wenn diese Option deaktiviert ist, fallen zwei Datenpunkte an (Anmeldeereignis und E-Mail-Adresse).

{% alert note %}
Wenn Sie diese Einstellung deaktivieren, wird nicht auf veränderte Daten geprüft. Sie verhindert jedoch, dass die Integration alle Benutzerattribute im Profil des Benutzers sendet, die nicht im ursprünglichen Eingangsstapel empfangen oder ausdrücklich als Attribut für das Ereignis festgelegt wurden. Es ist wichtig, dass Sie trotzdem sicherstellen, dass nur Deltas an Braze übergeben werden.
{% endalert %}

#### Überlegungen zum Deaktivieren von angereicherten Benutzerattributen

Wenn Sie die Option **Angereicherte Benutzerattribute einbeziehen** deaktivieren, sollten Sie einige Punkte beachten:
1. Die Server-zu-Server-Integration verwendet die mParticle Events API, um Ereignisse an Braze zu senden. Jede Anfrage wird durch ein Ereignis ausgelöst. Wenn ein Benutzerattribut geändert wird, z. B. die Aktualisierung einer E-Mail-Adresse, aber nicht mit einem bestimmten Ereignis verknüpft ist (z. B. einem benutzerdefinierten Ereignis zur Profilaktualisierung), wird der neue Wert nur als "angereichertes Attribut" in der Nutzlast des nächsten vom Benutzer ausgelösten Ereignisses an eine Ausgabe wie Braze übergeben. Wenn die Option **Angereicherte Benutzerattribute einbeziehen** deaktiviert ist, wird dieser neue Attributwert, der nicht mit einem bestimmten Ereignis verknüpft ist, nicht an Braze übergeben.
  - Um dieses Problem zu lösen, empfehlen wir, ein separates Ereignis "Benutzerattribut aktualisiert" zu erstellen, das nur die spezifischen Benutzerattribute, die aktualisiert wurden, an Braze sendet. Beachten Sie, dass Sie bei diesem Ansatz immer noch einen zusätzlichen Datenpunkt für das Ereignis "Benutzerattribut aktualisiert" protokollieren, aber der Datenpunktverbrauch ist weitaus geringer als das Senden aller Benutzerattribute bei jedem Anruf, bei dem die Funktion aktiviert ist.
2. Berechnete Attribute werden als angereicherte Benutzerattribute an Braze übergeben. Wenn Sie also "Angereicherte Benutzerattribute" deaktivieren, werden diese nicht mehr an Braze übergeben. Um berechnete Attribute an Braze weiterzuleiten, wenn "Angereicherte Benutzerattribute" ausgeschaltet sind, könnte ein [berechneter Attribut-Feed](https://docs.mparticle.com/guides/platform-guide/calculated-attributes/using-calculated-attributes/#forward-calculated-attributes-in-the-calculated-attributes-feed) helfen, ohne alle Attribute zu pushen. Der Feed gibt eine Aktualisierung an Braze weiter, wenn sich ein berechnetes Attribut ändert. 

### Senden von unnötigen oder doppelten Daten an Braze
Braze zählt jedes Mal einen Datenpunkt, wenn ein Attribut an Braze übergeben wird, auch wenn der Wert unverändert bleibt. Aus diesem Grund empfiehlt Braze, nur Daten weiterzuleiten, die für Aktionen innerhalb von Braze erforderlich sind, und sicherzustellen, dass nur Deltas von Attributen weitergegeben werden.

[1]: https://dashboard.braze.com/app_settings/developer_console
[2]: {% image_buster /assets/img_archive/dashboard_keys_locations.png %}
[3]: {% image_buster /assets/img_archive/mParticle_event_config.png %}
[4]: {% image_buster /assets/img_archive/mParticle_connections.png %}
[6]: {% image_buster /assets/img_archive/mparticle1.png %}
[7]: {% image_buster /assets/img_archive/mparticle2.png %}
[8]: {% image_buster /assets/img_archive/mparticle3.png %}
[9]: {% image_buster /assets/img_archive/mparticle4.png %}
[10]: {% image_buster /assets/img_archive/configure_settings.png %}
[11]: {% image_buster /assets/img_archive/mparticle5.png %}
[5]: \#embedded-kit-integration
