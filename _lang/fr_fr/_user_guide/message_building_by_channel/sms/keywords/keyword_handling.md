---
nav_title: Gestion personnalisée des mots-clés
article_title: Gestion personnalisée des mots-clés
page_order: 3
description: "Cet article de référence explique comment Braze traite les messages SMS bidirectionnels et les réponses automatiques. Il inclut des explications sur le fonctionnement des déclencheurs de mots-clés, ainsi que sur les catégories de mots-clés personnalisés et la prise en charge multilingue."
page_type: reference
channel:
  - SMS

---

# Gestion personnalisée des mots-clés

> Cet article de référence explique comment Braze traite les messages SMS bidirectionnels et les réponses automatiques. Il inclut des explications sur le fonctionnement des déclencheurs de mots-clés, ainsi que sur les catégories de mots-clés personnalisés et la prise en charge multilingue.

## Messagerie bidirectionnelle (réponses aux mots-clés personnalisés)

La messagerie bidirectionnelle vous permet d’envoyer des messages et de traiter les réponses à ces messages. Les utilisateurs finaux doivent envoyer un mot-clé à Braze, puis l’utilisateur reçoit une réponse automatique. Appliquée correctement, la messagerie bidirectionnelle peut être une solution simple, immédiate et dynamique pour le marketing client, et qui permet de gagner du temps et des ressources tout au long du processus.

## Gestion des mots-clés et des réponses automatiques

Les SMS avec Braze vous permettent de créer des déclencheurs de mots-clés, de personnaliser les réponses, de définir des ensembles de mots-clés pour plusieurs langues et d’établir des catégories de mots-clés personnalisés. 

{% tabs %}
{% tab Ajouter des déclencheurs de mots-clés %}

#### Ajouter des déclencheurs de mots-clés

Outre les mots-clés par défaut d’abonnement et de désabonnement, vous pouvez définir vos propres mots-clés pour déclencher des réponses d’abonnement, de désabonnement et d’aide.

Pour définir vos propres mots-clés, procédez comme suit :

1. Dans le tableau de bord de Braze, sélectionnez **Audience** > **Groupes d’abonnement** et sélectionnez votre groupe d'abonnement aux SMS.<br><br>
2. Sous **SMS Global Keywords**, cliquez sur l'icône représentant un crayon à côté de la catégorie de mots-clés à laquelle vous souhaitez ajouter un mot-clé. ![]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. Dans l'onglet qui s'ouvre, ajoutez un mot-clé que vous souhaitez déclencher dans cette catégorie de mots-clés. Notez que les mots-clés ne sont pas sensibles à la casse et que les mots-clés universels tels que `START`, `YES` et `UNSTOP` ne peuvent pas être modifiés. ![Modification des mots-clés pour la catégorie Abonnement. Les mots-clés ajoutés sont « START », « UNSTOP » et « YES ». Le champ de réponse indique « Vous n’êtes plus abonné aux messages provenant de ce numéro. Répondez HELP pour obtenir de l’aide. Répondez STOP pour vous désabonner. Des tarifs de messages et de données peuvent être appliqués."]({% image_buster /assets/img/sms/keyword_edit2.png %})

Les règles suivantes s’appliquent aux mots-clés et aux réponses à des mots-clés :

| Mots-clés | Réponses à des mots-clés |
| -------- | ----------------- |
| \- Caractères valides codés en UTF-8<br>\- Vingt mots-clés maximum par catégorie au total<br>\- Longueur maximale de 34 caractères<br>\- Longueur minimale de 1 caractère <br>\- Ne peut pas contenir des espaces<br>\- Doit être sensible à la casse et unique dans tout le groupe d’abonnement | \- Ne peut pas être vide<br>\- Longueur maximale de 300 caractères<br>\- Caractères valides en UTF-8 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Vous voulez voir comment utiliser ces mots-clés dans vos campagnes et Canvas pour recibler et déclencher des messages ? Consultez notre article sur le [reciblage par SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) pour plus d'informations.
{% endalert %}
{% endtab %}

{% tab Gérer les réponses %}

#### Gérer les réponses

Vous pouvez gérer vos propres réponses qui sont envoyées aux utilisateurs après qu'ils aient saisi un mot-clé dans une catégorie de mots-clés spécifique.

