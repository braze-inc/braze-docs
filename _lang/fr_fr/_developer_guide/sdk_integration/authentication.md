---
page_order: 1.2
nav_title: Authentification
article_title: "Configurer l'authentification pour le SDK de Braze"
description: "Cet article de référence couvre l’authentification SDK et la manière d’activer cette fonctionnalité dans le SDK Braze."
platform:
  - iOS
  - Android
  - Web
  
---

# Mise en place de l'authentification SDK

> L’authentification SDK vous permet de fournir des preuves cryptographiques (côté serveur généré) aux requêtes SDK effectuées pour au nom des utilisateurs connectés.

## Fonctionnement

Après avoir activé cette fonctionnalité dans votre app, vous pouvez configurer le tableau de bord de Braze pour qu'il rejette toute demande avec un jeton Web JSON (JWT) invalide ou manquant, ce qui inclut :

- Envoi d’événements personnalisés, d’attributs, d’achats et de données de session
- Créer de nouveaux utilisateurs dans votre espace de travail Braze
- Mise à jour des attributs de profil utilisateur standard
- Réception ou déclenchement de messages

Vous pouvez désormais empêcher les utilisateurs connectés non authentifiés d'utiliser la clé API SDK de votre application pour effectuer des actions malveillantes, telles que l'usurpation d'identité de vos autres utilisateurs.

## Mise en place de l'authentification

### Étape 1 : Configurez votre serveur {#server-side-integration}

#### Étape 1.1 : Générer une paire de clés publiques/privées {#generate-keys}

Générez une paire de clés publiques/privées RSA256. La clé publique sera ajoutée au tableau de bord de Braze, tandis que la clé privée devra être stockée en toute sécurité sur votre serveur.

Nous recommandons une clé RSA 2048 bits pour une utilisation avec l’algorithme JWT RS256.

{% alert warning %}
N'oubliez pas de conserver vos clés privées _privées_. N’exposez jamais ou ne saisissez jamais votre clé privée dans votre application ou site Internet. Toute personne qui connaît votre clé privée peut se faire passer pour un autre utilisateur ou créer des utilisateurs au nom de votre application.
{% endalert %}

#### Étape 1.2 : Créer un jeton Web JSON pour l’utilisateur actuel {#create-jwt}

Une fois que vous avez votre clé privée, votre application côté serveur doit l’utiliser pour renvoyer un JWT à votre application ou site Internet pour l’utilisateur actuellement connecté.

En général, cette logique peut aller partout où votre application demande normalement le profil de l’utilisateur actuel, comme un endpoint de connexion ou partout où votre application a rafraîchi le profil de l’utilisateur actuel.

Lors de la génération du JWT, les champs suivants sont attendus :

**En-tête JWT**

| Champ | Requis | Description                         |
| ----- | -------- | ----------------------------------- |
| `alg` | Oui  | L’algorithme pris en charge est `RS256`. |
| `typ` | Oui  | Le type doit être égal à `JWT`.        |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

**Charge utile JWT**

| Champ | Requis | Description                                                                            |
| ----- | -------- | -------------------------------------------------------------------------------------- |
| `sub` | Oui  | Le « sujet » doit être égal à l’ID utilisateur que vous fournissez à Braze SDK lorsque vous appelez `changeUser`  |
| `exp` | Oui | L’« expiration » ou le moment où vous souhaitez que ce jeton expire.                                |

{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert tip %}
Pour en savoir plus sur les jetons Web JSON ou pour parcourir les nombreuses bibliothèques open source qui simplifient ce processus de signature, consultez [https://jwt.io](https://jwt.io).
{% endalert %}

### Étape 2 : Configurer le SDK Braze {#sdk-integration}

Cette fonctionnalité est disponible à partir des [versions du SDK]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions):

{% sdk_min_versions swift:5.0.0 android:14.0.0 web:3.3.0 %}

{% alert note %}
Pour les intégrations iOS, cette page détaille les étapes à suivre pour le SDK Swift de Braze. Pour un exemple d'utilisation dans l'ancien SDK iOS d'AppboyKit, référez-vous à [ce fichier](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/AppDelegate.m) et à [ce fichier.](https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/Stopwatch/Sources/Utils/SdkAuthDelegate.m)
{% endalert %}

#### Étape 2.1 : Activez l'authentification dans le SDK de Braze.

