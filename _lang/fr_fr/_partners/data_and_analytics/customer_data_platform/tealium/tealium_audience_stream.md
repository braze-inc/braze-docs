---
nav_title: Tealium AudienceStream
article_title: Tealium AudienceStream
page_order: 2
alias: /partners/tealium_audience_stream/
description: "Cet article de référence présente le partenariat entre Braze et Tealium, un Centre de données universel qui vous permet de connecter des données mobiles, web et alternatives à d'autres sources tierces."
page_type: partner
search_tag: Partner

---

# Tealium AudienceStream

> Tealium [AudienceStream](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/introduction/) est un moteur de segmentation omnicanal des clients et d'action en temps réel. AudienceStream prend les données qui affluent dans EventStream et crée des profils de visiteurs représentant les attributs les plus importants de l'engagement de vos clients avec votre marque. 

L'intégration entre Braze et Tealium s'appuie sur les profils des visiteurs d'AudienceStream. Les comportements partagés segmentent ces profils pour créer des ensembles de visiteurs présentant des traits communs, appelés audiences. Ces audiences peuvent contribuer à alimenter votre pile technologique marketeur en temps réel via des connecteurs. 

{% alert important %}
Tealium AudienceStreams et EventStreams offrent à la fois des actions de connecteur par lots et non par lots. Le connecteur non-batch doit être utilisé lorsque les requêtes en temps réel sont importantes pour le cas d'utilisation et qu'il n'y a pas d'inquiétude quant à la limite de débit de l'API Braze. Contactez le service d'[assistance]({{site.baseurl}}/braze_support/) de Braze ou votre gestionnaire de la satisfaction client si vous avez des questions.
{% endalert %}

## Prérequis

