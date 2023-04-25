---
nav_title: Test
article_title: Test de notification Push pour iOS
platform: iOS
page_order: 29
description: "Cet article couvre les tests de la ligne de commande push pour vos notifications push iOS."
channel:
  - Notification push

---

# Tester {#push-testing}

Si vous souhaitez tester des notifications push et in-app à l’aide de la ligne de commande, vous pouvez envoyer une seule notification par le terminal via cURL et l’[API d’envoi de messages][29]. Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test :

- `YOUR_API_KEY` : disponible sur la page **Developer Console**
- `YOUR_EXTERNAL_USER_ID` : disponible sur la page **User Profile Search (Recherche de profil utilisateur)**. Voir [attribution d’ID utilisateur][32] pour plus d’informations.
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {{YOUR_API_KEY}}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```
L’exemple précédent concerne les clients sur l’instance `US-01`. Si vous n’êtes pas dans cette instance, consultez notre [Documentation API][66] pour voir quel endpoint doit effectuer les requêtes.

[29]: {{site.baseurl}}/api/endpoints/messaging/
[32]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#assigning-a-user-id
[66]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