Lorsque cette fonctionnalité est activée, le SDK Braze ajoutera le dernier JWT connu de l’utilisateur actuel aux demandes réseau effectuées sur les serveurs Braze.

{% alert note %}
Ne vous inquiétez pas, l'initialisation avec cette seule option n'aura aucun impact sur la collecte des données, jusqu'à ce que vous [appliquiez l'authentification](#braze-dashboard) dans le tableau de bord de Braze.
{% endalert %}

{% tabs %}
{% tab Web %}
Lorsque vous appelez `initialize`, définissez la propriété `enableSdkAuthentication` facultative à `true`.
```javascript
import * as braze from "@braze/web-sdk";
braze.initialize("YOUR-API-KEY-HERE", {
  baseUrl: "YOUR-SDK-ENDPOINT-HERE",
  enableSdkAuthentication: true,
});
```
{% endtab %}
{% tab React Native %}
L'authentification SDK doit être activée lors de l'initialisation native du SDK. Ajoutez la configuration suivante à votre code natif iOS et Android :

**iOS (AppDelegate.swift)**

```swift
import BrazeKit
import braze_react_native_sdk

let configuration = Braze.Configuration(
  apiKey: "{YOUR-BRAZE-API-KEY}",
  endpoint: "{YOUR-BRAZE-ENDPOINT}"
)
configuration.api.sdkAuthentication = true
let braze = BrazeReactBridge.perform(
  #selector(BrazeReactBridge.initBraze(_:)),
  with: configuration
).takeUnretainedValue() as! Braze
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

Après avoir activé l'authentification SDK dans la couche native, vous pouvez utiliser les méthodes JavaScript React Native présentées dans les étapes suivantes.
{% endtab %}
{% tab Java %}
Lors de la configuration de l'instance Braze, appelez `setIsSdkAuthenticationEnabled` à `true`.
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```

Vous pouvez également ajouter `<bool name="com_braze_sdk_authentication_enabled">true</bool>` à votre braze.xml.
{% endtab %}
{% tab KOTLIN %}
Lors de la configuration de l'instance Braze, appelez `setIsSdkAuthenticationEnabled` à `true`.
```kotlin
BrazeConfig.Builder brazeConfigBuilder = BrazeConfig.Builder()
    .setIsSdkAuthenticationEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```

Vous pouvez également ajouter `<bool name="com_braze_sdk_authentication_enabled">true</bool>` à votre braze.xml.
{% endtab %}
{% tab Objective-C %}
Pour activer l'authentification SDK, définissez la propriété `configuration.api.sdkAuthentication` de votre objet `BRZConfiguration` sur `YES` avant d'initialiser l'instance de Braze :

```objc
BRZConfiguration *configuration =
    [[BRZConfiguration alloc] initWithApiKey:@"{BRAZE_API_KEY}"
                                    endpoint:@"{BRAZE_ENDPOINT}"];
configuration.api.sdkAuthentication = YES;
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
AppDelegate.braze = braze;
```
{% endtab %}
{% tab Swift %}
Pour activer l'authentification SDK, définissez la propriété `configuration.api.sdkAuthentication` de votre objet `Braze.Configuration` sur `true` lors de l'initialisation du SDK :

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}",
                                        endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
```
{% endtab %}
{% tab Dart %}
Actuellement, l’authentification SDK doit être activée dans le cadre de l’initialisation du SDK dans le code iOS et Android natif. Pour activer l’authentification SDK dans le SDK Flutter, suivez les intégrations pour iOS et Android depuis les autres onglets. Une fois l'authentification SDK activée, le reste de la fonctionnalité peut être intégré dans Dart.
{% endtab %}
{% tab Flutter %}
L'authentification du SDK doit être activée dans le cadre de l'initialisation du SDK dans le code natif d'iOS et d'Android. Lorsqu'elle est activée dans la couche native, vous pouvez utiliser les méthodes du SDK Flutter pour transmettre la signature JWT.

**iOS**

Pour activer l'authentification SDK, définissez la propriété `configuration.api.sdkAuthentication` sur `true` dans votre code natif iOS :

```swift
let configuration = Braze.Configuration(apiKey: "{YOUR-BRAZE-API-KEY}", endpoint: "{YOUR-BRAZE-ENDPOINT}")
configuration.api.sdkAuthentication = true
let braze = Braze(configuration: configuration)
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

