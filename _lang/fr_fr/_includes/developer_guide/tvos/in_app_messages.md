{% alert important %}
Gardez à l'esprit que vous devrez implémenter votre propre interface utilisateur personnalisée, étant donné que l’envoi de messages in-app est pris en charge par une interface utilisateur Headless à l'aide du SDK Swift, qui n'inclut pas d'interface utilisateur ou de vues par défaut pour tvOS.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/swift.md %}

## Activation des messages in-app

### Étape 1 : Créer une nouvelle application iOS

Dans Braze, sélectionnez **Paramètres** > **Paramètres des applications**, puis **Ajouter une application**. Saisissez un nom pour votre application tvOS, sélectionnez **iOS**, _et non tvOS_, puis sélectionnez **Ajouter une application**.

![ALT_TEXT.]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
Si vous cochez la case **tvOS**, vous ne pourrez pas personnaliser les messages in-app pour tvOS.
{% endalert %}

### Étape 2 : Obtenir la clé API de votre application

Dans les paramètres de votre application, sélectionnez votre nouvelle appli tvOS, puis prenez note de la clé API de votre appli. Vous utiliserez cette clé pour configurer votre application dans Xcode.

![ALT_TEXT]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### Étape 3 : Intégrer BrazeKit

Utilisez la clé API de votre application pour intégrer le [SDK Braze Swift](https://github.com/braze-inc/braze-swift-sdk) à votre projet tvOS dans Xcode. Il vous suffit d'intégrer BrazeKit à partir du SDK Swift de Braze.

### Étape 4 : Créez votre interface utilisateur personnalisée

Braze ne proposant pas d'interface utilisateur par défaut pour les messages in-app sur tvOS, vous devrez la personnaliser vous-même. Pour une description complète, consultez notre tutoriel étape par étape : [Personnalisation des messages in-app pour tvOS.](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization) Pour obtenir un exemple de projet, consultez les [exemples du SDK Swift de Braze](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui).
