---
nav_title: Envoyer des messages de test
article_title: Envoyer des messages de test
page_order: 6
description: "Cet article de référence couvre les messages de test pour différents canaux."

---

# Envoyer des messages de test

> Avant d’envoyer une campagne de messagerie à vos utilisateurs, vous pouvez la tester pour vous assurer qu’elle semble correcte et fonctionne de la manière prévue. Créer et envoyer des messages de test pour sélectionner des appareils ou des membres de l’équipe est très facile à l’aide des outils du tableau de bord.

## Créer un segment d’essai spécifié <a class="margin-fix" name="test-segment"></a>

Une fois que vous avez créé un segment d'essai, vous pouvez l'utiliser pour tester **n'importe lequel** de nos canaux de communication. S'il est configuré correctement, le processus ne devra être effectué qu'une seule fois.

Pour mettre en place un segment d'essai, accédez à la page **Segments** du tableau de bord et créez un nouveau segment. Cliquez sur **Ajouter un** filtre pour choisir l'un des filtres de test qui se trouvent en bas du menu déroulant.

![Une campagne de test de Braze présentant les filtres disponibles à l'étape du ciblage.]({% image_buster /assets/img_archive/testmessages1.png %})

Deux de ces filtres de test vous permettent de sélectionner des utilisateurs avec des adresses e-mail spécifiques ou des [ID]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#setting-user-ids) externes.

![Un menu déroulant affichant plusieurs filtres répertoriés sous un titre intitulé Testing]({% image_buster /assets/img_archive/testmessages2.png %})

Les filtres de l’adresse de courriel et de l’ID utilisateurs ont tous deux trois options :

  1) "**Égaux"** \- Cette option permet de rechercher une correspondance exacte avec l'e-mail ou l'ID de l'utilisateur que vous avez fourni. Utilisez cette option si vous souhaitez envoyer les campagnes de test uniquement aux appareils associés à un seul e-mail ou ID utilisateur.

  2) **"N'est pas égal"** \- Utilisez cette option si vous souhaitez exclure un e-mail ou un ID utilisateur particulier des campagnes test.

  3) "**Correspondances"** \- Cette option permet de trouver les utilisateurs dont l'adresse e-mail ou l'ID correspond à une partie du terme de recherche que vous avez fourni. Vous pouvez utiliser cette fonction pour trouver uniquement les utilisateurs qui ont une adresse "@yourcompany.com", ce qui vous permet d'envoyer des messages à tous les membres de votre équipe.

Vous pouvez sélectionner plusieurs e-mails spécifiques en utilisant l'option "correspond" et en séparant les adresses e-mail par le caractère | (par exemple, "correspond" "email1@braze.com | email2@braze.com").

Ces filtres peuvent également être utilisés conjointement pour limiter votre liste d’utilisateurs de test. Par exemple, le segment d'essai peut inclure un filtre d'adresse e-mail qui « correspond » à « @braze.com » et un autre filtre qui « n’est pas égal à » « sales@braze.com ». 

Après avoir ajouté les filtres de test à votre segment test, vous pouvez vérifier que vous n'avez sélectionné que les utilisateurs voulus en cliquant sur **Aperçu** en haut de l'éditeur de segment ou en exportant les données utilisateur de ce segment au format CSV en cliquant sur l'icône d'engrenage dans le coin droit de l'éditeur et en sélectionnant **Exporter toutes les données utilisateur en CSV** dans le menu déroulant.

