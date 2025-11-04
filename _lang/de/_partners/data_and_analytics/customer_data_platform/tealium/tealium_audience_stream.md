---
nav_title: Tealium AudienceStream
article_title: Tealium AudienceStream
page_order: 2
alias: /partners/tealium_audience_stream/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Tealium, einer universellen Datendrehscheibe, die es Ihnen ermöglicht, mobile, Internet- und alternative Daten mit anderen Drittanbieter-Datenquellen zu verbinden."
page_type: partner
search_tag: Partner

---

# Tealium AudienceStream

> Tealium [AudienceStream](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/introduction/) ist eine Omnichannel-Kund:in-Segmentierung und Realtime Action Engine. AudienceStream nimmt die Daten, die in EventStream einfließen, und erstellt Besucherprofile, die die wichtigsten Attribute des Engagements Ihrer Kund:innen mit Ihrer Marke darstellen. 

Die Integration von Braze und Tealium nutzt die AudienceStream Besucherprofile. Gemeinsame Verhaltensweisen segmentieren diese Profile, um Gruppen von Besuchern mit gemeinsamen Merkmalen zu erstellen, die als Zielgruppen bezeichnet werden. Diese Zielgruppen können Ihren Technologie-Stack für Marketingtechnologien in Realtime über Konnektoren unterstützen. 

{% alert important %}
Tealium AudienceStreams und EventStreams bieten sowohl Batch- als auch Non-Batch-Konnektor-Aktionen. Der Konnektor ohne Stapelverarbeitung sollte verwendet werden, wenn Anfragen in Realtime für den Anwendungsfall wichtig sind und keine Bedenken bestehen, dass die Spezifikationen für die Rate-Limits der Braze APIs überschritten werden. Kontaktieren Sie den Braze [Support]({{site.baseurl}}/braze_support/) oder Ihren Customer-Success-Manager:in, wenn Sie Fragen haben.
{% endalert %}

## Voraussetzungen

