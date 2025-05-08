---
nav_title: Notifications push
article_title: Notifications push pour le SDK de Cordova Braze
platform:
  - Cordova
  - iOS
  - Android
page_order: 1
page_type: reference
description: "Cet article traite de l’implémentation des notifications push sur Cordova."
channel: push
---

# Intégration de notifications Push

> Découvrez comment intégrer les notifications push pour le SDK Cordova Braze.

{% multi_lang_include cordova/prerequisites.md %}

## Fonctionnalités de base des notifications push

Par défaut, les fonctionnalités de base des notifications push sont activées dans le plug-in Cordova de Braze. Vous pouvez désactiver ces fonctionnalités en [personnalisant vos configurations XML.]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_setup/customizations/#customization-options) Pour approfondir les fonctionnalités des notifications push natives, consultez les guides sur les notifications push pour [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/) et [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/).

## Fonctionnalités étendues des notifications push

{% alert important %}
Chaque fois que vous ajoutez, supprimez ou mettez à jour vos plug-ins Cordova, Cordova remplace le Podfile dans votre projet Xcode. Cela signifie que vous devrez répéter ce processus à chaque fois que vous modifierez vos plug-ins Cordova.
{% endalert %}

### Notifications push riches

#### Étape 1 : Créer une extension de service de notification

Dans votre projet Xcode, créez une extension de service de notification. Pour obtenir une présentation complète, consultez le [tutoriel sur les notifications push riches sous iOS](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

#### Étape 2 : Ajouter une nouvelle cible

Ouvrez votre Podfile et ajoutez `BrazeNotificationService` à la cible d'extension du service de notification [que vous venez de créer](#step-1-create-a-notification-service-extension). Si `BrazeNotificationService` est déjà ajouté à une cible, retirez-le avant de continuer. Pour éviter les erreurs de symboles dupliqués, utilisez des liens statiques.

```ruby
target 'NOTIFICATION_SERVICE_EXTENSION' do
  use_frameworks! :linkage => :static
  pod 'BrazeNotificationService'
end
```

Remplacez `NOTIFICATION_SERVICE_EXTENSION` par le nom de votre extension de service de notification. Votre Podfile devrait ressembler à ce qui suit :

```ruby
target 'MyAppRichNotificationService' do
  use_frameworks! :linkage => :static
  pod 'BrazeNotificationService'
end
```

#### Étape 3 : Réinstallez vos dépendances CocoaPods

Dans le terminal, allez dans le répertoire iOS de votre projet et réinstallez vos dépendances CocoaPod.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```

### Contenu push

#### Étape 1 : Créer une extension de contenu de notification

Dans votre projet Xcode, créez une extension de contenu de notification. Pour obtenir une présentation complète, consultez le [tutoriel sur les contenus push iOS](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories/).

#### Étape 2 : Configurez votre groupe d'applications push

Dans le fichier `config.xml` de votre projet, configurez le groupe d'applications push [que vous venez de créer](#step-1-create-a-notification-content-extension).

```xml
<preference name="com.braze.ios_push_app_group" value="NOTIFICATION_CONTENT_EXTENTION" />
```

Remplacez `PUSH_APP_GROUP` par le nom de votre groupe d'applications push. Votre site `config.xml` devrait ressembler à ce qui suit :

```xml
<preference name="com.braze.ios_push_app_group" value="MyPushAppGroup" />
```

#### Étape 3 : Ajouter une nouvelle cible

Ouvrez votre Podfile et ajoutez `BrazePushStory` à la cible d'extension de contenu de notification [que vous avez créée précédemment](#step-1-create-a-notification-content-extension). Pour éviter les erreurs de symboles dupliqués, utilisez des liens statiques.

```ruby
target 'NOTIFICATION_CONTENT_EXTENSION' do
  use_frameworks! :linkage => :static
  pod 'BrazePushStory'
end
```

Remplacez `NOTIFICATION_CONTENT_EXTENSION` par le nom de votre extension de contenu de notification. Votre Podfile devrait ressembler à ce qui suit :

```ruby
target 'MyAppNotificationContentExtension' do
  use_frameworks! :linkage => :static
  pod 'BrazePushStory'
end
```

#### Étape 4 : Réinstallez vos dépendances CocoaPods

Dans le terminal, allez dans votre répertoire iOS et réinstallez vos dépendances CocoaPod.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```
