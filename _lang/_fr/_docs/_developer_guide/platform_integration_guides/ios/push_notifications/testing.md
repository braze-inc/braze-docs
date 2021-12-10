---
nav_title: Tests en cours
article_title: Tests de notification push pour iOS
platform: iOS
page_order: 5.1
description: "Cet article couvre les tests de ligne de commande push pour vos notifications push iOS."
channel:
  - Pousser
---

# Tests en cours {#push-testing}

Si vous souhaitez tester les notifications dans l'application et push via la ligne de commande, vous pouvez envoyer une seule notification via le terminal via CURL et la [Messaging API][29]. Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test:

- `YOUR_API_KEY` — disponible sur la page [Console développeur][30]
- `YOUR_EXTERNAL_USER_ID` — disponible sur la [Page de recherche du profil utilisateur][31]. Voir la documentation sur [l'assignation des identifiants d'utilisateur][32]
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR_API_KEY" -d "{\"external_user_ids\":[\"YOUR_EXTERNAL_USER_ID\"],\"messages\":{\"apple_push\":{\"alert\":\"Test push\",\"extra\":{\"YOUR_KEY1\":\"YOUR_VALUE1\"}}}}" https://rest.iad-01.braze.com/messages/send
```
> Ce qui précède est un exemple pour les clients sur l'instance `US-01`. Si vous n'êtes pas sur cette instance, veuillez vous référer à notre [documentation API][66] pour voir à quel point de terminaison vous devez faire des demandes.

[29]: {{site.baseurl}}/api/endpoints/messaging/
[30]: https://dashboard-01.braze.com/app_settings/api_settings/
[31]: https://dashboard-01.braze.com/users/user_search/user-search/
[32]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#assigning-a-user-id
[66]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
