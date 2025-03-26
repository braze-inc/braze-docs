---
nav_title: Testen
article_title: Testen für FireOS
platform: FireOS
page_order: 19
page_type: reference
description: "Dieser Referenzartikel enthält Informationen zum Testen von FireOS In-App-Nachrichten und Push-Benachrichtigungen über die Kommandozeile."
channel: 
- push

---

# Testen

> Dieser Referenzartikel enthält Informationen zum Testen von FireOS In-App-Nachrichten und Push-Benachrichtigungen über die Kommandozeile.

Wenn Sie In-App- und Push-Benachrichtigungen über die Befehlszeile testen möchten, können Sie über cURL und die [Nachrichten-API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) eine einzelne Benachrichtigung über das Terminal senden. Sie müssen die folgenden Felder durch die richtigen Werte für Ihren Testfall ersetzen:

Erforderliche Felder:

- `YOUR-API-KEY-HERE` - verfügbar unter **Einstellungen** > **API-Schlüssel**. Stellen Sie sicher, dass der Schlüssel berechtigt ist, Nachrichten über den REST API-Endpunkt `/messages/send` zu versenden. 
- `EXTERNAL_USER_ID` - verfügbar auf der Seite **Benutzer suchen**.
- `REST_API_ENDPOINT_URL` - in Braze [Instanzen]({{site.baseurl}}/api/basics/#endpoints. Stellen Sie sicher, dass Sie den Endpunkt verwenden, der der Braze-Instanz entspricht, in der sich Ihr Workspace befindet.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, befinden sich diese Seiten an einer anderen Stelle: <br>- **API-Schlüssel** finden Sie unter **Entwicklerkonsole** > **API-Einstellungen** <br>- **Benutzer suchen** finden Sie unter **Benutzer** > **Benutzersuche**
{% endalert %}

Optionale Felder:
- `YOUR_KEY1` (optional)
- `YOUR_VALUE1` (optional)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR-API-KEY-HERE" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://{REST_API_ENDPOINT_URL}/messages/send 
```

