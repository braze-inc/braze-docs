{% multi_lang_include developer_guide/prerequisites/cordova.md %} Vous devrez également [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=cordova).

## Mise en place de notifications push riches

### Étape 1 : Créer une extension de service de notification

Dans votre projet Xcode, créez une extension de service de notification. Pour obtenir une présentation complète, consultez le [tutoriel sur les notifications push riches sous iOS](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).

### Étape 2 : Ajouter une nouvelle cible

Ouvrez votre Podfile et ajoutez `BrazeNotificationService` à la cible d'extension du service de notification [que vous venez de créer](#cordova_step-1-create-a-notification-service-extension). Si `BrazeNotificationService` est déjà ajouté à une cible, retirez-le avant de continuer. Pour éviter les erreurs de symboles dupliqués, utilisez des liens statiques.

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

### Étape 3 : Réinstallez vos dépendances CocoaPods

Dans le terminal, allez dans le répertoire iOS de votre projet et réinstallez vos dépendances CocoaPod.

```bash
cd PATH_TO_PROJECT/platform/ios
pod install
```
