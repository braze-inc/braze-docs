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

- `YOUR_API_KEY` : disponible sur la **Developer Console**
- `YOUR_EXTERNAL_USER_ID` : disponible sur la page **User Profile Search (Recherche de profil utilisateur)**
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {{YOUR_API_KEY}}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

Cet exemple utilise l’instance `US-01`. Si vous n’êtes pas sur cette instance, remplacez l’endpoint `US-01` avec [votre endpoint][66].

[13]: {{site.baseurl}}/api/endpoints/messaging/
[66]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/