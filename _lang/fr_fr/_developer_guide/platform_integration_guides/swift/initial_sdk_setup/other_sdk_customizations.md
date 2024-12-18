---
nav_title: Autres personnalisations du SDK
article_title: Autres personnalisations du SDK pour Swift
platform: Swift
description: "Ce document présente des étapes supplémentaires pour configurer le SDK Braze Swift."
page_order: 3

---

# Autres personnalisations du SDK pour Swift

> Le SDK Swift de Braze peut être configuré en modifiant les propriétés des membres de l'objet `Braze.Configuration` attaché à votre instance de Braze. Notez que la configuration ne peut être effectuée qu'avant l'initialisation de l'instance de Braze avec `Braze(configuration:)`.

Pour obtenir une liste complète des configurations disponibles, reportez-vous à la [documentation de la classe Braze.Configuration](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class).

## Niveau de journalisation de Braze

Le niveau de journalisation par défaut pour le SDK Braze Swift est `.error` dans le tableau suivant. Ce niveau est le niveau le plus minimal au-dessus d'une journalisation totalement désactivée.

Consultez la liste suivante des niveaux de journalisation disponibles :

| Swift       | Objectif-C              | Description                                                       |
|-------------|--------------------------|-------------------------------------------------------------------|
| `.debug`    | `BRZLoggerLevelDebug`    | Enregistrer les informations de débogage + `.info` + `.error`                    |
| `.info`     | `BRZLoggerLevelInfo`     | Enregistrer des informations générales sur le SDK (changements au niveau des utilisateurs, etc.) + `.error`. |
| `.error`    | `BRZLoggerLevelError`    | Erreurs de journalisation.                                                       |
| `.disabled` | `BRZLoggerLevelDisabled` | Aucun enregistrement n'a lieu.                                                |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Réglage du niveau de journalisation

Le niveau de journalisation peut être attribué au moment de l'exécution de votre objet `Braze.Configuration`:

{% tabs %}
{% tab swift %}

```swift
let configuration = Braze.Configuration(
  apiKey: "<BRAZE_API_KEY>",
  endpoint: "<BRAZE_ENDPOINT>"
)
// Enable logging of general SDK information (such as user changes, etc.)
configuration.logger.level = .info
let braze = Braze(configuration: configuration)
```

{% endtab %}
{% tab OBJECTIF-C %}

```objc
BRZConfiguration *configuration = [[BRZConfiguration alloc] initWithApiKey:self.APIKey
                                                                  endpoint:self.apiEndpoint];
// Enable logging of general SDK information (such as user changes, etc.)
[configuration.logger setLevel:BRZLoggerLevelInfo];
Braze *braze = [[Braze alloc] initWithConfiguration:configuration];
```

{% endtab %}
{% endtabs %}

Pour savoir comment utiliser pleinement l’enregistreur Braze, reportez-vous à la [documentation de la classe Logger](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/logger-swift.class).

