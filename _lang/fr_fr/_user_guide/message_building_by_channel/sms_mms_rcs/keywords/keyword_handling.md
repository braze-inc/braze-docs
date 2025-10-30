---
nav_title: Traitement personnalisé des mots-clés
article_title: Traitement personnalisé des mots-clés
page_order: 3
description: "Cet article de référence explique comment Braze gère les envois bidirectionnels de messages SMS, MMS et RCS, ainsi que les réponses automatiques. Vous y trouverez notamment des explications sur le fonctionnement du déclencheur de mots clés, ainsi que des catégories de mots clés personnalisées et une prise en charge multilingue."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS

---

# Traitement personnalisé des mots-clés

> Cet article de référence explique comment Braze gère les envois bidirectionnels de messages SMS, MMS et RCS, ainsi que les réponses automatiques. Vous y trouverez notamment des explications sur le fonctionnement du déclencheur de mots clés, ainsi que des catégories de mots clés personnalisées et une prise en charge multilingue.

## Envoi de messages dans les deux sens (réponses par mots-clés personnalisés)

La messagerie bidirectionnelle vous permet d'envoyer des messages et de traiter les réponses à ces messages. L'utilisateur final doit envoyer un mot-clé à Braze, qui lui répondra automatiquement. Appliqué correctement, l'envoi de messages bidirectionnels peut constituer une solution simple, immédiate et dynamique au marketing client, tout en enregistrant des économies de temps et de ressources.

## Gestion des mots-clés et des réponses automatiques

SMS, MMS et RCS avec Braze vous donne la possibilité de créer des déclencheurs de mots-clés, des réponses personnalisées, de définir des ensembles de mots-clés pour plusieurs langues et d'établir des catégories de mots-clés personnalisés. 

{% tabs %}
{% tab Add Keyword Triggers %}

#### Ajouter des déclencheurs de mots-clés

Outre les mots-clés d'acceptation et de refus par défaut, vous pouvez également définir vos propres mots-clés pour déclencher des réponses d'acceptation, de refus et d'aide.

Pour définir vos propres mots-clés, procédez comme suit :

1. Dans le tableau de bord de Braze, allez dans **Audience** > **Gestion des groupes d'abonnement** et sélectionnez un groupe d'abonnement **SMS/MMS/RCS**.<br><br>
2. Sous **Mots clés globaux**, sélectionnez l'icône en forme de crayon à côté de la catégorie de mots clés à laquelle vous souhaitez ajouter un mot clé. !mots-clés d'abonnement avec l'icône du crayon qui s'affiche.]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br>
3. Dans l'onglet qui s'ouvre, ajoutez un mot-clé que vous souhaitez déclencher dans cette catégorie de mots-clés. Notez que les mots-clés sont insensibles à la casse et que les mots-clés universels tels que `START`, `YES`, et `UNSTOP` ne peuvent pas être modifiés. ![Modifier les mots-clés pour la catégorie "Abonnement". Les mots-clés ajoutés sont "START", "UNSTOP" et "YES". Le champ du message de réponse indique "Vous avez été désabonné des messages provenant de ce numéro. Répondez à HELP pour obtenir de l'aide. Répondez STOP pour vous désabonner. Les tarifs des messages et des données peuvent s'appliquer."]({% image_buster /assets/img/sms/keyword_edit2.png %})

Les règles suivantes s'appliquent aux mots-clés et aux réponses aux mots-clés :

| Mots clés | Réponses par mot-clé |
| -------- | ----------------- |
| \- Caractères encodés UTF-8 valides<br>\- Maximum de 20 mots-clés par catégorie au total<br>\- Longueur maximale de 34 caractères<br>\- Longueur minimale de 1 caractère <br>\- Ne peut contenir d'espaces<br>\- Doit être insensible à la casse et unique dans le groupe d'abonnement. | \- Ne peut être vide<br>\- Longueur maximale de 300 caractères<br>\- Caractères UTF-8 valides |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Vous souhaitez voir comment ces mots-clés peuvent être utilisés dans vos campagnes et Canvas pour recibler et déclencher des messages ? Visitez le site [Reciblage]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) pour plus d'informations.
{% endalert %}
{% endtab %}

{% tab Manage responses %}

#### Gérer les réponses

