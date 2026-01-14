## Contrôle du trafic sur le réseau

### Demande de politiques de traitement

Braze permet à l’utilisateur de contrôler le trafic réseau à l’aide des protocoles suivants :

{% tabs local %}
{% tab automatique %}
Par défaut, la valeur de l'enum `RequestPolicy` est fixée à `automatic`. Lorsqu'elle est définie, des requêtes immédiates au serveur sont effectuées lorsque des données orientées vers l'utilisateur sont requises pour les fonctionnalités de Braze, telles que les messages in-app.

Le SDK Braze gérera automatiquement toutes les communications du serveur, y compris :

- Suppression des données d’événements personnalisés et d’attributs sur les serveurs de Braze
- Mise à jour des cartes de contenu et des géorepérages
- Demander de nouveaux messages in-app

Pour minimiser la charge serveur, Braze effectue des purges périodiques des nouvelles données utilisateur au bout de quelques secondes.
{% endtab %}

{% tab manuel %}
Lorsque la valeur de l'enum `RequestPolicy` est `manual`, le fonctionnement est identique à celui du traitement automatique des demandes, à l'exception de ce qui suit :

- Les attributs personnalisés et les données d’événements personnalisés ne sont pas automatiquement purgés du serveur tout au long de la session utilisateur.
- Braze effectuera toujours des requêtes réseau automatiques pour les fonctionnalités internes, telles que la demande de messages in-app, la création de modèles Liquid dans les messages in-app, les géorepérages et le suivi de la localisation. Pour plus de détails, consultez la [documentation](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/api-swift.class/requestpolicy-swift.enum/manual) `Braze.Configuration.Api.RequestPolicy.manual`. Lorsque ces demandes internes sont effectuées, les attributs personnalisés stockés localement et les données d’événements personnalisés peuvent être purgés vers le serveur Braze, selon le type de demande.
{% endtab %}
{% endtabs %}

### Effacement manuel des données de l'utilisateur

Les données peuvent être transférées manuellement vers les serveurs de Braze à tout moment en utilisant la méthode suivante :

{% tabs %}
{% tab swift %}
```swift
AppDelegate.braze?.requestImmediateDataFlush()
```
{% endtab %}
{% tab OBJECTIF-C %}
```objc
[AppDelegate.braze requestImmediateDataFlush];
```
{% endtab %}
{% endtabs %}

### Définition de la politique de traitement des demandes

Ces politiques peuvent être définies au moment du démarrage de l'application, lorsque vous initialisez la configuration de Braze. Dans l'objet `configuration`, définissez l'élément [`Braze.Configuration.Api.RequestPolicy`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/api-swift.class/requestpolicy-swift.enum)) comme indiqué dans l'extrait de code suivant :

{% tabs %}
{% tab swift %}
```swift
configuration.api.requestPolicy = .automatic
```
{% endtab %}
{% tab OBJECTIF-C %}
```objc
configuration.api.requestPolicy = BRZRequestPolicyAutomatic;
```
{% endtab %}
{% endtabs %}
