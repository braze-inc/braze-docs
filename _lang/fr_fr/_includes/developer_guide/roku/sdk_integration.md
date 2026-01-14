## Intégration du SDK Roku

### Étape 1 : Ajouter des fichiers

Les fichiers du SDK Braze sont disponibles dans le répertoire `sdk_files` du [référentiel SDK Roku de Braze](https://github.com/braze-inc/braze-roku-sdk).

1. Ajouter `BrazeSDK.brs` à votre application dans le répertoire `source`.
2. Ajouter `BrazeTask.brs` et `BrazeTask.xml` à votre application dans le répertoire `components`.

### Étape 2 : Ajouter des références

Ajouter une référence à `BrazeSDK.brs` dans votre scène principale, en utilisant l’élément `script` :

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

### Étape 3 : Configurer

Dans `main.brs`, définissez la configuration Braze sur le nœud global :

```brightscript
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = {YOUR_API_KEY}
' example endpoint: "https://sdk.iad-01.braze.com/"
config[config_fields.ENDPOINT] = {YOUR_ENDPOINT}
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

Vous trouverez votre [endpoint SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) et votre clé API dans le tableau de bord de Braze.

### Étape 4 : Initialiser Braze

Initialiser l’instance Braze :

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Configurations optionnelles

### Journalisation

Pour déboguer votre intégration Braze, vous pouvez afficher la console de débogage Roku pour les journaux Braze. Pour en savoir plus, reportez-vous au [Code de débogage](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md) des développeurs Roku.
