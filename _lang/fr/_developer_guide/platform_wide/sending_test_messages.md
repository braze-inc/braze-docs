---
nav_title: Envoi des messages de test
article_title: Envoi des messages de test
page_order: 3
description: "Cet article de référence couvre les messages de test pour différents canaux."

---

# Envoyer des messages de test

Avant d’envoyer une campagne de messagerie à vos utilisateurs, vous pouvez la tester pour vous assurer qu’elle semble correcte et fonctionne de la manière prévue. Créer et envoyer des messages de test pour sélectionner des appareils ou des membres de l’équipe est très facile à l’aide des outils du tableau de bord.

## Créer un segment d’essai spécifié <a class="margin-fix" name="test-segment"></a>

Une fois que vous avez configuré un segment d’essai, vous pouvez l’utiliser pour tester **n’importe lequel** de nos canaux de messagerie. Le processus est très simple et s’il est configuré correctement, il n’aura besoin d’être fait qu’une seule fois.

Accédez à la page « Segments » du tableau de bord et créez un nouveau segment. Dans le menu déroulant sous « Add Filter » (Ajouter un filtre) se trouvent les filtres de test au bas de la liste.

![Une campagne de test Braze affichant les filtres disponibles dans l’étape de ciblage.][1]

Nos filtres de test permettent de sélectionner des utilisateurs avec des adresses e-mail spécifiques ou des [ID utilisateur][2] externes.

![][3]

Ces filtres ont trois options :

  1) **« Égal à"** - Recherche l’adresse e-mail exacte ou l’ID utilisateur que vous fournissez. Utilisez cette option si vous souhaitez envoyer les campagnes de test uniquement aux appareils associés à un seul e-mail ou ID utilisateur.

  2) **« N’est pas égal à"** - Utilisez cette option si vous souhaitez exclure un e-mail ou un ID utilisateur particulier des campagnes de test.

  3) **« Correspond"** - Trouve les utilisateurs qui ont des adresses e-mail ou des ID utilisateur qui correspondent à une partie du terme que vous fournissez. Vous pouvez l’utiliser pour trouver uniquement les utilisateurs disposant d’une adresse « @votresociété.com », ce qui vous permet d’envoyer des messages à tous les membres de votre équipe.

Ces filtres peuvent également être utilisés conjointement pour limiter votre liste d’utilisateurs de test. Par exemple, le segment d’essai peut inclure un filtre d’adresse e-mail qui « correspond à » « @braze.com » et un autre filtre qui  « n’est pas égal à » « sales@braze.com ». Vous pouvez également sélectionner plusieurs e-mails spécifiques en utilisant l’option « correspondances » et en séparant les adresses e-mail avec un caractère &#124; (p. ex., « correspondances » « e-mail1@braze.com &#124; email2@braze.com »).

Après avoir ajouté les filtres de test à votre segment d’essai, vérifiez que vous n’avez sélectionné que les utilisateurs désirés en cliquant sur Preview (Aperçu) en haut de l’éditeur de segments ou en exportant les données utilisateur de ce segment en CSV en cliquant sur l’icône d’engrenage dans le coin droit de l’éditeur et en sélectionnant « CSV Exporter toutes les données utilisateur » dans le menu déroulant.

![][4]

>  L’exportation des données utilisateur du segment en CSV vous donnera l’image la plus précise de ceux qui font partie de ce segment. L’onglet [Preview][9] (Aperçu) n’affiche qu’un échantillon des utilisateurs dans le segment - voir la FAQ pour davantage de précisions - et peut donc sembler ne pas avoir sélectionné tous les membres prévus.

Une fois que vous avez confirmé que vous ne ciblez que les utilisateurs qui doivent recevoir le message de test, vous pouvez soit sélectionner ce segment dans une campagne existante que vous souhaitez tester, soit cliquer sur **Start Campaign** (Démarrer la campagne) dans le menu du segment.

## Envoi d’une notification push test ou de messages in-app <a class="margin-fix" name="push-inapp-test"></a>

Pour envoyer des notifications push test et/ou des messages dans l’application, vous devez cibler votre segment d’essai précédemment créé. Commencez par créer une campagne et suivez les étapes habituelles. Lorsque vous atteignez l’étape **Target Users** (Utilisateurs cibles), sélectionnez votre segment d’essai comme illustré sur l’image suivante.

![Une campagne de test Braze affichant les segments disponibles dans l’étape de ciblage.][11]

Terminez la confirmation de votre campagne et lancez-la pour tester votre notification push et vos messages dans l’application.

>  Assurez-vous de sélectionner **Allow users to become re-eligible to receive campaign** (Autoriser les utilisateurs à devenir rééligibles pour recevoir la campagne) dans la partie **Schedule** (Planification) de l’assistant de campagne si vous avez l’intention d’utiliser une campagne unique pour vous envoyer un message de test à plusieurs reprises.