Après avoir activé l'authentification SDK dans la couche native, vous pouvez utiliser les méthodes du SDK Flutter présentées dans les étapes suivantes.
{% endtab %}
{% tab Unity %}
L'authentification SDK doit être activée lors de l'initialisation native du SDK. Ajoutez la configuration suivante à votre code natif iOS et Android :

**iOS**

Définissez la propriété `SDKAuthenticationEnabled` à `true` dans votre fichier de configuration :

```xml
<key>SDKAuthenticationEnabled</key>
<true/>
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

Après avoir activé l'authentification SDK dans la couche native, vous pouvez utiliser les méthodes C# d'Unity présentées dans les étapes suivantes.
{% endtab %}
{% tab Cordova %}
L'authentification SDK doit être activée lors de l'initialisation native du SDK. Ajoutez la configuration suivante à votre code natif iOS et Android :

**iOS**

Pour activer l'authentification SDK, définissez la propriété `enableSDKAuthentication` sur `true` dans votre `config.xml`:

```xml
<preference name="com.braze.ios_enable_sdk_authentication" value="true" />
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

Après avoir activé l'authentification SDK dans la couche native, vous pouvez utiliser les méthodes JavaScript de Cordova présentées dans les étapes suivantes.
{% endtab %}
{% tab .NET MAUI (Xamarin) %}
L'authentification SDK doit être activée lors de l'initialisation native du SDK. Configurez l'authentification SDK séparément pour iOS et Android :

**iOS**

Pour activer l'authentification du SDK, définissez la propriété `configuration.Api.SdkAuthentication` sur `true` lors de l'initialisation du SDK :

```csharp
var configuration = new BRZConfiguration("YOUR-API-KEY", "YOUR-ENDPOINT");
configuration.Api.SdkAuthentication = true;
var braze = new Braze(configuration);
```

**Android (braze.xml)**

```xml
<bool name="com_braze_sdk_authentication_enabled">true</bool>
```

Après avoir activé l'authentification SDK, vous pouvez utiliser les méthodes MAUI .NET présentées dans les étapes suivantes.
{% endtab %}
{% tab Expo %}
Lorsque vous utilisez le plugin Braze Expo, définissez la propriété `enableSdkAuthentication` sur `true` dans la configuration de votre application. Cela permet de configurer automatiquement l'authentification SDK dans les couches natives d'iOS et d'Android sans nécessiter de modifications manuelles du code natif.

**app.json ou app.config.js**

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          "enableSdkAuthentication": true
        }
      ]
    ]
  }
}
```

Après avoir activé l'authentification SDK dans la configuration de votre app, vous pouvez utiliser les méthodes JavaScript React Native présentées dans l'onglet React Native pour les étapes suivantes.

{% alert note %}
Pour un exemple de mise en œuvre complet, consultez l'[application d'exemple du plugin Braze Expo](https://github.com/braze-inc/braze-expo-plugin/blob/main/example/components/Braze.tsx) sur GitHub.
{% endalert %}
{% endtab %}
{% endtabs %}

#### Étape 2.2 : Définir le JWT de l'utilisateur actuel

Lorsque votre application appelle la méthode Braze `changeUser`, fournissez également le JWT qui a été [généré côté serveur.](#braze-dashboard)

Vous pouvez également configurer le jeton pour actualiser la mi-session pour l’utilisateur actuel.

{% alert note %}
Gardez à l’esprit que `changeUser` ne doit être appelée que lorsque l’ID utilisateur a _réellement été modifié_. Vous ne devez pas utiliser cette méthode pour mettre à jour le jeton d'authentification (JWT) si l'ID de l'utilisateur n'a pas changé.
{% endalert %}

{% tabs %}
{% tab Web %}
Fournissez le JWT lors de l'appel [`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser):

```javascript
import * as braze from "@braze/web-sdk";
braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Ou, lorsque vous avez actualisé la mi-session jeton de l’utilisateur :

```javascript
import * as braze from "@braze/web-sdk";
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab React Native %}

Fournissez le JWT lors de l'appel [`changeUser`](https://braze-inc.github.io/braze-react-native-sdk/classes/Braze.Braze-1.html#changeUser):

```typescript
import Braze from '@braze/react-native-sdk';

Braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Ou, lorsque vous avez actualisé la mi-session jeton de l’utilisateur :

```typescript
import Braze from '@braze/react-native-sdk';

Braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Java %}

Fournissez le JWT lors de l'appel [`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html):