| Name | Beschreibung |
| ---- | ----------- |
| Tealium Konto | Sie benötigen ein [Tealium-Konto](https://my.tealiumiq.com/) mit serverseitigem Zugriff. Wir empfehlen, auch die Client-seitigen Integrationen zu nutzen, um von dieser Partnerschaft zu profitieren. |
| REST-API-Schlüssel | Ein Braze REST API-Schlüssel mit den Berechtigungen `users.track`, `users.delete`, und `subscription.status.set`.<br><br>Dieser kann  erstellt werden unter **Braze-Dashboard > Entwicklungskonsole > REST-API-Schlüssel > Neuen API-Schlüssel erstellen**.|
| [Braze REST Endpunkt]({{site.baseurl}}/api/basics/#endpoints) | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der [Braze-URL für Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Attribute und Badges einrichten

#### Attribute verstehen

Der erste Schritt bei der Verwendung von AudienceStream besteht darin, Attribute zu erstellen. Attribute erlauben es Ihnen, die wichtigen Merkmale zu definieren, die die Gewohnheiten, Vorlieben, Aktionen und das Engagement eines Besuchers für Ihre Marke repräsentieren. 

**Besuchen Sie Attribute**: Visit Attribute beziehen sich auf den aktuellen Besuch (oder die Sitzung) des Nutzers:innen. Die Daten, die in diesen Attributen gespeichert sind, bleiben für die Dauer des Besuchs erhalten. Einige Beispiele für Besuchsattribute sind:
- Besuchsdauer (Anzahl)
- Aktueller Browser (String)
- Currents Gerät (String)
- Anzahl der Seitenansichten (Anzahl)

**Attribute des Besuchers**: Die Attribute des Besuchers beziehen sich auf den aktuellen Nutzer:innen. Die Daten, die in diesen Attributen gespeichert sind, bleiben für die Lifetime des Nutzers bestehen. Einige Beispiele für Besucherattribute sind: 
- Lifetime-Value der Bestellung (Anzahl)
- Vorname (String)
- Geburtsdatum (Datum)
- Einkäufe Marken (Tally)

Besuchen Sie [Tealium](https://docs.tealium.com/server-side/attributes/about/) für eine vollständige Liste der verfügbaren Datentypen.

##### Anreicherung von Attributen

Sobald Sie die gewünschten Attribute identifiziert haben, können Sie diese mit [Anreicherungen](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/attributes-enrichments/) konfigurieren - Geschäftsregeln, die festlegen, wann und wie die Werte der Attribute aktualisiert werden sollen. Jeder Datentyp bietet eine eigene Auswahl an Anreicherungen, um den Wert des Attributs zu manipulieren. Dies steht im Zusammenhang mit der Einstellung "WANN". Die folgenden Optionen stehen für jedes Attribut von Besuchen und Besuchern zur Verfügung:

- Neuer Besucher: tritt auf, wenn ein Besucher zum ersten Mal auf Ihre Website kommt.
- Neuer Besuch: tritt bei einem neuen Besuch eines Besuchers auf.
- Jedes Ereignis: tritt bei jedem Ereignis ein.
- Besuch beendet: tritt auf, wenn ein Besuch endet.

Sie können auch eine angepasste Bedingung, eine so genannte Regel, erstellen, die bestimmt, wann die Anreicherung stattfindet.

#### Abzeichen

Badges sind spezielle Attribute für Besucher, die wertvolle Verhaltensmuster darstellen. Badges werden Besuchern auf der Grundlage der Logik ihrer Anreicherungen zugewiesen oder entzogen. Diese Logik kombiniert in der Regel mehrere Bedingungen, um Besuchersegmente zu erfassen, oder legt einen Schwellenwert fest, wenn ein bestimmter Wert erreicht wird.

#### Attribut und Badge Beispiel

{% tabs local %}
{% tab Attribut %}

Erstellen Sie ein Besucher-Attribut "Lifetime-Order-Value", das den kumulativen Betrag berechnet, den der Kund:in für alle abgeschlossenen Bestellungen (Kauf-Event) ausgegeben hat (`order_total`). Um den Lifetime-Value in Ihrem Tealium-Konto einzurichten, befolgen Sie bitte die folgenden Anweisungen:

1. Navigieren Sie zu **AudienceStream > Besucher-/Besuchsattribute** und klicken Sie auf **Attribut hinzufügen**.
2. Wählen Sie den Bereich als **Besucher** aus und klicken Sie auf **Weiter**.
3. Wählen Sie den Datentyp **Nummer** aus und klicken Sie auf **Weiter**.
4. Geben Sie den Namen des Attributs ein, "Lifetime Order Value".
5. Klicken Sie auf **Anreicherung hinzufügen** und wählen Sie **Erhöhungs- oder Verkleinerungszahl**.
6. Wählen Sie das Attribut aus, das den Wert enthält, um den erhöht werden soll (`order_total`).
7. Lassen Sie das "WANN" auf "Jedes Ereignis" eingestellt und klicken Sie dann auf **Neue Regel erstellen**.
8. Erstellen Sie eine Regel, die feststellt, wann ein Kauf-Event stattgefunden hat.
9. Klicken Sie auf **Speichern** und dann auf **Fertig stellen**.

Jetzt wird allen Kund:innen ein Attribut für den Lifetime-Value zugewiesen.

{% endtab %}
{% tab Badge %}

Sie können Badges erstellen, die Ihnen helfen, Ihre Nutzer:innen anhand bestimmter Attribute zu klassifizieren und zu targetieren. Im folgenden Beispiel erstellen wir ein VIP Badge für Nutzer:innen mit einem "Lifetime-Value" von über $500.

1. Navigieren Sie zu **AudienceStream > Besucher-/Besuchsattribute** und klicken Sie auf **Attribut hinzufügen**.
2. Wählen Sie den Bereich als **Besucher** aus und klicken Sie auf **Weiter**.
3. Wählen Sie den Datentyp **Badge** aus und klicken Sie auf **Weiter**.
4. Geben Sie den Namen des Badges ein, "VIP".
5. Klicken Sie auf **Anreicherung hinzufügen** und wählen Sie **Badge zuweisen**.
6. Lassen Sie die Option "WANN" auf "Jedes Ereignis" eingestellt.
7. Erstellen Sie eine Regel für die Zuweisung von Badges, indem Sie **Regel erstellen** auswählen. Weisen Sie dieser Regel einen Titel zu und setzen Sie die Regel mithilfe des zuvor erstellten Attributs auf "...hat das Attribut "Lifetime Order Value größer als 500".
8. Klicken Sie auf **Speichern** und dann auf **Fertig stellen**.

{% endtab %}
{% endtabs %}

### Schritt 2: Erstellen Sie eine Zielgruppe

Wählen Sie auf der Tealium-Startseite unter **AudienceStream** in der Seitenleiste **Audiences** aus. Hier können Sie eine Zielgruppe von Nutzer:innen mit gemeinsamen Attributen erstellen. Der Eingang oder der Austritt eines Nutzers aus dieser Zielgruppe ist der Auslöser für die im nächsten Schritt eingerichtete Konnektor-Aktion, die diese Informationen an das Nutzerprofil in Braze weitergibt. 

Benennen Sie zunächst Ihre Zielgruppe und überlegen Sie dann, welche Attribute auf die Art der Zielgruppe zutreffen, die Sie schaffen möchten. Um zum Beispiel eine Zielgruppe von Nutzer:innen zu erstellen, könnten Sie eine Zielgruppe von Besuchern erstellen, die das **VIP Badge** haben.

Vergewissern Sie sich, dass Sie Ihre Zielgruppe **speichern / veröffentlichen**, wenn Sie fertig sind.

### Schritt 3: Einen Konnektor für Ereignisse erstellen

Ein Konnektor ist eine Integration zwischen Tealium und einem anderen Anbieter, die zur Übertragung von Daten verwendet wird. Diese Konnektoren enthalten Aktionen, die die unterstützten APIs des Partners repräsentieren. 

1. Navigieren Sie in der Seitenleiste von Tealium unter **Server-Side** zu **AudienceStream > Konnektoren für Zielgruppen.**
2. Wählen Sie den blauen Button **\+ Konnektor hinzufügen**, um den Marktplatz der Konnektoren zu durchsuchen. In dem neu erscheinenden Dialogfeld verwenden Sie die Spotlight-Suche, um den Konnektor **Braze** zu finden.
3. Um diesen Konnektor hinzuzufügen, klicken Sie auf die Kachel für den Konnektor **Braze**. Wenn Sie darauf klicken, können Sie die Verbindungsübersicht und eine Liste der erforderlichen Informationen, der unterstützten Aktionen und der Konfigurationsanweisungen anzeigen. Die Konfiguration umfasst drei Schritte: Quelle, Konfiguration und Aktion.

#### Quelle

Wählen Sie im daraufhin angezeigten **Quellendialog** die Zielgruppe aus, die Sie im vorherigen Schritt erstellt haben, und einen Auslöser, den Sie für Ihre Situation für geeignet halten. Sie können auch die Frequenzbegrenzung umschalten, um zu kontrollieren, wie oft diese Aktion ausgelöst wird. 

![]({% image_buster /assets/img/tealium/create_source.png %}){: style="max-width:90%;"}

#### Konfiguration

Als nächstes wird ein **Konfigurationsdialog** angezeigt. Wählen Sie unten auf der Seite **Konnektor hinzufügen** aus. Benennen Sie Ihren Konnektor und geben Sie hier den Endpunkt der Braze API und den REST-API-Schlüssel von Braze an.

![]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

Wenn Sie bereits einen Konnektor erstellt haben, können Sie optional einen vorhandenen Konnektor aus der Liste der verfügbaren Konnektoren verwenden und ihn mit dem Bleistiftsymbol an Ihre Bedürfnisse anpassen oder mit dem Papierkorbsymbol löschen. 

Nachdem Sie einen Konnektor zur Verknüpfung dieser Zielgruppe erstellt oder ausgewählt haben, klicken Sie auf Fertig, um fortzufahren.

#### Aktion

Benennen Sie als nächstes Ihre Konnektor-Aktion und wählen Sie einen Aktionstyp aus, der Daten gemäß der von Ihnen konfigurierten Abbildung sendet. Hier werden Sie Braze-Attribute auf Tealium-Attributnamen abbilden. Je nachdem, welche Aktionsart Sie auswählen, gibt es eine unterschiedliche Auswahl an Feldern, die Tealium benötigt. Im Folgenden finden Sie Beispiele und Erläuterungen zu diesen Feldern.

{% alert important %}
Nicht alle angebotenen Felder sind erforderlich.

![]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Nutzer:innen verfolgen - Batch und Non-Batch %}

Mit dieser Aktion können Sie die Attribute von Nutzer:innen, Ereignissen und Käufen in einer einzigen Aktion tracken. Obwohl die Aktion Nutzer:innen tracken sowohl für AudienceStream als auch für EventStream gleich ist, empfiehlt Tealium, die Abbildungen der Attribute der Nutzer:innen mit AudienceStream-Aktionen und die Abbildungen der Ereignisse und Käufe mit EventStream-Aktionen zu verknüpfen.

| Parameter | Beschreibung |
| ---------- | ----------- |
| Nutzer-ID | Verwenden Sie dieses Feld, um das Feld Nutzer:in von Tealium auf das entsprechende Feld von Braze abzubilden. Abbildung von einem oder mehreren Attributen der Nutzer:in. Wenn mehrere IDs angegeben werden, wird der erste Wert, der nicht leer ist, in der folgenden Reihenfolge ausgewählt: Externe ID, Braze ID, Alias-Name und Alias-Label.<br><br>\- Externe ID und Braze ID sollten beim Import von Push-Tokens nicht angegeben werden.<br>\- Wenn Sie einen Nutzer-Alias angeben, sollten der Alias-Name und das Alias-Label festgelegt werden. <br><br>Weitere Informationen finden Sie unter dem Braze-[Endpunkt `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). |
| Nutzerattribute | Verwenden Sie die vorhandenen Feldnamen der Braze-Benutzerprofile, um die Werte der Nutzerprofile im Braze-Dashboard zu aktualisieren, oder fügen Sie den Nutzerprofilen Ihre eigenen angepassten Daten für die [Attribute der Nutzer]({{site.baseurl}}/api/objects_filters/user_attributes_object/) hinzu.<br><br>\- Standardmäßig werden neue Nutzer:innen angelegt, wenn noch keine vorhanden sind.<br>\- Wenn Sie **Nur vorhandene Nutzer:innen aktualisieren** auf `true` setzen, werden nur vorhandene Nutzer:innen aktualisiert und keine neuen Nutzer:innen angelegt.<br>\- Wenn ein Tealium Attribut leer ist, wird es in Null umgewandelt und aus dem Nutzerprofil von Braze:innen entfernt. Anreicherungen sollten verwendet werden, wenn keine Nullwerte an Braze gesendet werden sollen, um ein Nutzer:in-Attribut zu entfernen. |
| Attribute der Nutzer:innen ändern | Verwenden Sie dieses Feld, um bestimmte Nutzer:innen-Attribute zu erhöhen oder zu verringern.<br><br>\- Integer-Attribute können um positive oder negative ganze Zahlen inkrementiert werden.<br>\- Attribute in Arrays können durch Hinzufügen oder Entfernen von Werten in bestehenden Arrays geändert werden. |
| Event | Ein Event stellt ein einzelnes Vorkommen eines angepassten Events durch einen bestimmten Nutzer:innen zu einem bestimmten Zeitpunkt dar. Verwenden Sie dieses Feld zum Tracking und zur Abbildung von Ereignisattributen, wie sie im [Braze-Ereignisobjekt]({{site.baseurl}}/api/objects_filters/event_object/) enthalten sind. <br><br>\- Das Attribut "Ereignis" `Name` ist für jedes zugeordnete Ereignis erforderlich.<br>\- Das Attribut `Time` wird automatisch auf jetzt gesetzt, wenn es nicht explizit abgebildet wird. <br>\- Standardmäßig werden neue Ereignisse erstellt, wenn noch keines vorhanden ist. Wenn Sie `Update Existing Only` auf `true` setzen, werden nur bestehende Ereignisse aktualisiert und es wird kein neues Ereignis erstellt.<br>\- Bilden Sie Attribute vom Typ Array ab, um mehrere Ereignisse hinzuzufügen. Attribute vom Typ Array müssen gleich lang sein.<br>\- Sie können Attribute mit einem einzigen Wert verwenden und auf jedes Ereignis anwenden. |
| Template für Veranstaltungen | Stellen Sie Ereignis-Templates zur Verfügung, auf die in den Daten referenziert werden kann. Templates können verwendet werden, um Daten zu transformieren, bevor sie an Braze gesendet werden. Weitere Informationen finden Sie in der [Anleitung für Templates](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) von Tealium. |
| Ereignis Template-Variable | Stellen Sie Template-Variablen für Ereignisse als Dateneingabe bereit. Lesen Sie den [Leitfaden für Template-Variablen](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) von Tealium, um mehr zu erfahren. |
| Kauf | Verwenden Sie dieses Feld, um die Attribute der Nutzer:innen zu verfolgen und abzubilden, wie sie im [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object/) Braze enthalten sind.<br><br>\- Die Attribute `Product ID`, `Currency`, und `Price` sind für jeden zugeordneten Kauf erforderlich.<br>\- Das Attribut "Kauf" `Time` wird automatisch auf "jetzt" gesetzt, wenn es nicht explizit abgebildet wird.<br>\- Standardmäßig werden neue Einkäufe angelegt, wenn noch keine vorhanden sind. Wenn Sie `Update Existing Only` auf `true` setzen, werden nur bestehende Käufe aktualisiert und es wird kein neuer Kauf angelegt.<br>\- Bilden Sie Attribute vom Typ Array ab, um mehrere Artikel zum Kauf hinzuzufügen. Attribute vom Typ Array müssen gleich lang sein.<br>\- Sie können Attribute mit einem einzigen Wert verwenden, die dann für jeden Artikel gelten.|
| Template kaufen | Templates können verwendet werden, um Daten zu transformieren, bevor sie an Braze gesendet werden.<br>\- Definieren Sie ein Purchase Template, wenn Sie Unterstützung für verschachtelte Objekte benötigen.<br>\- Wenn eine Einkaufsvorlage definiert wird, wird die Konfiguration, die im Abschnitt Einkäufe Ihrer Aktion eingerichtet wurde, ignoriert.<br>\- Weitere Informationen finden Sie in der [Anleitung für Templates](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) von Tealium.|
| Template kaufen variabel | Stellen Sie Produkt-Template-Variablen als Dateneingabe bereit. Lesen Sie den [Leitfaden für Template-Variablen](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) von Tealium, um mehr zu erfahren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_example2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Nutzer:in löschen - Nicht-Batch %}

Diese Aktion erlaubt es Ihnen, Nutzer:innen aus dem Braze-Dashboard zu löschen.

| Parameter | Beschreibung |
| ---------- | ----------- |
| Nutzer-ID | Verwenden Sie dieses Feld, um das Feld Nutzer:in von Tealium auf seine Braze-Entsprechung abzubilden.<br><br>\- Abbildung von einem oder mehreren Attributen der Nutzer:in. Wenn mehrere IDs angegeben werden, wird der erste Wert, der nicht leer ist, in der folgenden Reihenfolge ausgewählt: Externe ID, Braze ID, Alias-Name und Alias-Label.<br>\- Wenn Sie einen Nutzer:innen-Alias angeben, sollten sowohl Alias-Name als auch Alias-Label festgelegt werden.<br><br>Weitere Informationen finden Sie unter dem Braze-[Endpunkt `/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_delete2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Update Benutzer:innen Abo-Gruppe Status - Non-Batch %}
Mit dieser Aktion können Sie Nutzer:innen aus Abo-Gruppen für SMS oder E-Mail hinzufügen oder entfernen.

| Parameter | Beschreibung |
| ---------- | ----------- |
| Gruppe Typ | Verwenden Sie dieses Feld, um anzugeben, ob es sich um eine SMS- oder E-Mail-Abo-Gruppe handelt. |
| Update-Typ | Abbildung dieser Aktion auf ein Abmelde- oder Abo-Ereignis 
| Attribute | \- ID der Abo-Gruppe (erforderlich): Die ID der Abo-Gruppe, die sich auf den im vorhergehenden Feld abgebildeten Gruppentyp bezieht.<br>\- Externe ID: Die externe ID des Nutzers:in.<br><br>E-Mail gruppenspezifisch:<br>\- E-Mail: Die E-Mail Adresse des Nutzers:innen.<br>**Wenn die externe ID nicht definiert ist, wird die E-Mail benötigt.**<br><br>SMS gruppenspezifisch:<br>\- Telefon: Die Rufnummer im Format E.164. Zum Beispiel: +14155552671.<br>**Wenn die externe ID nicht definiert ist, wird das Telefon benötigt.** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/update_subscription.png %}){: style="max-width:90%"}

