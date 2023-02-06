---
nav_title: Authentification SDK
article_title: Authentification SDK
page_order: 5
description: "Cet article de référence couvre l’authentification SDK et la manière d’activer cette fonctionnalité dans le SDK Braze."
platform:
  - iOS
  - Android
  - Web
  
---

# Authentification SDK

L’authentification SDK vous permet de fournir des preuves cryptographiques (côté serveur généré) aux requêtes SDK effectuées pour au nom des utilisateurs connectés. Lorsque cette fonctionnalité est activée dans votre application, le tableau de bord de Braze peut être configuré pour rejeter les demandes avec une signature JWT manquante ou non valide.

Lorsqu’elle est activée, cette fonctionnalité empêchera les requêtes non autorisées qui utilisent la clé API SDK de votre application pour les utilisateurs connectés, notamment :
- Envoi d’événements personnalisés, d’attributs, d’achats et de données de session
- Création de nouveaux utilisateurs dans votre groupe d’applications Braze
- Mise à jour des attributs de profil utilisateur standard
- Réception ou déclenchement de messages

## Démarrage

Il existe quatre étapes de haut niveau pour commencer :

1. [Intégration côté serveur][1] - Générez une paire de clés publique et privée et utilisez votre clé privée pour créer un JWT (_Jeton Web JSON_) pour l’utilisateur connecté actuel.<br><br>
2. [Intégration SDK ][2]- Activez cette fonctionnalité dans le SDK Braze et demandez le jeton JWT généré à partir de votre serveur.<br><br>
3. [Ajout de clé publique ][3] - Ajoutez votre  _clé publique_  au tableau de bord de Braze dans la page **Gérer les paramètres**.<br><br>
4. [Basculer l’application dans le tableau de bord de Braze ][4]- Basculez l’application de cette fonctionnalité dans le tableau de bord de Braze, application par application.

## Intégration côté serveur {#server-side-integration}

### Générer une paire de clés publique/privée {#generate-keys}

Générer une paire de clés publiques/privées RSA. La clé publique sera ajoutée au tableau de bord de Braze, tandis que la clé privée devra être stockée en toute sécurité sur votre serveur.

Nous recommandons une clé RSA avec 2 048 bits pour une utilisation avec l’algorithme RS256 JWT.

{% alert warning %}
N’oubliez pas de conserver vos clés privées _privé_. N’exposez jamais ou ne saisissez jamais votre clé privée dans votre application ou site Internet. Toute personne qui connaît votre clé privée peut se faire passer pour un autre utilisateur ou créer des utilisateurs au nom de votre application.
{% endalert %}

### Créer un jeton Web JSON pour l’utilisateur actuel {#create-jwt}

Une fois que vous avez votre clé privée, votre application côté serveur doit l’utiliser pour renvoyer un JWT à votre application ou site Internet pour l’utilisateur actuellement connecté.

En général, cette logique peut aller partout où votre application demande normalement le profil de l’utilisateur actuel, comme un endpoint de connexion ou partout où votre application a rafraîchi le profil de l’utilisateur actuel.

Lors de la génération du JWT, les champs suivants sont attendus :

**En-tête JWT**

| Champ | Requis | Description                         |
| ----- | -------- | ----------------------------------- |
| `alg` | **Oui**  | L’algorithme pris en charge est `RS256`. |
| `typ` | **Oui**  | Le type doit être égal à `JWT`.        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

**Charge utile JWT**

| Champ | Requis | Description                                                                            |
| ----- | -------- | -------------------------------------------------------------------------------------- |
| `sub` | **Oui**  | Le « sujet » doit être égal à l’ID utilisateur que vous fournissez à Braze SDK lorsque vous appelez `changeUser` |
| `exp` | **Oui**  | L’« expiration » ou le moment où vous souhaitez que ce jeton expire.                                |
| `aud` | Non       | La demande d’« audience » est facultative, et si elle est effectuée, elle doit être égale à `braze`                      |
| `iss` | Non       | La demande « émetteur » est facultative, et si elle est effectuée, elle doit être égale à votre clé API SDK.              |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### Bibliothèques JWT

