---
nav_title: Tests en cours
article_title: Test de FireOS
platform: Pare-feu
page_order: 1
page_type: Référence
description: "Cette page fournit des informations sur le test des messages dans l'application et la notification via la ligne de commande."
channel:
  - Pousser
---

# Tests depuis la ligne de commande

Si vous souhaitez tester les notifications dans l'application et push via la ligne de commande, vous pouvez envoyer une seule notification via le terminal via cURL et la [Messaging API][13]. Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test:

- `YOUR_API_KEY` - disponible sur la page [Console Développeur][14]
- `YOUR_EXTERNAL_USER_ID` - disponible sur la [Page de recherche du profil utilisateur][15]
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_API_KEY" -d "{\"external_user_ids\":[\"YOUR_EXTERNAL_USER_ID\"],\"messages\":{\"kindle_push\":{\"title\":\"Test push title\",\"alert\":\"Test push\",\"extra\":{\"YOUR_KEY1\":\"YOUR_VALUE1\"}}}}" https://rest.iad-01.braze.com/messages/send
```
> Ce qui précède est un exemple pour les clients sur l'instance `US-01`. Si vous n'êtes pas sur cette instance, veuillez vous référer à notre [documentation API][66] pour voir à quel point de terminaison vous devez faire des demandes.

[13]: {{site.baseurl}}/api/endpoints/messaging/
[14]: https://dashboard-01.braze.com/app_settings/api_settings/
[15]: https://dashboard-01.braze.com/users/user_search/user-search/
[66]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/