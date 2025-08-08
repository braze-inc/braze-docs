---
nav_title: Erweiterung der Ereignisweiterleitung
article_title: Adobe
description: "Dieser referenzierte Artikel behandelt die Braze Event Forward-Erweiterung, mit der Sie die im Adobe Experience Platform Edge Network erfassten Daten nutzen und sie in Form von serverseitigen Ereignissen an Braze senden können."
page_type: partner
page_order: 2
search_tag: Partner

---

# Tracking Events API Erweiterung der Ereignisweiterleitung

> Die [Ereignisweiterleitungserweiterung](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en) Braze Track Events API erlaubt es Ihnen, Daten zu nutzen, die im Adobe Experience Platform Edge Network erfasst wurden, und sie in Form von serverseitigen Ereignissen an Braze zu senden, indem Sie die [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) API.

Dieses Dokument beschreibt die Anwendungsfälle der Erweiterung, wie Sie sie in Ihren Bibliotheken für die Ereignisweiterleitung installieren und wie Sie ihre Funktionen in einer [Regel für](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) die Ereignisweiterleitung einsetzen.

{% alert note %}
Das Senden von Attributen an Braze kann den Verbrauch von Datenpunkten in Braze erhöhen. Wenden Sie sich an Ihren Braze-Konto Manager:in, bevor Sie Attribute senden. Weitere Informationen finden Sie in der Dokumentation von Braze über [abrechenbare Datenpunkte]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#billable-data-points).
{% endalert %}

## Anwendungsfälle

Diese Erweiterung sollte Daten aus dem Edge Network in Braze verwenden, um die Vorteile seiner Analytics- und Targeting-Funktionen für Kunden zu nutzen.

Nehmen Sie zum Beispiel ein Einzelhandelsunternehmen mit einer Multichannel-Präsenz (Website und Mobile) und der Erfassung von Transaktions- oder Konversationsdaten als Ereignisdaten von ihrer Website und ihren mobilen Plattformen. 

