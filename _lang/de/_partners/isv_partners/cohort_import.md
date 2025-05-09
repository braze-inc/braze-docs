---
nav_title: Integration von Kohortenimport
alias: /cohort_import/
hidden: true
---

# Integration des Kohortenimports von Partnern

> Das Feature der Partner Kohortenimport Integration erlaubt es unseren Partnern, sich mit Braze zu integrieren, um Nutzer:innen-Kohorten zu versenden, die in der Anwendung des Partners generiert wurden.

## Cluster-URLs

Braze hostet unsere Anwendung auf mehreren Clustern in den USA und der EU. Die URL für die Import-Endpunkte ist unterschiedlich, je nachdem, auf welchem Cluster die Instanz des Unternehmens des Clients gehostet wird:

| INSTANZ | REST ENDPUNKT |
| ----- | ------------------------------- |
| US-01 | `https://rest.iad-01.braze.com` |
| US-02 | `https://rest.iad-02.braze.com` |
| US-03 | `https://rest.iad-03.braze.com` |
| US-04 | `https://rest.iad-04.braze.com` |
| US-05 | `https://rest.iad-05.braze.com` |
| US-06 | `https://rest.iad-06.braze.com` |
| US-07 | `https://rest.iad-07.braze.com` |
| US-08 | `https://rest.iad-08.braze.com` |
| EU-01 | `https://rest.fra-01.braze.eu`  |
| EU-02 | `https://rest.fra-02.braze.eu`  |
| AU-01 | `https://rest.au-01.braze.com`  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Endpunkt-URLs

Nicht nur die Top-Level-URLs sind clusterspezifisch, sondern auch jeder Endpunkt ist partnerspezifisch. Wenn Sie beispielsweise in unseren US01-Cluster importieren, hat die URL das Format `https://rest.iad-01.braze.com/partners/[partner_name]/…`, wobei `[partner_name]` normalerweise der Name des Unternehmens des Partners ist. Die Besonderheiten der einzelnen Endpunkte werden in den folgenden Abschnitten beschrieben.

## Authentifizierung

Um Kohortendaten in Braze zu importieren, sind zwei Authentifizierungsschlüssel erforderlich.

### API-Schlüssel des Partners

Der Partner API-Schlüssel identifiziert den Partner der Integration und bestätigt, dass die Anfrage für den Import gültig ist. Der Schlüssel sollte im Text der Anfrage im Feld `partner_api_key` enthalten sein.

Beim Einrichten der Integration in der Anwendung des Partners sollte der Client aufgefordert werden, seinen Braze-Cluster anzugeben, damit die Integration weiß, welche Cluster-URL und welchen API-Schlüssel des Partners sie beim Importieren von Daten verwenden soll.

Braze wird dem Partner den/die API-Schlüssel zur Verfügung stellen, bevor der Partner mit der Entwicklung der Integration beginnt. Im Allgemeinen werden wir einen einzigen Schlüssel bereitstellen, der für alle US-Cluster gültig ist, und einen weiteren Schlüssel, der für unseren EU-Cluster gültig ist.

### Client-Datenimport-Schlüssel

Der Datenimport-Schlüssel des Clients identifiziert den Workspace des Clients, in den die Kohorte importiert werden soll. Der Schlüssel sollte im Text der Anfrage im Feld `client_secret` enthalten sein.

Dieser Schlüssel wird im Dashboard des Clients in den Einstellungen für die Integration des Partners generiert. Beim Einrichten der Integration in der Anwendung des Partners sollte der Client aufgefordert werden, seinen Datenimport-Schlüssel anzugeben, damit die Integration weiß, an welchen Client und Workspace sie Daten senden soll.

## API Endpunkt-Spezifikationen

### Name der Kohorte Endpunkt

Der Endpunkt Kohortenname kann verwendet werden, um den Namen einer Kohorte auf der Grundlage ihrer ID anzugeben. Dieser Endpunkt sollte immer dann aufgerufen werden, wenn eine Kohorte erstmals nach Braze exportiert wird oder wenn der Name einer Kohorte, die Braze bereits bekannt ist, geändert wird.

