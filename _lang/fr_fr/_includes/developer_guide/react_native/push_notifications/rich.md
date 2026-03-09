{% multi_lang_include developer_guide/prerequisites/react_native.md %} Il vous sera également nécessaire de [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native).

## Utilisation d'Expo pour activer les notifications push riches

Pour le SDK React native, **les notifications push riches sont disponibles par défaut pour Android**.

Pour activer les notifications push enrichies sur iOS à l'aide d'Expo, configurez la propriété `enableBrazeIosRichPush` sur `true` dans votre objet `expo.plugins` dans `app.json` :

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosRichPush": true
        }
      ]
    ]
  }
}
```

Enfin, ajoutez l'identifiant du bundle de cette extension d'application à la configuration des informations d'identification de votre projet : `<your-app-bundle-id>.BrazeExpoRichPush`. Pour plus de détails sur ce processus, reportez-vous à la section [Utiliser les extensions d'applications avec Expo Application Services]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native#reactnative_app-extensions).