```java
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Ou, lorsque vous avez actualisé la mi-session jeton de l’utilisateur :

```java
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab KOTLIN %}

Fournissez le JWT lors de l'appel [`changeUser`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html):

```kotlin
Braze.getInstance(this).changeUser("NEW-USER-ID", "JWT-FROM-SERVER")
```

Ou, lorsque vous avez actualisé la mi-session jeton de l’utilisateur :

```kotlin
Braze.getInstance(this).setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER")
```
{% endtab %}
{% tab Objective-C %}

Fournissez le JWT lors de l'appel [`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)):

```objc
[AppDelegate.braze changeUser:@"userId" sdkAuthSignature:@"JWT-FROM-SERVER"];
```

Ou, lorsque vous avez actualisé la mi-session jeton de l’utilisateur :

```objc
[AppDelegate.braze setSDKAuthenticationSignature:@"NEW-JWT-FROM-SERVER"];
```
{% endtab %}
{% tab Swift %}

Fournissez le JWT lors de l'appel [`changeUser`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)):

```swift
AppDelegate.braze?.changeUser(userId: "userId", sdkAuthSignature: "JWT-FROM-SERVER")
```
Ou, lorsque vous avez actualisé la mi-session jeton de l’utilisateur :

```swift
AppDelegate.braze?.set(sdkAuthenticationSignature: "NEW-JWT-FROM-SERVER")
```
{% endtab %}
{% tab Dart %}

Fournissez le JWT lors de l'appel [`changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser):

```dart
braze.changeUser("userId", sdkAuthSignature: "JWT-FROM-SERVER")
```
Ou, lorsque vous avez actualisé la mi-session jeton de l’utilisateur :

```dart
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER")
```

{% endtab %}
{% tab Flutter %}

Fournissez le JWT lorsque vous appelez `changeUser`:

```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();
braze.changeUser("NEW-USER-ID", sdkAuthSignature: "JWT-FROM-SERVER");
```

Ou, lorsque vous avez actualisé la mi-session jeton de l’utilisateur :

```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();
braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Unity %}

Fournissez le JWT lorsque vous appelez `ChangeUser`:

```csharp
BrazeBinding.ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Ou, lorsque vous avez actualisé la mi-session jeton de l’utilisateur :

```csharp
BrazeBinding.SetSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Cordova %}

Fournissez le JWT lorsque vous appelez `changeUser`:

```javascript
BrazePlugin.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Ou, lorsque vous avez actualisé la mi-session jeton de l’utilisateur :

```javascript
BrazePlugin.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab .NET MAUI (Xamarin) %}

Fournissez le JWT lorsque vous appelez `ChangeUser`:

**iOS**

```csharp
Braze.SharedInstance?.ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Ou, lorsque vous avez actualisé la mi-session jeton de l’utilisateur :

```csharp
Braze.SharedInstance?.SetSDKAuthenticationSignature("NEW-JWT-FROM-SERVER");
```

**Android**

```csharp
Braze.GetInstance(this).ChangeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Ou, lorsque vous avez actualisé la mi-session jeton de l’utilisateur :

```csharp
Braze.GetInstance(this).SetSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% tab Expo %}

Lorsque vous utilisez le plugin Braze Expo, utilisez les mêmes méthodes du SDK React Native. Fournissez le JWT lorsque vous appelez `changeUser`:

```typescript
import Braze from '@braze/react-native-sdk';

Braze.changeUser("NEW-USER-ID", "JWT-FROM-SERVER");
```

Ou, lorsque vous avez actualisé la mi-session jeton de l’utilisateur :

```typescript
import Braze from '@braze/react-native-sdk';

Braze.setSdkAuthenticationSignature("NEW-JWT-FROM-SERVER");
```
{% endtab %}
{% endtabs %}

#### Étape 2.3 : Enregistrer une fonction de rappel pour les jetons invalides {#sdk-callback}

