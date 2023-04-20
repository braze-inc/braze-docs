---
nav_title: Envoyer des messages de test
article_title: Envoyer des messages de test
page_order: 3
description: "Cet article de référence couvre les messages de test pour différents canaux."

---

# Envoyer des messages de test

> Avant d’envoyer une campagne de messagerie à vos utilisateurs, vous pouvez la tester pour vous assurer qu’elle semble correcte et fonctionne de la manière prévue. Créer et envoyer des messages de test pour sélectionner des appareils ou des membres de l’équipe est très facile à l’aide des outils du tableau de bord.

## Créer un segment d’essai spécifié <a class="margin-fix" name="test-segment"></a>

Une fois que vous avez configuré un segment d’essai, vous pouvez l’utiliser pour tester **n’importe lequel** de nos canaux de messagerie. Si le processus est configuré correctement, une seule fois suffira à le réaliser.

Pour configurer un segment d'essai, accédez à la page **Segments**  du tableau de bord et créez un nouveau segment. Cliquez sur **Add Filter** (Ajouter un filtre) pour choisir les filtres de test qui se trouvent vers le bas du menu déroulant.

![Une campagne de test Braze affichant les filtres disponibles dans l’étape de ciblage.][1]

Deux filtres de test de ce type vous permettent de sélectionner des utilisateurs avec des adresses e-mail spécifiques ou des [ID utilisateur][2] externes.

![Un menu déroulant présentant plusieurs filtres répertoriés sous un en-tête indiquant Essais][3]

Les filtres de l’adresse de courriel et de l’ID utilisateurs ont tous deux trois options :

  1) **« Égal à »** : Recherche l’adresse e-mail exacte ou l’ID utilisateur que vous fournissez. Utilisez cette option si vous souhaitez envoyer les campagnes de test uniquement aux appareils associés à un seul e-mail ou ID utilisateur.

  2) **« N’est pas égal à »** : Utilisez cette option si vous souhaitez exclure un e-mail ou un ID utilisateur particulier des campagnes de test.

  3) **« Correspond »** : Trouve les utilisateurs qui ont des adresses e-mail ou des ID utilisateur qui correspondent à une partie du terme que vous fournissez. Vous pouvez l’utiliser pour trouver uniquement les utilisateurs disposant d’une adresse « @votresociété.com », ce qui vous permet d’envoyer des messages à tous les membres de votre équipe.

Vous pouvez sélectionner plusieurs e-mails spécifiques en utilisant l’option « correspondances » et en séparant les adresses e-mail avec un caractère &#124; (p. ex., « correspondances » « e-mail1@braze.com &#124; email2@braze.com »).

Ces filtres peuvent également être utilisés conjointement pour limiter votre liste d’utilisateurs de test. Par exemple, le segment d’essai peut inclure un filtre d’adresse e-mail qui « correspond à » « @braze.com » et un autre filtre qui  « n’est pas égal à » « sales@braze.com ». 

Après avoir ajouté les filtres de test à votre segment d’essai, vérifiez que vous n’avez sélectionné que les utilisateurs désirés en cliquant sur **Preview** (Aperçu) en haut de l’éditeur de segments ou en exportant les données utilisateur de ce segment en CSV, en cliquant sur l’icône d’engrenage dans l’angle à droite de l’éditeur et en sélectionnant **CSV Export All User Data** (CSV Exporter toutes les données utilisateur) dans le menu déroulant.

![Une rubrique d’une campagne Braze intitulée Détails du segment][4]

>  L’exportation des données utilisateur du segment en CSV vous donnera l’image la plus précise de ceux qui dont partie de ce segment. L’onglet **Aperçu** n’affiche qu’un échantillon des utilisateurs dans le segment et peut donc sembler ne pas avoir sélectionné tous les membres prévus.

## Envoi d’une notification push test ou de messages in-app <a class="margin-fix" name="push-inapp-test"></a>

Pour envoyer des notifications push test et/ou des messages in-app, vous devez cibler votre segment d’essai précédemment créé. Commencez par créer une campagne et suivez les étapes habituelles. Lorsque vous atteignez l’étape **Utilisateurs cible**, sélectionnez votre segment d’essai dans le menu déroulant.

