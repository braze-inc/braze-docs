---
nav_title: Erweiterung der Ereignisweiterleitung
article_title: Adobe
description: "Dieser Referenzartikel behandelt die Braze-Event-Forward-Erweiterung, mit der Sie die im Adobe Experience Platform Edge Network erfassten Daten nutzen und in Form von serverseitigen Ereignissen an Braze senden können."
page_type: partner
page_order: 2
search_tag: Partner

---

# Track Events API Erweiterung zur Weiterleitung von Ereignissen

> Mit der [Ereignisweiterleitungserweiterung](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en) Braze Track Events API können Sie die im Adobe Experience Platform Edge Network erfassten Daten nutzen und sie in Form von serverseitigen Ereignissen über die [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) API.

Dieses Dokument beschreibt die Anwendungsfälle der Erweiterung, wie Sie sie in Ihren Event-Forwarding-Bibliotheken installieren und wie Sie ihre Funktionen in einer [Event-Forwarding-Regel](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) einsetzen.

{% alert note %}
Das Senden von Attributen an Braze kann den Datenpunktverbrauch von Braze erhöhen. Wenden Sie sich an Ihren Braze-Kundenbetreuer, bevor Sie Attribute senden. Weitere Informationen finden Sie in der Braze-Dokumentation über [abrechenbare Datenpunkte]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#billable-data-points).
{% endalert %}

## Anwendungsfälle

Diese Erweiterung sollte Daten aus dem Edge Network in Braze verwenden, um dessen Kundenanalyse- und Targeting-Funktionen zu nutzen.

Nehmen wir zum Beispiel ein Einzelhandelsunternehmen mit einer Multichannel-Präsenz (Website und Mobilgeräte), das Transaktions- oder Konversationsdaten als Ereignisdaten von seiner Website und seinen mobilen Plattformen erfasst. 