| Feld | Typ | Erforderlich | Anmerkungen |
| ----- | ---- | -------- | ----- |
| `partner_api_key` | String | Ja | Partnerspezifischer API-Schlüssel, der in allen Anfragen von Partnern an Braze verwendet wird. Dieser Schlüssel ist clusterspezifisch (siehe [API-Schlüssel des Partners](#partner-api-key)), so dass der Partner den Cluster kennen muss, in den die Kohorten geschrieben werden sollen. |
| `client_secret` | String | Ja | Datenimport-Schlüssel für den Client, zu dessen Kohorte dies gehört. |
| `cohort_id` | String | Ja | Bezeichner für die Kohorte. Dieser Bezeichner sollte für den angegebenen Client eindeutig sein. |
| `name` | String | Ja | Vom Client festgelegter Name für die Kohorte |
| `created_at` | String | Ja | Zeitstempel im ISO-8601-Format |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

#### Beispiel einer Anfrage:

`POST: https://rest.iad-01.braze.com/partners/[partner_name]/cohorts`
```
{
	"partner_api_key" : "123456-1234-1234-12345678",
	"client_secret" : "234567-2345-2345-23456789",
	"cohort_id" : "[some unique identifier generated by the partner]",
	"name" : "Name of the cohort that will appear in the Braze dashboard",
	"created_at" : "2021-01-21T19:20:30+05:00"
}
```

### Endpunkt der Nutzer:innen Kohorte

Der Endpunkt Nutzerkohorte erlaubt es, anzugeben, welche Nutzer:innen zu einer bestimmten Kohorte hinzugefügt oder aus ihr entfernt wurden. Dieser Endpunkt sollte aufgerufen werden, wenn eine Kohorte aufgefrischt wird. Nur Nutzer:innen, die neu in die Kohorte eingetreten sind oder die Kohorte seit der letzten Aktualisierung verlassen haben, sollten an Braze gesendet werden.

| Feld | Typ | Erforderlich | Anmerkungen |
| ----- | ---- | -------- | ----- |
| `partner_api_key` | String | Ja | Partnerspezifischer API-Schlüssel, der in allen Anfragen von Partnern an Braze verwendet wird. Dieser Schlüssel ist cluster-spezifisch (siehe [Partner API-Schlüssel](#partner-api-key)), so dass die Integration den Cluster kennen muss, in den die Kohorten geschrieben werden sollen. |
| `client_secret` | String | Ja | Datenimport-Schlüssel für den Client, zu dessen Kohorte dies gehört. |
| `cohort_id` | String | Ja | Bezeichner für die Kohorte. Der Bezeichner sollte für den angegebenen Client eindeutig sein. |
| `cohort_changes` | Array von Objekten | Ja | Objekte können zwei Felder haben. Eine, `user_ids`, ist erforderlich und kann ein Array aus `external_ids`, `device_ids` und `aliases` sein. Jedes Element ist eine ID für einen Nutzer:in, dessen Status in der Kohorte sich geändert hat. Das zweite Feld, `should_remove`, ist ein optionaler Boolescher Wert, der angibt, ob die Nutzer:innen in diesem Objekt aus der Kohorte entfernt werden sollen, anstatt sie hinzuzufügen. Der Standardwert ist false. Die maximale kombinierte Länge der Nutzer:innen IDs in einer Anfrage beträgt 1.000.<br/><br/>Identifizierte Nutzer:innen können entweder über ihre `external_id` oder `alias` abgeglichen werden. Anonyme Nutzer:innen können über ihre `device_id` gefunden werden. Wenn Sie eine Geräte ID für einen identifizierten Nutzer:innen eingeben, wird Braze diesen Nutzer:innen nicht hinzufügen oder entfernen. Sie müssen für identifizierte Nutzer:innen externe IDs oder Aliase verwenden. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

#### Beispiel einer Anfrage:

`POST: https://rest.iad-01.braze.com/partners/[partner_name]/cohorts/users`
```
{
	"partner_api_key" : "123456-1234-1234-12345678",
	"client_secret" : "234567-2345-2345-23456789",
	"cohort_id" : "[some unique identifier generated by the partner]",
	"cohort_changes" : [
	   {"user_ids": ["test_user_1", "test_user_2"]}
	]
}
```

## Rate-Limiting

Zusätzlich zu den maximal 1.000 IDs pro Anfrage im Endpunkt der Nutzer:innen-Kohorte sind diese Endpunkt-Anfragen auf 250.000 Anfragen pro Stunde rate-limitiert.

## Kohorten Filter

Braze fügt einen Filter hinzu, der es einem Dashboard-Benutzer erlaubt, Nutzer:innen aus einer Targeting-Zielgruppe ein- oder auszuschließen, wenn sie zu einer Partner-Kohorte gehören. Der Filter bietet eine Dropdown-Liste mit den Namen aller Kohorten, die Braze für diesen Client kennt. Dieser Filter ist nur für Clients sichtbar, mit denen sich Partner und Braze auf diese Integration geeinigt haben.

## Fehlersuche

In der folgenden Tabelle finden Sie spezifische Fehlercodes für die Endpunkte von Kohortenimport und wie Sie diese beheben können.

| Fehlercode | Beschreibung |
| ----- | ---- |
| `400` | `cohort_id` muss ein gültiger String sein |
|  | `cohort_changes` muss ein Array von Objekten mit den Schlüsseln `user_ids` und/oder `device_ids` sein, die auf ein String-Array abgebildet werden, oder ein `aliases` Objekt |
|  | Pro Anfrage sind nur 1.000 `user_ids`, `device_ids`, und `aliases` zulässig. |
|  | `name` muss ein nicht leerer String sein |
|  | `created_at` muss eine gültige Zeit in Form eines [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601) Strings sein |
| `401` | Ungültiger API-Schlüssel des Partners |
|  | Ungültiges Client-Geheimnis |
|  | Partner nicht aktiviert für Client mit Client Geheimnis: **<Client Geheimnis>** |
|  | Unbefugter Zugriff |
| `423` | Ressource gesperrt |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Weitere Informationen zur Fehlerbehebung finden Sie unter [Fehler & Antworten]({{site.baseurl}}/api/errors/), in denen die verschiedenen Fehler und Server-Antworten beschrieben werden, die bei der Verwendung der Braze API auftreten können.
