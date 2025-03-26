---
nav_title: Tealium AudienceStream
article_title: Tealium AudienceStream
page_order: 2
alias: /partners/tealium_audience_stream/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Tealium, einer universellen Datendrehscheibe, die es Ihnen ermöglicht, mobile, Web- und alternative Daten mit anderen Drittquellen zu verbinden."
page_type: partner
search_tag: Partner

---

# Tealium AudienceStream

> Tealium [AudienceStream](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/introduction/) ist eine Omnichannel-Kundensegmentierungs- und Echtzeit-Aktionsmaschine. AudienceStream verwendet die Daten, die in EventStream einfließen, und erstellt Besucherprofile, die die wichtigsten Attribute des Engagements Ihrer Kunden mit Ihrer Marke darstellen. 

Die Integration von Braze und Tealium nutzt die Besucherprofile von AudienceStream. Gemeinsame Verhaltensweisen segmentieren diese Profile, um Gruppen von Besuchern mit gemeinsamen Merkmalen zu erstellen, die als Zielgruppen bezeichnet werden. Diese Zielgruppen können über Konnektoren Ihr Marketingtechnologiepaket in Echtzeit unterstützen. 

{% alert important %}
Tealium AudienceStreams und EventStreams bieten sowohl Batch- als auch Non-Batch-Connector-Aktionen. Der Non-Batch-Connector sollte verwendet werden, wenn Echtzeitanfragen für den Anwendungsfall wichtig sind und keine Bedenken bestehen, dass die API-Ratenbeschränkungen von Braze überschritten werden. Wenden Sie sich an den [Braze-Support]({{site.baseurl}}/braze_support/) oder Ihren Kundenbetreuer, wenn Sie irgendwelche Fragen haben.
{% endalert %}

## Voraussetzungen

