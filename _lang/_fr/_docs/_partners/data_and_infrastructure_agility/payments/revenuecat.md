---
nav_title: RevenueCat
description: "L'intégration de RevenueCat et Braze vous permet de synchroniser automatiquement les événements de cycle de vie d'achat et d'abonnement de vos clients sur toutes les plateformes. Cela vous permet de construire des campagnes qui réagissent à la phase de cycle de vie de l'abonnement de vos clients, comme s'engager avec les clients qui se sont retirés pendant leur essai gratuit ou envoyer des rappels aux clients avec des problèmes de facturation."
alias: /fr/partners/revenuecat/
page_type: partenaire
search_tag: Partenaire
---

# RevenueCat

> RevenueCat est la source unique de vérité pour votre statut d'abonnement sur iOS, Android et web. Que vous construisiez une nouvelle application ou que vous ayez déjà des millions d'abonnés, vous pouvez utiliser RevenueCat pour construire des achats inter-plateformes dans l'application, gérez vos produits et abonnés, et analysez vos données - aucun code serveur requis.

L'intégration de RevenueCat et Braze vous permet de synchroniser automatiquement les événements de cycle de vie d'achat et d'abonnement de vos clients sur toutes les plateformes. Cela vous permet de construire des campagnes qui réagissent à la phase de cycle de vie de l'abonnement de vos clients, comme s'engager avec les clients qui se sont retirés pendant leur essai gratuit ou envoyer des rappels aux clients avec des problèmes de facturation. Avec des données d'abonnement précises et à jour au Brésil, vous serez configuré pour turbocharger vos campagnes.

## Exigences

Au minimum, vous aurez besoin d'activer l'intégration depuis le tableau de bord RevenueCat pour connecter RevenueCat à Braze. Si vous utilisez le Braze SDK, vous pouvez utiliser ensemble les SDK RevenueCat et Braze pour améliorer l'intégration en veillant à ce que le même identifiant client soit utilisé dans les deux systèmes.

