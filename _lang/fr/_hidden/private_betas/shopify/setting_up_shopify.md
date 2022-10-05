---
nav_title: Configuration de Shopify
article_title: "Configuration de Shopify"
description: "Cet article explique comment configurer Shopify, une société de commerce international, qui vous permet de connecter de manière transparente votre boutique Shopify à Braze pour faire passer certains webhooks Shopify dans Braze."
page_type: partner
search_tag: Partenaire
permalink: "/setting_up_shopify/"
hidden: true

---

# Configuration de Shopify

> [Shopify](https://www.shopify.com/) est une société leader dans le commerce mondial ; elle fournit des outils fiables pour démarrer, développer, commercialiser et gérer une entreprise de vente en détail, quelle que soit sa taille. Shopify améliore le commerce pour tous les utilisateurs avec une plateforme et des services conçus pour assurer la fiabilité tout en offrant une meilleure expérience d’achat pour les consommateurs où qu’ils soient. 

L’intégration de Shopify et de Braze permet aux marques de connecter leur boutique Shopify de manière transparente pour transmettre certains webhooks Shopify dans Braze. Exploitez les stratégies multicanaux de Braze et de Canvas pour recibler vos utilisateurs avec des messages sur les paniers abandonnés afin d’inciter les clients à terminer leur achat ou de recibler les utilisateurs en fonction de leurs achats précédents. 

## Conditions préalables

Tous les clients de Braze souhaitant utiliser l’intégration Shopify doivent signer le formulaire de commande Shopify de Braze. Contactez votre responsable de compte pour plus de détails.

Cette intégration crée des profils d’utilisateurs alias si nous ne sommes pas en mesure de faire correspondre les données Shopify avec l’e-mail ou le numéro de téléphone. Reportez-vous à la section suivante pour plus d’informations sur [le rapprochement des utilisateurs Shopify]({{site.baseurl}}/shopify_data/#user-reconciliation). Consultez vos équipes de développement au sujet des impacts en aval et de la nécessité de fusionner ces profils d’utilisateurs dans le cadre de votre cycle de vie des utilisateurs avant d’activer l’intégration. 

| Configuration requise | Description |
| ----------- | ----------- |
| Boutique Shopify | Vous devez avoir une boutique [Shopify](https://www.shopify.com) active.<br><br>Notez que, pour le moment, vous ne pouvez connecter qu’une boutique Shopify par groupe d’applications. |
| Segmentation de propriété d’événement activée | Pour vous assurer que vous pouvez segmenter les propriétés de vos événements Shopify, vous devez travailler avec votre gestionnaire du succès des clients ou avec [l’assistance de Braze]({{site.baseurl}}/braze_support/) pour confirmer que la segmentation des propriétés d’événements est activée pour votre tableau de bord. |
| Prise en charge des attributs personnalisés imbriqués | Celle-ci sera activée avec l’intégration à Shopify.<br><br>Vous aurez accès à cette fonctionnalité pour recevoir les attributs personnalisés d’abonnement au marketing Shopify. |
{: .reset-td-br-1 .reset-td-br-2}

## Qu’est-ce qui est pris en charge dans l’intégration ?

- Intégration du SDK Web de Braze via Shopify ScriptTag
- Données utilisateur synchronisées dans Braze
- Capacité à orchestrer les cas d’utilisateurs d’e-commerce à plusieurs canaux suivants :
   - Parcours d’achat de l’utilisateur
   - Panier abandonné et déconnexion des utilisateurs
   - Reciblage après achat
   - Messages transactionnels

## Intégration

Les types de cas d’utilisation de Shopify que vous prévoyez de soutenir détermineront le parcours d’intégration que vous allez configurer dans le processus d’onboarding du tableau de bord de Braze.

<style>
    table {
        table-layout: fixed;
        width: 100%;
    }
    table td {
    word-break: break-word;
    }
</style>

| Cas d’utilisation prévu | Méthode d’intégration |
| -------- | ------------------ |
| Reciblez les clients lorsqu’ils commencent leur parcours d’achat. Vous pouvez reciblez avec les événements d’e-commerce de type TOFU suivants :<br>   • Produit cliqué<br>   • Produit vu<br>   • Panier abandonné | SDK Web de Braze via Shopify ScriptTag |
| Prend en charge les paiements abandonnés, les achats et le ciblage post-achat :<br>   • Paiement abandonné<br>   • Commande créée<br>   • Événement d’achat Braze | Webhooks Shopify |
| Prise en charge de la messagerie marketing transactionnelle :<br>   • Commande payée<br>   • Exécution de la commande<br>   • Exécution partielle de la commande<br>   • Annulation de la commande<br>   • Remboursement de la commande | Webhooks Shopify |
|Suivi anonyme des utilisateurs | SDK Web de Braze via Shopify ScriptTag |
| Prise en charge des canaux :<br>   • Messagerie dans le navigateur | SDK Web de Braze via Shopify ScriptTag |

### Étape 1 : Localiser Shopify dans le tableau de bord
Dans Braze, accédez à **Technology Partners** puis recherchez **Shopify**. Sur la page partenaire Shopify, sélectionnez **Begin Setup** (Commencer la configuration) pour démarrer le processus d’intégration.

![Section Importation de données et installation du SDK Web de la page partenaire Shopify dans Braze.][2]{: style="max-width:80%;"}

### Étape 2 : Configurer Shopify
![][3]{: style="float:right;max-width:30%;margin-top:15px;"} 

Au cours du processus d’onboarding, vous devrez :
1. Associer votre nom de boutique Shopify
2. Sélectionner les événements Shopify
3. Activer un canal Braze
4. Installation de l’application Braze dans votre vitrine
<br><br>

### Étape 2a : Associer un nom de boutique Shopify

Lorsque vous cliquez sur **Begin Setup** (Commencer la configuration), il vous sera demandé d’indiquer votre **nom de boutique Shopify**. Assurez-vous de bien saisir le nom de votre boutique, et non le [domaine Shopify](https://help.shopify.com/en/manual/domains).

![][6]{: style="max-width:65%;"} 

#### Étape 2b : SDK Web

Dans l’étape suivante de l’assistant de configuration, vous recevrez des informations sur le SDK Web de Braze. Le SDK Web de Braze peut être intégré via Shopify ScriptTag pour déverrouiller les fonctionnalités suivantes :
- Intégration du SDK Web de Braze en un clic à votre boutique Shopify
- Suivi anonyme des utilisateurs
- Suivi clés en main pour les événements d’e-commerce de type TOFU :
  - Produit affiché
  - Produit cliqué
  - Panier abandonné
- Option pour activer la messagerie sur navigateur

Gardez à l’esprit que lorsque vous activez le SDK Web de Braze, il commencera à suivre les utilisateurs actifs mensuels, et les données utilisateur recueillies seront comptabilisées dans votre consommation de données.


![][4]{: style="max-width:65%;"} 

{% alert note %}
- Pour mieux comprendre l’intégration requise, consultez le guide [Intégration SDK Web via Shopify ScriptTag]({{site.baseurl}}/scripttag_web_sdk_integration/).
- Pour plus d’informations sur le SDK Web de Braze, consultez notre [présentation du SDK Web]({{site.baseurl}}/user_guide/onboarding_with_braze/web_sdk/).
{% endalert %}

### Étape 2c : Sélectionner les événements Shopify

Ensuite, vous pourrez sélectionner les événements Shopify que vous souhaitez intégrer à Braze.

Pour les événements marqués d’un astérisque (&#42;), vous devrez intégrer le SDK Web de Braze pour suivre ces événements.

![][7]{: style="max-width:65%;"} 

### Étape 2d : Messagerie sur navigateur (facultatif)

Une fois que vous avez sélectionné et confirmé les événements Shopify à obtenir, vous aurez la possibilité d’inclure des messages dans le navigateur dans le cadre de votre intégration. La messagerie sur navigateur permet aux marques de diffuser des contenus riches sur leur boutique Shopify, notamment pour mettre en avant des promotions et obtenir des abonnements par e-mail et/ou SMS. Pour en savoir plus, consultez la section [Messages dans l’application]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/#potential-use-cases).

![][5]{: style="max-width:65%;"} 

### Étape 2e : Installez l’application Braze dans votre vitrine

Après avoir sélectionné vos événements et canaux Shopify, vous pouvez confirmer vos paramètres d’intégration dans l’assistant de configuration. Une fois confirmé, sélectionnez **Aller sur Shopify** pour installer l’application Shopify de Braze. Après avoir sélectionné **Install App** (Installer l’application), vous serez redirigé vers Braze pour terminer l’installation de l’application et afficher vos paramètres d’intégration.

![][8]{: style="max-width:85%;"} 

## Résolution des problèmes

{% details Why is my Shopify app install still pending? %}
Votre installation peut être en attente pour l’une des raisons suivantes : 
  - Lorsque Braze configure vos webhooks Shopify
  - Lorsque Braze communique avec Shopify

Si l’installation de votre application reste en attente pendant 1 heure, Braze arrête l’installation et vous serez invité à réessayer l’opération.<br><br>
![]({% image_buster /assets/img/Shopify/shopify_integration8.png %}){: style="max-width:80%;"}
{% enddetails %}

{% details Why did my Shopify app install fail? %}
Votre installation a échoué pour l’une des raisons suivantes : 
  - Braze n’a pas pu joindre Shopify
  - Échec de traitement de la demande par Braze 
  - Votre jeton d’accès à Shopify n’est pas valide 
  - L’application Braze Shopify a été supprimée de votre page d’administration Shopify

Si cela se produit, vous pourrez sélectionner **Retry Setup** (Réessayer l’installation) et recommencer le processus d’installation.<br><br>
![]({% image_buster /assets/img/Shopify/shopify_integration16.png %}){: style="max-width:80%;"}
{% enddetails %}

{% details How do I uninstall the Braze application from my Shopify store? %}
Vous devrez aller sur votre page d’administration Shopify située sous **Apps** (Applications). Vous verrez alors une option pour supprimer l’application Braze<br><br>
![]({% image_buster /assets/img/Shopify/shopify_integration12.png %}){: style="max-width:80%;"}
{% enddetails %}

[2]: {% image_buster /assets/img/Shopify/shopify_integration2.png %} 
[3]: {% image_buster /assets/img/Shopify/scripttag1.png %} 
[4]: {% image_buster /assets/img/Shopify/scripttag2.png %} 
[5]: {% image_buster /assets/img/Shopify/scripttag3.png %} 
[6]: {% image_buster /assets/img/Shopify/scripttag4.png %} 
[7]: {% image_buster /assets/img/Shopify/scripttag5.png %} 
[8]: {% image_buster /assets/img/Shopify/scripttag.gif %} 