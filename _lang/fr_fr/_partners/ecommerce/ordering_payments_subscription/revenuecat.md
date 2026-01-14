---
nav_title: RevenueCat
article_title: RevenueCat
description: "L'intégration de RevenueCat et Braze vous permet de synchroniser automatiquement les événements du cycle de vie des achats et des abonnements de vos clients sur les différentes plateformes. Cela vous permet de créer des campagnes qui réagissent à l'étape du cycle de vie de l'abonnement de vos clients, par exemple en engageant le dialogue avec les clients qui se sont désabonnés pendant leur essai gratuit ou en envoyant des rappels aux clients qui ont des problèmes de facturation."
alias: /partners/revenuecat/
page_type: partner
search_tag: Partner

---

# RevenueCat

> [RevenueCat](https://www.revenuecat.com/) est la seule source de vérité pour votre état d'abonnement sur iOS, Android et le web. Que vous soyez en train de créer une nouvelle application ou que vous ayez déjà des millions d'abonnés, vous pouvez utiliser RevenueCat pour créer des achats in-app multiplateformes, gérer vos produits et vos abonnés, et analyser vos données - sans code serveur.

_Cette intégration est maintenue par RevenueCat._

## À propos de l'intégration

L'intégration de RevenueCat et Braze vous permet de synchroniser automatiquement les événements du cycle de vie des achats et des abonnements de vos clients sur les différentes plateformes. Cela vous permet de créer des campagnes qui réagissent à l'étape du cycle de vie de l'abonnement de vos clients, par exemple en engageant le dialogue avec les clients qui se sont désabonnés pendant leur essai gratuit ou en envoyant des rappels aux clients qui ont des problèmes de facturation.

## Conditions préalables

Au minimum, vous devrez activer l'intégration depuis le tableau de bord de RevenueCat pour connecter RevenueCat à Braze. Si vous utilisez le SDK Braze, vous pouvez utiliser les SDK RevenueCat et Braze conjointement pour améliorer l'intégration en vous assurant que le même identifiant client est utilisé dans les deux systèmes.

| Exigence | Description |
|---|---|
| Compte et application RevenueCat | Un [compte RevenueCat](https://app.revenuecat.com/login) est nécessaire pour bénéficier de ce partenariat. Vous devez également disposer d'une application RevenueCat configurée. |
| RevenueCat SDK | En plus du SDK Braze requis, nous vous recommandons d'installer le [SDK RevenueCat](https://docs.revenuecat.com/docs/configuring-sdk) pour fournir des alias utilisateurs à RevenueCat. |
| Instance de Braze | Votre instance Braze peut être obtenue auprès de votre gestionnaire d'onboarding Braze ou sur la [page d'aperçu des API ]({{site.baseurl}}/api/basics/#endpoints).<br><br>RevenueCat nécessite que l'instance Braze envoie les données côté serveur au bon endpoint REST de Braze. |
| Clé d'API REST Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Clé API REST du test de Braze (facultatif) | Une clé API de test peut être utilisée pour les achats de test et de production si vous souhaitez que ces requêtes soient envoyées à des instances Braze distinctes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation 

- Déclenchez une campagne d'onboarding mettant en avant vos fonctionnalités premium lorsqu'un client commence un essai gratuit.
- Envoyez un rappel pour mettre à jour les informations de facturation lorsqu'un événement "Problème de facturation" est reçu.
- Envoyez une enquête de satisfaction après qu'un client a annulé un essai gratuit. 

## Intégration

### Étape 1 : Définir l'identité de l'utilisateur de Braze

Dans le SDK Braze, vous pouvez définir l'ID utilisateur Braze pour qu'il corresponde à l'ID utilisateur de l'application RevenueCat, ce qui garantit que les événements envoyés depuis Braze et RevenueCat peuvent être synchronisés avec le même utilisateur.

Configurez le SDK de Braze avec le même ID d'utilisateur d'application que RevenueCat ou utilisez la méthode `.changeUser()` du SDK de Braze.

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

#### Envoi de l'objet alias d'utilisateur à Braze (facultatif) 

Si vous souhaitez envoyer un identifiant unique différent de l'ID de l'utilisateur de l'application RevenueCat, mettez à jour les utilisateurs en utilisant les données suivantes comme attributs d'abonné RevenueCat.

| Clé | Description |
|---|---|
| `$brazeAliasName` | Le site `alias_name` de Braze dans l'[objet alias d'utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/) |
| `$brazeAliasLabel` | Le site `alias_label` de Braze dans l'[objet alias d'utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ces deux attributs sont nécessaires pour que l'[objet alias d'utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/) soit envoyé avec vos données d'événement. Ces propriétés peuvent être définies manuellement, comme tout autre [attribut de l'utilisateur de RevenueCat](https://docs.revenuecat.com/docs/subscriber-attributes). Des extraits de code sont présentés à la première étape.

### Étape 2 : Envoyez des événements RevenueCat à Braze

Après avoir configuré le SDK d'achat RevenueCat et le SDK Braze pour qu'ils aient la même identité d'utilisateur, vous pouvez activer l'intégration et configurer les noms d'événements à partir du tableau de bord de Braze.

1. Naviguez vers votre projet dans le tableau de bord RevenueCat et recherchez la carte **Intégrations** dans le menu de gauche. Sélectionnez **\+ Nouveau**.
2. Ensuite, sélectionnez **Braze** parmi les intégrations disponibles et ajoutez votre instance Braze et la clé de l'API REST de Braze. 
3. Saisissez les noms d'événements que RevenueCat enverra ou choisissez les noms d'événements par défaut. Vous trouverez plus de détails sur les événements disponibles à l'[étape 3.](#configure-event-names)
4. Spécifiez si vous voulez que RevenueCat génère le rapport des recettes (après la commission de la boutique d’applications) ou le chiffre d'affaires (ventes brutes).

![Paramètres de Braze dans RevenueCat avec des champs pour l'instance de Braze, l'identifiant de la clé API et l'identifiant du bac à sable.]({% image_buster /assets/img/revenuecat/braze_settings_in_revenuecat.png %})

### Étape 3 : Configurer les noms des événements {#configure-event-names}

Saisissez les noms des événements que RevenueCat enverra ou sélectionnez les noms d'événements par défaut en sélectionnant **Utiliser les noms d'événements par défaut**. Les événements que RevenueCat permet d'envoyer sont décrits dans le tableau suivant.

| Événement | Description |
|---|---|
| Achat initial | Le premier achat d'un produit d'abonnement à renouvellement automatique qui ne contient pas d'essai gratuit. |
| Début de l’essai | Le début d'un essai gratuit d'un produit d'abonnement à renouvellement automatique. |
| Essai gratuit converti | Lorsqu'un produit d'abonnement à renouvellement automatique passe d'une période d'essai gratuite à une période payante normale. |
| Procès annulé | Lorsqu'un utilisateur désactive le renouvellement d'un produit d'abonnement à renouvellement automatique pendant une période d'essai gratuite. |
| Renouvellement | Lorsqu'un produit d'abonnement à renouvellement automatique est renouvelé ou qu'un utilisateur rachète le produit d'abonnement à renouvellement automatique après une interruption de son abonnement. |
| Annulation | Lorsqu'un utilisateur désactive les renouvellements pour un produit d'abonnement à renouvellement automatique pendant la période payée normale. |
| Achat sans abonnement | L'achat de tout produit qui n'est pas un abonnement à renouvellement automatique. |
| Expiration | Lorsqu'un abonnement expire. |
| Problème de facturation | En cas de problème lors de la facturation à l'utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour les événements qui incluent des revenus, RevenueCat enregistrera automatiquement ce montant avec l'événement dans Braze, comme les conversions d'essais et les renouvellements.

## Grâce à cette intégration

Après avoir configuré les paramètres de Braze dans RevenueCat, les événements commenceront automatiquement à circuler de RevenueCat vers Braze sans aucune autre action de votre part.

## Personnalisation

### Ajoutez une clé API d’environnement de test pour les tests.

Si vous ne fournissez qu'une seule clé API REST de Braze à RevenueCat, seuls les événements de production seront envoyés. Si vous souhaitez également envoyer des événements de test en bac à sable, [créez une autre clé API REST Braze]({{site.baseurl}}/api/basics/#app-group-rest-api-keys) et ajoutez-la à vos paramètres Braze dans RevenueCat.