{% endtab %}
{% endtabs %}

Wählen Sie **Finish**.

#### Zusammenfassung

Sehen Sie sich die Zusammenfassung des von Ihnen erstellten Konnektors an. Wenn Sie die von Ihnen gewählten Optionen ändern möchten, wählen Sie **Zurück** zum Bearbeiten oder **Beenden** zum Abschließen.

Ihr Konnektor wird nun in der Liste der Konnektoren auf Ihrer Tealium-Startseite angezeigt.

Stellen Sie sicher, dass Sie Ihren Konnektor speichern oder veröffentlichen, wenn Sie fertig sind. Die von Ihnen konfigurierten Aktionen werden nun ausgelöst, wenn die triggernden Verbindungen erfüllt sind. 

### Schritt 4: Testen Sie Ihren Tealium Konnektor

Nachdem Ihr Konnektor betriebsbereit ist, sollten Sie ihn testen, um sicherzustellen, dass er ordnungsgemäß funktioniert. Der einfachste Weg, dies zu testen, ist die Verwendung des Tealium **Trace Tools**. Um Trace nutzen zu können, müssen Sie die Tealium Tools-Browsererweiterung hinzugefügt haben.

1. Um einen neuen Trace zu starten, wählen Sie **Trace** in der Seitenleiste unter **Serverseitige** Optionen. Klicken Sie auf **Start** und erfassen Sie die Trace ID.
2. Öffnen Sie die Browsererweiterung und geben Sie die Trace ID in AudienceStream Trace ein.
3. Prüfen Sie das Realtime-Protokoll.
4. Suchen Sie nach der Aktion, die Sie validieren möchten, indem Sie auf den Eintrag **Ausgelöste Aktionen** klicken, um ihn zu erweitern.
5. Suchen Sie nach der Aktion, die Sie validieren möchten, und sehen Sie sich den Protokollstatus an. 

