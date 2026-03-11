---
page_order: 1.4
nav_title: Journalisation détaillée
article_title: Consignation prolixe
description: "Veuillez découvrir comment activer la journalisation détaillée pour le SDK Braze, collecter des journaux à des fins de résolution des problèmes et les partager avec l'assistance Braze."
---

# Consignation prolixe

> La journalisation détaillée fournit des informations précises et de bas niveau provenant du SDK Braze, vous permettant ainsi de comprendre comment le SDK s'initialise, communique avec les serveurs et traite les canaux de communication tels que les notifications push, les messages in-app et les cartes de contenu.

Lorsque quelque chose ne fonctionne pas comme prévu, par exemple lorsqu'une notification push n'arrive pas, qu'un message in-app ne s'affiche pas ou que les données utilisateur ne se synchronisent pas, les journaux détaillés vous aident à identifier la cause profonde. Au lieu de deviner, vous pouvez observer précisément ce que fait le SDK à chaque étape.

{% alert tip %}
Si vous souhaitez effectuer un débogage sans activer manuellement la journalisation détaillée, vous pouvez utiliser le [débogueur SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) pour créer des sessions de débogage directement dans le tableau de bord de Braze.
{% endalert %}

## Quand utiliser la journalisation détaillée

Activez la journalisation détaillée lorsque nécessaire :

- **Vérifiez l'initialisation du SDK** : Veuillez vérifier que le SDK démarre correctement avec la clé API et l'endpoint appropriés.
- **Résolution des problèmes de réception/distribution des messages** : Veuillez vérifier si les jetons push sont enregistrés, si les messages in-app sont déclenchés ou si les cartes de contenu sont synchronisées.
- **Déboguer les liens profonds** : Veuillez vérifier que le SDK reçoit et ouvre les liens profonds provenant des notifications push, des messages in-app ou des cartes de contenu.
- **Vérifier le suivi de session** : Veuillez vérifier que les sessions commencent et se terminent comme prévu.
- **Diagnostiquer les problèmes de connectivité** : Veuillez examiner les requêtes réseau et les réponses entre le SDK et les serveurs Braze.

## Activation de la journalisation détaillée

{% alert important %}
Les journaux détaillés sont destinés exclusivement aux environnements de développement et de test. Veuillez désactiver la journalisation détaillée avant de déployer votre application en production afin d'éviter que des informations sensibles ne soient exposées.
{% endalert %}

{% tabs %}
{% tab Android %}

Activez la journalisation détaillée avant tout autre appel SDK dans votre`Application.onCreate()`méthode afin de capturer la sortie la plus complète.

**En code :**

{% subtabs %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.VERBOSE);
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.VERBOSE
```
{% endsubtab %}
{% endsubtabs %}

**Dans `braze.xml`:**

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```

Pour vérifier que la journalisation détaillée est activée, veuillez rechercher`V/Braze`dans votre sortie Logcat. Par exemple :

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

