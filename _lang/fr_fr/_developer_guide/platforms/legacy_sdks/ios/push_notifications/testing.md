---
nav_title: Test
article_title: Test de notification Push pour iOS
platform: iOS
page_order: 29
description: "Cet article de référence couvre les tests de la ligne de commande push pour vos notifications push iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Tester {#push-testing}

Si vous souhaitez tester des notifications push et in-app à l’aide de la ligne de commande, vous pouvez envoyer une seule notification par le terminal via cURL et [l’API d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging/). Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test :

Champs obligatoires :

- `YOUR-API-KEY-HERE` - disponible dans **Réglages** > **Clés API**. Assurez-vous que la clé est autorisée à envoyer des messages via l’endpoint de l’API REST `/messages/send`. 
- `EXTERNAL_USER_ID` - disponible sur la page **Recherche d'utilisateurs.** 
- `REST_API_ENDPOINT_URL` - répertoriés sur le site Braze [Instances]({{site.baseurl}}/api/basics/#endpoints. Assurez-vous que l'utilisation de l'endpoint correspond à l'instance de Braze sur laquelle se trouve votre espace de travail.

Champs facultatifs :
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR-API-KEY-HERE" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://{REST_API_ENDPOINT_URL}/messages/send 
```
