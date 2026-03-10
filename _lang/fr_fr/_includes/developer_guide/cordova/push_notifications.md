{% multi_lang_include developer_guide/prerequisites/cordova.md %} Une fois l'intégration SDK effectuée, la fonctionnalité de notification push de base est activée par défaut. Pour utiliser [les notifications push riches]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=cordova) et [le contenu push]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=cordova), il est nécessaire de les configurer individuellement. Pour utiliser les messages push iOS, il est également nécessaire de télécharger un certificat push valide.

{% alert warning %}
Chaque fois que vous ajoutez, supprimez ou mettez à jour vos plugins cordova, cordova écrasera le fichier Podfile dans le projet Xcode de votre application iOS. Cela signifie que vous devrez reconfigurer ces fonctionnalités à chaque fois que vous modifiez vos plugins cordova.
{% endalert %}

## Activation de la création de liens profonds push

Par défaut, le SDK Braze Cordova ne gère pas automatiquement les liens profonds provenant des notifications push. Pour activer les liens profonds push, veuillez suivre les étapes de configuration décrites dans [la section Création de liens profonds]({{site.baseurl}}/developer_guide/cordova/deep_linking/).
Pour plus d'informations sur ces options et d'autres options de configuration push, veuillez consulter [la section Configurations facultatives]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional).

## Désactiver les notifications push de base (iOS uniquement)

Une fois que vous avez effectué l'intégration du SDK Braze Cordova pour iOS, les fonctionnalités de base des notifications push sont activées par défaut. Pour désactiver cette fonctionnalité dans votre application iOS, veuillez ajouter ce qui suit à votre`config.xml`fichier. Pour plus d'informations, veuillez consulter [la section Configurations optionnelles]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional).

```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
