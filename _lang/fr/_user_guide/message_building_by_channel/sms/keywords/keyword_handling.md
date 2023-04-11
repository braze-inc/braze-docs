---
nav_title: Gestion personnalisée des mots-clés
article_title: Gestion personnalisée des mots-clés
page_order: 2
description: "Cet article de référence explique comment Braze traite les messages SMS bidirectionnels et les réponses automatiques. Il inclut des explications sur le fonctionnement des déclencheurs de mots-clés, ainsi que sur les catégories de mots-clés personnalisés et la prise en charge multilingue."
page_type: reference
channel:
  - SMS

---

<br>
{% alert important %}
Êtes-vous actuellement un client SMS non natif ? Si oui, consultez la [documentation sur les SMS non natifs](/docs/user_guide/message_building_by_channel/sms/non_native/) et l’article sur la gestion des mots-clés.
{% endalert %}

## Messagerie bidirectionnelle (réponses aux mots-clés personnalisés)

La messagerie bidirectionnelle vous permet d’envoyer des messages et de traiter les réponses à ces messages. Les utilisateurs finaux doivent envoyer un mot-clé à Braze, puis l’utilisateur reçoit une réponse automatique. Appliquée correctement, la messagerie bidirectionnelle peut être une solution simple, immédiate et dynamique pour le marketing client, et qui permet de gagner du temps et des ressources tout au long du processus.

## Gestion des mots-clés et des réponses automatiques

Les SMS avec Braze vous permettent de créer des déclencheurs de mots-clés, de personnaliser les réponses, de définir des ensembles de mots-clés pour plusieurs langues et d’établir des catégories de mots-clés personnalisés. 

{% tabs %}
{% tab Add Keyword Triggers %}

#### Ajouter des déclencheurs de mots-clés

Outre les mots-clés par défaut d’abonnement et de désabonnement, vous pouvez définir vos propres mots-clés pour déclencher des réponses d’abonnement, de désabonnement et d’aide.

![Modification des mots-clés pour la catégorie Abonnement. Les mots-clés ajoutés sont « START », « UNSTOP » et « YES ». Le champ de réponse indique « Vous n’êtes plus abonné aux messages provenant de ce numéro. Répondez HELP pour obtenir de l’aide. Répondez STOP pour vous désabonner. Des tarifs pour les messages et les données peuvent s’appliquer. »]({% image_buster /assets/img/sms/keyword_edit2.png %}){: style="float:right;max-width:40%;margin-left:10px;"}
1. Pour définir vos propres mots-clés, accédez à la section SMS du tableau de bord situé dans Subscription Groups (Groupes d’abonnement).<br><br>
2. Dans SMS Global Keywords (Mots-clés globaux SMS), sélectionnez une catégorie de mots-clés pour ajouter un mot-clé à l’aide de l’icône en forme de crayon.<br><br>
3. Dans la boîte de dialogue qui s’affiche, ajoutez le mot-clé souhaité pour déclencher cette catégorie de mots-clés. Notez que les mots-clés sont sensibles à la casse et que les mots-clés universels `START`, `YES` et `UNSTOP` ne sont pas modifiables. 

![]({% image_buster /assets/img/sms/sms_keywords.png %})

Les règles suivantes s’appliquent aux mots-clés et aux réponses à des mots-clés :

| Mots-clés | Réponses à des mots-clés |
| -------- | ----------------- |
| - Caractères valides codés en UTF-8<br>- Vingt mots-clés maximum par catégorie au total<br>- Longueur maximale de 34 caractères<br>- Longueur minimale de 1 caractère <br>- Ne peut pas contenir des espaces<br>- Doit être sensible à la casse et unique dans tout le groupe d’abonnement | - Ne peut pas être vide<br>- Longueur maximale de 300 caractères<br>- Caractères valides en UTF-8 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
Vous voulez voir comment utiliser ces mots-clés dans vos campagnes et Canvas pour recibler et déclencher des messages ? Consultez notre article [Reciblage des SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) pour plus d’informations.
{% endalert %}
{% endtab %}

{% tab Manage responses %}

#### Gérer les réponses

