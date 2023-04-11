---
hidden: true
nav_title: Contrôle fin du trafic du réseau
article_title: Contrôle fin du trafic réseau pour iOS
platform: iOS
page_order: 1
description: "Cet article couvre le contrôle fin du trafic réseau pour votre application iOS."

---

# Contrôle fin du trafic réseau

## Demander des politiques de traitement

Braze permet à l’utilisateur de contrôler le trafic réseau à l’aide des protocoles suivants :

### Traitement automatique des demandes

***`ABKRequestProcessingPolicy` valeur enum : `ABKAutomaticRequestProcessing`***

- C’est la valeur de **politique de demande par défaut**.
- Le SDK Braze gérera automatiquement toutes les communications du serveur, y compris :
    - Suppression des données d’événements personnalisés et d’attributs sur les serveurs de Braze
    - Mise à jour des cartes de contenu et des geofences
    - Demander de nouveaux messages in-app
- Des requêtes serveur immédiates sont effectuées lorsque des données utilisateur sont requises pour les fonctionnalités de Braze, telles que les messages in-app.
- Pour minimiser la charge serveur, Braze effectue des purges périodiques des nouvelles données utilisateur au bout de quelques secondes.

Les données peuvent être transférées manuellement vers les serveurs de Braze à tout moment en utilisant la méthode suivante :

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

***`ABKRequestProcessingPolicy` valeur enum : `ABKManualRequestProcessing`***

- Ce protocole est le même que le traitement automatique des requêtes sauf :
    - Les attributs personnalisés et les données d’événements personnalisés ne sont pas automatiquement purgés du serveur tout au long de la session utilisateur.
- Braze effectuera toujours des requêtes réseau automatiques pour les fonctionnalités internes, telles que la demande de messages in-app, la création de modèles Liquid dans les messages in-app, le Geofences et le suivi de la localisation. Pour plus de détails, voir la déclaration `ABKRequestProcessingPolicy` dans [`Appboy.h`][4]. Lorsque ces demandes internes sont effectuées, les attributs personnalisés stockés localement et les données d’événements personnalisés peuvent être purgés vers le serveur Braze, selon le type de demande.

Les données peuvent être transférées manuellement vers les serveurs de Braze à tout moment en utilisant la méthode suivante :

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

Ces politiques peuvent être définies au démarrage de l’application à partir de la méthode [`startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions`][3]. Dans le dictionnaire `appboyOptions`, définissez `ABKRequestProcessingPolicyOptionKey` comme indiqué dans l’extrait de code suivant :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
NSDictionary *appboyOptions = @{
  // Other entries
  ABKRequestProcessingPolicyOptionKey : @(ABKAutomaticRequestProcessing)
};
```

{% endtab %}
{% tab swift %}

```swift
let appboyOptions: [AnyHashable: Any] = [
  // Other entries
  ABKRequestProcessingPolicyOptionKey: ABKRequestProcessingPolicy.automaticRequestProcessing.rawValue
]
```

{% endtab %}
{% endtabs %}

### Définir la politique de demande au moment de l’exécution

La politique de traitement de demande peut également être définie pendant l’exécution via la propriété `requestProcessingPolicy` sur `Appboy` :

{% tabs %}
{% tab OBJECTIVE-C %}

```objc
// Sets the request processing policy to automatic (the default value)
[Appboy sharedInstance].requestProcessingPolicy = ABKAutomaticRequestProcessing;
```

{% endtab %}
{% tab swift %}

```swift
// Sets the request processing policy to automatic (the default value)
Appboy.sharedInstance()?.requestProcessingPolicy = ABKRequestProcessingPolicy.automaticRequestProcessing
```

{% endtab %}
{% endtabs %}

## Arrêt manuel de la communication serveur à la volée

Si, à tout moment, une communication serveur « à la volée » doit être interrompue, vous devez employer la méthode suivante :

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

Après avoir employé cette méthode, vous devez réinitialiser le mode de traitement de demande sur automatique. C’est pourquoi nous vous recommandons de ne l’utiliser que si le système d’exploitation vous oblige à arrêter les tâches d’arrière-plan ou quelque chose de similaire.

[3]: https://appboy.github.io/appboy-ios-sdk/docs/interface_appboy.html#aa9f1bd9e4a5c082133dd9cc344108b24
[4]: https://github.com/Appboy/appboy-ios-sdk/blob/master/AppboyKit/include/Appboy.h
