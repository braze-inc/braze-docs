---
nav_title: Manipulation des mots clés personnalisés
article_title: Manipulation des mots clés personnalisés
page_order: 2
description: "Cet article de référence traite de la manière dont Braze traite la messagerie SMS bidirectionnelle et les réponses automatiques. Cela inclut des explications sur le fonctionnement du déclenchement de mots clés ainsi que des catégories de mots clés personnalisées et le support multi-langage."
page_type: Référence
channel:
  - SMS
---

<br>
{% alert important %}
Êtes-vous actuellement un client SMS non-natif ? Si c'est le cas, veuillez visiter la [documentation SMS non-native](/docs/user_guide/message_building_by_channel/sms/non_native/) pour votre article de gestion des mots clés correspondants.
{% endalert %}

## Messagerie bidirectionnelle (réponses personnalisées aux mots-clés)

La messagerie bidirectionnelle vous permet d'envoyer des messages et de traiter les réponses à ces messages. Il faut que les utilisateurs envoient un mot clé à Braze, auquel cet utilisateur recevra une réponse automatique. Appliquée correctement, la messagerie bidirectionnelle peut être une solution simple, immédiate et dynamique pour le marketing de la clientèle, en économisant du temps et des ressources.

## Gestion des mots-clés et des réponses automatiques

SMS avec Braze vous donne la possibilité de créer des déclencheurs de mots-clés, des réponses personnalisées, de définir des ensembles de mots clés pour plusieurs langues, et d'établir des catégories de mots clés personnalisées.

{% tabs %}
{% tab Add Keyword Triggers %}

#### Ajouter des déclencheurs de mots clés

En plus des mots-clés opt-in et opt-out par défaut listés ci-dessus, vous pouvez également définir vos propres mots-clés pour déclencher les réponses Opt-In, Opt-Out et Help .

![Domicile]({% image_buster /assets/img/sms/keyword_edit2.png %}){: style="float:right;max-width:40%;margin-left:10px;"}
1. Pour définir vos propres mots clés, accédez à la section SMS du tableau de bord situé sous Groupes d'abonnement.<br><br>
2. Sous les mots clés globaux SMS, sélectionnez une catégorie de mots clés pour ajouter un mot clé en sélectionnant l'icône du crayon.<br><br>
3. Dans la boîte de dialogue qui apparaît, ajoutez un mot clé que vous souhaitez déclencher dans cette catégorie de mots-clés. Notez que les mots-clés sont sensibles à la casse, et les mots-clés universels comme `START`, `OUI`, et `UNSTOP` ne peuvent pas être changés. Veuillez lire les règles ci-dessous qui s'appliquent aux mots-clés et aux réponses par mots-clés.<br><br>![photo]({% image_buster /assets/img/sms/sms_keywords.png %})

| Mots clés                                                                                                                                                                                                                                                                                                                  | Réponses aux mots clés                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| - Caractères encodés UTF-8 valides<br>- Maximum de 20 mots-clés par catégorie au total<br>- Longueur maximale de 34 caractères<br>- Longueur minimale de 1 caractère <br>- Ne peut pas contenir d'espaces<br>- Requis pour être insensible à la casse et unique dans le groupe d'abonnements | - Ne peut pas être vide<br>- Longueur maximale de 300 caractères<br>- Caractères UTF-8 valides |
{: .reset-td-br-1 .reset-td-br-2}

{% alert tip %}
Intéressé par la façon dont ces mots-clés peuvent être utilisés dans vos campagnes et Canvases pour repérer et déclencher des messages ? Visitez notre [article de relocalisation par SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) pour plus d'informations.
{% endalert %}
{% endtab %}

{% tab Manage responses %}

#### Gérer les réponses

Vous pouvez gérer vos propres réponses qui sont envoyées aux utilisateurs après avoir écrit un mot clé dans une catégorie spécifique de mots-clés.

![Domicile]({% image_buster /assets/img/sms/keyword_edit2.png %}){: style="float:right;max-width:40%;margin-left:10px;"}
1. Pour gérer vos réponses par mots-clés, accédez à la section SMS du tableau de bord situé sous Groupes d'abonnement. <br><br>
2. Sous SMS Global Keywords, sélectionnez une catégorie de mots clés pour éditer une réponse en sélectionnant l'icône crayon.<br><br>
3. Dans la boîte de dialogue qui apparaît, modifiez et enregistrez votre réponse. Veuillez garder à l'esprit les [six règles pour être en conformité]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/#the-six-rules-to-get-compliance-right) lorsque vous créez votre réponse et lisez les règles ci-dessous qui s'appliquent aux mots-clés et aux réponses par mots-clés.<br><br>

![Réponses]({% image_buster /assets/img/sms/keyword_home.png %})

| Mots clés                                                                                                                                                                                                                                                                                                                  | Réponses aux mots clés                                                                                     |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| - Caractères encodés UTF-8 valides<br>- Maximum de 20 mots-clés par catégorie au total<br>- Longueur maximale de 34 caractères<br>- Longueur minimale de 1 caractère <br>- Ne peut pas contenir d'espaces<br>- Requis pour être insensible à la casse et unique dans le groupe d'abonnements | - Ne peut pas être vide<br>- Longueur maximale de 300 caractères<br>- Caractères UTF-8 valides |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

## Prise en charge multi-langues