Vous pouvez gérer vos propres réponses qui sont envoyées aux utilisateurs après qu'ils ont saisi un mot-clé dans une catégorie de mots-clés spécifique.

1. Dans le tableau de bord de Braze, allez dans **Audience** > **Gestion des groupes d'abonnement** et sélectionnez un groupe d'abonnement **SMS/MMS/RCS**. <br><br>
2. Sous **Mots clés globaux**, sélectionnez une catégorie de mots clés pour laquelle vous souhaitez modifier une réponse en cliquant sur l'icône représentant un crayon. !Mots clés à abonnement avec l'icône du crayon qui s'affiche.]({% image_buster /assets/img/sms/sms_keywords.png %})<br><br> 
3. Dans l'onglet qui s'ouvre, modifiez votre réponse. N'oubliez pas nos [six règles de conformité]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/#the-six-rules-to-get-compliance-right) lorsque vous créez votre réponse, et lisez les règles suivantes qui s'appliquent aux mots-clés et aux réponses par mot-clé. \![Réponses]({% image_buster /assets/img/sms/keyword_home.png %}){: style="max-width:70%;"}<br><br>
4. Pour raccourcir automatiquement les URL statiques dans votre réponse, basculez sur l'option **Raccourcissement des liens.**  Le compteur de caractères se met à jour pour indiquer la longueur prévue de l'URL raccourci. GIF montrant la mise à jour du compteur de caractères lorsque le bouton "Raccourcir le lien" est basculé.]({% image_buster /assets/img/sms/link_shortening.gif %}){: style="max-width:60%;"}

##### Considérations

| Mots clés | Réponses par mot-clé |
| -------- | ----------------- |
| \- Caractères encodés UTF-8 valides<br>\- Maximum de 20 mots-clés par catégorie au total<br>\- Longueur maximale de 34 caractères<br>\- Longueur minimale de 1 caractère <br>\- Ne peut contenir d'espaces<br>\- Doit être insensible à la casse et unique dans le groupe d'abonnement. | \- Ne peut être vide<br>\- Longueur maximale de 300 caractères<br>\- Caractères UTF-8 valides |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

{% alert tip %}
Si un canevas basé sur des actions est déclenché par un message SMS, MMS ou RCS entrant, vous pouvez faire référence aux propriétés SMS, MMS ou RCS dans la première [étape de message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) du canevas.
{% endalert %}

## Prise en charge multilingue

Lors d'un envoi vers certains pays, un expéditeur peut être tenu de prendre en charge les mots-clés entrants et les réponses sortantes dans une langue locale. Pour ce faire, Braze vous permet de créer un paramètre de mot-clé spécifique à la langue.
\![Liste déroulante affichant les langues à ajouter en tant que paramètre de mot-clé.]({% image_buster /assets/img/sms/multi-language.png %}){: style="float:right;max-width:50%;margin-left:10px;"}

### Créer des mots-clés spécifiques à une langue

Sélectionnez **Ajouter une langue** et choisissez votre langue cible ou recherchez une langue dans le menu déroulant.

{% alert important %}
Les langues autres que l'anglais ne sont pas accompagnées de mots-clés et de réponses prédéfinis. Les expéditeurs devront donc collaborer avec leurs équipes marketing et juridiques pour ajouter les mots-clés nécessaires à cet ensemble. Sinon, Braze ne traitera pas les messages entrants localisés pour ces langues.
{% endalert %}

Si vous devez supprimer une langue, sélectionnez le bouton **Supprimer la langue** en bas à droite.

!page des mots-clés globaux avec l'onglet "Italien" sélectionné. Des onglets supplémentaires existent pour chaque langue ajoutée.]({% image_buster /assets/img/sms/multi-language2.png %})

## Catégories de mots-clés personnalisées

Outre les trois catégories de mots-clés par défaut (Abonnement, Désabonnement et Aide), vous pouvez créer jusqu'à 25 catégories de mots-clés qui vous sont propres. Cela vous permet d'identifier des mots-clés arbitraires et de mettre en place des réponses spécifiques à votre entreprise. Un exemple de catégorie pourrait être "PROMO" ou "RABAIS", ce qui pourrait susciter une réponse sur les promotions qui ont lieu ce mois-ci. 