![Une section d'une campagne Braze intitulée Segment Details]({% image_buster /assets/img_archive/testmessages3.png %})

>  L’exportation des données utilisateur du segment en CSV vous donnera l’image la plus précise de ceux qui dont partie de ce segment. L'onglet " **Aperçu"** ne représente qu'un échantillon des utilisateurs du segment et peut donc donner l'impression de ne pas avoir sélectionné tous les membres prévus.

## Envoi d’une notification push test ou de messages in-app <a class="margin-fix" name="push-inapp-test"></a>

Pour envoyer des notifications push test et/ou des messages in-app, vous devez cibler votre segment d’essai précédemment créé. Commencez par créer une campagne et suivez les étapes habituelles. Lorsque vous arrivez à l'étape **Utilisateurs ciblés**, sélectionnez votre segmentation test dans le menu déroulant.

![Campagne d'essai de Braze présentant les segments disponibles lors de l'étape de ciblage.]({% image_buster /assets/img_archive/test_segment.png %})

Terminez la confirmation de votre campagne et lancez-la pour tester votre notification push et vos messages dans l’application.

>  Veillez à sélectionner **Autoriser les utilisateurs à redevenir éligibles pour recevoir la campagne** dans la partie **Planification** du compositeur de la campagne si vous avez l'intention d'utiliser une seule campagne pour vous envoyer un message test plus d'une fois.

## Envoi d’un message e-mail test

Si vous ne testez que des messages e-mails, vous n’avez pas à configurer un segment d'essai. Dans la première étape du composeur de campagne où vous rédigez le message e-mail de votre campagne, cliquez sur **Envoyer un test** et saisissez l'adresse e-mail à laquelle vous souhaitez envoyer un e-mail de test. 

![Une campagne de Braze avec l'onglet Test Send sélectionné]({% image_buster /assets/img_archive/testmessages45.png %})

{% alert tip %}
Vous pouvez également activer ou désactiver l'ajout de [TEST (ou SEED)]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#append-email-subject-lines) à vos envois de messages.
{% endalert %}

## Tester depuis la ligne de commande

Sinon, si vous souhaitez tester les notifications push via la ligne de commande, vous pouvez suivre les exemples suivants pour chaque plateforme.

### Test de notification push avec applications iOS via cURL

Vous pouvez envoyer une notification unique par l'intermédiaire du terminal via CURL et l'[API d'envoi de messages.]({{site.baseurl}}/api/endpoints/messaging/) Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test :

- `YOUR_API_KEY` - disponible dans **Réglages** > **Clés API**
- `YOUR_EXTERNAL_USER_ID` - disponible sur la page **Recherche d'utilisateurs** 
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), ces pages se trouvent à un emplacement/localisation différent : <br>\- Les **clés API** sont situées dans la **console de développement** > **Paramètres API**. <br>\- L’option **Rechercher des utilisateurs** est située dans **Utilisateurs** > **Recherche d'utilisateurs**
{% endalert %}

>  Les exemples suivants illustrent les endpoints API appropriés pour les clients de l’`US-01`instance. Si vous n'êtes pas sur cette instance, reportez-vous à notre [documentation API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) pour savoir à quel endpoint adresser vos requêtes.

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

Vous pouvez envoyer une notification unique par le biais du terminal via cURL et l'[API d'envoi de messages.]({{site.baseurl}}/api/endpoints/messaging/) Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test :

- `YOUR_API_KEY` (Allez dans **Paramètres** > **Clés API**.)
- `YOUR_EXTERNAL_USER_ID` ( Recherchez un profil utilisateur sur la page **Recherche d'utilisateurs**).
- `YOUR_KEY1` (facultatif)
- `YOUR_VALUE1` (facultatif)

>  Les exemples suivants illustrent les endpoints API appropriés pour les clients de l’`US-01`instance. Si vous n'êtes pas sur cette instance, reportez-vous à notre [documentation API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) pour savoir à quel endpoint adresser vos requêtes.

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

Vous pouvez envoyer une notification unique par le biais du terminal via cURL et l'[API d'envoi de messages.]({{site.baseurl}}/api/endpoints/messaging/) Vous devrez remplacer les champs suivants par les valeurs correctes pour votre cas de test :

- `YOUR_API_KEY` - disponible sur la page de la **console de développement** 
- `YOUR_EXTERNAL_USER_ID` - disponible sur la page **Recherche d'utilisateurs** 
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

- Si vous affichez le [centre de préférences de]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-groups) Braze à partir des **messages de test**, le bouton d'envoi sera grisé.
- L’en-tête de désabonnement de la liste n’est pas incluse dans les courriels envoyés par la fonctionnalité de message test
- Pour les messages dans l’appli et les cartes de contenu, l’utilisateur cible doit avoir un jeton de notification push pour l’appareil cible

