---
nav_title: Écrire aux utilisateurs
article_title: Écrire aux utilisateurs
description: "Cet article de référence explique comment Braze va gérer les messages des utilisateurs."
page_type: reference
channel:
  - WhatsApp
page_order: 5.1
alias: /user_guide/message_building_by_channel/whatsapp/quick_replies/

---

# Messages des utilisateurs

> WhatsApp est un canal de communication bidirectionnel. Non seulement votre marque peut envoyer des messages aux utilisateurs, mais ils peuvent également participer à des conversations en utilisant des campagnes modélisées et des Canvases. Il existe différents moyens d'y parvenir, notamment les réponses rapides WhatsApp et les mots déclencheurs. Les appels à l'action (CTAs) de réponse rapide sont un excellent moyen d'encourager l'engagement des utilisateurs avec vos messages WhatsApp.

## Déclencheurs basés sur l'action 

Les campagnes et les Canvas peuvent commencer, se ramifier et avoir des changements en cours de route à partir d'un message WhatsApp entrant (un utilisateur envoyant un message à votre WhatsApp), comme un mot déclencheur. 

Assurez-vous que votre mot déclencheur correspond à ce que vous attendez des utilisateurs.

**Choses à savoir :**
- Chaque lettre de votre mot déclencheur doit être en majuscule lorsqu'il est configuré. Braze n'exige pas que les mots déclencheurs entrants envoyés par les utilisateurs soient en majuscules. Par exemple, envoyer un message "jOin2023" déclenchera toujours le Canvas ou la campagne.
- Si aucun mot déclencheur n'est spécifié sur le déclencheur basé sur l'action du calendrier d'entrée, la campagne ou Canvas s'exécutera pour TOUS les messages WhatsApp entrants. Cela inclut les messages qui ont des phrases correspondantes dans les campagnes actives et les Canvases, auquel cas l'utilisateur recevra deux messages WhatsApp.

{% tabs %}
{% tab Campagne %}

![]({% image_buster /assets/img/whatsapp/whatsapp27.png %})

![]({% image_buster /assets/img/whatsapp/whatsapp26.png %})

{% endtab %}
{% tab Canvas %}

![]({% image_buster /assets/img/whatsapp/whatsapp25.png %})

![]({% image_buster /assets/img/whatsapp/whatsapp24.png %})
{% endtab %}
{% endtabs %}

## Réponses non reconnues

Nous vous recommandons d'inclure une option pour les réponses non reconnues sur les Canvases interactifs. Cela guide les utilisateurs à comprendre quels sont les invites disponibles et fixe les attentes pour le canal. La gestion des attentes peut être particulièrement utile si vous avez des canaux WhatsApp avec chat en direct avec un agent. 
- Dans l'étape d'action, après avoir créé les groupes d'action pour les phrases de filtre personnalisées, ajoutez un groupe d'action supplémentaire pour "Envoyer un message WhatsApp", mais **ne cochez pas Où se trouve le corps du message**. Cela capturera toutes les réponses utilisateur non reconnues, similaire à une clause "else". 
- Nous recommandons de suivre avec un message WhatsApp informant l'utilisateur que ce canal n'est pas surveillé et de les guider vers un canal de support si nécessaire. 

## Réponses rapides 

![L’écran du téléphone affichant un bouton d’appel à l’action qui renverra le texte du bouton cliqué.][11]{: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

Les réponses rapides apparaissent sous forme d’options de bouton cliquable dans la conversation, mais agissent comme si un utilisateur avait répondu par du texte. Braze traite ensuite ceux-ci comme des messages entrants et peut renvoyer des réponses prédéfinies en fonction du bouton cliqué. Utilisez l'étape "Action de message entrant WhatsApp" lors de la création et du filtrage des réponses de vos utilisateurs.

![Un message WhatsApp affichant du texte et trois boutons d'appel à l'action.][13]{: style="max-width:50%;"}

### Configurer les expériences de réponse rapide dans Canvas

#### Étape 1 : Créer des CTA

Tout d'abord, créez vos CTA de réponse rapide dans le [Gestionnaire de Modèles de Messages WhatsApp](https://business.facebook.com/wa/manage/message-templates/) au sein d'un modèle de message. 

![L’interface utilisateur du gestionnaire de modèles de messages WhatsApp montrant comment créer un bouton CTA, en fournissant le type de bouton (personnalisé) et le texte du bouton.][12]{: style="max-width:80%;"}

Une fois que votre modèle a été soumis et approuvé par WhatsApp, vous pouvez l’utiliser pour créer un Canvas dans Braze. 

{% alert tip %}
Vous pouvez créer le Canvas avant de recevoir l’approbation de votre modèle de message.
{% endalert %}

#### Étape 2 : Créer votre Canvas

Ensuite, créez un Canvas avec une étape de message qui inclut votre modèle créé. 

![][14]

Créez une étape d’action qui suit l’étape du message. Créez un groupe par option de réponse rapide dans cette étape d’action.

![Un Canvas où l’action d’évaluation est « envoyer un message entrant WhatsApp ».][15]

Pour chaque groupe d’options de réponse rapide, spécifiez le texte exact en tant que bouton que vous faites correspondre. Notez que les mots-clés doivent être en majuscules. 

![Une étape Canvas où l’action « envoyer un message entrant WhatsApp » est définie pour être envoyée lorsqu’un corps de message spécifique est reçu.][16]

Si vous souhaitez une réponse par défaut pour les utilisateurs qui répondent au message avec du texte au lieu de réponses rapides, créez un groupe supplémentaire sans corps de message correspondant.

Depuis ce point, continuez à créer le Canvas comme vous le feriez habituellement.

### Réponses

Vous désirerez probablement un message de réponse pour chaque réponse. Nous vous recommandons d’avoir une option « fourre-tout » pour les réponses qui ne sont pas dans les limites des réponses rapides (par exemple, pour les clients qui répondent par un message général plutôt qu’une invite prédéterminée). Par exemple, « Nous sommes désolés, nous n’avons pas reconnu votre réponse. Pour les problèmes d’assistance, veuillez envoyer un message à <support channel>. »

![Un Canvas créé montrant les réponses pour chaque bouton d’appel à l’action.][18]

Notez que vous pouvez utiliser toutes les actions suivantes proposées par Braze Canvas, telles que des messages en réponse, des mises à jour du profil utilisateur ou des webhooks Braze à Braze. 

[1]: {% image_buster /assets/img/whatsapp/whatsapp24.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp25.png %}
[3]: {% image_buster /assets/img/whatsapp/whatsapp26.png %}
[4]: {% image_buster /assets/img/whatsapp/whatsapp27.png %} 

[11]: {% image_buster /assets/img/whatsapp/whatsapp11.png %}
[12]: {% image_buster /assets/img/whatsapp/whatsapp12.png %}
[13]: {% image_buster /assets/img/whatsapp/whatsapp13.png %}
[14]: {% image_buster /assets/img/whatsapp/whatsapp14.png %}
[15]: {% image_buster /assets/img/whatsapp/whatsapp15.png %}
[16]: {% image_buster /assets/img/whatsapp/whatsapp16.png %}
[17]: {% image_buster /assets/img/whatsapp/whatsapp17.png %}
[18]: {% image_buster /assets/img/whatsapp/whatsapp18.png %}
