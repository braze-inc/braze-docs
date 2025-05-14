---
nav_title: Lokalise
article_title: Lokalise
description: "Cet article de référence présente le partenariat entre Braze et Lokalise, un service de gestion des traductions pour les équipes agiles."
alias: /partners/lokalise/
page_type: partner
search_tag: Partner

---

# Lokalise

> [Lokalise](https://lokalise.com) est un service de gestion des traductions pour les équipes agiles.

_Cette intégration est maintenue par Lokalise._

## À propos de l'intégration

L'intégration entre Braze et Lokalise s'appuie sur le contenu connecté pour vous permettre d'insérer facilement du contenu traduit dans vos campagnes Braze en fonction des paramètres linguistiques de l'utilisateur.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Lokalise | Un compte Lokalise est nécessaire pour bénéficier de ce partenariat. |
| Projet de traduction Lokalise | Un projet de traduction Lokalise doit être créé avant de mettre en place cette intégration. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Créez un nouveau projet Lokalise

Pour créer un nouveau projet de traduction, connectez-vous à Lokalise et sélectionnez **Nouveau projet**. Ensuite, nommez votre projet, choisissez une **langue de base** (la langue à partir de laquelle vous allez traduire), ajoutez une ou plusieurs **langues cibles** et choisissez le type de projet **Localisation de logiciels.** Lorsque vous êtes prêt, cliquez sur **Continuer**.

## Intégration

Dans Lokalise, vous allez créer une clé de traduction pour chacune des variables de contenu connecté que vous définissez dans Braze. Lorsque les traductions sont prêtes, vous pouvez générer un fichier JSON par langue et le publier sur les URL qui serviront votre contenu connecté.

### Étape 1 : Configuration des langues utilisateur

Si vous ne l'avez pas encore fait, ouvrez le tableau de bord de Braze et allez dans **Utilisateurs > Importation d'utilisateurs.** Ici, vous pouvez importer vos utilisateurs. Lorsque vous préparez un fichier CSV pour l'importation, veillez à inclure une colonne de langues avec les langues des utilisateurs. Ce champ linguistique sera utilisé ultérieurement lors de l'affichage des traductions. 

{% alert important %}
Les codes linguistiques utilisés doivent correspondre à ceux de Braze et de Lokalise.
{% endalert %}
### Étape 2 : Préparer vos traductions sur Lokalise

Ensuite, pour préparer vos traductions sur Lokalise, vous devez créer manuellement les clés de traduction avec le même nom que celui que vous utilisez sur les variables de contenu connecté de Braze. 

Par exemple, créons une clé de traduction simple, `description` :
1. Ouvrez votre projet Lokalise, cliquez sur **Ajouter une clé**, entrez "description" dans le champ **Clé**.
2. Tapez "Description de démonstration" dans le champ **Valeur de langue de base**.
3. Ajoutez "Web" dans la liste déroulante **Plateformes.**  
4. Lorsque vous êtes prêt, cliquez sur **Enregistrer.**

![][1]{: style="max-width:60%"}

Votre clé de traduction devrait apparaître dans l'éditeur de projet :

![][2]{: style="max-width:90%"}

#### Problèmes connus

- Vos clés doivent être attribuées à la plate-forme **Web.** 
- Évitez d'utiliser des clés contenant des points (`.`) ou la chaîne de caractères `_on`. Par exemple, utilisez `this_is_the_key` au lieu de `this.is.the.key`, et `join_us_instagram` au lieu de `join_us_on_instagram`.

### Étape 3 : Configuration de l'application Braze sur Lokalise

Ouvrez votre projet Lokalise et cliquez sur **Apps.** Ici, recherchez et installez l'application Braze. L'écran suivant s'affiche :

![Configuration de Braze sur Lokalise indiquant l'ID du projet et l'URL des fichiers de traduction.][3]

Dans l'**URL du fichier de traduction**, Lokalise publie un fichier JSON contenant toutes les traductions de vos clés dans le projet. Vous obtiendrez autant d'URL de fichiers de traduction que de langues cibles dans votre projet. C'est pourquoi les URL des fichiers de traduction qui en résultent comportent deux parties :

1. La première partie du chemin URL est commune à toutes les langues.
2. Le nom du fichier JSON à la fin de l'URL est basé sur le code de la langue.

L'URL du fichier de traduction est l'URL dont vous aurez besoin pour configurer une campagne Braze. Vous pouvez actualiser le contenu du fichier JSON en cliquant sur **Actualiser**. Notez que l'URL restera la même et que vous n'aurez pas besoin de modifier votre appel au contenu connecté dans Braze.

### URL du test

Pour tester cette URL, copiez-la et remplacez {% raw %}`{{${language}}}`{% endraw %} par un code de langue (par exemple, `en`) et ouvrez cette URL dans votre navigateur. Vous obtiendrez un fichier JSON contenant vos clés et vos traductions :

![][4]

### Étape 4 : Utilisation des traductions dans la campagne Braze

#### Insérer un appel à contenu connecté

Lorsque vous êtes prêt, retournez dans Braze et ouvrez une campagne existante ou créez-en une nouvelle. Nous allons créer une nouvelle campagne e-mail avec un exemple de contenu pour cet exemple. Cliquez sur **Modifier le corps de l'e-mail**.

Pour insérer vos traductions, vous devez ajouter la requête de contenu connecté dans le code HTML, soit en haut du document, soit juste avant le premier endroit où une traduction est nécessaire. Vous pouvez le faire en insérant la balise suivante :

{% raw %}
`{% connected_content https://exports.live.lokalise.cloud/braze/123abc/456xyz/{{${language}}}.json :save translations %}`
{% endraw %}

Remplacez l'URL `https://exports.live.lokalise.cloud/...` par l'URL du fichier de traduction récupéré à l'étape précédente.

{% raw %}

- `{{${language}}}` signifie "insérer la langue de l'utilisateur sur ce poste". Vous pouvez également coder en dur le code de votre langue, par exemple `en.json`.
  - Pour vous assurer que le fichier JSON traduit approprié est récupéré pour chaque utilisateur, vous devez placer l'attribut de profil `{{${language}}}` ou un autre attribut personnalisé similaire contenant la langue de l'utilisateur à la fin de l'URL des fichiers de traduction. (par exemple, `/{{${language}}}.json`) Les valeurs contenues dans ces attributs doivent correspondre au préfixe de chacun des fichiers JSON traduits. Cela permet de s'assurer que le fichier de traduction correct est renvoyé pour chaque utilisateur.
- `:save translations` enregistrera le contenu JSON dans la variable translations.

#### Afficher les traductions

Utilisez maintenant la variable translations pour afficher les traductions souhaitées par leur clé.

Par exemple, pour afficher la clé `description`, utilisez`{{ translations.description }}`.

{% endraw %}
![][6]

Enfin, enregistrez le modèle d'e-mail et prévisualisez-le. Vous devriez voir votre traduction s'afficher.

## Questions fréquemment posées

**Que se passe-t-il si je supprime accidentellement une clé de Lokalise ?**<br>
La chaîne de caractères correspondante sur Braze n'aura plus de traduction.

**Si j'ai un paramètre local défini sur `en` mais que je le remplace par `en-US` dans Lokalise, Braze pourra-t-il le fichier en tant que `en-US` ?**<br>
Non, les codes ISO locaux doivent correspondre sur Braze et Lokalise.

**Peut-on utiliser l’indicateur `:rerender` pour connecter du contenu Lokalise ?**<br>
Oui, bien sûr. Vous pouvez consulter la documentation de Braze pour savoir comment ajouter ce drapeau.

**Après avoir actualisé le fichier de traduction sur Lokalise, pourquoi ne vois-je pas de changements dans le contenu traduit sur Braze ?**<br>
Braze met en cache le contenu traduit et son actualisation peut prendre quelques minutes. Si vous testez vos campagnes et avez besoin de voir les résultats des traductions immédiatement, vous pouvez utiliser le paramètre `:cache_max_age` comme expliqué dans cet article de référence.


[1]: {% image_buster /assets/img/lokalise/1_add_key.png %}
[2]: {% image_buster /assets/img/lokalise/2_translation_key_added.png %}
[3]: {% image_buster /assets/img/lokalise/3_lokalise_braze_app.png %}
[4]: {% image_buster /assets/img/lokalise/4_testing_json_lokalise.png %}
[5]: {% image_buster /assets/img/lokalise/5_edit_email.png %}
[6]: {% image_buster /assets/img/lokalise/6_integration_usage_sample.png %}