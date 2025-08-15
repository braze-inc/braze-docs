---
nav_title: Écrire aux utilisateurs
article_title: Écrire aux utilisateurs
description: "Cet article de référence explique comment Braze va gérer les messages des utilisateurs."
page_type: reference
channel:
  - WhatsApp
page_order: 5.1
alias: /whatsapp_quick_replies/

---

# Messages des utilisateurs

> WhatsApp est un canal de communication bidirectionnel. Non seulement votre marque peut envoyer des messages aux utilisateurs, mais ils peuvent également participer à des conversations en utilisant des campagnes modélisées et des Canvases. Il existe plusieurs façons de procéder, notamment les réponses rapides de WhatsApp, les messages de liste et les mots déclencheurs. Les appels à l'action (CTA) des réponses rapides et des messages de liste sont un excellent moyen d'encourager l'engagement des utilisateurs dans vos envois de messages WhatsApp.

## Déclencheurs basés sur l'action 

Les campagnes et les toiles peuvent démarrer, se ramifier et être modifiées en cours de route à partir d'un message WhatsApp entrant (un utilisateur envoyant un message sur votre WhatsApp), tel qu'un mot déclencheur. 

Assurez-vous que votre mot déclencheur correspond à ce que vous attendez des utilisateurs.

**Choses à savoir :**
- Chaque lettre de votre mot déclencheur doit être en majuscule lorsqu'il est configuré. Braze n'exige pas que les mots déclencheurs entrants envoyés par les utilisateurs soient en majuscules. Par exemple, envoyer un message "jOin2023" déclenchera toujours le Canvas ou la campagne.
- Si aucun mot déclencheur n'est spécifié sur le déclencheur basé sur l'action du calendrier d'entrée, la campagne ou Canvas s'exécutera pour TOUS les messages WhatsApp entrants. Cela inclut les messages qui ont des phrases correspondantes dans les campagnes actives et les Canvases, auquel cas l'utilisateur recevra deux messages WhatsApp.

{% tabs %}
{% tab Campagne %}