Ausführlichere Anweisungen zur Implementierung des Trace-Tools von Tealium finden Sie in der [Trace-Dokumentation](https://docs.tealium.com/server-side/connectors/trace/about/) von Tealium.

## Demo zur Integration

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Mögliche Mehrkosten für Datenpunkte

Es gibt drei Möglichkeiten, wie Sie bei der Integration von Braze über Tealium versehentlich auf Mehrkosten bei den Daten stoßen können:

#### Doppelte Daten senden - nur Braze-Deltas von Attributen senden
Tealium sendet keine Braze-Deltas von Nutzer:innen-Attributen. Wenn Sie zum Beispiel eine EventStream-Aktion haben, die den Vornamen, die E-Mail und die Handynummer eines Nutzers trackt, sendet Tealium alle drei Attribute an Braze, sobald die Aktion getriggert wird. Tealium wird nicht danach suchen, was sich geändert hat oder aktualisiert wurde und nur diese Informationen senden.<br><br> 
**Lösung**: <br>Sie können in Ihrem Backend überprüfen, ob sich ein Attribut geändert hat oder nicht, und wenn ja, die entsprechenden Methoden von Tealium aufrufen, um das Nutzerprofil zu aktualisieren. **Das tun Nutzer:innen, die Braze direkt integrieren, normalerweise auch.** <br>**ODER**<br> Wenn Sie keine eigene Version eines Nutzerprofils in Ihrem Backend speichern und nicht feststellen können, ob sich Attribute ändern oder nicht, können Sie AudienceStream verwenden und [Anreicherungen erstellen](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/), um Nutzer:in nur dann zu senden, wenn sich die Werte geändert haben. 

#### Senden von irrelevanten Daten oder unnötiges Überschreiben von Daten
Wenn Sie mehrere EventStreams haben, die auf denselben Event-Feed zielen, werden **alle für diesen Konnektor aktivierten Aktionen** automatisch ausgelöst, sobald eine einzelne Aktion getriggert wird. **Dies kann auch dazu führen, dass Daten in Braze überschrieben werden.**<br><br>
**Lösung**: <br>Richten Sie eine separate Ereignisspezifikation oder einen Feed ein, um jede Aktion zu tracken. <br>**ODER**<br> Deaktivieren Sie Aktionen (oder Konnektoren), die Sie nicht auslösen möchten, mit den Umschaltern im Dashboard von Tealium.

#### Braze zu früh initialisieren
Nutzer:innen, die Tealium mit dem Braze Web SDK Tag integrieren, können einen dramatischen Anstieg ihrer MAU verzeichnen. **Wenn Braze beim Laden der Seite initialisiert wird, erstellt Braze jedes Mal ein anonymes Profil, wenn ein Internet Nutzer:in zum ersten Mal auf die Website navigiert.** Manche möchten das Nutzer:innen-Verhalten nur dann tracken, wenn die Nutzer:innen eine Aktion abgeschlossen haben, wie z.B. "Angemeldet" oder "Video angesehen", um ihre MAU-Zahl zu senken. <br><br>
**Lösung**: <br>Richten Sie [Lastregeln](https://docs.tealium.com/iq-tag-management/load-rules/about/) ein, um genau zu bestimmen, wann und wo ein Tag auf Ihrer Website geladen wird.

