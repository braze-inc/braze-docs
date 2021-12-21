---
nav_title: Création d'une carte de contenu
article_title: Création d'une carte de contenu
page_order: 0
description: "Cet article de référence couvre la façon de créer, composer, configurer et envoyer des Cartes de Contenu à l'aide de campagnes Braze et de Canvases."
tool:
  - Toile
  - Campagnes
channel:
  - cartes de contenu
---

# Création d'une carte de contenu

Vous pouvez créer une Carte de Contenu à l'aide de la plateforme Braze à l'aide de campagnes et de Canvases.

## Création de la carte de contenu dans les campagnes et les toiles

{% tabs %}
{% tab Campaign %}

### Construire votre message

Naviguez vers la section **Campagne** du tableau de bord et cliquez sur __Créer une campagne__ pour ouvrir un nouvel assistant de messagerie pour votre carte de contenu. Ensuite, suivez le flux de l'assistant de messagerie pour créer et lancer rapidement votre carte de contenu.

![Créez votre carte de contenu]({% image_buster /assets/img/create-cc.gif %})

1. Nommez votre campagne quelque chose de clair et significatif.
2. Ajouter __Teams__ et __Tags__, si nécessaire.
  - Les balises facilitent la recherche et la création de rapports à partir de vos campagnes. Par exemple, lorsque vous utilisez [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/), vous pouvez filtrer par balises particulières.
3. Ajoutez et nommez autant de variantes que vous avez besoin pour cette campagne.
  - Vous pouvez choisir différentes plateformes, types de messages et mises en page pour chacune de vos variantes ajoutées.

{% alert tip %}
Si tous les messages de votre campagne vont être similaires ou ont le même contenu, écrivez votre message avant d'ajouter des variantes supplémentaires. Vous pouvez ensuite choisir **Copier de la variante** dans le menu déroulant **Ajouter une variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

### Configurez votre toile

Naviguez vers la page **Canvas** du tableau de bord et cliquez sur __Créer Canvas__ pour commencer à configurer votre Canevas. Ensuite, suivez le flux de l'assistant Canvas pour créer et lancer rapidement votre carte de contenu.

1. Nommez votre toile quelque chose de clair et de significatif.
2. Ajouter **Teams** et **Tags**, si nécessaire.
  - Les étiquettes rendent vos toiles faciles à trouver et à construire des rapports. Par exemple, lorsque vous utilisez [Report Builder]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/), vous pouvez filtrer par balises particulières.
3. Définissez vos événements de conversion. Canvas prend en charge jusqu'à quatre événements de conversion. Ces événements doivent être attribués lors de la création de Canvas et ne peuvent pas être modifiés une fois que Canvas a démarré.
4. Configurez votre **Schedule d'Entrée**. Canvas offre une entrée planifiée, basée sur l'action et déclenchée par API.
5. Sélectionnez votre **Audience d'Entrée**. Ici, vous pouvez déterminer qui entrera dans ce Canvas et les utilisateurs cibles par segments et filtres; ces conditions ne seront pas réévaluées à chaque étape. Dans ce dialogue, vous avez également la possibilité de sélectionner les contrôles d'entrée, par exemple permettre aux utilisateurs de ré-entrer ce canevas et de définir une limite d'entrée. Vous recevrez également automatiquement un instantané de ce à quoi ressemble cette population ciblée approximativement en ce moment.
6. Définissez vos **paramètres d'envoi**. Ici, vous pouvez définir les options d'envoi de messages pour toutes les étapes de Canvas. Certaines de ces options incluent la configuration des paramètres d'abonnement, l'ajustement de la limite de débit, le plafonnement de fréquence de basculement et plus encore.
7. Ajoutez une étape dans le constructeur de Canvas . Dans cette étape, cliquez sur **Messages** puis sélectionnez le canal de messagerie de la **Carte de contenu**. Ici, vous allez créer et configurer votre Carte de Contenu.<br>![Create Your Content Card]({% image_buster /assets/img/content_card.gif %}){: style="max-width:90%"}

