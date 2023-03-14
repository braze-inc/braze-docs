---
nav_title: Test
article_title: Tester pour FireOS
platform: FireOS
page_order: 19
page_type: reference
description: "Cette page fournit des informations sur la manière de tester des messages in-app FireOS et des notifications push à l’aide de la ligne de commande."
channel: 
- Notification push

---

# Tester depuis la ligne de commande

Si vous souhaitez tester des notifications push et in-app à l’aide de la ligne de commande, vous pouvez envoyer une seule notification par le terminal via cURL et l’[API d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test :

Champs obligatoires :
- `YOUR-API-KEY-HERE` : disponible sur la page **Developer Console** Assurez-vous que la clé est autorisée à envoyer des messages via l’endpoint de l’API REST `/messages/send`. 
- `EXTERNAL_USER_ID` : disponible sur la page **User Profile Search (Recherche de profil utilisateur)**.
- `REST_API_ENDPOINT_URL` : listé sur les [instances]({{site.baseurl}}/api/basics/#endpoints) Braze. Assurez-vous que l’utilisation de l’endpoint correspond à l’instance Braze sur laquelle se trouve votre groupe d’apps.

Champs facultatifs :
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

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

[13]: {{site.baseurl}}/api/endpoints/messaging/
[66]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/