>  Si vous ne testez que des messages électroniques, vous n’avez pas à configurer un segment de test. Dans la première étape de l’assistant de campagne où vous composez l’e-mail de votre campagne, cliquez sur **Send Test** (Envoyer un test) pour envoyer le projet de message électronique à votre boîte de réception.

## Envoi d’un message e-mail test

![][5]

Cliquez sur ce bouton pour afficher une fenêtre où vous pouvez saisir l’adresse e-mail que vous souhaitez envoyer par e-mail. Cliquez sur **Send Test** (Envoyer un test) et votre e-mail de test sera envoyé sous peu.

## Tester depuis la ligne de commande

Sinon, si vous souhaitez tester des notifications push via la ligne de commande, vous pouvez suivre les exemples suivants pour chaque plateforme.

### Test de notification push avec applications iOS via cURL

Vous pouvez envoyer une seule notification par le terminal via CURL et l’[API de messagerie][13]. Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test :

- `YOUR_API_KEY` - disponible sur la page [Developer Console][14]
- `YOUR_EXTERNAL_USER_ID` - disponible sur la page [User Profile Search][15] (Recherche de profil utilisateur)
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)


>  Les exemples suivants illustrent les endpoints API appropriés pour les clients de l’`US-01`instance. Si vous n’êtes pas dans cette instance, consultez notre [Documentation API][66] pour voir quel endpoint doit effectuer les requêtes.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {{YOUR_API_KEY}}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert": "Test push",
      "extra": { 
        "YOUR_KEY1" :"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

### Test de notification push avec applications Android via cURL

Vous pouvez envoyer une seule notification par le terminal via cURL et l’[API de messagerie][13]. Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test :

- `YOUR_API_KEY` - disponible sur la page [Developer Console][14]
- `YOUR_EXTERNAL_USER_ID` - disponible sur la page [User Profile Search][15] (Recherche de profil utilisateur)
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

>  Les exemples suivants illustrent les endpoints API appropriés pour les clients de l’`US-01`instance. Si vous n’êtes pas dans cette instance, consultez notre [Documentation API][66] pour voir quel endpoint doit effectuer les requêtes.

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

### Test de notification push avec applications Kindle via cURL

Vous pouvez envoyer une seule notification par le terminal via cURL et l’[API de messagerie][13]. Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test :

- `YOUR_API_KEY` - disponible sur la page [Developer Console][14]
- `YOUR_EXTERNAL_USER_ID` - disponible sur la page [User Profile Search][15] (Recherche de profil utilisateur)
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {{YOUR_API_KEY}}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "kindle_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra":{
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

### Test de notification push avec les applications Windows Universal via cURL

Vous pouvez envoyer une seule notification par le terminal via cURL et l’[API de messagerie][13]. Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test :

- `YOUR_API_KEY` - disponible sur la page [Developer Console][14]
- `YOUR_EXTERNAL_USER_ID` - disponible sur la page [User Profile Search][15] (Recherche de profil utilisateur)

>  Les exemples suivants illustrent les endpoints API appropriés pour les clients de l’`US-01`instance. Si vous n’êtes pas dans cette instance, consultez notre [Documentation API][66] pour voir quel endpoint doit effectuer les requêtes.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {{YOUR_API_KEY}}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "windows_push": {
      "push_type":"toast_text_01",
      "toast_text1":"test_title"
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

### Test de notification push avec les applications de téléphone Windows via cURL

Vous pouvez envoyer une seule notification par le terminal via cURL et l’[API de messagerie][13]. Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test :

- `YOUR_API_KEY` - disponible sur la page [Developer Console][14]
- `YOUR_EXTERNAL_USER_ID` - disponible sur la page [User Profile Search][15] (Recherche de profil utilisateur)

>  Les exemples suivants illustrent les endpoints API appropriés pour les clients de l’`US-01`instance. Si vous n’êtes pas dans cette instance, consultez notre [Documentation API][66] pour voir quel endpoint doit effectuer les requêtes.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {{YOUR_API_KEY}}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "windows_push": {
      "push_type":"toast",
      "toast_title":"test_title",
      "toast_content":"message_goes_here",
      "toast_navigation_uri":"uri_goes_here"
    }
  }
}' https://rest.iad-01.braze.com/messages/send
```

[1]: {% image_buster /assets/img_archive/testmessages1.png %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#setting-user-ids
[3]: {% image_buster /assets/img_archive/testmessages2.png %}
[4]: {% image_buster /assets/img_archive/testmessages3.png %}
[5]: {% image_buster /assets/img_archive/testmessages45.png %}
[9]: {{site.baseurl}}/developer_guide/platform_wide/platform_features/#user-segmentation
[11]: {% image_buster /assets/img_archive/test_segment.png %}
[13]: {{site.baseurl}}/api/endpoints/messaging/
[14]: https://dashboard-01.braze.com/app_settings/api_settings/
[15]: https://dashboard-01.braze.com/users/user_search/user-search/
[66]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