Pour plus de détails sur la configuration et la configuration de votre Canvas, reportez-vous à [Créer un Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

{% endtab %}
{% endtabs %}

## Étape 1 : Spécifiez vos types de messages

### Types de messages

En savoir plus sur le comportement et l'apparence attendus de chacun de ces messages sur notre [page de détails créatifs]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/), ou en cliquant sur les types de messages liés dans les tables.

Ces types de cartes de contenu sont acceptés par les applications mobiles et par les applications web.

| Type de message                                                                                                              | Description du type                                                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [Classique]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#classic)                 | Cette carte a une mise en page simple avec un titre en gras, le texte du message et une image optionnelle qui se trouve à gauche du titre et du texte. Il est préférable d'utiliser une image carrée ou une icône avec la Carte Classique. |
| [Image sous-titrée]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#captioned-image) | Cette carte vous permet de présenter votre contenu avec copie et une image attrayant d'attention!                                                                                                                                          |
| [Bannière]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/#banner)                   | La Bannière Card vous permet d'obtenir une attention créative et de commande avec de l'espace pour les images, gifs et autres contenus non textuels.                                                                                       |
{: .reset-td-br-1 .reset-td-br-2}

## Étape 2 : Composer une carte de contenu

L'onglet Composer dans l'Assistant Campagne (situé dans l'assistant étape de Canvas) vous permet de modifier tous les aspects du contenu et du comportement de votre message.

!\[Composer une fiche de contenu\]\[24\]

Le contenu ici varie en fonction du type de message choisi lors de l'étape précédente, mais peut inclure n'importe laquelle des options ci-dessous :

| Contenus                 | Options                                                                                                        | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------ | -------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Langue                   | Consultez notre [liste complète des langues disponibles][18].                                                  | Cliquez sur __Ajouter des langues__ et sélectionnez les langues désirées dans la liste fournie. Ceci insérera Liquid dans votre message. Nous vous recommandons de sélectionner vos langues avant d'écrire votre contenu afin que vous puissiez renseigner votre texte où il appartient dans le Liquid.                                                                                                                                                             |
| Titre & Texte du message | Nous recommandons des titres et des messages clairs et concis.                                                 | Écrivez tout ce que vous voulez. Il n'y a pas de limites, mais plus vite vous pouvez recevoir votre message et faire cliquer, mieux c'est.                                                                                                                                                                                                                                                                                                                          |
| Image                    | Cliquez sur __Ajouter une image__ ou utilisez une URL d'image.                                                 | Le cas échéant, cliquez sur __Include Image__ ou __Upload Image__ et suivez les instructions présentées. Chaque type de message et plate-forme peut avoir ses propres proportions et exigences suggérées - assurez-vous de vérifier ce qui est avant de mettre en service ou de faire une image à partir de zéro ! <br> <br> Les champs de messages de carte de contenu sont limités à 2 kb de taille totale, comme indiqué dans la section ci-dessous. |
| Épinglage                | Une carte épinglée s'affichera en haut du flux d'un utilisateur et ne peut pas être rejetée par l'utilisateur. | Si plusieurs cartes dans le flux d'un utilisateur sont épinglées, les cartes épinglées s'afficheront dans l'ordre chronologique. Une fois qu'une carte a été envoyée, vous ne pouvez pas mettre à jour son option épinglée rétroactivement. Changer cette option après l'envoi d'une campagne n'affectera que les envois futurs.                                                                                                                                    |
| Comportement au clic     | Pour Android, iOS, ou Web : <br> __Rediriger vers l'URL Web__, __Lien Profond vers l'app__ ou __Aucun__. | Lorsque votre client clique sur un lien présenté dans la carte, votre lien peut l'approfondir dans votre application ou sur un autre site.                                                                                                                                                                                                                                                                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert warning %}
Les champs de message de la carte de contenu sont limités à 2 Ko dans la taille totale, calculée en ajoutant la taille d'octet des champs suivants : Titre, Message, URL de l'image, texte de lien, URL de lien et paire clé/valeur (noms + valeurs). Les messages qui dépassent cette taille ne seront pas envoyés. Notez que cela n'inclut pas la taille de l'image mais plutôt la longueur de l'URL de l'image.
{% endalert %}

{% alert note %}

Chaque utilisateur peut recevoir jusqu'à 100 cartes de contenu non expirées et non rejetées. Comme un utilisateur devient éligible pour plus de 100 cartes, Braze commencera à retirer les anciennes cartes de son flux, même si elles n'ont pas été lues.

{% endalert %}

## Étape 3 : Configurer les paramètres supplémentaires

Ajoutez [paires clé-valeur][19] à votre message, si nécessaire.

Vous pouvez utiliser des paires de valeur clé pour créer des catégories pour vos cartes, créer plusieurs fils de cartes de contenu ([Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/multiple_feeds/), [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/multiple_feeds/), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/multiple_feeds/), et personnaliser le tri des cartes.

## Étape 4 : Construisez le reste de votre campagne ou Canvas

{% tabs %}
{% tab Campaign %}

Construisez le reste de votre campagne; consultez les sections ci-dessous pour plus de détails sur la meilleure façon d'utiliser nos outils pour construire des Cartes de Contenu.

#### Choisissez le calendrier de livraison ou le déclencheur

- Les cartes de contenu peuvent être livrées en fonction d'une heure planifiée, d'une action, ou en fonction d'un déclencheur API.
- Vous pouvez également définir la durée de la campagne et les heures tranquilles dans cette étape.
- Déterminer l'expiration de la carte de contenu. Définissez une date d'expiration spécifique ou les jours jusqu'à ce qu'une carte expire, jusqu'à 30 jours. Toutes les variantes ont des dates d'expiration identiques.
- Le plafonnement de fréquence ne s'applique pas aux cartes de contenu.

#### Choisir le segment cible

- Ensuite, vous devez choisir le segment cible dans le menu déroulant.
- Vous recevrez automatiquement un instantané de ce à quoi ressemble cette population approximative de segments.
- Gardez à l'esprit que l'adhésion exacte au segment est toujours calculée juste avant l'envoi du message.

#### Choisir les événements de conversion

- Braze vous permet de suivre la fréquence à laquelle les utilisateurs effectuent des actions spécifiques (c'est-à-dire des événements de conversion) après avoir reçu une campagne.
- Vous avez la possibilité d'autoriser jusqu'à une fenêtre de 30 jours au cours de laquelle une conversion sera comptée si l'utilisateur prend l'action spécifiée.

Une fois que vous avez terminé la construction de la dernière de votre campagne, révisez ses détails, [testez-la]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/testing/), puis envoyez-la !

{% alert warning %}
Une fois qu'une carte de contenu est lancée, elle ne peut pas être modifiée. Il ne peut qu'être empêché d'envoyer aux nouveaux utilisateurs et supprimé des flux d'utilisateurs.
{% endalert %}

{% endtab %}

{% tab Canvas %}

Complétez les sections restantes de votre étape sur Canvas ; voir les sections ci-dessous pour plus de détails sur la meilleure façon d'utiliser nos outils pour construire des cartes de contenu. Après avoir créé et configuré votre étape, Consultez notre [Documentation sur le Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) pour plus de détails sur la façon de construire le reste de votre Canvas, implémentez des tests multivariés et une sélection intelligente, et plus encore.

#### Choisir le calendrier des étapes

- Les cartes de contenu peuvent être livrées en fonction de l'heure programmée ou de l'action sur Canvas

#### Choisir un public

- Ensuite, vous devez régler les options de l'audience pour cette étape. Ici, vous pouvez affiner davantage les destinataires de cette étape en spécifiant des segments et en ajoutant des filtres supplémentaires. Les options de l'audience seront vérifiées après le délai, au moment où les messages sont envoyés.

#### Choisir le comportement d'avancement

- Enfin, sélectionnez votre comportement d'avancement pour cette étape. Ici, vous pouvez choisir soit "Avancer lorsque le message est envoyé" qui fait passer vos utilisateurs aux étapes suivantes lorsque la Carte de Contenu est envoyée, ou « Audience immédiatement avancée » qui avise les utilisateurs lorsque soit la Carte de Contenu est envoyée, soit la Carte de Contenu n'a pas été envoyée parce qu'elle a été abandonnée.
- Pour en savoir plus sur le comportement de l'avancement de Canvas , consultez la [Documentation sur Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/?redirected=true).

Une fois que vous avez fini de construire votre Canvas Step, passez en revue ses détails et [testez-le]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/testing/)!

{% endtab %}
{% endtabs %}

## Choses à savoir

### Capacités non encore prises en charge

Les fonctionnalités suivantes ne sont pas encore supportées pour les cartes de contenu :
- Bons de réduction
- Plafond de fréquence
- Réordonner les Cartes de Contenu de Braze
- Modifications post-lancement


### Comportement d'envoi

Une fois que les Cartes de Contenu ont été envoyées, comme les e-mails, elles restent en attente dans une "boîte de réception" prête à être envoyée à l'utilisateur. Une fois que le contenu est intégré à la Carte de Contenu (au moment de l'affichage), le contenu ne peut pas être modifié au cours de sa durée. Cela s'applique même si vous appelez une API via le contenu connecté, et les données à partir du point de terminaison changent ; ces données ne seront pas mises à jour. Il ne peut qu'être empêché d'envoyer aux nouveaux utilisateurs et supprimé des flux d'utilisateurs. Si vous modifiez une campagne, seules les __futures__ cartes envoyées auront la mise à jour.