Vous pouvez gérer vos propres réponses, envoyées aux utilisateurs quand ils saisissent un mot-clé dans une catégorie de mots-clés spécifique.

![Accueil]({% image_buster /assets/img/sms/keyword_edit2.png %}){: style="float:right;max-width:40%;margin-left:10px;"}
1. Pour gérer vos réponses à des mots-clés, accédez à la section SMS du tableau de bord situé dans Subscription Groups (Groupes d’abonnement). <br><br>
2. Dans SMS Global Keywords (Mots-clés globaux SMS), sélectionnez une catégorie de mots-clés pour modifier une réponse à l’aide de l’icône en forme de crayon.<br><br> 
3. Dans la boîte de dialogue qui s’affiche, modifiez et enregistrez votre réponse. Gardez à l’esprit les [six règles pour garantir la conformité]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/#the-six-rules-to-get-compliance-right) lorsque vous créez votre réponse, et lisez les règles suivantes qui s’appliquent aux mots-clés et aux réponses aux mots-clés.<br><br>

![Réponses]({% image_buster /assets/img/sms/keyword_home.png %})

| Mots-clés | Réponses à des mots-clés |
| -------- | ----------------- |
| - Caractères valides codés en UTF-8<br>- Vingt mots-clés maximum par catégorie au total<br>- Longueur maximale de 34 caractères<br>- Longueur minimale de 1 caractère <br>- Ne peut pas contenir des espaces<br>- Doit être sensible à la casse et unique dans tout le groupe d’abonnement | - Ne peut pas être vide<br>- Longueur maximale de 300 caractères<br>- Caractères valides en UTF-8 |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

{% alert tip %} 
Si un Canvas par événement est déclenché par un SMS entrant, vous pouvez référencer les propriétés du SMS dans la première [étape de message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) du Canvas.
{% endalert %}

## Prise en charge multilingue

Lors de l’envoi vers certains pays, un expéditeur doit éventuellement prendre en charge les mots-clés entrants et les réponses sortantes dans une langue locale. Pour ce faire, Braze vous permet de créer un mot-clé spécifique à une langue. 
![][16]{: style="float:right;max-width:40%;margin-left:10px;"}

Pour commencer, cliquez sur **Add a language** (Ajouter une langue) et sélectionnez votre langue cible ou recherchez une langue dans le menu déroulant.

{% alert important %}
Notez que d’autres langues sont fournies sans mots-clés et réponses prédéfinis, comme l’anglais. Les expéditeurs doivent donc travailler avec leurs équipes marketing et juridique pour ajouter tous les mots-clés requis à l’ensemble en question. Sinon, Braze ne traitera pas les messages entrants localisés pour ces langues. 
{% endalert %}

Si vous devez supprimer une langue, cliquez sur le bouton **Delete Language** (Supprimer la langue) en bas à droite.

![Page SMS Global Keywords (Mots-clés globaux SMS) avec l’onglet « French » (Français) sélectionné. Il existe un onglet pour chaque langue ajoutée.][5]

## Catégories de mots-clés personnalisés

Outre les trois catégories de mots-clés par défaut (Abonnement, Désabonnement et Aide), vous pouvez créer jusqu’à 25 catégories de mots-clés. De cette façon, vous pouvez identifier les mots-clés arbitraires et définir des réponses spécifiques à votre entreprise. Une catégorie peut par exemple être « PROMO » ou « RABAIS », motivant éventuellement des réponses à des promotions actives au cours de ce mois. 

Comme ces mots-clés personnalisés fonctionnent en permanence, tout utilisateur abonné à votre service de messagerie peut envoyer des mots-clés de texte et recevoir une réponse à tout moment. À l’exception de ce comportement, vous pouvez également définir des mots-clés spécifiques qui ne peuvent être envoyés qu’à [certains points]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#lifecycle-specific-keywords) du cycle de vie de votre utilisateur. 

![Mots-clés pour une catégorie « Promotions ». Si un utilisateur envoie le message « DEALS », « PROMOS » ou « PROMOTIONS », il reçoit le message « Découvrez les promotions spéciales qui vous attendent sur example.com/promos ».][12]

### Créer une catégorie personnalisée