Pour en savoir plus sur les jetons Web JSON ou pour parcourir les [nombreuses bibliothèques open source](https://jwt.io/#libraries-io) qui simplifient ce processus de signature, consultez [https ://jwt.io](https://jwt.io).

## Intégration SDK {#sdk-integration}

Cette fonctionnalité est disponible à partir des [versions SDK]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions) suivantes :

{% sdk_min_versions web:3.3.0 ios:4.3.0 android:14.0.0 %}

### Activez cette fonction dans le SDK Braze.

Lorsque cette fonctionnalité est activée, le SDK Braze ajoutera le dernier JWT connu de l’utilisateur actuel aux demandes réseau effectuées sur les serveurs Braze.

{% alert note %}
Ne vous inquiétez pas, l’initialisation avec cette option seule n’aura aucune incidence sur la collecte de données jusqu’à ce que vous commenciez à [forcer l’authentification](#braze-dashboard) dans le tableau de bord de Braze.
{% endalert %}

{% tabs %}
{% tab Javascript %}
Lorsque vous appelez `initialize`, définissez la propriété `enableSdkAuthentication` facultative à `true`.
```javascript
import* as braze from"@braze/web-sdk";
braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
  enableSdkAuthentication: true,
});
```
{% endtab %}
{% tab Java %}
Lors de la configuration de l’instance Appboy, appelez le `setIsSdkAuthenticationEnabled` vers `true`.
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```

Vous pouvez également ajouter `<bool name="com_braze_sdk_authentication_enabled">true</bool>` à votre braze.xml.
{% endtab %}
{% tab KOTLIN %}
Lors de la configuration de l’instance Appboy, appelez le `setIsSdkAuthenticationEnabled` vers `true`.
```kotlin
BrazeConfig.Builder brazeConfigBuilder = BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```

Vous pouvez également ajouter `<bool name="com_braze_sdk_authentication_enabled">true</bool>` à votre braze.xml.
{% endtab %}
{% tab Objective-C %}
Pour activer l’authentification SDK, ajoutez la clé `EnableSDKAuthentication` au dictionnaire `Braze` dans votre fichier `.plist` et attribuez-lui la valeur « vrai ».

Vous pouvez également activer l’authentification SDK lors de l’initialisation du SDK :

```objc
[Appboy startWithApiKey:@"YOUR-API-KEY"
            inApplication:application
        withLaunchOptions:launchOptions
        withAppboyOptions:@{ABKEnableSDKAuthenticationKey : @YES}];
```
{% endtab %}
{% tab Swift %}
Pour activer l’authentification SDK, ajoutez la clé `EnableSDKAuthentication` au dictionnaire `Braze` dans votre fichier `.plist` et attribuez-lui la valeur « vrai ».

Vous pouvez également activer l’authentification SDK lors de l’initialisation du SDK :

```swift
Appboy.start(withApiKey: "YOUR-API-KEY",
                 dans l’application,
                 withLaunchOptions:launchOptions,
                 withAppboyOptions:[ ABKEnableSDKAuthenticationKey : true ])
```
{% endtab %}
{% tab Dart %}
Actuellement, l’authentification SDK doit être activée dans le cadre de l’initialisation du SDK dans le code iOS et Android natif. Pour activer l’authentification SDK dans le SDK Flutter, suivez les intégrations pour iOS et Android depuis les autres onglets. Une fois que l’authentification SDK est activée, le reste de la fonctionnalité peut être intégré à Dart.
{% endtab %}
{% endtabs %}

### Définir le jeton JWT de l’utilisateur actuel

Lorsque votre application appelle la méthode `changeUser` Braze, fournissez également le jeton JWT qui a été [généré côté serveur][4].

Vous pouvez également mettre à jour le jeton pour actualiser la session de jeton pour l’utilisateur actuel.

{% alert note %}
Gardez à l’esprit que `changeUser` ne doit être appelée que lorsque l’ID utilisateur a _réellement été modifié_. Vous ne devez pas utiliser cette méthode pour mettre à jour la signature si l’ID utilisateur n’a pas changé.
{% endalert %}

{% tabs %}
{% tab Javascript %}
Fournissez le jeton JWT lorsque vous lancez `changeUser` :

```javascript
import* as braze from"@braze/web-sdk";
braze.changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER");
```

Ou, lorsque vous avez actualisé la mi-session jeton de l’utilisateur :

```javascript
import* as braze from"@braze/web-sdk";
braze.setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER");
```
{% endtab %}
{% tab Java %}

Fournissez le jeton JWT lorsque vous lancez `appboy.changeUser` :

```java
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER");
```

Ou, lorsque vous avez actualisé la mi-session jeton de l’utilisateur :

```java
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER");
```
{% endtab %}
{% tab KOTLIN %}

Fournissez le jeton JWT lorsque vous lancez `appboy.changeUser` :

```kotlin
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-TOKEN-FROM-SERVER")
```

Ou, lorsque vous avez actualisé la mi-session jeton de l’utilisateur :

```kotlin
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-TOKEN-FROM-SERVER")
```
{% endtab %}
{% tab Objective-C %}

Fournissez le jeton JWT lorsque vous lancez `changeUser` :

```objc
[[Appboy sharedInstance] changeUser:@"userId" sdkAuthSignature:@"signature"];
```

Ou, lorsque vous avez actualisé la mi-session jeton de l’utilisateur :

```objc
[[Appboy sharedInstance] setSdkAuthenticationSignature:@"signature"];
```
{% endtab %}
{% tab Swift %}

Fournissez le jeton JWT lorsque vous lancez `changeUser` :

```swift
Appboy.sharedInstance()?.changeUser("userId", sdkAuthSignature: "signature")
```
Ou, lorsque vous avez actualisé la mi-session jeton de l’utilisateur :

```swift
Appboy.sharedInstance()?.setSdkAuthenticationSignature("signature")
```
{% endtab %}
{% tab Dart %}

Fournissez le jeton JWT lorsque vous lancez `changeUser` :

```dart
braze.changeUser("userId", sdkAuthSignature: "signature")
```
Ou, lorsque vous avez actualisé la mi-session jeton de l’utilisateur :

```dart
braze.setSdkAuthenticationSignature("signature")
```

{% endtab %}
{% endtabs %}

### Enregistrer une fonction de rappel pour les jetons invalides {#sdk-callback}

Lorsque cette fonction est définie comme [« Obligatoire »](#enforcement-options), les scénarios suivants entraîneront le rejet des demandes SDK par Braze :
- Le JWT a expiré au moment où l’API Braze a été reçue
- JWT était vide ou manquant
- JWT n’a pas vérifié les clés publiques que vous avez téléchargées sur le tableau de bord de Braze

Lorsque les demandes SDK échouent pour l’une de ces raisons, une fonction de rappel que vous avez fournie sera appelée avec un [code d’erreur ][9] correspondant. Les demandes échouées seront périodiquement récupérées jusqu’à ce que votre application fournisse un nouveau JWT valide.

Cette fonction de rappel inclut l’ID utilisateur pour lequel la demande a échoué, le [code d’erreur][9] et la signature de l’échec. Si _cet utilisateur_ est toujours connecté, vous pouvez utiliser cette fonction de rappel comme une opportunité de demander un nouveau JWT depuis votre serveur et de fournir le SDK de Braze avec ce nouveau jeton valide.

{% alert tip %}
Ces méthodes de fonction de rappel sont un excellent endroit pour ajouter votre propre service de surveillance ou d’erreur afin de suivre la fréquence à laquelle vos demandes de Braze sont rejetées.
{% endalert %}

{% tabs %}
{% tab Javascript %}
```javascript
import* as braze from"@braze/web-sdk";
braze.subscribeToSdkAuthenticationFailures((authFailure) => {
  // TODO: Vous pouvez, à titre facultatif, vous connecter à votre service error-reporting (signalement des erreurs)
  // TODO: Vérifiez si utilisateur de l’errorEvent correspond à l’utilisateur actuellement connecté
  const updated_jwt = await getNewTokenSomehow(errorEvent);
  appboy.setSdkAuthenticationSignature(updated_jwt);
});
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(this).subscribeToSdkAuthenticationFailures(errorEvent -> {
    // TODO: Vous pouvez, à titre facultatif, vous connecter à votre service error-reporting (signalement des erreurs)
    // TODO: Vérifiez si utilisateur de l’errorEvent correspond à l’utilisateur actuellement connecté
    String newToken = getNewTokenSomehow(errorEvent);
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
Braze.getInstance(this).subscribeToSdkAuthenticationFailures({ errorEvent: BrazeSdkAuthenticationErrorEvent ->
    // TODO: Vous pouvez, à titre facultatif, vous connecter à votre service error-reporting (signalement des erreurs)
    // TODO: Vérifiez si utilisateur de l’errorEvent correspond à l’utilisateur actuellement connecté
    val newToken: String = getNewTokenSomehow(errorEvent)
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken)
})
```
{% endtab %}
{% tab Objective-C %}
```objc
[[Appboy sharedInstance] setSdkAuthenticationDelegate:delegate];

// Méthodes d’implémentation dans la délégation
- (void)handleSdkAuthenticationError:(ABKSdkAuthenticationError *)errorEvent {
  // TODO: Vous pouvez, à titre facultatif, vous connecter à votre service error-reporting (signalement des erreurs)
  // TODO: Vérifiez si utilisateur de l’errorEvent correspond à l’utilisateur actuellement connecté
  NSLog(@"Invalid SDK Authentication signature.");
  NSString *newSignature = getNewSignatureSomehow(errorEvent);
  [[Appboy sharedInstance] setSdkAuthenticationSignature:newSignature];
}
```
{% endtab %}
{% tab Swift %}
```swift
Appboy.sharedInstance()?.setSdkAuthenticationDelegate(delegate)

// Méthodes d’implémentation dans la délégation
func handle(_ errorEvent: ABKSdkAuthenticationError?) {
  // TODO: Vous pouvez, à titre facultatif, vous connecter à votre service error-reporting (signalement des erreurs)
  // TODO: Vérifiez si utilisateur de l’errorEvent correspond à l’utilisateur actuellement connecté
  print("Invalid SDK Authentication signature.")
  let newSignature = getNewSignatureSomehow(errorEvent)
  Appboy.sharedInstance()?.setSdkAuthenticationSignature(newSignature)
}
```
{% endtab %}
{% tab Dart %}
```dart
braze.setBrazeSdkAuthenticationErrorCallback((BrazeSdkAuthenticationError error) async {
  // TODO: Vous pouvez, à titre facultatif, vous connecter à votre service error-reporting (signalement des erreurs)
  // TODO: Vérifiez si utilisateur de l’errorEvent correspond à l’utilisateur actuellement connecté
  print("Invalid SDK Authentication signature.")
  let newSignature = getNewSignatureSomehow(errorEvent)
  braze.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% endtabs %}

L’argument `errorEvent` transmis à cette fonction de rappel contiendra les informations suivantes :

| Propriété | Description |
| -------- | ----------- |
| `reason` | Une description de la raison pour laquelle la demande a échoué. |
| `error_code` | Un code d’erreur interne utilisé par Braze. |
| `user_id` | L’ID utilisateur à partir duquel la demande a échoué. |
| `signature` | Le JWT qui a échoué.|
{: .reset-td-br-1 .reset-td-br-2}

## Ajout de clés publiques {#key-management}

Dans la page **Gérer les paramètres** du tableau de bord, ajoutez votre clé publique à une application spécifique du tableau de bord de Braze. Chaque application prend en charge jusqu’à 3 clés publiques. Notez que les mêmes clés publiques/privées peuvent être utilisées sur les applications.

Pour ajouter une clé publique :

1. Choisissez l’application dans la liste des applications disponibles.
2. Sous **Authentification SDK**, cliquez sur **Ajouter une clé publique**.
3. Coller dans la clé publique et ajouter une description facultative.
4. Après avoir enregistré vos modifications, la clé apparaîtra dans la liste des clés publiques.

Pour supprimer une clé ou pour définir une clé dans la clé principale, choisissez l’action correspondante dans le menu de débordement à côté de chaque clé.

## Activation du tableau de bord de Braze {#braze-dashboard}

Une fois votre [Intégration côté serveur][1]  et [Intégration SDK][2] terminées, vous pouvez commencer à activer cette fonction pour ces applications spécifiques.

N’oubliez pas que les demandes SDK continueront à circuler comme d’habitude - sans authentification - _sauf_ si le paramètre d’authentification SDK de l’application est passé à **requis** dans le tableau de bord de Braze.

Si quelque chose ne va pas dans votre intégration (c.-à-d. votre application ne transmet pas correctement les jetons au SDK ou votre serveur génère des jetons invalides), il suffit de **désactiver** cette fonctionnalité dans le tableau de bord de Braze et les données recommenceront à circuler comme d’habitude, sans vérification.

### Options d’application {#enforcement-options}

Dans la page du tableau de bord `Settings`, chaque application dispose de trois états d’authentification SDK qui contrôlent la manière dont Braze vérifie les requêtes.

| Réglage| Description|
| ------ | ---------- |
| **Désactivé** | Braze ne vérifiera pas le JWT fourni à un utilisateur. (Paramètre par défaut)|
| **Facultatif** | Braze vérifiera les demandes pour les utilisateurs connectés, mais ne rejettera pas les demandes non valides. |
| **Requis** | Braze vérifiera les demandes pour les utilisateurs connectés, et rejettera les JWT non valides.|
{: .reset-td-br-1 .reset-td-br-2}

![][8]

Le paramètre « **Facultatif** » est un moyen utile de surveiller l’impact potentiel que cette fonction aura sur le trafic SDK de votre application.

Les signatures JWT non valides seront signalées dans les modes **Facultatif** et **Requis** mais seulement le mode **Requis** rejettera les demandes de SDK obligeant les applications à réessayer et à demander de nouvelles signatures.

## Analyse {#analytics}

Chaque application présente une ventilation des erreurs d’authentification SDK relevées lorsque cette fonction est en mode **Facultatif** et **Requis**.

Les données sont disponibles en temps réel, et vous pouvez déplacer le curseur sur les points du graphique pour voir la répartition des erreurs pour une date donnée.

![Graphique montrant le nombre d’erreurs d’authentification. Le nombre total d’erreurs, le type d’erreur et la plage de dates réglables sont également affichés.][10]{: style="max-width:80%"}

## Codes d’erreur {#error-codes}

| Code d’erreur| Cause de l’erreur | Description |
| --------  | ------------ | ---------  |
| 10 | `EXPIRATION_REQUIRED` | L’expiration est un champ obligatoire pour l’utilisation de Braze.|
| 20 | `DECODING_ERROR` | Clé publique non conforme ou erreur générale non détectée.|
| 21 | `SUBJECT_MISMATCH` | Les sujets attendus et réels ne sont pas les mêmes.|
| 22 | `EXPIRED` | Le jeton fourni a expiré.|
| 23 | `INVALID_PAYLOAD` | La charge utile jeton n’est pas valide.|
| 24 | `INCORRECT_ALGORITHM` | L’algorithme du jeton n’est pas pris en charge.|
| 25 | `PUBLIC_KEY_ERROR` | La clé publique n’a pas pu être convertie au format approprié.|
| 26 | `MISSING_TOKEN` | Aucun jeton n’a été fourni dans la demande.|
| 27 | `NO_MATCHING_PUBLIC_KEYS` | Aucune clé publique ne correspond au jeton fourni.|
| 28 | `PAYLOAD_USER_ID_MISMATCH` | Tous les identifiants d’utilisateur de la demande de charge utile ne sont pas requis.|
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3}

## Foire aux Questions {#faq}

#### Cette fonction doit-elle être activée sur toutes mes applications en même temps ? {#faq-app-by-app}

Non, cette fonctionnalité peut être activée pour des applications spécifiques et n’a pas besoin d’être utilisée sur toutes vos applications, en même temps.

#### Que se passe-t-il pour les utilisateurs qui sont toujours sur les versions antérieures de mon application ? {#faq-sdk-backcompatibility}

Lorsque vous commencez à faire appliquer cette fonctionnalité, les demandes effectuées par les versions anciennes d’applications seront rejetées par Braze et récupérées par les SDK. Une fois que les utilisateurs ont mis à niveau leur application vers une version prise en charge, les demandes mises en file d’attente seront à nouveau acceptées.

Dans la mesure du possible, il convient de faire en sorte que les utilisateurs effectuent la mise à niveau comme pour toute autre mise à niveau obligatoire. Vous pouvez également conserver la fonction ["facultatif"][6] jusqu’à ce que vous voyiez qu’un pourcentage acceptable d’utilisateurs a été mis à niveau.

#### Quelle expiration dois-je utiliser lors de la génération de jetons JWT ? {#faq-expiration}

Nous vous recommandons d’utiliser la valeur la plus élevée parmi : la durée moyenne de la session, l’expiration du cookie/jeton de la session, ou la fréquence à laquelle votre application rafraîchirait autrement le profil utilisateur actuel.

#### Que se passe-t-il si un JWT expire au milieu de la session d’un utilisateur ? {#faq-jwt-expiration}

Si le jeton d’un utilisateur expire à mi-session, le SDK a une [fonction de rappel][7]. Il sera appelé à laisser votre application savoir qu’un nouveau jeton JWT est nécessaire pour continuer à envoyer des données à Braze.

#### Que se passe-t-il si mon intégration côté serveur est interrompue et que je ne peux plus créer JWT ? {#faq-server-temps d’arrêt}

Si votre serveur n’est pas en mesure de fournir des jetons JWT ou si vous remarquez un problème d’intégration, vous pouvez toujours désactiver la fonction dans le tableau de bord de Braze.

Une fois désactivée, toutes les demandes de SDK échouées en attente seront finalement récupérées par le SDK et acceptées par Braze.

#### Pourquoi cette fonction utilise-t-elle des clés publiques/privées plutôt que des secrets partagés ? {#faq-shared-secrets}

Lorsque vous utilisez des secrets partagés, toute personne ayant accès à ce secret partagé (c.-à-d. la page du tableau de bord de Braze) serait en mesure de générer des jetons et de se faire passer pour vos utilisateurs finaux.

Nous utilisons plutôt des clés publiques/privées pour que ni même les employés de Braze (seuls les utilisateurs de votre tableau de bord) aient accès à vos clés privées.

#### Comment les demandes rejetées seront-elles récupérées ? {#faq-retry-logic}

Lorsqu’une demande est rejetée en raison d’une erreur d’authentification, les SDK invoqueront votre fonction de rappel utilisé pour actualiser la signature JWT de l’utilisateur. 

Les demandes réessaieront périodiquement en utilisant une approche de délais exponentielle. Après 50 tentatives consécutives échouées, les nouvelles tentatives seront interrompues jusqu’à la prochaine session. Chaque SDK dispose également d’une méthode qui permet de demander manuellement un rafraîchissement des données.

[1]: #server-side-integration
[2]: #sdk-integration
[3]: #key-management
[4]: #braze-dashboard
[5]: #create-jwt
[6]: #enforcement-options
[7]: #sdk-callback
[8]: {% image_buster /assets/img/sdk-auth-settings.png %}
[9]: #error-codes
[10]: {% image_buster /assets/img/sdk-auth-analytics.png %}
