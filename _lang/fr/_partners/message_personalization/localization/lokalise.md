---
nav_title: Lokalise
article_title: Lokalise
description: "Cet article présente le partenariat entre Braze et Lokalise, un service de gestion des traductions pour les équipes agiles."
alias: /partners/lokalise/
page_type: partner
search_tag: Partenaire

---

# Lokalise

> [Lokalise](https://lokalise.com) est un service de gestion des traductions pour les équipes agiles.

L’intégration Braze et Lokalise exploite le contenu connecté pour vous permettre d’insérer facilement du contenu traduit dans vos campagnes Braze en fonction des paramètres de langue de l’utilisateur.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Lokalise | Un compte Lokalise est requis pour profiter de ce partenariat. |
| Projet de traduction Lokalise | Un projet de traduction Lokalise doit être créé avant de mettre en place cette intégration. |
{: .reset-td-br-1 .reset-td-br-2}

### Créer un nouveau projet Lokalise

Pour créer un nouveau projet de traduction, connectez-vous à Lokalise et sélectionnez **New Project (Nouveau projet)**. Ensuite, nommez votre projet, choisissez une **Base Language** (langue source) (la langue à partir de laquelle vous allez traduire), ajoutez une ou plusieurs **Target Languages (langues cibles)** et choisissez le type de projet **Software Localization (Localisation de logiciels)**. Une fois que vous êtes prêt, cliquez sur **Proceed (Continuer)**.

## Intégration

Dans Lokalise, vous allez créer une clé de traduction pour chacune des variables du Contenu connecté que vous définissez dans Braze. Une fois les traductions prêtes, vous pouvez générer un fichier JSON par langue et le publier sur les URL qui serviront votre contenu connecté.

### Étape 1 : Configuration les langues des utilisateurs

Si vous ne l'avez pas encore fait, ouvrez le tableau de bord de Braze et allez dans **Users > User import (Utilisateurs > Importation d'utilisateurs)**. Vous pouvez importer vos utilisateurs ici. Lorsque vous préparez un fichier CSV pour importation, veillez à inclure une colonne de langue avec les langues des utilisateurs. Ce champ de langue sera utilisé ultérieurement lors de l'affichage des traductions. 

{% alert important %}
Les codes linguistiques utilisés doivent correspondre à la fois à Braze et à Lokalise.
{% endalert %}
### Étape 2 : Préparer vos traductions sur Lokalise

Ensuite, pour préparer vos traductions sur Lokalise, vous devrez créer manuellement les clés de traduction avec le même nom que vous utilisez sur les variables de Contenu connecté Braze. 

En guise d’exemple, créons une clé de traduction simple, `description` :
1. Ouvrez votre projet Lokalise, cliquez sur **Add Key (Ajouter une clé)**, entrez "description" dans le champ **Key (Clé)**.
2. Saisissez "Description de la démo" dans le champ **Base Language Value (Valeur de la langue source)**.
3. Ajoutez "Web" dans la liste déroulante **Platforms (plateformes)**. 
4. Une fois que vous êtes prêt, cliquez sur **Save (Enregistrer)**.

![][1]{: style="max-width:60%"}

Votre clé de traduction devrait apparaître dans l'éditeur de projet :

![][2]{: style="max-width:90%"}

#### Problèmes connus

- Vos clés doivent être affectées à la plateforme **Web**.
- Évitez d'utiliser des clés qui contiennent des points (`.`) ou la chaîne de caractères `_on`. Par exemple, utilisez `this_is_the_key`, au lieu de `this.is.the.key`, et utilisez `join_us_instagram` au lieu de `join_us_on_instagram`.

### Étape 3 : Configuration de l'application Braze dans Lokalise

Ouvrez votre projet Lokalise, et cliquez sur **Apps**. Ici, cherchez et installez l'application Braze. Vous verrez apparaître l'écran suivant :

![Configuration de Braze sur Lokalise listant l'ID du projet et l'URL des fichiers de traduction.][3]

Dans **Translation File URL** (URL du fichier de traduction), Lokalise publie un fichier JSON contenant toutes les traductions de vos clés dans le projet. Vous obtiendrez autant d'URL de fichiers de traduction que de langues cibles dans votre projet. C'est pourquoi les URL des fichiers de traduction résultants comportent deux parties :

1. La première partie de l’adresse URL est commune à toutes les langues.
2. Le nom du fichier JSON à la fin de l'URL est basé sur le code de la langue.

