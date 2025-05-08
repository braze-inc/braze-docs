---
nav_title: SEEN
article_title: SEEN
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und SEEN, einer Plattform zur Gestaltung personalisierter Videos, um das Engagement während der Customer Journey zu steigern."
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# SEEN

> [SEEN](https://seen.io/) ist eine Videoplattform zur Personalisierung, die es Unternehmen erlaubt, Videos rund um ihre Kund:in zu erstellen und zu erstellen, um so ein stärkeres Engagement zu erreichen. Mit SEEN können Sie ein Video um Ihre Daten herum entwerfen, es in der Cloud in großem Umfang personalisieren und es dann dort verteilen, wo es am besten funktioniert.

## Anwendungsfälle

SEEN bietet automatisierte Video-Personalisierung über die gesamte Customer Journey hinweg. Zu den üblichen Anwendungen gehören Onboarding, Loyalität, Registrierung und Konversion sowie Rückgewinnung und Anti-Abwanderung.

## Voraussetzungen

Bevor Sie beginnen, benötigen Sie Folgendes:

| Voraussetzung          | Beschreibung                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Eine SEEN-Kampagne   | Um von dieser Partnerschaft zu profitieren, ist eine SEEN Kampagne erforderlich.                                                                     |
| Datenquelle   | Sie müssen Daten an SEEN senden, um Ihre Videos zu personalisieren. Stellen Sie sicher, dass Sie alle relevanten Daten in Braze zur Verfügung haben und dass Sie Daten mit **braze_id** als Bezeichner übergeben. |
| Braze-Daten-Transformation Webhook URL   | Die Braze Datentransformation wird verwendet, um die von SEEN eingehenden Daten so umzuformatieren, dass sie vom /users/track Endpunkt von Braze akzeptiert werden können. |

## Rate-Limit

Die SEEN API nimmt derzeit 1.000 Anrufe pro Stunde entgegen.

## Integration von SEEN mit Braze

Im folgenden Beispiel senden wir die Daten der Nutzer:innen zur Erstellung von Videos an SEEN und erhalten einen eindeutigen Link zur Landing Page und ein eindeutiges, personalisiertes Thumbnail zurück an Braze zur Verteilung. Dieses Beispiel verwendet einen POST-Webhook, um Daten an SEEN zu senden, und eine Datentransformation, um die Daten zurück an Braze zu erhalten. Wenn Sie mehrere Videokampagnen mit SEEN haben, wiederholen Sie den Vorgang, um Braze mit allen Videokampagnen zu verbinden.

{% alert tip %}
Wenn Sie Probleme haben, wenden Sie sich bitte an Ihren Customer-Success-Manager:in von SEEN.
{% endalert %}

### Schritt 1: Erstellen Sie eine Webhook-Kampagne

Erstellen Sie eine neue [Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks) in Braze. Geben Sie Ihrer Kampagne einen Namen und referenzieren Sie dann die folgende Tabelle, um Ihren Webhook zusammenzustellen:

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
      <td>Verwenden Sie die <code>POST</code> Methode:</td>
    </tr>
    <tr>
      <td><strong>Anfragetext</strong></td>
      <td>Geben Sie den Text Ihrer Anfrage in Rohform ein, etwa so wie im Folgenden.<br><br><pre><code>[
    {
    "first_name":"{{${first_name}}}",
    "last_name":"{{${last_name}}}",
    "email":"{{${email_address}}}",
    "customer_id":"{{${braze_id}}}"
    }
]</code></pre><br>Weitere Informationen finden Sie unter <a href="https://docs.seen.io/api-documentation/ntRoJJ3rXoHzFXhA94JiHB/overview/tvy2F5tS3JRM7DfcHwz5fK#request-content">SEEN API</a>.</td>
    </tr>
    <tr>
      <td><strong>Anfrage-Header</strong></td>
      <td>Verwenden Sie die folgenden Informationen, um Ihre Anfrage-Header auszufüllen:<br><strong>Autorisierung</strong>: <code>Token {token}</code><br>- <strong>Content-Typ:</strong> <code>application/json</code><br><br>Sie erhalten Ihren Authentifizierungs-Token von SEEN.</td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Sie können den Webhook jetzt mit einem Nutzer:innen testen, indem Sie auf den Tab **Test** wechseln.

Wenn alles wie gewünscht funktioniert, gehen Sie zu Braze und setzen Sie die Rate, mit der die Kampagne Nachrichten versendet, auf 10 **Nachrichten pro Minute**. Auf diese Weise überschreiten Sie nicht das Rate-Limits des SEEN von 1.000 Anrufen pro Stunde.

### Schritt 2: Datentransformation erstellen

1. Erstellen Sie neue [angepasste Attribut-Felder]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) für `landing_page_url` und `email_thumbnail_url`. Dies sind die beiden Attribute, die wir in diesem Beispiel verwenden werden.
2. Öffnen Sie [Datentransformation]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation/#prerequisites) unter **Dateneinstellungen** und wählen Sie **Transformation erstellen**.
3. Geben Sie Ihrer Transformation einen Namen, wählen Sie **Neu beginnen** und setzen Sie das **Ziel** auf **POST: Nutzer:innen tracken**.
4. Wählen Sie **Ihre Webhook URL mit SEEN teilen**.
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
Wenn Sie andere Daten einbeziehen möchten, müssen Sie diese ebenfalls angeben. Denken Sie daran, auch mit SEEN zu sprechen, damit die Callback-Nutzdaten alle benötigten Felder enthalten.
{% endalert %}

{: start="6"}
6\. Senden Sie eine Test-Nutzlast an den angegebenen Endpunkt. Wenn Sie die in der [SEEN-Dokumentation](https://docs.seen.io/api-documentation/ntRoJJ3rXoHzFXhA94JiHB/callbacks/k9DEbcgkq3Vr2pxbHyPQbp) definierte Callback-Nutzlast verwenden möchten, können Sie diese selbst mit [Postman](https://www.postman.com/) oder einem anderen ähnlichen Dienst versenden:

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