![Une campagne de test Braze affichant les segments disponibles dans l’étape de ciblage.][11]

Terminez la confirmation de votre campagne et lancez-la pour tester votre notification push et vos messages dans l’application.

>  Assurez-vous de sélectionner **Allow users to become re-eligible to receive campaign** (Autoriser les utilisateurs à devenir rééligibles pour recevoir la campagne) dans la partie **Schedule** (Planification) de l’assistant de campagne si vous avez l’intention d’utiliser une campagne unique pour vous envoyer un message de test à plusieurs reprises.

## Envoi d’un message e-mail test

Si vous ne testez que des messages e-mails, vous n’avez pas à configurer un segment d'essai. Dans la première étape de l’assistant de campagne où vous composez l’e-mail de votre campagne, cliquez sur **Send Test** (Envoyer un test) et saisir l’adresse de courriel à laquelle vous souhaitez envoyer le courriel test. 

![Une campagne Braze avec l’onglet Test Send (Envoyer un test) sélectionné][5]

{% alert tip %} 
Vous pouvez également activer ou désactiver le fait que [TEST (ou SEED)][14] soit ajouté à vos messages de test.
{% endalert %}


## Tester depuis la ligne de commande

Sinon, si vous souhaitez tester des notifications push via la ligne de commande, vous pouvez suivre les exemples suivants pour chaque plateforme.

### Test de notification push avec applications iOS via cURL

Vous pouvez envoyer une seule notification par le terminal via CURL et l’[API de messagerie][13]. Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test :

- `YOUR_API_KEY` - disponible sur la page **Developer Console**
- `YOUR_EXTERNAL_USER_ID` : disponible sur la page **User Search** (Recherche d’utilisateur)
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)


>  Les exemples suivants illustrent les endpoints API appropriés pour les clients de l’`US-01`instance. Si vous n’êtes pas dans cette instance, consultez notre [Documentation API][66] pour voir quel endpoint doit effectuer les requêtes.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
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

- `YOUR_API_KEY` - disponible sur la page **Developer Console**
- `YOUR_EXTERNAL_USER_ID` : disponible sur la page **User Search** (Recherche d’utilisateur)
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

>  Les exemples suivants illustrent les endpoints API appropriés pour les clients de l’`US-01`instance. Si vous n’êtes pas dans cette instance, consultez notre [Documentation API][66] pour voir quel endpoint doit effectuer les requêtes.

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
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

- `YOUR_API_KEY` - disponible sur la page **Developer Console**
- `YOUR_EXTERNAL_USER_ID` : disponible sur la page **User Search** (Recherche d’utilisateur)
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
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

## Limites des messages test

Dans quelques rares situations, les messages test ne sont pas dotés d’une parité complète de fonctionnalités lors du lancement d’une campagne ou de canvas à un ensemble d’utilisateurs réels. Dans ces situations, pour valider ce comportement, vous devez lancer la campagne ou le canvas à un ensemble limité d’utilisateurs.

- Consulter le [Preference center (Centre de préférence)][16] de Braze depuis **Test Messages (Messages test)** a pour effet de griser le bouton soumettre
- L’en-tête de désabonnement de la liste n’est pas incluse dans les courriels envoyés par la fonctionnalité de message test
- Pour les messages dans l’appli et les cartes de contenu, l’utilisateur cible doit avoir un jeton de notification push pour l’appareil cible

[1]: {% image_buster /assets/img_archive/testmessages1.png %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#setting-user-ids
[3]: {% image_buster /assets/img_archive/testmessages2.png %}
[4]: {% image_buster /assets/img_archive/testmessages3.png %}
[5]: {% image_buster /assets/img_archive/testmessages45.png %}
[9]: {{site.baseurl}}/developer_guide/platform_wide/platform_features/#user-segmentation
[11]: {% image_buster /assets/img_archive/test_segment.png %}
[13]: {{site.baseurl}}/api/endpoints/messaging/
[66]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
[16]: {{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups
[14]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings/#test-and-seed-subject-lines
