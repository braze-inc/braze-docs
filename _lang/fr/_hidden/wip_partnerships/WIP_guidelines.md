---
alias: /partners/partner_walkthrough/
title: Documentation du partenaire
nav_title: Documents partenaire
hidden: true
page_type: article de référence
---

# Documentation de partenariat

Bienvenue, partenaires Braze, et merci d’avoir contribué à notre base de connaissances client. Créer et ajouter des pages partenaires au référentiel de documents Braze peut être rapide et simple avec les bons outils et la bonne configuration.

Présentation de la documentation de partenariat
- [Configurez votre environnement local](#setup_env)
- [Créez et ajoutez du contenu à votre page](#create_page)
- [Mise en forme de l’image, du lien et de l’extrait de code](#image_links)
- [Vérification et test](#testing)
- [Engagement avec Github](#committing)
- [Processus de vérification](#review)
<br><br>
{% alert important %}
Ce guide de partenariat est destiné aux NOUVEAUX partenaires de Braze qui **n'ont pas de documentation existante** déjà hébergée sur notre site. Si vous êtes un partenaire existant mettant à jour votre documentation, accédez à votre page partenaire (`braze-docs` > `_docs` > `_partners`) et mettez à jour vos pages comme vous le feriez normalement. 
{% endalert %}

## Étape 1 : Configurez votre environnement local {#setup_env}

Pour contribuer aux documents de Braze, vous devez avoir un compte GitHub pour valider les changements et les modifications. 

Nous recommandons d’abord de [dupliquer](https://help.github.com/en/github/getting-started-with-github/fork-a-repo) notre référentiel GitHub, puis de créer un clone local de votre duplication :
1. Naviguez jusqu’au principal [dépôt de documents de Braze](https://github.com/Appboy/braze-docs), et cliquez sur **Fork (Dupliquer)**. .<br><br>
2. Ensuite, dans ce nouveau référentiel, cliquez sur le bouton **Cloner ou télécharger**. Dans la fenêtre de dialogue visible à l’écran, cliquez sur **Utiliser SSH**, et **Enregistrer le lien de référentiel fourni** pour l’étape 3. <br><br>
3. Enfin, suivez notre Guide GitHub Wiki pour configurer votre [environnement local](https://github.com/Appboy/braze-docs/wiki/Set-Up-Your-Local-Environment#configuring-the-github-braze-docs-repo)[`Retrait en magasin`]**en ignorant l’étape 3 du guide**, et plutôt, **à l’aide du lien de référentiel enregistré,** pour cloner votre dépôt.

Après avoir configuré votre environnement local, assurez-vous de signer notre [CLC](https://www.braze.com/docs/cla) (contrat de licence de contribution),  _cette étape étant obligatoire_.

## Étape 2 : Créez et ajoutez du contenu à votre page {#create_page}

Pour créer votre page partenaire, ouvrez le référentiel braze-docs et naviguez jusqu’au `wip_partnerships` dossier  dans le référentiel. <br>Vous pouvez trouver ce dossier à l’aide du chemin suivant : `braze-docs` > `_docs` > `_hidden` > `wip_partnerships`. Vous trouverez ici un [modèle de partenariat]({{site.baseurl}}/partners/your_partner_name/).

Ensuite, créez un dossier, nommez-le, copiez ce modèle dans votre dossier et mettez-vous au travail !

> Votre chemin devrait maintenant ressembler à ceci : <br>`braze-docs` > `_docs` > `_hidden` > `wip_partnerships` > `partner_name` (dossier) > `partner.md`.
### Ressources utiles

Liens utiles à référencer lorsque vous écrivez :
- [Guide de style de rédaction de Braze et meilleures pratiques](https://docs.google.com/document/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub): Un petit coup d’œil à notre guide de style de rédaction et aux meilleures pratiques pour améliorer la correspondance entre votre documentation et notre communication.<br>
- [Page de style (test) des documents Braze](https://www.braze.com/docs/home/styling_test_page/) et [mise en forme spéciale](https://github.com/braze-inc/braze-docs/wiki/Special-Formatting) : Vous voyez quelque chose d’intéressant dans nos documents que vous souhaitez inclure sur votre page ? Vous voulez savoir comment ajouter des graphiques, des onglets, des fichiers téléchargeables, et bien plus encore ? Consultez notre page de style (test) et les pages de mise en forme spéciale pour commencer.

### Composants du modèle

Votre [modèle de partenariat]({{site.baseurl}}/partners/your_partner_name/) est composé de trois composants principaux, les métadonnées, le contenu et les références. 

{% tabs %}
{% tab Meta data %}
Ces informations aident notre recherche Braze à trouver, étiqueter et catégoriser correctement votre page de documents. 
```
---
nav_title: Votre page partenaire
article_title: Votre page partenaire
page_order: 1
description: "Il s'agit de la description qui apparaîtra dans le moteur de recherche et de référencement de Google. Essayez de la rendre informative et concise, mais brève."
alias: /partners/your_partner_name/
page_type: partenaire
search_tag: Partenaire
hidden: true
---
```

{% alert note %}
Notez qu’il vous est demandé de remplir tous les champs de métadonnées, **sauf**[`Retrait en magasin`]`page_order`, `page_type`, et `hidden`.
{% endalert %}

{% endtab %}
{% tab Content %}
Ces informations constituent l’essentiel du document. Ici, vous pouvez gérer les conditions préalables, les étapes d’intégration, les cas d’utilisation, etc.

Pour plus d’informations sur les contenus, consultez notre [modèle de partenariat]({{site.baseurl}}/partners/your_partner_name/) qui liste ce qui doit être inclus.

```
# [Nom du partenaire]
> Bienvenue dans le modèle de partenaire Braze ! Ici, vous trouverez tout ce dont vous avez besoin pour créer votre page partenaire. Dans cette première section, écrivez une brève description de votre entreprise. Incluez également un lien vers votre site principal. 
Dans ce second paragraphe, expliquez la relation entre votre entreprise et Braze. Ce paragraphe doit expliquer comment Braze et votre entreprise collaborent pour reserrer le lien entre l’utilisateur Braze et son client. Expliquez ce qui se produit lorsqu'un utilisateur de Braze s'intègre ou tire parti de votre partenariat et des services que vous offrez.
## Conditions préalables
Cette section doit indiquer ce dont vous avez besoin pour terminer cette intégration de partenariat. La meilleure façon de fournir ces informations est de rédiger un paragraphe d'instructions rapides qui décrit tous les détails non techniques importants ou les informations à connaître, comme le fait de savoir si votre intégration sera soumise ou non à des contrôles de sécurité ou à des habilitations supplémentaires. Utilisez ensuite un graphique pour décrire les exigences techniques de l’intégration.
{% alert important %}
Les exigences suivantes sont des exigences générales dont vous pourriez avoir besoin pour Braze. Nous vous recommandons d'utiliser le titrage et le phrasé attribués figurant dans le tableau suivant. Assurez-vous d’ajuster les descriptions et de les adapter à votre intégration de partenariat. 
{% endalert %}
| Configuration requise | Description |
| ----------- | ----------- |
| Compte partenaire | Un compte partenaire est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. .|
| Endpoint REST de Braze | [URL de votre endpoint REST][1]. Votre endpoint dépendra de l’URL Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2}
## Cas d’utilisation
Les cas d’utilisation peuvent constituer un élément essentiel de votre documentation. Bien que ce ne soit pas obligatoire, vous pouvez définir à cet endroit les cas d’utilisation typiques ou nouveaux pour l’intégration. Cela peut être utilisé comme un moyen de vendre ou de proposer une montée en gamme. Fournit du contexte, des idées et, surtout, un moyen de visualiser les capacités de l'intégration.
## Intégration
C’est là que vous divisez l’intégration en étapes. N’écrivez pas des paragraphes sans fin : il s’agit de documents techniques qui seront utilisés par les marketeurs et les développeurs à des fins d’intégration et d’exécution. Votre principal objectif est d’écrire une documentation descriptive qui aide l’utilisateur Braze à faire son travail.
```

{% endtab %}
{% tab References %}
Cette dernière section est située à la fin de votre document. Ici, vous dresserez la liste de toutes les références dont vous avez besoin pour les liens et images que vous souhaitez inclure dans votre document. Consultez l’étape suivante à propos des meilleures pratiques pour ajouter des images et des liens à votre document.
```
[1]: https://www.braze.com/docs/developer_guide/rest_api/basics/#endpoints
```
{% endtab %}
{% endtabs %}

## Étape 3 : Mise en forme de l’image, du lien et de l’extrait de code {#image_links}

Les liens et images sont indispensables dans un document d’intégration. Ils complètent vos instructions avec des images utiles, transmettent des informations aux utilisateurs qui peuvent être difficiles ou inutiles à expliquer avec des mots. 

### Images

Plus la qualité des images que vous pouvez fournir est élevée, mieux c'est. Les images ne doivent pas inclure d’informations importantes telles que les clés API ou les noms d’employés ; nous recommandons de flouter les informations en question. Les images doivent également être rognées pour contenir uniquement les informations utiles. En cas de doute, ajoutez des captures d’écran, car elles peuvent toujours être supprimées lors du processus d’approbation.

Pour ajouter des images à votre document de partenaire, vous devez les placer dans le référentiel dossier `img`. Vous pouvez trouver ce dossier à l’aide du chemin suivant : `braze-docs` > `assets` > `img`.

Dans ce nouveau dossier, créez un dossier pour conserver vos images de partenariat. Nommez ce dossier avec le nom de votre entreprise.

![Dossier partenaire Braze][1]{: style="max-width:70%"}

Pour référencer vos images dans votre document, utilisez le format suivant : 

{% raw %}
```
![topic_name][1]
```
{% endraw %}

Et à la fin de votre document, cliquez sur votre image.

{% raw %}
```
[1]: {% image_buster /assets/img/partner_file/image_name.png %}
```
{% endraw %}

### Liens

Pour ajouter des liens à votre document, vous devez suivre ce format :
{% raw %}
```
Pour plus d’informations, consultez [cette page Web ou la page][1].
```
{% endraw %}

Et à la fin de votre document, ajoutez votre lien.
{% raw %}
```
[1]: https://www.braze.com/docs/user_guide/onboarding_with_braze/integration/
```
{% endraw %}

### Liquid

Les intégrations partenaires tirent souvent parti de nos capacités Liquid dans le tableau de bord. Si vous prévoyez d’utiliser des extraits de code Liquid, positionnez-les entre les balises {&#37; raw &#37;} et {&#37; endraw &#37;} ou un avertissement Liquid sera généré dans Liquid.

{% raw %}

{&#37; raw &#37;}<br>
?user_braze_id={{&#36;{braze_id}}}<br>
{&#37; endraw &#37;}

{% endraw %}

## Étape 4 : Vérification et test {#testing}

L’une des choses les plus importantes à faire, avant de valider vos changements, est de réaliser un test pour s’assurer que tout semble fonctionner correctement. Cela peut être fait en exécutant une commande de `rake` dans votre terminal.

Dans votre terminal, vous verrez que la commande commence à fonctionner. Ce processus peut prendre plusieurs minutes. Votre commande sera effectuée une fois la mention « effectuée en x secondes, appuyez sur Ctrl+C pour arrêter » visible dans le terminal.

Ensuite, vous pouvez vérifier votre [localhost](http://localhost:4000/docs/).

Ici, vous pouvez consulter la page que vous avez créée à l’aide de l’alias attribué au préalable dans les métadonnées de l’article. Une fois le localhost ouvert, ajoutez l’alias pour accéder à votre page.

Example: `http://localhost:4000/docs/` + `/partners/your_partner_name/`

Votre page sera visible à l’adresse `http://localhost:4000/docs/partners/your_partner_name/`

Après avoir vérifié vos modifications, appuyez sur **Ctrl+C** dans le terminal et terminez la commande Rake.

## Étape 5 : Engagement avec Github {#committing}

Une fois que vous avez apporté les modifications adéquates à votre document de partenariat, enregistrez votre document et validez vos modifications. 

Dans le référentiel de documents GitHub de Braze, trouvez votre branche. Si votre document est terminé et prêt à être examiné, allez dans votre référentiel dupliqué dans GitHub et sélectionnez `New Pull Request`. Ensuite, sélectionnez la façon dont vous souhaitez fusionner votre branche dupliquée, nommez votre demande avec votre nom de partenariat et apportez toutes les informations pertinentes qui pourront nous être utiles lors de l’examen de votre contenu. 

![Fusionner les branches][2]

1. Configurez votre branche à fusionner de la même manière que celle illustrée dans l’image précédente.<br><br>
2. Nommez votre demande de tirage de la façon suivante : « Nom du partenariat - Documents partenaires"<br><br>
3. Fournissez toute information pertinente qui peut aider l’équipe de documentation de Braze à confirmer vos changements, et indiquez votre **chef de produit Braze** pour le contacter. Si nécessaire, nous vous recontacterons par la suite.<br><br>
4. Une fois que vous avez fait des changements, citez @KellieHawks et @Timothy-Kim dans un commentaire dans la demande de tirage, et notre équipe prendra le relais.<br><br>

## Processus de vérification {#review}

Le processus de vérification peut prendre entre quelques jours et une semaine pour être approuvé. Nous sommes conscients que d’autres entreprises et rédacteurs peuvent avoir un style d’écriture différent de celui adopté par Braze. Nous aurons donc besoin de temps pour nous assurer qu’il correspond à la communication de Braze.

Une fois que nos rédacteurs ont approuvé la demande de tirage, nous la déplacerons de `wip_partnerships` vers le bon emplacement dans notre référentiel. Notez que nous ne pouvons pas fusionner votre documentation dans notre référentiel tant que l’équipe de partenariat Braze n’a pas été informée. Contactez votre contact de partenariat Braze pour obtenir une date de sortie anticipée.

Et voilà ! Merci de contribuer aux documents de Braze ! 

[1]: {% image_buster /assets/img/partner_template/partner_folder.png %}
[2]: {% image_buster /assets/img/partner_template/partner_merge.png %}