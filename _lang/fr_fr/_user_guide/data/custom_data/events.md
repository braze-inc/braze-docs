---
nav_title: Événements
article_title: Événements
page_order: 0
page_type: reference
description: "Cet article décrit les différents événements de Braze - événements standard, événements d'achat et événements personnalisés - ainsi que leur utilité."
---

# Événements 

> Cette page présente les différents événements de Braze et leur objectif.

Braze utilise quelques types d'événements différents pour fournir une compréhension complète du comportement et de l'engagement des utilisateurs avec votre marque. Chaque type d'événement a un objectif unique :

- [Événements standard](#standard-events): Fournir une compréhension de base de l'engagement des utilisateurs avec votre application ou votre site.
- [Événements d’achat](#purchase-events) : Crucial pour comprendre le comportement d'achat des utilisateurs et pour le suivi des chiffres d'affaires. 
- [Événements personnalisés](#custom-events): Fournissez des informations plus approfondies sur les comportements des utilisateurs qui sont uniques à votre appli ou à votre entreprise.

En suivant ces différents types d'événements, vous pouvez acquérir une connaissance plus approfondie de vos utilisateurs, ce qui peut éclairer vos stratégies marketing, vous aider à optimiser votre application et vous donner les moyens d'offrir une expérience utilisateur plus personnalisée. Plongeons dans l'aventure !

## Événements standard

Dans Braze, les événements standard sont des actions prédéfinies que les utilisateurs peuvent effectuer dans votre appli et que Braze suit automatiquement après que vous avez intégré le SDK de Braze. Voici quelques exemples d'événements types :

- Lancement de l'application
- [Achat](#purchase-events)
- Lancer la session
- Fin de session
- A cliqué sur la notification push
- A ouvert l’e-mail

En tant que marketeur, vous pouvez utiliser ces événements standard pour comprendre le comportement et l'engagement des utilisateurs avec votre appli. Par exemple, vous pouvez voir à quelle fréquence les utilisateurs lancent votre application ou combien d'achats sont effectués. Ces informations peuvent s'avérer précieuses pour la création de campagnes marketing ciblées.

Il est important de noter que si les événements standards sont automatiquement suivis par Braze, les événements d'achat, les événements personnalisés et les attributs personnalisés doivent être configurés par votre équipe de développement en fonction de vos besoins et objectifs spécifiques.

## Événements d’achat

Les événements d'achat sont un moyen d'enregistrer et de suivre les achats effectués par vos utilisateurs. Il s'agit d'un type d'événement standard disponible par défaut après l'intégration du SDK Braze. De ce fait, lorsque vous utilisez les événements d'achat pour effectuer le suivi des achats, vous pouvez contrôler vos revenus au fil du temps et sur différentes sources de revenus, directement depuis Braze.

Les événements d'achat enregistrent les informations clés suivantes concernant un achat :

- ID du produit (généralement le nom ou la catégorie du produit)
- Devise
- Prix
- Quantité

Vous pouvez ensuite utiliser ces données pour segmenter vos utilisateurs en fonction de leur valeur vie client, de leur fréquence d'achat, de leurs achats spécifiques, etc.

Braze prend également en charge les achats dans plusieurs devises. Si un achat est déclaré dans une devise autre que le dollar américain, il sera affiché dans le tableau de bord de Braze en dollars américains, sur la base du taux de change en vigueur à la date à laquelle l'achat a été déclaré.

Pour en savoir plus, consultez notre article consacré aux [événements d'achat]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/).

{% details Exemple de mise en œuvre %}

Notez que la mise en œuvre effective des événements d'achat nécessitera quelques connaissances techniques, car elle implique l'intégration du SDK de Braze à votre appli. Votre gestionnaire de la satisfaction client guidera votre équipe tout au long de ce processus dans le cadre de votre onboarding, mais les étapes générales sont les suivantes :

1. **Intégrez le SDK Braze :** Avant d'enregistrer des événements, vous devez intégrer le SDK de Braze dans votre application.
2. **Enregistrez l'événement d'achat :** Une fois le SDK intégré, vous pouvez enregistrer un événement d’achat dès qu'un utilisateur effectue un achat dans votre application. Ceci se fait généralement dans la fonction ou la méthode appelée lorsqu'un achat est effectué.

Voici un exemple d'enregistrement d'un événement d'achat dans une application iOS à l'aide de Swift :

```swift
Appboy.sharedInstance()?.logPurchase("product_name", inCurrency: "USD", atPrice: NSDecimalNumber(string: "1.99"), withQuantity: 1)
```

Dans cet exemple, "nom_du_produit" est le nom du produit acheté, "USD" est la devise de l'achat, "1,99" est le prix du produit et "1" est la quantité achetée.

{:start="3"}
3\. **Visualisez l'événement d'achat dans le tableau de bord de Braze :** Une fois l'événement d'achat enregistré, vous pouvez le consulter dans le tableau de bord de Braze. Vous pouvez utiliser ces données pour analyser vos revenus, segmenter vos utilisateurs, et bien plus encore.

N'oubliez pas que la mise en œuvre exacte peut varier en fonction de la plateforme (iOS, Android, Web) et des exigences spécifiques de votre application. 

{% enddetails %}

## Événements personnalisés

Les événements personnalisés sont des événements que vous définissez en fonction des actions spécifiques que vous souhaitez suivre au sein de votre app ou de votre site. Braze ne les suit pas automatiquement : vous devez configurer manuellement ces événements dans votre implémentation du SDK Braze. Les événements personnalisés peuvent aller de l'achèvement d'un niveau dans un jeu à la mise à jour des informations de profil d'un utilisateur.

Voici un exemple d'enregistrement d'un événement personnalisé dans une app iOS à l'aide de Swift :

```swift
Appboy.sharedInstance()?.logCustomEvent("completed_level")
```

Dans cet exemple, "completed_level" est le nom de l'événement personnalisé qui est enregistré lorsqu'un utilisateur termine un niveau dans un jeu. Cet événement personnalisé est ensuite enregistré sur leur profil utilisateur dans Braze, que vous pouvez utiliser pour déclencher des campagnes et personnaliser les messages.

Pour en savoir plus, consultez notre article consacré aux [événements personnalisés]({{site.baseurl}}/user_guide/data/custom_data/custom_events/).

{% details Exemple de mise en œuvre %}

Tout comme les événements d’achat, les événements personnalisés nécessitent une configuration supplémentaire. Voici un processus général de mise en œuvre des événements personnalisés dans Braze :

1. **Intégrez le SDK Braze :** Avant de pouvoir enregistrer des événements, vous devez intégrer le SDK de Braze dans votre application.
2. **Définissez votre événement personnalisé :** Déterminez l'action de votre application que vous souhaitez suivre en tant qu'événement personnalisé. Il peut s'agir de tout ce qui est significatif pour votre application, comme un utilisateur qui termine un niveau dans un jeu, un utilisateur qui met à jour son profil ou un utilisateur qui effectue un type d'achat spécifique.
3. **Enregistrez l'événement personnalisé :** Après avoir défini votre événement personnalisé, vous pouvez l'enregistrer dans le code de votre application. Cela se fait généralement dans la fonction ou la méthode qui est appelée lorsque l'action se produit.

Voici un exemple d'enregistrement d'un événement personnalisé dans une app iOS à l'aide de Swift :

```swift
Appboy.sharedInstance()?.logCustomEvent("updated_profile")
```

Dans cet exemple, "updated_profile" est le nom de l'événement personnalisé qui est enregistré lorsqu'un utilisateur met à jour son profil.

{:start="4"}
4\. **Ajoutez des propriétés à votre événement personnalisé (facultatif) :** Si vous souhaitez capturer des détails supplémentaires sur l'événement personnalisé, vous pouvez lui ajouter des propriétés. Pour ce faire, vous devez transmettre un dictionnaire de propriétés lorsque vous enregistrez l'événement.

Voici un exemple d'enregistrement d'un événement personnalisé avec des propriétés dans une app iOS à l'aide de Swift :

```swift
let properties: [AnyHashable: Any] = ["Property Name": "Property Value"]
Appboy.sharedInstance()?.logCustomEvent("updated_profile", withProperties: properties)
```

Dans cet exemple, l'événement personnalisé a une propriété appelée "Nom de la propriété" avec une valeur de "Valeur de la propriété".

{:start="5"}
5\. **Affichez l'événement personnalisé dans le tableau de bord de Braze :** Une fois l'événement personnalisé enregistré, vous pouvez le consulter dans le tableau de bord de Braze. Vous pouvez utiliser ces données pour analyser le comportement des utilisateurs, les segmenter, etc.

{% enddetails %}

<!--

### Using custom events instead of purchase events to track purchases

You might prefer to use custom events to track purchases if you need to capture more specific or additional information about the purchase that the standard purchase event doesn't cover. Here's what you can do with custom events that you can't accomplish with purchase events:

- **Custom definitions:** Custom events can be defined based on any significant action within your app. This level of customization is not available with standard purchase events, which are predefined and specifically designed to track purchases.
- **Additional properties:** You can log additional properties to custom events that provide more context about the event. For example, you could log a custom event when a user makes a purchase and include properties such as the product category or the payment method. This is not possible with standard purchase events, which have a fixed schema that only tracks the product name, currency, price, and quantity.
- **Event frequency:** Custom events allow you to track the frequency of specific actions. With purchase events, you can only track the occurrence of purchases, not other types of actions.

#### Use case 1

Let's say you have an eCommerce app, and you want to track the purchase itself and the product category. The standard purchase event in Braze does not capture this level of detail, so you could use a custom event instead.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Product Category": "Electronics"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the product category is "Electronics". Now you can segment your users based on the product categories they purchase from.

#### Use case 2

Consider a fitness app where users can purchase personal training sessions or premium workout plans. In this case, you might want to track these purchases as custom events to capture additional details about the purchase.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Workout Plan": "10 Sessions Personal Training"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the workout plan is "10 Sessions Personal Training". Now you can segment your users based on the types of workout plans they purchase.

-->


