{% multi_lang_include developer_guide/prerequisites/swift.md %} Vous devrez également activer les messages in-app.

## Types de messages

{% tabs %}
{% multi_lang_include developer_guide/_shared/in_app_messages/message_types/swift.md %}
{% endtabs %}

## Activation des messages in-app

### Étape 1 : Créez une implémentation de `BrazeInAppMessagePresenter`

Pour permettre à Braze d'afficher des messages in-app, créez une implémentation du protocole `BrazeInAppMessagePresenter` et attribuez-la à l'option `inAppMessagePresenter` de votre instance Braze. Vous pouvez également utiliser le présentateur par défaut de Braze UI en instanciant un objet `BrazeInAppMessageUI`.

Notez que vous devrez importer la bibliothèque `BrazeUI` pour accéder à la classe `BrazeInAppMessageUI`.

{% tabs %}
{% tab swift %}

```swift
AppDelegate.braze?.inAppMessagePresenter = BrazeInAppMessageUI()
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
AppDelegate.braze.inAppMessagePresenter = [[BrazeInAppMessageUI alloc] init];
```
{% endtab %}
{% endtabs %}

### Étape 2 : Manipuler aucun déclencheur correspondant

Mettre en œuvre [`BrazeDelegate.(_:noMatchingTriggerForEvent)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazedelegate/braze(_:nomatchingtriggerforevent:)-8rt7y/) dans la classe `BrazeDelegate` concernée. Lorsque Braze ne parvient pas à trouver un déclencheur correspondant à un événement particulier, il appelle automatiquement cette méthode.