Lorsque cette fonctionnalité est définie comme [requise](#enforcement-options), les scénarios suivants entraînent le rejet des demandes de SDK par Braze :
- Le JWT a expiré au moment où l’API Braze a été reçue
- JWT était vide ou manquant
- JWT n’a pas vérifié les clés publiques que vous avez téléchargées sur le tableau de bord de Braze

Vous pouvez utiliser `subscribeToSdkAuthenticationFailures` pour vous abonner à être averti lorsque les demandes SDK échouent pour l’une de ces raisons. Une fonction de rappel contient un objet avec les éléments suivants . [`errorCode`](#error-codes), `reason` pour l'erreur, le `userId` de la demande (l'utilisateur ne peut pas être anonyme) et le jeton d'authentification (JWT) à l'origine de l'erreur. 

Les demandes échouées seront périodiquement récupérées jusqu’à ce que votre application fournisse un nouveau JWT valide. Si cet utilisateur est toujours connecté, vous pouvez profiter de ce rappel pour demander un nouveau JWT à votre serveur et fournir au SDK de Braze ce nouveau jeton valide.

Lorsque vous recevez une erreur d'authentification, vérifiez que l'adresse `userId` indiquée dans l'erreur correspond à l'utilisateur actuellement connecté, puis récupérez une nouvelle signature sur votre serveur et fournissez-la au SDK de Braze. Vous pouvez également enregistrer ces erreurs dans votre service de surveillance ou de signalement des erreurs.

{% alert tip %}
Ces méthodes de fonction de rappel sont un excellent endroit pour ajouter votre propre service de surveillance ou d’erreur afin de suivre la fréquence à laquelle vos demandes de Braze sont rejetées.
{% endalert %}

{% tabs %}
{% tab Web %}
```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToSdkAuthenticationFailures((error) => {
  console.error("SDK authentication failed:", error);
  console.log("Error code:", error.errorCode);
  console.log("User ID:", error.userId);
  // Note: Do not log error.signature as it contains sensitive authentication credentials
  
  // Verify the error.userId matches the currently logged-in user
  // Fetch a new token from your server and set it
  fetchNewSignature(error.userId).then((newSignature) => {
    braze.setSdkAuthenticationSignature(newSignature);
  });
});
```
{% endtab %}
{% tab React Native %}
```typescript
import Braze from '@braze/react-native-sdk';

const sdkAuthErrorSubscription = Braze.addListener(
  Braze.Events.SDK_AUTHENTICATION_ERROR,
  (error) => {
    console.log(`SDK Authentication for ${error.userId} failed with error code ${error.errorCode}.`);
    
    const updated_jwt = getNewTokenSomehow(error);
    Braze.setSdkAuthenticationSignature(updated_jwt);
  }
);

// Don't forget to remove the listener when done
// sdkAuthErrorSubscription.remove();
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(this).subscribeToSdkAuthenticationFailures(error -> {
    String newToken = getNewTokenSomehow(error);
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
Braze.getInstance(this).subscribeToSdkAuthenticationFailures({ error: BrazeSdkAuthenticationErrorEvent ->
    val newToken: String = getNewTokenSomehow(error)
    Braze.getInstance(getContext()).setSdkAuthenticationSignature(newToken)
})
```
{% endtab %}
{% tab Objective-C %}

```objc
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
braze.sdkAuthDelegate = delegate;
AppDelegate.braze = braze;

// Method to implement in delegate
- (void)braze:(Braze *)braze sdkAuthenticationFailedWithError:(BRZSDKAuthenticationError *)error {
  NSLog(@"Invalid SDK Authentication Token.");
  NSString *newSignature = getNewTokenSomehow(error);
  [AppDelegate.braze setSDKAuthenticationSignature:newSignature];
}
```
{% endtab %}
{% tab Swift %}

```swift
let braze = Braze(configuration: configuration)
braze.sdkAuthDelegate = delegate
AppDelegate.braze = braze

// Method to implement in delegate
func braze(_ braze: Braze, sdkAuthenticationFailedWithError error: Braze.SDKAuthenticationError) {
  print("Invalid SDK Authentication Token.")
  let newSignature = getNewTokenSomehow(error)
  AppDelegate.braze?.set(sdkAuthenticationSignature: newSignature)
}
```
{% endtab %}
{% tab Dart %}
```dart
braze.setBrazeSdkAuthenticationErrorCallback((BrazeSdkAuthenticationError error) async {
  print("Invalid SDK Authentication Token.");
  final newSignature = getNewTokenSomehow(error);
  braze.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% tab Flutter %}
```dart
import 'package:braze_plugin/braze_plugin.dart';

BrazePlugin braze = BrazePlugin();

braze.setBrazeSdkAuthenticationErrorCallback((BrazeSdkAuthenticationError error) async {
  print("SDK Authentication for ${error.userId} failed with error code ${error.errorCode}.");
  
  String newSignature = getNewTokenSomehow(error);
  braze.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% tab Unity %}
**iOS**

Définissez le délégué d'authentification du SDK dans votre mise en œuvre native d'iOS :

```csharp
public class SdkAuthDelegate : BRZSdkAuthDelegate
{
  public void Braze(Braze braze, BRZSDKAuthenticationError error)
  {
    Debug.Log("Invalid SDK Authentication Token.");
    string newSignature = GetNewTokenSomehow(error);
    BrazeBinding.SetSdkAuthenticationSignature(newSignature);
  }
}
```

**Android**

```csharp
Braze.GetInstance(this).SubscribeToSdkAuthenticationFailures((error) => {
  string newToken = GetNewTokenSomehow(error);
  Braze.GetInstance(this).SetSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab Cordova %}
```javascript
BrazePlugin.subscribeToSdkAuthenticationFailures((error) => {
  console.log(`SDK Authentication for ${error.user_id} failed with error code ${error.error_code}.`);
  
  const newSignature = getNewTokenSomehow(error);
  BrazePlugin.setSdkAuthenticationSignature(newSignature);
});
```
{% endtab %}
{% tab .NET MAUI (Xamarin) %}
**iOS**

Définissez le délégué à l'authentification du SDK sur votre instance `Braze`:

```csharp
public class SdkAuthDelegate : BRZSdkAuthDelegate
{
  public override void Braze(Braze braze, BRZSDKAuthenticationError error)
  {
    Console.WriteLine("Invalid SDK Authentication Token.");
    string newSignature = GetNewTokenSomehow(error);
    Braze.SharedInstance?.SetSDKAuthenticationSignature(newSignature);
  }
}

// Set the delegate during initialization
var configuration = new BRZConfiguration("YOUR-API-KEY", "YOUR-ENDPOINT");
configuration.Api.SdkAuthentication = true;
var braze = new Braze(configuration);
braze.SdkAuthDelegate = new SdkAuthDelegate();
```

**Android**

```csharp
Braze.GetInstance(this).SubscribeToSdkAuthenticationFailures((error) => {
  string newToken = GetNewTokenSomehow(error);
  Braze.GetInstance(this).SetSdkAuthenticationSignature(newToken);
});
```
{% endtab %}
{% tab Expo %}
Lorsque vous utilisez le plugin Braze Expo, utilisez les mêmes méthodes du SDK React Native :

```typescript
import Braze from '@braze/react-native-sdk';

const sdkAuthErrorSubscription = Braze.addListener(
  Braze.Events.SDK_AUTHENTICATION_ERROR,
  (error) => {
    console.log(`SDK Authentication for ${error.userId} failed with error code ${error.errorCode}.`);
    
    const updated_jwt = getNewTokenSomehow(error);
    Braze.setSdkAuthenticationSignature(updated_jwt);
  }
);

// Don't forget to remove the listener when done
// sdkAuthErrorSubscription.remove();
```
{% endtab %}
{% endtabs %}

### Étape 3 : Activer l'authentification dans le tableau de bord {#braze-dashboard}

Ensuite, vous pouvez activer l'authentification dans le tableau de bord de Braze pour les apps que vous avez configurées précédemment.

Gardez à l'esprit que les requêtes SDK continueront à circuler comme d'habitude sans authentification, sauf si le paramètre d'authentification SDK de l'app est défini sur **Requis** dans le tableau de bord de Braze.

En cas de problème avec votre intégration (par exemple, votre application transmet incorrectement des jetons au SDK ou votre serveur génère des jetons invalides), désactivez cette fonctionnalité dans le tableau de bord de Braze, et les données recommenceront à circuler comme d'habitude sans vérification.

#### Options d’application {#enforcement-options}

Dans la page **Gérer les paramètres** du tableau de bord, chaque application dispose de trois états d’authentification SDK qui contrôlent la manière dont Braze vérifie les requêtes.

| Réglage| Description|
| ------ | ---------- |
| **Désactivé** | Braze ne vérifiera pas le JWT fourni à un utilisateur. (Paramètre par défaut)|
| **Facultatif** | Braze vérifiera les demandes pour les utilisateurs connectés, mais ne rejettera pas les demandes non valides. |
| **Requis** | Braze vérifiera les demandes pour les utilisateurs connectés, et rejettera les JWT non valides.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/sdk-auth-settings.png %})

Le paramètre **Facultatif** est un moyen utile de surveiller l'impact potentiel de cette fonctionnalité sur le trafic SDK de votre application.

Un JWT invalide sera signalé dans les deux états, **facultatif** et **obligatoire**, mais seul l'état **obligatoire** rejettera les demandes de SDK, obligeant les applications à réessayer et à demander un nouveau JWT.

## Gérer les clés publiques {#key-management}

### Ajouter une clé publique

Vous pouvez ajouter jusqu'à trois clés publiques pour chaque application : une clé principale, une clé secondaire et une clé tertiaire. Si nécessaire, vous pouvez également ajouter la même clé à plusieurs applications. Pour ajouter une clé publique :

1. Rendez-vous sur le tableau de bord de Braze et sélectionnez **Paramètres** > **Paramètres de l'application**.
2. Choisissez une application dans votre liste d'applications disponibles.
3. Sous **Authentification SDK**, sélectionnez **Ajouter une clé publique**.
4. Saisissez une description facultative, collez votre clé publique, puis sélectionnez **Ajouter une clé publique**.

### Attribuer une nouvelle clé primaire

Pour attribuer une clé secondaire ou tertiaire comme nouvelle clé principale :

1. Rendez-vous sur le tableau de bord de Braze et sélectionnez **Paramètres** > **Paramètres de l'application**.
2. Choisissez une application dans votre liste d'applications disponibles.
3. Sous **Authentification SDK**, choisissez une clé et sélectionnez **Gérer** > **Faire une clé primaire.**

### Supprimer une clé

Pour supprimer une clé principale, [attribuez d'abord une nouvelle clé principale](#assign-a-new-primary-key), puis supprimez votre clé. Pour supprimer une clé non primaire :

1. Rendez-vous sur le tableau de bord de Braze et sélectionnez **Paramètres** > **Paramètres de l'application**.
2. Choisissez une application dans votre liste d'applications disponibles.
3. Sous **Authentification SDK**, choisissez une clé non primaire et sélectionnez **Gérer** > **Supprimer la clé publique.**

## Analyses {#analytics}

Chaque application affichera une ventilation des erreurs d'authentification SDK collectées lorsque cette fonctionnalité est dans l'état **Facultatif** et **Requis**.

Les données sont disponibles en temps réel, et vous pouvez déplacer le curseur sur les points du graphique pour voir la répartition des erreurs pour une date donnée.

![Graphique montrant le nombre d’erreurs d’authentification. Le nombre total d’erreurs, le type d’erreur et la plage de dates réglables sont également affichés.]({% image_buster /assets/img/sdk-auth-analytics.png %}){: style="max-width:80%"}

## Codes d’erreur {#error-codes}

| code d'erreur| Cause de l’erreur | Description | Marche à suivre pour résoudre le problème |
| --------  | ------------ | ---------  | ---------  |
| 10 | `EXPIRATION_REQUIRED` | L’expiration est un champ obligatoire pour l’utilisation de Braze.| Ajoutez un champ `exp` ou un champ d'expiration à votre logique de création de JWT. |
| 20 | `DECODING_ERROR` | Clé publique non conforme ou erreur générale non détectée.| Copiez votre JWT dans un outil de test de JWT pour diagnostiquer pourquoi votre JWT a un format invalide. |
| 21 | `SUBJECT_MISMATCH` | Les sujets attendus et réels ne sont pas les mêmes.| Le champ `sub` doit être le même ID que celui transmis à la méthode `changeUser` du SDK. |
| 22 | `EXPIRED` | Le jeton fourni a expiré.| Prolongez votre expiration ou actualisez périodiquement les jetons avant qu'ils n'expirent. |
| 23 | `INVALID_PAYLOAD` | La charge utile jeton n’est pas valide.| Copiez votre JWT dans un outil de test de JWT pour diagnostiquer pourquoi votre JWT a un format invalide. |
| 24 | `INCORRECT_ALGORITHM` | L’algorithme du jeton n’est pas pris en charge.| Modifiez votre JWT pour utiliser le chiffrement `RS256`. Les autres types ne sont pas pris en charge. |
| 25 | `PUBLIC_KEY_ERROR` | La clé publique n’a pas pu être convertie au format approprié.| Copiez votre JWT dans un outil de test de JWT pour diagnostiquer pourquoi votre JWT a un format invalide. |
| 26 | `MISSING_TOKEN` | Aucun jeton n’a été fourni dans la demande.| Assurez-vous que vous passez un jeton lorsque vous appelez `changeUser(id, token)` et que votre jeton n'est pas vide.|
| 27 | `NO_MATCHING_PUBLIC_KEYS` | Aucune clé publique ne correspond au jeton fourni.| La clé privée utilisée dans le JWT ne correspond à aucune clé publique configurée pour votre appli. Confirmez que vous avez ajouté les clés publiques à la bonne application de votre espace de travail qui correspond à cette clé API.|
| 28 | `PAYLOAD_USER_ID_MISMATCH` | Les ID des utilisateurs dans les données utiles de la demande ne correspondent pas tous à ce qui est exigé.| Ceci est inattendu et peut donner lieu à une charge utile malformée. Ouvrez un ticket d'assistance pour obtenir de l'aide. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Foire aux questions (FAQ) {#faq}

#### Cette fonctionnalité doit-elle être activée sur toutes mes applications en même temps ? {#faq-app-by-app}

Non, cette fonctionnalité peut être activée pour des applications spécifiques et n’a pas besoin d’être utilisée sur toutes vos applications, en même temps.

#### Que se passe-t-il pour les utilisateurs qui sont toujours sur les versions antérieures de mon application ? {#faq-sdk-backward-compatibility}

Lorsque vous commencez à faire appliquer cette fonctionnalité, les demandes effectuées par les versions anciennes d’applications seront rejetées par Braze et récupérées par les SDK. Une fois que les utilisateurs auront mis à jour leur application vers une version prise en charge, les demandes en file d'attente seront à nouveau acceptées.

Dans la mesure du possible, il convient de faire en sorte que les utilisateurs effectuent la mise à niveau comme pour toute autre mise à niveau obligatoire. Vous pouvez également laisser la fonctionnalité [en option](#enforcement-options) jusqu'à ce que vous constatiez qu'un pourcentage acceptable d'utilisateurs a effectué la mise à niveau.

#### Quelle expiration dois-je utiliser lors de la génération d'un JWT ? {#faq-expiration}

Nous vous recommandons d’utiliser la valeur la plus élevée parmi : la durée moyenne de la session, l’expiration du cookie/jeton de la session, ou la fréquence à laquelle votre application rafraîchirait autrement le profil utilisateur actuel.

#### Que se passe-t-il si un JWT expire au milieu de la session d’un utilisateur ? {#faq-jwt-expiration}

Si le jeton d'un utilisateur expire à mi-session, le SDK dispose d'une [fonction de rappel](#sdk-callback) qu'il invoquera pour indiquer à votre application qu'un nouveau JWT est nécessaire pour continuer à envoyer des données à Braze.

#### Que se passe-t-il si mon intégration côté serveur est interrompue et que je ne peux plus créer un JWT ? {#faq-server-downtime}

Si votre serveur n'est pas en mesure de fournir un JWT ou si vous remarquez un problème d'intégration, vous pouvez toujours désactiver la fonctionnalité dans le tableau de bord de Braze.

Une fois désactivée, toutes les demandes de SDK échouées en attente seront finalement récupérées par le SDK et acceptées par Braze.

#### Pourquoi cette fonction utilise-t-elle des clés publiques/privées plutôt que des secrets partagés ? {#faq-shared-secrets}

Lors de l'utilisation de secrets partagés, toute personne ayant accès à ce secret partagé, comme la page du tableau de bord de Braze, serait en mesure de générer des jetons et d'usurper l'identité de vos utilisateurs finaux.

Nous utilisons plutôt des clés publiques/privées pour que ni même les employés de Braze (seuls les utilisateurs de votre tableau de bord) aient accès à vos clés privées.

#### Comment les demandes rejetées seront-elles récupérées ? {#faq-retry-logic}

Lorsqu'une demande est rejetée en raison d'une erreur d'authentification, le SDK invoque votre rappel utilisé pour actualiser le JWT de l'utilisateur. 

Les demandes réessaieront périodiquement en utilisant une approche de délais exponentielle. Après 50 tentatives consécutives échouées, les nouvelles tentatives seront interrompues jusqu’à la prochaine session. Chaque SDK dispose également d’une méthode qui permet de demander manuellement un rafraîchissement des données.

#### Pouvez-vous utiliser l'authentification SDK pour les utilisateurs anonymes ? {#faq-anonymous-users}

Non. L'authentification par le SDK ne fonctionne pas pour les utilisateurs anonymes.
