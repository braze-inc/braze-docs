---
nav_title: Exemples d’applications
article_title: Exemples d’applications pour Android et FireOS
platform: 
  - Android
  - FireOS
page_order: 10
description: "Cet article de référence explique comment utiliser les exemples d’applications Android."

---

# Exemples d’applications

> Les SDK de Braze sont tous accompagnés d'un exemple d'application dans le référentiel pour vous faciliter la tâche. Chacune de ces applications est entièrement modulable afin que vous puissiez tester les fonctionnalités de Braze et les implémenter dans vos propres applications. 

Tester le comportement dans votre propre application par rapport au comportement attendu et aux chemins de code des exemples d’applications est un excellent moyen de déboguer les problèmes que vous pourriez rencontrer.

## Créer l’application de test Droidboy
Notre application de test au sein du [dépôt GitHub Android SDKBraze](https://github.com/braze-inc/braze-android-sdk "Android GitHub Repository") s'appelle Droidboy. Suivez ces instructions pour créer une copie entièrement fonctionnelle de celle-ci parallèlement à votre projet.

1. Créez un nouvel [espace de travail]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#app-group-configuration) et notez la clé d'identification de l'API Braze.<br><br>
2. Copiez votre ID d’expéditeur FCM et votre clé d’identification de l’API Braze dans les emplacements appropriés `/droidboy/res/values/braze.xml` (entre les balises des chaînes nommées `com_braze_push_fcm_sender_id` et `com_braze_api_key`, respectivement).<br><br>
3. Copiez votre clé de serveur FCM et votre ID de serveur dans les paramètres de votre espace de travail sous **Gérer les paramètres.**<br><br>
4. Pour assembler l’APK Droidboy, exécutez `./gradlew assemble` dans le répertoire SDK. Utilisez `gradlew.bat` sous Windows.<br><br>
5. Pour installer automatiquement l’APK Droidboy sur un appareil de test, exécutez `./gradlew installDebug` dans le répertoire SDK :

## Créer l’application de test Hello Braze
L’application de test Hello Braze présente un cas d’utilisation minimal du SDK Braze et montre en outre comment intégrer facilement le SDK Braze dans un projet Gradle.

1. Copiez votre clé d'identification API de la page **Gérer les paramètres** dans votre fichier `braze.xml` dans le dossier `res/values`.
![]({% image_buster /assets/img_archive/hello_appboy.png %})<br><br>
2. Pour installer l’exemple d’application sur un appareil ou un émulateur, exécutez la commande suivante dans le répertoire SDK :
```
./gradlew installDebug
```
Si votre variable `ANDROID_HOME` n’est pas correctement définie ou n’a pas de dossier `local.properties` avec un dossier `sdk.dir` valide, ce plug-in va également installer le SDK de base pour vous. Consultez le [dépôt de plugins](https://github.com/JakeWharton/sdk-manager-plugin) pour plus d'informations.

Pour plus d'informations sur le système de création du SDK Android, consultez le [fichier README du référentiel GitHub](https://github.com/braze-inc/braze-android-sdk/blob/master/README.md).

