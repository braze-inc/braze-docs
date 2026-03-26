{% multi_lang_include developer_guide/prerequisites/cordova.md %} Vous devrez également [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=cordova).

## Mise en place de contenus push

### Étape 1 : Créer une extension de contenu de notification

Dans votre projet Xcode, créez une extension de contenu de notification. Pour obtenir une présentation complète, consultez le [tutoriel sur les contenus push iOS](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories/).

### Étape 2 : Configurez votre groupe d'applications push

Dans le fichier `config.xml` de votre projet, configurez le groupe d'applications push [que vous venez de créer](#cordova_step-1-create-a-notification-content-extension).

```xml
<preference name="com.braze.ios_push_app_group" value="NOTIFICATION_CONTENT_EXTENTION" />
```

Remplacez `PUSH_APP_GROUP` par le nom de votre groupe d'applications push. Votre site `config.xml` devrait ressembler à ce qui suit :

```xml
<preference name="com.braze.ios_push_app_group" value="MyPushAppGroup" />
```

### Étape 3 : Ajouter une nouvelle cible

Ouvrez votre Podfile et ajoutez `BrazePushStory` à la cible d'extension de contenu de notification [que vous avez créée précédemment](#cordova_step-1-create-a-notification-content-extension). Pour éviter les erreurs de symboles dupliqués, utilisez des liens statiques.

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

### Étape 4 : Réinstallez vos dépendances CocoaPods

Dans le terminal, allez dans votre répertoire iOS et réinstallez vos dépendances CocoaPod.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```
