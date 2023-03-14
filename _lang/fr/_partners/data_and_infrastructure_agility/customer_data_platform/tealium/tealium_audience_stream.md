---
nav_title: Tealium AudienceStream
article_title: Tealium AudienceStream
page_order: 2.1
alias: /partners/tealium_audience_stream/
description: "Cet article présente le partenariat entre Braze et Tealium, un hub de données universel qui vous permet de connecter des données mobiles, Web ou autres à d’autres sources tierces."
page_type: partner
search_tag: Partenaire

---

# Tealium AudienceStream

> Tealium [AudienceStream](https://community.tealiumiq.com/t5/Customer-Data-Hub/Introduction-to-AudienceStream/ta-p/16087) est un moteur de segmentation client omnicanal et d’action en temps réel. AudienceStream extrait les données qui affluent dans EventStream et crée des profils de visiteurs qui représentent les attributs les plus importants concernant l’engagement de vos clients envers votre marque. 

L’intégration de Braze et de Tealium tire parti des profils visiteur d’AudienceStream. Les comportements partagés segmentent ces profils pour créer des ensembles de visiteurs avec des caractéristiques communes, connus sous le nom d’audiences. Ces audiences peuvent vous aider à alimenter votre pile de technologie marketing en temps réel grâce à des connecteurs. 

{% alert important %}
Les AudienceStreams et EventStreams de Tealium offrent des actions de connecteurs par lot et sans lots. Le connecteur sans lots doit être utilisé lorsque des demandes en temps réel sont importantes pour le cas d’utilisation et qu’il n’y a aucun risque d’atteindre la limite de débit d’API de Braze. Si vous avez des questions, contactez le [service d’assistance]({{site.baseurl}}/braze_support/) de Braze ou votre gestionnaire du succès des clients. 
{% endalert %}

## Conditions préalables

| Nom | Description |
| ---- | ----------- |
| Compte Tealium | Un [Compte Tealium](https://my.tealiumiq.com/) avec un accès côté serveur est requis. Nous vous recommandons également d’utiliser des intégrations côté client pour profiter de ce partenariat. |
| Clé API REST | Une clé API REST Braze avec des autorisations `users.track`, `users.delete` et `subscription.status.set`.<br><br>Pour créer une clé API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé API REST) > Create New API Key (Créer une nouvelle clé API)**|
| [Endpoint REST de Braze][6] | URL de votre endpoint REST. Votre endpoint dépendra de [l’URL Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Configurer des attributs et des badges

#### Comprendre les attributs

Pour utiliser AudienceStream, la première étape consiste à créer des attributs. Les attributs vous permettent de définir les caractéristiques importantes qui représentent les habitudes, préférences, actions et engagements d’un visiteur par rapport à votre marque. 

**Attributs de visite** : Les attributs de visite sont liés à la visite (ou session) actuelle de l’utilisateur. Les données stockées dans ces attributs sont conservées pendant toute la durée de la visite. Voici quelques exemples d’attributs de visite :
- Durée de la visite (chiffre)
- Navigateur actuel (chaîne de caractère)
- Appareil actuel (chaîne de caractère)
- Nombre de pages visitées (chiffre)

**Attributs de visiteur** : Les attributs de visiteur sont liés à l’utilisateur actuel. Les données stockées dans ces attributs sont conservées pendant toute la durée de vie de l’utilisateur. Voici quelques exemples d’attributs de visiteur : 
- Valeur de la commande à vie (chiffre)
- Prénom (chaîne de caractères)
- Date de naissance (date)
- Achats et marques (décompte)

Rendez-vous sur le site Web de [Tealium][1] pour obtenir la liste complète des types de données disponibles.

##### Enrichissement des attributs

Après avoir trouvé les attributs souhaités, vous pouvez les configurer avec des [enrichissements](https://community.tealiumiq.com/t5/Getting-Started-with/Attributes-Enrichments/ta-p/25786), c’est-à-dire des règles métier qui déterminent quand et comment mettre à jour les valeurs des attributs. Chaque type de données comprend ses propres enrichissements pour manipuler la valeur de l’attribut. Cela est associé au paramètre « WHEN (QUAND) ». Les options suivantes sont disponibles pour chaque attribut de visite et de visiteur :

- Nouveau visiteur : survient la première fois qu’un visiteur consulte votre site.
- Nouvelle visite : se produit lorsqu’un visiteur fait une nouvelle visite.
- Tout événement : se produit pour tout événement.
- Visite terminée : se produit lorsqu’une visite se termine.

Vous pouvez également créer une condition personnalisée, appelée règle, qui déterminera la date à laquelle l’enrichissement aura lieu.

#### Badges

Les badges sont des attributs de visiteur spéciaux qui représentent des modèles de comportement précieux. Les badges sont attribués aux visiteurs ou retirés en fonction de la logique de leurs enrichissements. Cette logique associe généralement plusieurs conditions pour collecter des segments de visiteurs ou définit un seuil pour déterminer à quel moment une valeur donnée est atteinte.

#### Exemple d’attributs et de badges

{% tabs local %}
{% tab Attribute %}

Créez un attribut visiteur « Lifetime Order Value (Valeur des commandes à vie) » qui calcule le montant cumulé dépensé (`order_total`) par le client pour toutes les commandes terminées (événement d’achat). Suivez les instructions ci-dessous pour configurer la valeur des commandes à vie dans votre compte Tealium :

1. Accédez à **AudienceStream > Visitor/Visit Attributes (Attributs visiteur/visite)** et cliquez sur **Add Attribute (Ajouter un attribut)**.
2. Sélectionnez la portée comme **Visitor (Visiteur)**, puis cliquez sur **Continue (Continuer)**.
3. Sélectionnez le **Number (Nombre)** du type de données et cliquez sur **Continue (Continuer)**.
4. Saisissez le nom de l’attribut : « Lifetime Order Value (Valeur des commandes à vie) ».
5. Cliquez sur **Add Enrichment (Ajouter un enrichissement)** et sélectionnez **Increment or Decrement Number (Nombre d’incréments ou de diminutions)**.
6. Sélectionnez l’attribut contenant la valeur d’incrémentation (`order_total`).
7. Laissez le champ « WHEN (QUAND) » défini sur « Any Event (Tout événement) », puis cliquez sur **Create a New Rule (Créer une nouvelle règle)**.
8. Créez une règle qui identifie le moment où un événement d’achat a été effectué.
9. Cliquez sur **Save (Enregistrer)**, puis **Finish (Terminer)**.

Un attribut de valeur des commandes à vie sera maintenant associé à tous les clients.

{% endtab %}
{% tab Badge %}

Vous pouvez créer des badges qui vous aident à classer et à cibler vos utilisateurs en fonction de certains attributs partagés. Pour l’exemple suivant, nous créons un badge VIP pour les utilisateurs dont la « Valeur des commandes à vie » est supérieure à 500 $.

1. Accédez à **AudienceStream > Visitor/Visit Attributes (Attributs visiteur/visite)** et cliquez sur **Add Attribute (Ajouter un attribut)**.
2. Sélectionnez la portée comme **Visitor (Visiteur)**, puis cliquez sur **Continue (Continuer)**.
3. Sélectionnez le **Badge** du type de données et cliquez sur **Continue (Continuer)**.
4. Saisissez le nom du badge : « VIP ».
5. Cliquez sur **Add Enrichment (Ajouter un enrichissement)** et sélectionnez **Assign Badge (Attribuer un badge)**.
6. Laissez le champ « WHEN (QUAND) » défini sur « Any Event (Tout événement) ».
7. Créez une règle d’attribution de badge en sélectionnant **Create Rule (Créer une règle)**. Attribuez un titre à cette règle et à l’aide de l’attribut que vous venez de créer, définissez la règle sur « ...has attribute "Lifetime Order Value greater than 500" (… a un attribut « Valeur des commandes à vie supérieure à 500 ») ».
8. Cliquez sur **Save (Enregistrer)**, puis sur **Finish (Terminer)**.

{% endtab %}
{% endtabs %}

### Étape 2 : Créer une audience

À partir de la page d’accueil de Tealium, sélectionnez **Audiences** sous **AudienceStream** dans la barre de navigation latérale. Ici, vous pouvez créer une audience d’utilisateurs avec des attributs communs. L’entrée ou la sortie d’un utilisateur de cette audience sera le déclencheur de l’action du connecteur (configuré à l’étape suivante), qui transmet ces informations au profil utilisateur de Braze. 

Nommez d’abord votre audience, puis réfléchissez aux attributs qui s’appliquent au type d’audience que vous essayez de créer. Par exemple, pour créer une audience d’utilisateurs VIP, vous pourriez créer une audience de visiteurs qui ont le **badge VIP**.

Assurez-vous d’**Enregistrer/Publier** votre audience une fois terminé.

### Étape 3 : Créer un connecteur d’événement

Un connecteur est une intégration entre Tealium et un autre fournisseur qui est utilisée pour transmettre des données. Ces connecteurs contiennent des actions qui représentent les API prises en charge par leur partenaire. 

1. De la barre latérale de Tealium, sous **Server-Side (Côté serveur)**, accédez à **AudiencStream > Audience Connectors (Connecteurs d’audience)**.
2. Cliquez sur le bouton bleu **+ Add Connector (+ Ajouter un connecteur)** pour ouvrir le marketplace des connecteurs. Dans la boîte de dialogue qui apparaît, utilisez la recherche Spotlight pour trouver le connecteur **Braze**.
3. Pour ajouter ce connecteur, cliquez sur la vignette du connecteur **Braze**. Après avoir cliqué, vous pouvez afficher le résumé de la connexion et la liste des informations requises, des actions prises en charge et des instructions de configuration. La configuration comprend trois étapes : source, configuration et action.

#### Source

Dans la boîte de dialogue **Source** qui apparaît, sélectionnez l’audience que vous avez créée à l’étape précédente ainsi qu’un déclencheur qui vous semble approprié pour votre situation. Vous pouvez également activer la limite de fréquence pour contrôler la fréquence de déclenchement de cette action. 

![]({% image_buster /assets/img/tealium/create_source.png %}){: style="max-width:90%;"}

#### Configuration

Ensuite, une boîte de dialogue **Configuration** s’affiche. Sélectionnez **Add Connector (Ajouter un connecteur)** au bas de la page. Donnez un nom à votre connecteur et fournissez votre endpoint d’API Braze et la clé API REST de Braze.

![]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

Si vous aviez déjà créé un connecteur auparavant, vous avez la possibilité d’utiliser un élément existant dans la liste des connecteurs disponibles et de le modifier pour répondre à vos besoins en cliquant sur l’icône Crayon ou de le supprimer en cliquant sur l’icône Corbeille. 

Après avoir créé ou sélectionné un connecteur pour lier cette audience, cliquez sur Done (Terminé) pour continuer.

#### Action

Ensuite, nommez l’action de votre connecteur et sélectionnez un type d’action pour envoyer des données en fonction du mappage que vous configurez. Ici, vous allez mapper les attributs de Braze aux noms des attributs de Tealium. Tealium affichera différents champs à remplir en fonction du type d’action que vous avez choisi. Voici des exemples et explications de ces champs.

{% alert important %}
Tous les champs ne sont pas obligatoires.

![]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Track User (Batch and Non-Batch) %}

Cette action vous permet de suivre les attributs des utilisateurs, événements et achats en une seule action. Bien que l’action Track User (Suivre l’utilisateur) soit la même pour AudienceStream et EventStream, Tealium recommande de définir des mappages d’attributs utilisateur pour les actions AudienceStream et des mappages d’événements et d’achats pour les actions EventStream.

| Paramètres | Description |
| ---------- | ----------- |
| ID utilisateur | Utilisez ce champ pour mapper le champ ID utilisateur de Tealium à son équivalent dans Braze. Mappez un ou plusieurs attributs d’ID utilisateur. Si plusieurs ID ont été indiqués, la première valeur non vide sera prélevée en fonction de l’ordre de priorité suivant : ID externe, ID Braze, nom d’alias et libellé d’alias.<br><br>- L’ID externe et l’ID de Braze ne doivent pas être indiqués si vous importez des jetons de notification push.<br>- Si vous indiquez un alias d’utilisateur, le nom d’alias et le libellé d’alias doivent également être fournis. <br><br>Pour plus d’informations, consultez l’[endpoint users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze. |
| Attributs utilisateur | Utilisez les champs de profil utilisateur de Braze pour mettre à jour les valeurs de profil utilisateur dans le tableau de bord de Braze ou ajouter vos propres données d’[attribut utilisateur]({{site.baseurl}}/api/objects_filters/user_attributes_object/) personnalisées dans les profils utilisateur.<br><br>- Par défaut, de nouveaux utilisateurs seront créés s’il n’en existe aucun.<br>- En définissant **Update Existing Only (Mettre uniquement à jour les utilisateurs existants)** sur `true`, seuls les utilisateurs existants seront mis à jour, et aucun nouvel utilisateur ne sera créé.<br>- Si un attribut Tealium est vide, il sera défini en « nul » et supprimé du profil utilisateur Braze. Les enrichissements doivent être utilisés si les valeurs nulles ne doivent pas être envoyées à Braze pour supprimer un attribut utilisateur. |
| Modifier les attributs utilisateur | Utilisez ce champ pour incrémenter ou décrémenter certains attributs utilisateur<br><br>- Les attributs entiers peuvent être incrémentés par des entiers positifs ou négatifs.<br>- Les attributs de matrice peuvent être modifiés en ajoutant ou en supprimant des valeurs provenant des matrices existantes. |
| Événement | Un événement représente une occurrence unique d’un événement personnalisé pour un utilisateur particulier à un timestamp donné. Utilisez ce champ pour suivre et mapper les attributs d’événements tels que ceux de l’[objet événement]({{site.baseurl}}/api/objects_filters/event_object/) de Braze. <br><br>- Le `Name` de l’attribut événement est requis pour chaque événement mappé.<br>- L’`Time` de l’attribut événement est automatiquement défini à l’heure actuelle, sauf si cela est explicitement mappé. <br>- Par défaut, de nouveaux événements seront créés s’il n’en existe aucun. En définissant `Update Existing Only (Mettre à jour uniquement les utilisateurs existants)` sur `true`, seuls les événements existants seront mis à jour, et aucun nouvel événement ne sera créé.<br>- Mappez les attributs de type de matrice pour ajouter plusieurs événements. Les attributs de type de matrice doivent être de longueur égale.<br>- Les attributs de valeur unique peuvent être utilisés et appliqués à chaque événement. |
| Modèle d’événement | Fournissez des modèles d’événements à référencer dans les données du corps. Les modèles peuvent être utilisés pour transformer des données avant de les envoyer à Braze. Consultez le [Guide des modèles](https://community.tealiumiq.com/t5/AudienceStream/Webhook-Send-Custom-Request-Trimou-Templating-Engine-Guide/ta-p/15246/) de Tealium pour en savoir plus. |
| Variable du modèle d’événement | Fournissez des variables de modèle d’événement comme entrée de données. Consultez le [Guide des variables de modèles](https://community.tealiumiq.com/t5/AudienceStream/Webhook-Send-Custom-Request-Template-Variables-Guide/ta-p/15245/) de Tealium pour en savoir plus. |
| Achat | Utilisez ce champ pour suivre et mapper les achats des utilisateurs tels que ceux de l’[objet achat]({{site.baseurl}}/api/objects_filters/purchase_object/) de Braze.<br><br>- Les attributs d’achat, `ID produit`, `Currency` et `Price` sont nécessaires pour chaque achat mappé.<br>- Le `Time` de l’attribut achat est automatiquement défini à l’heure actuelle, sauf si cela est explicitement mappé.<br>- Par défaut, de nouveaux achats seront créés s’il n’en existe aucun. En définissant `Update Existing Only (Mettre à jour uniquement les utilisateurs existants)` sur `true`, seuls les achats existants seront mis à jour, et aucun nouvel achat ne sera créé.<br>- Mappez les attributs de type de matrice pour ajouter plusieurs éléments d’achat. Les attributs de type de matrice doivent être de longueur égale.<br>- Les attributs de valeur unique peuvent être utilisés et s’appliqueront à chaque élément.|
| Modèle d’achat | Les modèles peuvent être utilisés pour transformer des données avant de les envoyer à Braze.<br>- Définissez un modèle d’achat si vous avez besoin de prendre en charge des objets imbriqués.<br>- Lorsqu’un modèle d’achat est défini, la configuration de la section Achats de votre action sera ignorée.<br>- Consultez le [Guide des modèles](https://community.tealiumiq.com/t5/AudienceStream/Webhook-Send-Custom-Request-Trimou-Templating-Engine-Guide/ta-p/15246/) de Tealium pour en savoir plus.|
| Variable du modèle d’achat | Fournissez des variables de modèle de produit comme entrée de données. Consultez le [Guide des variables de modèles](https://community.tealiumiq.com/t5/AudienceStream/Webhook-Send-Custom-Request-Template-Variables-Guide/ta-p/15245/) de Tealium pour en savoir plus. |
{: .reset-td-br-1 .reset-td-br-2}

![]({% image_buster /assets/img/tealium/track_user_example2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Delete User (Non-Batch) %}

Cette action vous permet de supprimer des utilisateurs du tableau de bord de Braze.

| Paramètres | Description |
| ---------- | ----------- |
| ID utilisateur | Utilisez ce champ pour mapper le champ ID utilisateur de Tealium à son équivalent dans Braze.<br><br>- Mappez un ou plusieurs attributs d’ID utilisateur. Si plusieurs ID ont été indiqués, la première valeur non vide sera prélevée en fonction de l’ordre de priorité suivant : ID externe, ID Braze, nom d’alias et libellé d’alias.<br>- Si vous indiquez un alias d’utilisateur, le nom d’alias et le libellé d’alias ne doivent pas être fournis.<br><br>Pour plus d’informations, consultez l’[endpoint /users/delete]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) de Braze. |
{: .reset-td-br-1 .reset-td-br-2}

![]({% image_buster /assets/img/tealium/track_user_delete2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Update User Subscription Group Status (Non-Batch) %}
Cette action vous permet d’ajouter ou de supprimer des utilisateurs des groupes d’abonnement par e-mail ou SMS de Braze.

| Paramètres | Description |
| ---------- | ----------- |
| Type de groupe | Utilisez ce champ pour indiquer s’il s’agit d’un groupe d’abonnement par e-mail ou SMS. |
| Type de mise à jour | Mappez cette action à un événement d’abonnement ou de désabonnement 
| Attributs | - ID du groupe d’abonnement (obligatoire) : L’ID du groupe d’abonnement associé au type de groupe mappé dans le champ précédent.<br>- ID externe : L’ID externe de l’utilisateur.<br><br>Spécifique au groupe E-mail :<br>- E-mail : L’adresse e-mail de l’utilisateur.<br>**Si l’ID externe n’est pas défini, l’e-mail sera requis.**<br><br>Spécifique au groupe SMS :<br>- Téléphone : Le numéro de téléphone au format E.164. Par exemple, +14155552671.<br>**Si l’ID externe n’est pas défini, le téléphone sera requis.** |
{: .reset-td-br-1 .reset-td-br-2}

![]({% image_buster /assets/img/tealium/update_subscription.png %}){: style="max-width:90%"}

{% endtab %}
{% endtabs %}

Cliquez sur **Finish (Terminer)**.

#### Résumé

Afficher le résumé du connecteur que vous avez créé. Si vous souhaitez modifier les options sélectionnées, cliquez sur **Back (Retour)** pour les modifier ou sur **Finish (Terminer)**.

Votre connecteur s’affiche maintenant dans la liste des connecteurs sur votre page d’accueil Tealium.

Assurez-vous d’**Enregistrer/Publier** votre connecteur une fois terminé. Les actions que vous avez configurées vont maintenant se déclencher lorsque les connexions du déclencheur sont satisfaites. 

### Étape 4 : Tester votre connecteur Tealium

Une fois votre connecteur en marche et en cours d’exécution, vous devez le tester pour vous assurer qu’il fonctionne correctement. Le moyen le plus simple de tester votre connecteur est d’utiliser l’**outil Trace** de Tealium. Pour commencer à utiliser Trace, assurez-vous d’avoir ajouté l’extension de navigateur Tealium Tools.

1. Pour démarrer une nouvelle action de suivi, sélectionnez **Trace** sur la barre latérale sous les options **Server-Side (Côté serveur)**. Cliquez sur **Start (Démarrer)** et notez l’ID de Trace.
2. Ouvrez l’extension du navigateur et saisissez l’ID de Trace dans AudienceStream Trace.
3. Vérifiez le journal en temps réel.
4. Vérifiez l’action que vous souhaitez valider en cliquant sur l’entrée **Actions Triggered (Actions déclenchées)** pour développer la liste.
5. Recherchez l’action que vous souhaitez valider et consultez l’état du journal. 

Consultez la [documentation Trace][21] de Tealium pour obtenir des instructions détaillées sur l’utilisation de l’outil Trace de Tealium.

## Démo de l’intégration

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Dépassements potentiels des points de données

Il existe trois façons principales d’atteindre accidentellement des dépassements de données lorsque vous intégrez Braze via Tealium :

#### Envoyer des données en double - envoyez uniquement des deltas d’attributs à Braze
Tealium n’envoie pas de deltas d’attributs utilisateur à Braze. Par exemple, si vous avez une action EventStream qui suit le prénom, l’e-mail et le numéro de téléphone portable d’un utilisateur, Tealium enverra ces trois attributs à Braze chaque fois que l’action est déclenchée. Tealium ne recherchera pas ce qui a changé ou ce qui a été mis à jour pour n’envoyer que ces informations.<br><br> 
**Solution** : <br>Vous pouvez vérifier votre back-end pour déterminer si un attribut a changé ou non. Si c’est le cas, suivez les méthodes de Tealium correspondantes pour mettre à jour le profil utilisateur. **C’est ce que font généralement les utilisateurs qui intègrent directement Braze.** <br>**OU**<br> Si vous ne stockez pas votre propre version d’un profil utilisateur dans votre dossier et si vous ne pouvez pas déterminer si des attributs changent ou non, vous pouvez utiliser AudienceStream et [créer des enrichissements](https://community.tealiumiq.com/t5/Customer-Data-Hub/Using-Enrichments/ta-p/11932) pour envoyer uniquement les attributs utilisateur lorsque les valeurs ont changé. Reportez-vous à la documentation de Tealium sur les [règles d’enrichissement](https://community.tealiumiq.com/t5/Server-Side-Connectors/Braze-Connector-Setup-Guide/ta-p/29761#) pour plus d’informations.

#### Envoyer des données non pertinentes ou écraser inutilement des données
Si vous avez plusieurs EventStream qui ciblent le même flux d’événements, **toutes les actions activées pour ce connecteur** se déclencheront automatiquement chaque fois qu’une action est déclenchée, **cela pourrait également entraîner l’écrasement des données dans Braze.**<br><br>
**Solution** : <br>Configurez une spécification ou un flux d’événement distinct pour suivre chaque action. <br>**OU**<br> Désactivez les actions (ou les connecteurs) que vous ne voulez pas déclencher en utilisant les boutons de bascule du tableau de bord Tealium.

#### Initialiser Braze trop tôt
Il se peut que les utilisateurs qui intègrent Tealium à l’aide de la balise du SDK Web de Braze observent une augmentation spectaculaire de leur MAU. **Si Braze est initialisé pendant le chargement de la page, Braze créera un profil anonyme chaque fois qu’un utilisateur Web navigue sur le site pour la première fois.** Certaines personnes voudront suivre le comportement des utilisateurs uniquement lorsque ceux-ci ont effectué certaines actions, comme « Signed In (Connecté) » ou « Watched Video (Vidéo regardée) », pour réduire leur MAU. <br><br>
**Solution** : <br>Configurez les règles de chargement pour déterminer exactement quand et où une balise doit charger sur votre site. Vous pouvez en savoir plus sur les règles de chargement et sur la manière de les configurer dans le [Centre d’apprentissage Tealium](https://community.tealiumiq.com/t5/Customer-Data-Hub/Building-an-Audience/ta-p/11881).

[1]: https://community.tealiumiq.com/t5/Getting-Started-with/Attributes/ta-p/25785
[15]: {% image_buster /assets/img/tealium/create_configuration.png %}
[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
[21]: https://community.tealiumiq.com/t5/Getting-Started-with/Trace/ta-p/25797
[17]: {% image_buster /assets/img/tealium/save_publish.png %}