---
alias: /fr/partners/partner_walkthrough/
title: Documentation des partenaires
nav_title: Documentation des partenaires
hidden: vrai
page_type: Référence
---

# Documentation du partenariat

Bienvenue, Braze Partners et merci de contribuer à notre base de connaissances de la clientèle. La création et l'ajout de pages partenaires au référentiel Braze docs peuvent être rapides et simples grâce aux bons outils et à la bonne configuration.

Aperçu de la documentation du partenariat
- [Configurer votre environnement local](#setup_env)
- [Créer et ajouter du contenu à votre page](#create_page)
- [Formatage de l'image, du lien et du code snippet](#image_links)
- [Révision et test](#testing)
- [Commiting vers Github](#committing)
- [Processus de revue](#review) <br><br>
{% alert important %}
Ce guide de partenariat est destiné aux partenaires de NOUVEAU Braze qui **n'ont pas de documentation existante** déjà hébergée sur notre site. Si vous êtes un partenaire existant mettant à jour votre documentation, accédez à votre page partenaire située à `braze-docs` -> `_docs` -> `_partners` et mettez à jour vos pages comme vous le feriez habituellement.
{% endalert %}

## Étape 1 : Configurez votre environnement local {#setup_env}

Pour contribuer à Braze docs, vous devez avoir un compte Github pour valider les modifications et les modifications.

Nous vous recommandons d'abord de [forking](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) notre dépôt GitHub, puis de créer un clone local de votre fork:
1. Naviguez vers le repo principal [braze-docs](https://github.com/Appboy/braze-docs), et cliquez sur __Fork__ dans le coin supérieur droit de la page. <br><br>
2. Ensuite, dans ce dépôt nouvellement bifurqué, cliquez sur le bouton vert __Cloner ou télécharger__. Dans la boîte de dialogue qui apparaît, cliquez sur __Utiliser SSH__et __enregistrer le lien de dépôt fourni__ pour l'étape 3. <br><br>
3. Enfin, suivez notre Guide Github Wiki sur la configuration de votre [environnement local](https://github.com/Appboy/braze-docs/wiki/Set-Up-Your-Local-Environment#configuring-the-github-braze-docs-repo) __ommitting étape 3 du guide,__, et à la place, __en utilisant le lien de dépôt enregistré,__ pour cloner votre dépôt bifurqué.

Après avoir configuré votre environnement local, assurez-vous de signer notre [CLU](https://www.braze.com/docs/cla) (Accord de Licence de Contribution), _cette étape est nécessaire_.

## Étape 2 : Créer et ajouter du contenu à votre page {#create_page}

Pour créer votre page partenaire, ouvrez le dépôt braze-docs et accédez au dossier `wip_partners` dans le dépôt. <br>Ce dossier peut être trouvé en suivant le chemin du fichier : `braze-docs` -> `_docs` -> `_hidden` -> `wip_partners`. Ici, vous trouverez un [modèle de partenariat]({{site.baseurl}}/partners/your_partner_name/).

Ensuite, créez un dossier, nommez-le votre nom de partenaire, copiez ce modèle dans votre dossier et mettez-le au travail!

> Votre pathing de fichier devrait maintenant ressembler à ceci: <br>`braze-docs` -> `_docs` -> `_hidden` -> `wip_partnerships` -> `partner_name` (dossier) -> `partenaire. d`.

### Ressources utiles

Liens utiles à la référence en écrivant :
- [Le guide de style d'écriture Braze et les meilleures pratiques](https://docs.google.com/document/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub): un rapide déluge de notre guide de style d'écriture et de nos meilleures pratiques aident à aligner votre documentation sur notre voix.<br>
- [Braze docs styling page de test](https://www.braze.com/docs/home/styling_test_page/) et [de formatage spécial](https://github.com/braze-inc/braze-docs/wiki/Special-Formatting): Voyez quelque chose de cool dans notre documentation que vous voulez inclure dans votre page ? Vous voulez savoir comment ajouter des graphiques, des onglets, des fichiers téléchargeables et plus encore ? Consultez notre page de test de style et nos pages spéciales de mise en forme pour commencer.

### Composants de modèle

Votre [modèle de partenariat]({{site.baseurl}}/partners/your_partner_name/) est composé de trois composants principaux, les métadonnées, le contenu et les références.

{% tabs %}
{% tab Meta data %}
Cette information aide notre recherche Braze à trouver, étiqueter et catégoriser correctement votre page de documentation.
```
---
nav_title: Votre page partenaire
article_title: Votre page partenaire
page_order: 1

description: "Ceci est la description de Google Search et SEO qui apparaîtra ; essayez de rendre cette information et concise, mais brève.
alias : /partners/your_partner_name/

page_type : partenaire
search_tag : partenaire
caché : vrai
---
```

{% alert note %}
Notez que nous vous demandons de remplir tous les champs de métadonnées __sauf__ `page_order`, `page_type`, et `caché`.
{% endalert %}

{% endtab %}
{% tab Content %}
Cette information est la viande du document. Ici vous couvrirez les conditions préalables, les étapes d'intégration, les cas d'utilisation, etc.

Pour plus d'informations sur ce qu'il faut inclure dans le contenu, consultez notre [modèle de partenariat]({{site.baseurl}}/partners/your_partner_name/) qui décompose ce qui doit être inclus.

```
# [Nom du partenaire]

> Bienvenue dans le modèle du partenaire de Braze ! Ici, vous trouverez tout ce dont vous avez besoin pour créer votre page partenaire. Dans cette première section, incluez une brève description de votre entreprise. De plus, incluez un lien vers votre site principal. 

Dans ce deuxième paragraphe, explorez la relation entre votre entreprise et le Brésil. Ce paragraphe devrait expliquer comment Braze et votre partenaire de l'entreprise ensemble pour resserrer le lien entre l'utilisateur de Braze et son client. Expliquez la « élévation » qui se produit lorsqu'un utilisateur de Braze s'intègre à votre partenariat et les services que vous offrez.

## Pré-requis

Cette section devrait indiquer ce dont vous avez besoin pour compléter cette intégration de partenariat. La meilleure façon de fournir ces informations est d'utiliser un paragraphe d'instruction rapide qui décrit tous les détails non techniquement importants ou les informations "besoin de savoir" que votre intégration soit ou non soumise à des contrôles de sécurité ou à des autorisations supplémentaires. Ensuite, utilisez un graphique pour décrire les exigences techniques de l'intégration.

{% alert important %}
Les exigences énumérées ci-dessous sont des exigences typiques que vous pourriez avoir besoin du Brésil. Nous vous recommandons d'utiliser le titre et le libellé attribués listés dans le graphique ci-dessous. Assurez-vous d'ajuster les descriptions et de les adapter à votre intégration de partenariat. 
{% endalert %}

| Exigences | Description |
| ----------- | ----------- |
| Compte partenaire | Un compte partenaire est requis pour profiter de ce partenariat. |
| Braze REST API key | A Braze REST API Key with `users.track` permissions. <br><br> Ceci peut être créé dans le tableau de bord __Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API __ |
| Braze REST endpoint | [Votre URL REST terminal][1]. Votre point de terminaison dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d'utilisation

Les cas d'utilisation peuvent être une partie critique de votre documentation. Bien que facultatif, c'est un bon endroit pour décrire les cas d'utilisation typiques ou même romans pour l'intégration. Cela peut être utilisé comme un moyen de vendre ou de vendre la relation - il fournit le contexte, , et plus important encore, une façon de visualiser les capacités de l'intégration.

## Intégration

C'est là que vous décomposez l'intégration en étapes. Ne vous contentez pas d'écrire des paragraphes interminables - ce sont des documents techniques qui seront utilisés par les marketeurs et les développeurs pour faire fonctionner l'intégration. Votre objectif principal est d'écrire une documentation descriptive qui aide l'utilisateur de Braze à faire le travail.
```

{% endtab %}
{% tab References %}
Cette dernière section se trouve à la fin de votre document. Ici, vous listerez toutes les références dont vous avez besoin pour les liens et les images que vous voulez inclure dans votre document. Veuillez consulter l'étape suivante sur les meilleures pratiques pour ajouter des images et des liens à votre doc.
```
[1]: https://www.braze.com/docs/developer_guide/rest_api/basics/#endpoints
```
{% endtab %}
{% endtabs %}

## Étape 3: Formatage de l'image, du lien et du code snippet {#image_links}

Les liens et les images sont une partie nécessaire de tout document d'intégration. Ils aident à compléter vos instructions par des images utiles, à communiquer aux utilisateurs des informations qui peuvent être difficiles ou inutiles à expliquer en mots.

### Images

Plus la qualité des images est élevée, mieux c'est. Les images ne doivent pas inclure d'informations importantes telles que les clés API ou les noms des employés; nous vous recommandons de graver des informations telles que celle-ci. Les images doivent également être recadrées de façon très étroite pour n'afficher que des informations utiles. En cas de doute, incluez les captures d'écran, car elles peuvent toujours être supprimées dans le processus d'approbation.

Pour ajouter des images à votre doc partenaire, vous devez les placer dans le dossier `img` de notre dépôt. Ce dossier peut être trouvé en suivant le chemin du fichier : `braze-docs` -> `assets` -> `img`.

Dans ce nouveau dossier, créez un dossier pour conserver vos images en partenariat. Nommez ce dossier pour le nom de votre entreprise.

!\[Dossier partenaire Braze\]\[1\]{: style="max-width:70%"}

Pour référencer vos images dans votre document, utilisez le format indiqué ci-dessous.

{% raw %}
```
![topic_name][1]
```
{% endraw %}

Et à la fin de votre document, faites un lien vers votre image.

{% raw %}
```
[1]: {% image_buster /assets/img/partner_file/image_name.png %}
```
{% endraw %}

### Liens

Pour ajouter des liens à votre document, vous devez suivre ce format :
{% raw %}
```
Pour plus d'informations, consultez [ce site ou cette page][1].
```
{% endraw %}

Et à la fin de votre document, ajoutez votre lien.
{% raw %}
```
[1]: https://www.braze.com/docs/user_guide/onboarding_with_braze/integration/
```
{% endraw %}

### Liquide

Les intégrations de partenaires tirent souvent parti de nos capacités Liquid dans le tableau de bord. Si vous prévoyez d'inclure des extraits de code Liquid, ils doivent être emballés entre {&#37; raw &#37;} et {&#37; endraw &#37;} ou vous obtiendrez un avertissement Liquid dans markdown.

{% raw %}

{&#37; raw &#37;}<br> ?user_braze_id={{&#36;{braze_id}}}<br>
{&#37; endraw &#37;}

{% endraw %}

## Étape 4 : Révision et test {#testing}

L'une des choses les plus importantes que vous puissiez faire avant de valider vos modifications est de tester que tout semble et fonctionne comme il se doit. Cela peut être fait en exécutant une commande `rake` dans votre terminal.

Dans votre terminal, vous verrez que la commande commence à fonctionner. Ce processus peut prendre plusieurs minutes. Vous saurez quand la commande est terminée quand vous verrez "fait en x secondes, appuyez sur ctrl-c pour arrêter" apparaître dans le terminal.

Ensuite, vous pouvez vérifier votre [localhost](http://localhost:4000/docs/).

Ici vous pouvez naviguer vers la page que vous avez créée en utilisant l'alias que vous avez assigné précédemment dans les métadonnées de l'article. Une fois que vous ouvrez le localhost, ajoutez l'alias pour accéder à votre page.

Exemple: `http://localhost:4000/docs/` + `/partners/votre_partner_name/`

Votre page sera visible à `http://localhost:4000/docs/partners/your_partner_name/`

Après avoir examiné vos modifications, appuyez sur **Ctrl-C** dans le terminal et terminez la commande rake.

## Étape 5 : Commiting to Github {#committing}

Une fois que vous avez apporté les modifications adéquates à votre doc de partenariat, enregistrez votre document et validez vos modifications.

Dans le dépôt GitHub de Braze docs, trouvez votre branche. Si votre document est terminé et prêt à être revu, accédez à votre dépôt bifurqué dans Github et sélectionnez `Nouvelle Pull Request`. Ensuite, sélectionnez comment vous souhaitez que votre branche forked soit fusionnée, nommez votre demande de nom de votre société et fournissez toute information pertinente que nous pouvons utiliser pour référencer lorsque nous examinons votre contenu.

!\[Branches de Fusion\]\[2\]

1. Configurez votre branche pour qu'elle soit fusionnée de manière similaire à celle montrée ci-dessus.<br><br>
2. Nommez votre Pull Request en tant que "Nom de Partenariat - Documentation Partenaires"<br><br>
3. Fournir toutes les informations pertinentes qui peuvent aider l'équipe de documentation de Braze à confirmer vos modifications, ainsi que votre __gestionnaire de produits Braze__ afin que nous puissions leur contacter pour vous contacter au sujet de vos changements si nécessaire.<br><br>
4. Une fois que vous avez fini de faire des changements, étiquetez @KellieHawks et @Timothy-Kim dans un commentaire dans la pull request, et notre équipe y jettera un œil.<br><br>

## Processus de révision {#review}

Le processus d’examen peut prendre plusieurs jours à une semaine pour être approuvé. Nous comprenons que d'autres entreprises et écrivains peuvent avoir un style d'écriture différent de celui que nous utilisons à Braze, donc nous aurons besoin de temps pour nous assurer qu'il s'aligne avec la voix Braze et le formatage spécifique que nous utilisons.

Une fois que nos auteurs auront approuvé la demande de pull, nous la déplacerons de `wip_partners` à l'emplacement correct dans notre dépôt. Veuillez noter que nous ne pouvons pas fusionner votre documentation dans notre référentiel tant que l'équipe de partenariat de Braze ne l'a pas fait. Communiquez avec votre interlocuteur de partenariat de Braze pour une date de sortie anticipée.

Et vous avez terminé ! Merci pour votre contribution à Braze docs !
[1]: {% image_buster /assets/img/partner_template/partner_folder.png %} [2]: {% image_buster /assets/img/partner_template/partner_merge.png %}
