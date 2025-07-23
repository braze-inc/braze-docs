## Utilisation du gestionnaire Google Tag Manager {#initialization-tag}

### Étape 1 : Configurer les notifications push (facultatif)

Si vous souhaitez envoyer des messages push par l'intermédiaire du Google Tag Manager, suivez d'abord les tags d'[intégration des messages push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web):
1. Configurez le service de traitement de votre site, en le plaçant dans le répertoire racine de votre site.
2. Configurez l'enregistrement du navigateur - Une fois le service de traitement configuré, vous devez définir la méthode `braze.requestPushPermission()` soit de manière native dans leur application, soit par le biais d'une balise HTML personnalisée (via le tableau de bord de GTM). Vous devrez également vous assurer que la balise est activée après l'initialisation du SDK.

### Étape 2 : Sélectionner la balise d’initialisation

Recherchez Braze dans la galerie de modèles de la communauté, puis sélectionnez la **balise d’initialisation de Braze**.

![Une boîte de dialogue affichant les paramètres de configuration de la balise d’initialisation de Braze. Les paramètres inclus sont "type d'étiquette", "clé API", "endpoint API", "version SDK", "external user ID" et "Safari web push ID".]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

### Étape 3 : Configurer les paramètres

Saisissez votre clé d’identification de l’API Braze et l’endpoint du SDK, que vous trouverez dans la page **Gérer les paramètres** de votre tableau de bord. Entrez la version `major.minor` la plus récente du SDK Web. Par exemple, si la dernière version est `4.1.2`, saisissez `4.1`. Vous pouvez consulter la liste des versions du SDK dans notre [journal des modifications](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md).

### Étape 4 : Choisir les options d’initialisation

Choisissez parmi l'ensemble d'options d'initialisation supplémentaires décrites dans le guide [Initial setup]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#step-2-initialize-braze).

### Étape 5 : Vérifier et réaliser la QA

Une fois que vous avez déployé cette balise, il existe deux manières de vérifier que l’intégration est correcte :

1. En utilisant l' [outil de débogage](https://support.google.com/tagmanager/answer/6107056?hl=en) de Google Tag Manager, vous devriez voir que l'étiquette d'initialisation Braze a été déclenchée sur vos pages ou événements configurés.
2. Vous devriez voir les demandes réseau faites à Braze et la bibliothèque globale `window.braze` devrait maintenant être définie sur votre page Web.
