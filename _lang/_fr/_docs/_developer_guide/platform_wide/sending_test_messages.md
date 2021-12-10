---
nav_title: Envoi de messages de test
article_title: Envoi de messages de test
page_order: 3
description: "Cet article de référence couvre l'envoi de messages de test pour différents canaux."
---

# Envoi de messages de test

Avant d'envoyer une campagne de messagerie à vos utilisateurs, vous voudrez peut-être le tester pour vous assurer qu'il a l'air correct et qu'il fonctionne de la manière prévue. Créer et envoyer des messages de test pour sélectionner des appareils ou des membres de votre équipe est très simple en utilisant les outils du tableau de bord.

## Création d'un segment de test désigné <a class="margin-fix" name="test-segment"></a>

Une fois que vous avez configuré un segment de test, vous pouvez l'utiliser pour tester __n'importe quel__ de nos canaux de messagerie. Le processus est très simple et s'il est correctement configuré, il ne faudra le faire qu'une seule fois.

Naviguez vers la page "Segments" dans le tableau de bord et créez un nouveau segment. Dans le menu déroulant "Ajouter un filtre", vous trouverez nos filtres de test en bas de la liste.

!\[Filtres de tests\]\[1\]

Nos filtres de test vous permettent de sélectionner des utilisateurs avec des adresses e-mail spécifiques ou des [identifiants d'utilisateurs externes][2].

!\[Options de filtre de test\]\[3\]

Ces filtres ont trois options :

  1) __"Equals"__ - Cela va chercher une correspondance exacte de l'e-mail ou de l'identifiant utilisateur que vous fournissez. Utilisez ceci si vous voulez seulement envoyer les campagnes de test à des appareils associés à un seul e-mail ou identifiant d'utilisateur.

  2) __"N'est pas égal"__ - Utilisez ceci si vous voulez exclure un e-mail ou un identifiant utilisateur particulier des campagnes de test.

  3) __"Correspondance"__ - Ceci trouvera les utilisateurs qui ont des adresses e-mail ou des identifiants d'utilisateur qui correspondent à une partie du terme de recherche que vous fournissez. Vous pouvez l'utiliser pour trouver uniquement les utilisateurs qui ont une adresse "@yourcompany.com", vous permettant d'envoyer des messages à tous les membres de votre équipe.

Ces filtres peuvent également être utilisés en conjonction entre eux pour affiner votre liste d'utilisateurs de test. Par exemple, le segment de test pourrait inclure un filtre d'adresse électronique qui "correspondante" "@braze.com" et un autre filtre qui "ne correspond pas" "sales@braze.com". Vous pouvez également sélectionner plusieurs e-mails spécifiques en utilisant l'option "matches" et en séparant les adresses e-mail avec un caractère <code>|</code> (e. . "matches" "email1@braze.com &#124; email2@braze.com").

Après avoir ajouté les filtres de test à votre segment de test, vous pouvez vérifier que vous avez sélectionné seulement les utilisateurs que vous aviez voulu en cliquant sur "Aperçu" en haut de l'éditeur de segment, ou en exportant les données utilisateur de ce segment en CSV en cliquant sur l'icône d'engrenage dans le coin droit de l'éditeur et en sélectionnant "CSV Exporter toutes les données utilisateurs" dans le menu déroulant.

!\[Verify Test Segment\]\[4\]

> Exporter les données utilisateur du segment vers CSV vous donnera l'image la plus précise de qui tombe sous ce segment. L'onglet "Aperçu" n'est qu'un exemple d'utilisateurs dans le segment - [voir plus de détails à ce sujet dans notre FAQ][9] - et peut donc ne pas avoir sélectionné tous les membres prévus.

Une fois que vous avez confirmé que vous ne visez que les utilisateurs que vous voulez recevoir le message de test. vous pouvez soit sélectionner ce segment dans une campagne existante que vous voulez tester ou cliquer sur **Démarrer la campagne** dans le menu du segment.

## Envoi d'une notification test push ou de messages dans l'application <a class="margin-fix" name="push-inapp-test"></a>

Pour envoyer des notifications de test push et/ou des messages dans l'application, vous devez cibler votre segment de test précédemment créé. Commencez par créer votre campagne et suivez les étapes habituelles. Lorsque vous atteignez l'étape **Utilisateurs cibles** , sélectionnez votre segment de test comme indiqué ci-dessous.

!\[Segment de test\]\[11\]

Terminez la confirmation de votre campagne et lancez-la pour tester vos notifications push et vos messages dans l'application.

> Assurez-vous de cocher la case intitulée « Autoriser les utilisateurs à redevenir éligibles pour recevoir une campagne » dans la section __Planifier__ de l'assistant de campagne si vous avez l'intention d'utiliser une seule campagne pour vous envoyer un message de test plus d'une fois.

> Si vous ne testez que des messages électroniques, vous n'avez pas à configurer un segment de test. Dans la première étape de l'assistant de campagne où vous composez le message électronique de votre campagne. il y a un bouton "Envoyer le Test" en bas à gauche.

## Envoi d'un message de test

!\[Envoyer le bouton de test\]\[5\]

En cliquant sur ce bouton, une fenêtre apparaît où vous pouvez entrer l'adresse e-mail à laquelle vous souhaitez que l'e-mail de test soit envoyé. Cliquez sur "Envoyer le Test" et votre e-mail de test sera envoyé sous peu.

## Test de push via cURL

Alternativement, si vous souhaitez tester les notifications push via la ligne de commande, vous pouvez suivre les exemples suivants pour chaque plateforme.

### Tester le push avec les applications iOS via cURL

