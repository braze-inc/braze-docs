---
nav_title: Réponses rapides
article_title: Réponses rapides
description: "Cet article de référence explique comment implémenter des communications bidirectionnelles dans Canvas à l’aide des réponses rapides WhatsApp."
page_type: partner
search_tag: Partenaire
page_order: 6
channel:
  - WhatsApp
---

# Réponses rapides

![L’écran du téléphone affichant un bouton d’appel à l’action qui renverra le texte du bouton cliqué.][1]{: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

> Les appels à l’action (CTA) des réponses rapides de WhatsApp sont un excellent moyen d’encourager l’engagement des utilisateurs avec vos communications WhatsApp. Braze peut traiter ces messages et configurer des actions en fonction de la sélection de l’utilisateur. De plus, ces CTA peuvent réduire les erreurs de va-et-vient en fournissant un bouton facilement cliquable, éliminant ainsi la nécessité pour vos utilisateurs de saisir des réponses.

Les boutons CTA des réponses rapides arrivent sous forme de messages entrants vers le système Braze, ce qui signifie que vous utiliserez l’étape d’action « Message WhatsApp entrant » lors de la création et du filtrage des réponses de vos utilisateurs. 

## Qu’est-ce qu’une réponse rapide ?

Les réponses rapides apparaissent sous forme d’options de bouton cliquable dans la conversation, mais agissent comme si un utilisateur avait répondu par du texte. Braze les traite ensuite comme des messages entrants et peut renvoyer des réponses définies en fonction du bouton cliqué.

![Un message WhatsApp affichant du texte et trois boutons d’appel à l’action.][3]{: style="max-width:50%;"}

## Configurer les expériences de réponse rapide dans Canvas

### Étape 1 : Créer des CTA

Tout d’abord, créez vos CTA de réponse rapide dans le [gestionnaire de modèles de messages WhatsApp](https://business.facebook.com/wa/manage/message-templates/) dans un modèle de message. 

![L’interface utilisateur du gestionnaire de modèles de messages WhatsApp montrant comment créer un bouton CTA, en fournissant le type de bouton (personnalisé) et le texte du bouton.][2]{: style="max-width:80%;"}

Une fois que votre modèle a été soumis et approuvé par WhatsApp, vous pouvez l’utiliser pour créer un Canvas dans Braze. 

{% alert tip %}
Vous pouvez créer le Canvas avant de recevoir l’approbation de votre modèle de message. 
{% endalert %}

### Étape 2 : Créer votre Canvas

Ensuite, créez un Canvas avec une étape de message qui inclut votre modèle créé. 

![][4]

Créez une étape d’action qui suit l’étape du message. Créez un groupe par option de réponse rapide dans cette étape d’action.

![Un Canvas où l’action d’évaluation est « envoyer un message entrant WhatsApp ».][5]

Pour chaque groupe d’options de réponse rapide, spécifiez le texte exact en tant que bouton que vous faites correspondre. Notez que les mots-clés doivent être en majuscules. 

![Une étape Canvas où l’action « envoyer un message entrant WhatsApp » est définie pour être envoyée lorsqu’un corps de message spécifique est reçu.][6]

Si vous souhaitez une réponse par défaut pour les utilisateurs qui répondent au message avec du texte au lieu de réponses rapides, créez un groupe supplémentaire sans corps de message correspondant.

Depuis ce point, continuez à construire le Canvas comme vous le feriez habituellement.

## Réponses

Vous désirerez probablement un message de réponse pour chaque réponse. Nous vous recommandons d’avoir une option « fourre-tout » pour les réponses qui ne sont pas dans les limites des réponses rapides (c.-à-d. pour les clients qui répondent par un message général plutôt qu’une invite prédéterminée). Par exemple, « Nous sommes désolés, nous n’avons pas reconnu votre réponse. Pour les problèmes d’assistance, veuillez envoyer un message à <support channel> ».

![Un Canvas créé montrant les réponses pour chaque bouton d’appel à l’action.][8]

Notez que vous pouvez utiliser toutes les actions suivantes proposées par Braze Canvas, telles que des messages en réponse, des mises à jour du profil utilisateur ou des webhooks Braze à Braze. 

[1]: {% image_buster /assets/img/whatsapp/whatsapp11.png %} 
[2]: {% image_buster /assets/img/whatsapp/whatsapp12.png %} 
[3]: {% image_buster /assets/img/whatsapp/whatsapp13.png %} 
[4]: {% image_buster /assets/img/whatsapp/whatsapp14.png %} 
[5]: {% image_buster /assets/img/whatsapp/whatsapp15.png %} 
[6]: {% image_buster /assets/img/whatsapp/whatsapp16.png %} 
[7]: {% image_buster /assets/img/whatsapp/whatsapp17.png %} 
[8]: {% image_buster /assets/img/whatsapp/whatsapp18.png %} 