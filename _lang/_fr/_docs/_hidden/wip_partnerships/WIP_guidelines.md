---
alias: /fr/partners/partner_walkthrough/
title: Documentation des partenaires
nav_title: Documentation des partenaires
hidden: vrai
page_type: Référence
---

# Documentation de partenariat

Bienvenue à Braze Partners et merci de contribuer à notre base de connaissances de nos clients. La création et l'ajout de pages partenaires au référentiel Braze docs peuvent être rapides et simples grâce aux bons outils et à la bonne configuration.

Aperçu de la documentation du partenariat
- [Configurez votre environnement local](#setup_env)
- [Créer et ajouter du contenu à votre page](#create_page)
- [Formatage de l'image, du lien et du code du snippet](#image_links)
- [Révision et test](#testing)
- [Commiting vers Github](#committing)
- [Processus de révision](#review)

{% alert important %}
Notez que ce guide de partenariat est destiné aux partenaires de NOUVEAU Braze qui __n'ont pas de documentation existante__ déjà hébergée sur notre site. Si vous êtes un partenaire existant mettant à jour votre documentation, accédez à votre page partenaire située dans : `braze-docs` -> `_docs` -> `_partners` et mettez à jour vos pages comme vous le feriez habituellement.
{% endalert %}

## Étape 1 : Configurez votre environnement local {#setup_env}

Pour contribuer à la documentation de Braze, vous devez avoir un compte Github avec lequel vous pouvez livrer des modifications et des modifications.

Nous vous recommandons d'abord __[de créer un forking](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) notre dépôt GitHub__, puis de créer un __clone local de votre fork__:
1. Naviguez vers le repo principal [braze-docs](https://github.com/Appboy/braze-docs), et cliquez sur __Fork__ dans le coin supérieur droit de la page. <br><br>
2. Ensuite, dans ce dépôt nouvellement bifurqué, cliquez sur le bouton vert __Cloner ou télécharger__. Dans la boîte de dialogue qui apparaît, cliquez sur __Utiliser SSH__et __enregistrer le lien de dépôt fourni__ pour l'étape 3. <br><br>
3. Enfin, suivez notre Guide de Wiki Github sur la façon de configurer votre [environnement local](https://github.com/Appboy/braze-docs/wiki/Set-Up-Your-Local-Environment#configuring-the-github-braze-docs-repo) __ommitting étape 3 du guide,__, et à la place, __en utilisant le lien de dépôt enregistré,__ pour cloner votre dépôt bifurqué.

Après avoir configuré votre environnement local, assurez-vous de signer notre [CLU](https://www.braze.com/docs/cla) (Accord de Licence de Contribution), _cette étape est nécessaire_.

## Étape 2 : Créer et ajouter du contenu à votre page {#create_page}

Pour créer votre page partenaire, ouvrez le dépôt braze-docs et accédez au dossier `wip_partners` dans le dépôt. <br>Ce dossier peut être trouvé en suivant le chemin du fichier : `braze-docs` -> `_docs` -> `_hidden` -> `wip_partners`.

Ici, vous trouverez un [Modèle de Partenariat]({{site.baseurl}}/partners/your_partner_name/). Ensuite, créez un dossier, nommez-le votre nom de partenaire, copiez ce modèle dans votre dossier et mettez-le au travail!

> Votre pathing de fichier devrait maintenant ressembler à ceci: `braze-docs` -> `_docs` -> `_hidden` -> `wip_partnerships` -> `partner_name` (dossier) -> `partenaire. d`.

### Ressources utiles

Liens utiles à la référence en écrivant :
- [Braze Writing Style Guide et Meilleures Pratiques](https://docs.google.com/document/d/e/2PACX-1vTtzHpcihaXTTYD85LoKIvYBvpCQFLr8n0BDKRDRAMEz_DnZdHJJINKL24r4JXkRUui24pl_DVxbu2T/pub#h.wstt3flbts5k): Un rapide skim de notre guide de style d'écriture et des meilleures pratiques aident à aligner votre documentation sur notre voix.<br>
- [Braze Docs Styling Test Page](https://www.braze.com/docs/home/styling_test_page/) et [Format Spécial](https://github.com/braze-inc/braze-docs/wiki/Special-Formatting): Voyez quelque chose de cool dans notre documentation que vous voulez inclure dans votre page ? Vous voulez savoir comment ajouter des graphiques, des onglets, des fichiers téléchargeables et plus encore ? Consultez notre page de test de style et nos pages de mise en forme spéciale pour commencer.

### Composants de modèle

Votre [Modèle de Partenariat]({{site.baseurl}}/partners/your_partner_name/) est composé de trois composants principaux, les métadonnées, le contenu et les références.

{% tabs %}
{% tab MetaData %}
Cette information aide notre recherche Braze à trouver, étiqueter et catégoriser correctement votre page de documentation.
```
---
nav_title: Votre page partenaire
page_order: 1

description: "C'est la recherche Google et la description SEO qui apparaîtront. Essayez de rendre cette information et concise, mais bref.
alias : /partners/your_partnership_name/

page_type : partenaire
search_tag : partenaire
masqué : vrai
---
```

{% alert note %}
Notez que nous vous demandons de remplir tous les champs de métadonnées __sauf__ `page_order`, `page_type`, et `caché`.
{% endalert %}

{% endtab %}
{% tab Content %}
Cette information est la viande du document. Ici vous couvrirez les conditions préalables, les étapes d'intégration, les cas d'utilisation, etc. Pour plus d'informations sur ce qu'il faut inclure dans le contenu, consultez notre [Modèle de partenariat]({{site.baseurl}}/partners/your_partner_name/) qui décompose ce qui doit être inclus.
```
# [Nom du partenaire]

> Bienvenue dans le modèle de page partenaire ! Ici, vous trouverez tout ce dont vous avez besoin pour créer votre page partenaire. Dans cette première section, vous devez décrire le partenaire dans le premier paragraphe d'une phrase ou deux. En outre, inclure un lien vers le site principal de ce partenaire.

Dans le deuxième paragraphe, vous devriez explorer et expliquer la relation entre Braze et ce partenaire. Ce paragraphe devrait expliquer comment Braze et ce partenaire travaillent ensemble pour resserrer le lien entre l'utilisateur de Braze et son client. Expliquez la « élévation » qui se produit lorsqu'un utilisateur de Braze s'intègre ou tire parti de ce partenaire et de ses services.

## Exigences ou pré-requis

Cette section vous propose tout ce dont vous avez besoin pour vous intégrer au partenaire et commencer à utiliser ses services. La meilleure façon de fournir ces informations est d'utiliser un paragraphe d'instruction rapide qui décrit tous les détails non techniques importants de "besoin de savoir" des informations, que votre intégration soit ou non soumise à des contrôles de sécurité ou à des autorisations supplémentaires. Ensuite, vous devriez utiliser un tableau pour décrire les exigences techniques de l'intégration.

{% alert important %}
Les exigences énumérées ci-dessous sont des exigences typiques que vous pourriez avoir besoin du Brésil. Nous vous recommandons d'utiliser le titre attribué, l'origine, les liens et le phrasé tel que listé dans le graphique ci-dessous. Assurez-vous d'ajuster la description afin que vous sachiez à quoi sert chacune de ces exigences.
{% endalert %}

| Exigence | Origine | Accès | Description |
|---|---|---|---|
| Braze API Key | Braze | Vous aurez besoin de créer une nouvelle clé API.<br><br>Ceci peut être créé dans la __console développeur -> Paramètres API -> Créer une nouvelle clé API__ avec __utilisateurs. permissions__ de rack. | Cette description devrait vous indiquer ce qu'il faut faire avec la clé API de Braze. |
| Braze REST Terminal | Braze | [Braze REST Endpoint List][1] | Votre URL REST Endpoint URL. Votre point de terminaison dépendra de l'URL de Braze pour votre instance. |

## [Type d'intégration] Intégration

C'est là que vous décomposez l'intégration en étapes. Ne vous contentez pas d'écrire des paragraphes sans fin - ce sont des documents techniques... Poursuite dans le modèle de partenariat.
```

{% endtab %}
{% tab References %}
Cette dernière section se trouve à la fin de votre document. Vous trouverez ici la liste de toutes les références dont vous avez besoin pour les liens et les images que vous voulez inclure dans votre document. Veuillez consulter l'étape suivante sur les meilleures pratiques pour ajouter des images et des liens à votre doc.
```
[1]: https://www.braze.com/docs/developer_guide/rest_api/basics/#endpoints
```
{% endtab %}
{% endtabs %}

## Étape 3 : Formatage de l'image, du lien et du code du snippet {#image_links}

Les liens et les images sont une partie nécessaire de tout document d'intégration. Ils aident à compléter vos instructions par des images utiles, à communiquer aux utilisateurs des informations qui peuvent être difficiles ou inutiles à expliquer en mots.

### Images

Plus la qualité des images est élevée, mieux c'est. Les images ne doivent pas inclure d'informations importantes telles que les clés API ou les noms des employés; nous vous recommandons de graver des informations telles que celle-ci. Les images doivent également être recadrées de façon très étroite pour n'afficher que des informations utiles. En cas de doute, incluez les captures d'écran, car elles peuvent toujours être supprimées dans le processus d'approbation.

Pour ajouter des images à votre doc partenaire, vous devez les placer dans le dossier `img` de notre dépôt. Ce dossier peut être trouvé en suivant le chemin du fichier : `braze-docs` -> `assets` -> `img`.

Dans ce nouveau dossier, créez un dossier pour conserver vos images en partenariat. Nommez ce dossier votre nom de partenaire.

!\[Braze Partner Folder\]\[1\]{: style="max-width:70%"}

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
## Révision et test {#testing}

L'une des choses les plus importantes que vous puissiez faire avant de valider vos modifications est de tester que tout semble et fonctionne comme il se doit. Cela peut être fait en exécutant une commande `rake` dans votre terminal.

Dans votre terminal, vous verrez que la commande commence à fonctionner. Ce processus peut prendre plusieurs minutes. Vous saurez quand la commande est terminée quand vous verrez "fait en x secondes, appuyez sur ctrl-c pour arrêter" apparaître dans le terminal.

Ensuite, vous pouvez vérifier votre [localhost](http://localhost:4000/docs/).

Ici vous pouvez naviguer vers la page que vous avez créée grâce à l'alias que vous avez assigné précédemment. Une fois que vous ouvrez le localhost, ajoutez l'alias pour accéder à votre page.

Exemple: `http://localhost:4000/docs/` + `/partners/votre_partner_name/`

Votre page sera visible à `http://localhost:4000/docs/partners/your_partner_name/`

Une fois que vous avez passé en revue vos modifications, appuyez sur Ctrl-C dans le terminal, mettant fin à la commande rake.

## Commiting vers Github {#committing}

Une fois que vous avez apporté les modifications adéquates à votre doc de partenariat, enregistrez votre document et validez vos modifications.

Dans le dépôt GitHub de Braze docs, vous pourrez trouver votre branche. Si votre document est terminé et prêt à être revu, accédez à votre dépôt bifurqué dans Github et sélectionnez `Nouvelle Pull Request`. Ensuite, sélectionnez comment vous souhaitez que votre branche forked soit fusionnée, nommez votre demande de nom de votre société et fournissez toute information pertinente que nous pouvons utiliser pour référencer lorsque nous examinons votre contenu.

1. Configurez votre branche à fusionner de manière similaire comme indiqué ci-dessous.<br>!\[Merge Branches\]\[2\]<br><br>
2. Nommez votre Pull Request en tant que "Nom de Partenariat - Documentation Partenaires"<br><br>
3. Fournir toutes les informations pertinentes qui peuvent aider l'équipe de documentation de Braze à confirmer vos modifications, ainsi que votre __gestionnaire de produits Braze__ afin que nous puissions leur contacter pour vous contacter au sujet de vos changements si nécessaire.<br><br>
4. Une fois que vous avez fini de faire des changements, ajoutez @KellieHawks et @Timothy-Kim dans un commentaire au sein du RP, et notre équipe y jettera un œil.<br><br>

## Processus de révision {#review}

Le processus d’examen peut prendre plusieurs jours à une semaine pour être approuvé. Nous comprenons que d'autres entreprises et écrivains peuvent avoir un style d'écriture différent de celui que nous utilisons à Braze, donc nous aurons besoin de temps pour nous assurer qu'il s'aligne avec la voix Braze et le formatage spécifique que nous utilisons.

Une fois que la demande d'ajout a été approuvée par nos auteurs, nous allons le déplacer de `wip_partners` à l'emplacement correct dans notre dépôt. Veuillez noter que nous ne pouvons pas fusionner votre documentation dans notre référentiel tant que l'équipe de partenariat de Braze n'a pas donné son approbation. Communiquez avec votre partenaire Braze pour une date de sortie anticipée.

Et vous avez terminé ! Merci pour votre contribution à Braze Docs!
[1]: {% image_buster /assets/img/partner_template/partner_folder.png %} [2]: {% image_buster /assets/img/partner_template/partner_merge.png %}
