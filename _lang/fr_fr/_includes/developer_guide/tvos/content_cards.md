## Conditions préalables

Avant de pouvoir utiliser les cartes de contenu, vous devez intégrer le [SDK Swift de Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift) dans votre application. Vous devrez ensuite suivre les étapes de configuration de votre application tvOS.

{% alert important %}
Gardez à l'esprit que vous devrez implémenter votre propre interface utilisateur personnalisée, car les cartes de contenu sont prises en charge par une interface utilisateur Headless à l'aide du SDK Swift, qui n'inclut pas d'interface utilisateur ou de vues par défaut pour tvOS.
{% endalert %}

## Configurer votre application tvOS

### Étape 1 : Créer une nouvelle application iOS

Dans Braze, sélectionnez **Paramètres** > **Paramètres des applications**, puis **Ajouter une application**. Saisissez un nom pour votre application tvOS, sélectionnez **iOS**, _et non tvOS_, puis sélectionnez **Ajouter une application**.

![ALT_TEXT.]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
Si vous cochez la case **tvOS**, vous ne pourrez pas personnaliser les cartes de contenu pour tvOS.
{% endalert %}

### Étape 2 : Obtenir la clé API de votre application

Dans les paramètres de votre application, sélectionnez votre nouvelle appli tvOS, puis prenez note de la clé API de votre appli. Vous utiliserez cette clé pour configurer votre application dans Xcode.

![ALT_TEXT]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### Étape 3 : Intégrer BrazeKit

Utilisez la clé API de votre application pour intégrer le [SDK Braze Swift](https://github.com/braze-inc/braze-swift-sdk) à votre projet tvOS dans Xcode. Il vous suffit d'intégrer BrazeKit à partir du SDK Swift de Braze.

### Étape 4 : Créez votre interface utilisateur personnalisée

Braze ne proposant pas d'interface utilisateur par défaut pour les cartes de contenu sur tvOS, vous devrez la personnaliser vous-même. Pour une description complète, consultez notre tutoriel étape par étape : [Personnalisation des cartes de contenu pour tvOS.](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization/) Pour obtenir un exemple de projet, consultez les [exemples du SDK Swift de Braze](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#contentcards-custom-ui).
