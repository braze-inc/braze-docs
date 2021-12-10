---
nav_title: Flux auditif de Tealium
article_title: Flux auditif de Tealium
page_order: 2.1
alias: /fr/partners/tealium_audience_stream/
description: "Cet article décrit le partenariat entre Braze et Tealium, un hub de données universel qui vous permet de connecter des données mobiles, Web et alternatives à d'autres sources tierces."
page_type: partenaire
search_tag: Partenaire
---

# Flux auditif de Tealium

> Tealium AudienceStream est un moteur de segmentation client Omnichannel et d'action en temps réel. AudienceStream prend les données qui affluent dans EventStream et crée des profils de visiteurs qui représentent les attributs les plus importants de l'engagement de vos clients avec votre marque.

Les profils de visiteurs de Tealium AudienceStream sont segmentés par des comportements partagés pour créer des audiences, des ensembles de visiteurs avec des traits communs. Ces auditoires alimentent votre technologie de marketing en temps réel via des connecteurs. Pour plus d'informations sur AudienceStream, consultez la documentation de Tealium [ici](https://community.tealiumiq.com/t5/Customer-Data-Hub/Introduction-to-AudienceStream/ta-p/16087).

## Pré-requis

| Nom                                         | Libellé                                                                                                                                                                                                                 |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Clé API REST                                | Une clé API Braze REST avec les permissions `users.track`. <br><br>Ceci peut être créé dans le __tableau de bord Braze__ -> __Console développeur__ -> __Clé d'API REST__ -> __Créer une nouvelle clé API__ |
| Compte Tealium & Informations sur le compte | Vous devez avoir un compte Tealium actif avec un accès côté serveur et client pour utiliser AudienceStream avec Braze.                                                                                                  |
| [Point de terminaison REST Braze][6]        | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL de Braze pour votre instance.                                                                                                               |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Veuillez noter que Tealium AudienceStreams et EventStreams sont empilés selon les spécifications de Braze afin que nos clients ne courent pas le risque de dépasser la limite de taux [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Veuillez contacter le support [de Braze]({{site.baseurl}}/braze_support/) ou votre CSM si vous avez des questions.
{% endalert %}

## Étape 1 : Mettre en place des attributs et des badges

### Comprendre les attributs

La première étape dans l'utilisation de AudienceStream est de créer des attributs. Les attributs vous permettent de définir les caractéristiques importantes qui représentent les habitudes, les préférences, les actions et l'engagement d'un visiteur avec votre marque.

__Attribut de visite__: Les attributs de la visite sont liés à la visite (ou session) en cours de l'utilisateur. Les données stockées dans ces attributs persistent pour la durée de la visite. Quelques exemples d'attributs de visite :
- Durée de la visite (Nombre)
- Navigateur actuel (chaîne de caractères)
- Périphérique actuel (chaîne de caractères)
- Nombre de pages vues (Nombre)

__Attributs de Visiteur__: Les attributs de Visiteur se rapportent à l'utilisateur actuel. Les données stockées dans ces attributs persistent pour la durée de vie de l'utilisateur. Quelques exemples d'attributs de visiteur seraient:
- Valeur de la commande à vie (Nombre)
- Prénom (chaîne de caractères)
- Date de naissance (Date)
- Marques achetées (Tally)

Pour consulter une liste complète des types de données, consultez cette [documentation de Tealium][1].

### Enrichissement d'attributs

Une fois que vous avez identifié vos attributs, vous pouvez les configurer avec des enrichissements - des règles métier qui déterminent quand et comment mettre à jour les valeurs des attributs. Chaque type de données offre sa propre sélection d'enrichissements pour manipuler la valeur de l'attribut. Ceci est associé au paramètre "WHEN". Les options suivantes sont disponibles pour chaque visite et chaque attribut visiteur :

- Nouveau visiteur – se produit la première fois qu'un visiteur arrive sur votre site
- Nouvelle visite - se produit lors d'une nouvelle visite par un visiteur
- N'importe quel événement - se produit sur n'importe quel événement
- Visite terminée - se produit quand une visite se termine

### Badges

Les badges sont des attributs spéciaux de visiteurs qui représentent des modèles de comportement intéressants. Les badges sont attribués ou retirés des visiteurs en fonction de la logique de leurs enrichissements. Cette logique combine généralement plusieurs conditions en une seule pour capturer des segments de visiteurs ou fixe un seuil pour quand une valeur particulière est atteinte.

### Exemple d'attribut et de badge

{% tabs local %}
{% tab Attribute %}

En regardant l'attribut visiteur `Valeur de commande à vie`, cet attribut visiteur calcule le montant cumulé dépensé par le client pour toutes les commandes terminées. Pour configurer la valeur de votre commande à vie dans votre compte Tealium, suivez les instructions ci-dessous.

1. Naviguez vers __AudienceStream -> Attributs visiteur/Visiter__ et cliquez sur __Ajouter un attribut__.
2. Sélectionnez la portée en tant que __Visiteur__ et cliquez sur __Continuer__.
3. Sélectionnez le type de données __Number__ et cliquez sur __Continuer__.
4. Entrez le nom de l'attribut, "Valeur de la commande à vie".
5. Cliquez sur __Ajouter une enrichissement__ et sélectionnez __Incrément ou Decrement Number__.
6. Sélectionnez l'attribut contenant la valeur à incrémenter par (order_total).
7. Laisser le paramètre "QUEL" à "N'importe quel événement".
8. Cliquez sur __Enregistrer__, puis __Terminer__.

Maintenant, tous les clients auront un attribut à valeur de commande à vie qui leur est lié.

{% endtab %}
{% tab Badge %}

Ensuite, vous pouvez créer des badges qui vous aideront à classer et cibler vos utilisateurs par certains attributs qu'ils partagent. Pour l'exemple ci-dessous, nous allons créer un badge VIP pour les utilisateurs qui ont une valeur à vie de plus de 500 $.

1. Naviguez vers __AudienceStream -> Attributs visiteur/Visiter__ et cliquez sur __Ajouter un attribut__.
2. Sélectionnez la portée en tant que __Visiteur__ et cliquez sur __Continuer__.
3. Sélectionnez le type de données __Badge__ et cliquez sur __Continuer__.
4. Entrez le nom du badge, "VIP".
5. Cliquez sur __Ajouter une richesse__ et sélectionnez __Assigner un badge__.
6. Créez une règle pour l'affectation des badges en sélectionnant __Créer une règle__.
7. Assignez un titre à cette règle, et en utilisant l'attribut précédent créé, définissez la règle à ". Attribut .has __Valeur de commande à vie supérieure à 500__"
8. Laisser le paramètre "QUEL" à "N'importe quel événement".
9. Cliquez sur __Enregistrer__, puis __Terminer__.

{% endtab %}
{% endtabs %}

Pour en savoir plus sur les attributs et les badges, consultez la [documentation de Tealium](https://community.tealiumiq.com/t5/Getting-Started-with/Attributes-Enrichments/ta-p/25786).

## Étape 2 : Créer un public

À partir de la page principale du concentrateur de données client de Tealium, sélectionnez __Public__ sous __AudienceStream__ du côté gauche de la page. Ici, vous serez en mesure de créer un public d'utilisateurs qui ont des attributs communs que vous sélectionnez.

Tout d'abord, nommez votre public, puis prenez un peu de temps pour réfléchir à quel type d'attributs serait applicable pour le type d'audience que vous essayez de créer. Par exemple, pour créer un public de abandons de panier VIP, vous pouvez créer un public de visiteurs qui ont le badge VIP ____ un badge __Abandon du panier__ assigné.

## Étape 3 : Créer un connecteur d'audience

À partir de la page principale, sélectionnez __Connecteur Audience__ sous __AudienceStream__. Ici, vous pouvez créer et configurer votre connecteur. À partir de la page Connecteur d'audience, sélectionnez __+ Ajouter un connecteur__, rechercher __Braze__, et sélectionner __Braze__ comme type de connecteur.

### Sélectionner la source

Dans la nouvelle fenêtre qui apparaît, vous pourrez maintenant sélectionner le public que vous avez créé à l'étape précédente. en plus de sélectionner un déclencheur que vous estimez approprié à votre situation. Vous avez également la possibilité de basculer sur la limite de fréquence pour contrôler la fréquence de déclenchement de cette action.

### Configuration

!\[Create Configuration\]\[15\]{: style="float:right;max-width:30%;margin-left:15px;margin-bottom:15px;"}

Ensuite, une boîte de dialogue __Configuration__ apparaîtra. Ici, vous devez sélectionner __Ajouter un connecteur__ et renseigner certaines valeurs demandées par Tealium et Braze:

Si vous avez créé un connecteur avant, vous pouvez optionnellement utiliser un connecteur existant dans la liste disponible et le modifier pour s'adapter à vos besoins avec l'icône crayon ou le supprimer avec l'icône de la corbeille.

Une fois que vous avez sélectionné un connecteur pour relier ce public pour cliquer sur Terminé et continuer.

### Action

Ensuite, vous devez sélectionner une action de connecteur. Une action de connecteur envoie des données en fonction du mapping que vous configurez. Le connecteur Braze vous permet de mapper les attributs de Braze aux noms d'attributs de Tealium.

1. Dans la boîte de dialogue __Action__ , sélectionnez l'une des actions à mettre en place.
2. Selon l'action que vous avez choisie, il y aura une sélection variée de champs requis par Tealium. Voici des exemples et des explications de ces champs.

{% alert important %}
__Notez que tous les champs proposés ne sont pas obligatoires__. <br>Si vous souhaitez sauter un champ, Tealium vous demande __de le minimiser__ avant de continuer à l'étape suivante.

![Minimize]({% image_buster /assets/img/tealium/minimize.gif %}){: style="largeur-max-80%"}
{% endalert %}

{% tabs local %}
{% tab Track User %}

Cette action vous permet de suivre les attributs des utilisateurs, des événements et des achats en une seule action.

| Paramètres                              | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Identifiant de l'utilisateur            | Utilisez ce champ pour associer le champ ID de l'utilisateur de Tealium à son équivalent Braze. <br><br>- Si l'importation de Push Tokens, ID externe et ID Braze ne doit pas être spécifiée.<br>- Si vous spécifiez un alias utilisateur, le nom d'alias et l'étiquette d'alias doivent tous deux être définis. <br><br>Pour plus d'informations, consultez le Braze [/users/track endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Attributs de l'utilisateur              | Utilisez les noms de champs de profil utilisateur existants de Braze pour mettre à jour les valeurs de profil d'utilisateur dans le tableau de bord Braze ou ajoutez vos propres données d'attributs personnalisés aux profils d'utilisateurs.<br><br>- Par défaut, les nouveaux utilisateurs seront créés si on n'existe pas.<br>- En définissant `Mettre à jour uniquement` à `vrai` seuls les utilisateurs existants seront mis à jour et aucun nouvel utilisateur ne sera créé.<br><br>Pour en savoir plus sur l'objet Attributs d'utilisateur, consultez notre documentation []({{site.baseurl}}/api/objects_filters/user_attributes_object/)                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Modifier les attributs de l'utilisateur | Utilisez ce champ pour incrémenter ou décrémenter certains attributs utilisateur<br><br>- Les attributs entiers peuvent être incrémentés par des entiers positifs ou négatifs.<br>- Les attributs d'un tableau peuvent être modifiés en ajoutant ou en supprimant des valeurs des tableaux existants.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Attributs de l'événement                | Un événement représente une seule occurrence d'un événement personnalisé par un utilisateur particulier à la valeur horaire désignée. Utilisez ce champ pour suivre et cartographier les attributs d'événement comme ceux de l'objet Braze. <br><br>- Attribut d'événement `Nom` est requis pour chaque événement associé.<br>- Attribut événement `Temps` est automatiquement défini à maintenant, sauf si explicitement associé. <br>- Par défaut, de nouveaux événements seront créés si on n'existe pas. En définissant `Mettre à jour uniquement` à `true` seuls les événements existants seront mis à jour et aucun nouvel événement ne sera créé.<br>- Attributs de type tableau de carte pour ajouter plusieurs événements. Les attributs de type de tableau doivent être de longueur égale.<br>- Les attributs de valeur unique peuvent être utilisés et s'appliqueront à chaque événement.<br><br>Pour en savoir plus sur l'objet événement de Braze, consultez notre [documentation]({{site.baseurl}}/api/objects_filters/event_object/). |
| Attributs d'Achat                       | Utilisez ce champ pour suivre et cartographier les attributs d'achat des utilisateurs comme ceux de l'objet Achat Braze.<br><br>- Attributs d'achat `ID Produit`, `La devise` et `le prix` sont requis pour chaque achat cartographié.<br>- Attribut d'achat `Temps` est automatiquement réglé sur maintenant, à moins qu'il ne soit explicitement associé.<br>- Par défaut, de nouveaux achats seront créés si on n'existe pas. En définissant `Mettre à jour uniquement` à `vrai` seuls les achats existants seront mis à jour et aucun nouvel achat ne sera créé.<br>- Attributs de type Tableau de carte pour ajouter plusieurs articles d'achat. Les attributs de type de tableau doivent être de longueur égale.<br>- Les attributs de valeur unique peuvent être utilisés et s'appliqueront à chaque élément.<br><br>Pour en savoir plus sur l'objet d'achat de Braze, consultez notre [documentation]({{site.baseurl}}/api/objects_filters/purchase_object/)                                                                                 |
{: .reset-td-br-1 .reset-td-br-2}

![Suivre l'exemple d'utilisateur]({% image_buster /assets/img/tealium/track_user_example.jpg %}){: style="largeur-max-70%"}

{% endtab %}
{% tab Delete User %}

Cette action vous permet de supprimer des utilisateurs du tableau de bord Braze.

| Paramètres                   | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Identifiant de l'utilisateur | Utilisez ce champ pour associer le champ ID de l'utilisateur de Tealium à son équivalent Braze. <br><br>- Mapper un ou plusieurs identifiants d'utilisateur. Lorsque plusieurs identifiants sont spécifiés, la première valeur non vide est choisie en fonction de l'ordre de priorité suivant : ID externe, ID Braze, Nom d'alias & Étiquette d'alias.<br>- Lorsque vous spécifiez un alias utilisateur, le nom d'alias et l'étiquette d'alias doivent tous deux être définis.<br><br>Pour plus d'informations, voir le Braze [/users/delete endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/). |
{: .reset-td-br-1 .reset-td-br-2}

![Supprimer les utilisateurs]({% image_buster /assets/img/tealium/track_user_delete.png %}){: style="largeur-max-70%"}

{% endtab %}
{% endtabs %}

Sélectionnez __Continuer__.

### Enregistrer et publier
!\[Save/Publish\]\[17\]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"} Les actions que vous avez configurées vont maintenant se déclencher lorsque les connexions de déclenchement sont satisfaites. Les données se remplissent en temps réel à mesure que chaque action se déclenche.

## Étape 4 : Testez votre connecteur de Tealium

Une fois que votre connecteur est opérationnel, vous devriez le tester pour vous assurer qu'il fonctionne correctement. La façon la plus simple de tester ceci est d'utiliser le Tealium __Outil de traçage__.

1. Commencer une nouvelle trace. Cela peut être fait en sélectionnant Trace dans la barre latérale gauche dans les options `côté serveur`.
2. Examinez le journal en temps réel.
3. Vérifiez l'action que vous voulez valider en cliquant sur __Actions Déclenchées__ entrée pour développer.
4. Recherchez l'action que vous souhaitez valider et afficher le statut du journal.

Pour des instructions plus détaillées sur la façon d'implémenter l'outil Trace de Tealium, consultez leur [documentation Trace][21].

## Surcharges de données potentielles

Il y a trois moyens primaires de frapper accidentellement les surages de données lors de l'intégration de Braze dans Tealium.

#### __La journalisation des données est insuffisante__
Tealium n'envoie pas les deltas de Braze des attributs de l'utilisateur. Par exemple, si vous avez une action EventStream qui suit le prénom d'un utilisateur et le numéro de téléphone cellulaire, Tealium enverra les trois attributs à Braze chaque fois que l'action est déclenchée. Tealium ne cherchera pas ce qui a changé ou a été mis à jour et n'enverra que cette information.<br><br> __Solution__: <br>Vous pouvez vérifier votre propre backend pour évaluer si un attribut a changé ou non et dans l'affirmative, appeler les méthodes pertinentes de Tealiums pour mettre à jour le profil de l’utilisateur. __C'est ce que font les utilisateurs qui intègrent Braze directement.__ <br>__OR__<br> Si vous ne stockez pas votre propre version d'un profil utilisateur dans votre backend, et ne peut pas dire si les attributs changent ou pas, vous pouvez utiliser AudienceStream pour suivre les changements d'attribut utilisateur.

#### __Envoi de données non pertinentes__
Si vous avez plusieurs EventStream qui ciblent le même flux d'événement, __toutes les actions activées pour ce connecteur__ seront automatiquement déclenchées à chaque fois qu'une seule action est déclenchée, __cela pourrait aussi résulter en l'écrasement des données en Brésil. _<br><br> __Solution__: <br>Configurez une spécification d'événement séparée ou un flux pour suivre chaque action. <br>__OR__<br> Désactivez les actions (ou connecteurs) que vous ne voulez pas tirer en utilisant les commutateurs du tableau de bord de Tealium.

#### __Initialisation de Braze trop tôt__
Les utilisateurs qui intègrent Tealium à l'aide de Braze Web SDK Tag peuvent assister à une augmentation spectaculaire de leur MAU. __Si Braze est initialisé au chargement de la page, Braze créera un profil anonyme chaque fois qu'un utilisateur navigue sur le site pour la première fois.__ Certains peuvent ne vouloir suivre le comportement de l'utilisateur qu'une fois que les utilisateurs ont terminé une action, comme « Connecté » ou « Vidéo visionnée » afin de réduire leur nombre de MAU. <br><br> __Solution__: <br>Configurer des règles de charge pour déterminer exactement quand et où un Tag se charge sur votre site. Vous pouvez en savoir plus sur les règles de chargement et comment les configurer dans le [Tealium Learning Center](https://community.tealiumiq.com/t5/Customer-Data-Hub/Building-an-Audience/ta-p/11881).
[15]: {% image_buster /assets/img/tealium/create_configuration.png %} [17]: {% image_buster /assets/img/tealium/save_publish.png %}


[1]: https://community.tealiumiq.com/t5/Getting-Started-with/Attributes/ta-p/25785
[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
[21]: https://community.tealiumiq.com/t5/Getting-Started-with/Trace/ta-p/25797