Vous pouvez envoyer une seule notification via le terminal via CURL et la [Messaging API][13]. Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test:

- `YOUR_API_KEY` - disponible sur la page [Console Développeur][14]
- `YOUR_EXTERNAL_USER_ID` - disponible sur la [Page de recherche du profil utilisateur][15]
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)


> Les exemples ci-dessous démontrent les points de terminaison API appropriés pour les clients sur l'instance `US-01`. Si vous n'êtes pas sur cette instance, veuillez vous référer à notre [documentation API][66] pour voir à quel point de terminaison vous devez faire des demandes.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {{YOUR_API_KEY}}" -d "{\"external_user_ids\":[\"YOUR_EXTERNAL_USER_ID\"],\"messages\":{\"apple_push\":{\"alert\":\"Test push\",\"extra\":{\"YOUR_KEY1\":\"YOUR_VALUE1\"}}}}" https://rest.iad-01.braze.com/messages/send
```

### Tester le push avec les applications Android via cURL

Vous pouvez envoyer une seule notification via le terminal via cURL et la [Messaging API][13]. Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test:

- `YOUR_API_KEY` - disponible sur la page [Console Développeur][14]
- `YOUR_EXTERNAL_USER_ID` - disponible sur la [Page de recherche du profil utilisateur][15]
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

> Les exemples ci-dessous démontrent les points de terminaison API appropriés pour les clients sur l'instance `US-01`. Si vous n'êtes pas sur cette instance, veuillez vous référer à notre [documentation API][66] pour voir à quel point de terminaison vous devez faire des demandes.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {{YOUR_API_KEY}}" -d "{\"external_user_ids\":[\"YOUR_EXTERNAL_USER_ID\"],\"messages\":{\"android_push\":{\"title\":\"Test push title\",\"alert\":\"Test push\",\"extra\":{\"YOUR_KEY1\":\"YOUR_VALUE1\"}}" https://rest.iad-01.braze.com/messages/send
```

### Tester le push avec les applications Kindle via cURL

Vous pouvez envoyer une seule notification via le terminal via cURL et la [Messaging API][13]. Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test:

- `YOUR_API_KEY` - disponible sur la page [Console Développeur][14]
- `YOUR_EXTERNAL_USER_ID` - disponible sur la [Page de recherche du profil utilisateur][15]
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {{YOUR_API_KEY}}" -d "{\"external_user_ids\":[\"YOUR_EXTERNAL_USER_ID\"],\"messages\":{\"kindle_push\":{\"title\":\"Test push title\",\"alert\":\"Test push\",\"extra\":{\"YOUR_KEY1\":\"YOUR_VALUE1\"}}" https://rest.iad-01.braze.com/messages/send
```

### Tester la push avec les applications Windows Universal via cURL

Vous pouvez envoyer une seule notification via le terminal via cURL et la [Messaging API][13]. Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test:

- `YOUR_API_KEY` - disponible sur la page [Console Développeur][14]
- `YOUR_EXTERNAL_USER_ID` - disponible sur la [Page de recherche du profil utilisateur][15]
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

> Les exemples ci-dessous démontrent les points de terminaison API appropriés pour les clients sur l'instance `US-01`. Si vous n'êtes pas sur cette instance, veuillez vous référer à notre [documentation API][66] pour voir à quel point de terminaison vous devez faire des demandes.

```bash
curl -X POST -H "Content-Type: application/json" -H "Autorisation: Bearer {{YOUR_API_KEY}}" -d "{\"external_user_ids\":[\"YOUR_EXTERNAL_USER_ID\"],\"messages\":{\"windows_push\":{\"push_type\":\"toast_text_01\",\"toast_text1\":\"test_title\"}}}" https://rest.iad-01.braze.com/messages/send
```

### Tester les applications de Push avec Windows Phone via cURL

Vous pouvez envoyer une seule notification via le terminal via cURL et la [Messaging API][13]. Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test:

- `YOUR_API_KEY` - disponible sur la page [Console Développeur][14]
- `YOUR_EXTERNAL_USER_ID` - disponible sur la [Page de recherche du profil utilisateur][15]
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

> Les exemples ci-dessous démontrent les points de terminaison API appropriés pour les clients sur l'instance `US-01`. Si vous n'êtes pas sur cette instance, veuillez vous référer à notre [documentation API][66] pour voir à quel point de terminaison vous devez faire des demandes.

```bash
curl -X POST -H "Content-Type: application/json" -H "Autorisation: Bearer {{YOUR_API_KEY}}" -d "{\"external_user_ids\":[\"YOUR_EXTERNAL_USER_ID\"],\"messages\":{\"windows_push\":{\"push_type\":\"toast\",\"toast_title\":\"test_title\",\"toast_content\":\"message_goes_here\",\"toast_navigation_uri\":\"uri_goes_here\"}}}" https://rest.iad-01.braze.com/messages/send
```
[1]: {% image_buster /assets/img_archive/testmessages1.png %} [3]: {% image_buster /assets/img_archive/testmessages2.png %} [4]: {% image_buster /assets/img_archive/testmessages3. ng %} [5]: {% image_buster /assets/img_archive/testmessages45.png %} [11]: {% image_buster /assets/img_archive/test_segment.png %}

[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#setting-user-ids
[9]: {{site.baseurl}}/developer_guide/platform_wide/platform_features/#user-segmentation
[13]: {{site.baseurl}}/api/endpoints/messaging/
[14]: https://dashboard-01.braze.com/app_settings/api_settings/
[15]: https://dashboard-01.braze.com/users/user_search/user-search/
[66]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
