---
nav_title: GESEHEN
article_title: GESEHEN
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und SEEN, einer Plattform zur Gestaltung personalisierter Videos, um das Engagement während der gesamten Customer Journey zu erhöhen."
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# GESEHEN

> [SEEN](https://seen.io/) ist eine Videoplattform zur Personalisierung, die es Unternehmen ermöglicht, Videos zu erstellen und auf ihre Kunden abzustimmen, um ihnen ein ansprechendes Erlebnis zu bieten. Mit SEEN können Sie ein Video um Ihre Daten herum entwerfen, es in der Cloud in großem Umfang personalisieren und es dann dort verteilen, wo es am besten funktioniert.

## Anwendungsfälle

SEEN bietet automatisierte Videopersonalisierung über die gesamte Customer Journey. Zu den üblichen Anwendungen gehören Onboarding, Loyalität, Anmeldungen und Konversion sowie Win-Back und Anti-Abwanderung.

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung          | Beschreibung                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Eine SEEN-Kampagne   | Um die Vorteile dieser Partnerschaft zu nutzen, ist eine SEEN-Kampagne erforderlich.                                                                     |
| Datenquelle   | Um Ihre Videos zu personalisieren, müssen Sie Daten an SEEN senden. Stellen Sie sicher, dass Sie alle relevanten Daten in Braze zur Verfügung haben und dass Sie Daten mit **braze_id** als Bezeichner übergeben. |
| Braze Data Transformation Webhook URL   | Braze Data Transformation wird verwendet, um die von SEEN eingehenden Daten so umzuformatieren, dass sie vom /users/track-Endpunkt von Braze akzeptiert werden können. |

## Preisgrenze

Die SEEN API nimmt derzeit 1.000 Anrufe pro Stunde entgegen.

## Integration von SEEN mit Braze

Im folgenden Beispiel senden wir die Daten der Benutzer zur Videoerstellung an SEEN und erhalten einen eindeutigen Landing Page-Link und ein eindeutiges, personalisiertes Thumbnail zurück an Braze zur Verteilung. Dieses Beispiel verwendet einen POST-Webhook, um Daten an SEEN zu senden, und eine Datenumwandlung, um die Daten zurück an Braze zu erhalten. Wenn Sie mehrere Videokampagnen mit SEEN haben, wiederholen Sie den Vorgang, um Braze mit allen Videokampagnen zu verbinden.

{% alert tip %}
Sollten Sie Probleme haben, wenden Sie sich bitte an Ihren SEEN Customer Success Manager, um Hilfe zu erhalten.
{% endalert %}

### Schritt 1: Erstellen Sie eine Webhook-Kampagne

Erstellen Sie eine neue [Webhook-Kampagne](https://www.braze.com/docs/user_guide/message_building_by_channel/webhooks) in Braze. Geben Sie Ihrer Kampagne einen Namen und entnehmen Sie dann der folgenden Tabelle, wie Sie Ihren Webhook zusammenstellen:

{% raw %}
<table>
  <thead>
    <tr>
      <th><strong>Feld</strong></th>
      <th><strong>Details</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Webhook-URL</strong></td>
      <td>Verwenden Sie die folgende Webhook-URL. Sie erhalten Ihr <code>campaign_slug</code> von SEEN, um den richtigen Endpunkt aufzurufen.<br><br><code>https://api.seen.io/v1/campaigns/{campaign_slug}/receivers/</code></td>
    </tr>
    <tr>
      <td><strong>HTTP-Methode</strong></td>
      <td>Verwenden Sie die <code>POST</code> Methode.</td>
    </tr>
    <tr>
      <td><strong>Anfragetext</strong></td>
      <td>Geben Sie den Text Ihrer Anfrage in Rohform ein, ähnlich wie im Folgenden.<br><br><pre><code>[
    {
    "first_name":"{{${first_name}}}",
    "last_name":"{{${last_name}}}",
    "email":"{{${email_address}}}",
    "customer_id":"{{${braze_id}}}"
    }
]</code></pre><br>Weitere Informationen finden Sie unter <a href="https://docs.seen.io/api-documentation/ntRoJJ3rXoHzFXhA94JiHB/overview/tvy2F5tS3JRM7DfcHwz5fK#request-content">SEEN API</a>.</td>
    </tr>
    <tr>
      <td><strong>Kopfzeilen der Anfrage</strong></td>
      <td>Verwenden Sie die folgenden Informationen, um die Kopfzeilen Ihrer Anfrage auszufüllen:<br>- <strong>Autorisierung:</strong> <code>Token {token}</code><br>- <strong>Inhalt-Typ:</strong> <code>application/json</code><br><br>Sie erhalten Ihren Authentifizierungs-Token von SEEN.</td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Sie können den Webhook jetzt mit einem Benutzer testen, indem Sie auf die Registerkarte **Test** wechseln.

Wenn alles wie gewünscht funktioniert, gehen Sie zu Braze und setzen Sie die Rate, mit der die Kampagne sendet, auf 10 **Nachrichten pro Minute**. Auf diese Weise überschreiten Sie nicht das SEEN-Ratenlimit von 1.000 Anrufen pro Stunde.

### Schritt 2: Datenumwandlung erstellen

1. Erstellen Sie neue [benutzerdefinierte Attributfelder](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) für `landing_page_url` und `email_thumbnail_url`. Dies sind die beiden Attribute, die wir in diesem Beispiel verwenden werden.
2. Öffnen Sie [Datenumwandlung](https://www.braze.com/docs/user_guide/data_and_analytics/data_transformation/creating_a_transformation/#prerequisites) unter **Dateneinstellungen** und wählen Sie **Umwandlung erstellen**.
3. Geben Sie Ihrer Transformation einen Namen, wählen Sie **Neu beginnen** und setzen Sie das **Ziel** auf **POST: Benutzer verfolgen**.
4. Wählen Sie **Ihre Webhook-URL mit SEEN teilen**.
5. Sie können den folgenden Code als Ausgangspunkt für die Transformation verwenden:

```javascript
let brazecall = {
  "attributes": [
    {
      "braze_id": payload.customer_id,
      "_update_existing_only": true,
      "landing_page_url": payload.landing_page_url,
      "email_thumbnail_url": payload.email_thumbnail_url
    }
  ]
};
return brazecall;
```
{% alert note %}
Wenn Sie andere Daten einbeziehen möchten, müssen Sie diese ebenfalls angeben. Denken Sie daran, sich auch mit SEEN abzusprechen, damit die Nutzlast des Rückrufs alle benötigten Felder enthält.
{% endalert %}

{: start="6"}
6\. Senden Sie eine Test-Nutzlast an den angegebenen Endpunkt. Wenn Sie die in der [SEEN-Dokumentation](https://docs.seen.io/api-documentation/ntRoJJ3rXoHzFXhA94JiHB/callbacks/k9DEbcgkq3Vr2pxbHyPQbp) definierte Rückruf-Payload verwenden möchten, können Sie diese selbst mit [Postman](https://www.postman.com/) oder einem anderen ähnlichen Dienst versenden:

```json
{
        "customer_id": "101",
        "campaign_slug": "onboarding",
        "landing_page_url": "your.subdomain.com/v/12345",
        "video_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/output.m3u8",
        "thumbnail_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/thumbnail.jpg",
        "email_thumbnail_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/email_thumbnail.jpg"
       
}
```

{: start="7"}
7\. Wählen Sie **Validieren**, um sicherzustellen, dass alles wie vorgesehen funktioniert.
8\. Wählen Sie **Speichern** und **Aktivieren**.
