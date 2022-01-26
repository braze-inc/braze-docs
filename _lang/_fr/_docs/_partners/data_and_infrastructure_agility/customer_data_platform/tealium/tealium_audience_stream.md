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

> Tealium [AudienceStream](https://community.tealiumiq.com/t5/Customer-Data-Hub/Introduction-to-AudienceStream/ta-p/16087) est un moteur de segmentation client Omnichannel et d'action en temps réel. AudienceStream prend les données qui affluent dans EventStream et crée des profils de visiteurs représentant les attributs les plus importants de l'engagement de vos clients avec votre marque.

L'intégration de Braze et de Tealium tire parti des profils des visiteurs de AudienceStream. Les comportements partagés segmentent ces profils pour créer des ensembles de visiteurs avec des traits communs, appelés auditoires. Ces auditoires peuvent aider à alimenter votre technologie de marketing en temps réel via des connecteurs.

{% alert important %}
Veuillez noter que Tealium AudienceStreams et EventStreams sont empilés selon les spécifications de Braze afin que nos clients ne courent pas le risque de dépasser la limite de taux [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Veuillez contacter le support [de Braze]({{site.baseurl}}/braze_support/) ou votre CSM si vous avez des questions.
{% endalert %}

## Pré-requis

| Nom                                  | Libellé                                                                                                                                                                                                                                  |
| ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte Tealium                       | Un [compte Tealium](https://my.tealiumiq.com/) avec accès au serveur et au côté client est requis pour tirer parti de ce partenariat.                                                                                                    |
| Clé API REST                         | Une clé d'API Braze REST avec les permissions `users.track` et `users.delete`. <br><br>Ceci peut être créé dans le **tableau de bord Braze** > **Console développeur** > **Clé d'API REST** > **Créer une nouvelle clé API** |
| [Point de terminaison REST Braze][6] | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL de Braze pour votre instance.                                                                                                                                |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Mettre en place des attributs et des badges

#### Comprendre les attributs

La première étape dans l'utilisation de AudienceStream est de créer des attributs. Les attributs vous permettent de définir les caractéristiques importantes qui représentent les habitudes, les préférences, les actions et l'engagement d'un visiteur avec votre marque.

**Attribut de Visite**: Les attributs de la visite sont liés à la visite actuelle (ou session) de l'utilisateur. Les données stockées dans ces attributs persistent pour la durée de la visite. Quelques exemples d'attributs de visite incluent :
- Durée de la visite (Nombre)
- Navigateur actuel (chaîne de caractères)
- Périphérique actuel (chaîne de caractères)
- Nombre de pages vues (Nombre)

**Attributs de Visiteur**: Les attributs de Visiteur se rapportent à l'utilisateur actuel. Les données stockées dans ces attributs persistent pour la durée de vie de l'utilisateur. Quelques exemples d'attributs de visiteur incluent :
- Valeur de la commande à vie (Nombre)
- Prénom (chaîne de caractères)
- Date de naissance (Date)
- Marques achetées (Tally)

Visitez [Tealium][1] pour une liste complète des types de données disponibles.

##### Enrichissement d'attributs

Une fois que vous avez identifié vos attributs, vous pouvez les configurer avec [enrichissements](https://community.tealiumiq.com/t5/Getting-Started-with/Attributes-Enrichments/ta-p/25786) - des règles métier qui déterminent quand et comment mettre à jour les valeurs des attributs. Chaque type de données offre sa propre sélection d'enrichissements pour manipuler la valeur de l'attribut. Ceci est associé au paramètre "WHEN". Les options suivantes sont disponibles pour chaque visite et chaque attribut visiteur :

- Nouveau Visiteur : se produit la première fois qu'un visiteur vient sur votre site.
- Nouvelle visite : se produit lors d'une nouvelle visite par un visiteur.
- N'importe quel événement : se produit sur n'importe quel événement.
- Visite terminée : se produit lorsqu'une visite se termine.

#### Badges

Les badges sont des attributs spéciaux de visiteurs qui représentent des modèles de comportement précieux. Les badges sont attribués ou retirés des visiteurs en fonction de la logique de leurs enrichissements. Cette logique combine généralement plusieurs conditions pour capturer des segments de visiteurs ou fixe un seuil pour quand une valeur particulière est atteinte.

#### Exemple d'attribut et de badge

{% tabs local %}
{% tab Attribute %}

En regardant l'attribut visiteur `Valeur de commande à vie`, cet attribut calcule le montant cumulé dépensé par le client pour toutes les commandes terminées. Pour configurer la valeur de votre commande à vie dans votre compte Tealium, suivez les instructions ci-dessous :

1. Naviguez vers **AudienceStream -> Attributs visiteur/Visiter** et cliquez sur **Ajouter un attribut**.
2. Sélectionnez la portée en tant que **Visiteur** et cliquez sur **Continuer**.
3. Sélectionnez le type de données **Number** et cliquez sur **Continuer**.
4. Entrez le nom de l'attribut, "Valeur de la commande à vie".
5. Cliquez sur **Ajouter une enrichissement** et sélectionnez **Incrément ou Decrement Number**.
6. Sélectionnez l'attribut contenant la valeur à incrémenter par (order_total).
7. Laisser le paramètre "QUEL" à "N'importe quel événement".
8. Cliquez sur **Enregistrer**, puis **Terminer**.

Maintenant, tous les clients auront un attribut à valeur de commande à vie qui leur est lié.

{% endtab %}
{% tab Badge %}

Vous pouvez créer des badges qui vous aident à classer et cibler vos utilisateurs par certains attributs qu'ils partagent. Pour l'exemple ci-dessous, nous créons un badge VIP pour les utilisateurs d'une valeur à vie de plus de 500 $.

1. Naviguez vers **AudienceStream > Visiteur/Visiter les Attributs** et cliquez sur **Ajouter un attribut**.
2. Sélectionnez la portée en tant que **Visiteur** et cliquez sur **Continuer**.
3. Sélectionnez le type de données **Badge** et cliquez sur **Continuer**.
4. Entrez le nom du badge, "VIP".
5. Cliquez sur **Ajouter une richesse** et sélectionnez **Assigner un badge**.
6. Créez une règle pour l'affectation des badges en sélectionnant **Créer une règle**. Assignez un titre à cette règle, et en utilisant l'attribut précédent créé, définissez la règle à ". attribut .has **Valeur de commande à vie supérieure à 500**".
7. Laisser le paramètre "QUEL" à "N'importe quel événement".
8. Cliquez sur **Enregistrer**, puis **Terminer**.

{% endtab %}
{% endtabs %}

### Étape 2 : Créer un public

À partir de la page d'accueil de Tealium, sélectionnez **Audience** sous **AudienceStream** du côté gauche de la page. Ici, vous pouvez créer un public d'utilisateurs avec les attributs communs que vous sélectionnez.

Premièrement, nommez votre public, puis prenez un peu de temps pour réfléchir à quels attributs seraient applicables pour le type de public que vous essayez de créer. Par exemple, pour créer un public de abandons de panier VIP, vous pouvez créer un public de visiteurs qui ont le badge **VIP** et le badge **Abandon du panier** assigné.

Assurez-vous de **Enregistrer / Publier** votre connecteur une fois terminé.

### Étape 3 : Créer un connecteur d'événement

Un connecteur est une intégration entre Tealium et un autre fournisseur utilisé pour transmettre des données. Ces connecteurs contiennent des actions qui représentent les API supportées par leur partenaire.

1. À partir de la barre latérale gauche dans Tealium sous **côté serveur**, accédez à **AudienceStream > Connecteurs d'audience**.
2. Sélectionnez le bouton bleu **+ Ajouter un connecteur** pour regarder à travers la place de marché du connecteur. Dans la nouvelle boîte de dialogue qui apparaît, utilisez la recherche de spotlight pour trouver le connecteur **Braze**.
3. Pour ajouter ce connecteur, cliquez sur la tuile du connecteur **Braze**. Une fois cliqué, vous pouvez consulter le résumé de la connexion et une liste des informations requises, des actions prises en charge et des instructions de configuration. La configuration comprend quatre étapes : source, configuration, action et résumé.

#### Source

Dans le dialogue **Source** qui apparaît, sélectionnez le public que vous avez créé à l'étape précédente et un déclencheur que vous estimez approprié à votre situation. Vous avez également la possibilité de basculer sur la limite de fréquence pour contrôler la fréquence de déclenchement de cette action.

#### Configuration

Ensuite, une boîte de dialogue **Configuration** apparaîtra. Sélectionnez **Ajouter un connecteur** au bas de la page. Nommez votre connecteur et fournissez votre point de terminaison API Braze et votre clé API REST Braze ici.

![Créer une configuration]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="largeur-max-70%;"}

Si vous avez créé un connecteur avant, vous pouvez optionnellement utiliser un connecteur existant dans la liste disponible et le modifier pour s'adapter à vos besoins avec l'icône crayon ou le supprimer avec l'icône de la corbeille.

Une fois que vous avez sélectionné un connecteur pour lier cet audience, cliquez sur **Terminé** pour continuer.

#### Action

Ensuite, nommez l'action de votre connecteur et sélectionnez un type d'action qui enverra des données en fonction du mapping que vous configurez. Ici, vous associerez les attributs Braze aux noms d'attributs de Tealium. Selon le type d'action que vous choisissez, il y aura une sélection variée de champs requis par Tealium. Voici des exemples et des explications de ces champs.

{% alert important %}
**Notez que tous les champs proposés ne sont pas obligatoires**. <br>Si vous souhaitez sauter un champ, Tealium vous demande **de le minimiser** avant de continuer à l'étape suivante.

![Minimize]({% image_buster /assets/img/tealium/minimize.gif %}){: style="largeur-max-80%"}
{% endalert %}

{% tabs local %}
{% tab Track User %}

Cette action vous permet de suivre les attributs des utilisateurs, des événements et des achats en une seule action.

| Paramètres                              | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Identifiant de l'utilisateur            | Utilisez ce champ pour associer le champ ID de l'utilisateur de Tealium à son équivalent Braze. <br><br>- L'ID externe et l'ID Braze ne doivent pas être spécifiés si l'importation de jetons push est importée.<br>- Si vous spécifiez un alias d'alias, le nom de l'alias et l'étiquette de l'alias doivent être définis. <br><br>Pour plus d'informations, consultez le Braze [/users/track endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Attributs de l'utilisateur              | Utilisez les noms de champs de profil utilisateur existants de Braze pour mettre à jour les valeurs de profil d'utilisateur dans le tableau de bord Braze ou ajoutez vos propres données personnalisées [d'attribut utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/) aux profils d'utilisateur.<br><br>- Par défaut, de nouveaux utilisateurs seront créés si on n'existe pas.<br>- En définissant **Mettre à jour uniquement** à `vrai`, seuls les utilisateurs existants seront mis à jour et aucun nouvel utilisateur ne sera créé.                                                                                                                                                                                                                                                                                                                                                                                                |
| Modifier les attributs de l'utilisateur | Utilisez ce champ pour incrémenter ou décrémenter certains attributs utilisateur<br><br>- Les attributs entiers peuvent être incrémentés par des entiers positifs ou négatifs.<br>- Les attributs d'un tableau peuvent être modifiés en ajoutant ou en supprimant des valeurs des tableaux existants.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Attributs de l'événement                | Un événement représente une seule occurrence d'un événement personnalisé par un utilisateur particulier à un horodatage. Utilisez ce champ pour suivre et cartographier les attributs d'événement comme ceux de l'objet [événement Braze]({{site.baseurl}}/api/objects_filters/event_object/). <br><br>- Attribut événement `Nom` est requis pour chaque événement associé.<br>- Attribut événement `Temps` est automatiquement défini à maintenant, sauf si explicitement associé. <br>- Par défaut, de nouveaux événements seront créés si on n'existe pas. En définissant `Update Existing Only` à `true`, seuls les événements existants seront mis à jour et aucun nouvel événement ne sera créé.<br>- Attributs de type tableau de carte pour ajouter plusieurs événements. Les attributs de type de tableau doivent être de longueur égale.<br>- Les attributs de valeur unique peuvent être utilisés et appliqués à chaque événement. |
| Attributs d'achat                       | Utilisez ce champ pour suivre et cartographier les attributs d'achat des utilisateurs comme ceux de l'objet d'achat [Braze]({{site.baseurl}}/api/objects_filters/purchase_object/).<br><br>- Attributs d'achat `ID Produit`, `La devise` et `le prix` sont requis pour chaque achat cartographié.<br>- L'attribut d'achat `Time` est automatiquement défini à maintenant, sauf si explicitement associé.<br>- Par défaut, de nouveaux achats seront créés si on n'existe pas. En définissant `Update Existing Only` à `true`, seuls les achats existants seront mis à jour et aucun nouvel achat ne sera créé.<br>- Attributs de type tableau de carte pour ajouter plusieurs articles d'achat. Les attributs de type de tableau doivent être de longueur égale.<br>- Les attributs de valeur unique peuvent être utilisés et s'appliqueront à chaque élément.                                                                                |
{: .reset-td-br-1 .reset-td-br-2}

![Suivre l'exemple d'utilisateur]({% image_buster /assets/img/tealium/track_user_example.jpg %}){: style="largeur-max-80%"}

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

Sélectionnez **Continuer**.

#### Summary

Voir le résumé du connecteur que vous avez créé. Si vous souhaitez modifier les options de votre choix, sélectionnez **Retour** pour modifier ou **Terminer** pour terminer.

Votre connecteur s'affiche maintenant dans la liste des connecteurs sur votre page d'accueil de Tealium.

Assurez-vous de **Enregistrer / Publier** votre connecteur une fois terminé. Les actions que vous avez configurées vont maintenant se déclencher lorsque les connexions de déclenchement seront atteintes.

### Étape 4 : Testez votre connecteur de Tealium

Une fois que votre connecteur est opérationnel, vous devriez le tester pour vous assurer qu'il fonctionne correctement. La façon la plus simple de tester ceci est d'utiliser le Tealium **Outil de traçage**.

1. Pour démarrer une nouvelle trace, sélectionnez **Trace** dans la barre latérale gauche sous les options **Server-Side**.
2. Examinez le journal en temps réel.
3. Vérifiez l'action que vous voulez valider en cliquant sur l'entrée **Actions Déclenchées** pour développer.
4. Recherchez l'action que vous souhaitez valider et afficher le statut du journal.

Pour des instructions plus détaillées sur l'implémentation de l'outil Trace de Tealium, consultez leur [documentation de traces][21].

## Surcharges de données potentielles

Il y a trois moyens primaires de frapper accidentellement les dépassements de données lors de l'intégration de Braze dans Tealium :

#### La journalisation des données est insuffisante
Tealium n'envoie pas les deltas de Braze des attributs de l'utilisateur. Par exemple, si vous avez une action EventStream qui suit le prénom d'un utilisateur et le numéro de téléphone cellulaire, Tealium enverra les trois attributs à Braze chaque fois que l'action est déclenchée. Tealium ne cherchera pas ce qui a changé ou a été mis à jour et n'enverra que cette information.<br><br> **Solution**: <br>Vous pouvez vérifier votre backend pour évaluer si un attribut a changé ou pas, et, le cas échéant, appelez les méthodes pertinentes de Tealium pour mettre à jour le profil de l’utilisateur. **C'est ce que font les utilisateurs qui intègrent Braze directement.** <br>**OU**<br> Si vous ne stockez pas votre propre version d'un profil utilisateur dans votre backend et ne pouvez pas dire si les attributs changent ou pas, vous pouvez utiliser AudienceStream pour suivre les changements d'attributs de l'utilisateur.

#### Envoi de données non pertinentes
Si vous avez plusieurs EventStreams qui ciblent le même flux d'événement, **toutes les actions activées pour ce connecteur** seront automatiquement déclenchées à chaque fois qu'une seule action est déclenchée, **cela pourrait aussi résulter en l'écrasement des données en Brésil.**<br><br> **Solution**: <br>Mettre en place une spécification d'événement séparée ou un flux pour suivre chaque action. <br>**OU**<br> Désactivez les actions (ou connecteurs) que vous ne voulez pas tirer en utilisant les interrupteurs du tableau de bord de Tealium.

#### Initialisation de Braze trop tôt
Les utilisateurs qui intègrent Tealium à l'aide de la balise Braze Web SDK peuvent assister à une augmentation spectaculaire de leur MAU. **Si Braze est initialisé au chargement de la page, Braze créera un profil anonyme chaque fois qu'un utilisateur navigue sur le site pour la première fois.** Certains peuvent ne vouloir suivre le comportement de l'utilisateur qu'une fois que les utilisateurs ont terminé une action, comme « Connecté » ou « Vidéo visionnée », pour abaisser leur nombre de MAU. <br><br> **Solution**: <br>Configurer des règles de charge pour déterminer exactement quand et où un tag se charge sur votre site. Vous pouvez en savoir plus sur les règles de charge et comment les configurer dans le [centre d'apprentissage de Tealium](https://community.tealiumiq.com/t5/Customer-Data-Hub/Building-an-Audience/ta-p/11881).
[15]: {% image_buster /assets/img/tealium/create_configuration.png %} [17]: {% image_buster /assets/img/tealium/save_publish.png %}

[1]: https://community.tealiumiq.com/t5/Getting-Started-with/Attributes/ta-p/25785
[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
[21]: https://community.tealiumiq.com/t5/Getting-Started-with/Trace/ta-p/25797