---
nav_title: Crowdin
article_title: Crowdin
description: "Utilisez l'intégration Crowdin pour traduire vos campagnes, vos expériences Canvas, vos modèles d'e-mail et vos blocs de contenu grâce à la mémoire de traduction, aux glossaires et à la traduction automatique."
alias: /partners/crowdin/
page_type: partner
search_tag: Partner

---

# Crowdin

> [Crowdin](https://crowdin.com/) est une plateforme de gestion de la localisation basée sur l'intelligence artificielle qui aide les équipes à automatiser la traduction de leurs logiciels, applications et contenus marketing.

Connectez Crowdin à Braze pour gérer les traductions de vos campagnes et expériences Canvas. La synchronisation automatisée fonctionne avec la traduction automatique, la mémoire de traduction et les glossaires, garantissant ainsi la cohérence entre les flux de travail humains et automatisés.

_Cette intégration est maintenue par Crowdin._

## À propos de l'intégration

Crowdin propose deux applications pour Braze : [Braze Campaigns & Canvas](https://store.crowdin.com/braze-content-translation) et [Braze Email Templates](https://store.crowdin.com/braze-app). Choisissez celle qui correspond aux fonctionnalités Braze que vous localisez. Le tableau suivant les compare.

### Choisir la bonne application Crowdin

| Canal ou fonctionnalité | Braze Campaigns & Canvas | Braze Email Templates |
| --- | --- | --- |
| **Campagnes** | ✅ Pris en charge | ❌ Non pris en charge |
| **Étapes du canvas** | ✅ Pris en charge | ❌ Non pris en charge |
| **Modèles d'e-mail** | ❌ Non pris en charge | ✅ Pris en charge |
| **Blocs de contenu** | ❌ Non pris en charge | ✅ Pris en charge |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Conditions préalables

| Condition | Description |
| --- | --- |
| **Compte Crowdin** | Un [compte Crowdin.com](https://accounts.crowdin.com/register) ou un [compte Crowdin Enterprise](https://accounts.crowdin.com/workspace/create) est requis. |
| **Projet Crowdin** | Avant de connecter Braze, [créez un projet de traduction](https://support.crowdin.com/creating-project/) dans Crowdin ou Crowdin Enterprise. |
| **Clé API REST de Braze** | Une clé API REST de Braze avec les autorisations pour les campagnes, Canvas, les blocs de contenu, les attributs personnalisés, les e-mails et les modèles. |
| **Endpoint REST de Braze** | L'URL spécifique de votre endpoint REST Braze (par exemple, `https://rest.iad-03.braze.com`). |
| **Paramètres multilingues de Braze** | Les locales doivent être configurées dans votre tableau de bord de Braze sous **Paramètres** > **Paramètres de localisation**. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Intégration Braze Campaigns & Canvas

Si vous localisez du contenu dans des messages en production, utilisez l'[application Braze Campaigns & Canvas](https://store.crowdin.com/braze-content-translation) pour synchroniser les chaînes de caractères traduisibles de vos brouillons de campagnes et de Canvas avec le support multilingue de Braze.

Pour un tutoriel vidéo, consultez [Braze Campaigns & Canvas integration](https://youtu.be/ahG1ET4VRKA).

### Étape 1 : Configurer les paramètres multilingues dans Braze

Avant de connecter Crowdin, ajoutez vos langues cibles dans Braze.

1. Dans Braze, accédez à **Paramètres** > **Paramètres de localisation**.
2. Ajoutez les langues que vous prévoyez de prendre en charge.

![Page des locales Braze sous Paramètres, affichant les noms de locale, les clés de locale et l'option Ajouter une locale.]({% image_buster /assets/img/crowdin/braze_locales.png %})

{: start="3"}
3. Notez chaque **clé de locale** (par exemple, `en-US`, `fr-FR`, `es-ES`). Vous utiliserez ces valeurs lors du mappage des langues dans Crowdin.

### Étape 2 : Configurer le projet Braze dans Crowdin

1. Dans votre compte Crowdin Enterprise ou Crowdin.com, accédez au **Store** dans le menu de gauche.
2. Recherchez **Braze Campaigns & Canvas**, puis sélectionnez **Installer**.

![Crowdin Store avec Braze Campaigns & Canvas sélectionné et le bouton Installer mis en évidence.]({% image_buster /assets/img/crowdin/crowdin_store_campaigns_canvas.png %})

{: start="3"}
3. Sélectionnez le ou les projets dans lesquels vous souhaitez utiliser cette intégration.
4. Pour ouvrir l'intégration, accédez à **Intégrations** > **Braze Campaigns & Canvas** dans votre projet.

#### Connecter Braze à Crowdin

Autorisez la connexion avec vos identifiants API Braze :

![Formulaire de connexion Crowdin Braze Campaigns & Canvas avec la clé API REST, l'endpoint REST et le bouton Se connecter avec Braze Campaigns & Canvas.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_login.png %})

- **Clé API REST de Braze :** Créez-la dans Braze sous **Paramètres** > **API et identifiants** > **Clés API**. Accordez les autorisations nécessaires à cette intégration (campagnes, Canvas, blocs de contenu et attributs personnalisés).
- **Endpoint REST de Braze :** Saisissez l'URL de votre instance Braze (par exemple, `https://rest.iad-03.braze.com`). Pour en savoir plus, consultez [Endpoints de l'API REST]({{site.baseurl}}/api/basics/#endpoints).

![Page des clés API REST de Braze avec le bouton Créer une clé API et le contrôle de copie de l'endpoint REST.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

Sélectionnez **Se connecter avec Braze Campaigns & Canvas**.

### Étape 3 : Configurer le mappage des langues dans Crowdin

Après avoir connecté votre compte, associez chaque langue de votre projet Crowdin à la locale Braze correspondante.

1. Dans le tableau de bord de l'intégration **Braze Campaigns & Canvas**, sélectionnez l'icône d'engrenage **Paramètres** dans le coin supérieur droit.

![Écran de l'intégration Braze Campaigns & Canvas avec Paramètres dans la barre d'actions supérieure.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_settings.png %})

{: start="2"}
2. Ouvrez l'onglet **Paramètres généraux**.
3. Saisissez les clés de locale. Crowdin affiche les langues de votre projet (par exemple, français, italien). Dans chaque champ, entrez la **clé de locale Braze** correspondante.
   - Par exemple, si Braze utilise `it` pour l'italien, saisissez `it` à côté d'italien dans Crowdin.
   - Chaque entrée doit correspondre exactement à la **clé de locale** définie dans les **Paramètres de localisation** de Braze.

![Fenêtre modale des paramètres sur l'onglet Paramètres généraux, affichant les champs de filtre de fichiers et les lignes de mappage des langues (par exemple, français associé à fr).]({% image_buster /assets/img/crowdin/crowdin_language_mapping_settings.png %})

{: start="4"}
4. Sélectionnez **Enregistrer** pour confirmer le mappage.

### Étape 4 : Ajouter des balises de traduction à votre message Braze

Crowdin lit les mêmes **balises de traduction** Liquid que Braze utilise pour les messages multilingues. Ajoutez {% raw %}`{% translation your_id_here %}` et `{% endtranslation %}`{% endraw %} autour de chaque texte, URL d'image ou URL de lien que vous souhaitez traduire. Chaque bloc nécessite un `id` unique (par exemple, `greeting` ou `welcome_header`).

**Exemple :**

{% raw %}`{% translation greeting %}Hello!{% endtranslation %}`{% endraw %}

Pour le HTML, le Liquid dans les liens et les autres cas de figure, suivez les mêmes règles que dans [Traduire les locales]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales) (par exemple, placez les balises autour des segments les plus petits possible et n'encadrez que les parties spécifiques à la langue des URL lors de la localisation des liens).

Enregistrez votre message Braze en tant que **brouillon** avant que Crowdin puisse détecter et récupérer le contenu.

### Étape 5 : Gérer les traductions dans Crowdin

L'écran de l'intégration comporte deux volets :

- **Volet droit (Braze) :** Vos campagnes et Canvas.
- **Volet gauche (Crowdin) :** Le contenu déjà synchronisé pour la traduction.

![Panneaux Crowdin et Braze Campaigns & Canvas avec des dossiers pour les campagnes et les locales, Synchroniser avec Braze et Synchroniser avec Crowdin.]({% image_buster /assets/img/crowdin/crowdin_campaigns_canvas_sync_panels.png %})

#### Synchroniser le contenu

1. Dans le volet **Braze (droite)**, cochez la case de la campagne ou du Canvas à traduire.
2. Sélectionnez **Synchroniser avec Crowdin**.
3. Une fois la synchronisation terminée, le fichier apparaît dans le volet **Crowdin (gauche)**. Les traducteurs peuvent alors ouvrir les chaînes de caractères dans l'éditeur Crowdin.

#### Renvoyer les traductions vers Braze

1. Lorsque les traductions sont terminées à 100 % dans Crowdin, retournez dans l'onglet **Intégrations**.
2. Sélectionnez le contenu terminé dans le volet **Crowdin (gauche)**.
3. Sélectionnez **Synchroniser avec Braze**. Les chaînes de caractères traduites sont alors envoyées dans les variantes linguistiques correspondantes de votre campagne Braze.

### Étape 6 : Prévisualiser le message en tant qu'utilisateur multilingue dans Braze

Pour vérifier l'intégration :

1. Ouvrez votre campagne dans le **compositeur de messages Braze**.
2. Accédez à l'onglet **Test**.
3. Sélectionnez **Prévisualiser le message en tant qu'utilisateur**.
4. Recherchez un profil utilisateur dont l'attribut `language` correspond à l'une de vos locales traduites.
5. Vérifiez que le contenu passe de la langue source à la version traduite.

## Intégration Braze Email Templates

Si vous localisez les e-mails au niveau du modèle, utilisez l'[application Braze Email Templates](https://store.crowdin.com/braze-app) pour synchroniser le HTML depuis votre bibliothèque multimédia Braze.

Pour un tutoriel vidéo, consultez [Braze Email Templates integration](https://youtu.be/g0YMKW3jEjk).

### Étape 1 : Installer l'application

1. Dans votre projet Crowdin, accédez à l'onglet **Store**.
2. Recherchez **Braze Email Templates** et sélectionnez **Installer**.

![Crowdin Store avec Braze Email Templates sélectionné et le bouton Installer mis en évidence.]({% image_buster /assets/img/crowdin/crowdin_store_email_templates.png %})

{: start="3"}
3. Sélectionnez le ou les projets dans lesquels vous souhaitez utiliser cette intégration.
4. Pour ouvrir l'intégration, accédez à **Intégrations** > **Braze Email Templates** dans votre projet.

### Étape 2 : Se connecter à Braze

Autorisez la connexion avec vos identifiants API Braze :

![Formulaire de connexion Crowdin Braze Email Templates avec la clé API REST, l'endpoint REST et le bouton Se connecter avec Braze Email Templates.]({% image_buster /assets/img/crowdin/crowdin_email_templates_login.png %}){: style="max-width:85%;"}

1. **Clé API REST de Braze :** Accordez les autorisations `templates.email` et `content_blocks` (lecture et écriture). Créez la clé dans Braze sous **Paramètres** > **API et identifiants** > **Clés API**.

![Page des clés API REST de Braze avec le bouton Créer une clé API et le contrôle de copie de l'endpoint REST.]({% image_buster /assets/img/crowdin/braze_rest_api_keys.png %})

{: start="2"}
2. Pour l'**endpoint REST de Braze**, utilisez l'URL spécifique à votre instance (par exemple, `https://rest.iad-03.braze.com`).
3. Sélectionnez **Se connecter avec Braze Email Templates**.

### Étape 3 : Synchroniser le contenu pour la traduction

L'écran de l'intégration affiche votre bibliothèque Braze :

- **Volet droit (Braze) :** Les **modèles d'e-mail** et les **blocs de contenu** que vous pouvez synchroniser.
- **Volet gauche (Crowdin) :** Le contenu en cours de traduction.

1. Dans le volet **Braze (droite)**, cochez la case à côté des modèles ou blocs que vous souhaitez localiser.
2. Sélectionnez **Synchroniser avec Crowdin**.
3. Crowdin récupère le code source HTML. Les traducteurs travaillent dans l'éditeur Crowdin avec un **aperçu WYSIWYG en direct** pour que la mise en page reste intacte.

![Onglet Aperçu de l'éditeur Crowdin affichant le HTML d'e-mail localisé et les chaînes de caractères traduisibles.]({% image_buster /assets/img/crowdin/crowdin_editor_wysiwyg_preview.png %}){: style="max-width:85%;"}

### Étape 4 : Livrer les modèles traduits

Lorsque les traductions atteignent 100 % :

1. Sélectionnez les fichiers terminés dans le volet **Crowdin (gauche)**.
2. Sélectionnez **Synchroniser avec Braze**.
3. Crowdin crée automatiquement des versions localisées de ces ressources dans votre bibliothèque multimédia Braze (par exemple, `Template_Name_fr`).

![Panneaux Crowdin et Braze Email Templates listant les modèles d'e-mail et les blocs de contenu, avec Synchroniser avec Braze et Synchroniser avec Crowdin.]({% image_buster /assets/img/crowdin/crowdin_email_templates_sync_panels.png %})