---
nav_title: RevenueCat
article_title: RevenueCat
description: "L’intégration entre RevenueCat et Braze permet de synchroniser automatiquement les événements d’achat et d’abonnement de vos clients sur plusieurs plateformes. Cela vous permet de créer des campagnes qui réagissent en fonction de l’étape du cycle de vie d’abonnement de vos clients, par exemple pour communiquer avec des clients qui se sont désinscrits pendant leur essai gratuit ou envoyer des rappels aux clients en défaut de paiement."
alias: /partners/revenuecat/
page_type: partner
search_tag: Partenaire

---

# RevenueCat

> [RevenueCat](https://www.revenuecat.com/) est une source unique pour votre statut d’abonnement sur iOS, Android et Web. Que vous conceviez une nouvelle application ou que vous ayez déjà des millions d’utilisateurs abonnés, vous pouvez utiliser RevenueCat pour créer des achats in-app sur plusieurs plateformes, gérer vos produits et vos abonnés, et analyser vos données sans aucun code serveur.

L’intégration entre RevenueCat et Braze permet de synchroniser automatiquement les événements d’achat et d’abonnement de vos clients sur plusieurs plateformes. Cela vous permet de créer des campagnes qui réagissent en fonction de l’étape du cycle de vie d’abonnement de vos clients, par exemple pour communiquer avec des clients qui se sont désinscrits pendant leur essai gratuit ou envoyer des rappels aux clients en défaut de paiement.

## Conditions préalables

Vous devrez au minimum activer l’intégration depuis le tableau de bord de RevenueCat pour connecter RevenueCat à Braze. Si vous utilisez le SDK de Braze, vous pouvez combiner les SDK de RevenueCat et de Braze pour améliorer l’intégration en garantissant que le même identifiant client est utilisé dans les deux systèmes.

| Condition | Description |
|---|---|
| Compte et application RevenueCat | Un compte [RevenueCat][9] est requis pour profiter de ce partenariat. Vous devez également disposer d’une application RevenuCat configurée. |
| SDK RevenueCat | En plus du SDK de Braze, nous vous recommandons d’installer le [SDK de RevenueCat][8] pour fournir des alias d’utilisateur à RevenuEcat. |
| Instance de Braze | Votre instance Braze peut être obtenue auprès de votre gestionnaire d’onboarding Braze ou est disponible sur la [page API overview]({{site.baseurl}}/api/basics/#endpoints).<br><br>RevenueCat nécessite l’instance Braze pour envoyer l’intégration côté serveur au bon endpoint REST de Braze. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Clé API REST test de Braze (facultatif) | Une clé API test qui peut être utilisée pour effectuer des tests ou des achats de production si vous souhaitez que ces requêtes soient envoyées à des instances de Braze séparées. |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d’utilisation 

- Déclencher une campagne d’onboarding mettant en évidence vos fonctionnalités premium lorsqu’un client commence un essai gratuit.
- Envoyer un rappel pour mettre à jour les informations de facturation lorsqu’un événement « Problème de facturation » est reçu.
- Envoyer une enquête après qu’un client ait annulé un essai gratuit. 

## Intégration

### Étape 1 : Définir l’ID utilisateur Braze

Dans le SDK de Braze, vous pouvez définir l’ID utilisateur Braze pour qu’il corresponde à l’ID d’utilisateur de l’application RevenueCat et vous assurer que les événements envoyés depuis Braze et RevenueCat puissent être synchronisés avec le même utilisateur.

Configurez le SDK de Braze avec le même ID d’utilisateur de l’application que celui de RevenueCat ou utilisez la méthode `.changeUser()` du SDK de Braze.

{% tabs local %}
{% tab swift %}
```swift
// Configure Purchases SDK
Purchases.configure(withAPIKey: "public_sdk_key", appUserID: "my_app_user_id")

// Change user in Braze SDK
Appboy.sharedInstance()?.changeUser("my_app_user_id")

// Optional User Alias Object attributes
Purchases.shared.setAttributes(["$brazeAliasName" : "name", 
                             "$brazeAliasLabel" : "label"])
```
{% endtab %}
{% tab objective-c %}
```objc
// Configure Purchases SDK
[RCPurchases configureWithAPIKey:@"public_sdk_key" appUserID:@"my_app_user_id"];

// Change user in Braze SDK
[[Appboy sharedInstance] changeUser:@"my_app_user_id"];

// Optional User Alias Object attributes
[[RCPurchases sharedPurchases] setAttributes:@{
    @"$brazeAliasName": @"name",
    @"$brazeAliasLabel": @"label"
}];
```
{% endtab %}
{% tab java %}
```java
// Configure Purchases SDK
Purchases.configure(this, "public_sdk_key", "my_app_user_id");

// Change user in Braze SDK
Braze.getInstance(context).changeUser(my_app_user_id);

// Optional User Alias Object attributes
Map<String, String> attributes = new HashMap<String, String>();
attributes.put("$brazeAliasName", "name");
attributes.put("$brazeAliasLabel", "label");

Purchases.getSharedInstance().setAttributes(attributes);
```
{% endtab %}
{% endtabs %}

#### Envoyer un objet alias d’utilisateur à Braze (facultatif) 

Si vous souhaitez envoyer un identifiant utilisateur unique différent de l’ID d’utilisateur de l’application RevenueCat, mettez à jour les utilisateurs avec les données suivantes comme attributs d’utilisateurs abonnés RevenueCat.

| Clé | Description |
|---|---|
| `$brazeAliasName` | Le `alias_name` de Braze dans l’[objet alias utilisateur][2] |
| `$brazeAliasLabel` | Le `alias_label` de Braze dans l’[objet alias utilisateur][2] |
{: .reset-td-br-1 .reset-td-br-2}

Les deux attributs sont obligatoires pour que l’[objet alias utilisateur][2] soit envoyer avec vos données d’événement. Ces propriétés peuvent être définies manuellement, comme n’importe quelle autre [Attribut d’utilisateur abonné RevenueCat][4]. Des exemples d’extrait de code sont présentés à l’étape 1.

### Étape 2 : Envoyer des événements RevenuCat à Braze

Après avoir configuré le SDK d’achats de RevenueCat et le SDK de Braze pour qu’ils aient le même ID utilisateur, vous pouvez activer l’intégration et configurer les noms d’événements depuis le tableau de bord de RevenueCat.

1. Accédez à votre projet dans le tableau de bord de RevenueCat et recherchez la carte **Integrations** dans le menu de gauche. Cliquez sur **+ New (+ Nouveau)**.
2. Ensuite, sélectionnez **Braze** à partir de la liste des intégrations disponibles et ajoutez votre instance Braze et la clé API REST de Braze. 
3. Saisissez les noms des événements que RevenueCat enverra ou choisissez les noms d’événements par défaut. Vous trouverez plus d’informations sur les événements disponibles à l’[étape 3](#configure-event-names).
4. Indiquez si vous souhaitez que RevenueCat présente les recettes (après la coupure de l’App Store) ou le chiffre d’affaires (ventes brutes).

![Paramètres de Braze dans RevenueCat avec champs pour instance de Braze, identificateur de clé API et identifiant de sandbox.][3]

### Étape 3 : Configurer les noms d’événement{#configure-event-names}

Saisissez les noms des événements que RevenueCat enverra ou choisissez les noms d’événements par défaut en sélectionnant **Use Default Event Names (Utiliser les noms d’événements par défaut)**. Les événements pris en charge par RevenueCat sont décrits dans le tableau suivant.

| Événement | Description |
|---|---|
| Achat initial | Premier achat d’un produit avec abonnement renouvelé automatiquement qui ne contient pas d’essai gratuit. |
| Essai démarré | Le début d’un essai gratuit pour un produit avec abonnement renouvelé automatiquement. |
| Essai converti | Lorsqu’un produit avec abonnement renouvelé automatiquement convertit un essai gratuit en un abonnement normal. |
| Trial Canceled (Essai annulé) | Lorsqu’un utilisateur désactive le renouvellement d’un produit avec abonnement renouvelé automatiquement pendant une période d’essai gratuite. |
| Renouvellement | Lorsque l’abonnement d’un produit avec abonnement renouvelé automatiquement est renouvelé, ou lorsqu’un utilisateur achète à nouveau un produit à renouvellement automatique après s’être désabonné pendant un certain temps. |
| Annulation | Lorsqu’un utilisateur désactive le renouvellement d’un produit avec abonnement renouvelé automatiquement pendant la période d’abonnement. |
| Achat sans abonnement | L’achat de tout produit sans abonnement renouvelé automatiquement. |
| Expiration | Lorsqu’un abonnement expire. |
| Problème de facturation | Lorsqu’un problème s’est produit au moment de facturer un utilisateur. |
{: .reset-td-br-1 .reset-td-br-2}

Pour les événements qui incluent le chiffre d’affaires, RevenueCat enregistrera automatiquement ce montant avec l’événement dans Braze, comme les conversions d’essai et les renouvellements.

## Comment utiliser cette intégration

Après avoir configuré les paramètres de Braze dans RevenueCat, les événements commenceront automatiquement à être transférés de RevenueCat à Braze sans aucune autre action de votre part.

## Personnalisation

### Ajouter une clé API sandbox pour les tests

Si vous ne fournissez qu’une seule clé API REST Braze à RevenueCat, seuls les événements de production seront envoyés. Si vous souhaitez également envoyer des événements de test de sandbox, [créez une autre clé API REST Braze][11] et ajoutez-la à vos paramètres Braze dans RevenueCat.

[2]: {{site.baseurl}}/api/objects_filters/user_alias_object/
[3]: {% image_buster /assets/img/revenuecat/braze_settings_in_revenuecat.png %}
[4]: https://docs.revenuecat.com/docs/subscriber-attributes
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[8]: https://docs.revenuecat.com/docs/configuring-sdk
[9]: https://app.revenuecat.com/login
[11]: {{site.baseurl}}/api/basics/#app-group-rest-api-keys