1. Dans le tableau de bord de Braze, sélectionnez **Audience** > **Groupes d’abonnement** et sélectionnez votre groupe d'abonnement aux SMS. <br><br>
2. Sous **Mots clés globaux SMS**, sélectionnez une catégorie de mots clés pour laquelle vous souhaitez modifier une réponse en cliquant sur l'icône représentant un crayon. ![]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br> 
3. Dans l'onglet qui s'ouvre, modifiez votre réponse. Gardez à l'esprit nos [six règles de conformité]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/#the-six-rules-to-get-compliance-right) lorsque vous créez votre réponse, et lisez les règles suivantes qui s'appliquent aux mots-clés et aux réponses par mot-clé. ![Réponses]({% image_buster /assets/img/sms/keyword_home.png %})<br><br>
4. Pour raccourcir automatiquement les URL statiques dans votre réponse, basculez sur l'option **Raccourcissement des liens.**  Le compteur de caractères sera mis à jour pour indiquer la longueur prévue de l'URL raccourci. ![Un GIF montrant la mise à jour du compteur de caractères lorsque le basculeur "Link Shortening" est activé.]({% image_buster /assets/img/sms/link_shortening.gif %}){: style="max-width:50%;"}

##### Considérations

| Mots-clés | Réponses à des mots-clés |
| -------- | ----------------- |
| \- Caractères valides codés en UTF-8<br>\- Vingt mots-clés maximum par catégorie au total<br>\- Longueur maximale de 34 caractères<br>\- Longueur minimale de 1 caractère <br>\- Ne peut pas contenir des espaces<br>\- Doit être sensible à la casse et unique dans tout le groupe d’abonnement | \- Ne peut pas être vide<br>\- Longueur maximale de 300 caractères<br>\- Caractères valides en UTF-8 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

{% alert tip %}
Si un canvas basé sur une action est déclenché par un message SMS entrant, vous pouvez référencer les propriétés du SMS dans la première [étape message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) du canvas.
{% endalert %}

## Prise en charge multilingue

Lors de l’envoi vers certains pays, un expéditeur doit éventuellement prendre en charge les mots-clés entrants et les réponses sortantes dans une langue locale. Pour ce faire, Braze vous permet de créer un mot-clé spécifique à une langue.
![][16]{: style="float:right;max-width:40%;margin-left:10px;"}

### Créer des mots-clés spécifiques à une langue

Cliquez sur **Ajouter une langue** et sélectionnez votre langue cible ou recherchez une langue dans le menu déroulant.

{% alert important %}
Notez que d’autres langues sont fournies sans mots-clés et réponses prédéfinis, comme l’anglais. Les expéditeurs doivent donc travailler avec leurs équipes marketing et juridique pour ajouter tous les mots-clés requis à l’ensemble en question. Sinon, Braze ne traitera pas les messages entrants localisés pour ces langues.
{% endalert %}

Si vous devez supprimer une langue, cliquez sur le bouton **Supprimer la langue** en bas à droite.

![Page SMS Global Keywords (Mots-clés globaux SMS) avec l’onglet « French » (Français) sélectionné. Il existe un onglet pour chaque langue ajoutée.][5]

## Catégories de mots-clés personnalisés

Outre les trois catégories de mots-clés par défaut (Abonnement, Désabonnement et Aide), vous pouvez créer jusqu'à 25 catégories de mots-clés qui vous sont propres. De cette façon, vous pouvez identifier les mots-clés arbitraires et définir des réponses spécifiques à votre entreprise. Une catégorie peut par exemple être « PROMO » ou « RABAIS », motivant éventuellement des réponses à des promotions actives au cours de ce mois. 

Comme ces mots-clés personnalisés fonctionnent en permanence, tout utilisateur abonné à votre service de messagerie peut envoyer des mots-clés de texte et recevoir une réponse à tout moment. En plus de ce comportement, vous avez également la possibilité de définir des mots-clés spécifiques qui ne peuvent être envoyés qu'à [certains moments]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#lifecycle-specific-keywords) du cycle de vie de l'utilisateur. 

