{% multi_lang_include developer_guide/prerequisites/react_native.md %} Vous devrez également [configurer les notifications push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native).

## Permettre les contenus push

Pour le SDK React Native, les **contenus push sont disponibles par défaut pour Android**.

Pour activer les contenus push sur iOS à l'aide d'Expo, assurez-vous qu'un groupe d'applications est défini pour votre application. Pour plus d'informations, voir [Ajouter un groupe d'applications]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/push_story/#adding-an-app-group).

Ensuite, configurez la propriété `enableBrazeIosPushStories` sur `true` et attribuez votre ID de groupe d'applications à `iosPushStoryAppGroup` dans votre objet `expo.plugins` dans `app.json` :

```json
{
  "expo": {
    "plugins": [
      [
        "@braze/expo-plugin",
        {
          ...
          "enableBrazeIosPushStories": true,
          "iosPushStoryAppGroup": "group.com.company.myApp.PushStories"
        }
      ]
    ]
  }
}
```

Enfin, ajoutez l'identifiant du bundle de cette extension d'application à la configuration des informations d'identification de votre projet : `<your-app-bundle-id>.BrazeExpoPushStories`. Pour plus de détails sur ce processus, reportez-vous à la section [Utiliser les extensions d'applications avec Expo Application Services]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native#reactnative_app-extensions).

{% alert warning %}
Si vous utilisez les contenus push avec Expo Application Services, assurez-vous d'utiliser l’indicateur `EXPO_NO_CAPABILITY_SYNC=1` lors de l'exécution de `eas build`. Il existe un problème connu dans la ligne de commande qui supprime la capacité des groupes d'applications du profil de provisionnement de votre extension.
{% endalert %}
