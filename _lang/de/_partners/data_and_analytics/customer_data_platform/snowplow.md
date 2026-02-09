---
nav_title: Snowplow
article_title: Snowplow
description: "Dieser Artikel referenziert die Partnerschaft zwischen Braze und Snowplow, einer Plattform für Dateninfrastrukturen, die es Ihnen erlaubt, Snowplow-Ereignisse in Realtime an Braze weiterzuleiten, indem Sie Snowplows Event Forwarding nutzen."
alias: /partners/snowplow/
page_type: partner
search_tag: Partner

---

# Snowplow

> [Snowplow](https://snowplowanalytics.com) ist eine skalierbare Plattform für eine umfangreiche, qualitativ hochwertige Datenerfassung mit geringer Latenz. Snowplow wurde entwickelt, um hochwertige, vollständige Verhaltensdaten für Unternehmen zu sammeln.

_Diese Integration wird von Snowplow gepflegt._

## Über die Integration

Die Integration von Braze und Snowplow ermöglicht Ihnen die Weiterleitung von Snowplow-Ereignissen an Braze in Realtime mit Hilfe der Snowplow Event Forwarding Lösung. Mit dieser Integration können Sie Ereignisse an Braze senden und gleichzeitig Flexibilität und Kontrolle bieten. Genauer gesagt, können Sie das:
- Filtern und transformieren Sie Ereignisse, bevor Sie sie an Braze senden.
- Ordnen Sie Snowplow-Ereignisdaten den Nutzer:innen-Attributen, angepassten Events und Käufen von Braze zu.
- Bewahren Sie alle Daten in Ihrer privaten Cloud auf, bis Sie sie weiterleiten möchten.
- Stellen Sie die Lösung selbst innerhalb Ihres bestehenden Snowplow Cloud-Kontos bereit. 

Die [Ereignisweiterleitung](https://docs.snowplow.io/docs/destinations/forwarding-events/) von Snowplow ist ein kostenpflichtiges Feature, das Snowplow Kund:innen zur Verfügung steht. Um Ereignisse ohne dieses Add-On an Braze weiterzuleiten, verwenden Sie die Google Tag Manager Server-Side [Integration](https://docs.snowplow.io/docs/destinations/forwarding-events/google-tag-manager-server-side/) von Snowplow [.](https://docs.snowplow.io/docs/destinations/forwarding-events/google-tag-manager-server-side/) 

Nutzen Sie die umfangreichen Verhaltensdaten von Snowplow, um leistungsstarke kundenorientierte Interaktionen in Braze voranzutreiben und personalisierte Nachrichten in Echtzeit zugestellt zu bekommen.

## Voraussetzungen

| Anforderung             | Beschreibung                                                                                                                                                                                                                                                                              |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Schneepflug-Pipeline       | Sie brauchen eine Schneepflug-Pipeline, die funktioniert.                                                                                                                                                                                                                                          |
| Zugang zur Schneepflug-Konsole | Sie müssen Zugriff auf die Snowplow-Konsole haben, um Ereignis-Forwarder zu konfigurieren.                                                                                                                                                                                                                                |
| Braze REST API-Schlüssel      | Ein Braze REST API-Schlüssel mit den folgenden Berechtigungen: `users.track`, `users.alias.new`, `users.identify`, `users.export.ids`, `users.merge`, `users.external_ids.rename`, und `users.alias.update`. <br><br> Sie können diesen im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellen. |
| Braze REST Endpunkt     | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab.                                                                                                                                     |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

### Personalisierte, aktionsbasierte Zustellung
Verwenden Sie eines der zahlreichen Ereignisse, die Snowplow standardmäßig sammelt, oder definieren Sie angepasste Events, um noch detailliertere Customer Journeys zu gestalten, die für Ihr Unternehmen sinnvoll sind. Nutzen Sie die reichhaltigen Verhaltensdaten von Snowplow, um Funnels für Kunden zu entwerfen und Ihren Marketing- und Produkt-Teams dabei zu helfen, Konversion und Produktnutzung durch Braze zu maximieren.

### Dynamische Segmentierung
Erstellen Sie dynamische Zielgruppen in Braze auf der Grundlage der hochwertigen Verhaltensdaten von Snowplow: Wenn Nutzer:innen in Ihrem Produkt, Ihrer App oder Ihrer Website Aktionen durchführen, können Sie die von Snowplow in Echtzeit erfassten Verhaltensdaten nutzen, um Nutzer:innen automatisch zu relevanten Segmenten in Braze hinzuzufügen oder zu entfernen.

## Integration

### Schritt 1: Konfigurieren Sie das Ziel in der Snowplow-Konsole

So erstellen Sie den Event Forwarder:

1. Navigieren Sie in der Snowplow-Konsole zu **Ziele** und wählen Sie **Neues Ziel erstellen**.
2. Wenn Sie die Verbindung konfigurieren, wählen Sie **Braze** als Verbindungstyp aus.
3. Geben Sie Ihren Braze API-Schlüssel und Ihren REST API-Endpunkt ein.
4. Speichern Sie die Verbindung.

### Schritt 2: Konfigurieren Sie den Event Forwarder

Bei der Konfiguration des Forwarders können Sie auswählen, welche Snowplow-Ereignisse weitergeleitet werden sollen, und sie auf Braze-Objekttypen abbilden:

1. **[Nutzer:innen Attribute]({{site.baseurl}}/api/objects_filters/user_attributes_object)**: Aktualisieren Sie die Daten des Nutzerprofils und die angepassten Eigenschaften der Nutzer:innen.
2. **[Angepasste Events]({{site.baseurl}}/api/objects_filters/event_object)**: Senden Sie Nutzer:innen Aktionen und Verhaltensweisen.
3. **[Einkäufe]({{site.baseurl}}/api/objects_filters/purchase_object)**: Senden Sie Transaktionsdaten mit Produktdetails.

Für jeden Objekttyp können Sie Feldzuordnungen konfigurieren, um festzulegen, wie Snowplow Ereignisdaten auf Braze Felder abgebildet werden. Detaillierte Anweisungen zur Einrichtung und Konfiguration der Abbildung von Feldern finden Sie in der [Dokumentation](https://docs.snowplow.io/docs/destinations/forwarding-events/creating-forwarders/) von Snowplow [zum Erstellen von Forwardern](https://docs.snowplow.io/docs/destinations/forwarding-events/creating-forwarders/).

### Schritt 3: Validieren Sie die Integration

Bestätigen Sie, dass die Ereignisse Braze erreichen, indem Sie die folgenden Seiten in Ihrem Braze-Konto überprüfen:

1. **Query Builder**: Navigieren Sie in Braze zu **Analytics** > **Query Builder**. Sie können Abfragen zu den folgenden Tabellen schreiben, um eine Vorschau der von Snowplow weitergeleiteten Daten zu erhalten: `USER_BEHAVIORS_CUSTOMEVENT_SHARED` und `USERS_BEHAVIORS_PURCHASE_SHARED`.
2. **API-Nutzungs-Dashboard**: Navigieren Sie in Braze zu **Einstellungen** > **APIs und Bezeichner**, um ein Chart der API-Nutzung im Laufe der Zeit anzuzeigen. Sie können speziell nach dem API-Schlüssel filtern, den Snowplow verwendet, und sowohl Erfolge als auch Misserfolge sehen.

## Anpassen von Eigenschaften senden

Sie können angepasste Eigenschaften über die Standardfelder hinaus senden. Die Struktur hängt davon ab, welchen Braze-Objekttyp Sie verwenden:

- **Nutzer**:**innen-Attribute**: Fügen Sie als Top-Level-Felder hinzu (zum Beispiel `subscription_tier`, `loyalty_points`)
- **Event-Eigenschaften**: Verschachtelung unter `properties` Objekt (zum Beispiel `properties.plan_type`, `properties.feature_flag`)
- **Kauf-Details der Eigenschaften**: Verschachtelung unter `properties` Objekt (zum Beispiel `properties.color`, `properties.size`)

Für Eigenschaftsnamen, die Leerzeichen enthalten, verwenden Sie die Klammerschreibweise (z.B. `["account type"]` oder `properties["campaign source"]`).

Einzelheiten zu den unterstützten Datentypen, den Anforderungen an die Benennung der Eigenschaften und den Größenbeschränkungen für die Nutzdaten finden Sie in der [Dokumentation zum Ereignisobjekt]({{site.baseurl}}/api/objects_filters/event_object).

## Beschränkungen

**Rate-Limits:** Braze setzt ein Rate-Limits von 3.000 API-Aufrufen alle drei Sekunden für die Track Nutzer:innen API durch. Da Snowplow keine Stapelverarbeitung für Ereignis-Forwarder unterstützt, fungiert dieses API Rate-Limit auch als Rate-Limit für Ereignisse. Wenn Ihr Eingabedurchsatz 3.000 Ereignisse pro drei Sekunden überschreitet, kann es zu erhöhten Latenzzeiten kommen.
