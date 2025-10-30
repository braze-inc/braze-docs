### Conditions préalables

Avant de pouvoir utiliser cette méthode d'intégration, vous devez [créer un compte et un conteneur pour Google Tag Manager](https://support.google.com/tagmanager/answer/14842164).

### Étape 1 : Ouvrez la galerie de modèles d'étiquettes

Dans [Google Tag Manager](https://tagmanager.google.com/), choisissez votre espace de travail, puis sélectionnez **Modèles.** Dans la sous-fenêtre **Modèle d'étiquette**, sélectionnez **Galerie de recherche.**

![La page des tags pour un exemple d'espace de travail dans Google Tag Manager.]({% image_buster /assets/img/web-gtm/search_tag_template_gallery.png %}){: style="max-width:95%;"}

### Étape 2 : Ajouter le modèle d'étiquette d'initialisation

Dans la galerie de modèles, recherchez `braze-inc`, puis sélectionnez **Braze Initialization Tag.**

![La galerie de modèles présentant les différents modèles "Braze-inc".]({% image_buster /assets/img/web-gtm/template_gallery_results.png %}){: style="max-width:80%;"}

Sélectionnez **Ajouter à l'espace de travail** > **Ajouter.**

![La page "Braze Initialization Tag" dans Google Tag Manager.]({% image_buster /assets/img/web-gtm/add_to_workspace.png %}){: style="max-width:70%;"}

### Étape 3 : Configurer l'étiquette

Dans la section **Modèles**, sélectionnez le modèle que vous venez d'ajouter.

![La page "Templates" du Google Tag Manager présente le modèle de balise d'initialisation de Braze.]({% image_buster /assets/img/web-gtm/select_tag_template.png %}){: style="max-width:95%;"}

Sélectionnez l'icône en forme de crayon pour ouvrir le menu déroulant **Configuration des étiquettes**.

![La tuile Configuration de l'étiquette avec l'icône "crayon" affichée.]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

Saisissez les informations minimales requises :

| Champ         | Description |
| ------------- | ----------- |
| **Clé API**   | Votre [clé API Braze]({{site.baseurl}}/api/basics/#about-rest-api-keys), que vous trouverez dans le tableau de bord de Braze sous **Paramètres** > **Paramètres de l'application**. |
| **Endpoint de l’API** | L'URL de votre endpoint REST. Votre endpoint dépendra de l'URL de Braze pour [votre instance]({{site.baseurl}}/api/basics/#endpoints). |
| **Version du SDK**  | La version `MAJOR.MINOR` la plus récente du SDK Braze Web figurant dans le [journal des modifications]({{site.baseurl}}/developer_guide/changelogs/?sdktab=web). Par exemple, si la dernière version est `4.1.2`, saisissez `4.1`. Pour plus d'informations, voir [À propos de la gestion des versions du SDK]({{site.baseurl}}/developer_guide/sdk_integration/version_management/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Pour des paramètres d'initialisation supplémentaires, sélectionnez **Options d'initialisation de Braze** et choisissez les options dont vous avez besoin.

![La liste des options d'initialisation de la Braze se trouve sous "Configuration de l'étiquette".]({% image_buster /assets/img/web-gtm/braze_initialization_options.png %}){: style="max-width:65%;"}

### Étape 4 : Réglé sur Déclencheur sur *toutes les pages*

L'étiquette d'initialisation doit être exécutée sur toutes les pages de votre site. Cela vous permet d'utiliser les méthodes du SDK de Braze et d'enregistrer les analyses/analytiques du web push.

### Étape 5 : Vérifiez votre intégration

Vous pouvez vérifier votre intégration en utilisant l'une des options suivantes :

- **Option 1 :** Grâce à l' [outil de débogage](https://support.google.com/tagmanager/answer/6107056?hl=en) de Google Tag Manager, vous pouvez vérifier si l'étiquette d'initialisation Braze se déclenche correctement sur vos pages ou événements configurés.
- **Option 2 :** Vérifiez si des requêtes réseau sont adressées à Braze depuis votre page web. En outre, la bibliothèque globale `window.braze` doit maintenant être définie.