![][13]{: style="float:right;max-width:40%;margin-left:10px;"}

Pour créer une catégorie de mots-clés personnalisés, modifiez le groupe d’abonnement approprié, puis cliquez sur **Add Custom Keyword Category** (Ajouter une catégorie de mots-clés personnalisés). Vous pouvez alors fournir un nom de catégorie de mots-clés et définir les mots-clés que l’utilisateur peut saisir pour recevoir le message de réponse.

Une fois créée, cette catégorie de mots-clés est disponible dans vos [filtres et déclencheurs]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) pour vos campagnes et Canvas.

Les mots-clés créés dans les catégories de mots-clés personnalisés respectent toutes les règles et validations relatives à la création de nouveaux mots-clés. 

### Mots-clés spécifiques au cycle de vie

Si, pour un cas d’utilisation, vous souhaitez limiter l’envoi par un client d’un mot-clé spécifique pendant son cycle de vie (lors de son premier onboarding, par exemple) pour recevoir une réponse, vous pouvez utiliser le déclencheur « Envoyer un SMS entrant au groupe d’abonnement dans la catégorie de mots-clés AUTRE » dans votre campagne ou Canvas, et définir certains mots-clés ad hoc que vos utilisateurs peuvent envoyer à un moment donné.

Ce déclencheur prend en charge le filtrage sur le message entrant spécifique à l’aide de comparaisons « est/n’est pas » du message, mais aussi des règles d’expression régulière « correspond/ne correspond pas » pour valider l’entrée de l’utilisateur.

#### Canvas

![Canvas Step par événement avec le déclencheur Envoyer un SMS entrant au groupe d’abonnement « Service de message marketing A » dans la catégorie de mots-clés « Autre », où le corps du message correspond à l’expression régulière de saut de symbole caret. »][14]{: style="max-width:80%;"}

#### Campagne

![Campagne par événement avec le déclencheur Envoyer un SMS entrant au groupe d’abonnement « Service de message marketing A » dans la catégorie de mots-clés « Autre », où le corps du message est « Mot-clé 1 » ou « Mot-clé 2 » ou n’est pas « Mot-clé A ».][15]{: style="max-width:80%;"}

### Gérer les mots-clés inconnus

Bien que cela ne soit pas obligatoire, nous recommandons fortement de configurer une réponse automatique lorsque les utilisateurs envoient des mots-clés SMS entrants qui ne correspondent pas à un mot-clé existant. Ce message informe l’utilisateur que le mot-clé n’est pas reconnu et offre quelques conseils. 

Pour ce faire, créez une campagne SMS avec un message de type « Désolé ! Nous n’avons pas reconnu ce mot-clé, envoyez STOP pour arrêter ou HELP pour obtenir de l’aide. » Ensuite, lors de l’étape de livraison, sélectionnez **Livraison par événement** et utilisez le déclencheur **Sent inbound SMS to subscription group with keyword category OTHER** (Envoi SMS entrant au groupe d’abonnement dans la catégorie de mots-clés AUTRE).

![]({% image_buster /assets/img/sms/sms_other.png %})

{% alert tip %}
Vous voulez voir comment utiliser ces mots-clés et catégories de mots-clés dans vos campagnes et Canvas pour recibler et déclencher les messages ? Consultez notre article [Reciblage des SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) pour plus d’informations.
{% endalert %}

[oblink]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process
[1]: {% image_buster /assets/img/sms/keyword_edit2.png %}
[2]: {% image_buster /assets/img/sms/keyword_home.png %}
[unknown]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/unknown_phone_numbers/
[endpoint]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[IMAGE2]: {% image_buster /assets/img/sms/sms_message_body.png %}
[5]: {% image_buster /assets/img/sms/multi-language2.png %}
[12]: {% image_buster /assets/img/sms/sms_custom_keyword.png %}
[13]: {% image_buster /assets/img/sms/sms_custom_step.png %}
[14]: {% image_buster /assets/img/sms/canvas_trigger.png %}
[15]: {% image_buster /assets/img/sms/campaign_trigger.png %}
[16]: {% image_buster /assets/img/sms/multi-language.png %}