Si vous avez besoin de supprimer les anciennes cartes, vous devez arrêter la campagne pour le faire. Cela peut être fait en naviguant vers votre campagne de carte de contenu et en sélectionnant `Stop Campaign`. L'arrêt de la campagne affiche l'invite affichée ci-dessous. Si vous souhaitez supprimer les Cartes de Contenu, cochez la case pour supprimer toutes les cartes qui ont été envoyées. Cela rendra la carte cachée par le SDK lors de la prochaine synchronisation.

!\[Carte de contenu\]\[25\]

### Événements de suppression de carte {#action-based-card-removal}

Certaines Cartes de Contenu ne sont pertinentes que jusqu'à ce qu'un utilisateur effectue une action. Par exemple, une carte incitant les utilisateurs à activer leur compte ne devrait pas être affichée une fois que l'utilisateur a terminé cette tâche d'intégration.

Dans une campagne ou Canvas Message, vous pouvez éventuellement ajouter un __Événement de suppression__ pour spécifier quels événements ou achats personnalisés devraient entraîner la suppression des cartes précédemment envoyées du flux de cet utilisateur ; déclenchée via SDK ou REST API.

{% alert tip %}
Vous pouvez spécifier plusieurs événements personnalisés et achats qui devraient supprimer une carte du flux d'un utilisateur. Une fois que **n'importe quelle** de ces actions sont effectuées par l'utilisateur, toutes les cartes existantes envoyées par les cartes de la campagne seront supprimées. Les futures cartes éligibles continueront d'être envoyées selon le calendrier du message.
{% endalert %}

![Événement de suppression de carte de contenu]({% image_buster /assets/img/content_cards/content_card_removal_event.png %})

### Mise à jour des cartes déjà envoyées

Si vous trouvez que vous devez apporter des modifications aux cartes qui ont déjà été envoyées:

1. Arrêter votre campagne
2. Supprimer les cartes de contenu actives des flux d'utilisateurs
3. Modifier votre campagne si nécessaire
4. Redémarrez votre campagne
[24]: {% image_buster /assets/img/content_card_compose.png %} [25]: {% image_buster /assets/img/cc_remove.png %}

[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported
[19]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/
