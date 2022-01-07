---
nav_title: RevenueCat
description: "L'intégration de RevenueCat et Braze vous permet de synchroniser automatiquement les événements de cycle de vie d'achat et d'abonnement de vos clients sur toutes les plateformes. Cela vous permet de construire des campagnes qui réagissent à la phase de cycle de vie de l'abonnement de vos clients, comme s'engager avec les clients qui se sont retirés pendant leur essai gratuit ou envoyer des rappels aux clients avec des problèmes de facturation."
alias: /fr/partners/revenuecat/
page_type: partenaire
search_tag: Partenaire
---

# RevenueCat

> [RevenueCat](https://www.revenuecat.com/) est la seule source de vérité pour votre statut d'abonnement sur iOS, Android et web. Que vous construisiez une nouvelle application ou que vous ayez déjà des millions d'abonnés, vous pouvez utiliser RevenueCat pour construire des achats inter-plateformes dans l'application, gérez vos produits et abonnés, et analysez vos données - aucun code serveur requis.

L'intégration de RevenueCat et Braze vous permet de synchroniser automatiquement les événements de cycle de vie d'achat et d'abonnement de vos clients sur toutes les plateformes. Cela vous permet de construire des campagnes qui réagissent à la phase de cycle de vie de l'abonnement de vos clients, comme s'engager avec les clients qui se sont retirés pendant leur essai gratuit ou envoyer des rappels aux clients avec des problèmes de facturation.

## Pré-requis

Au minimum, vous aurez besoin d'activer l'intégration depuis le tableau de bord RevenueCat pour connecter RevenueCat à Braze. Si vous utilisez le Braze SDK, vous pouvez utiliser ensemble les SDK RevenueCat et Braze pour améliorer l'intégration en veillant à ce que le même identifiant client soit utilisé dans les deux systèmes.

| Exigences                              | Libellé                                                                                                                                                                                                                                                                                                         |
| -------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte RevenueCat et application       | Un compte [RevenueCat][9] est requis pour profiter de ce partenariat. Vous devez également avoir une application RevenueCat configurée.                                                                                                                                                                         |
| RevenueCat SDK                         | En plus du Braze SDK requis, nous vous recommandons d'installer le [RevenueCat SDK][8] pour fournir des alias utilisateur à RevenueCat.                                                                                                                                                                         |
| Instance Braze                         | Votre instance Braze peut être obtenue auprès de votre gestionnaire d'intégration Braze ou peut être trouvée sur la page [Aperçu de l'API]({{site.baseurl}}/api/basics/#endpoints).<br><br>RevenueCat nécessite que l'instance Braze envoie le côté serveur au bon point de terminaison Braze REST. |
| Braze clé API REST                     | Une clé API Braze REST avec les permissions `users.track`. <br><br> Ceci peut être créé dans le **tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API**                                                                                                    |
| Clé d'API REST test Braze (facultatif) | Une clé API de test peut être utilisée pour les achats de test et de production si vous souhaitez que ces demandes soient envoyées à des instances de Braze séparées.                                                                                                                                           |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d'utilisation

- Déclenchez une campagne d'intégration mettant en évidence vos fonctionnalités premium lorsqu'un client commence un essai gratuit.
- Envoyer un rappel pour mettre à jour les informations de facturation lorsqu'un événement "Facturation" est reçu.
- Envoyer une enquête de rétroaction après qu'un client annule un essai gratuit.

## Intégration

### Étape 1 : Définir l'identité de l'utilisateur Braze

Dans le Braze SDK, vous pouvez définir l'ID de l'utilisateur Braze pour qu'il corresponde à l'ID de l'utilisateur de l'application RevenueCat, en veillant à ce que les événements envoyés par Braze et RevenueCat puissent être synchronisés avec le même utilisateur.

Configurez le SDK Braze avec le même ID utilisateur de l'application que RevenueCat ou utilisez la méthode Braze SDK `.changeUser()`.

{% tabs local %}
{% tab swift %}
```swift
// Configurer les achats SDK
Purchases.configure(withAPIKey: "public_sdk_key", appUserID: "my_app_user_id")

// Changer l'utilisateur dans Braze SDK
Appboy.sharedInstance()?. hangeUser("my_app_user_id")

// Attributs optionnels d'alias d'utilisateur
Achats.shared. etAttributes(["$brazeAliasName" : "name", 
                             "$brazeAliasLabel" : "label"])
```
{% endtab %}
{% tab objective-c %}
```objc
// Configurer les achats SDK
[RCPurchases configureWithAPIKey:@"public_sdk_key" appUserID:@"my_app_user_id"];

// Changer l'utilisateur dans Braze SDK
[[Appboy sharedInstance] changeUser:@"my_app_user_id"];

// Attributs optionnels de l'objet alias d'utilisateur
[[RCPurchases sharedPurchases] setAttributes:@{
    @"$brazeAliasName": @"name",
    @"$brazeAliasLabel": @"label"
}];
```
{% endtab %}
{% tab java %}
```java
// Configurer les achats de SDK
Purchases.configure(ceci, "public_sdk_key", "my_app_user_id");

// Change l'utilisateur dans Braze SDK
Braze.getInstance(contexte). hangeUser(my_app_user_id);

// Attributs optionnels d'alias d'utilisateurs
Map<String, String> attributs = new HashMap<String, String>();
attributs. ut("$brazeAliasName", "name");
attributes.put("$brazeAliasLabel", "label");

Purchases.getSharedInstance().setAttributes(attributes);
```
{% endtab %}
{% endtabs %}

#### Envoyer un objet alias utilisateur à Braze (facultatif)

Si vous voulez envoyer un autre identifiant d'utilisateur unique différent de l'identifiant de l'application RevenueCat, mettre à jour les utilisateurs avec les données suivantes comme attributs d'abonné RevenueCat.

| Clés               | Libellé                                                          |
| ------------------ | ---------------------------------------------------------------- |
| `$brazeAliasName`  | Le Braze `alias_name` dans l'objet alias de l'utilisateur [][2]  |
| `$brazeAliasLabel` | Le Braze `alias_label` dans l'objet alias de l'utilisateur [][2] |
{: .reset-td-br-1 .reset-td-br-2}

Les deux attributs sont requis pour que l'objet [alias utilisateur][2] soit envoyé à côté de vos données d'événement. Ces propriétés peuvent être définies manuellement, comme n'importe quel attribut d'abonné [RevenueCat][4]. Des exemples de code snippets sont montrés ci-dessus.

### Étape 2 : Envoyez des événements RevenueCat à Braze

Après avoir configuré RevenueCat a acheté SDK et Braze SDK pour avoir la même identité d'utilisateur, vous pouvez activer l'intégration et configurer les noms des événements à partir du tableau de bord RevenueCat.

1. Naviguez vers votre projet dans le tableau de bord RevenueCat et trouvez la carte **Intégrations** dans le menu de gauche. Sélectionnez **+ Nouveau**.
2. Ensuite, sélectionnez **Braze** dans l'intégration disponible et ajoutez votre instance Braze et votre clé API Braze REST.
3. Entrez les noms d'événements que RevenueCat enverra ou choisira les noms d'événement par défaut. Plus de détails sur les événements disponibles peuvent être trouvés à [l'étape 3](#configure-event-names).
4. Indiquez si vous voulez que RevenueCat rapporte les recettes (après coupure du magasin d'application) ou les revenus (ventes brutes).

!\[Paramètres de Braze en revenuecat\]\[3\]

### Étape 3 : Configurer les noms des événements {#configure-event-names}

Entrez les noms d'événements que RevenueCat enverra ou sélectionnera à partir des noms d'événements par défaut en sélectionnant **Utiliser les noms d'événements par défaut**. Les événements que RevenueCat prend en charge l'envoi sont décrits ci-dessous.

| Evénement               | Libellé                                                                                                                                                                             |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Achat initial           | Le premier achat d'un produit d'abonnement auto-renouvelant qui ne contient pas d'essai gratuit.                                                                                    |
| Essai commencé          | Le début d'un essai gratuit de produit d'abonnement auto-renouvelable.                                                                                                              |
| Essai converti          | Lorsqu'un produit d'abonnement renouvelant automatiquement convertit d'un essai gratuit à une période normale payante.                                                              |
| Essai annulé            | Lorsqu'un utilisateur désactive les renouvellements pour un produit d'abonnement auto-renouvelé pendant une période d'essai gratuite.                                               |
| Renouvellement          | Lorsqu'un produit d'abonnement renouvelé automatiquement ou qu'un utilisateur réachète le produit d'abonnement à renouvellement automatique après une expiration de son abonnement. |
| Annulation              | Lorsqu'un utilisateur désactive les renouvellements pour un produit d'abonnement auto-renouvelé pendant la période normale payante.                                                 |
| Achat hors abonnement   | L'achat de tout produit qui n'est pas un abonnement à renouvellement automatique.                                                                                                   |
| Expiration              | Quand un abonnement expire.                                                                                                                                                         |
| Problème de facturation | Lorsqu'il y a eu un problème en essayant de charger l'utilisateur.                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2}

Pour les événements qui incluent les revenus, RevenueCat enregistrera automatiquement ce montant avec l'événement au Brésil, tels que les conversions d'essai et les renouvellements.

## Utiliser cette intégration

Après avoir configuré les paramètres de Braze dans RevenueCat, les événements commenceront automatiquement à s'écouler de RevenueCat à Braze sans aucune autre action de votre part.

## Personnalisation

### Ajouter une clé API sandbox pour les tests

Si vous ne fournissez qu'une seule clé API Braze REST à RevenueCat, seuls les événements de production seront envoyés. Si vous voulez également envoyer des événements de test sandbox, [créez une autre clé API REST de Braze][11] et ajoutez-la à vos paramètres Braze dans RevenueCat.
[3]: {% image_buster /assets/img/revenuecat/braze_settings_in_revenuecat.png %}

[2]: {{site.baseurl}}/api/objects_filters/user_alias_object/

[2]: {{site.baseurl}}/api/objects_filters/user_alias_object/

[2]: {{site.baseurl}}/api/objects_filters/user_alias_object/

[2]: {{site.baseurl}}/api/objects_filters/user_alias_object/

[2]: {{site.baseurl}}/api/objects_filters/user_alias_object/
[4]: https://docs.revenuecat.com/docs/subscriber-attributes
[8]: https://docs.revenuecat.com/docs/configuring-sdk
[9]: https://app.revenuecat.com/login
[11]: {{site.baseurl}}/api/basics/#app-group-rest-api-keys
