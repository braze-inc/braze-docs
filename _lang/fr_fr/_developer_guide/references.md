---
nav_title: "Références et exemples d'applications"
article_title: "Références, référentiels et exemples d'applications du SDK de Braze"
page_order: 5.5
description: "Il s'agit d'une liste de documentation de référence, de dépôts GitHub et d'exemples d'applications appartenant à chaque SDK Braze."
---

# Références, référentiels et exemples d'applications

> Il s'agit d'une liste de documentation de référence, de dépôts GitHub et d'exemples d'applications appartenant à chaque SDK Braze. La documentation de référence d'un SDK détaille les classes, types, fonctions et variables disponibles. Le dépôt GitHub fournit quant à lui des informations sur les déclarations de fonctions et d'attributs, les modifications de code et les versions du SDK. Chaque dépôt comprend également des exemples d'applications entièrement constructibles que vous pouvez utiliser pour tester les fonctionnalités de Braze ou mettre en œuvre en même temps que vos propres applications.

## Liste des ressources

{% alert note %}
Actuellement, certains SDK n'ont pas de documentation de référence dédiée, mais nous y travaillons activement.
{% endalert %}

| Plateforme          | Article de référence                                                                                                                                    | Référentiel                                                                 | Exemple d’application                                                                |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| SDK Android       | [Documentation de référence](https://braze-inc.github.io/braze-android-sdk/kdoc/index.html)                                                                           | [Dépôt GitHub](https://github.com/braze-inc/braze-android-sdk)      | [Exemple d’application](https://github.com/braze-inc/braze-android-sdk/tree/master/samples)      |
| SDK Swift         | [Documentation de référence](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze)                                                                | [Dépôt GitHub](https://github.com/braze-inc/braze-swift-sdk)            | [Exemple d’application](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples)            |
| Web SDK           | [Documentation de référence](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize)                                                               | [Dépôt GitHub](https://github.com/braze-inc/braze-web-sdk)              | [Exemple d’application](https://github.com/braze-inc/braze-web-sdk/tree/master/sample-builds)              |
| SDK Cordova       | [Dossier de déclaration](https://github.com/braze-inc/braze-cordova-sdk/blob/master/www/BrazePlugin.js)                                      | [Dépôt GitHub](https://github.com/braze-inc/braze-cordova-sdk)      | [Exemple d’application](https://github.com/braze-inc/braze-cordova-sdk/tree/master/sample-project)      |
| SDK Flutter       | [Documentation de référence](https://pub.dev/documentation/braze_plugin/latest/braze_plugin/)                                                   | [Dépôt GitHub](https://github.com/braze-inc/braze-flutter-sdk)      | [Exemple d’application](https://github.com/braze-inc/braze-flutter-sdk/tree/master/example)      |
| React Native SDK  | [Dossier de déclaration](https://github.com/braze-inc/braze-react-native-sdk/blob/master/src/index.d.ts)                   | [Dépôt GitHub](https://github.com/braze-inc/braze-react-native-sdk) | [Exemple d’application](https://github.com/braze-inc/braze-react-native-sdk/tree/master/BrazeProject) |
| SDK Roku          | N/A                                                                                                                                                         | [Dépôt GitHub](https://github.com/braze-inc/braze-roku-sdk)            | [Exemple d’application](https://github.com/braze-inc/braze-roku-sdk/tree/main/torchietv)            |
| SDK Unity         | [Fichier de déclaration](https://github.com/braze-inc/braze-unity-sdk/blob/master/Assets/Plugins/Appboy/BrazePlatform.cs)     | [Dépôt GitHub](https://github.com/braze-inc/braze-unity-sdk)          | [Exemple d’application](https://github.com/braze-inc/braze-unity-sdk/tree/master/unity-samples)          |
| Unreal Engine SDK | N/A                                                                                                                                                         | [Dépôt GitHub](https://github.com/braze-inc/braze-unreal-sdk)        | [Exemple d’application](https://github.com/braze-inc/braze-unreal-sdk/tree/master/BrazeSample)        |
| .NET MAUI SDK       | N/A                                                                                                                                                         | [Dépôt GitHub](https://github.com/braze-inc/braze-xamarin-sdk)      | [Exemple d’application](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples)      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Créer un exemple d'application

{% tabs %}
{% tab android %}
### Créer "Droidboy"

Notre application de test au sein du [dépôt GitHub Android SDKBraze](https://github.com/braze-inc/braze-android-sdk "Android GitHub Repository") s'appelle Droidboy. Suivez ces instructions pour créer une copie entièrement fonctionnelle de celle-ci parallèlement à votre projet.

1. Créez un nouvel [espace de travail]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#app-group-configuration) et notez la clé d'identification de l'API Braze.<br><br>
2. Copiez votre ID d’expéditeur FCM et votre clé d’identification de l’API Braze dans les emplacements appropriés `/droidboy/res/values/braze.xml` (entre les balises des chaînes nommées `com_braze_push_fcm_sender_id` et `com_braze_api_key`, respectivement).<br><br>
3. Copiez votre clé de serveur FCM et votre ID de serveur dans les paramètres de votre espace de travail sous **Gérer les paramètres.**<br><br>
4. Pour assembler l’APK Droidboy, exécutez `./gradlew assemble` dans le répertoire SDK. Utilisez `gradlew.bat` sous Windows.<br><br>
5. Pour installer automatiquement l’APK Droidboy sur un appareil de test, exécutez `./gradlew installDebug` dans le répertoire SDK :

### Créer "Hello Braze" (Bonjour Braze)

L’application de test Hello Braze présente un cas d’utilisation minimal du SDK Braze et montre en outre comment intégrer facilement le SDK Braze dans un projet Gradle.

1. Copiez votre clé d'identification API de la page **Gérer les paramètres** dans votre fichier `braze.xml` dans le dossier `res/values`.
![]({% image_buster /assets/img_archive/hello_appboy.png %})<br><br>
2. Pour installer l’exemple d’application sur un appareil ou un émulateur, exécutez la commande suivante dans le répertoire SDK :
```
./gradlew installDebug
```
Si votre variable `ANDROID_HOME` n’est pas correctement définie ou n’a pas de dossier `local.properties` avec un dossier `sdk.dir` valide, ce plug-in va également installer le SDK de base pour vous. Consultez le [dépôt de plugins](https://github.com/JakeWharton/sdk-manager-plugin) pour plus d'informations.

Pour plus d'informations sur le système de création du SDK Android, consultez le [fichier README du référentiel GitHub](https://github.com/braze-inc/braze-android-sdk/blob/master/README.md).
{% endtab %}

{% tab swift %}
### Créer des applications de test en Swift

Suivez ces instructions pour concevoir et exécuter nos applications de test.

1. Créez un nouvel [espace de travail]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps) et notez la clé API de l'identifiant de l'app et son endpoint.
2. En fonction de votre méthode d'intégration (gestionnaire de paquets swift, CocoaPods, manuel), sélectionnez le fichier `xcodeproj` approprié à ouvrir.
3. Placez votre clé API et votre endpoint dans le champ approprié du fichier `Credentials`.
{% endtab %}
{% endtabs %}

{% alert note %}
Lors de l'assurance qualité de votre intégration SDK, utilisez le [débogueur SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) pour résoudre les problèmes sans avoir à activer l'enregistrement des données pour votre application.
{% endalert %}