Ces mots-clés personnalisés fonctionnent en "permanence", ce qui signifie que tout utilisateur abonné à votre service de messages peut envoyer des mots-clés par SMS et recevoir une réponse à tout moment. En plus de ce comportement, vous avez également la possibilité de définir des mots-clés spécifiques qui ne peuvent être envoyés qu'à [certains moments]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#lifecycle-specific-keywords) du cycle de vie de l'utilisateur. 

\![Mots-clés pour une catégorie "Promo". Si un utilisateur envoie "YO" par SMS, il reçoit un message avec un code promotionnel.]({% image_buster /assets/img/sms/sms_custom_keyword.png %})

### Création d'une catégorie personnalisée

Pour créer une catégorie de mots-clés personnalisée, procédez comme suit :

1. Modifiez le groupe d'abonnement approprié.
2. Sélectionnez **Ajouter un mot-clé personnalisé**. \![Champs pour ajouter de nouveaux mots-clés.]({% image_buster /assets/img/sms/sms_custom_step.png %}){: style="max-width:90%;"}
3. Indiquez le nom d'une catégorie de mots-clés et définissez les mots-clés qu'un utilisateur peut saisir pour recevoir le message de réponse.

Une fois cette catégorie de mots-clés créée, elle sera disponible pour [filtrer et déclencher]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) dans vos campagnes et Canevas.

Les mots-clés créés dans les catégories de mots-clés personnalisés respectent toutes les règles et validations relatives à la création de nouveaux mots-clés. 

### Mots-clés spécifiques au cycle de vie

Si vous avez un cas d'utilisation dans lequel vous souhaitez limiter le moment où un client peut envoyer un mot-clé spécifique au cours de son cycle de vie (par exemple, au cours de son premier onboarding initial) pour recevoir une réponse, vous pouvez utiliser le déclencheur **Envoyer un SMS entrant au groupe d'abonnement dans la catégorie de mot-clé AUTRE** dans votre campagne ou Canvas et définir les mots-clés que vos utilisateurs peuvent envoyer à un moment donné.

Ce déclencheur permet de filtrer le message entrant spécifique en utilisant les comparaisons is or is not du message, ainsi que les règles d'expression régulière pour valider l'entrée de l'utilisateur.

#### Canevas

!étape Canvas basée sur une action avec le déclencheur Envoyer un SMS entrant au groupe d'abonnement "Messaging Service" dans la catégorie de mots-clés "Other" où le corps du message correspond à l'expression régulière "caret symbol skip".]({% image_buster /assets/img/sms/canvas_trigger.png %}){: style="max-width:90%;"}

#### Campagne

Campagne basée sur des actions avec le déclencheur Envoyer un SMS entrant au groupe d'abonnement "Marketing par sms A" dans la catégorie de mots-clés "Autre" où le corps du message est "Mot-clé 1" ou "Mot-clé 2" ou n'est pas "Mot-clé A".]({% image_buster /assets/img/sms/campaign_trigger.png %}){: style="max-width:90%;"}

### Traiter les mots-clés inconnus

Bien que cela ne soit pas obligatoire, nous vous recommandons vivement de mettre en place une réponse automatique lorsque les utilisateurs envoient des mots-clés entrants qui ne correspondent pas à un mot-clé existant. Ce message informe l'utilisateur que le mot-clé n'est pas reconnu et lui donne des conseils. 

Pour ce faire, créez une campagne SMS, MMS ou RCS avec un message du type "Désolé ! Nous n'avons pas reconnu ce mot-clé, le texte STOP pour arrêter ou HELP pour aider". Ensuite, à l'étape de la livraison, sélectionnez **Livraison par action** et utilisez le déclencheur **Envoi de SMS entrants au groupe d'abonnement dans la catégorie de mots clés AUTRE**.

Envoi basé sur une action pour une campagne dont le déclencheur est "Envoi d'un SMS entrant à un subscription group dans la catégorie de mots-clés "Autre"".]({% image_buster /assets/img/sms/sms_other.png %})

{% alert tip %}
Vous souhaitez savoir comment ces mots-clés et catégories de mots-clés peuvent être utilisés dans vos campagnes et Canvas pour recibler et déclencher des messages ? Visitez le site [Reciblage]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) pour plus d'informations.
{% endalert %}