Mithilfe verschiedener [Tag-Regeln](https://experienceleague.adobe.com/docs/experience-platform/tags/home.html?lang=en) werden diese Daten in Realtime an das Edge-Netzwerk gesendet. Von hier aus sendet die Erweiterung für die Ereignisweiterleitung von Braze automatisch relevante Ereignisse von der Server-Seite an Braze.

## Rate-Limits

| API | Rate-Limits |
| --- | --- |
| Nutzer:innen Tracking | 50.000 Anfragen pro Minute.<br><br>Einzelheiten finden Sie in der [Dokumentation der User Tracking API]({{site.baseurl}}/api/endpoints/user_data/post_user_track#rate-limit).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Erfassen Sie die erforderlichen Konfigurationsdetails

Um das Edge Network mit Braze zu verbinden, benötigen Sie Folgendes:

| Schlüssel-Typ | Beschreibung |
| --- | --- |
| Braze-Instanz | Ihre Braze-Instanz erhalten Sie von Ihrem Braze Onboarding Manager oder auf der [Übersichtsseite über die APIs]({{site.baseurl}}/api/basics/#endpoints). |
| Braze REST API-Schlüssel | Ein REST-API-Schlüssel von Braze mit allen Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Schritt 2: Erstellen Sie ein Geheimnis

Erstellen Sie ein neues [Ereignisweiterleitungsgeheimnis](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/secrets.html?lang=en) und setzen Sie den Wert auf Ihren [Braze API-Schlüssel](https://experienceleague.adobe.com/docs/experience-platform/tags/extensions/server/braze/overview.html?lang=en#configuration-details). Dies wird verwendet, um die Verbindung zu Ihrem Konto zu authentifizieren und den Wert sicher zu halten.

### Schritt 3: Installieren und konfigurieren Sie die Braze-Erweiterung

1. Um die Erweiterung zu installieren, [erstellen Sie eine Eigenschaft für die Ereignisweiterleitung](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en#properties) oder wählen Sie stattdessen eine vorhandene Eigenschaft zur Bearbeitung aus.
2. Wählen Sie dann in der linken Navigation **Erweiterungen** aus. Wählen Sie auf dem Tab **Katalog** die Option Auf der Karte für die Braze-Erweiterung **installieren** aus.
3. Geben Sie auf dem nächsten Bildschirm Ihre REST Instanz und Ihren API-Schlüssel ein und wählen Sie anschließend **Speichern**.

### Schritt 4: Erstellen Sie eine Regel zum Senden von Ereignissen

Nachdem Sie die Erweiterung installiert haben, erstellen Sie eine neue [Regel für](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) die Ereignisweiterleitung und konfigurieren die Bedingungen wie gewünscht. Wenn Sie die Aktionen für die Regel konfigurieren, wählen Sie die **Braze-Erweiterung** aus und wählen Sie dann **Ereignis senden** als Aktionstyp.

![]({% image_buster /assets/img/efe.png %})

{% tabs local %}
{% tab Nutzer:in Identifikation %}

| Eingabe | Beschreibung |
| --- | --- |
| Externe Benutzer-ID | Eine lange, zufällige und gut verteilte UUID oder GUID. Wenn Sie eine andere Methode zur Benennung Ihrer Nutzer:innen wählen, müssen diese ebenfalls lang, zufällig und gut verteilt sein. Erfahren Sie mehr über die [vorgeschlagene Namenskonvention für Nutzer:innen]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#suggested-user-id-naming-convention). |
| Braze Nutzer:innen ID | Braze Nutzer:innen Bezeichner. |
| Nutzer:in alias | Ein Alias dient als alternativer eindeutiger Bezeichner für Nutzer:innen. Verwenden Sie Aliase, um Nutzer:innen anhand anderer Dimensionen als Ihrer zentralen ID zu identifizieren.<br><br>Das Nutzer-Alias-Objekt besteht aus zwei Teilen: einem `alias_name` für den Bezeichner selbst und einem `alias_label`, der den Typ des Alias angibt. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Bezeichnungen haben, aber nur einen `alias_name` pro `alias_label`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Um das Ereignis mit einem Nutzer:innen zu verknüpfen, müssen Sie entweder das Feld `External User ID`, das Feld `Braze User Identifier` oder den Abschnitt `User Alias` ausfüllen.
{% endalert %}

{% endtab %}
{% tab Daten zum Ereignis %}

| Eingabe | Beschreibung | Erforderlich |
| --- | --- | --- |
| Event-Name | Name der Veranstaltung. | Ja |
| Zeit der Veranstaltung | Datumszeit als String im Format ISO 8601 oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. | Ja |
| Bezeichner der App | Der App-Bezeichner oder `app_id` ist ein Parameter, der eine Aktivität mit einer bestimmten App in Ihrem Workspace verbindet. Es zeigt an, mit welcher App innerhalb des Arbeitsbereichs Sie interagieren. | Kein:e |
| Event-Eigenschaften | Ein JSON-Objekt mit angepassten Eigenschaften des Events. | Kein:e |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Für die Aktion **Braze Ereignis senden** müssen nur der **Ereignisname** und die **Ereigniszeit** angegeben werden, aber Sie sollten so viele Informationen wie möglich in das Feld für angepasste Eigenschaften eingeben. Siehe [Ereignisobjekt]({{site.baseurl}}/api/objects_filters/event_object/) für weitere Details.
{% endalert %}

{% endtab %}
{% tab Nutzer:innen Attribut %}

Benutzerattribute können ein JSON-Objekt sein, das Felder enthält, mit denen ein Attribut mit dem angegebenen Namen und Wert für das angegebene Nutzerprofil erstellt oder aktualisiert wird. Die folgenden Eigenschaften werden unterstützt:

| Nutzer:innen Attribut | Beschreibung |
| --- | --- |
| Vorname | Vorname des Nutzers:innen. |
| Nachname | Nachname des Nutzers:in. |
| Telefon | Telefonnummer des Nutzers:innen. |
| E-Mail | E-Mail Adresse des Nutzers:innen. |
| Geschlecht | Einer der folgenden Strings: "M", "F", "O" (andere), "N" (nicht zutreffend), "P" (lieber nicht sagen). |
| Ort | Der Ort des Nutzers:in. |
| Land | Das Land des Nutzers:in als String im Format [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). |
| Sprache | Die Sprache des Nutzers:in als String im Format [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). |
| Geburtsdatum | Die Nutzerdaten der Nutzer:innen als String im Format "JJJJ-MM-TT" (z.B. 1980-12-21). |
| Zeitzone | Name der Zeitzone aus der [IANA-Zeitzonendatenbank](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (z. B. 'Amerika/New_York' oder 'Eastern Time (US & Canada)'). |
| Facebook | Ein Hash mit einem der folgenden Werte: `id` (String), `likes` (String-Array), `num_friends` (Ganzzahl). |
| Twitter | Hash mit einer der folgenden Angaben: id (Ganzzahl), `screen_name` (String, X (ehemals Twitter) Handle), `followers_count` (Ganzzahl), `friends_count` (Ganzzahl), `statuses_count`(Ganzzahl). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Alle in der Konfiguration hinzugefügten Attribute werden jedes Mal gesendet, wenn das Ereignis an Braze gesendet wird, unabhängig davon, ob sich der Wert des Attributs geändert hat. Wenn Sie Nutzer:innen-Attribute konfigurieren, stellen Sie sicher, dass Sie wissen, wie sich dies auf die Nutzung Ihrer Datenpunkte auswirkt.
{% endalert %}

{% endtab %}
{% endtabs %}

### Schritt 5: Erstellen Sie eine Regel zum Senden eines Kauf-Events

Nachdem Sie die Erweiterung installiert haben, erstellen Sie eine neue [Regel für](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) die Ereignisweiterleitung und konfigurieren die Bedingungen wie gewünscht. Wenn Sie die Aktionen für die Regel konfigurieren, wählen Sie die **Braze-Erweiterung** aus und wählen dann als Aktionstyp **Kauf-Event senden**.

![]({% image_buster /assets/img/efe2.png %})

{% tabs local %}
{% tab Nutzer:in Identifikation %}

| Eingabe | Beschreibung |
| --- | --- |
| Externe Benutzer-ID | Eine lange, zufällige und gut verteilte UUID oder GUID. Wenn Sie eine andere Methode zur Benennung Ihrer Nutzer:innen wählen, müssen diese ebenfalls lang, zufällig und gut verteilt sein. Erfahren Sie mehr über die [vorgeschlagene Namenskonvention für Nutzer:innen]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#suggested-user-id-naming-convention). |
| Braze Nutzer:innen ID | Braze Nutzer:innen Bezeichner. |
| Nutzer:in alias | Ein Alias dient als alternativer eindeutiger Bezeichner für Nutzer:innen. Verwenden Sie Aliase, um Nutzer:innen anhand anderer Dimensionen als Ihrer zentralen ID zu identifizieren.<br><br>Das Nutzer-Alias-Objekt besteht aus zwei Teilen: einem `alias_name` für den Bezeichner selbst und einem `alias_label`, der den Typ des Alias angibt. Nutzer:innen können mehrere Aliasnamen mit unterschiedlichen Bezeichnungen haben, aber nur einen `alias_name` pro `alias_label`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Um das Ereignis mit einem Nutzer:innen zu verknüpfen, müssen Sie entweder das Feld `External User ID`, das Feld `Braze User Identifier` oder den Abschnitt `User Alias` ausfüllen.
{% endalert %}

{% endtab %}
{% tab Daten zum Kauf %}

| Eingabe | Beschreibung | Erforderlich |
| --- | --- | --- |
| Produkt ID | Bezeichner für den Kauf. (zum Beispiel Produktname oder Produktkategorie) | Ja |
| Kaufzeitpunkt | Datumszeit als String im Format ISO 8601 oder im Format `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. | Ja |
| Währung | Währung als String im Format des alphabetischen [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) Währungscodes. | Ja |
| Preis | Der Preis des Objekts. | Ja |
| Menge | Die gekaufte Menge. Wenn nicht angegeben, ist der Standardwert 1. Der Höchstwert muss kleiner als 100 sein. | Kein:e |
| Bezeichner der App | Der App-Bezeichner oder `app_id` ist ein Parameter, der eine Aktivität mit einer bestimmten App in Ihrem Workspace verbindet. Es zeigt an, mit welcher App innerhalb des Arbeitsbereichs Sie interagieren. | Kein:e |
| Eigenschaften des Kaufs | Ein JSON-Objekt mit angepassten Eigenschaften des Kaufs. | Kein:e |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Für die Aktion **Kauf-Event senden** muss nur `Product ID`, `Purchase Time`, `Currency` und `Price` angegeben werden, aber Sie sollten so viele Informationen wie möglich in das Feld Kauf-Details eingeben. Siehe [Kauf-Objekt]({{site.baseurl}}/api/objects_filters/purchase_object/) für weitere Details.
{% endalert %}

{% endtab %}
{% tab Benutzerattribute %}

In der Konfigurationsansicht können Sie wählen, ob Attribute mit jedem Ereignis gesendet werden sollen.

Benutzerattribute können ein JSON-Objekt sein, das Felder enthält, mit denen ein Attribut mit dem angegebenen Namen und Wert für das angegebene Nutzerprofil erstellt oder aktualisiert wird. Die folgenden Eigenschaften werden unterstützt:

| Nutzer:innen Attribut | Beschreibung |
| --- | --- |
| Vorname | Vorname des Nutzers:innen. |
| Nachname | Nachname des Nutzers:in. |
| Telefon | Telefonnummer des Nutzers:innen. |
| E-Mail | E-Mail Adresse des Nutzers:innen. |
| Geschlecht | Einer der folgenden Strings: "M", "F", "O" (andere), "N" (nicht zutreffend), "P" (lieber nicht sagen). |
| Ort | Der Ort des Nutzers:in. |
| Land | Das Land des Nutzers:in als String im Format [ISO-3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). |
| Sprache | Die Sprache des Nutzers:in als String im Format [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). |
| Geburtsdatum | Die Nutzerdaten der Nutzer:innen als String im Format "JJJJ-MM-TT" (z.B. 1980-12-21). |
| Zeitzone | Name der Zeitzone aus der [IANA-Zeitzonendatenbank](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (z. B. 'Amerika/New_York' oder 'Eastern Time (US & Canada)'). |
| Facebook | Ein Hash mit einem der folgenden Werte: `id` (String), `likes` (String-Array), `num_friends` (Ganzzahl). |
| Twitter | Hash mit einer der folgenden Angaben: id (Ganzzahl), `screen_name` (String, X (ehemals Twitter) Handle), `followers_count` (Ganzzahl), `friends_count` (Ganzzahl), `statuses_count`(Ganzzahl). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Alle in der Konfiguration hinzugefügten Attribute werden jedes Mal gesendet, wenn das Ereignis an Braze gesendet wird, unabhängig davon, ob sich der Wert des Attributs geändert hat. Wenn Sie Nutzer:innen-Attribute konfigurieren, vergewissern Sie sich bitte, dass Sie wissen, wie sich dies auf den Verbrauch Ihrer Datenpunkte auswirkt.
{% endalert %}

{% endtab %}
{% endtabs %}

### Schritt 6: Daten innerhalb von Braze validieren

Wenn die Ereignissammlung und die Integration von Adobe Experience Platform erfolgreich waren, sehen Sie die Ereignisse in der Braze-Konsole, wenn [Sie Nutzer:innen-Profile anzeigen]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/). Insbesondere werden die an Braze gesendeten neuen Ereignisdaten im Abschnitt **Käufe** oder **angepasste Events** auf der [Übersichts-Registerkarte]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#overview-tab) eines bestimmten Nutzers angezeigt.