Pour plus de détails, veuillez consulter [la documentation relative à la journalisation dans le SDK Android]({{site.baseurl}}/developer_guide/sdk_integration#android_enabling-logs).

{% endtab %}
{% tab Swift %}

Veuillez définir le niveau de journalisation sur`.debug` votre`Braze.Configuration`objet lors de l'initialisation.

{% subtabs %}
{% subtab SWIFT %}
```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
configuration.logger.level = .debug
let braze = Braze(configuration: configuration)
```
{% endsubtab %}
{% subtab OBJECTIVE-C %}
```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:@"<BRAZE_API_KEY>"
                                                                  endpoint:@"<BRAZE_ENDPOINT>"];
[configuration.logger setLevel:BRZLoggerLevelDebug];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```
{% endsubtab %}
{% endsubtabs %}

Le`.debug`niveau est le plus détaillé et est recommandé pour la résolution des problèmes. Pour plus de détails, veuillez consulter [la documentation relative à la journalisation du SDK Swift]({{site.baseurl}}/developer_guide/sdk_integration#swift_log-levels).

{% endtab %}
{% tab Web %}

Veuillez ajouter`?brazeLogging=true`  en tant que paramètre URL ou activer la journalisation lors de l'initialisation du SDK :

```javascript
braze.initialize('YOUR-API-KEY', {
    baseUrl: 'YOUR-SDK-ENDPOINT',
    enableLogging: true
});
```

Vous pouvez également basculer la journalisation après l'initialisation :

```javascript
braze.toggleLogging();
```

Les journaux apparaissent dans l'onglet **Console** des outils de développement de votre navigateur. Pour plus de détails, veuillez consulter [la section Journalisation du SDK Web]({{site.baseurl}}/developer_guide/sdk_integration#web_logging).

{% endtab %}
{% tab Unity %}

1. Ouvrez les paramètres de configuration de Braze en sélectionnant **Braze** > **Configuration de Braze**.
2. Veuillez sélectionner le menu déroulant **Afficher les paramètres Android de Braze**.
3. Dans le champ **Niveau de journalisation SDK**, veuillez saisir `0`.

{% endtab %}
{% tab React Native %}

Définissez le niveau de journalisation lors de la configuration du SDK :

```javascript
const configuration = new Braze.BrazeConfiguration('YOUR-API-KEY', 'YOUR-SDK-ENDPOINT');
configuration.logLevel = Braze.LogLevel.Verbose;
```

{% endtab %}
{% endtabs %}

## Collecte des journaux

Après avoir activé la journalisation détaillée, veuillez reproduire le problème que vous rencontrez lors de la résolution des problèmes, puis collecter les journaux à partir de la console ou de l'outil de débogage de votre plateforme.

{% tabs %}
{% tab Android %}

Veuillez utiliser **Logcat** dans Android Studio pour enregistrer les journaux :

1. Veuillez connecter votre appareil ou démarrer un émulateur.
2. Dans Android Studio, veuillez ouvrir **Logcat** à partir du panneau inférieur.
3. Veuillez filtrer par`V/Braze`ou`D/Braze`pour isoler la sortie du SDK Braze.
4. Veuillez reproduire le problème.
5. Veuillez copier les journaux pertinents et les enregistrer dans un fichier texte.

{% endtab %}
{% tab iOS %}

Veuillez utiliser l'application **Console** sur macOS pour enregistrer les journaux :

1. Veuillez installer l'application sur votre appareil avec la journalisation détaillée activée.
2. Veuillez connecter votre appareil à votre Mac.
3. Veuillez ouvrir l'application **Console** et sélectionner votre appareil dans la barre latérale **Appareils**.
4. Veuillez filtrer les journaux en utilisant`Braze`  ou`BrazeKit`  dans la barre de recherche.
5. Veuillez reproduire le problème.
6. Veuillez copier les journaux pertinents et les enregistrer dans un fichier texte.

{% endtab %}
{% tab Web %}

Veuillez utiliser les outils de développement de votre navigateur :

1. Veuillez ouvrir les outils de développement de votre navigateur (généralement **F12** ou **Cmd+Option+I**).
2. Veuillez vous rendre dans l'onglet **Console**.
3. Veuillez reproduire le problème.
4. Veuillez copier la sortie de la console et l'enregistrer dans un fichier texte.

{% endtab %}
{% endtabs %}

{% alert tip %}
Lorsque vous collectez des journaux pour l'assistance Braze, veuillez commencer l'enregistrement avant de lancer votre application et poursuivre jusqu'à ce que le problème soit résolu. Cela permet de saisir l'intégralité de la séquence des événements.
{% endalert %}

## Lecture des journaux détaillés

Les journaux détaillés suivent une structure cohérente qui vous aide à suivre les activités du SDK. Pour apprendre à interpréter les sorties de journal pour des canaux spécifiques, y compris les entrées clés à rechercher et les modèles de résolution des problèmes courants, veuillez consulter [la section Lecture des journaux détaillés]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs).

## Partage des journaux avec le service d'assistance Braze

Lorsque vous contactez l'assistance Braze pour un problème lié au SDK, veuillez inclure les informations suivantes :

1. **Fichier journal détaillé** : Enregistrement complet des journaux depuis avant le lancement de l'application jusqu'à la survenue du problème.
2. **Étapes à suivre pour reproduire** le problème : Une description claire des actions de déclenchement du problème.
3. **Comportement attendu par rapport au comportement réel** : Ce que vous vous attendiez à ce qui se produise et ce qui s'est produit à la place.
4. **Version du SDK** : La version du SDK Braze que vous utilisez.
5. **Plateforme et version du système d'exploitation** : Par exemple, iOS 18.0, Android 14 ou Chrome 120.