Lors de l'envoi à certains pays, un expéditeur peut être requis pour supporter les mots-clés entrants et les réponses sortantes dans une langue locale. Pour cela, Braze vous permet de créer un paramètre de mot clé spécifique à la langue. !\[Envoi multi-langues\]\[16\]{: style="float:right;max-width:40%;margin-left:10px;"}

Pour commencer, cliquez sur **Ajouter une langue** et sélectionnez votre langue cible ou recherchez une langue dans le menu déroulant.

{% alert important %}
Notez que les autres langues ne sont pas fournies avec des mots-clés prédéfinis et des réponses comme l'anglais, ainsi les expéditeurs devront travailler avec leurs équipes de marketing et légales pour ajouter tous les mots-clés requis à cet ensemble. Sinon, Braze ne gérera pas les messages entrants localisés pour ces langues.
{% endalert %}

Si vous devez supprimer une langue, cliquez sur le bouton **Supprimer la langue** en bas à droite.

!\[Mots-clés Globaux SMS\]\[5\]

## Catégories de mots clés personnalisés

En plus des trois catégories de mots clés par défaut (opt-in, opt-out et aide), vous pouvez également créer jusqu'à 10 de vos propres catégories de mots-clés. Cela vous permet d'identifier des mots-clés arbitraires et de configurer des réponses spécifiques à votre entreprise. Un exemple de catégorie pourrait être "PROMO" ou "DISCOUNT", ce qui pourrait déclencher une réponse sur les promotions qui se déroulent ce mois-ci.

Ces mots-clés personnalisés fonctionnent dans une capacité "toujours", ce qui signifie que tout utilisateur abonné à votre service de message peut écrire des mots clés et recevoir une réponse à n'importe quel moment. En plus de ce comportement, vous avez également la possibilité de définir des mots-clés spécifiques qui ne peuvent être envoyés qu'à [certains points]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#lifecycle-specific-keywords) du cycle de vie de votre utilisateur.

!\[Exemple de Mots-clés\]\[12\]

### Créer une catégorie personnalisée

!\[Catégorie de mots-clés personnalisée\]\[13\]{: style="float:right;max-width:40%;margin-left:10px;"}

Pour créer une catégorie de mots clés personnalisés, éditez le groupe d'abonnement approprié, et cliquez sur **Ajouter une catégorie de mots clés personnalisés**. Ici, vous serez en mesure de fournir un nom de catégorie de mots-clés et de définir les mots-clés dans lesquels un utilisateur peut écrire pour recevoir le message de réponse.

Une fois créée, cette catégorie de mots-clés sera disponible pour [filtrer et déclencher]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) contre vos campagnes et vos Canvases.

Les mots-clés créés dans les catégories de mots-clés personnalisés adhèrent à toutes les règles et validations indiquées ci-dessus pour la création de nouveaux mots-clés.

### Mots-clés spécifiques au cycle de vie

Si vous avez un cas d'utilisation où vous souhaitez limiter quand un client peut envoyer un mot clé spécifique pendant son cycle de vie (par ex. lors de leur première intégration initiale) pour recevoir une réponse, vous pouvez utiliser le déclencheur "Envoyer les SMS entrants à un groupe d'abonnement dans la catégorie des mots clés AUTRE" dans votre campagne ou Canvas et définir des mots-clés ad hoc que vos utilisateurs peuvent envoyer à un moment donné. Ce déclencheur prend en charge le filtrage sur le message entrant spécifique en utilisant / n'est pas une comparaison du message, ainsi que les correspondances/ne correspondent pas aux règles regex pour valider l'entrée de l'utilisateur.

#### Toile

!\[Exemple\]\[14\]{: style="max-width:80%;"}

#### Campagnes

!\[Exemple de Campagne\]\[15\]{: style="max-width:80%;"}

### Traitement avec des mots-clés inconnus

Bien que ce ne soit pas obligatoire, nous recommandons fortement de configurer une réponse automatique lorsque les utilisateurs envoient des mots-clés SMS entrants qui ne correspondent pas à un mot clé existant. Ce message avertira l'utilisateur que le mot clé n'est pas reconnu et offre un certain conseil.

Cela peut être fait en créant une campagne SMS avec un message comme "Désolé! Nous n'avons pas reconnu ce mot clé, le texte STOP pour arrêter ou aider à l'aide." Ensuite, à l'étape de la livraison, sélectionnez **Action-Based Delivery** et utilisez le déclencheur **Envoyé SMS entrant vers le groupe d'abonnement dans la catégorie des mots clés AUTRE**.


![Confirmation par SMS]({% image_buster /assets/img/sms/sms_other.png %})

{% alert tip %}
Intéressé par la façon dont ces mots-clés et ces catégories de mots clés peuvent être utilisés dans vos campagnes et Canvases pour redimensionner et déclencher des messages ? Visitez notre [article de relocalisation par SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) pour plus d'informations.
{% endalert %}
[1]: {% image_buster /assets/img/sms/keyword_edit2.png %} [2]: {% image_buster /assets/img/sms/keyword_home.png %} [IMAGE2]: {% image_buster /assets/img/sms/sms_message_body. ng %} [5]: {% image_buster /assets/img/sms/multi-language2.png %} [12]: {% image_buster /assets/img/sms/sms_custom_keyword. ng %} [13]: {% image_buster /assets/img/sms/sms_custom_step.png %} [14]: {% image_buster /assets/img/sms/canvas_trigger. ng %} [15]: {% image_buster /assets/img/sms/campaign_trigger.png %} [16]: {% image_buster /assets/img/sms/multi-language.png %}