![Options de planification de campagnes basées sur l'action.]({% image_buster /assets/img/whatsapp/whatsapp27.png %})

{% endtab %}
{% tab Canvas %}

![Options de planification de Canvas basées sur l'action.]({% image_buster /assets/img/whatsapp/whatsapp25.png %})

{% endtab %}
{% endtabs %}

## Réponses non reconnues

Nous vous recommandons d'inclure une option pour les réponses non reconnues sur les Canvases interactifs. Cela guide les utilisateurs à comprendre quels sont les invites disponibles et fixe les attentes pour le canal. La gestion des attentes peut être particulièrement utile si vous avez des canaux WhatsApp avec chat en direct avec un agent. 
- Dans l'étape d'action, après avoir créé les groupes d'action pour les phrases de filtre personnalisées, ajoutez un groupe d'action supplémentaire pour "Envoyer un message WhatsApp", mais **ne cochez pas Où se trouve le corps du message**. Cela capturera toutes les réponses utilisateur non reconnues, similaire à une clause "else". 
- Nous recommandons de suivre avec un message WhatsApp informant l'utilisateur que ce canal n'est pas surveillé et de les guider vers un canal de support si nécessaire. 

## Réponses rapides 

![L'écran de téléphone affichant un bouton d'appel à l'action répondra au texte du bouton cliqué.]({% image_buster /assets/img/whatsapp/whatsapp11.png %}){: style="float:right;max-width:25%;margin-left:15px;border: 0;"}

Les réponses rapides apparaissent sous forme d’options de bouton cliquable dans la conversation, mais agissent comme si un utilisateur avait répondu par du texte. Braze traite ensuite ceux-ci comme des messages entrants et peut renvoyer des réponses prédéfinies en fonction du bouton cliqué. Utilisez l'étape "Action de message entrant WhatsApp" lors de la création et du filtrage des réponses de vos utilisateurs.

![Un message WhatsApp comportant du texte et trois boutons d'appel à l'action.]({% image_buster /assets/img/whatsapp/whatsapp13.png %}){: style="max-width:50%;"}

### Configurer l'expérience de réponse rapide dans Canvas

#### Étape 1 : Créer des CTA

Tout d'abord, créez vos CTA de réponse rapide dans le [Gestionnaire de Modèles de Messages WhatsApp](https://business.facebook.com/wa/manage/message-templates/) au sein d'un modèle de message. 

![L'interface utilisateur du gestionnaire de modèles de messages WhatsApp montre comment créer un bouton CTA, en indiquant le type de bouton (personnalisé) et le texte du bouton.]({% image_buster /assets/img/whatsapp/whatsapp12.png %}){: style="max-width:80%;"}

Une fois que votre modèle a été soumis et approuvé par WhatsApp, vous pouvez l’utiliser pour créer un Canvas dans Braze. 

{% alert tip %}
Vous pouvez créer le Canvas avant de recevoir l’approbation de votre modèle de message.
{% endalert %}

#### Étape 2 : Créer votre Canvas

Ensuite, créez un Canvas avec une étape de message qui inclut votre modèle créé. 

![Compositeur d'envois de messages par étapes sur WhatsApp avec un modèle de réponse rapide rempli.]({% image_buster /assets/img/whatsapp/whatsapp14.png %})

Créez une étape d’action qui suit l’étape du message. Créez un groupe par option de réponse rapide dans cette étape d’action.

![Un canvas dont l'action d'évaluation est "envoyer un message entrant whatsapp".]({% image_buster /assets/img/whatsapp/whatsapp15.png %})

Pour chaque groupe d’options de réponse rapide, spécifiez le texte exact en tant que bouton que vous faites correspondre. Notez que les mots-clés doivent être en majuscules. 

![Une étape du canvas où l'action "envoyer un message whatsapp entrant" est définie pour être envoyée lorsqu'un corps de message spécifique est reçu.]({% image_buster /assets/img/whatsapp/whatsapp16.png %})

Si vous souhaitez une réponse par défaut pour les utilisateurs qui répondent au message avec du texte au lieu de réponses rapides, créez un groupe supplémentaire sans corps de message correspondant.

Depuis ce point, continuez à créer le Canvas comme vous le feriez habituellement.

### Réponses

Vous désirerez probablement un message de réponse pour chaque réponse. Nous vous recommandons d’avoir une option « fourre-tout » pour les réponses qui ne sont pas dans les limites des réponses rapides (par exemple, pour les clients qui répondent par un message général plutôt qu’une invite prédéterminée). Par exemple, « Nous sommes désolés, nous n’avons pas reconnu votre réponse. Pour les problèmes d’assistance, veuillez envoyer un message à <support channel>. »

![Un canvas créé montre les réponses pour chaque bouton d'action.]({% image_buster /assets/img/whatsapp/whatsapp18.png %})

Notez que vous pouvez utiliser toutes les actions suivantes proposées par Braze Canvas, telles que des messages en réponse, des mises à jour du profil utilisateur ou des webhooks Braze à Braze. 

## Liste des messages

Les messages de liste apparaissent sous la forme d'un corps de message avec une liste d'options cliquables. Chaque liste peut comporter plusieurs sections et chaque liste peut comporter jusqu'à 10 lignes.

![Exemple d'un message WhatsApp avec des lignes correspondant à différents styles de mode.]({% image_buster /assets/img/whatsapp/list_message_example.png %}){: style="max-width:40%;"}

### Configurer l'expérience message de la liste dans Canvas

#### Étape 1 : Créer ou modifier un canevas existant basé sur l'action

Vous ne pouvez ajouter des messages de la liste WhatsApp aux canevas que s'ils sont basés sur une action, car ils doivent être en réponse à un message de l'utilisateur.

#### Étape 2 : Créer une étape de l'envoi des messages WhatsApp

Ajoutez une [étape de message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) WhatsApp, puis sélectionnez la présentation du message de réponse de **Message de liste.**

![Une collection sélectionnable des différents types d'envois de messages de réponse WhatsApp que vous pouvez créer, y compris "Message de liste".]({% image_buster /assets/img/whatsapp/list_message_option.png %}){: style="max-width:70%;"}

Ajoutez un nom de **bouton Liste** que les utilisateurs sélectionneront pour afficher votre liste. Ensuite, utilisez les champs du **contenu de la liste** pour créer votre liste :

- **Section :** Ajoutez jusqu'à 10 sections pour regrouper et organiser les éléments de votre liste. Par exemple, un détaillant de vêtements peut utiliser des sections pour organiser ses produits en fonction des styles saisonniers (printemps, été, automne et hiver) ou des articles vestimentaires (hauts, bas et chaussures).
- **Rangée :** Ajoutez jusqu'à 10 lignes, ou éléments de liste, dans toutes les sections.
- **Description de la ligne (facultatif) :** Ajoutez une description facultative à toutes les lignes (éléments de la liste).

![La section "Contenu de la liste" a été complétée par deux sections et plusieurs lignes et descriptions de lignes.]({% image_buster /assets/img/whatsapp/list_content.png %}){: style="max-width:60%;"}

Modifiez l'ordre des sections et des lignes en sélectionnant et en faisant glisser l'icône située à côté de leur nom.

![Déplacement d'une section de liste vers un nouvel emplacement/localisation.]({% image_buster /assets/img/whatsapp/drag_list_order.png %}){: style="max-width:60%;"}

De retour dans le compositeur Canvas, ajoutez un [parcours d'action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) après l'étape du message qui comporte un groupe pour chaque réponse à la liste. Dans chaque groupe :

1. Ajoutez un déclencheur pour le **groupe d'abonnement WhatsApp entrant envoyé** et sélectionnez le groupe d'abonnement WhatsApp correspondant.
2. Cochez la case **Endroit où se trouve le corps du message**.
3. Spécifiez le contenu d'une ligne (ou d'un élément de liste).

![Compositeur pour un parcours d'action avec des groupes pour différents styles de vêtements.]({% image_buster /assets/img/whatsapp/action_path_list_message.png %})

Continuez à créer votre Canvas.

### Création de parcours d'actions pour les descriptions longues

Si vous avez des descriptions de ligne, vous devez utiliser l'**expression régulière Matches** pour spécifier une ligne. Par exemple, si vous souhaitez spécifier une ligne avec la description "Notre nouveau style qui s'adapte à votre paire de bottines préférée", vous pouvez utiliser l'[expression régulière]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/) avec "bottines".

![Un déclencheur WhatsApp utilisant le filtre pour "Matches expression régulière" pour capturer les messages de réponse avec "ankle boots".]({% image_buster /assets/img/whatsapp/regex_list_message.png %})

## Considérations relatives aux messages de réponse

Les messages de réponse doivent être envoyés dans les 24 heures suivant la réception du message d'un utilisateur. Pour aider à créer des expériences réussies, Braze vérifie la logique des messages pour confirmer qu'il existe un message utilisateur entrant en amont qui débloque le message de réponse. 

Les événements suivants débloquent les messages d'envoi de messages : 

- Message entrant 
  - [Parcours d'action]({{site.baseurl}}/action_paths/) ou [entrée basée sur une action]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) avec le déclencheur **Envoyer un message entrant WhatsApp**.

![Une étape d'entrée basée sur une action avec le déclencheur "Envoyer un message entrant WhatsApp".]({% image_buster /assets/img/whatsapp/whatsapp_inbound_message_trigger.png %})

- [Entrée déclenchée par l'API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/)
- Envoi de messages sur les produits 
  - [`ecommerce.cart_updated`]({{site.baseurl}}/user_guide/data/custom_data/recommended_events/ecommerce_events/?tab=ecommerce.cart_updated#types-of-ecommerce-recommended-events) événement

![Un parcours d'action avec le déclencheur d'un événement personnalisé réalisé `ecommerce.cart_updated`.]({% image_buster /assets/img/whatsapp/ecommerce_cart_updated.png %})

