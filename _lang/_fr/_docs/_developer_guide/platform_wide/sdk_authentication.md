---
nav_title: Authentification SDK
article_title: Authentification SDK
page_order: 5
description: "Cet article de référence couvre l'authentification SDK et la façon d'activer cette fonctionnalité dans le Braze SDK."
platform:
  - iOS
  - Android
  - Web
---

# Authentification SDK

L'authentification SDK vous permet de fournir une preuve cryptographique (côté serveur généré) aux requêtes SDK faites au nom des utilisateurs connectés. Lorsque cette fonctionnalité est activée dans votre application, le tableau de bord Braze peut être configuré pour rejeter les requêtes avec une signature JWT manquante ou non valide.

Lorsqu'elle est activée, cette fonctionnalité empêchera les requêtes non autorisées qui utilisent la clé d'API SDK de votre application pour les utilisateurs connectés, y compris :
- Envoi d'événements personnalisés, d'attributs, d'achats et de données de session
- Création de nouveaux utilisateurs dans votre groupe d'applications Braze
- Mise à jour des attributs de profil utilisateur standard
- Recevoir ou déclencher des messages

## Commencer

Il y a quatre étapes de haut niveau pour commencer:

1. [Intégration Server-Side][1] - Générer une paire de clés publique et privée, et utilisez votre clé privée pour créer un JWT (_JSON Web Token_) pour l'utilisateur connecté.<br><br>
2. [Intégration SDK][2] - Activez cette fonctionnalité dans le SDK Braze et demandez le jeton JWT généré à partir de votre serveur.<br><br>
3. [Ajout de clés publiques][3] - Ajoutez votre _clé publique_ au tableau de bord Braze dans la page "Gérer les paramètres".<br><br>
4. [Activer/désactiver l'application dans le tableau de bord Braze][4] - Basculer l'application de cette fonctionnalité dans le tableau de bord Braze sur la base d'une application par application.

## Intégration côté serveur {#server-side-integration}

### Générer une paire de clés publique/privée {#generate-keys}

Générer une paire de clés RSA publique/privée. La clé publique sera éventuellement ajoutée au tableau de bord Braze, tandis que la clé privée devrait être stockée de manière sécurisée sur votre serveur.

Nous recommandons une clé RSA avec 2048 bits à utiliser avec l'algorithme RS256 JWT.

{% alert warning %}
N'oubliez pas de garder vos clés privées _privées_. Ne jamais exposer ou coder en dur votre clé privée dans votre application ou votre site Web. Quiconque connaît votre clé privée peut emprunter l'identité ou créer des utilisateurs au nom de votre application.
{% endalert %}

### Créer un jeton web JSON pour l'utilisateur actuel {#create-jwt}

Une fois que vous avez votre clé privée, votre application côté serveur devrait l'utiliser pour renvoyer un JWT à votre application ou site web pour l'utilisateur actuellement connecté.

Généralement, cette logique peut aller là où votre application demande normalement le profil de l'utilisateur actuel; comme un point de connexion ou où votre application actualise le profil de l'utilisateur actuel.

Lors de la génération du JWT, les champs suivants sont attendus :

**En-tête JWT**

| Champ | Requis  | Libellé                                  |
| ----- | ------- | ---------------------------------------- |
| `alg` | **Oui** | L'algorithme pris en charge est `RS256`. |
| `typ` | **Oui** | Le type doit être égal à `JWT`.          |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

**Charge JWT**

| Champ      | Requis  | Libellé                                                                                                               |
| ---------- | ------- | --------------------------------------------------------------------------------------------------------------------- |
| `sous`     | **Oui** | Le "sujet" devrait être égal à l'ID de l'utilisateur que vous fournissez aux SDK Braze lors de l'appel à `changeUser` |
| `exp`      | **Oui** | La "expiration" de quand vous voulez que ce jeton expire.                                                             |
| `audonien` | Non     | La revendication "public" est optionnelle, et si elle est définie, devrait être égale `braze`                         |
| `iss`      | Non     | La revendication "émetteur" est optionnelle, et si elle est définie, devrait être égale à votre clé d'API SDK.        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Bibliothèques JWT

Pour en savoir plus sur les jetons Web JSON, ou pour parcourir les [nombreuses bibliothèques open source](https://jwt.io/#libraries-io) qui simplifient ce processus de signature, consultez [https://jwt. o](https://jwt.io).

## Intégration du SDK {#sdk-integration}

Cette fonctionnalité est disponible parmi les [versions SDK suivantes]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions):

{% sdk_min_versions web:3.3.0 ios:4.3.0 android:14.0.0 %}

### Activez cette fonctionnalité dans le Braze SDK.

Lorsque cette fonctionnalité est activée, le Braze SDK ajoutera la dernière JWT connue de l'utilisateur actuel aux requêtes de réseau faites à Braze Servers.

{% alert note %}
Ne vous inquiétez pas, l'initialisation avec cette seule option n'affectera en rien la collecte de données tant que vous n'aurez pas démarré l' [authentification](#braze-dashboard) dans le tableau de bord de Braze.
{% endalert %}

{% tabs %}
{% tab Javascript %}
Lors de l'appel à `initialiser`, définissez la propriété facultative `sdkAuthentication` à `true`.
```javascript
importer le braze à partir de "@braze/web-sdk";
braze.initialize("VOTRE-API-KEY-ICI", {
  baseUrl: "VOTRE-SDK-ENDPOINT-HERE",
  enableSdkAuthentication: true,
});
```
{% endtab %}
{% tab Java %}
Lors de la configuration de l'instance Appboy, appelez `setIsSdkAuthenticationEnabled` à `true`.
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```

Alternativement, vous pouvez ajouter `<bool name="com_braze_sdk_authentication_enabled">vrai</bool>` à votre braze.xml.
{% endtab %}
{% tab KOTLIN %}
Lors de la configuration de l'instance Appboy, appelez `setIsSdkAuthenticationEnabled` à `true`.
```kotlin
BrazeConfig.Builder brazeConfigBuilder = BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```

Alternativement, vous pouvez ajouter `<bool name="com_braze_sdk_authentication_enabled">vrai</bool>` à votre braze.xml.
{% endtab %}
{% tab Objective-C %}
Pour activer l'authentification SDK, ajoutez la clé `EnableSDKAuthentication` au dictionnaire `Braze` dans votre `. liste` le fichier et le définir à true.

Vous pouvez également activer l'authentification SDK lors de l'initialisation du SDK :

```objc
[Appboy startWithApiKey:@"VOTRE API-KEY"
            inApplication:application
        withLaunchOptions:launchOptions
        withAppboyOptions:@{ABKEnableSDKAuthenticationKey : @YES}];
```
{% endtab %}
{% tab Swift %}
Pour activer l'authentification SDK, ajoutez la clé `EnableSDKAuthentication` au dictionnaire `Braze` dans votre `. liste` le fichier et le définir à true.

Vous pouvez également activer l'authentification SDK lors de l'initialisation du SDK :

```swift
Appboy.start(withApiKey: "VOTRE-API-KEY",
                 in:application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableSDKAuthenticationKey : true ])
```
{% endtab %}
{% endtabs %}

### Définir le jeton JWT de l'utilisateur actuel

Chaque fois que votre application appelle la méthode Braze `changeUser` , fournissez également le jeton JWT qui était [généré côté serveur][4].

Vous pouvez également mettre à jour le jeton pour actualiser le jeton en milieu de session pour l'utilisateur actuel.

{% alert note %}
Gardez à l'esprit que `changeUser` ne doit être appelé que lorsque l'ID de l'utilisateur _a réellement changé_. Vous ne devriez pas utiliser cette méthode comme moyen de mettre à jour la signature si l'identifiant de l'utilisateur n'a pas changé.
{% endalert %}

{% tabs %}
{% tab Javascript %}
Fournissez le jeton JWT lorsque vous appelez `changeUser`:

```javascript
importer le braze depuis "@braze/web-sdk";
braze.changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER");
```

Ou, lorsque vous avez actualisé le jeton de l'utilisateur en milieu de session :

```javascript
importer le braze depuis "@braze/web-sdk";
braze.setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER");
```
{% endtab %}
{% tab Java %}

Fournissez le jeton JWT en appelant `appboy.changeUser`:

```java
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER");
```

Ou, lorsque vous avez actualisé le jeton de l'utilisateur en milieu de session :

```java
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER");
```
{% endtab %}
{% tab KOTLIN %}

Fournissez le jeton JWT en appelant `appboy.changeUser`:

```kotlin
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER")
```

Ou, lorsque vous avez actualisé le jeton de l'utilisateur en milieu de session :

```kotlin
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER")
```
{% endtab %}
{% tab Objective-C %}

Fournissez le jeton JWT lorsque vous appelez `changeUser`:

```objc
[[Appboy sharedInstance] changeUser:@"userId" sdkAuthSignature:@"signature"];
```

Ou, lorsque vous avez actualisé le jeton de l'utilisateur en milieu de session :

```objc
[[Appboy sharedInstance] setSdkAuthenticationSignature:@"signature"];
```
{% endtab %}
{% tab Swift %}

Fournissez le jeton JWT lorsque vous appelez `changeUser`:

```swift
Appboy.sharedInstance()?.changeUser("userId", sdkAuthSignature: "signature")
```
Ou, lorsque vous avez actualisé le jeton de l'utilisateur en milieu de session :

```swift
Appboy.sharedInstance()?.setSdkAuthenticationSignature("signature")
```
{% endtab %}
{% endtabs %}

### Enregistrer une fonction de rappel pour les jetons non valides {#sdk-callback}

Lorsque cette fonctionnalité est définie comme ["Requis"](#enforcement-options), les scénarios suivants provoqueront le rejet des requêtes SDK par Braze:
- JWT a expiré au moment de la réception par l'API Braze
- JWT est vide ou manquant
- JWT n'a pas réussi à vérifier les clés publiques que vous avez téléchargées sur le tableau de bord Braze

Lorsque les requêtes SDK échouent pour l'une de ces raisons, une fonction de rappel que vous fournissez sera appelée avec un [Code d'erreur][9] pertinent. Les demandes échouées seront périodiquement réessayées jusqu'à ce que votre application fournisse un nouveau JWT valide.

Ce rappel inclut l'ID de l'utilisateur pour lequel la requête a échoué, le [Code d'erreur][9]pertinent et la signature échouée. Si _cet utilisateur_ est toujours connecté, vous pouvez utiliser ce callback comme une opportunité de demander un nouveau JWT à votre serveur et fournir au SDK de Braze ce nouveau jeton valide.

{% alert tip %}
Ces méthodes de rappel sont un excellent endroit pour ajouter votre propre service de surveillance ou de journalisation des erreurs pour garder une trace de la fréquence de rejet de vos requêtes Braze.
{% endalert %}

{% tabs %}
{% tab Javascript %}
```javascript
importez le braze de "@braze/web-sdk";
braze. ubscribeToSdkAuthenticationFailures((authFailure) => {
  // TODO: optionally log to your error-reporting service
  // TODO: check if the errorEvent user matches the currently logged-in user
  const updated_jwt = wait getNewTokenSomehow(errorEvent);
  appboy. etSdkAuthenticationSignature (mise à jour);
});
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(ceci). ubscribeToSdkAuthenticationFailures(errorEvent -> {
    // TODO: optionally log to your error-reporting service
    // TODO: check if the errorEvent user matches the currently logged-in user
    String newToken = getNewTokenSomehow(errorEvent);
    Le Brésil. etInstance(getContext()).setSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
Braze.getInstance(ceci). ubscribeToSdkAuthenticationFailures({ errorEvent: BrazeSdkAuthenticationErrorEvent ->
    // TODO: optionally log to your error-reporting service
    // TODO: check if the errorEvent user matches the currently logged-in user
    val newToken: String = getNewTokenSomehow(errorEvent)
    Braze. etInstance(getContext()).setSdkAuthenticationSignature(newToken)
})
```
{% endtab %}
{% tab Objective-C %}
```objc
[[Appboy sharedInstance] setSdkAuthenticationDelegate:delegate];

// Méthode à implémenter en délégué
- (void)handleSdkAuthenticationError:(ABKSdkAuthenticationError *)errorEvent {
  // TODO: éventuellement log sur votre service de rapport d'erreurs
  // TODO: vérifier si l'utilisateur errorEvent correspond à l'utilisateur actuellement connecté
  NSLog(@"Signature d'authentification SDK invalide. );
  NSString *newSignature = getNewSignatureSomehow(errorEvent);
  [[Appboy sharedInstance] setSdkAuthenticationSignature:newSignature];
}
```
{% endtab %}
{% tab Swift %}
```swift
Appboy.sharedInstance()?.setSdkAuthenticationDelegate(delegate)

// Méthode pour implémenter en délégué
func handle(_ errorEvent: ABKSdkAuthenticationError?) {
        // TODO: optionnellement log to your error-reporting service
        // TODO: check if the errorEvent user matches the currently logged-in user
        print("Invalid SDK Authentication signature.")
        let newSignature = getNewSignatureSomehow(errorEvent)
        Appboy.sharedInstance()?.setSdkAuthenticationSignature(newSignature)
}
```
{% endtab %}
{% endtabs %}

L'argument `errorEvent` passé à ce callback contiendra les informations suivantes :

| Propriété             | Libellé                                                         |
| --------------------- | --------------------------------------------------------------- |
| `Raison`              | Une description de la raison pour laquelle la requête a échoué. |
| `erreur_code`         | Un code d'erreur interne utilisé par Braze.                     |
| `ID de l'utilisateur` | L'ID de l'utilisateur à partir duquel la requête a échoué.      |
| `signature`           | La JWT qui a échoué.                                            |
{: .reset-td-br-1 .reset-td-br-2}

## Ajout de clés publiques {#key-management}

Dans la page "Gérer les paramètres" du tableau de bord, ajoutez votre clé publique à une application spécifique dans le tableau de bord de Braze. Chaque application prend en charge jusqu'à 3 clés publiques. Notez que les mêmes clés publiques/privées peuvent être utilisées dans les applications.

Pour ajouter une clé publique :
1. Choisissez l'application dans le menu de gauche
2. Cliquez sur le bouton **Ajouter une clé publique** dans les paramètres d'authentification SDK
3. Coller dans la clé publique et ajouter une description facultative
4. Après avoir enregistré vos modifications, la clé apparaîtra dans la liste des clés publiques.

Pour supprimer une clé, ou pour promouvoir une clé à la touche principale, choisissez l'action correspondante dans le menu de débordement à côté de chaque touche.

## Activation dans le tableau de bord Braze {#braze-dashboard}

Une fois que votre [intégration côté serveur][1] et [intégration SDK][2] sont terminées, vous pouvez commencer à activer cette fonctionnalité pour ces applications spécifiques.

Gardez à l'esprit Les requêtes SDK continueront à couler comme d'habitude - sans authentification - _sauf si_ le paramètre d'authentification SDK de l'application est passé à **requis** dans le tableau de bord Braze.

Si quelque chose ne va pas avec votre intégration (i.e. votre application passe incorrectement des jetons vers le SDK, ou votre serveur génère des jetons invalides), simplement **désactiver** cette fonctionnalité dans le tableau de bord de Braze et les données reprendront comme d'habitude, sans vérification.

### Options de mise en application {#enforcement-options}

Dans la page `Paramètres` du tableau de bord, chaque application a trois états d'authentification SDK qui contrôlent la façon dont Braze vérifie les requêtes.

| Réglages      | Libellé                                                                                                       |
| ------------- | ------------------------------------------------------------------------------------------------------------- |
| **Désactivé** | Braze ne vérifiera pas le JWT fourni pour un utilisateur. (Paramètre par défaut)                              |
| **Optionnel** | Braze vérifiera les requêtes pour les utilisateurs connectés, mais ne rejettera pas les requêtes non valides. |
| **Requis**    | Braze vérifiera les requêtes pour les utilisateurs connectés et rejettera les JWT non valides.                |
{: .reset-td-br-1 .reset-td-br-2}

!\[Réglage du tableau de bord\]\[8\]

Le paramètre «**Optional**» est un moyen utile de surveiller l'impact potentiel de cette fonctionnalité sur le trafic SDK de votre application.

Les signatures JWT invalides seront signalées à la fois dans les états **Optionnel** et **Required** Cependant, seul l'état **Requis** rejettera les requêtes SDK provoquant une nouvelle tentative des applications et une nouvelle demande de signatures.

## Analyses {#analytics}

Chaque application affichera une ventilation des erreurs d'authentification SDK collectées alors que cette fonctionnalité est dans l'état **Optionnel** et **Requis**.

Les données sont disponibles en temps réel et vous pouvez survoler les points du tableau pour voir une ventilation des erreurs pour une date donnée.

!\[Erreurs d'authentification\]\[10\]

## Codes d'erreur {#error-codes}

| Code d'erreur | Raison de l'erreur                    | Libellé                                                                                                             |
| ------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| 10            | `Vous n'avez pas besoin d'EXPIRATION` | L'expiration est un champ requis pour l'utilisation de Braze.                                                       |
| 20            | `Erreur de décodage`                  | La clé publique ne correspond pas ou une erreur générale non prise.                                                 |
| 21            | `MISSION_MISES`                       | Les sujets attendus et réels ne sont pas les mêmes.                                                                 |
| 22            | `EXPIRÉ`                              | Le jeton fourni a expiré.                                                                                           |
| 23            | `INVALID_PAYLOAD`                     | Le bloc de jeton n'est pas valide.                                                                                  |
| 24            | `ALGORITEMENT_INCORRECT_TITLE`        | L'algorithme du jeton n'est pas pris en charge.                                                                     |
| 25            | `Impossible de publier la clé`        | La clé publique n'a pas pu être convertie dans le bon format.                                                       |
| 26            | `format@@0 MISSING_TOKEN`             | Aucun jeton n'a été fourni dans la requête.                                                                         |
| 27            | `NOT_MATCHING_POPUP_TITLE`            | Aucune clé publique ne correspond au jeton fourni.                                                                  |
| 28            | `MISMATCH_INSTALLATION`               | Tous les identifiants de l'utilisateur dans la charge utile de la requête ne correspondent pas à ce qui est requis. |
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3}

## Foire aux questions {#faq}

#### Puis-je utiliser cette fonctionnalité uniquement sur certaines de mes applications ? {#faq-app-by-app}

Oui, cette fonctionnalité peut être activée pour des applications spécifiques et n'a pas besoin d'être utilisée sur toutes vos applications.

#### Qu'advient-il des utilisateurs qui sont encore sur des versions plus anciennes de mon application ? {#faq-sdk-backward-compatibility}

Lorsque vous commencez à appliquer cette fonctionnalité, les requêtes faites par les anciennes versions de l'application seront rejetées par Braze et ré-essayées par les SDKs. Une fois que les utilisateurs auront mis à jour leur application vers une version prise en charge, ces requêtes seront à nouveau acceptées.

Si possible, vous devriez pousser les utilisateurs à mettre à jour comme vous le feriez pour toute autre mise à jour obligatoire. Alternativement, vous pouvez conserver la fonctionnalité ["optionnelle"][6] jusqu'à ce qu'un pourcentage acceptable d'utilisateurs aient été mis à niveau.

#### À quelle expiration devrais-je utiliser lors de la génération de jetons JWT ? {#faq-expiration}

Nous vous recommandons d'utiliser la valeur supérieure de : durée moyenne de la session, expiration des cookies/jetons de session, ou la fréquence à laquelle votre application actualiserait autrement le profil de l'utilisateur actuel.

#### Que se passe-t-il si une JWT expire au milieu de la session d'un utilisateur ? {#faq-jwt-expiration}

Si le jeton d'un utilisateur expire en milieu de session, le SDK a une [fonction de callback][7] qu'il invoquera pour informer votre application qu'un nouveau jeton JWT est nécessaire pour continuer à envoyer des données à Braze.

#### Que se passe-t-il si mon intégration côté serveur est interrompue et que je ne peux plus créer de JWT ? {#faq-server-downtime}

Si votre serveur n'est pas en mesure de fournir des jetons JWT ou si vous remarquez un problème d'intégration, vous pouvez toujours désactiver la fonctionnalité dans le tableau de bord Braze.

Une fois désactivée, toutes les requêtes SDK en attente échouées seront éventuellement ré-essayées par le SDK et acceptées par Braze.

#### Pourquoi cette fonctionnalité utilise-t-elle des clés publiques ou privées au lieu des secrets partagés ? {#faq-shared-secrets}

Lorsque vous utilisez les secrets partagés, toute personne ayant accès à ce secret partagé (i.e. la page du tableau de bord Braze) serait en mesure de générer des jetons et d'usurper l'identité de vos utilisateurs finaux.

Au lieu de cela, nous utilisons des clés publiques/privées pour que même les employés de Braze (encore moins vos utilisateurs du tableau de bord) n'aient pas accès à vos clés privées.

#### Comment les demandes rejetées seront-elles tentées? {#faq-retry-logic}

Lorsqu'une requête est rejetée à cause d'une erreur d'authentification, les SDK invoqueront votre callback utilisé pour actualiser la signature JWT de l'utilisateur.

Les demandes réessaieront périodiquement en utilisant une approche exponentielle de rétrograde. Après 50 tentatives échouées consécutives, les tentatives seront suspendues jusqu'à la prochaine session. Chaque SDK a également une méthode pour demander manuellement une purge de données.
[8]: {% image_buster /assets/img/sdk-auth-settings.png %} [10]: {% image_buster /assets/img/sdk-auth-analytics.png %}

[1]: #server-side-integration

[1]: #server-side-integration
[2]: #sdk-integration
[2]: #sdk-integration
[3]: #key-management
[4]: #braze-dashboard
[4]: #braze-dashboard
[6]: #enforcement-options
[7]: #sdk-callback
[9]: #error-codes