| Name | Beschreibung |
| ---- | ----------- |
| Tealium-Konto | Ein [Tealium-Konto](https://my.tealiumiq.com/) mit serverseitigem Zugriff ist erforderlich. Wir empfehlen, auch die clientseitigen Integrationen zu nutzen, um von dieser Partnerschaft zu profitieren. |
| REST-API-Schlüssel | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.track`, `users.delete`, und `subscription.status.set`.<br><br>Dieser kann über **Braze Dashboard > Developer Console > REST API Key > Create New API Key** erstellt werden **.**|
| [Braze REST Endpunkt][6] | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Attribute und Abzeichen einrichten

#### Attribute verstehen

Der erste Schritt bei der Verwendung von AudienceStream besteht darin, Attribute zu erstellen. Attribute ermöglichen es Ihnen, die wichtigen Merkmale zu definieren, die die Gewohnheiten, Vorlieben, Handlungen und das Engagement eines Besuchers für Ihre Marke darstellen. 

**Besuchen Sie Attribute**: Visit-Attribute beziehen sich auf den aktuellen Besuch (oder die Sitzung) des Benutzers. Die in diesen Attributen gespeicherten Daten bleiben für die Dauer des Besuchs erhalten. Einige Beispiele für Besuchsattribute sind:
- Besuchsdauer (Anzahl)
- Aktueller Browser (String)
- Aktuelles Gerät (String)
- Anzahl der Seitenansichten (Anzahl)

**Besucher-Attribute**: Besucherattribute beziehen sich auf den aktuellen Benutzer. Die in diesen Attributen gespeicherten Daten bleiben während der gesamten Lebensdauer des Benutzers erhalten. Einige Beispiele für Besucherattribute sind: 
- Lifetime-Bestellwert (Anzahl)
- Vorname (String)
- Geburtsdatum (Datum)
- Einkäufe Marken (Tally)

Besuchen Sie [Tealium][1] für eine vollständige Liste der verfügbaren Datentypen.

##### Attribut-Anreicherung

Sobald Sie die gewünschten Attribute identifiziert haben, können Sie diese mit [Enrichments](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/attributes-enrichments/) konfigurieren - Geschäftsregeln, die bestimmen, wann und wie die Werte der Attribute aktualisiert werden. Jeder Datentyp bietet eine eigene Auswahl an Anreicherungen, um den Wert des Attributs zu bearbeiten. Dies steht im Zusammenhang mit der Einstellung "WANN". Die folgenden Optionen sind für jedes Besuchs- und Besucherattribut verfügbar:

- Neuer Besucher: tritt auf, wenn ein Besucher zum ersten Mal auf Ihre Website kommt.
- Neuer Besuch: tritt bei einem neuen Besuch eines Besuchers auf.
- Jedes Ereignis: tritt bei jedem Ereignis ein.
- Besuch beendet: tritt auf, wenn ein Besuch endet.

Sie können auch eine benutzerdefinierte Bedingung, eine so genannte Regel, erstellen, die bestimmt, wann die Anreicherung erfolgt.

#### Abzeichen

Badges sind spezielle Besucherattribute, die wertvolle Verhaltensmuster darstellen. Abzeichen werden Besuchern auf der Grundlage der Logik ihrer Anreicherungen zugewiesen oder entzogen. Diese Logik kombiniert in der Regel mehrere Bedingungen, um Besuchersegmente zu erfassen, oder legt einen Schwellenwert fest, wenn ein bestimmter Wert erreicht wird.

#### Beispiel für Attribute und Abzeichen

{% tabs local %}
{% tab Attribut %}

Erstellen Sie ein Besucherattribut "Lifetime Order Value", das den kumulativen Betrag berechnet, den der Kunde für alle abgeschlossenen Bestellungen (Kaufereignis) ausgegeben hat (`order_total`). Um einen lebenslangen Bestellwert in Ihrem Tealium-Konto einzurichten, befolgen Sie bitte die folgenden Anweisungen:

1. Navigieren Sie zu **AudienceStream > Besucher-/Besuchsattribute** und klicken Sie auf **Attribut hinzufügen**.
2. Wählen Sie den Bereich als **Besucher** aus und klicken Sie auf **Weiter**.
3. Wählen Sie den Datentyp **Nummer** und klicken Sie auf **Weiter**.
4. Geben Sie den Namen des Attributs ein, "Lifetime Order Value".
5. Klicken Sie auf **Anreicherung hinzufügen** und wählen Sie **Erhöhen oder Verringern der Anzahl**.
6. Wählen Sie das Attribut, das den Wert enthält, um den Sie erhöhen möchten (`order_total`).
7. Lassen Sie die Option "WANN" auf "Jedes Ereignis" eingestellt und klicken Sie dann auf **Neue Regel erstellen**.
8. Erstellen Sie eine Regel, die feststellt, wann ein Kaufereignis eingetreten ist.
9. Klicken Sie auf **Speichern** und dann auf **Fertig stellen**.

Jetzt wird allen Kunden ein Lifetime-Bestellwert zugewiesen.

{% endtab %}
{% tab Abzeichen %}

Sie können Abzeichen erstellen, die Ihnen helfen, Ihre Benutzer anhand bestimmter gemeinsamer Merkmale zu klassifizieren und anzusprechen. Für das folgende Beispiel erstellen wir ein VIP-Abzeichen für Benutzer mit einem "Lifetime Order Value" von über $500.

1. Navigieren Sie zu **AudienceStream > Besucher-/Besuchsattribute** und klicken Sie auf **Attribut hinzufügen**.
2. Wählen Sie den Bereich als **Besucher** aus und klicken Sie auf **Weiter**.
3. Wählen Sie den Datentyp **Ausweis** und klicken Sie auf **Weiter**.
4. Geben Sie den Namen des Ausweises ein, "VIP".
5. Klicken Sie auf **Anreicherung hinzufügen** und wählen Sie **Abzeichen zuweisen**.
6. Lassen Sie die Option "WANN" auf "Jedes Ereignis" eingestellt.
7. Erstellen Sie eine Regel für die Ausweiszuweisung, indem Sie **Regel erstellen** wählen. Weisen Sie dieser Regel einen Titel zu und setzen Sie die Regel mithilfe des zuvor erstellten Attributs auf "...hat das Attribut "Lifetime Order Value größer als 500".
8. Klicken Sie auf **Speichern** und dann auf **Fertig stellen**.

{% endtab %}
{% endtabs %}

### Schritt 2: Ein Publikum schaffen

Wählen Sie auf der Tealium-Startseite in der Seitenleiste unter **AudienceStream** die Option **Audiences**. Hier können Sie eine Zielgruppe von Benutzern mit gemeinsamen Attributen erstellen. Der Eintritt oder Austritt eines Benutzers aus dieser Zielgruppe ist der Auslöser für die im nächsten Schritt eingerichtete Verbindungsaktion, die diese Informationen an das Benutzerprofil in Braze weitergibt. 

Benennen Sie zunächst Ihr Publikum und überlegen Sie dann, welche Eigenschaften auf die Art von Publikum zutreffen, das Sie ansprechen möchten. Um zum Beispiel eine Zielgruppe von VIP-Benutzern zu erstellen, könnten Sie eine Zielgruppe von Besuchern erstellen, die das **VIP-Abzeichen** haben.

Vergewissern Sie sich, dass Sie Ihr Publikum **speichern/veröffentlichen**, wenn Sie fertig sind.

### Schritt 3: Erstellen Sie einen Ereignis-Connector

Ein Konnektor ist eine Integration zwischen Tealium und einem anderen Anbieter, die der Datenübertragung dient. Diese Konnektoren enthalten Aktionen, die die unterstützten APIs des Partners darstellen. 

1. Navigieren Sie in der Seitenleiste von Tealium unter **Server-Side** zu **AudienceStream > Audience Connectors**.
2. Klicken Sie auf die blaue Schaltfläche **\+ Konnektor hinzufügen**, um den Marktplatz für Konnektoren zu durchsuchen. In dem neu erscheinenden Dialogfeld verwenden Sie die Spotlight-Suche, um den **Braze-Anschluss** zu finden.
3. Um diesen Anschluss hinzuzufügen, klicken Sie auf die Kachel **Braze-Anschluss**. Wenn Sie darauf klicken, können Sie die Verbindungsübersicht und eine Liste der erforderlichen Informationen, unterstützten Aktionen und Konfigurationsanweisungen anzeigen. Die Konfiguration umfasst drei Schritte: Quelle, Konfiguration und Aktion.

#### Quelle

Wählen Sie im angezeigten **Quellendialog** die Zielgruppe, die Sie im vorherigen Schritt erstellt haben, und einen Auslöser, den Sie für Ihre Situation für geeignet halten. Sie können auch die Frequenzbegrenzung einschalten, um zu bestimmen, wie oft diese Aktion ausgelöst wird. 

![]({% image_buster /assets/img/tealium/create_source.png %}){: style="max-width:90%;"}

#### Konfiguration

Als nächstes wird ein **Konfigurationsdialog** angezeigt. Wählen Sie unten auf der Seite **Anschluss hinzufügen**. Benennen Sie Ihren Connector und geben Sie hier Ihren Braze-API-Endpunkt und Ihren Braze-REST-API-Schlüssel an.

![]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

Wenn Sie bereits eine Verbindung erstellt haben, können Sie optional eine bestehende Verbindung aus der Liste der verfügbaren Verbindungen verwenden und sie mit dem Bleistiftsymbol an Ihre Bedürfnisse anpassen oder mit dem Papierkorbsymbol löschen. 

Nachdem Sie einen Connector für die Verknüpfung dieser Zielgruppe erstellt oder ausgewählt haben, klicken Sie auf Fertig, um fortzufahren.

#### Aktion

Benennen Sie als nächstes Ihre Konnektoraktion und wählen Sie einen Aktionstyp, der Daten entsprechend der von Ihnen konfigurierten Zuordnung sendet. Hier werden Sie Braze-Attribute auf Tealium-Attributnamen abbilden. Je nachdem, welche Aktionsart Sie wählen, gibt es eine unterschiedliche Auswahl an Feldern, die von Tealium benötigt werden. Im Folgenden finden Sie Beispiele und Erläuterungen zu diesen Feldern.

{% alert important %}
Nicht alle angebotenen Felder sind erforderlich.

![]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Benutzer verfolgen - Batch und Non-Batch %}

Mit dieser Aktion können Sie Benutzer-, Ereignis- und Kaufattribute in einer einzigen Aktion verfolgen. Obwohl die Aktion Benutzer verfolgen für AudienceStream und EventStream identisch ist, empfiehlt Tealium, die Zuordnungen von Benutzerattributen mit AudienceStream-Aktionen und die Zuordnungen von Ereignissen und Käufen mit EventStream-Aktionen festzulegen.

| Parameter | Beschreibung |
| ---------- | ----------- |
| Nutzer-ID | Verwenden Sie dieses Feld, um das Tealium-Benutzer-ID-Feld seinem Braze-Äquivalent zuzuordnen. Ordnen Sie ein oder mehrere Benutzer-ID-Attribute zu. Wenn mehrere IDs angegeben werden, wird der erste Wert, der nicht leer ist, anhand der folgenden Prioritätsreihenfolge ausgewählt: Externe ID, Braze ID, Alias-Name und Alias-Etikett.<br><br>\- Externe ID und Braze ID sollten beim Importieren von Push-Tokens nicht angegeben werden.<br>\- Wenn Sie einen Benutzer-Alias angeben, sollten der Alias-Name und das Alias-Label festgelegt werden. <br><br>Weitere Informationen finden Sie auf dem Braze [`/users/track` Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). |
| Nutzerattribute | Verwenden Sie die vorhandenen Feldnamen der Benutzerprofile von Braze, um die Werte der Benutzerprofile im Braze-Dashboard zu aktualisieren, oder fügen Sie den Benutzerprofilen Ihre eigenen [benutzerdefinierten Attributdaten]({{site.baseurl}}/api/objects_filters/user_attributes_object/) hinzu.<br><br>\- Standardmäßig werden neue Benutzer angelegt, wenn keine vorhanden sind.<br>\- Wenn Sie **Nur vorhandene Benutzer aktualisieren** auf `true` setzen, werden nur vorhandene Benutzer aktualisiert und keine neuen Benutzer erstellt.<br>\- Wenn ein Tealium-Attribut leer ist, wird es in Null umgewandelt und aus dem Braze-Benutzerprofil entfernt. Anreicherungen sollten verwendet werden, wenn zum Entfernen eines Benutzerattributs keine Nullwerte an Braze gesendet werden sollen. |
| Benutzerattribute ändern | Verwenden Sie dieses Feld, um bestimmte Benutzerattribute zu erhöhen oder zu verringern<br><br>\- Ganzzahlige Attribute können um positive oder negative ganze Zahlen erhöht werden.<br>\- Array-Attribute können durch Hinzufügen oder Entfernen von Werten in bestehenden Arrays geändert werden. |
| Event | Ein Ereignis stellt ein einzelnes Auftreten eines benutzerdefinierten Ereignisses durch einen bestimmten Benutzer zu einem bestimmten Zeitpunkt dar. Verwenden Sie dieses Feld, um Ereignisattribute wie die im [Braze-Ereignisobjekt]({{site.baseurl}}/api/objects_filters/event_object/) zu verfolgen und zuzuordnen. <br><br>\- Das Ereignisattribut `Name` ist für jedes zugeordnete Ereignis erforderlich.<br>\- Das Ereignisattribut `Time` wird automatisch auf jetzt gesetzt, wenn es nicht explizit zugewiesen wird. <br>\- Standardmäßig werden neue Ereignisse erstellt, wenn noch keines vorhanden ist. Wenn Sie `Update Existing Only` auf `true` setzen, werden nur bestehende Ereignisse aktualisiert und es wird kein neues Ereignis erstellt.<br>\- Ordnen Sie Attribute vom Typ Array zu, um mehrere Ereignisse hinzuzufügen. Attribute vom Typ Array müssen gleich lang sein.<br>\- Einzelwertattribute können verwendet und auf jedes Ereignis angewendet werden. |
| Ereignis-Vorlage | Stellen Sie Ereignisvorlagen bereit, auf die in den Körperdaten verwiesen werden kann. Vorlagen können verwendet werden, um Daten umzuwandeln, bevor sie an Braze gesendet werden. Weitere Informationen finden Sie im [Vorlagen-Leitfaden](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) von Tealium. |
| Variable Ereignis-Vorlage | Geben Sie Variablen der Ereignisvorlage als Dateneingabe ein. Weitere Informationen finden Sie im [Leitfaden für Vorlagenvariablen](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) von Tealium. |
| Kauf | Verwenden Sie dieses Feld, um die Kaufattribute des Benutzers zu verfolgen und zuzuordnen, wie sie im [Braze-Kaufobjekt]({{site.baseurl}}/api/objects_filters/purchase_object/) enthalten sind.<br><br>\- Die Kaufattribute `Product ID`, `Currency` und `Price` sind für jeden zugeordneten Kauf erforderlich.<br>\- Das Kaufattribut `Time` wird automatisch auf jetzt gesetzt, wenn es nicht explizit zugewiesen wird.<br>\- Standardmäßig werden neue Einkäufe angelegt, wenn noch keine vorhanden sind. Wenn Sie `Update Existing Only` auf `true` setzen, werden nur bestehende Käufe aktualisiert und es wird kein neuer Kauf angelegt.<br>\- Ordnen Sie Attribute vom Typ Array zu, um mehrere Kaufartikel hinzuzufügen. Attribute vom Typ Array müssen gleich lang sein.<br>\- Einzelwertattribute können verwendet werden und gelten für jeden Artikel.|
| Vorlage kaufen | Vorlagen können verwendet werden, um Daten umzuwandeln, bevor sie an Braze gesendet werden.<br>\- Definieren Sie eine Kaufvorlage, wenn Sie Unterstützung für verschachtelte Objekte benötigen.<br>\- Wenn eine Kaufvorlage definiert wird, wird die Konfiguration, die im Abschnitt Käufe Ihrer Aktion eingerichtet wurde, ignoriert.<br>\- Weitere Informationen finden Sie im [Vorlagen-Leitfaden](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) von Tealium.|
| Kaufvorlage variabel | Stellen Sie Produktvorlagenvariablen als Dateneingabe bereit. Weitere Informationen finden Sie im [Leitfaden für Vorlagenvariablen](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) von Tealium. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_example2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Benutzer löschen - Nicht-Batch %}

Mit dieser Aktion können Sie Benutzer aus dem Braze Dashboard löschen.

| Parameter | Beschreibung |
| ---------- | ----------- |
| Nutzer-ID | Verwenden Sie dieses Feld, um das Tealium-Benutzer-ID-Feld seinem Braze-Äquivalent zuzuordnen.<br><br>\- Ordnen Sie ein oder mehrere Benutzer-ID-Attribute zu. Wenn mehrere IDs angegeben werden, wird der erste Wert, der nicht leer ist, anhand der folgenden Prioritätsreihenfolge ausgewählt: Externe ID, Braze ID, Alias-Name und Alias-Etikett.<br>\- Wenn Sie einen Benutzer-Alias angeben, sollten sowohl Alias-Name als auch Alias-Bezeichnung festgelegt werden.<br><br>Weitere Informationen finden Sie unter dem [Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) Braze [`/users/delete`.]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_delete2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Status der Benutzerabonnementgruppe aktualisieren - Nicht-Batch %}
Mit dieser Aktion können Sie Benutzer zu den SMS- oder E-Mail-Abonnementgruppen von Braze hinzufügen oder entfernen.

| Parameter | Beschreibung |
| ---------- | ----------- |
| Gruppe Typ | Verwenden Sie dieses Feld, um anzugeben, ob es sich um eine SMS- oder E-Mail-Abonnementgruppe handelt. |
| Typ aktualisieren | Ordnen Sie diese Aktion einem Abmelde- oder Abonnementereignis zu 
| Attribute | \- ID der Abonnementgruppe (erforderlich): Die ID der Abonnementgruppe, die sich auf den im vorhergehenden Feld zugeordneten Gruppentyp bezieht.<br>\- Externe ID: Die externe ID des Benutzers.<br><br>E-Mail-Gruppe spezifisch:<br>\- E-Mail: Die E-Mail-Adresse des Benutzers.<br>**Wenn die externe ID nicht definiert ist, wird die E-Mail benötigt.**<br><br>SMS-Gruppe spezifisch:<br>\- Telefon: Die Rufnummer im Format E.164. Zum Beispiel: +14155552671.<br>**Wenn die externe ID nicht definiert ist, wird das Telefon benötigt.** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/update_subscription.png %}){: style="max-width:90%"}

{% endtab %}
{% endtabs %}

Wählen Sie **Finish**.

#### Zusammenfassung

Sehen Sie sich die Zusammenfassung des von Ihnen erstellten Connectors an. Wenn Sie die von Ihnen gewählten Optionen ändern möchten, wählen Sie **Zurück** zum Bearbeiten oder **Beenden** zum Abschließen.

Ihr Connector wird nun in der Liste der Connectoren auf Ihrer Tealium-Startseite angezeigt.

Stellen Sie sicher, dass Sie Ihren Connector speichern oder veröffentlichen, wenn Sie fertig sind. Die von Ihnen konfigurierten Aktionen werden nun ausgelöst, wenn die Auslöserverbindungen erfüllt sind. 

### Schritt 4: Testen Sie Ihren Tealium-Anschluss

Nachdem Ihr Connector eingerichtet ist, sollten Sie ihn testen, um sicherzustellen, dass er ordnungsgemäß funktioniert. Der einfachste Weg, dies zu testen, ist die Verwendung des Tealium **Trace Tools**. Um Trace nutzen zu können, müssen Sie die Browser-Erweiterung Tealium Tools hinzufügen.

1. Um einen neuen Trace zu starten, wählen Sie **Trace** in der Seitenleiste unter **Serverseitige** Optionen. Klicken Sie auf **Start** und erfassen Sie die Trace-ID.
2. Öffnen Sie die Browsererweiterung und geben Sie die Trace-ID in AudienceStream Trace ein.
3. Prüfen Sie das Echtzeit-Protokoll.
4. Suchen Sie nach der Aktion, die Sie validieren möchten, indem Sie auf den Eintrag **Ausgelöste Aktionen** klicken, um ihn zu erweitern.
5. Suchen Sie nach der Aktion, die Sie validieren möchten, und sehen Sie sich den Protokollstatus an. 

Ausführlichere Anweisungen zur Implementierung des Trace-Tools von Tealium finden Sie in der [Trace-Dokumentation][21] ] von Tealium.

## Demo zur Integration

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Mögliche Überschreitungen der Datenpunkte

Es gibt drei Möglichkeiten, wie Sie bei der Integration von Braze über Tealium versehentlich auf Datenüberlastungen stoßen können:

#### Doppelte Daten senden - senden Sie nur Braze-Deltas von Attributen
Tealium sendet keine Braze-Deltas von Benutzerattributen. Wenn Sie zum Beispiel eine EventStream-Aktion haben, die den Vornamen, die E-Mail-Adresse und die Handynummer eines Benutzers erfasst, sendet Tealium alle drei Attribute an Braze, sobald die Aktion ausgelöst wird. Tealium wird nicht danach suchen, was sich geändert hat oder aktualisiert wurde und nur diese Informationen senden.<br><br> 
**Lösung**: <br>Sie können Ihr Backend überprüfen, um festzustellen, ob sich ein Attribut geändert hat oder nicht, und wenn ja, die entsprechenden Methoden von Tealium aufrufen, um das Benutzerprofil zu aktualisieren. **Das ist es, was Benutzer, die Braze direkt integrieren, normalerweise tun.** <br>**ODER**<br> Wenn Sie keine eigene Version eines Benutzerprofils in Ihrem Backend speichern und nicht feststellen können, ob sich Attribute ändern oder nicht, können Sie AudienceStream verwenden und [Anreicherungen erstellen](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/), um Benutzerattribute nur dann zu senden, wenn sich Werte geändert haben. 

#### Senden von irrelevanten Daten oder unnötiges Überschreiben von Daten
Wenn Sie mehrere EventStreams haben, die auf denselben Event-Feed abzielen, werden **alle für diesen Connector aktivierten Aktionen** automatisch ausgelöst, sobald eine einzelne Aktion ausgelöst wird. **Dies kann auch dazu führen, dass Daten in Braze überschrieben werden.**<br><br>
**Lösung**: <br>Richten Sie eine separate Ereignisspezifikation oder einen Feed ein, um jede Aktion zu verfolgen. <br>**ODER**<br> Deaktivieren Sie Aktionen (oder Verbindungen), die Sie nicht auslösen möchten, indem Sie die Kippschalter im Tealium-Dashboard verwenden.

#### Braze zu früh initialisieren
Benutzer, die Tealium mit dem Braze Web SDK-Tag integrieren, können einen dramatischen Anstieg ihrer MAU verzeichnen. **Wenn Braze beim Laden der Seite initialisiert wird, erstellt Braze jedes Mal ein anonymes Profil, wenn ein Webbenutzer zum ersten Mal auf die Website zugreift.** Manche möchten das Nutzerverhalten nur dann verfolgen, wenn die Nutzer eine Aktion abgeschlossen haben, wie z. B. "Angemeldet" oder "Video angesehen", um ihre MAU-Zahl zu senken. <br><br>
**Lösung**: <br>Legen Sie [Lastregeln](https://docs.tealium.com/iq-tag-management/load-rules/about/) fest, um genau zu bestimmen, wann und wo ein Tag auf Ihrer Website geladen wird.

[1]: https://docs.tealium.com/server-side/attributes/about/
[15]: {% image_buster /assets/img/tealium/create_configuration.png %}
[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
[21]: https://docs.tealium.com/server-side/connectors/trace/about/
[17]: {% image_buster /assets/img/tealium/save_publish.png %}