| Nom | Descriptif |
| ---- | ----------- |
| Compte Tealium | Un [compte Tealium](https://my.tealiumiq.com/) avec accès au serveur est nécessaire. Nous vous recommandons également d'utiliser les intégrations côté client pour profiter de ce partenariat. |
| Clé d'API REST | Une clé API REST Braze avec`users.track`, `users.delete` et des autorisations `subscription.status.set`.<br><br>Celle-ci peut être créée dans le **tableau de bord de Braze > Console de développement > Clé API REST > Créer une nouvelle clé API**|
| [Endpoint REST Braze]({{site.baseurl}}/api/basics/#endpoints) | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Configurer des attributs et des badges

#### Comprendre les attributs

Pour commencer à utiliser AudienceStream, vous devez créer des attributs. Les attributs vous permettent de définir les caractéristiques importantes qui représentent les habitudes, les préférences, les actions et l'engagement d'un visiteur envers votre marque. 

**Les attributs de visite** : Les attributs de visite se rapportent à la visite (ou session) en cours de l'utilisateur. Les données stockées dans ces attributs persistent pendant toute la durée de la visite. Voici quelques exemples d'attributs de visite :
- Durée de la visite (nombre)
- Navigateur actuel (Chaîne de caractères)
- Appareil actuel (chaîne de caractères)
- Nombre de pages vues (nombre)

**Attributs des visiteurs**: Les attributs du visiteur se rapportent à l'utilisateur actuel. Les données stockées dans ces attributs persistent pendant toute la durée de vie de l'utilisateur. Voici quelques exemples d'attributs des visiteurs : 
- Valeur vie client (nombre)
- Prénom (chaîne de caractères)
- Date de naissance (Date)
- Achats marques (Tally)

Visitez [Tealium](https://docs.tealium.com/server-side/attributes/about/) pour une liste complète des types de données disponibles.

##### Enrichissement des attributs

Une fois que vous avez identifié les attributs souhaités, vous pouvez les configurer avec des [enrichissements](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/attributes-enrichments/), c'est-à-dire des règles de gestion qui déterminent quand et comment mettre à jour les valeurs des attributs. Chaque type de données offre sa propre sélection d'enrichissements pour manipuler la valeur de l'attribut. Il est associé au paramètre "QUAND". Les options suivantes sont disponibles pour chaque visite et attribut de visiteur :

- Nouveau visiteur : se produit lorsque qu’un visiteur vient sur votre site.
- Nouvelle visite : se produit lors d'une nouvelle visite d'un visiteur.
- Tout événement : se produit lors de tout événement.
- Visite terminée : se produit lorsqu'une visite se termine.

Vous pouvez également créer une condition personnalisée, appelée règle, qui déterminera le moment de l'enrichissement.

#### Badges

Les badges sont des attributs spéciaux des visiteurs qui représentent des modèles de comportement précieux. Les badges sont attribués ou retirés aux visiteurs en fonction de la logique de leurs enrichissements. Cette logique combine généralement plusieurs conditions pour capturer des segments de visiteurs ou définit un seuil lorsqu'une valeur particulière est atteinte.

#### Exemple d'attribut et de badge

{% tabs local %}
{% tab Attribut %}

Créez un attribut visiteur "Lifetime Order Value" qui calcule le montant cumulé dépensé (`order_total`) par le client pour toutes les commandes passées (événement d'achat). Pour définir la valeur vie client dans votre compte Tealium, suivez les instructions ci-dessous :

1. Naviguez vers **AudienceStream > Attributs de visiteur/visite** et cliquez sur **Ajouter un attribut**.
2. Sélectionnez le champ d'application **Visiteur** et cliquez sur **Continuer**.
3. Sélectionnez le type de données **Nombre** et cliquez sur **Continuer.**
4. Saisissez le nom de l'attribut, "Valeur à vie des commandes".
5. Cliquez sur **Ajouter un enrichissement** et sélectionnez **Incrémenter ou Décrémenter le nombre.**
6. Sélectionnez l'attribut contenant la valeur à incrémenter (`order_total`).
7. Laissez le paramètre "QUAND" sur "Tout événement", puis cliquez sur **Créer une nouvelle règle**.
8. Créez une règle qui identifie le moment où un événement d'achat s'est produit.
9. Cliquez sur **Enregistrer**, puis sur **Terminer**.

Désormais, tous les clients seront associés à un attribut personnalisé de valeur vie de la commande.

{% endtab %}
{% tab Badge %}

Vous pouvez créer des badges qui vous aident à classer et à cibler vos utilisateurs en fonction de certains attributs qu'ils partagent. Dans l'exemple suivant, nous créons un badge VIP pour les utilisateurs dont la "valeur à vie client" est supérieure à 500 $.

1. Naviguez vers **AudienceStream > Attributs de visiteur/visite** et cliquez sur **Ajouter un attribut**.
2. Sélectionnez le champ d'application **Visiteur** et cliquez sur **Continuer**.
3. Sélectionnez le type de données **Badge** et cliquez sur **Continuer.**
4. Saisissez le nom du badge, "VIP".
5. Cliquez sur **Ajouter un enrichissement** et sélectionnez **Attribuer un badge**.
6. Laissez le paramètre "QUAND" sur "Tout événement".
7. Créez une règle pour l'attribution des badges en sélectionnant **Créer une règle**. Attribuez un titre à cette règle et, à l'aide de l'attribut créé précédemment, définissez la règle comme suit : "...a l'attribut "Valeur vie client supérieure à 500".
8. Cliquez sur **Enregistrer**, puis sur **Terminer**.

{% endtab %}
{% endtabs %}

### Étape 2 : Créer une audience

Sur la page d'accueil de Tealium, sélectionnez **Audiences** sous **AudienceStream** dans la barre de navigation latérale. Ici, vous pouvez créer une audience d'utilisateurs ayant des attributs communs. L'entrée ou la sortie d'un utilisateur de cette audience sera le déclencheur de l'action connecteur, définie à l'étape suivante, qui transmettra ces informations au profil utilisateur dans Braze. 

Commencez par nommer votre audience, puis réfléchissez aux caractéristiques du type d'audience que vous essayez de créer. Par exemple, pour créer une audience d'utilisateurs VIP, vous pouvez créer une audience de visiteurs qui possèdent le **badge VIP.**

Veillez à **enregistrer / publier** votre audience lorsque vous avez terminé.

### Étape 3 : Créer un connecteur d'événement

Un connecteur est une intégration entre Tealium et un autre fournisseur utilisé pour transmettre des données. Ces connecteurs contiennent des actions qui représentent les API prises en charge par leur partenaire. 

1. Dans la barre latérale de Tealium, sous **Côté serveur**, naviguez vers **AudienceStream > Audience Connecteurs**.
2. Sélectionnez le bouton bleu **\+ Ajouter un connecteur** pour consulter la place de marché des connecteurs. Dans la nouvelle boîte de dialogue qui apparaît, utilisez la recherche par projecteur pour trouver le connecteur **Braze**.
3. Pour ajouter ce connecteur, cliquez sur la tuile de connecteur **Braze**. Lorsque vous cliquez sur ce bouton, vous pouvez afficher le résumé de la connexion et une liste des informations requises, des actions prises en charge et des instructions de configuration. La configuration comprend trois étapes : la source, la configuration et l'action.

#### Source

Dans la boîte de dialogue **Source** qui s'affiche, sélectionnez l'audience que vous avez créée à l'étape précédente et un déclencheur qui vous semble adapté à votre situation. Vous pouvez également basculer sur la limite de fréquence pour contrôler la fréquence de déclenchement de cette action. 

![]({% image_buster /assets/img/tealium/create_source.png %}){: style="max-width:90%;"}

#### Configuration

Une boîte de dialogue de **configuration** apparaît ensuite. Sélectionnez **Ajouter un connecteur** en bas de la page. Nommez votre connecteur et indiquez ici l’endpoint de l’API Braze et votre clé API REST Braze.

![]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

Si vous avez déjà créé un connecteur, vous pouvez utiliser un connecteur existant dans la liste des connecteurs disponibles et le modifier en fonction de vos besoins à l'aide de l'icône du crayon ou le supprimer à l'aide de l'icône de la corbeille. 

Après avoir créé ou sélectionné un connecteur pour relier cette audience, cliquez sur Terminé pour continuer.

#### Action

Ensuite, nommez votre action de connecteur et sélectionnez un type d'action qui enverra des données selon le mappage que vous avez configuré. Ici, vous mapperez les attributs Braze aux noms d'attributs Tealium. Selon le type d'action que vous choisissez, les champs requis par Tealium seront plus ou moins nombreux. Vous trouverez ci-dessous des exemples et des explications concernant ces champs.

{% alert important %}
Tous les champs proposés ne sont pas obligatoires.

![]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab Suivi des utilisateurs - lots et non-lots %}

Cette action vous permet de suivre les attributs des utilisateurs, des événements et des achats en une seule action. Bien que l'action Suivre l'utilisateur soit la même pour AudienceStream et EventStream, Tealium recommande de définir des mappages d'attributs utilisateurs avec des actions AudienceStream et des mappages d'événements et d'achats avec les actions EventStream.

| Paramètres | Description |
| ---------- | ----------- |
| ID utilisateur | Utilisez ce champ pour mapper le champ ID utilisateur de Tealium à son équivalent Braze. Mapper un ou plusieurs attributs d'ID utilisateur. Lorsque plusieurs identifiants sont spécifiés, la première valeur non vide est choisie en fonction de l'ordre de priorité suivant : ID externe, ID Braze, Nom d'alias, et libellé d'alias.<br><br>\- L’ID externe et l’ID Braze ne doivent pas être spécifiés si vous importez des jetons de notifications push.<br>Si vous spécifiez un alias d'utilisateur, le nom de l'alias et le libellé d'alias doivent être définis. <br><br>Pour plus d'informations, consultez l’[`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) Braze. |
| Attributs utilisateur | Utilisez les noms de champs existants du profil utilisateur de Braze pour mettre à jour les valeurs du profil utilisateur dans le tableau de bord de Braze ou ajoutez vos propres données d'[attributs]({{site.baseurl}}/api/objects_filters/user_attributes_object/) personnalisés aux profils utilisateurs.<br><br>Par défaut, de nouveaux utilisateurs seront créés s’il n’en existe aucun.<br>En définissant **Mettre à jour uniquement les existants** sur `true`, seuls les utilisateurs existants seront mis à jour et aucun nouvel utilisateur ne sera créé.<br>Si un attribut Tealium est vide, il sera converti en null et supprimé du profil utilisateur Braze. Les enrichissements doivent être utilisés si des valeurs nulles ne doivent pas être envoyées à Braze pour supprimer un attribut utilisateur. |
| Modifier les attributs de l'utilisateur | Utilisez ce champ pour augmenter ou diminuer certains attributs utilisateur<br><br>Les attributs entiers peuvent être incrémentés par des entiers positifs ou négatifs.<br>Les attributs de tableau peuvent être modifiés en ajoutant ou en supprimant des valeurs provenant des tableaux existants. |
| Événement | Un événement représente une seule occurrence d'un événement personnalisé par un utilisateur particulier à un horodatage. Utilisez ce champ pour suivre et mapper les attributs d'événement comme ceux de l'objet d'événement Braze [event object]({{site.baseurl}}/api/objects_filters/event_object/). <br><br>L'attribut d'événement `Name` est requis pour chaque événement mappé.<br>L'attribut d'événement `Time` est automatiquement défini sur Maintenant à moins qu’il ne soit explicitement mappé. <br>Par défaut, de nouveaux événements seront créés s'il n'en existe pas. En définissant `Update Existing Only` sur `true`, seuls les événements existants seront mis à jour, et aucun nouvel événement ne sera créé.<br>Mapper les attributs de type tableau pour ajouter plusieurs événements. Les attributs de type tableau doivent être de longueur égale.<br>\- Des attributs à valeur unique peuvent être utilisés et appliqués à chaque événement. |
| Modèle d'événement | Fournir des modèles d'événements à référencer dans les données de corps. Les modèles peuvent être utilisés pour transformer des données avant de les envoyer à Braze. Reportez-vous au [Guide des modèles](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) de Tealium pour en savoir plus. |
| Variable de modèle d'événement | Fournir des variables de modèle d'événement comme entrée de donnée. Reportez-vous au [Guide des variables de modèle](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) de Tealium pour en savoir plus. |
| Achat | Utilisez ce champ pour suivre et mapper les attributs d'achat des utilisateurs comme ceux dans l'objet d'achat Braze [purchase object]({{site.baseurl}}/api/objects_filters/purchase_object/).<br><br>\- Les attributs d'achat `Product ID`, `Currency` et `Price` sont requis pour chaque achat mappé.<br>\- L'attribut d'achat `Time` est automatiquement défini sur Maintenant à moins qu’il ne soit explicitement mappé.<br>Par défaut, de nouveaux achats seront créés s'il n'en existe pas. En définissant `Update Existing Only` sur `true`, seules les achats existants seront mis à jour, et aucun nouvel achat ne sera créé.<br>Mapper les attributs de type tableau pour ajouter plusieurs articles d'achat. Les attributs de type tableau doivent être de longueur égale.<br>Les attributs à valeur unique peuvent être utilisés et s'appliqueront à chaque élément.|
| Acheter le modèle | Les modèles peuvent être utilisés pour transformer les données avant qu'elles ne soient envoyées à Braze.<br>\- Définissez un modèle d'achat si vous avez besoin de prendre en charge des objets imbriqués.<br>Lorsqu'un modèle d'achat est défini, la configuration définie dans la section des achats de votre action sera ignorée.<br>Reportez-vous au [Guide des modèles](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/) de Tealium pour en savoir plus.|
| Variable du modèle d’achat | Fournir les variables de modèle de produit comme entrée de donnée. Reportez-vous au [Guide des variables de modèle](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/) de Tealium pour en savoir plus. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_example2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Suppression d'un utilisateur - hors lot %}

Cette action vous permet de supprimer des utilisateurs du tableau de bord de Braze.

| Paramètres | Description |
| ---------- | ----------- |
| ID de l'utilisateur | Utilisez ce champ pour mapper le champ ID de l'utilisateur Tealium à son équivalent Braze.<br><br>\- Mappez un ou plusieurs attributs de l'ID de l'utilisateur. Lorsque plusieurs identifiants sont spécifiés, la première valeur non vide est choisie en fonction de l'ordre de priorité suivant : ID externe, ID Braze, Nom d'alias, et libellé d'alias.<br>Lors de la spécification d'un alias d'utilisateur, le nom d'alias et le libellé d'alias doivent être définis tous les deux.<br><br>Pour plus d'informations, consultez [`/users/delete`l'endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) de Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_delete2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab Mise à jour du statut du groupe d'abonnement d'un utilisateur - Non-Batch %}
Cette action vous permet d'ajouter ou de supprimer des utilisateurs des groupes d'abonnement SMS ou e-mail de Braze.

| Paramètres | Descriptif |
| ---------- | ----------- |
| Type de groupe | Utilisez ce champ pour indiquer s'il s'agit d'un groupe d'abonnement par SMS ou par e-mail. |
| Type de mise à jour | Mappez cette action à un événement de désinscription ou d'abonnement. 
| Attributs | \- ID du groupe d'abonnement (obligatoire) : L'ID du groupe d'abonnement lié au type de groupe mappé dans le champ précédent.<br>\- ID externe : L'ID externe de l'utilisateur.<br><br>Spécifique à un groupe d'e-mails :<br>\- E-mail : L'adresse e-mail de l'utilisateur.<br>**Si l'ID externe n'est pas défini, l'e-mail devra être fourni.**<br><br>Spécifique au groupe SMS :<br>\- Téléphone : Le numéro de téléphone au format E.164. Par exemple, +14155552671.<br>**Si l'ID externe n'est pas défini, le numéro de téléphone devra être fourni.** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/update_subscription.png %}){: style="max-width:90%"}

{% endtab %}
{% endtabs %}

Sélectionnez **Terminer**.

#### Résumé

Affichez le résumé du connecteur que vous avez créé. Si vous souhaitez modifier les options choisies, sélectionnez **Retour** pour modifier ou **Terminer** pour compléter.

Votre connecteur est maintenant affiché dans la liste des connecteurs sur votre page d'accueil Tealium.

Veillez à enregistrer ou à publier votre connecteur lorsque vous avez terminé. Les actions que vous avez configurées se déclencheront désormais lorsque les connexions du déclencheur seront satisfaites. 

### Étape 4 : Testez votre connecteur Tealium

Après que votre connecteur soit opérationnel, vous devriez le tester pour vous assurer qu'il fonctionne correctement. La manière la plus simple de tester cela est d'utiliser l'**outil de traçage** de Tealium. Pour commencer à utiliser l’outil de traçage, assurez-vous d'avoir ajouté l'extension de navigateur Tealium Tools.

1. Pour lancer une nouvelle trace, sélectionnez **Trace** dans la barre latérale sous Options **côté serveur.**  Cliquez sur **Démarrer** et capturez l'ID de l’outil de traçage.
2. Ouvrez l'extension du navigateur et entrez l'ID de traçage dans AudienceStream Trace.
3. Examinez le journal en temps réel.
4. Vérifiez l'action que vous souhaitez valider en cliquant sur l'entrée **Actions déclenchées** pour développer.
5. Recherchez l'action que vous voulez valider et consultez l’état du journal. 

Reportez-vous à la [documentation Trace](https://docs.tealium.com/server-side/connectors/trace/about/) de Tealium pour obtenir des instructions plus détaillées sur la mise en œuvre de l'outil Trace de Tealium.

## démonstration d'intégration

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## Dépassements potentiels de point de donnée

Il existe principalement trois façons de dépasser accidentellement les limites de données lors de l'intégration de Braze via Tealium :

#### Envoi de données en double - n'envoyez que les deltas Braze des attributs.
Tealium n'envoie pas à Braze les deltas des attributs des utilisateurs. Par exemple, si vous avez une action Eventstream qui suit le prénom, l'e-mail et le numéro de téléphone portable d'un utilisateur, Tealium enverra ces trois attributs à Braze chaque fois que l'action sera déclenchée. Tealium ne cherchera pas ce qui a changé ou a été mis à jour et n'enverra que ces informations.<br><br> 
**Solution** : <br>Vous pouvez vérifier votre backend pour évaluer si un attribut a changé ou non, et si c'est le cas, appeler les méthodes pertinentes de Tealium pour mettre à jour le profil utilisateur. **C'est ce que font généralement les utilisateurs qui intègrent Braze directement.** <br>**OU**<br> Si vous ne stockez pas votre propre version d'un profil utilisateur dans votre backend et que vous ne pouvez pas savoir si les attributs changent ou non, vous pouvez utiliser AudienceStream et [créer des enrichissements](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/) pour n'envoyer les attributs de l'utilisateur que lorsque les valeurs ont changé. 

#### Envoi de données non pertinentes ou écrasement inutile de données
Si vous avez plusieurs EventStreams qui ciblent le même flux d'événements, **toutes les actions activées pour ce connecteur** se déclencheront automatiquement à chaque fois qu'une action unique est déclenchée, **ce qui pourrait également entraîner l'écrasement de données dans Braze**.<br><br>
**Solution**: <br>Configurez une spécification d'événement distincte ou un flux pour suivre chaque action. <br>**OU**<br> Désactivez les actions (ou connecteurs) que vous ne souhaitez pas déclencher en utilisant les commutateurs dans le tableau de bord Tealium.

#### Initialisation de Braze trop tôt
Les utilisateurs intégrant Tealium en utilisant la balise du SDK Web Braze peuvent voir une augmentation spectaculaire de leur MAU. **Si Braze est initialisé au chargement de la page, Braze créera un profil anonyme chaque fois qu'un utilisateur web navigue sur le site pour la première fois.** Certains peuvent vouloir suivre le comportement des utilisateurs uniquement lorsque ceux-ci ont effectué une action, telle que "Connecté" ou "Regardé une vidéo", afin de réduire leur nombre de MAU. <br><br>
**Solution** : <br>Configurez les [règles de chargement](https://docs.tealium.com/iq-tag-management/load-rules/about/) pour déterminer exactement quand et où une étiquette se charge sur votre site.

