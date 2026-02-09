## À propos du SDK du moteur Unreal Braze

Avec le plugin Braze Unreal SDK, vous pouvez :

* Évaluer et suivre les sessions dans votre application ou votre jeu
* Suivre des achats et des événements personnalisés dans l’application
* Mettre à jour les profils d’utilisateur avec des attributs standard et personnalisés
* Envoyer des notifications push
* Intégrer vos applications Unreal à des parcours Canvas plus importants
* Envoyer des communications cross-canaux, comme par exemple par e-mail ou SMS, en fonction des interactions dans l’application

## Intégration du SDK d'Unreal Engine

### Étape 1 : Ajouter le plugin Braze

Dans votre terminal, clonez le [dépôt GitHub Unreal Engine Braze SDK](https://github.com/braze-inc/braze-unreal-sdk).

```bash
git clone git@github.com:braze-inc/braze-unreal-sdk.git
```

Copiez ensuite le répertoire `BrazeSample/Plugins/Braze` et ajoutez-le dans le dossier Plugin de votre application.

### Étape 2 : Activer le plugin

Activez le plugin pour votre projet C++ ou Blueprint.

{% tabs %}
{% tab C++ %}
Pour les projets C++, configurez votre module pour qu'il fasse référence au module Braze. Dans votre `\*.Build.cs file`, ajoutez `"Braze"` à votre `PublicDependencyModuleNames`.

```cpp
PublicDependencyModuleNames.AddRange(new string[] { "Core", "CoreUObject", "Engine", "InputCore", "Braze" });
```
{% endtab %}

{% tab Plan d'action %}
Pour les projets Blueprint, allez dans **Settings** > **Plugins**, puis à côté de **Braze** cochez **Enabled**.

![EnablePlugin]({% image_buster /assets/img/unreal_engine/EnablePlugin.png %})
{% endtab %}
{% endtabs %}

### Étape 3 : Définissez votre clé API et votre endpoint.

Définissez votre clé API et votre endpoint dans le projet `DefaultEngine.ini`.

```cpp
[/Script/Braze.BrazeConfig]
bAutoInitialize=True ; true by default, initialize when the project starts
AndroidApiKey= ; your API key
IOSApiKey= ; your API key
CustomEndpoint= ; your endpoint
```

{% alert warning %}
Pour les projets ciblant le SDK Android 31+, Unreal créera des builds qui échoueront lors de l'installation sur les appareils Android 12+ avec l'erreur INSTALL_PARSE_FAILED_MANIFEST_MALFORMED. Pour corriger ce problème, localisez le fichier patch `UE4_Engine_AndroidSDK_31_Build_Fix.patch` git à la racine de ce dépôt et appliquez-le à votre création des sources d'Unreal.
{% endalert %}

### Étape 4 : Initialiser manuellement le SDK (facultatif)

Par défaut, le SDK s'initialise automatiquement au lancement. Si vous souhaitez avoir plus de contrôle sur l'initialisation (par exemple, attendre le consentement de l'utilisateur ou définir le niveau de journalisation), vous pouvez désactiver `AutoInitialize` dans votre site `DefaultEngine.ini` et initialiser manuellement en C++ ou en Blueprint.

{% tabs %}
{% tab C++ %}
En C++ natif, accédez au BrazeSubsystem et appelez `InitializeBraze()` en lui transmettant éventuellement un Config pour remplacer les paramètres de Engine.ini.

```cpp
UBrazeSubsystem* const BrazeSubsystem = GEngine->GetEngineSubsystem<UBrazeSubsystem>();
UBraze* const BrazeInstance = BrazeSubsystem->InitializeBraze();
```
{% endtab %}

{% tab Plan d'action %}
Dans Blueprint, les mêmes fonctions sont accessibles en tant que nœuds Blueprint :  
Utilisez le nœud `GetBrazeSubsystem` pour appeler son nœud `Initialize`.  
Un objet BrazeConfig peut éventuellement être créé dans Blueprint et transmis à `Initialize`

![InitializeBraze]({% image_buster /assets/img/unreal_engine/InitializeBraze.png %})
{% endtab %}
{% endtabs %}

## Configurations optionnelles

### Journalisation

{% tabs local %}
{% tab Android %}
Vous pouvez définir le niveau de journalisation au moment de l'exécution en utilisant C++ ou dans un nœud de Blueprint.

{% subtabs %}
{% subtab C++ %}
Pour définir le niveau de journalisation au moment de l'exécution, appelez `UBrazeSubsystem::AndroidSetLogLevel`.

```cpp
UBrazeSubsystem* const BrazeSubsystem = GEngine->GetEngineSubsystem<UBrazeSubsystem>();
BrazeSubsystem->AndroidSetLogLevel(EBrazeLogLevel::Verbose);
UBraze* const BrazeInstance = BrazeSubsystem->InitializeBraze();
```
{% endsubtab %}

{% subtab Blueprint %}
Dans Blueprint, vous pouvez utiliser le nœud **Android Set Log Level :** 

![Le nœud Android Set Log Level dans Blueprint.]({% image_buster /assets/img/unreal_engine/AndroidSetLogLevel.png %})
{% endsubtab %}
{% endsubtabs %}

Afin de s'assurer que la journalisation est définie lorsque le SDK Braze Initialize est appelé, il est recommandé de l'appeler avant `InitializeBraze`.
{% endtab %}

{% tab iOS %}
Pour activer le niveau de journalisation dans le site `info.plist`, allez dans **Réglages** > **Réglages du projet**, puis sélectionnez **iOS** sous **Plateformes**. Sous **Extra PList Data**, recherchez **Additional Plist Data**, puis entrez votre niveau de journal :

```xml
<key>Appboy</key>
<dict>
  <key>LogLevel</key>
  <string>0</string>
</dict>
```

Le niveau de journalisation par défaut est 8, ce qui correspond à une journalisation minimale. Pour en savoir plus sur les niveaux de journalisation : [Autres personnalisations du SDK]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/)
{% endtab %}
{% endtabs %}