| Exigences                                   | Origine    | Accès                                                                                                                                                                               | Libellé                                                                                                                                            |
| ------------------------------------------- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte RevenueCat et application configurée | RevenueCat | [https://app.revenuecat.com/login][9]                                                                                                                                               | Vous devez avoir un compte actif et une application configurée avec RevenueCat pour utiliser leur service.                                         |
| Intégration de RevenueCat SDK               | RevenueCat | [https://docs.revenuecat.com/docs/configuring-sdk][8]                                                                                                                               | RevenueCat doit être installé avec succès dans votre application.                                                                                  |
| Intégration de Braze SDK                    | Brasero    | Pour plus de détails concernant les SDK de Braze, veuillez vous référer à notre documentation [iOS][5], [Android][6], et [Web][7].                                                  | Il est fortement recommandé d'installer le SDK Braze pour fournir des alias utilisateurs à RevenueCat.                                             |
| Instance de Braze                           | Brasero    | Votre instance Braze peut être obtenue auprès de votre gestionnaire d'intégration Braze ou peut être trouvée sur la page [Aperçu de l'API]({{site.baseurl}}/api/basics/#endpoints). | RevenueCat a besoin de l'instance Braze pour envoyer le serveur au bon point de terminaison Braze REST.                                            |
| Clé API Braze                               | Brasero    | Vos clés API peuvent être trouvées dans la __console développeur -> paramètres -> clés API REST__.                                                                                  | RevenueCat a besoin de la clé API pour envoyer le serveur au Brésil.                                                                               |
| Braze Test API Key (Optionnel)              | Brasero    | Vos clés API peuvent être trouvées dans la __console développeur -> paramètres -> clés API REST__.                                                                                  | Vous pouvez utiliser une clé API séparée pour les achats de test et de production si vous souhaitez les envoyer à des instances de Braze séparées. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration du serveur à serveur

### Étape 1 : Configurer les paramètres Braze dans RevenueCat

Naviguez vers votre application dans le tableau de bord RevenueCat, choisissez __Braze__ dans le menu des intégrations, et ajoutez votre instance Braze et votre clé API Braze.

!\[braze_settings_in_revenuecat\]\[3\]

### Étape 2 : Configurer les noms des événements dans RevenueCat

Entrez les noms d'événements que RevenueCat enverra ou sélectionnera à partir des noms d'événements par défaut en cliquant sur **Utiliser les noms d'événements par défaut**. Les événements que RevenueCat prend en charge l'envoi sont décrits ci-dessous.

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

RevenueCat enregistrera automatiquement ce montant avec l'événement à Braze pour les événements qui ont des revenus, tels que les conversions d'essai et les renouvellements.

### Étape 3 : Fixer l'identité de l'utilisateur Braze

Dans le Braze SDK, vous pouvez définir l'ID de l'utilisateur Braze pour qu'il corresponde à l'ID de l'utilisateur de l'application RevenueCat. De cette façon, les événements envoyés par Braze SDK et RevenueCat peuvent être synchronisés avec le même utilisateur.

Configurez le SDK Braze avec le même ID d'utilisateur d'application que RevenueCat ou utilisez la méthode `.changeUser()` sur le Braze SDK.

#### (Facultatif) Envoyer un alias d'utilisateur à Braze

Si vous voulez envoyer un autre identifiant d'utilisateur unique différent de celui de RevenueCat App ID, mettre à jour les utilisateurs avec les données ci-dessous en tant qu'attributs d'abonné RevenueCat.

| Clés               | Libellé                                                    |
| ------------------ | ---------------------------------------------------------- |
| `$brazeAliasName`  | Le Braze `alias_name` dans l'objet [Alias utilisateur][2]  |
| `$brazeAliasLabel` | Le Braze `alias_label` dans l'objet [Alias utilisateur][2] |
{: .reset-td-br-1 .reset-td-br-2}

Les deux attributs sont requis pour que l'objet [Alias Utilisateur][2] soit envoyé à côté de vos données d'événement. Ces propriétés peuvent être définies manuellement, comme n'importe quel attribut d'abonné [RevenueCat][4].

{% tabs %}
{% tab swift %}
```swift
// Configurer les achats SDK
Purchases.configure(withAPIKey: "public_sdk_key", appUserID: "my_app_user_id")

// Changer l'utilisateur dans Braze SDK
Appboy.sharedInstance()?. hangeUser("my_app_user_id")

// [Optional] Définir les attributs de l'objet User Alias
Purchases.shared. etAttributes(["$brazeAliasName" : "alias_name", 
                             "$brazeAliasLabel" : "alias_label"])
```
{% endtab %}
{% tab objective-c %}
```objc
// Configurer les achats SDK
[RCPurchases configureWithAPIKey:@"public_sdk_key" appUserID:@"my_app_user_id"];

// Changer l'utilisateur dans Braze SDK
[[Appboy sharedInstance] changeUser:@"my_app_user_id"];

// [Optional] Définir les attributs de l'objet User Alias
[[RCPurchases sharedPurchases] setAttributes:@{
    @"$brazeAliasName": @"alias_name",
    @"$brazeAliasLabel": @"alias_label"
}];
```
{% endtab %}
{% tab kotlin %}
```kotlin
// Configurer les achats de SDK
Purchases.configure(ceci, "public_sdk_key", "my_app_user_id");

// Change l'utilisateur dans Braze SDK
Braze.getInstance(this). hangeUser("my_app_user_id");

// [Optional] Définir les attributs de l'objet User Alias
Purchases.sharedInstance. etAttributes(mapOf("$brazeAliasName" à "alias_name",
                                             "$brazeAliasLabel" à "alias_label"));
```
{% endtab %}
{% tab java %}
```java
// Configurer les achats de SDK
Purchases.configure(ceci, "public_sdk_key", "my_app_user_id");

// Change l'utilisateur dans Braze SDK
Braze.getInstance(this). hangeUser("my_app_user_id");

// [Optional] Set User Alias Object Attributs
Map<String, String> attributes = new HashMap<String, String>();
attributs. ut("$brazeAliasName", "alias_name");
attributes.put("$brazeAliasLabel", "alias_label");

Purchases.getSharedInstance().setAttributes(attributes);
```
{% endtab %}
{% endtabs %}

## Personnalisation

### Ajouter une clé API Sandbox pour les tests

Seuls les événements d'achat de production seront envoyés si vous ne fournissez qu'une seule clé API de Braze REST à RevenueCat. Si vous voulez également envoyer des événements de test sandbox, [créez une autre clé API REST de Braze][11] et ajoutez-la à vos paramètres Braze dans RevenueCat.

## Utiliser cette intégration

Après avoir configuré les paramètres de Braze dans RevenueCat, les événements commenceront automatiquement à s'écouler de RevenueCat à Braze sans aucune autre action de votre part.

## Cas d'utilisation

- Déclenchez une campagne d'intégration mettant en évidence vos fonctionnalités premium lorsqu'un client commence un essai gratuit.
- Envoyer un rappel pour mettre à jour les informations de facturation lorsqu'un événement "Facturation" est reçu.
- Envoyer une enquête de rétroaction après qu'un client annule un essai gratuit.
[3]: {% image_buster /assets/img/revenuecat/braze_settings_in_revenuecat.png %}

[2]: {{site.baseurl}}/api/objects_filters/user_alias_object/

[2]: {{site.baseurl}}/api/objects_filters/user_alias_object/
[4]: https://docs.revenuecat.com/docs/subscriber-attributes
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[8]: https://docs.revenuecat.com/docs/configuring-sdk
[9]: https://app.revenuecat.com/login
[11]: {{site.baseurl}}/api/basics/#app-group-rest-api-keys