![Mots-clés pour une catégorie "Doubleoptin". Si un utilisateur envoie « Y », il reçoit le message « Merci d'avoir confirmé votre inscription à Hair Cuttery SMS ».][12]

### Création d'une catégorie personnalisée

Pour créer une catégorie de mots-clés personnalisée, procédez comme suit :

1. Modifiez le groupe d'abonnement approprié.
2. Cliquez sur **Ajouter un mot-clé personnalisé**. ![][13]{: style="max-width:90%;"}
3. Indiquez le nom d'une catégorie de mots-clés et définissez les mots-clés qu'un utilisateur peut saisir pour recevoir le message de réponse.

Une fois cette catégorie de mots-clés créée, elle sera disponible pour [filtrer et déclencher]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) dans vos campagnes et Canevas.

Les mots-clés créés dans les catégories de mots-clés personnalisés respectent toutes les règles et validations relatives à la création de nouveaux mots-clés. 

### Mots-clés spécifiques au cycle de vie

Si vous avez un cas d'utilisation dans lequel vous souhaitez limiter le moment où un client peut envoyer un mot-clé spécifique au cours de son cycle de vie (par exemple, au cours de son premier onboarding initial) pour recevoir une réponse, vous pouvez utiliser le déclencheur **Envoyer un SMS entrant au groupe d'abonnement dans la catégorie de mot-clé AUTRE** dans votre campagne ou Canvas et définir les mots-clés que vos utilisateurs peuvent envoyer à un moment donné.

Ce déclencheur prend en charge le filtrage sur le message entrant spécifique à l’aide de comparaisons « est/n’est pas » du message, mais aussi des règles d’expression régulière « correspond/ne correspond pas » pour valider l’entrée de l’utilisateur.

#### Canvas

![Étape du canevas basée sur des actions avec le déclencheur Envoyer un SMS entrant au groupe d'abonnement "Service de messagerie" dans la catégorie de mots-clés "Autre" lorsque le corps du message correspond à l'expression régulière "caret symbol skip."][14]{: style="max-width:90%;"}

#### Campagne arrêtée

![Campagne basée sur des actions avec le déclencheur Envoyer un SMS entrant au groupe d'abonnement "Marketing par sms A" dans la catégorie de mots clés "Autre" lorsque le corps du message est "Mot clé 1" ou "Mot clé 2" ou n'est pas "Mot clé A".][15]{: style="max-width:90%;"}

### Gérer les mots-clés inconnus

Bien que cela ne soit pas obligatoire, nous recommandons fortement de configurer une réponse automatique lorsque les utilisateurs envoient des mots-clés SMS entrants qui ne correspondent pas à un mot-clé existant. Ce message informe l’utilisateur que le mot-clé n’est pas reconnu et offre quelques conseils. 

Pour ce faire, créez une campagne SMS avec un message de type « Désolé ! Nous n’avons pas reconnu ce mot-clé, envoyez STOP pour arrêter ou HELP pour obtenir de l’aide. » Ensuite, à l'étape de la livraison, sélectionnez **Livraison par action** et utilisez le déclencheur **Envoi de SMS entrants au groupe d'abonnement dans la catégorie de mots clés AUTRE**.

![]({% image_buster /assets/img/sms/sms_other.png %})

{% alert tip %}
Vous voulez voir comment utiliser ces mots-clés et catégories de mots-clés dans vos campagnes et Canvas pour recibler et déclencher les messages ? Consultez notre article sur le [reciblage par SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) pour plus d'informations.
{% endalert %}

[oblink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[1]: {% image_buster /assets/img/sms/keyword_edit2.png %}
[2]: {% image_buster /assets/img/sms/keyword_home.png %}
[inconnu] : {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/unknown_phone_numbers/
[endpoint]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[IMAGE2]: {% image_buster /assets/img/sms/sms_message_body.png %}
[5]: {% image_buster /assets/img/sms/multi-language2.png %}
[12]: {% image_buster /assets/img/sms/sms_custom_keyword.png %}
[13]: {% image_buster /assets/img/sms/sms_custom_step.png %}
[14]: {% image_buster /assets/img/sms/canvas_trigger.png %}
[15]: {% image_buster /assets/img/sms/campaign_trigger.png %}
[16]: {% image_buster /assets/img/sms/multi-language.png %}