L'URL du fichier de traduction est l'URL dont vous aurez besoin lors de la configuration d'une campagne Braze. Vous pouvez mettre à jour le contenu du fichier JSON en cliquant sur **Refresh (Rafraîchir)**. Notez que l'URL restera la même et que vous n'aurez pas besoin de modifier votre appel au Contenu connecté dans Braze.

### Test de l’URL

Pour tester cette URL, copiez-la et remplacez {% raw %}`{{${language}}}`{% endraw %} par un code de langue (par exemple, `en`) et ouvrez cette URL dans votre navigateur. Vous verrez un fichier JSON avec vos clés et traductions :

![][4]

### Étape 4 : Utilisation des traductions dans la campagne Braze

#### Insérer un appel de Contenu connecté

Lorsque vous êtes prêt, retournez dans Braze et ouvrez une campagne existante ou créez-en une nouvelle. Pour cet exemple, nous allons créer une nouvelle campagne de courrier électronique avec un contenu type. Cliquez sur **Edit Email Body (Modifier le corps de l'e-mail)**.

Pour insérer vos traductions, vous devez ajouter la requête de Contenu connecté dans le HTML, soit en haut du document, soit juste avant le premier endroit où une traduction est nécessaire. Cela peut être fait en insérant le balisage suivant :

{% raw %}
`{% connected_content https://exports.live.lokalise.cloud/braze/123abc/456xyz/{{${language}}}.json :save translations %}`
{% endraw %}

Remplacez l'URL `https://exports.live.lokalise.cloud/...` par l'URL du fichier de traduction récupéré à l'étape précédente.

{% raw %}

- `{{${language}}}` signifie « insérer la langue de l’utilisateur à cet endroit ». Sinon, vous pouvez forcer votre code de langue, par exemple, `en.json`.
  - Pour vous assurer que le bon fichier JSON traduit est récupéré pour chaque utilisateur, vous devez placer soit l’attribut de profil `{{${language}}}`, soit un autre attribut personnalisé similaire contenant la langue de l’utilisateur, à la fin de l’URL des fichiers de traduction (p. ex. `/{{${language}}}.json`). Les valeurs contenues dans ces attributs doivent correspondre au préfixe de chaque fichier JSON traduit. Cela garantira que le bon fichier de traduction est retourné pour chaque utilisateur.
- `:save translations` enregistrera le contenu JSON sous les traductions disponibles.

#### Afficher des traductions

Maintenant, utilisez les variables de traduction pour afficher les traductions souhaitées en fonction de leurs clés.

Par exemple, pour afficher la clé `description`, utilisez `{{ translations.description }}`.

{% endraw %}
![][6]

Enfin, enregistrez le modèle d'e-mail et prévisualisez-le. Vous devriez voir votre traduction s'afficher.

## Foire aux questions

**Que se passe-t-il si je supprime accidentellement une clé de Lokalise ?**<br>
La chaîne de caractères correspondante sur Braze n'aura plus de traduction.

**Si j'ai un `en` local, mais que je la remplace par un `en-US` sur Lokalise, Braze le lira-t-il comme `en-US` ?**<br>
Non, les codes ISO locaux doivent correspondre sur Braze et Lokalise.

**Peut-on utiliser le drapeau `:rerender` pour connecter le contenu de Lokalise ?**<br>
Oui, bien sûr. Vous pouvez consulter la documentation de Braze pour savoir comment ajouter ce drapeau.

**Après avoir actualisé le fichier de traduction sur Lokalise, pourquoi ne puis-je pas voir de changements dans le contenu traduit sur Braze ?**<br>
Braze met en cache le contenu traduit, dont l'actualisation peut prendre quelques minutes. Si vous testez vos campagnes et avez besoin de voir les résultats des traductions immédiatement, vous pouvez utiliser le paramètre `:cache_max_age` comme expliqué dans cet article.

[1]: {% image_buster /assets/img/lokalise/1_add_key.png %}
[2]: {% image_buster /assets/img/lokalise/2_translation_key_added.png %}
[3]: {% image_buster /assets/img/lokalise/3_lokalise_braze_app.png %}
[4]: {% image_buster /assets/img/lokalise/4_testing_json_lokalise.png %}
[5]: {% image_buster /assets/img/lokalise/5_edit_email.png %}
[6]: {% image_buster /assets/img/lokalise/6_integration_usage_sample.png %}