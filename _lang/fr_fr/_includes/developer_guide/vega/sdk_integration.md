## À propos du SDK Braze Vega

Le SDK Braze Vega vous permet de collecter des analyses et d'afficher de riches messages in-app à vos utilisateurs. La plupart des méthodes du SDK Braze Vega sont asynchrones et renvoient des promesses qui doivent être attendues ou résolues.

## Intégration du SDK Braze Vega

### Étape 1 : Installer la bibliothèque Braze

Installez le SDK Braze Vega à l'aide de votre gestionnaire de paquets préféré.

{% tabs local %}
{% tab npm %}
Si votre projet utilise NPM, vous pouvez ajouter le SDK Braze Vega en tant que dépendance.

```bash
npm install @braze/vega-sdk --save
```

Après l'installation, vous pouvez importer les méthodes dont vous avez besoin :

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}

{% tab yarn %}
Si votre projet utilise Yarn, vous pouvez ajouter le SDK Braze Vega comme dépendance.

```bash
yarn add @braze/vega-sdk
```

Après l'installation, vous pouvez importer les méthodes dont vous avez besoin :

```javascript
import { initialize, changeUser, openSession } from "@braze/vega-sdk";
```
{% endtab %}
{% endtabs %}

### Étape 2 : Initialiser le SDK

Une fois le SDK Braze Vega ajouté à votre projet, initialisez la bibliothèque à l'aide de la clé API et de l'[URL de l'endpoint du SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) que vous trouverez dans **Settings** > **App Settings** dans votre tableau de bord Braze.

{% alert important %}
Vous devez attendre ou résoudre la promesse `changeUser` avant d'appeler d'autres méthodes Braze, sinon les événements et les attributs risquent d'être définis sur le mauvais utilisateur.
{% endalert %}

```javascript
import { useEffect } from "react-native";
import {
  initialize,
  changeUser,
  logCustomEvent,
  openSession,
  setCustomUserAttribute,
  setUserCountry
} from "@braze/vega-sdk";

const App = () => {
  useEffect(() => {
    const initBraze = async () => {
      // Initialize the SDK
      await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
        sessionTimeoutInSeconds: 60,
        appVersionNumber: "1.2.3.4",
        enableLogging: true, // set to `true` for debugging
      });

      // Change user
      await changeUser("user-id-123");
      
      // Start a session
      await openSession();
      
      // Log custom events and set user attributes
      logCustomEvent("visited-page", { pageName: "home" });
      setCustomUserAttribute("my-attribute", "my-attribute-value");
      setUserCountry("USA");
    };
    
    initBraze();
  }, []);
  
  return (
    // Your app components
  );
};
```

{% alert important %}
Les utilisateurs anonymes peuvent être pris en compte dans votre [MAU]({{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#monthly-active-users). Par conséquent, vous pouvez charger ou initialiser conditionnellement le SDK pour exclure ces utilisateurs de votre décompte de MAU.
{% endalert %}

## Configurations optionnelles

### Journalisation

Vous pouvez activer la journalisation SDK pour faciliter le débogage et la résolution des problèmes. Il existe plusieurs façons d'activer la journalisation.

#### Activer la journalisation pendant l'initialisation

Passez `enableLogging: true` à `initialize()` pour enregistrer les messages de débogage dans la console :

```javascript
initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  enableLogging: true
});
```

{% alert important %}
Les journaux de base sont visibles par tous les utilisateurs, il faut donc envisager de désactiver la journalisation avant de mettre votre code en production.
{% endalert %}

#### Activer la journalisation après l'initialisation

Utilisez `toggleLogging()` pour activer ou désactiver la journalisation du SDK après l'initialisation :

```javascript
import { toggleLogging } from "@braze/vega-sdk";

// Enable logging
toggleLogging();
```

#### Journalisation personnalisée

Utilisez `setLogger()` pour fournir une fonction d'enregistrement personnalisée afin de mieux contrôler la manière dont les enregistrements du SDK sont traités :

```javascript
import { setLogger } from "@braze/vega-sdk";

setLogger((message) => {
  console.log("Braze Custom Logger: " + message);
  // Add your custom logging logic here
});
```

### Options de configuration

Vous pouvez transmettre des options de configuration supplémentaires à `initialize()` pour personnaliser le comportement du SDK :

```javascript
await initialize("YOUR-API-KEY", "YOUR-SDK-ENDPOINT", {
  sessionTimeoutInSeconds: 60,        // Configure session timeout (default is 30 seconds)
  appVersionNumber: "1.2.3.4",        // Set your app version
  enableLogging: true,                 // Enable SDK logging
});
```

## Mise à niveau du SDK

Lorsque vous référencez le SDK Braze Vega depuis NPM ou Yarn, vous pouvez passer à la dernière version en mettant à jour la dépendance de votre paquet :

```bash
npm update @braze/vega-sdk
# or, using yarn:
yarn upgrade @braze/vega-sdk
```

## Tester votre intégration

Pour vérifier que l'intégration SDK fonctionne correctement :

1. Initialisez le SDK avec `enableLogging: true` pour voir les messages de débogage dans la console.
2. Veillez à `await changeUser()` avant d'appeler d'autres méthodes du SDK
3. Appelez `await openSession()` pour commencer une session
4. Vérifiez dans votre tableau de bord de Braze, sous **Aperçu**, que les données de la session sont bien enregistrées.
5. Testez l'enregistrement d'un événement personnalisé et vérifiez qu'il apparaît dans votre tableau de bord.


