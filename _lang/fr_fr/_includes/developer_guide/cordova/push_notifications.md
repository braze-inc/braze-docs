{% multi_lang_include developer_guide/prerequisites/cordova.md %} Une fois que vous avez intégré le SDK, la fonctionnalité de base des notifications push est activée par défaut. Pour utiliser les [notifications push riches]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=cordova) et les [contenus push]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=cordova), vous devrez les configurer individuellement. Pour utiliser les messages push d'iOS, vous devez également télécharger un certificat push valide.

{% alert warning %}
Chaque fois que vous ajoutez, supprimez ou mettez à jour vos plugins Cordova, Cordova écrase le Podfile dans le projet Xcode de votre application iOS. Cela signifie que vous devrez à nouveau configurer ces fonctionnalités à chaque fois que vous modifierez vos plugins Cordova.
{% endalert %}

## Désactivation des notifications push de base (iOS uniquement).

Après avoir intégré le SDK Braze Cordova pour iOS, la fonctionnalité de base des notifications push est activée par défaut. Pour désactiver cette fonctionnalité dans votre application iOS, ajoutez ce qui suit à votre fichier `config.xml`. Pour plus d'informations, voir [Configurations optionnelles]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional).

```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
