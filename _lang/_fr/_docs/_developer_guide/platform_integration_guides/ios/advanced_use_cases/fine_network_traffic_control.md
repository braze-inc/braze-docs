---
nav_title: Contrôle du trafic réseau Fine
article_title: Contrôle du trafic réseau Fine pour iOS
platform: iOS
page_order: 1
description: "Cet article couvre comment implémenter un contrôle du trafic réseau fin pour votre application iOS"
---

# Contrôle du trafic du réseau

## Règles de traitement des demandes

Braze permet à l'utilisateur de contrôler le trafic réseau en utilisant les protocoles suivants :

### Traitement automatique des demandes

__*`ABKRequestProcessingPolicy` valeur enum : `ABKAutomaticRequestProcessing`*__

- Ceci est la valeur **de la politique de requête par défaut**.
- Le Braze SDK gérera automatiquement toutes les communications du serveur, y compris :
    - Vider les données des événements personnalisés et des attributs aux serveurs de Braze
    - Mise à jour du flux de nouvelles, des fiches de contenu et des géorepérages
    - Demande de nouveaux messages dans l'application
- Les requêtes immédiates du serveur sont effectuées lorsque des données destinées aux utilisateurs sont requises pour toutes les fonctionnalités de Braze, telles que les messages intégrés à l'application.
- Pour minimiser la charge du serveur, Braze effectue des purges périodiques de nouvelles données utilisateur toutes les quelques secondes.

Les données peuvent être collectées manuellement sur les serveurs de Braze à tout moment en utilisant la méthode suivante :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

### Traitement manuel des demandes

__*`ABKRequestProcessingPolicy` valeur enum : `ABKManualRequestProcessing`*__

- Ce protocole est le même que le traitement automatique des requêtes **EXCEPTEZ**:
    - Les attributs personnalisés et les données d'événement personnalisés ne sont pas automatiquement vidés sur le serveur tout au long de la session utilisateur.
- Braze effectuera toujours des requêtes de réseau automatiques pour des fonctionnalités internes, telles que la demande de messages dans l'application, le modèle de liquide dans les messages In-App, les géofences et le suivi de localisation. Pour plus de détails, voir la déclaration `ABKRequestProcessingPolicy` dans [`Appboy.h`][4]. Lorsque ces demandes internes sont faites, les attributs personnalisés stockés localement et les données d'événement personnalisés peuvent être vidés sur le serveur Braze, selon le type de requête.

Les données peuvent être collectées manuellement sur les serveurs de Braze à tout moment en utilisant la méthode suivante :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

## Définition de la politique de traitement des demandes

### Définir la politique de demande au démarrage

Ces règles peuvent être définies au démarrage de l'application à partir de la méthode [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`][3]. Dans le dictionnaire `appboyOptions` , définissez la `ABKRequestProcessingPolicyOptionKey` comme indiqué ci-dessous :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
NSDictionary *appboyOptions = @{
  // Autres entrées
  ABKRequestProcessingOptionKey : @(ABKAutomaticRequestProcessing)
};
```

{% endtab %}
{% tab swift %}

```swift
let appboyOptions : [AnyHashable: Any] = [
  // Autres entrées
  ABKRequestProcessingPolicyOptionKey: ABKRequestProcessingPolicy.automaticRequestProcessing.rawValue
]
```

{% endtab %}
{% endtabs %}

### Définir la politique de requête lors de l'exécution

La politique de traitement des requêtes peut également être définie pendant l'exécution, via la propriété `requestProcessingPolicy` sur `Appboy`. Par exemple :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Définit la politique de traitement des requêtes à la valeur automatique (la valeur par défaut)
[Appboy sharedInstance].requestProcessingPolicy = ABKAutomaticRequestProcessing;
```

{% endtab %}
{% tab swift %}

```swift
// Définit la politique de traitement des requêtes à la valeur automatique (la valeur par défaut)
Appboy.sharedInstance()?.requestProcessingPolicy = ABKRequestProcessingPolicy.automaticRequestProcessing
```

{% endtab %}
{% endtabs %}

## Arrêt manuel de la communication du serveur en vol

Si à tout moment une communication serveur "en vol" doit être arrêtée, vous devez appeler la méthode suivante :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
[[Appboy sharedInstance] shutdownServerCommunication];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.shutdownServerCommunication();
```

{% endtab %}
{% endtabs %}

Après avoir appelé cette méthode, vous devez réinitialiser le mode de traitement des requêtes à l'automatique. Pour cette raison, nous vous recommandons de l'appeler uniquement si le système d'exploitation vous oblige à arrêter des tâches de fond ou quelque chose de similaire.

[3]: https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24
[4]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h
