---
nav_title: Mise en œuvre avancée
article_title: Mise en œuvre avancée du SDK
platform: 
  - Unity
  - iOS
  - Android
page_order: 2
description: "Cet article de référence traite de l’implémentation avancée du SDK pour la plateforme Unity."
---

# Mise en œuvre avancée

> Cet article de référence traite de l’implémentation avancée du SDK pour la plateforme Unity.

## Personnaliser le package Unity

Vous pouvez choisir de personnaliser et d’exporter le package Unity de Braze en utilisant les scripts fournis.

1. Clonez le [projet GitHub du SDK Braze Unity](https://github.com/appboy/appboy-unity-sdk):

	```bash
	git clone git@github.com:braze-inc/braze-unity-sdk.git
	```
2. Dans le répertoire `braze-unity-sdk/scripts`, exécutez `./generate_package.sh` pour exporter les packages Unity. Unity doit être ouvert pendant l’exécution de `generate_package.sh`.
3. Les packages seront exportés vers `braze-unity-sdk/unity-package/`.
4. Dans l'éditeur Unity, importez le package souhaité dans votre projet Unity en naviguant vers **Assets** > **Import Package** > **Custom Package**.
5. (facultatif) Désélectionnez tous les fichiers que vous ne souhaitez pas importer.

Vous pouvez personnaliser le package Unity exporté en modifiant à la fois `generate_package.sh` et le script d’exportation situé sur `Assets/Editor/Build.cs`.

## Compatibilité Prime 31

Pour utiliser le plug-in Unity de Braze avec les plug-ins Prime31, modifiez le `AndroidManifest.xml` de votre projet pour utiliser les classes d’activité compatibles Prime31. Modifier toutes les références de
`com.braze.unity.BrazeUnityPlayerActivity` vers `com.braze.unity.prime31compatible.BrazeUnityPlayerActivity`

## Notification push Amazon ADM

Braze prend en charge l'intégration de [Amazon ADM push](https://developer.amazon.com/public/apis/engage/device-messaging) dans les applications Unity. Si vous souhaitez intégrer les notifications push Amazon ADM, créez un fichier appelé `api_key.txt` contenant votre clé API ADM et placez-le dans le dossier `Plugins/Android/assets/`.  Pour plus d'informations sur l'intégration d'Amazon ADM avec Braze, consultez nos [instructions d'intégration des notifications push ADM]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/adm_push_notifications/).

## Options d’implémentation avancées du SDK Android {#android-sdk-advanced}

### Activation de la journalisation détaillée dans l'éditeur Unity
Pour activer la journalisation verbeuse dans l'éditeur Unity, procédez comme suit :

1. Ouvrez les paramètres de configuration de Braze en sélectionnant **Braze** > **Configuration de Braze**.
2. Cliquez sur le menu déroulant **Afficher les paramètres Android de Braze**.
3. Dans le champ **Niveau de journalisation du SDK**, saisissez la valeur 0.

### Extension du lecteur Braze Unity (Android) {#extending-braze-unity-player}

L'exemple de fichier `AndroidManifest.xml` fourni contient une classe d'activité enregistrée, [`BrazeUnityPlayerActivity`](https://github.com/braze-inc/braze-android-sdk/blob/e804cb3a10ae68364b354b52abf1bef8a0d1a9dc/android-sdk-unity/src/main/java/com/braze/unity/BrazeUnityPlayerActivity.kt). Cette classe est intégrée au SDK Braze et étend `UnityPlayerActivity` à la gestion des sessions, l’enregistrement des messages in-app, la journalisation des analyses des notifications push et bien plus encore. Voir [Unity](https://docs.unity3d.com/Manual/AndroidUnityPlayerActivity.html) pour plus d'informations sur l'extension de la classe `UnityPlayerActivity`.

Si vous créez votre propre `UnityPlayerActivity` dans un projet de bibliothèque ou de plugin, vous devrez étendre notre `BrazeUnityPlayerActivity` pour intégrer votre fonctionnalité personnalisée avec Braze. Avant de commencer à travailler sur l’extension `BrazeUnityPlayerActivity`, suivez nos instructions pour intégrer Braze dans votre projet Unity.
1. Ajoutez le SDK Android de Braze en tant que dépendance à votre bibliothèque ou à votre projet de plug-in comme décrit dans les [instructions d'intégration du SDK Android de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/).
2. Intégrez notre `.aar` Unity, qui contient notre fonctionnalité spécifique à Unity, à votre projet de bibliothèque Android que vous constituez pour Unity. Le `appboy-unity.aar` est disponible dans notre [dépôt public](https://github.com/braze-inc/braze-unity-sdk/tree/master/Assets/Plugins/Android). Une fois que notre bibliothèque Unity a été intégrée avec succès, modifiez votre `UnityPlayerActivity` pour étendre `BrazeUnityPlayerActivity`.
3. Exportez votre bibliothèque ou votre projet de plug-in et déposez-le dans `/<your-project>/Assets/Plugins/Android` de manière habituelle. N’incluez pas de code source Braze dans votre bibliothèque ou votre plug-in, car ils seront déjà présents dans `/<your-project>/Assets/Plugins/Android`.
4. Modifier votre `/<your-project>/Assets/Plugins/Android/AndroidManifest.xml` pour spécifier votre sous-classe `BrazeUnityPlayerActivity` comme activité principale.

Vous devriez maintenant pouvoir mettre en package un `.apk` depuis l’IDE Unity qui est entièrement intégré à Braze et contient votre fonctionnalité `UnityPlayerActivity` personnalisée.

## Options d’implémentation avancée du SDK iOS {#ios-sdk-advanced}

### Activation de la journalisation détaillée dans l'éditeur Unity
Pour activer la journalisation verbeuse dans l'éditeur Unity, procédez comme suit :

1. Ouvrez les paramètres de configuration de Braze en sélectionnant **Braze** > **Configuration de Braze**.
2. Cliquez sur le menu déroulant **Afficher les paramètres Braze iOS**.
3. Dans le champ **Niveau de journalisation du SDK**, saisissez la valeur 0.

### Extension du SDK (iOS)

Pour étendre les comportements du SDK, bifurquez le [projet GitHub du SDK Unity de Braze](https://github.com/appboy/appboy-unity-sdk) et apportez les modifications nécessaires.

Pour publier votre code modifié en tant que package Unity, consultez nos [cas d'utilisation avancés]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/advanced_use_cases/).

### Passer d’une intégration manuelle à une intégration automatisée (iOS)

Pour profiter de l’intégration automatisée iOS proposée dans le SDK Unity de Braze, suivez ces étapes pour passer d’un mode manuel à une intégration automatisée.

1. Supprimez tous les codes liés à Braze de votre sous-classe `UnityAppController` de projet Xcode.
2. Supprimez les bibliothèques iOS de Braze de votre projet Unity ou Xcode (telles que `Appboy_iOS_SDK.framework` et `SDWebImage.framework`) et [importez le package Unity de Braze](#step-1-importing-the-braze-unity-package) dans votre projet Unity.
3. Suivez les instructions d'intégration sur [la configuration de votre clé API via Unity](#step-2-setting-your-api-key).