Mithilfe verschiedener [Tag-Regeln](https://experienceleague.adobe.com/docs/experience-platform/tags/home.html?lang=en) werden diese Daten in Echtzeit an das Edge-Netzwerk gesendet. Von hier aus sendet die Braze-Erweiterung zur Ereignisweiterleitung automatisch relevante Ereignisse von der Serverseite an Braze.

## Preisgrenzen

| API | Raten-Grenzwerte |
| --- | --- |
| Benutzer-Spur | 50.000 Anfragen pro Minute.<br><br>Weitere Informationen finden Sie in der [Dokumentation der User Track API]({{site.baseurl}}/api/endpoints/user_data/post_user_track#rate-limit).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Erfassen Sie die erforderlichen Konfigurationsdetails

Um das Edge Network mit Braze zu verbinden, benötigen Sie Folgendes:

| Schlüssel-Typ | Beschreibung |
| --- | --- |
| Hartlöt-Instanz | Ihre Braze-Instanz erhalten Sie von Ihrem Braze-Onboarding-Manager oder Sie finden sie auf der [API-Übersichtsseite]({{site.baseurl}}/api/basics/#endpoints). |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit allen Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Schritt 2: Erstellen Sie ein Geheimnis

Erstellen Sie ein neues [Ereignisweiterleitungsgeheimnis](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/secrets.html?lang=en) und setzen Sie den Wert auf Ihren [Braze API-Schlüssel](https://experienceleague.adobe.com/docs/experience-platform/tags/extensions/server/braze/overview.html?lang=en#configuration-details). Dies wird verwendet, um die Verbindung zu Ihrem Konto zu authentifizieren und den Wert sicher zu halten.

### Schritt 3: Installieren und konfigurieren Sie die Braze-Erweiterung

1. Um die Erweiterung zu installieren, [erstellen Sie eine Eigenschaft zur Ereignisweiterleitung](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en#properties) oder wählen Sie stattdessen eine vorhandene Eigenschaft zur Bearbeitung aus.
2. Wählen Sie dann **Erweiterungen** in der linken Navigation. Wählen Sie auf der Registerkarte **Katalog** die Option Auf der Karte **installieren** für die Erweiterung Braze.
3. Geben Sie auf dem nächsten Bildschirm Ihre REST-Instanz und Ihren API-Schlüssel ein und wählen Sie anschließend **Speichern**.

### Schritt 4: Erstellen Sie eine Regel zum Senden von Ereignissen

Nachdem Sie die Erweiterung installiert haben, erstellen Sie eine neue [Regel für](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) die Ereignisweiterleitung und konfigurieren die Bedingungen wie gewünscht. Wenn Sie die Aktionen für die Regel konfigurieren, wählen Sie die **Braze-Erweiterung** und dann **Ereignis senden** als Aktionstyp aus.

![][1]

{% tabs local %}
{% tab Benutzer-Identifikation %}

| Eingabe | Beschreibung |
| --- | --- |
| Externe Benutzer-ID | Eine lange, zufällige und gut verteilte UUID oder GUID. Wenn Sie eine andere Methode zur Benennung Ihrer Benutzer-IDs wählen, müssen diese ebenfalls lang, zufällig und gut verteilt sein. Erfahren Sie mehr über die [vorgeschlagene Namenskonvention für Benutzer-IDs]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#suggested-user-id-naming-convention). |
| Braze Benutzer-ID | Braze-Benutzerkennzeichen. |
| Benutzer-Alias | Ein Alias dient als alternativer eindeutiger Benutzeridentifikator. Verwenden Sie Aliasnamen, um Benutzer anhand anderer Dimensionen als Ihrer Hauptbenutzer-ID zu identifizieren.<br><br>Das Benutzer-Aliasobjekt besteht aus zwei Teilen: einem `alias_name` für den Bezeichner selbst und einem `alias_label`, der die Art des Alias angibt. Benutzer können mehrere Aliasnamen mit unterschiedlichen Bezeichnungen haben, aber nur einen `alias_name` pro `alias_label`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Um das Ereignis mit einem Benutzer zu verknüpfen, müssen Sie entweder das Feld `External User ID`, das Feld `Braze User Identifier` oder den Abschnitt `User Alias` ausfüllen.
{% endalert %}

{% endtab %}
{% tab Ereignisdaten %}

| Eingabe | Beschreibung | Erforderlich |
| --- | --- | --- |
| Event-Name | Name der Veranstaltung. | Ja |
| Zeit der Veranstaltung | Datums-Zeit als String im ISO 8601 oder im `yyyy-MM-dd'T'HH:mm:ss:SSSZ` Format. | Ja |
| App Kennung | Die App-Kennung oder `app_id` ist ein Parameter, der eine Aktivität mit einer bestimmten App in Ihrem Arbeitsbereich verbindet. Es zeigt an, mit welcher App innerhalb des Arbeitsbereichs Sie interagieren. | Kein:e |
| Event-Eigenschaften | Ein JSON-Objekt mit benutzerdefinierten Eigenschaften des Ereignisses. | Kein:e |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Für die Aktion **Ereignis senden von Braze** müssen nur ein **Ereignisname** und eine **Ereigniszeit** angegeben werden, aber Sie sollten so viele Informationen wie möglich in das Feld für benutzerdefinierte Eigenschaften eingeben. Siehe [Ereignisobjekt]({{site.baseurl}}/api/objects_filters/event_object/) für weitere Details.
{% endalert %}

{% endtab %}
{% tab Benutzer-Attribut %}

Benutzerattribute können ein JSON-Objekt sein, das Felder enthält, die ein Attribut mit dem angegebenen Namen und Wert im angegebenen Benutzerprofil erstellen oder aktualisieren. Die folgenden Eigenschaften werden unterstützt:

| Benutzer-Attribut | Beschreibung |
| --- | --- |
| Vorname | Vorname des Benutzers. |
| Nachname | Nachname des Benutzers. |
| Tel. | Telefonnummer des Benutzers. |
| E-Mail | E-Mail Adresse des Benutzers. |
| Geschlecht | Eine der folgenden Zeichenketten: "M", "F", "O" (andere), "N" (nicht zutreffend), "P" (lieber nicht sagen). |
| Ort | Die Stadt des Benutzers. |
| Land | Das Land des Benutzers als Zeichenkette im Format [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). |
| Sprache | Die Sprache des Benutzers als Zeichenkette im Format [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). |
| Geburtsdatum | Die Geburtsdaten des Benutzers als String im Format "JJJJ-MM-TT" (zum Beispiel 1980-12-21). |
| Zeitzone | Name der Zeitzone aus der [IANA-Zeitzonendatenbank](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (z. B. 'Amerika/New_York' oder 'Eastern Time (US & Canada)'). |
| Facebook | Ein Hash mit einem der folgenden Werte: `id` (String), `likes` (Array von Strings), `num_friends` (Integer). |
| Twitter | Hash mit einer der folgenden Angaben: id (Ganzzahl), `screen_name` (String, X (ehemals Twitter) Handle), `followers_count` (Ganzzahl), `friends_count` (Ganzzahl), `statuses_count`(Ganzzahl). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Alle in der Konfiguration hinzugefügten Attribute werden jedes Mal gesendet, wenn das Ereignis an Braze gesendet wird, unabhängig davon, ob sich der Wert des Attributs geändert hat. Wenn Sie Benutzerattribute konfigurieren, stellen Sie sicher, dass Sie wissen, wie sich dies auf Ihren Datenpunktverbrauch auswirkt.
{% endalert %}

{% endtab %}
{% endtabs %}

### Schritt 5: Erstellen Sie eine Regel zum Senden von Kaufereignissen

Nachdem Sie die Erweiterung installiert haben, erstellen Sie eine neue [Regel für](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) die Ereignisweiterleitung und konfigurieren die Bedingungen wie gewünscht. Wenn Sie die Aktionen für die Regel konfigurieren, wählen Sie die **Braze-Erweiterung** und dann als Aktionstyp **Kaufereignis senden** aus.

![][3]

{% tabs local %}
{% tab Benutzer-Identifikation %}

| Eingabe | Beschreibung |
| --- | --- |
| Externe Benutzer-ID | Eine lange, zufällige und gut verteilte UUID oder GUID. Wenn Sie eine andere Methode zur Benennung Ihrer Benutzer-IDs wählen, müssen diese ebenfalls lang, zufällig und gut verteilt sein. Erfahren Sie mehr über die [vorgeschlagene Namenskonvention für Benutzer-IDs]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#suggested-user-id-naming-convention). |
| Braze Benutzer-ID | Braze-Benutzerkennzeichen. |
| Benutzer-Alias | Ein Alias dient als alternativer eindeutiger Benutzeridentifikator. Verwenden Sie Aliasnamen, um Benutzer anhand anderer Dimensionen als Ihrer Hauptbenutzer-ID zu identifizieren.<br><br>Das Benutzer-Aliasobjekt besteht aus zwei Teilen: einem `alias_name` für den Bezeichner selbst und einem `alias_label`, der die Art des Alias angibt. Benutzer können mehrere Aliasnamen mit unterschiedlichen Bezeichnungen haben, aber nur einen `alias_name` pro `alias_label`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Um das Ereignis mit einem Benutzer zu verknüpfen, müssen Sie entweder das Feld `External User ID`, das Feld `Braze User Identifier` oder den Abschnitt `User Alias` ausfüllen.
{% endalert %}

{% endtab %}
{% tab Daten kaufen %}

| Eingabe | Beschreibung | Erforderlich |
| --- | --- | --- |
| Produkt-ID | Identifikator für den Kauf. (zum Beispiel Produktname oder Produktkategorie) | Ja |
| Kaufzeitpunkt | Datums-Zeit als Zeichenkette im ISO 8601 oder im `yyyy-MM-dd'T'HH:mm:ss:SSSZ` Format. | Ja |
| Währung | Währung als Zeichenkette im alphabetischen [ISO 4217-Währungscode-Format](https://en.wikipedia.org/wiki/ISO_4217). | Ja |
| Preis | Der Preis des Objekts. | Ja |
| Menge | Die gekaufte Menge. Wenn nicht angegeben, ist der Standardwert 1. Der Höchstwert muss kleiner als 100 sein. | Kein:e |
| App Kennung | Die App-Kennung oder `app_id` ist ein Parameter, der eine Aktivität mit einer bestimmten App in Ihrem Arbeitsbereich verbindet. Es zeigt an, mit welcher App innerhalb des Arbeitsbereichs Sie interagieren. | Kein:e |
| Eigenschaften des Kaufs | Ein JSON-Objekt mit benutzerdefinierten Eigenschaften des Kaufs. | Kein:e |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Für die Aktion **Kaufereignis senden** muss nur `Product ID`, `Purchase Time`, `Currency` und `Price` angegeben werden, aber Sie sollten so viele Informationen wie möglich in das Feld Kaufeigenschaften eingeben. Weitere Einzelheiten finden Sie unter [Kaufobjekt]({{site.baseurl}}/api/objects_filters/purchase_object/).
{% endalert %}

{% endtab %}
{% tab Benutzer-Attribute %}

In der Konfigurationsansicht können Sie wählen, ob mit jedem Ereignis Attribute gesendet werden sollen.

Benutzerattribute können ein JSON-Objekt sein, das Felder enthält, die ein Attribut mit dem angegebenen Namen und Wert im angegebenen Benutzerprofil erstellen oder aktualisieren. Die folgenden Eigenschaften werden unterstützt:

| Benutzer-Attribut | Beschreibung |
| --- | --- |
| Vorname | Vorname des Benutzers. |
| Nachname | Nachname des Benutzers. |
| Tel. | Telefonnummer des Benutzers. |
| E-Mail | E-Mail Adresse des Benutzers. |
| Geschlecht | Eine der folgenden Zeichenketten: "M", "F", "O" (andere), "N" (nicht zutreffend), "P" (lieber nicht sagen). |
| Ort | Die Stadt des Benutzers. |
| Land | Das Land des Benutzers als Zeichenkette im Format [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). |
| Sprache | Die Sprache des Benutzers als Zeichenkette im Format [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). |
| Geburtsdatum | Die Geburtsdaten des Benutzers als String im Format "JJJJ-MM-TT" (zum Beispiel 1980-12-21). |
| Zeitzone | Name der Zeitzone aus der [IANA-Zeitzonendatenbank](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (z. B. 'Amerika/New_York' oder 'Eastern Time (US & Canada)'). |
| Facebook | Ein Hash mit einem der folgenden Werte: `id` (String), `likes` (Array von Strings), `num_friends` (Integer). |
| Twitter | Hash mit einer der folgenden Angaben: id (Ganzzahl), `screen_name` (String, X (ehemals Twitter) Handle), `followers_count` (Ganzzahl), `friends_count` (Ganzzahl), `statuses_count`(Ganzzahl). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Alle in der Konfiguration hinzugefügten Attribute werden jedes Mal gesendet, wenn das Ereignis an Braze gesendet wird, unabhängig davon, ob sich der Wert des Attributs geändert hat. Wenn Sie Benutzerattribute konfigurieren, stellen Sie bitte sicher, dass Sie wissen, wie sich dies auf Ihren Datenpunktverbrauch auswirkt.
{% endalert %}

{% endtab %}
{% endtabs %}

### Schritt 6: Daten in Braze validieren

Wenn die Ereignissammlung und die Integration von Adobe Experience Platform erfolgreich waren, sehen Sie die Ereignisse in der Braze-Konsole, wenn [Sie die Benutzerprofile ansehen]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/). Konkret werden die an Braze gesendeten neuen Ereignisdaten im Abschnitt **Einkäufe** oder **Benutzerdefinierte Ereignisse** auf der [Übersichtsregisterkarte]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#overview-tab) eines bestimmten Benutzers angezeigt.

[1]: {% image_buster /assets/img/efe.png %}
[3]: {% image_buster /assets/img/efe2.png %}