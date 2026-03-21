---
nav_title: Guide de style Braze Docs
article_title: Guide de style Braze Docs
description: "Guide de style rédactionnel pour Braze Docs."
page_order: 0
noindex: true
---

# Guide de style Braze Docs

## Guide de style rédactionnel

<style>
.style-guide-table td {
  overflow-wrap: break-word;
  word-break: break-word;
  min-width: 0;
}
</style>

### Directives générales {#general-guidelines}

#### Voix et ton {#voice-and-tone}

La voix de la marque Braze est intelligente, conversationnelle et directe. Nous sommes une voix humaine dans un monde de jargon technologique ; nous apportons clarté et orientation à toute personne intéressée par l'art de l'engagement client ; et nous évitons le jargon au profit d'un langage concis, aussi facile à comprendre que puissant.

Pour aligner cette voix de marque dans notre rédaction et notre édition, nous utilisons trois principes directeurs : **direct, responsabilisant** et **humain**.

##### Direct

Structurez clairement votre rédaction et facilitez la recherche d'informations.

* Expliquez simplement les choses compliquées.
* Soyez concis.
* Utilisez un vocabulaire cohérent pour les fonctionnalités et les actions.

###### Directives

✅ Utilisez des visuels pour clarifier les sujets complexes. <br>
**Exemple :** L'image du cycle de vie du profil utilisateur dans l'[article sur le cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) aide à illustrer un concept délicat.

✅ Créez une hiérarchie d'information claire. <br>
**Exemple :** « Voici un aperçu de la gestion du contenu sur Braze Docs. Pour en savoir plus sur un sujet spécifique, choisissez la page dédiée dans la navigation. »

✅ Éliminez impitoyablement le jargon et les acronymes si possible. Sinon, définissez-les. <br>
**Exemple :** « Le Short Messaging Service (SMS) est utilisé pour envoyer et recevoir de courts messages texte. »

##### Responsabilisant

Quel problème essayez-vous de résoudre avec votre rédaction ? Gardez ce problème à l'esprit lors de la création de tout contenu.

* Expliquez le « pourquoi » et le « comment » pour donner aux utilisateurs la confiance nécessaire pour agir.
* Soyez précis lorsque vous expliquez les avantages, et soyez clair sur ce qui est et n'est pas possible.
* Offrez des conseils pratiques et des encouragements sincères.

###### Directives

✅ Facilitez la recherche du parcours optimal. <br>
**Exemple :** « Lorsque vous arrêtez un Canvas, les règles suivantes s'appliquent : 1. Les utilisateurs ne peuvent plus entrer dans le Canvas. 2. Aucun message supplémentaire n'est envoyé, quel que soit l'endroit où se trouve un utilisateur dans le flux. 3. **Exception :** les Canvas par e-mail ne s'arrêtent pas immédiatement. »

✅ Fournissez des exemples, des cas d'utilisation et des modèles qui simplifient ou améliorent le travail de l'utilisateur. <br>
**Exemple :** « `IInAppMessageManagerListener` inclut également des méthodes déléguées pour les clics sur le message lui-même ou sur l'un des boutons. Un cas d'utilisation courant consiste à intercepter un message lorsqu'un bouton ou un message est cliqué pour un traitement ultérieur. »

##### Humain

La rédaction informative est par nature aride — nous voulons que les lecteurs se concentrent sur le contenu, pas sur la forme. Nous pouvons tout de même écrire d'une manière qui aide nos lecteurs à traiter l'information qu'ils consomment et qui augmente les chances qu'ils intériorisent les connaissances. Soyez humain, laissez transparaître votre personnalité et soyez mémorable.

* Visez un ton conversationnel plutôt que formel.
* Concentrez-vous sur l'utilisateur ; respectez sa situation et son état émotionnel.
* Centrez activement l'expérience humaine, pas l'état de la machine.

###### Directives

✅ Appliquez le ton et les éléments de la marque de manière réfléchie. <br>
**Exemple :** « L'intégration avec Braze est un processus qui en vaut la peine. Mais vous êtes malin. Vous êtes ici. De toute évidence, vous le savez déjà. »

✅ Appliquez les [bonnes pratiques d'accessibilité](#accessibility) pour le contenu visuel et textuel. <br>
**Exemple :** Remplacer des expressions idiomatiques comme « clé en main » par « par défaut » rend votre texte plus accessible aux personnes dont le français n'est pas la langue maternelle.

✅ Fournissez un accompagnement cohérent tout au long du parcours utilisateur. <br>
**Exemple :** Utilisez le framework Diátaxis pour vous assurer de répondre aux besoins de différents utilisateurs à différents moments.

#### Accessibilité {#accessibility}

Braze vise à offrir une expérience inclusive. Utilisez les directives suivantes pour vous assurer que votre contenu pédagogique est accessible au [milliard de personnes](https://www.who.int/en/news-room/fact-sheets/detail/disability-and-health) ayant un besoin d'accessibilité.

##### Général

* Évitez le langage biaisé ou capacitiste. Pour plus d'informations, consultez la section sur le [langage inclusif](#inclusive-language).
* Utilisez un [lecteur d'écran](https://support.apple.com/guide/mac-help/use-accessibility-features-mh35884/mac) pour tester votre contenu.
* N'utilisez pas d'[esperluette](#ampersands) (&) à la place de « et » sauf pour faire référence à des éléments d'interface qui utilisent une esperluette.

##### Langage et mise en forme

* Utilisez un [langage simple](https://www.plainlanguage.gov/guidelines/).
* Placez les informations les plus importantes en début de section. Utilisez le modèle journalistique de la [pyramide inversée](https://en.wikipedia.org/wiki/Inverted_pyramid_(journalism)).
* Aérez les blocs de texte pour aider les lecteurs à parcourir l'information. Utilisez des paragraphes, des [listes](#lists), des [encadrés](#callouts-and-alerts) et des [images](#figures-and-other-images) pour améliorer la lisibilité.
* [Rédigez des phrases et des paragraphes courts](https://www.usability.gov/how-to-and-tools/methods/writing-for-the-web.html). En règle générale, visez un maximum de 20 mots par phrase et cinq phrases par paragraphe.
* Évitez les acronymes et expressions latins, car ils peuvent être difficiles à traduire. Utilisez plutôt des mots ou expressions simples.

##### Titres

* Utilisez des [titres et en-têtes](#headings-and-titles) uniques, descriptifs et clairs.
* Utilisez un h1 pour les titres de page.
* Ne sautez pas de niveaux de titre. Un h3 doit suivre un h2, et ainsi de suite.

##### Liens

* N'utilisez pas de texte de lien comme « En savoir plus », « ici » ou « ce document ». Pour d'autres formulations à éviter, consultez la section [Rédiger des liens](#writing-links).
* Évitez de placer deux liens côte à côte dans une phrase. Insérez un caractère ou un mot entre eux pour les séparer.
* Les [liens de téléchargement de fichiers](#links-for-file-download) doivent indiquer que cliquer sur le lien télécharge le fichier, ainsi que le type de fichier (PDF, CSV, etc.)
* Si le contexte ne le rend pas évident, les liens vers des sections de la même page doivent utiliser une [formulation standard](#structuring-links) indiquant cette action.

##### Images, vidéos et GIF

* Fournissez un [texte alternatif](#alt-text) pour chaque image qui résume les informations présentées dans l'image.
* N'utilisez pas les images comme seul moyen de présenter des informations. Fournissez toujours les étapes, le contenu ou les autres détails présentés dans l'image dans le texte environnant.
* N'utilisez pas d'images de sortie de terminal, d'exemples de code ou de texte. Utilisez plutôt du texte réel.
* Fournissez des sous-titres pour le contenu vidéo.
* N'utilisez pas d'éléments clignotants dans les vidéos ou les GIF.

##### Tableaux {#tables-1}

* Utilisez toujours une phrase d'introduction pour décrire l'objectif du tableau.
* Évitez les tableaux au milieu d'une liste, en particulier d'une liste d'étapes.

#### Audience internationale {#global-audience}

Nous rédigeons notre contenu pédagogique en anglais américain. Cependant, Braze est une marque internationale et, à ce titre, nous écrivons pour une audience mondiale. Utilisez les directives suivantes pour vous assurer que les clients comprennent votre rédaction même lorsque l'anglais n'est pas leur langue maternelle.

1. **Rédigez en pensant à la localisation :**
  * Formatez les [dates et heures](#dates-and-times) de manière non ambiguë.
  * Ne superposez pas de texte sur les images, car ce texte ne peut pas être traduit.
  * Évitez l'[argot et les expressions idiomatiques](#slang-and-idioms).
  * Fournissez du contexte. Ne supposez pas que le lecteur sait de quoi vous parlez.
2. **Rédigez des phrases courtes et précises :**
  * Utilisez un [langage simple](https://www.plainlanguage.gov/guidelines/).
  * Définissez les [abréviations](#abbreviations).
  * Évitez les [pronoms ambigus](#ambiguous-pronouns). Si un pronom peut être ambigu, remplacez-le par le nom approprié.
3. **Soyez cohérent :**
  * Utilisez le même terme pour un concept dans toutes les mentions du terme, y compris la même capitalisation et la même mise en forme du texte.
  * Rédigez les phrases dans l'ordre sujet + verbe + complément.
  * Si des instructions dépendent d'une condition, placez la clause conditionnelle en premier. Pour plus d'informations, consultez [l'ordre des clauses](#clause-order).
4. **Soyez inclusif :**
  * Utilisez un [langage inclusif](#inclusive-language).
  * Utilisez des [noms d'exemple](#example-names) diversifiés.
  * Évitez l'humour culturellement spécifique.

#### Langage inclusif {#inclusive-language}

Nous sommes peut-être une entreprise B2B, mais les personnes sont au cœur de ce que nous faisons, et notre marque est internationale. Chaque fois que nous faisons référence à une personne dans notre contenu, nous veillons à être inclusifs et respectueux. En cas de doute, consultez cette section ou [The Diversity Style Guide](https://www.diversitystyleguide.com/).

##### Âge

Sauf si c'est pertinent pour votre rédaction, ne faites pas référence à l'âge d'un sujet. N'utilisez pas de qualificatifs comme « jeune » ou « vieux » pour décrire un sujet ou une audience.

Si vous représentez un groupe d'âge, soyez descriptif et précis comme « Génération Z » au lieu de « jeunesse ». N'utilisez pas de descripteurs vagues comme « en âge universitaire » quand vous pourriez dire « étudiants » à la place.

##### Couleur

Évitez d'inclure des termes de couleur dans votre rédaction sauf si c'est absolument nécessaire, et si c'est le cas, incluez un texte explicatif.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Appuyez sur ✅ Enregistrer.</td><td style="width: 50%;">Appuyez sur l'icône verte Enregistrer.</td></tr>
<tr><td style="width: 50%;">Appuyez sur l'icône de coche verte.</td><td style="width: 50%;">Appuyez sur l'icône verte à côté du bouton rouge Annuler.</td></tr>
<tr><td style="width: 50%;">Appuyez sur l'icône verte.</td><td style="width: 50%;"></td></tr>
</tbody>
</table>
{:/}

Ne vous fiez pas à la couleur comme seul indicateur pour les éléments interactifs. Par exemple, soulignez les liens au survol ou marquez un champ obligatoire avec un astérisque.

Évitez de vous fier uniquement au vert et au rouge pour les indicateurs « bon » et « mauvais » (ou, plus souvent, « à faire » et « à éviter »). Le daltonisme rouge/vert est le type le plus courant de daltonisme. Si vous utilisez la couleur pour communiquer des recommandations, assurez-vous d'inclure également d'autres textes ou symboles pour transmettre le même message.

##### Langage condescendant {#condescending-language}

Lorsque vous rédigez des instructions ou détaillez des étapes à suivre, évitez d'utiliser des mots ou expressions tels que :

* simple, comme « Créer une campagne est simple. »
* simplement, comme « ...ajoutez simplement X dans Y »
* juste, comme « ...installez juste X »
* « C'est facile »

Si quelqu'un rencontre des difficultés avec les étapes ou les instructions, vos descripteurs désinvoltes peuvent sembler condescendants. Vous pourriez aussi involontairement exclure des personnes de votre documentation qui interprètent cela comme un indicateur qu'elles ne sont pas suffisamment compétentes pour suivre vos instructions.

##### Clients versus consommateurs

Lorsque vous faites référence aux utilisateurs de l'entreprise et à leurs consommateurs, utilisez les termes suivants en conséquence :

* **Clients :** Les marques avec lesquelles nous travaillons. Ne faites jamais référence à nos clients comme des « clients » au sens de « clients d'un prestataire ».
 * **Utilisateurs de l'entreprise :** Dans le contexte de la documentation, lorsqu'il est important de distinguer les utilisateurs de la plateforme des utilisateurs finaux qui reçoivent les messages marketing, utilisez « utilisateurs de l'entreprise ».
* **Consommateurs :** Les clients d'une marque avec laquelle nous travaillons.
* **Utilisateurs :** Généralement réservé à une statistique spécifique qui dépend de métriques « utilisateur » (comme la « rétention des utilisateurs »). Lorsque vous faites référence aux « utilisateurs » dans notre contenu, essayez d'abord d'être plus précis. Pensez acheteurs, consommateurs, patients, joueurs.

##### Départements et équipes

Mettez en majuscule les noms des départements ou des équipes. Ne mettez pas en majuscule « équipe » ou « département ».

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Marketing, équipe Aide à la décision Produit</td><td style="width: 50%;">marketing, aide à la décision Équipe Produit</td></tr>
<tr><td style="width: 50%;">département Revenue</td><td style="width: 50%;">Département Revenue</td></tr>
</tbody>
</table>
{:/}

##### Handicap

Ne faites pas référence au handicap d'une personne sauf si c'est spécifiquement pertinent pour votre rédaction. Dans ce cas, soyez respectueux et demandez si le sujet préfère un langage centré sur l'identité ou centré sur la personne. Lorsque vous faites référence à un sujet en situation de handicap, n'utilisez pas de termes comme « handicapé » de manière péjorative.

Le langage capacitiste inclut des mots ou expressions tels que « fou », « insensé », « aveugle à » ou « fermer les yeux sur », « estropier », « idiot », et d'autres. Choisissez des mots alternatifs selon le contexte.

##### Maladie

Lorsque vous décrivez une maladie, évitez des mots comme « souffrir », « lutter » ou « victime ». Visez un ton neutre et factuel.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">À faire</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">On lui a diagnostiqué un cancer.</td></tr>
<tr><td style="width: 100%;">Cette personne vit avec le VIH.</td></tr>
<tr><td style="width: 100%;">Il s'est remis de son AVC.</td></tr>
</tbody>
</table>
{:/}


##### Inclusivité dans le contenu

Mettez en valeur et représentez une communauté diversifiée. Soyez attentif et inclusif lorsque vous impliquez nos clients, intervenants, experts du secteur et membres de l'équipe Braze.

##### Titres de poste

En ce qui concerne les titres de poste, nous nous écartons du style AP. Dans tous les cas, nous mettons en majuscule les titres de poste lorsque nous faisons référence à quelqu'un en particulier.

###### Titre de poste avec nom d'entreprise

Mettez en majuscule les titres de poste formels lorsqu'ils précèdent ou suivent le nom d'une personne. Nous les formatons de trois manières :

1. **[Titre formel]** chez **[Nom de l'entreprise]** + **[Nom complet]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Creative Director chez PantsLabyrinth David Bowie</td><td style="width: 50%;">creative director chez PantsLabyrinth David Bowie</td></tr>
</tbody>
</table>
{:/}

{: start="2"}
2. **[Nom complet]** + virgule + **[Titre formel]** chez **[Nom de l'entreprise]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">David Bowie, Creative Director chez PantsLabyrinth</td><td style="width: 50%;">David Bowie, creative director chez PantsLabyrinth</td></tr>
</tbody>
</table>
{:/}

{: start="3"}
3. **[Nom de l'entreprise]** + **[Titre formel]** + **[Nom complet]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">PantsLabyrinth Creative Director David Bowie</td><td style="width: 50%;">PantsLabyrinth creative director David Bowie</td></tr>
</tbody>
</table>
{:/}

###### Titre de poste sans nom d'entreprise

Lorsque vous faites référence à une personne spécifique par son titre formel, mettez en majuscule son titre formel et son nom comme suit :

1. **[Titre formel]** + **[Nom complet]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">CEO Robin Fenty</td><td style="width: 50%;">Chief executive officer Robyn Fenty</td></tr>
</tbody>
</table>
{:/}

{: start="2"}
2. **[Titre formel]** + virgule + **[Nom complet]**

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">SVP, Product, Robin Fenty</td><td style="width: 50%;">senior vice president, product, Robyn Fenty</td></tr>
</tbody>
</table>
{:/}

###### Autres cas

Les titres formels sont « chez [ENTREPRISE] ». Les fondateurs et cofondateurs sont « de [ENTREPRISE] ». Les titres formels et les professions utilisés seuls n'ont pas besoin d'être en majuscule.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">J'ai écrit à leur chief data officer.</td><td style="width: 50%;">J'ai écrit à leur Chief Data Officer.</td></tr>
<tr><td style="width: 50%;">Nous avons parlé avec plusieurs analystes en aide à la décision.</td><td style="width: 50%;">Nous avons parlé avec plusieurs Analystes en Aide à la Décision.</td></tr>
<tr><td style="width: 50%;">Contactez votre Account Manager Braze.</td><td style="width: 50%;">J'ai écrit à leur Chief Data Officer. Contactez votre Account Manager Braze.</td></tr>
</tbody>
</table>
{:/}

Utilisez des titres de poste non genrés, sauf si le genre a déjà été établi.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">commercial(e)</td><td style="width: 50%;">vendeur/vendeuse</td></tr>
</tbody>
</table>
{:/}

Abrégez les titres lorsque c'est approprié, comme VP ou SVP, si c'est ainsi que la personne se réfère à son titre. En cas d'espace limité, les abréviations standard (VP, SVP, Sr., ou Jr.) sont acceptables.

##### Genre

Ne faites pas de suppositions sur le genre des personnes. Demandez aux sujets qui apparaissent dans votre contenu comment ils s'identifient.

Lorsque vous faites référence à des membres de la communauté, « queer » est acceptable. « Gay » ne l'est pas. Vous pouvez faire référence à un groupe de personnes comme « LGBTQ ». N'utilisez pas ce terme pour décrire un individu.

Lorsque vous vous adressez à des groupes de personnes dans votre contenu, évitez de genrer votre audience (exemple : « OK, mesdames ! »). Utilisez des expressions non genrées à la place (exemple : « Allons-y, tout le monde ! »).

« Ils/elles » est toujours acceptable comme pronom singulier ou pluriel dans tout notre contenu.

##### Santé mentale

La santé mentale et les maladies mentales couvrent un large éventail de conditions. Sauf si c'est pertinent pour ce que vous écrivez, ne faites pas référence à la santé mentale d'une personne. Évitez les mots et expressions stigmatisants. N'utilisez pas de termes médicaux de manière familière (exemple : « L'état déprimant des choses... »).

##### Noms

La première fois que vous mentionnez une personne, utilisez son prénom et son nom complet. Par la suite, utilisez soit son prénom, soit son nom de famille pour y faire référence.

##### Pronoms

Pour des informations sur l'utilisation appropriée des pronoms, consultez la section Langage et grammaire sur les [Pronoms](#pronouns).

##### Race, religion et ethnicité

Ne faites pas référence à la race, la religion ou l'ethnicité d'une personne sauf si c'est pertinent pour ce que vous écrivez. Dans les écrits où la race ou l'ethnicité entre en jeu, demandez à votre sujet comment il s'identifie.

N'utilisez pas de trait d'union pour indiquer une double appartenance ou religion. Utilisez plutôt un espace.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Muslim American</td><td style="width: 50%;">Muslim-American</td></tr>
<tr><td style="width: 50%;">Cuban American</td><td style="width: 50%;">Cuban-american</td></tr>
</tbody>
</table>
{:/}

Mettez en majuscule les noms propres des ethnicités, nationalités, peuples et tribus.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Cambodgien</td><td style="width: 50%;">cambodgien</td></tr>
<tr><td style="width: 50%;">Afro-Américains</td><td style="width: 50%;">afro-américains</td></tr>
</tbody>
</table>
{:/}

Mettez en majuscule les noms des religions ou des termes religieux.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Foi bahá'íe</td><td style="width: 50%;">foi bahá'íe</td></tr>
<tr><td style="width: 50%;">Bouddhiste</td><td style="width: 50%;">bouddhiste</td></tr>
</tbody>
</table>
{:/}

Ne vous appropriez pas des mots ou des expressions appartenant à l'anglais vernaculaire afro-américain (on fleek, bae, lit, woke).

Ne vous appropriez pas des mots ou des expressions spécifiques aux peuples autochtones (exemple : animal totem, pow-wow).

#### Sources tierces {#third-party-sources}

Ne copiez jamais le contenu d'autres sites, car cela peut violer les droits d'auteur. Le contenu peut être à la fois du texte et des images.

Au lieu de copier ou de citer des sites tiers, reformulez le contenu ou fournissez un lien vers le site tiers pour plus d'informations. Pour plus d'informations, consultez [Liens vers d'autres sites](#links-to-other-sites).

### Langage et grammaire {#language-and-grammar}

Respecter les règles de grammaire et de mécanique convenues nous aide à garder notre rédaction claire et cohérente. Cette section couvre ce que nous essayons de suivre dans notre documentation technique, sauf indication contraire.

#### Abréviations {#abbreviations}

Les abréviations, telles que les acronymes, les sigles et les mots raccourcis, peuvent nuire à notre clarté, notre voix et notre référencement.

Bien que certaines abréviations soient largement comprises, d'autres ne sont pas bien connues ou ne sont familières qu'à un groupe spécifique de clients. Faites preuve de discernement et, en règle générale, il est acceptable de ne pas développer une abréviation si elle est répertoriée dans le [American Heritage Dictionary](https://ahdictionary.com/).

Si une abréviation n'est pas bien connue, développez-la à la première mention, suivie de l'abréviation entre parenthèses. Pour toutes les mentions suivantes du terme, utilisez l'abréviation.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire : <em>Développer les abréviations peu courantes à la première mention</em></th><th style="width: 50%;">À éviter : <em>Développer les abréviations courantes</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Domaine de premier niveau (TLD)</td><td style="width: 50%;">Portable Document Format (PDF)</td></tr>
<tr><td style="width: 50%;">Identifiant universellement unique (UUID)</td><td style="width: 50%;">Universal Serial Bus (USB)</td></tr>
</tbody>
</table>
{:/}


Traitez les abréviations comme des mots ordinaires lorsque vous les mettez au pluriel, et n'ajoutez pas d'apostrophe — par exemple, API et SDK. La même règle s'applique pour l'article (un ou une) que vous utilisez — regardez comment vous prononcez l'abréviation. Lorsqu'une abréviation commence par un son vocalique, utilisez « un » ou « une » selon le genre ; pour les sons consonantiques, faites de même.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">À faire : <em>Utiliser les articles en fonction de la prononciation de l'abréviation</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">un ISP</td></tr>
<tr><td style="width: 100%;">une DLL</td></tr>
<tr><td style="width: 100%;">un site HTML</td></tr>
<tr><td style="width: 100%;">un fichier CSV</td></tr>
</tbody>
</table>
{:/}

#### Voix active {#active-voice}

Chez Braze, nous utilisons la voix active autant que possible. La voix active est notre référence. Évitez la voix passive, dans laquelle il peut être difficile de déterminer qui ou quoi effectue une action particulière.

Pour vérifier si votre phrase est à la voix passive, insérez « par quelqu'un » après le verbe. Si la phrase a du sens, elle est très probablement à la voix passive.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire : <em>Utiliser la voix active</em></th><th style="width: 50%;">À éviter : <em>Utiliser la voix passive, si possible</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Braze connecte les consommateurs aux marques qu'ils aiment.</td><td style="width: 50%;">Les consommateurs sont connectés aux marques qu'ils aiment.</td></tr>
<tr><td style="width: 50%;">Braze exige que les employés maintiennent leurs adresses à jour.</td><td style="width: 50%;">Les employés sont tenus de maintenir leurs adresses à jour.</td></tr>
<tr><td style="width: 50%;">Les administrateurs de l'entreprise peuvent configurer les exigences d'authentification pour se connecter à Braze.</td><td style="width: 50%;">Les exigences d'authentification pour se connecter à Braze peuvent être configurées par les administrateurs de l'entreprise.</td></tr>
</tbody>
</table>
{:/}

##### Exceptions

Il est acceptable d'utiliser la voix passive dans les cas suivants :

* Pour atténuer la responsabilité d'un sujet, généralement pour éviter de blâmer le lecteur :
  - **À faire :** Deux erreurs ont été trouvées dans l'e-mail.
  - **À éviter :** Vous avez créé deux erreurs dans l'e-mail.
* Si savoir qui est responsable de l'action n'est pas important :
  - **À faire :** Cet article a été mis à jour pour la dernière fois en décembre 2020.

#### Articles {#articles}

Utilisez les articles « un », « une » et « le/la/les » pour rendre votre rédaction claire et faciliter la traduction. Utilisez « le/la/les » avant un nom singulier ou pluriel spécifique, et « un » ou « une » avant un nom singulier non spécifique.

Pour déterminer si vous devez utiliser « un » ou « une », regardez le genre du nom qui suit. Les mêmes directives s'appliquent aux [abréviations](#abbreviations).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">À faire : <em>Utiliser les articles en fonction du genre et de la prononciation du mot qui suit.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">une heure</td></tr>
<tr><td style="width: 100%;">une minute</td></tr>
<tr><td style="width: 100%;">un article FAQ</td></tr>
<tr><td style="width: 100%;">un cours LAB</td></tr>
</tbody>
</table>
{:/}

#### Pronoms {#pronouns}

##### Pronoms personnels

Utilisez les pronoms de la deuxième personne (vous) autant que possible.

Ne faites pas référence aux clients de Braze comme « l'utilisateur » dans les écrits destinés au public ; adressez-vous plutôt directement au lecteur en utilisant « vous ». Pour faire référence aux clients de nos clients, utilisez « vos consommateurs » ou, si la situation concerne des statistiques utilisateur, « vos utilisateurs ».

Évitez les pronoms de la première personne (je, nous, notre) sauf dans les cas suivants :

* Entrées dans les FAQ. Par exemple, « Comment réinitialiser mon mot de passe ? ».
* Utilisation de « nous » pour faire référence à Braze en tant qu'organisation.
 * S'il n'est pas clair à qui « nous » fait référence, faites d'abord référence à Braze par son nom, puis utilisez « nous » dans les mentions suivantes.

##### Pronoms non genrés

Utilisez les pronoms que vos sujets utilisent. En cas d'incertitude, utilisez des formulations non genrées ou le pronom « ils/elles » au singulier. N'utilisez pas « il/elle » comme alternative.

N'utilisez des pronoms genrés (il/elle, lui/elle, son/sa) que si la personne à laquelle vous faites référence est effectivement de ce genre.

##### Pronoms ambigus {#ambiguous-pronouns}

Les pronoms remplacent les noms. Le mot auquel un pronom fait référence est appelé son antécédent. Lorsque vous rédigez des instructions ou du matériel pédagogique, assurez-vous de faire des références claires entre un pronom et son antécédent. Cela peut nécessiter de répéter les sujets pour clarifier le sens.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire : <em>S'assurer qu'un pronom fait clairement référence à son antécédent</em></th><th style="width: 50%;">À éviter : <em>Utiliser des références pronominales ambiguës</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Si vous saisissez du texte dans le champ, le texte ne change pas.</td><td style="width: 50%;">Si vous saisissez du texte dans le champ, il ne change pas.</td></tr>
<tr><td style="width: 50%;">Elle a dit à Sarah que la réponse de Sarah était incorrecte.</td><td style="width: 50%;">Elle a dit à Sarah que sa réponse était incorrecte.</td></tr>
<tr><td style="width: 50%;">Vous ne pouvez pas modifier une campagne archivée. Désarchivez une campagne pour la modifier.</td><td style="width: 50%;">Vous ne pouvez pas modifier une campagne archivée. Désarchivez-la pour la modifier.</td></tr>
</tbody>
</table>
{:/}

##### Pronoms facultatifs

Pour ajouter de la clarté à votre rédaction et faciliter la localisation, utilisez des pronoms relatifs tels que « qui », « que » et « lequel/laquelle ».

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire : <em>Utiliser « qui », « que » et « lequel » pour ajouter de la clarté.</em></th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Faites un clic droit sur le lien que vous souhaitez ouvrir.</td><td style="width: 50%;">Faites un clic droit sur le lien à ouvrir.</td></tr>
<tr><td style="width: 50%;">À partir de là, vous pouvez choisir la cohorte Tinyclues que vous souhaitez inclure.</td><td style="width: 50%;">À partir de là, vous pouvez choisir une cohorte Tinyclues à inclure.</td></tr>
</tbody>
</table>
{:/}

#### Majuscules {#capitalization}

Évitez les majuscules inutiles. Dans la plupart des cas, utilisez la casse de phrase. La casse de titre ne doit être utilisée que pour les noms propres ou les noms de fonctionnalités.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire : <em>Utiliser les minuscules pour les URL de sites web et les adresses e-mail</em></th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">www.braze.com/docs</td><td style="width: 50%;">www.Braze.com/docs</td></tr>
<tr><td style="width: 50%;">sample@email.com</td><td style="width: 50%;">SAMPLE@EMAIL.COM</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire : <em>Utiliser les minuscules pour les directions</em></th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">nord, sud, est, ouest</td><td style="width: 50%;">Nord, Sud, Est, Ouest</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire : <em>Mettre en majuscule les régions spécifiques et utiliser les majuscules pour les régions abrégées</em></th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">le Nord-Ouest</td><td style="width: 50%;">le nord-ouest</td></tr>
<tr><td style="width: 50%;">le sud du Connecticut</td><td style="width: 50%;">le Sud du Connecticut</td></tr>
<tr><td style="width: 50%;">l'Europe de l'Est</td><td style="width: 50%;">l'europe de l'est</td></tr>
<tr><td style="width: 50%;">APAC, EMEA</td><td style="width: 50%;">Apac, emea</td></tr>
</tbody>
</table>
{:/}

##### Marques et produits

Lorsque vous faites référence à une marque ou un produit, utilisez la capitalisation utilisée par la marque. Dans la plupart des cas, mettez en majuscule les noms des marques (Grindr, Walmart) et des produits (Benchmarks, Looker Blocks). Il est acceptable de commencer une phrase par une minuscule si le premier mot est le nom stylisé d'une marque comme eBay ou iTunes.

Pour les intercaps, référez-vous toujours à l'usage préféré par la marque à l'écrit (OkCupid, YouTube). N'utilisez pas les intercaps qui n'apparaissent que dans les logos ou les traitements graphiques (Amazon).

#### Ordre des clauses {#clause-order}

Si vous souhaitez dire au lecteur de faire quelque chose dans une circonstance spécifique, essayez de mentionner la circonstance avant de fournir l'instruction. Cela permet au lecteur de sauter l'instruction si la circonstance ne s'applique pas.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Pour les étapes de résolution des problèmes, consultez la FAQ des campagnes.</td><td style="width: 50%;">Consultez la FAQ des campagnes pour les étapes de résolution des problèmes.</td></tr>
<tr><td style="width: 50%;">Pour archiver votre campagne, cliquez sur l'icône d'engrenage et sélectionnez Archiver.</td><td style="width: 50%;">Cliquez sur l'icône d'engrenage et sélectionnez Archiver pour archiver votre campagne.</td></tr>
</tbody>
</table>
{:/}

#### Formes composées {#combining-forms}

[Utilisez un trait d'union](#hyphens) pour les formes composées lorsque l'expression est utilisée comme adjectif avant le nom.

**Exemple :** Un article unique en son genre

#### Contractions {#contractions}

Une contraction est une version raccourcie d'un mot ou d'une expression. En français, les contractions sont naturelles et courantes (l'article, j'ai, c'est, etc.). Utilisez-les pour maintenir un ton accessible et informel. Cependant, évitez les contractions qui pourraient nuire à la clarté ou à la compréhension de la phrase.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire : <em>Utiliser les contractions naturelles</em></th><th style="width: 50%;">À éviter : <em>Utiliser des contractions qui nuisent à la clarté</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Si vous êtes administrateur, vous pouvez gérer les coordonnées de votre entreprise.</td><td style="width: 50%;">Braze prendra désormais en charge l'intégration Shoptify.</td></tr>
<tr><td style="width: 50%;">Vous ne pouvez pas modifier une campagne archivée.</td><td style="width: 50%;">Vous n'auriez peut-être pas vu la taille de téléchargement restreinte.</td></tr>
</tbody>
</table>
{:/}

#### Modificateurs mal placés et sans antécédent {#dangling-and-misplaced-modifiers}

Les modificateurs sont des mots ou des expressions qui modifient d'autres mots ou expressions. Un modificateur sans antécédent ne modifie aucun sujet dans la phrase. Un modificateur mal placé est éloigné du sujet qu'il est censé modifier. Essentiellement, les modificateurs mal placés et sans antécédent peuvent créer de la confusion en se rattachant à la mauvaise partie de la phrase.

Écrire à la voix active aide à prévenir l'utilisation de modificateurs mal placés et sans antécédent. Assurez-vous d'utiliser un modificateur qui modifie clairement son sujet.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire : <em>Garder les phrases courtes et concises. Utiliser la voix active.</em></th><th style="width: 50%;">À éviter : <em>Utiliser des phrases longues avec des modificateurs pouvant créer de la confusion</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Les clients doivent configurer leurs paramètres SAML.</td><td style="width: 50%;">Vous avez peut-être des messages de test dans vos campagnes qui peuvent être supprimés.</td></tr>
<tr><td style="width: 50%;">Assurez-vous d'enregistrer vos brouillons de campagne.</td><td style="width: 50%;">En rentrant chez elle, Sarah a trouvé un chronomètre en or d'homme.</td></tr>
</tbody>
</table>
{:/}

#### Prépositions {#prepositions}

Il n'y a rien de mal à terminer une phrase par une préposition lorsque cela améliore la lisibilité. Placez une préposition ou un groupe prépositionnel là où cela a le plus de sens dans une phrase. Si vous avez des difficultés, lisez la phrase à voix haute et voyez si elle sonne naturellement.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Chaque option correspond à la priorité dans laquelle la notification apparaît.</td><td style="width: 50%;">Chaque option correspond à la priorité à laquelle la notification apparaît dans l'ordre.</td></tr>
<tr><td style="width: 50%;">Pour plus de détails, consultez la documentation du SDK pour la plateforme avec laquelle vous travaillez.</td><td style="width: 50%;">Pour plus de détails, consultez la documentation du SDK pour la plateforme sur laquelle vous êtes en train de travailler actuellement.</td></tr>
</tbody>
</table>
{:/}

#### Présent {#present-tense}

Utilisez le présent au lieu du futur. Le présent transmet l'immédiateté et démontre la confiance. Évitez d'utiliser le futur ou le conditionnel, en particulier lorsque vous faites référence au résultat d'une action de l'utilisateur.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Les groupes d'abonnement archivés ne peuvent pas être modifiés et n'apparaissent plus dans les filtres de segments.</td><td style="width: 50%;">Les groupes d'abonnement archivés ne pourront pas être modifiés et n'apparaîtront plus dans les filtres de segments.</td></tr>
<tr><td style="width: 50%;">L'utilisation d'un code court est le type de numéro le plus fiable pour inclure des liens.</td><td style="width: 50%;">L'utilisation d'un code court serait le type de numéro le plus fiable pour inclure des liens.</td></tr>
</tbody>
</table>
{:/}

N'utilisez le futur que lorsque vous parlez réellement de l'avenir. Évitez de prédire des [fonctionnalités futures](#describing-limitations).

#### Vulgarité {#profanity}

Restez correct. Cela a moins à voir avec la moralité qu'avec le fait que la vulgarité peut être clivante et rebutante pour une audience aussi large et internationale que la nôtre. On peut aussi argumenter que la vulgarité masque parfois une rédaction bâclée. Ce n'est tout simplement pas notre style.

#### Pluriels entre parenthèses {#plurals-in-parentheses}

N'utilisez pas de pluriels entre parenthèses. Utilisez plutôt la forme plurielle ou singulière du mot.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Personnalisez votre campagne avec les filtres suivants.</td><td style="width: 50%;">Personnalisez votre campagne avec le(s) filtre(s) suivant(s).</td></tr>
</tbody>
</table>
{:/}

#### Deuxième personne et première personne {#second-person-and-first-person}

Utilisez la deuxième personne dans vos instructions au lieu de la première personne — « vous » plutôt que « nous ».

Adressez-vous au lecteur comme étant celui qui effectue l'action. Adoptez un ton conversationnel — la plupart des lecteurs consultent la documentation lorsqu'ils n'ont pas accès immédiatement à un agent de support. Faites en sorte que l'article s'adresse directement à eux.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Si vous souhaitez ajouter une variante...</td><td style="width: 50%;">Si nous souhaitons ajouter une variante...</td></tr>
</tbody>
</table>
{:/}

Si vous demandez au lecteur de faire quelque chose, vous pouvez omettre le « vous » et utiliser l'impératif.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Téléchargez le fichier CSV.</td><td style="width: 50%;">Vous pouvez télécharger le fichier CSV.</td></tr>
<tr><td style="width: 50%;">Sélectionnez Soumettre.</td><td style="width: 50%;">Vous devrez sélectionner Soumettre.</td></tr>
</tbody>
</table>
{:/}

Lorsque vous utilisez la deuxième personne, assurez-vous de savoir qui est l'audience du document et soyez cohérent quant à la personne à laquelle vous vous adressez.

#### Argot et expressions idiomatiques {#slang-and-idioms}

Nous parlons simplement. Évitez d'utiliser de l'argot tendance ou des expressions idiomatiques qui s'adressent trop spécifiquement à une audience unique. Cela peut aussi rapidement dater les contenus et rendre difficile la localisation.

#### Orthographe {#spelling}

Utilisez l'orthographe de l'anglais américain pour les mots qui diffèrent en anglais britannique. Si vous n'êtes pas sûr de l'orthographe d'un mot, consultez d'abord le [Glossaire](#glossary). Si le mot n'y figure pas, consultez le [Merriam-Webster's Collegiate Dictionary](https://www.merriam-webster.com/).

Pour les mots accentués ou contenant des caractères spéciaux, assurez-vous de suivre correctement l'orthographe du dictionnaire. Dans certains cas, omettre involontairement ces accents peut donner un mot différent. Par exemple, « resume » signifie reprendre après un arrêt, tandis que « résumé » est un compte rendu de ses qualifications.

### Ponctuation {#punctuation}

#### Esperluettes {#ampersands}

N'utilisez pas d'esperluette (&) à la place de « et » dans le texte ou les titres, sauf si vous faites directement référence à l'interface utilisateur.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Éditeur par glisser-déposer</td><td style="width: 50%;">Éditeur Drag & Drop</td></tr>
<tr><td style="width: 50%;">SMS et MMS</td><td style="width: 50%;">SMS & MMS</td></tr>
</tbody>
</table>
{:/}

#### Apostrophes {#apostrophes}

En français, l'apostrophe est principalement utilisée pour l'élision (l'article, l'homme, j'ai). Suivez les règles standard de la grammaire française pour l'utilisation des apostrophes.

#### Deux-points {#colons}

Utilisez les deux-points à la fin d'une phrase d'introduction qui précède une liste ou un exemple. Votre phrase d'introduction doit pouvoir se suffire à elle-même en tant que phrase complète. Cela est important à la fois pour l'accessibilité et la localisation, car il est difficile de traduire des fragments de phrase.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">La structure générale est la suivante :</td><td style="width: 50%;">La structure générale est :</td></tr>
</tbody>
</table>
{:/}

Si le texte précédant les deux-points est en gras, mettez également les deux-points en gras.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><strong>Planification :</strong> Entrée basée sur le temps.</td><td style="width: 50%;"><strong>Planification</strong> : Entrée basée sur le temps.</td></tr>
</tbody>
</table>
{:/}

Si le texte précédant les deux-points est du texte de code, n'incluez pas les deux-points dans le texte de code, sauf s'ils font partie de l'élément de code.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>user_alias_label</code> : Un libellé commun pour regrouper les alias d'utilisateur.</td><td style="width: 50%;"><code>user_alias_label:</code> Un libellé commun pour regrouper les alias d'utilisateur.</td></tr>
</tbody>
</table>
{:/}

Vous pouvez également utiliser les deux-points pour relier deux phrases liées dans une phrase. Cependant, utilisez les deux-points avec parcimonie dans ce cas. Deux phrases séparées sont généralement plus lisibles.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">À faire</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">La semaine prochaine : nous partons en visite du West Village.</td></tr>
</tbody>
</table>
{:/}


#### Virgules {#commas}

Braze utilise la virgule d'Oxford (virgule de série) lors de la rédaction d'instructions ou de contenu pédagogique. Utilisez une virgule avant la dernière conjonction pour séparer les éléments d'une série.

Utilisez une virgule après une phrase d'introduction.

Si une conjonction de coordination (des mots comme « et », « mais », « ou », « pourtant », « donc ») sépare deux propositions indépendantes, placez la virgule après la première proposition et avant la conjonction. Cependant, cette virgule n'est pas nécessaire si les deux propositions sont courtes.

Par exemple, voici deux propositions indépendantes :

* « Tous les champs sont facultatifs. »
* « Vous devez spécifier au moins un champ. »

La phrase avec la conjonction de coordination « mais » est : « Tous les champs sont facultatifs, mais vous devez spécifier au moins un champ. »

Si une proposition indépendante et une proposition dépendante sont utilisées dans la même phrase, n'utilisez pas de virgule pour les séparer. N'utilisez une virgule dans ce scénario que si la phrase peut être mal interprétée sans la virgule.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Les états d'abonnement push sont des filtres et peuvent permettre aux utilisateurs de modifier les préférences de notification.</td><td style="width: 50%;">Les états d'abonnement push sont des filtres, et peuvent permettre aux utilisateurs de modifier les préférences de notification.</td></tr>
</tbody>
</table>
{:/}

#### Tirets {#dashes}

##### Tiret cadratin

Utilisez un tiret cadratin (—) lorsque vous utilisez un tiret dans une phrase pour indiquer une pensée séparée ou une interruption. Ne mettez pas d'espaces avant ou après le tiret cadratin. N'utilisez pas de tiret cadratin là où une virgule ou des parenthèses fonctionneraient tout aussi bien.

Consultez votre système d'exploitation pour savoir comment saisir un tiret cadratin :

* **macOS :** Appuyez sur Option + Maj + Tiret.
* **Windows :** Activez le verrouillage numérique, puis maintenez la touche Alt gauche enfoncée et tapez 0151 sur le pavé numérique.

##### Tiret demi-cadratin {#en-dash}

Utilisez un tiret demi-cadratin (–) pour indiquer une plage de nombres, comme signe moins ou pour indiquer des nombres négatifs. Ne mettez pas d'espaces avant ou après le tiret demi-cadratin, sauf lorsqu'il est utilisé comme signe moins. N'utilisez pas de trait d'union (-).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire : <em>Utiliser un tiret demi-cadratin pour une plage de nombres</em></th><th style="width: 50%;">À éviter : <em>Utiliser un trait d'union</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">2018–2021</td><td style="width: 50%;">2018-2021</td></tr>
</tbody>
</table>
{:/}

N'utilisez pas de tiret demi-cadratin pour les plages horaires. Pour plus de détails, consultez la section [Dates et heures](#dates-and-times).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire : <em>Utiliser un tiret demi-cadratin comme signe moins et inclure des espaces autour du tiret demi-cadratin</em></th><th style="width: 50%;">À éviter : <em>Utiliser un trait d'union</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">15 – 5 = 10</td><td style="width: 50%;">15-5=10</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire : <em>Utiliser un tiret demi-cadratin pour les nombres négatifs</em></th><th style="width: 50%;">À éviter : <em>Utiliser un trait d'union</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">–30</td><td style="width: 50%;">-30</td></tr>
</tbody>
</table>
{:/}

Consultez votre système d'exploitation pour savoir comment saisir un tiret demi-cadratin :

* **macOS :** Appuyez sur Option + Tiret.
* **Windows :** Activez le verrouillage numérique, puis maintenez la touche Alt gauche enfoncée et tapez 0150 sur le pavé numérique.

#### Points de suspension {#ellipses}

Un point de suspension est une série de trois points (...) qui indique l'omission d'un ou plusieurs mots. En général, évitez d'utiliser des points de suspension lors de la rédaction d'instructions ou de contenu pédagogique.

#### Points d'exclamation {#exclamation-points}

Un point d'exclamation peut être utilisé avec parcimonie pour un ton informel. Cependant, évitez d'abuser des points d'exclamation dans le texte. Envisagez plutôt d'utiliser des [encadrés](#callouts-and-alerts).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire : <em>Utiliser les points d'exclamation pour un ton informel pour les rappels et les introductions</em></th><th style="width: 50%;">À éviter : <em>Utiliser les points d'exclamation pour indiquer un avertissement ou une mise en garde</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">N'oubliez pas d'enregistrer vos modifications avant de quitter la page !</td><td style="width: 50%;">Les utilisateurs doivent recevoir un ou plusieurs messages d'une étape pour être comptés comme destinataire unique !</td></tr>
</tbody>
</table>
{:/}

#### Traits d'union {#hyphens}

Les traits d'union peuvent aider le lecteur à gagner en clarté dans une phrase en reliant les mots d'une expression. Voici quelques directives pour bien les utiliser.

Utilisez des traits d'union pour les modificateurs composés qui aident le lecteur à mieux comprendre le sujet.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">À faire</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">streaming de données en temps réel</td></tr>
</tbody>
</table>
{:/}

Utilisez des traits d'union pour relier une expression, avec un espace entre le modificateur et le sujet.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">À faire</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Solutions tout-en-un</td></tr>
</tbody>
</table>
{:/}

Utilisez des traits d'union pour une expression qui modifie un sujet. Il n'est pas nécessaire d'utiliser un trait d'union si l'expression est le sujet.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">C'était un fait bien connu.</td><td style="width: 50%;">Ce fait est bien-connu.</td></tr>
</tbody>
</table>
{:/}

N'utilisez pas de traits d'union à la place d'un tiret cadratin pour créer une pause dans une phrase.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">...intégrations tierces—comme Slack—et automatiser...</td><td style="width: 50%;">...intégrations tierces-comme Slack-et automatiser...</td></tr>
</tbody>
</table>
{:/}

N'utilisez pas de trait d'union après un adverbe. Gardez les mots séparés.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Fait à la hâte</td><td style="width: 50%;">Fait-à-la-hâte</td></tr>
</tbody>
</table>
{:/}

#### Parenthèses {#parentheses}

Utilisez les parenthèses avec parcimonie. Ne mettez jamais d'informations importantes entre parenthèses, car certains lecteurs sautent le contenu entre parenthèses.

Pour les parenthèses moins importantes, envisagez de reformuler la phrase pour supprimer les parenthèses. Par exemple, vous pouvez isoler l'expression ou la phrase en utilisant des virgules, des tirets, des points-virgules ou en ajoutant une nouvelle phrase.

Si les parenthèses font partie d'une phrase plus longue, placez le point à l'extérieur de la parenthèse. Si les parenthèses contiennent une phrase complète, placez le point à l'intérieur.

**Section connexe :** [Pluriels entre parenthèses](#plurals-in-parentheses)

#### Points {#periods}

Utilisez un point pour terminer les phrases. N'utilisez pas de point pour terminer les titres, les en-têtes, les sous-titres ou les éléments d'interface.

Pour les directives sur l'utilisation des points avec les éléments de liste, consultez [Listes](#lists).

#### Points-virgules {#semicolons}

Les points-virgules sont utiles pour scinder une phrase plus longue et plus complexe. Utilisez un point-virgule pour séparer deux propositions indépendantes étroitement liées par le sujet.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">À faire : <em>Utiliser un point-virgule pour scinder une phrase avec deux propositions indépendantes liées</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Le chat a dormi pendant l'orage ; le chien s'est réfugié sous le lit.</td></tr>
</tbody>
</table>
{:/}

Les points-virgules peuvent être utilisés pour séparer les éléments d'une liste si un (ou plusieurs) des éléments contient une virgule.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">À faire : <em>Utiliser un point-virgule pour scinder une phrase plus longue</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Jane Lang, notre modératrice ; Simon Mayer, CEO et cofondateur de PantsLabyrinth ; et Kara Seberg, CMO de Yachtr.</td></tr>
</tbody>
</table>
{:/}

#### Barres obliques {#slashes}

Il existe deux types de barres obliques : inversée (\\) et normale (/). N'utilisez pas de barres obliques pour indiquer des mots ou exemples alternatifs (« et/ou »).

Utilisez les barres obliques selon les besoins dans les chemins de fichiers et les URL.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire : <em>Utiliser une barre oblique pour les chemins de fichiers</em></th><th style="width: 50%;">À éviter : <em>Utiliser une barre oblique pour séparer des alternatives</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;"><code>/campaigns/data_series</code></td><td style="width: 50%;">vous/vos clients</td></tr>
</tbody>
</table>
{:/}

#### Guillemets {#quotation-marks}

Il existe deux types de guillemets : droits (" ") et typographiques (« »). En français, utilisez les guillemets français (« ») pour les citations et les chaînes de texte. Les points et les virgules se placent à l'extérieur des guillemets. Une exception est lorsque les guillemets incluent des informations exactes comme une chaîne de caractères. Utilisez des guillemets lorsque vous demandez aux utilisateurs de saisir une chaîne de texte spécifique dans un champ de texte.

{% alert note %}

Lorsque vous décrivez la syntaxe de recherche, les guillemets sont souvent utilisés pour signifier la recherche de texte exact. Dans ce cas, utilisez des crochets autour de la chaîne de texte et des guillemets comme requis par la syntaxe de recherche. Par exemple : <br><br>

*Mettez des guillemets autour de tout mot ou expression, comme ["segment d'essai"], et nous affichons les résultats contenant uniquement ces mots ou expressions exacts.*

{% endalert %}

Les exemples de code doivent utiliser des guillemets droits. Pour plus d'informations sur la mise en forme du code dans le texte, consultez [Code dans le texte](#code-in-text).

### Documentation technique {#technical-documentation}

#### Endpoints API {#api-endpoints}

En général, la documentation des endpoints API doit suivre les directives de ce guide de style. Cependant, il existe des sujets spécifiques qui peuvent nécessiter des directives de contenu différentes répertoriées dans ce document. Pour plus d'informations sur la mise en forme et le référencement des endpoints, consultez les [directives de documentation des endpoints API]({{site.baseurl}}/contributing/style_guide/api_endpoint_guidelines/).

#### Éviter les garanties {#avoid-guarantees}

Notre documentation doit s'abstenir de faire des engagements qui pourraient potentiellement entraîner des implications juridiques. Évitez d'utiliser des termes définitifs tels que « garantir » ou « assurer ». Utilisez plutôt des formulations prospectives comme « Conçu pour » ou « Destiné à » pour transmettre avec précision les capacités et les intentions du produit.

#### Décrire les interactions avec l'interface {#describing-interactions-with-the-ui}

Lorsque vous faites référence à des éléments de l'interface, respectez la capitalisation telle qu'elle apparaît dans l'interface. Cependant, si un libellé est entièrement en majuscules, utilisez la casse de phrase (exception : les libellés courts, comme les opérateurs AND ou OR).

Lorsque vous demandez à un lecteur d'interagir avec l'interface, mettez en gras l'élément d'interface avec lequel il interagit. Pour les chaînes qu'un utilisateur saisirait dans un champ, utilisez des guillemets.

Pour savoir quels verbes utiliser pour décrire les interactions avec l'interface, consultez le tableau suivant :

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<colgroup>
<col style="width: 20%;">
<col style="width: 40%;">
<col style="width: 40%;">
</colgroup>
<thead>
<tr><th>Verbe</th><th>Utilisation</th><th>Exemple</th></tr>
</thead>
<tbody>
<tr><td>Ouvrir</td><td><ul><li>Ouvrir des applications</li><li>Ouvrir des fichiers et des dossiers</li></ul></td><td><ul><li>Ouvrez Droidboy.</li><li>Ouvrez le fichier braze.xml.</li></ul></td></tr>
<tr><td>Fermer</td><td><ul><li>Fermer des applications</li><li>Fermer des fichiers et des dossiers</li></ul></td><td><ul><li>Fermez Droidboy.</li><li>Fermez le fichier braze.xml.</li></ul></td></tr>
<tr><td>Accéder à</td><td><ul><li>Accéder à une page spécifique de l'interface (onglet, page, section)</li><li>Accéder à une page web</li></ul></td><td><ul><li>Accédez à la page <strong>Segments</strong>, puis cliquez sur…</li><li>Accédez à example.com pour vous inscrire.</li></ul></td></tr>
<tr><td>&gt;</td><td>Suivre une séquence d'étapes lorsque toutes les étapes sont du même type.</td><td>Accédez à <strong>Segments</strong> &gt; <strong>Segment Insights</strong>.</td></tr>
<tr><td>Choisir</td><td>Prendre une décision subjective, stratégique, ouverte ou complexe.</td><td>Choisissez une stratégie de campagne.</td></tr>
<tr><td>Sélectionner</td><td><ul><li>Cocher une case</li><li>Sélectionner des éléments dans un menu déroulant</li><li>Sélectionner un onglet</li><li>Prendre une décision simple</li></ul></td><td><ul><li>Sélectionnez <strong>Afficher le mot de passe</strong>.</li><li>Sélectionnez un type de données dans le menu déroulant.</li><li>Sur la page <strong>Gérer les paramètres</strong>, sélectionnez l'onglet <strong>Événements personnalisés</strong>.</li><li>Sélectionnez une image.</li></ul></td></tr>
<tr><td>Décocher</td><td>Décocher une case.</td><td>Décochez la case <strong>Afficher le mot de passe</strong>.</td></tr>
<tr><td>Sélectionner</td><td>Sélectionner un élément dans l'interface.</td><td>Ajoutez un attribut personnalisé et sélectionnez <strong>Enregistrer</strong>.</td></tr>
<tr><td>Activer</td><td>Activer une option à bascule.</td><td>Activez l'<strong>en-tête List-Unsubscribe</strong>.</td></tr>
<tr><td>Désactiver</td><td>Désactiver une option à bascule.</td><td>Désactivez <strong>CSS en ligne sur les nouveaux e-mails par défaut</strong>.</td></tr>
<tr><td>Saisir</td><td>Taper une valeur.</td><td><ul><li>Dans le champ de texte, saisissez le nom de votre attribut personnalisé.</li><li>Saisissez « Braze » comme nom de source.</li></ul></td></tr>
</tbody>
</table>
{:/}

#### Décrire les limitations {#describing-limitations}

Rédigez de manière transparente sur les limitations du produit, sans distorsion ni manipulation. Les lecteurs réagissent vivement lorsqu'ils se sentent manipulés ou trompés, ce qui compromet l'efficacité de la documentation en tant que source de vérité utilitaire. Les clients s'appuient sur la documentation pour comprendre les limites du système sur lequel ils construisent afin de pouvoir utiliser Braze avec succès.

En même temps, soutenez l'intentionnalité du développement du produit en contextualisant les limitations de manière appropriée et positive.

* S'il existe une limitation souple (par exemple, une limite de débit API), présentez la limitation en parlant de la **limite par défaut** ou de l'**allocation initiale**.
* Fournissez un chemin significatif pour naviguer les limites souples. Fournissez des exemples de ces solutions de contournement le cas échéant.
 * Par exemple, Braze utilise des exercices de dimensionnement lors de l'onboarding pour aider les clients à comprendre comment des éléments tels que les points de données sont utilisés par d'autres entreprises de taille similaire. Lorsque vous discutez des points de données, il est approprié de parler de l'exercice de dimensionnement en même temps.
* Il est préférable de décrire un chemin positif plutôt qu'une atténuation.
 * Par exemple, au lieu de dire « Braze ne permet pas aux clients de faire cela par eux-mêmes. L'équipe de support doit activer cette fonctionnalité pour vous », dites « Pour activer cette fonctionnalité, contactez l'équipe de support. »
* Ne vous reposez pas trop sur les mêmes formulations toutes faites pour naviguer les limites souples. Si un utilisateur lit « Contactez votre conseiller » encore et encore, le conseil perd tout son sens.
* S'il existe une limitation stricte, essayez de décrire la raison derrière cette limite.
 * Par exemple : « Il y a une limite de 200 campagnes de messages in-app actives par événement par groupe d'applications pour optimiser la vitesse de livraison des messages et prévenir les délais d'attente. …Le client moyen de Braze a un total de 26 campagnes actives en même temps — il est donc peu probable que cette limitation vous affecte. »
* Ne décrivez pas de [fonctionnalités planifiées ou futures](#future-features) pour expliquer les limitations actuelles.
* Lorsque vous faites référence aux limites concernant les données personnalisées, utilisez le terme « capacité » au lieu de limites.
 * Par exemple : Par défaut, vous pouvez avoir 20 propriétés d'événement segmentables par espace de travail. Contactez votre Account Manager Braze pour augmenter votre capacité.

#### Fonctionnalités futures {#future-features}

Évitez les références aux fonctionnalités futures ou les suggestions que quelque chose pourrait être pris en charge à l'avenir.

N'utilisez pas de mots et d'expressions qui ancrent votre rédaction à un moment précis, car ils rendent le contenu rapidement obsolète. Concentrez-vous sur le fonctionnement actuel du produit, pas sur ce qui a changé (sauf pour le contenu lié au temps, comme les notes de version).

Évitez spécifiquement la liste suivante de mots et d'expressions, tirée du [guide de style de documentation développeur](https://developers.google.com/style/timeless-documentation) de Google :

* au moment de la rédaction
* actuellement
* ne prend pas encore en charge
* à terme
* futur, à l'avenir
* dernier
* nouveau, plus récent
* maintenant
* ancien, plus ancien
* présentement, à présent
* bientôt

#### Dépréciation de fonctionnalités {#features-deprecations}

Avant d'inclure des informations sur la dépréciation de fonctionnalités, assurez-vous d'avoir un calendrier général de quand les lecteurs peuvent s'attendre à ce que la fonctionnalité soit dépréciée (par exemple, fin 2025).

Une fois que vous avez un calendrier général, communiquez la dépréciation de la fonctionnalité tôt. Soyez clair dans votre rédaction sur les dépréciations afin que les lecteurs puissent clairement comprendre à quoi s'attendre.

N'utilisez pas de formulations qui pourraient susciter la peur, l'incertitude ou le doute chez les lecteurs. Fournissez un chemin clair vers l'avenir, comme ce par quoi la fonctionnalité dépréciée est remplacée ou une solution alternative.

#### Général versus spécifique {#general-vs-specific}

En tant que bonne pratique, rédigez des articles qui traitent des fonctionnalités de manière généralement applicable. Si plus de détails sont nécessaires pour des cas spécifiques ou des exceptions, créez une section séparée (ou un article séparé si le contenu fait la longueur d'un article web, environ 500 mots) qui décrit ce cas particulier. Créez des références croisées de l'article général vers l'article spécifique pour aider les utilisateurs à connecter ces concepts.

Évitez de créer du contenu dupliqué ou répétitif pour différents canaux ou fonctionnalités. Si la répétition est nécessaire, utilisez des fichiers `includes` et d'autres [bonnes pratiques de réutilisation de contenu]({{site.baseurl}}/contributing/content_management/reusing_content).

**Par exemple :** Un cas d'utilisation courant pour les clients de Braze est de recibler les utilisateurs qui ont précédemment interagi avec leurs messages. Le reciblage des utilisateurs peut être effectué via de nombreux outils d'engagement, notamment les campagnes, les Canvas, les pages d'accueil et les segments. Le reciblage des utilisateurs peut être effectué via de nombreux canaux : WhatsApp, SMS, Cartes de contenu, e-mail, notifications push, et plus encore. Souvent, les clients essaient de réengager un utilisateur via un canal différent de celui précédemment utilisé.
Au lieu de créer un article pour chaque outil d'engagement et chaque canal, créez un seul article qui traite des stratégies de reciblage des utilisateurs et décrit toutes les options disponibles. S'il y a des considérations spéciales pour des canaux/outils spécifiques, créez un article séparé qui décrit ces considérations et placez-le dans cette section de documentation. Créez des références croisées entre l'article général et l'article spécifique.

#### Métadonnées et YAML {#metadata-and-yaml}

Les articles de la documentation Braze nécessitent certaines métadonnées à des fins de recherche et d'indexation. Pour savoir quelles métadonnées sont requises, consultez la page GitHub sur les [mises en page YAML et métadonnées](https://github.com/braze-inc/braze-docs/wiki/YAML-%26-Metadata-Layouts).

#### Conventions de nommage {#naming-conventions}

Lorsque vous nommez des articles et des fichiers, assurez-vous de décrire le sujet général dans le titre. Incluez toujours un mot-clé et une brève description que les lecteurs comprennent facilement, en particulier pour les titres d'articles.

Pour les noms de fichiers, gardez le nom bref et évitez d'utiliser des articles (un, une, le/la). Séparez chaque mot par un tiret bas (_).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">À faire</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Cibler les utilisateurs</td></tr>
<tr><td style="width: 100%;">Créer une campagne e-mail</td></tr>
<tr><td style="width: 100%;">Erreurs et réponses API</td></tr>
<tr><td style="width: 100%;">sms_historical_performance.png</td></tr>
<tr><td style="width: 100%;">push_notification_test.png</td></tr>
</tbody>
</table>
{:/}

En général, pour les articles et les fichiers image, utilisez la même orthographe et la même capitalisation que l'article et les fichiers référencés. Pour les directives de style des titres d'articles, consultez [Titres et en-têtes](#headings-and-titles).

Lorsque vous faites référence à un fichier spécifique, utilisez la même orthographe du nom de fichier et la police de code. Pour les détails de mise en forme, consultez la page GitHub sur la [mise en forme spéciale](https://github.com/braze-inc/braze-docs/wiki/Special-Formatting).

#### Procédures et instructions {#procedures-and-instructions}

Cette section couvre quelques directives à garder à l'esprit lors de la rédaction d'instructions pour les procédures dans le tableau de bord de Braze.

Directives générales :

* **Utilisez le bon ton.** Pour les instructions, gardez votre rédaction courte, directe et orientée vers la tâche. Votre rédaction n'a pas besoin d'être sèche ou austère, mais elle doit être directe. Lorsque vous introduisez des tâches ou des sous-tâches, vous pouvez utiliser un ton plus informel pour varier. Évitez d'utiliser « s'il vous plaît » pour garder un ton informel. Utilisez les contractions pour garder un ton accessible.
* **Suivez un format de titre parallèle.** Choisissez un format pour vos titres et tenez-vous-y. Gardez votre contenu facile à parcourir et prévisible. Pour les titres basés sur des tâches et les titres de page, préférez les verbes à l'impératif (par exemple, « Créer une campagne e-mail »).

Avant les instructions :

* **Utilisez des introductions et des conditions préalables.** Ne sautez pas directement dans les étapes. Donnez plutôt du contexte sur ce que couvre votre article ou section, et fournissez toute information que le lecteur doit connaître avant de parcourir les instructions. Assurez-vous que toutes les conditions préalables sont listées en haut de l'article avec le titre « Conditions préalables ». Les en-têtes de tableau dans cette section doivent indiquer « Exigences ». « Exigences » est un terme acceptable pour énoncer une exigence de Braze, d'un fournisseur tiers ou d'un partenaire.
* **Commencez au début de la procédure.** Ne supposez pas que le lecteur a atteint cette page après avoir terminé une étape précédente. Si les instructions d'une tâche reprennent là où une autre s'est arrêtée, donnez un aperçu de l'endroit où se trouve le lecteur dans la procédure et de ce qu'il doit avoir terminé avant cette étape. Incluez des liens vers les étapes précédentes.

Rédaction des instructions :

* **Utilisez un langage orienté vers l'action.** Structurez la documentation autour de ce que l'utilisateur peut faire, pas de ce que le produit peut faire. Évitez un langage comme « Cette fonctionnalité [fait xyz] ». Pensez plutôt en termes de « Utilisez cette fonctionnalité pour [faire xyz] ».
* **Fournissez des étapes de localisation si nécessaire.** Assurez-vous que le lecteur regarde au bon endroit avec de brèves phrases telles que « Sur la page **Paramètres**, sélectionnez **Modifier**. » Si cela n'est pas suffisamment clair, fournissez une étape d'introduction. Par exemple, « Accédez à **Gérer les paramètres** et sélectionnez l'onglet **Paramètres**. »
* **Préfacez les instructions conditionnelles.** Placez les [clauses conditionnelles](#clause-order) en premier. Pour les instructions conditionnelles, préfacez l'étape avec « si » afin que le lecteur sache qu'il peut sauter l'étape si la condition ne s'applique pas à lui. Par exemple, « Si vous avez besoin de X, alors faites A > B > C. »
* **Renforcez l'ordre des tâches.** Pour la progression au sein d'une série d'étapes, utilisez l'expression « Lorsque vous avez » ou « Après avoir ». Pour la progression entre les tâches, commencez une section par « Maintenant que vous avez » ou « Après avoir ». Évitez l'expression « Une fois que vous avez », car cette utilisation spécifique de « une fois » ne se traduit pas bien.

#### Onglets {#tabs}

Les onglets peuvent être utilisés dans la documentation technique comme moyen d'organiser des informations groupées.

Un onglet fait référence à un élément qui peut être utilisé lors de la rédaction d'instructions pour démontrer un résumé de flux de travail ou pour organiser des informations groupées. C'est similaire à un tableau ou une liste, mais les informations sont regroupées dans des panneaux.

Envisagez d'utiliser des onglets lorsque les informations peuvent être regroupées pour éviter la duplication ou pour visualiser un flux de travail pour les lecteurs. Assurez-vous que les onglets contiennent des informations parallèles et ne sont pas utilisés lorsque le lecteur doit suivre des étapes séquentielles dans un flux de travail.

Par exemple, vous pouvez utiliser des onglets pour afficher des exemples de code dans différents langages de programmation. Dans ce cas, un lecteur basculerait entre les exemples en fonction des libellés des onglets au lieu de faire défiler l'article.

Pour les détails de mise en forme, consultez la page GitHub sur la [mise en forme spéciale](https://github.com/braze-inc/braze-docs/wiki/Special-Formatting). Vous pouvez également utiliser une [liste](#lists) ou un [tableau](#tables-1) pour organiser les informations.

### Mise en forme et organisation {#formatting-and-organizing}

#### Adresses {#addresses}

Utilisez le numéro suivi du nom de la rue comme suit :

*330 W. 34th St.*

Pour afficher une adresse complète, utilisez le numéro, suivi du nom de la rue, suivi de la ville, de l'état et du code postal. Il n'est pas nécessaire de mettre une virgule entre l'état et le code postal.

*330 W. 34th St., New York, NY 10001*

#### Libellés de boutons {#buttons-labels}

Les libellés de boutons doivent être clairs et prévisibles — l'utilisateur doit savoir quelle action se produit en sélectionnant le bouton. Utilisez la casse de phrase pour les libellés de boutons et commencez par un verbe fort. S'il n'est pas clair à quoi le verbe fait référence, utilisez le format [verbe] + [nom].

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">S'inscrire</td><td style="width: 50%;">S'Inscrire</td></tr>
<tr><td style="width: 50%;">Se connecter</td><td style="width: 50%;">Se Connecter</td></tr>
<tr><td style="width: 50%;">S'abonner</td><td style="width: 50%;">S'ABONNER</td></tr>
<tr><td style="width: 50%;">En savoir plus</td><td style="width: 50%;">Plus</td></tr>
</tbody>
</table>
{:/}

Omettez les mots et articles inutiles, tels que « un », « une » ou « le/la ».

#### Encadrés et alertes {#callouts-and-alerts}

Les alertes, également appelées encadrés, sont utilisées pour attirer l'attention sur des informations utiles au lecteur. Il existe quatre types d'alertes utilisés dans notre documentation :

* Important
* Note
* Astuce
* Avertissement

Utilisez les alertes avec parcimonie dans les articles. Pour plus d'informations, consultez les [bonnes pratiques pour les alertes]({{site.baseurl}}/contributing/style_guide/alerts/).

#### Code dans le texte {#code-in-text}

Il existe plusieurs scénarios où vous devez utiliser la police de code pour mettre en forme du texte dans une phrase. Voici une liste non exhaustive d'éléments qui doivent être en police de code :

* Noms et valeurs d'attributs
* Paramètres de requête API
* Noms de fichiers
* Chemins de fichiers
* Noms de méthodes, variables ou paramètres
* Noms d'éléments HTML et XML
* Codes de statut HTTP
* Texte saisi dans un terminal

Pour créer du texte de code en ligne dans la documentation Braze, entourez le texte de backticks (`).

#### Exemples de code {#code-samples}

Les exemples de code font référence à des blocs de texte de code qui affichent un extrait de code. Pour des raisons d'accessibilité, introduisez l'exemple de code avec une phrase explicative lorsque c'est possible.

Pour vous assurer que vos exemples de code sont lisibles, indentez chaque ligne de deux espaces par niveau d'indentation. Si vous avez des difficultés à mettre en forme vos exemples de code, essayez d'embellir votre code à l'aide d'un formateur, tel que [JSON Formatter](https://jsonformatter.org/json-pretty-print).

Pour créer des blocs de code dans la documentation Braze, consultez [Code Snippet Test](https://github.com/braze-inc/braze-docs/blob/develop/_docs/_home/styling_test_page.md#code-snippet-test). N'oubliez pas que les blocs de code doivent spécifier le type de langage pour assurer une coloration syntaxique correcte.

#### Dates et heures {#dates-and-times}

Écrivez les mois et les jours de la semaine en toutes lettres. Évitez les abréviations lorsque c'est possible. Pour les cas où l'abréviation des mois est nécessaire, n'abrégez que les suivants :

* janv.
* fév.
* août
* sept.
* oct.
* nov.
* déc.

Utilisez une [virgule](#commas) pour séparer la date de l'année. Si un jour de la semaine est utilisé avec la date, ajoutez-le avant le mois.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">À faire : <em>Utiliser le format de date préféré.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Septembre 2021</td></tr>
<tr><td style="width: 100%;">15 septembre 2021</td></tr>
<tr><td style="width: 100%;">Mercredi 15 septembre 2021</td></tr>
</tbody>
</table>
{:/}

Pour les plages de dates, utilisez un [tiret demi-cadratin](#en-dash).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">À faire</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">2010–2021</td></tr>
</tbody>
</table>
{:/}

Utilisez un tiret demi-cadratin pour les plages de dates.

Utilisez des chiffres avec les mentions am/pm, suivis d'un espace, puis de l'indication horaire. Supprimez les minutes pour les heures pleines.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire : <em>Utiliser des chiffres avec am ou pm.</em></th><th style="width: 50%;">À éviter : <em>Utiliser les minutes pour les heures pleines (sauf pour une plage).</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">12 pm</td><td style="width: 50%;">12:00 P.M.</td></tr>
</tbody>
</table>
{:/}

Pour les plages horaires, utilisez un tiret demi-cadratin pour séparer. N'ajoutez pas d'espaces avant ou après le tiret demi-cadratin.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">À faire : <em>Utiliser un tiret demi-cadratin pour les plages horaires.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">12:45–14:30</td></tr>
</tbody>
</table>
{:/}

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">À faire : <em>Utiliser les minutes pour les plages horaires.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">8:00 am–2:30 pm</td></tr>
</tbody>
</table>
{:/}

Pour référence dans les cas où des parties d'autres fuseaux horaires sont incluses (comme les webinaires, réunions ou événements), indiquez le fuseau horaire comme indiqué ci-dessous :

* Eastern Standard Time : EST
* Central Standard Time : CST
* Mountain Standard Time : MST
* Pacific Standard Time : PST
* Greenwich Mean Time : GMT
* Coordinated Universal Time : UTC
* Central European Time : CET
* Eastern Europe Time : EET
* Western Europe Time : WET
* Singapore Time : SGT
* China Standard Time : CST

#### Emojis {#emojis}

Bien que nous soyons décontractés, évitez d'utiliser des emojis dans le contenu pédagogique car ils peuvent être interprétés de différentes manières et donnent souvent une impression non professionnelle.

Les exceptions incluent les scénarios suivants :

* Lorsque vous utilisez ✅ et ❌ dans les tableaux pour indiquer le contenu pris en charge versus non pris en charge, ou recommandé versus non recommandé
* Lorsqu'ils sont utilisés dans des exemples de texte pour une campagne ou un message Canvas

#### Noms d'exemple {#example-names}

N'utilisez jamais de vrais noms, adresses e-mail ou toute autre information personnellement identifiable (PII). Utilisez plutôt des exemples fictifs ou du [texte de substitution](#placeholder-text).

Lorsque vous devez inclure des noms dans votre rédaction, consultez la liste Wikipedia des [prénoms unisexes](https://en.wikipedia.org/wiki/Unisex_name). Utilisez les pronoms « ils/elles », « leur » et « leurs » lorsque c'est possible, et évitez d'utiliser des exemples limités à un genre spécifique.

##### Adresses e-mail d'exemple

Utilisez le format « nom@example.com » pour les adresses e-mail génériques. Remplacez « nom » par un nom d'exemple. Par exemple :

* alex@example.com
* lee@example.com
* yuri@example.com

#### Figures et autres images {#figures-and-other-images}

Lors de la création de figures et d'images, consultez le [guide de style pour les images]({{site.baseurl}}/contributing/style_guide/image_style_guide/). N'incluez jamais d'informations personnellement identifiables (PII) dans les figures ou les images.

##### Texte alternatif {#alt-text}

Incluez toujours un texte alternatif avec les images. Les lecteurs d'écran annoncent le texte alternatif pour expliquer les images aux personnes malvoyantes. Votre texte alternatif doit donc transmettre toutes les informations clés représentées dans l'image.
Utilisez les directives suivantes lors de la rédaction du texte alternatif :

* Utilisez un [langage simple](https://www.plainlanguage.gov/guidelines/).
* Rédigez des phrases complètes et utilisez la casse de phrase.
* Omettez les mots inutiles.
* N'incluez pas « image de » ou « photo de ». Il est déjà compris que vous faites référence à une image.
* N'incluez pas de caractères spéciaux. Par exemple, au lieu d'esperluettes (&), utilisez le mot « et » écrit en toutes lettres.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Page de paramètres des événements personnalisés dans le tableau de bord de Braze avec Ajouter un rapport mis en surbrillance.</td><td style="width: 50%;">Une capture d'écran de la page Gérer les paramètres > Événements personnalisés dans le tableau de bord de Braze avec l'option d'ajouter un rapport mise en surbrillance.</td></tr>
</tbody>
</table>
{:/}

Laissez les balises alt explicitement vides (alt="") si l'image ajoute un composant visuel redondant à ce qui est expliqué dans le texte.

Ajouter un texte alternatif à chaque image ne rend pas automatiquement le contenu de la page web facile à naviguer et à consommer. Les visuels redondants sont puissants pour les utilisateurs voyants car l'information visuelle est facile à comprendre et à mémoriser. Cependant, le texte alternatif décrivant des images redondantes peut être inutile pour les utilisateurs qui ne peuvent pas voir l'image, car chaque élément de page exige une attention égale de la part des utilisateurs de lecteurs d'écran pour déterminer s'il est utile pour leur tâche.

##### Noms d'entreprise d'exemple

Si possible, prenez des captures d'écran depuis [dashboard-06](https://dashboard-06.braze.com/) afin d'utiliser l'un des noms d'entreprise FakeBrandz.

#### Types de fichiers et noms de fichiers {#file-types-and-filenames}

Lorsque vous faites référence à un type de fichier, utilisez le nom standard du type. Si le type de fichier est un acronyme, indiquez-le en majuscules.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire : <em>Utiliser le nom standard du type de fichier</em></th><th style="width: 50%;">À éviter : <em>Utiliser l'extension de fichier</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">CSV</td><td style="width: 50%;">.csv</td></tr>
<tr><td style="width: 50%;">fichier exécutable</td><td style="width: 50%;">.exe</td></tr>
<tr><td style="width: 50%;">GIF</td><td style="width: 50%;">.gif</td></tr>
<tr><td style="width: 50%;">JAR</td><td style="width: 50%;">.jar</td></tr>
<tr><td style="width: 50%;">JPEG</td><td style="width: 50%;">.jpg, .jpeg</td></tr>
<tr><td style="width: 50%;">JSON</td><td style="width: 50%;">.json</td></tr>
<tr><td style="width: 50%;">PDF</td><td style="width: 50%;">.pdf</td></tr>
<tr><td style="width: 50%;">PNG</td><td style="width: 50%;">.png</td></tr>
<tr><td style="width: 50%;">fichier Python</td><td style="width: 50%;">.py</td></tr>
<tr><td style="width: 50%;">fichier Bash</td><td style="width: 50%;">.sh</td></tr>
<tr><td style="width: 50%;">fichier texte</td><td style="width: 50%;">.txt</td></tr>
<tr><td style="width: 50%;">YAML</td><td style="width: 50%;">.yaml</td></tr>
<tr><td style="width: 50%;">ZIP</td><td style="width: 50%;">.zip</td></tr>
</tbody>
</table>
{:/}

Lorsque vous faites référence au nom d'un fichier, formatez le nom du fichier en texte de code. Pour plus d'informations, consultez la section [Code dans le texte](#code-in-text).

Lorsque vous nommez des fichiers dans la documentation Braze, tels que des articles ou des fichiers image, utilisez des minuscules et séparez les mots par des tirets bas, pas des traits d'union. Pour plus d'informations, consultez [Créer des fichiers et des dossiers](https://github.com/braze-inc/braze-docs/wiki/Creating-Files-&-Folders) sur GitHub.

#### Notes de bas de page {#footnotes}

Les notes de bas de page sont des annotations qui fournissent des informations supplémentaires et sont généralement placées à la fin d'une page. En raison de la mise en forme de notre texte, les notes de bas de page ne sont pas optimales pour la plupart des cas d'utilisation. Voici quand utiliser des notes de bas de page par rapport à d'autres méthodes d'attribution :

* Si vous présentez une liste de statistiques ou d'autres informations denses qui doivent toutes être attribuées à des sources, utilisez des notes de bas de page.
* Si vous présentez une ou deux informations, utilisez un lien ou une alerte.
* Si vous devez fournir des informations supplémentaires sur des éléments d'un tableau, utilisez un symbole astérisque (*) à côté de l'élément du tableau et présentez les informations après le tableau.

#### Mise en forme du texte dans les instructions {#formatting-text-in-instructions}

Utilisez une mise en forme de texte cohérente pour aider les lecteurs à trouver et interpréter les informations. Cette section fournit des directives sur la mise en forme à utiliser lors de la description ou de la référence à différents éléments de texte dans vos instructions.

Cette section couvre les éléments suivants :

* [Boutons](#buttons)
* [Cases à cocher](#checkboxes)
* [Commandes et options en ligne de commande](#command-line-commands-and-options)
* [Boîtes de dialogue](#dialog-boxes-(modals))
* [Messages d'erreur](#error-messages)
* [Noms de filtres et d'opérateurs](#filter-and-operator-names)
* [Noms de dossiers et de fichiers](#folder-and-filenames)
* [Noms de touches et combinaisons](#key-names-and-combinations)
* [Métriques](#metrics)
* [Pages](#pages)
* [Noms d'autorisations](#permission-names)
* [Onglets](#tabs-1)
* [Saisie de texte](#text-input)

##### Boutons {#buttons}

Lorsque vous faites référence à un bouton, utilisez du texte en gras pour le libellé du bouton. Dans la plupart des cas, respectez la capitalisation de l'interface. Pour les boutons dont le libellé est entièrement en majuscules (sauf les boutons OK), utilisez plutôt la casse de phrase.

Pour faire référence à un bouton, utilisez uniquement le libellé du bouton. Ne faites pas référence à un bouton comme « le bouton [libellé] ».

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Sélectionnez <strong>Ajouter des langues</strong>.</td><td style="width: 50%;">Sélectionnez le bouton <strong>Ajouter des langues</strong>. <br><br> Sélectionnez « Ajouter des langues ».</td></tr>
</tbody>
</table>
{:/}

Si le libellé se termine par deux-points ou des points de suspension, omettez la ponctuation finale.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Sélectionnez <strong>Enregistrer sous</strong></td><td style="width: 50%;">Sélectionnez <strong>Enregistrer sous…</strong></td></tr>
</tbody>
</table>
{:/}

Si un bouton est une icône, incluez le nom du bouton tel qu'il apparaît dans l'infobulle. Si un bouton avec une icône n'inclut pas d'infobulle, soumettez une demande pour qu'une infobulle soit ajoutée.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Sélectionnez ➕ <strong>Ajouter</strong>.</td><td style="width: 50%;">Sélectionnez l'icône ➕.</td></tr>
</tbody>
</table>
{:/}

##### Cases à cocher {#checkboxes}

Lorsque vous faites référence à une case à cocher, utilisez du texte en gras pour le libellé de la case. N'incluez pas le mot « case à cocher » sauf si la clarté l'exige. Préférez les termes « sélectionner/décocher » plutôt que « cocher/décocher ».

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Sélectionnez <strong>Envoyer la campagne aux utilisateurs dans leur fuseau horaire local</strong>.</td><td style="width: 50%;">Cochez <strong>Envoyer la campagne aux utilisateurs dans leur fuseau horaire local</strong>.</td></tr>
<tr><td style="width: 50%;">Décochez la case <strong>Quitter</strong>.</td><td style="width: 50%;">Décochez la case <strong>Quitter</strong>.</td></tr>
</tbody>
</table>
{:/}

##### Commandes et options en ligne de commande {#command-line-commands-and-options}

Lorsque vous faites référence à des commandes ou options en ligne de commande, utilisez la mise en forme de code. Respectez la capitalisation telle qu'elle apparaît ou telle qu'elle doit être saisie.

##### Boîtes de dialogue (modales) {#dialog-boxes-(modals)}

Évitez de faire référence aux boîtes de dialogue par leur nom sauf si la clarté l'exige. Décrivez plutôt ce que le lecteur doit faire. Si vous faites référence à une boîte de dialogue, utilisez du texte en gras pour le nom de la boîte de dialogue et respectez la capitalisation de l'interface.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Sélectionnez <strong>Télécharger</strong> puis sélectionnez un fichier à télécharger.</td><td style="width: 50%;">Sélectionnez <strong>Télécharger</strong> et utilisez la boîte de dialogue <strong>Téléchargement de fichier</strong> pour sélectionner un fichier à télécharger.</td></tr>
</tbody>
</table>
{:/}

##### Messages d'erreur {#error-messages}

Lorsque vous faites référence à des messages d'erreur qu'un lecteur peut rencontrer, encapsulez le message d'erreur entre guillemets. Pour les messages d'erreur plus longs, utilisez une citation en bloc.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">« Push Bounced: MismatchSenderId »</td><td style="width: 50%;"><em>Push Bounced: MismatchSenderID</em><br><br><code>Push Bounced: MismatchSenderID</code></td></tr>
</tbody>
</table>
{:/}

##### Noms de filtres et d'opérateurs {#filter-and-operator-names}

Lorsque vous faites référence aux noms de filtres et d'opérateurs pour les segments ou d'autres zones du tableau de bord, utilisez du texte de code. Respectez la casse de l'interface, y compris les éléments entièrement en majuscules tels que les opérateurs `OR` et `AND`.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Sélectionnez le filtre <code>First Used App</code> et…</td><td style="width: 50%;">Sélectionnez le filtre <strong>First Used App</strong> et…</td></tr>
<tr><td style="width: 50%;">Combinez les filtres avec l'opérateur <code>OR</code>.</td><td style="width: 50%;">Combinez les filtres avec l'opérateur « OR ».</td></tr>
</tbody>
</table>
{:/}

##### Noms de dossiers et de fichiers {#folder-and-filenames}

Lorsque vous faites référence à des noms de dossiers et de fichiers, utilisez du texte de code.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Ouvrez le fichier <code>braze.xml</code>.</td><td style="width: 50%;">Ouvrez le fichier <strong>braze.xml</strong>.</td></tr>
</tbody>
</table>
{:/}

##### Noms de touches et combinaisons {#key-names-and-combinations}

Lorsque vous faites référence à des noms de touches ou des combinaisons de touches, utilisez la [balise HTML `<kbd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd). Cela désigne la saisie textuelle de l'utilisateur à partir d'un clavier, d'une entrée vocale ou de tout autre dispositif de saisie de texte. Si vous travaillez dans un éditeur qui ne prend pas en charge le HTML personnalisé, utilisez du [texte de code](#code-in-text) à la place.

Écrivez les noms des touches tels que Commande, Contrôle, Option et Maj en toutes lettres. N'utilisez pas de symboles pour ces touches.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Appuyez sur <strong>Option</strong>.</td><td style="width: 50%;">Appuyez sur ⌥.</td></tr>
</tbody>
</table>
{:/}

Pour les combinaisons de touches, utilisez un signe plus (+) entre les touches, mais omettez le plus de toute mise en forme spéciale.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Appuyez sur <strong>Option + F12</strong>.</td><td style="width: 50%;">Appuyez sur ⌥ + F12.</td></tr>
</tbody>
</table>
{:/}

Par exemple, voici comment les balises clavier apparaissent dans la documentation Braze :
Pour arrêter la commande, appuyez sur **Contrôle + C**.

##### Métriques {#metrics}

Lorsque vous faites référence à une métrique dans un tableau ou une entrée de glossaire, utilisez des majuscules initiales sans mise en forme spéciale. Lorsque vous faites référence à une métrique dans une phrase, utilisez des majuscules initiales avec des italiques (comme *Machine Opens*).

##### Pages

Utilisez le terme page lorsque vous faites référence à une page web en général ou à une page spécifique du tableau de bord de Braze. Lorsque vous faites référence à un nom de page, utilisez le format « la page [libellé] » et mettez en gras le nom de la page.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Accédez à la page Segments.</td><td style="width: 50%;">Accédez à la page « Segments ».</td></tr>
</tbody>
</table>
{:/}

##### Noms d'autorisations {#permission-names}

Lorsque vous faites référence aux noms des autorisations utilisateur dans le tableau de bord, encadrez le nom de l'autorisation entre guillemets.

{% alert note %}

Actuellement, nous utilisons la casse de titre pour correspondre à la mise en forme du tableau de bord. Il est prévu de mettre à jour les noms d'autorisations dans l'interface vers la casse de phrase pour correspondre à nos standards.

{% endalert %}

##### Onglets {#tabs-1}

Lorsque vous faites référence à un onglet, utilisez le format « l'onglet [libellé] » et mettez en gras le nom de l'onglet.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Accédez à la page <strong>Gérer les paramètres</strong> et sélectionnez l'onglet <strong>Tags</strong>.</td><td style="width: 50%;">Accédez à la page « Gérer les paramètres » et sélectionnez l'onglet « Tags ».</td></tr>
</tbody>
</table>
{:/}

##### Saisie de texte {#text-input}

Lorsque vous demandez à un lecteur de saisir une chaîne de texte spécifique, encadrez le texte entre guillemets.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Dans le champ <strong>Nom</strong>, saisissez « Utilisateurs inactifs »</td><td style="width: 50%;">Dans le champ <strong>Nom</strong>, saisissez <code>Utilisateurs inactifs</code>.</td></tr>
</tbody>
</table>
{:/}

#### Foire aux questions (FAQ) {#frequently-asked-questions-faqs}

Ordonnez les FAQ en commençant par les informations que les gens veulent ou ont le plus besoin de connaître, puis organisez les FAQ par catégorie de problème s'il y en a plusieurs.

Pour chaque FAQ, commencez par répondre directement à la question, puis entrez dans les détails. Utilisez de vraies questions qui correspondent aux requêtes de recherche typiques et au vocabulaire des utilisateurs, ce qui aide à la trouvabilité des FAQ. Incluez des liens vers des ressources que l'utilisateur pourrait trouver utiles, telles que des articles connexes, des instructions pour contacter le support et du matériel pédagogique (guides pratiques, tutoriels, etc.) lorsqu'ils sont disponibles.

#### Géographie {#geography}

##### Villes

Écrivez tous les noms de villes en toutes lettres à la première mention dans le texte. Après cela, il est acceptable d'abréger les noms de villes bien connues comme NYC ou LA.

**Première mention :** San Francisco
**Deuxième mention :** SF

Pour les villes bien connues comme Londres ou Tokyo, il est acceptable de les introduire sans virgule suivie de l'état, de la province ou du pays.

Pour les villes ou les communes qui peuvent être inconnues de votre audience, incluez l'état, la province ou le pays.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 100%;">À faire</th></tr>
</thead>
<tbody>
<tr><td style="width: 100%;">Biloxi, Mississippi</td></tr>
<tr><td style="width: 100%;">New Bedford, MA</td></tr>
<tr><td style="width: 100%;">Anvers, Belgique</td></tr>
</tbody>
</table>
{:/}

##### Pays

Mettez en majuscule les noms de tous les pays. Pour abréger un nom de pays, écrivez la première mention en entier, suivie des initiales par la suite.

**Première mention :** États-Unis
**Deuxième mention :** US

Ne placez pas de points entre les noms de pays abrégés.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">UK</td><td style="width: 50%;">U.K.</td></tr>
<tr><td style="width: 50%;">Washington, DC</td><td style="width: 50%;">Washington, D.C.</td></tr>
</tbody>
</table>
{:/}

##### Régions

Mettez en majuscule à la fois la région et le modificateur directionnel.

**Exemple :** Californie du Nord, Europe de l'Est

Mettez en majuscule les noms propres décrivant une région ou un lieu spécifique.

**Exemple :** West Midlands, Amérique du Sud, South Chicago

##### États et provinces

Mettez en majuscule tous les états et provinces.

**Exemple :** New York, Québec

#### Titres et en-têtes {#headings-and-titles}

Pour les en-têtes et titres d'articles, utilisez la casse de phrase. Soyez descriptif lors de la rédaction des en-têtes et titres, et concentrez-vous sur l'objectif principal du contenu en fonction du type d'article. N'utilisez pas d'esperluettes à la place du mot « et ».

Pour les titres d'articles, lorsque c'est possible, évitez les gérondifs (verbes se terminant par *-ant*) au profit de verbes à l'impératif. Gardez les titres d'articles concis et assurez-vous qu'ils sont appropriés pour le contenu. Par exemple, un article de référence sur les messages SMS pourrait être intitulé « À propos des SMS ».

Pour les en-têtes d'articles, soyez concis et cohérent entre les titres d'en-têtes. Par exemple, si le style Heading 1 de l'article définit chaque étape (ex. **Étape 1 : Créer une nouvelle campagne push**), gardez ce format dans tous les en-têtes de l'article pour la cohérence.

Pour de l'aide sur le style dans Braze Docs, consultez la page Contributing pour les [exemples de style]({{site.baseurl}}/contributing/styling_examples/?tab=markdown).

##### Sous-tâches numériques

Pour les en-têtes qui décrivent des étapes ordonnées, utilisez des chiffres dans les en-têtes de sous-tâches.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Étape 2 : Créer une campagne SMS <br><br> Étape 2.1 : Composer votre message <br><br> Étape 2.2 : Planifier la livraison</td><td style="width: 50%;">Étape 2 : Créer une campagne SMS <br><br> Étape 2a : Composer votre message <br><br> Étape 2b : Planifier la livraison</td></tr>
</tbody>
</table>
{:/}

#### Introductions {#introductions}

Les introductions servent de vérification rapide pour les utilisateurs qui se demandent :

* Suis-je dans le bon document ? Est-ce pertinent pour moi ?
* Qu'est-ce que j'apprendrai si j'investis du temps à lire ce document ?
* Ai-je l'impression de suivre un parcours clair d'intégration ou de configuration pour SMS, e-mail, IAM, ou autre (même sans préciser quel document l'utilisateur devrait consulter ensuite) ?

Voici les directives générales pour les introductions. Consultez les directives spécifiques à chaque section pour des cas d'utilisation plus spécifiques.

* Les introductions peuvent faire de 1 à 5 phrases
* Les introductions doivent donner un aperçu du contenu du document ou servir d'ouverture pour le sujet
* Utilisez des citations en bloc
* Placez les introductions sous l'en-tête H1 de l'article

##### Partenaires

Incluez un aperçu du partenaire et une brève description de l'entreprise. Incluez également un lien vers le site du partenaire.

##### API

Incluez uniquement la phrase « Utilisez cet endpoint pour... » dans l'introduction. Nous voulons garder les endpoints API aussi faciles à naviguer que possible. Pour plus d'informations sur la structure et la mise en forme des endpoints API, consultez les [directives de documentation des endpoints API]({{site.baseurl}}/contributing/style_guide/api_endpoint_guidelines/).

##### Guide utilisateur et guide développeur

Les paragraphes d'introduction doivent être rédigés de l'une des deux manières suivantes :

1. Avec un paragraphe d'accroche ou une ouverture pour le sujet
2. Une déclaration de ce que contient l'article. Cela ressemble souvent à « Cet article de référence... ».

Bien que les étapes du guide utilisateur et du guide développeur amènent les utilisateurs à s'appuyer fortement sur les indices de la navigation tout au long de leur parcours client, bien que parfois redondant, il est utile de dire explicitement la valeur du document dès le début.

Par exemple, si un utilisateur parcourait le guide développeur pour intégrer Unity. Cette page avec le titre « Intégration » ne suffirait pas sans inclure la phrase d'introduction.

#### Listes {#lists}

Les listes sont idéales pour mettre en forme des informations connexes. N'utilisez pas de liste pour afficher un seul élément. Si vous souhaitez mettre en valeur un seul élément par rapport au texte environnant, utilisez une autre mise en forme.

Il existe trois types de listes : à puces, à lettres et numérotées. Incluez une phrase d'introduction complète qui peut se terminer par deux-points ou un point.

* Les listes à puces organisent des informations qui n'ont pas besoin d'être dans un ordre spécifique.
* Les listes à lettres sont utilisées pour définir des options mutuellement exclusives.
* Les listes numérotées indiquent une séquence d'étapes ordonnées.

Utilisez la même syntaxe pour tous les éléments de liste si possible.

Pour la capitalisation des éléments de liste, commencez chaque élément par une majuscule. Pour la ponctuation finale des éléments de liste, n'utilisez pas de ponctuation finale dans les scénarios suivants :

* Si l'élément de liste est un seul mot ou une phrase incomplète
* Si l'élément de liste ne contient pas de verbe
* Si l'élément de liste est en police de code
* Si l'élément de liste est un lien ou un titre de document

#### Mise en forme des médias {#media-formatting}

Cette section inclut des directives générales pour la mise en forme des images et des GIF dans votre contenu. Pour plus d'informations, y compris des exemples de captures d'écran, consultez le [guide de style pour les images]({{site.baseurl}}/contributing/style_guide/image_style_guide/).

| **À faire** | {::nomarkdown}<ul><li>Recadrez étroitement sur la fonctionnalité ou le composant mentionné.</li><li>Prenez des captures d'écran de haute qualité, de préférence sur un écran Retina (écran MacBook).</li><li>Créez un GIF d'une interaction ou d'un flux de travail.</li><li>Gardez à l'esprit que les utilisateurs ne peuvent pas mettre en pause ou parcourir un GIF pour voir les détails.</li><li>Passez les images dans un optimiseur pour réduire la taille du fichier (ImageOptim, TinyPNG ou Ezgif).</li><li>Visez un contraste élevé entre les éléments pour l'accessibilité.</li><li>Redimensionnez les images par pourcentages de hauteur plutôt que par des valeurs de pixels distinctes.</li></ul>{:/} |
| **À éviter** | {::nomarkdown}<ul><li>N'incluez pas l'en-tête ou la barre latérale du tableau de bord, car ceux-ci peuvent être expliqués dans une simple phrase.</li><li>N'incluez pas l'intégralité du tableau de bord.</li><li>N'incluez pas d'informations personnellement identifiables (sauf si elles sont floutées ou celles d'un utilisateur de démonstration).</li><li>N'incluez pas le cadre du navigateur (champ URL, favoris, onglets, etc.).</li><li>N'incluez pas les tableaux de bord de partenaires technologiques.</li><li>N'ajoutez pas de bordure ou d'ombre portée aux images.</li></ul>{:/} |

#### Nombres {#numbers}

Ne commencez jamais une phrase par un chiffre. L'exception est lorsque vous faites référence à une année (exemple : « 2019 a été une année mémorable »).

Écrivez les nombres en toutes lettres jusqu'à neuf. Pour les unités de mesure ou les nombres à partir de 10, utilisez le chiffre. Pour les nombres de plus de trois chiffres, utilisez un espace (en français). Écrivez les grands nombres en toutes lettres.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">1 000</td><td style="width: 50%;">1000</td></tr>
<tr><td style="width: 50%;">200 000</td><td style="width: 50%;">200000</td></tr>
<tr><td style="width: 50%;">1 000 000</td><td style="width: 50%;">1000000</td></tr>
<tr><td style="width: 50%;">9 milliards</td><td style="width: 50%;">9000000000</td></tr>
<tr><td style="width: 50%;">5 Mo</td><td style="width: 50%;">cinq Mo</td></tr>
</tbody>
</table>
{:/}

##### Devise

Indiquez toujours la devise à laquelle vous faites référence en utilisant le symbole de la devise avant le montant ou en l'écrivant en toutes lettres (exemple : pesos, euros, livres, etc.).

Utilisez la décimale pour les montants où le nombre de centimes est supérieur à zéro. Pour les sommes supérieures à trois chiffres, utilisez un espace (en français). N'incluez pas « ,00 » dans les sommes d'argent.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">20 USD</td><td style="width: 50%;">$20</td></tr>
</tbody>
</table>
{:/}

##### Numéros de téléphone

Lorsqu'un numéro de téléphone est référencé, placez des tirets entre les chiffres. Ne placez pas l'indicatif régional entre parenthèses.

Lorsque vous formatez des numéros de téléphone avec un indicatif de pays, utilisez un signe plus (+) avant l'indicatif de pays et placez l'indicatif régional entre parenthèses.

Fournissez un numéro avec un indicatif de pays comme suit : +1 (504) 327-7269

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">123-456-7890</td><td style="width: 50%;">(123)-456-7890</td></tr>
<tr><td style="width: 50%;">+1 (123) 456-7890</td><td style="width: 50%;">1 234-567-9012</td></tr>
</tbody>
</table>
{:/}

##### Fractions

Écrivez les fractions en toutes lettres et utilisez un trait d'union entre le numérateur et le dénominateur. N'utilisez pas de chiffres séparés par une barre oblique.

Dans certains cas où exprimer une fraction sous forme décimale est nécessaire, ajoutez un zéro avant la virgule décimale pour les fractions inférieures à un.

Lorsque vous exprimez des systèmes de notation utilisant des fractions, utilisez des chiffres pour écrire le classement.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">0,5</td><td style="width: 50%;">1/2</td></tr>
<tr><td style="width: 50%;">un tiers</td><td style="width: 50%;">un-tiers</td></tr>
<tr><td style="width: 50%;">9 sur 10</td><td style="width: 50%;">neuf sur dix</td></tr>
</tbody>
</table>
{:/}

##### Pourcentages

Utilisez des chiffres et un signe de pourcentage (%) sans espace entre eux. Cependant, si le pourcentage commence la phrase, écrivez le pourcentage entier en toutes lettres (nombre et pourcentage).

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">10%</td><td style="width: 50%;">10 %</td></tr>
<tr><td style="width: 50%;">Vingt pour cent des utilisateurs de l'entreprise sont...</td><td style="width: 50%;">20% des utilisateurs de l'entreprise sont...</td></tr>
</tbody>
</table>
{:/}

##### Plages

Utilisez un trait d'union pour indiquer une plage de nombres. N'utilisez pas de tiret demi-cadratin pour séparer les nombres dans une plage.

Pour les plages de nombres avec des unités, répétez l'unité de mesure après le nombre. Cela n'inclut pas la répétition des noms. Utilisez le mot « à » entre les nombres de la plage pour éviter la confusion.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">5 à 100</td><td style="width: 50%;">5–100</td></tr>
<tr><td style="width: 50%;">-10°C à 50°C</td><td style="width: 50%;">-10°C-50°C</td></tr>
</tbody>
</table>
{:/}

#### Texte de substitution {#placeholder-text}

Utilisez du texte de substitution pour indiquer où le lecteur doit fournir la valeur pertinente. Le texte de substitution doit indiquer le contenu qui est représenté. Par exemple, *YOUR_API_KEY* indique la clé API du lecteur.

##### Rédiger des textes de substitution

Lors de la création de texte de substitution, consultez les directives suivantes :

| Directive | Exemple |
| :---- | :---- |
| Utilisez des lettres majuscules et séparez les mots par des tirets bas (_). | `PLACEHOLDER_VARIABLE` |
| Pour le texte de substitution en ligne, utilisez des italiques. | *`PLACEHOLDER_VARIABLE`* |
| Pour le texte de substitution dans les blocs de code API (où vous ne pouvez pas utiliser d'italiques), encadrez les textes de substitution entre accolades ({}). | `<string name="com_appboy_api_key">{YOUR_APP_IDENTIFIER_API_KEY}</string>` |
| Pour le texte de substitution dans les blocs de code Liquid (où vous ne pouvez pas utiliser d'italiques), utilisez des lettres majuscules. | `{% raw %}{%- connected_content YOUR-API-URL :save items -%}{% endraw %}` |
| Ne sacrifiez pas la clarté pour la brièveté. Utilisez autant de mots que nécessaire pour représenter un texte de substitution. | **À faire :** `CAMPAIGN_NAME` <br> **À éviter :** _`NAME`_|

##### Utiliser les textes de substitution

Lors de l'introduction ou de l'explication d'un texte de substitution, consultez les directives suivantes :

| Directive | Exemple |
| :---- | :---- |
| Signalez les textes de substitution immédiatement après le texte de substitution. | Remplacez `<YOUR_APP_IDENTIFIER_API_KEY>` par votre [clé API d'identifiant d'application]({{site.baseurl}}/api/api_key/#the-app-identifier-api-key), que vous pouvez trouver sur la page **Paramètres**. |
| Pour signaler deux textes de substitution ou plus en même temps, utilisez une liste à puces. Listez chaque texte de substitution dans l'ordre où il apparaît dans le code. | Remplacez les éléments suivants : {::nomarkdown}<ul><li><code>PLACEHOLDER_VARIABLE</code> : une description de ce que le texte de substitution représente</li><li><code>PLACEHOLDER_VARIABLE</code> : une description de ce que le texte de substitution représente</li></ul>{:/} |
| Faites référence au texte de substitution dans la même mise en forme que celle dans laquelle il est affiché dans le texte ou le code. | `target <YOUR_APP_TARGET> do pod 'Appboy-iOS-SDK' end` <br><br> Remplacez `<YOUR_APP_TARGET>` par le nom de votre application cible. |

#### Produits {#products}

Lorsque vous faites référence à Braze et à ses fonctionnalités, utilisez les noms complets des produits et fonctionnalités, et mettez-les en majuscule conformément à l'interface. Ne mettez pas en majuscule les modèles ou les fonctionnalités courantes. Pour une liste des noms de produits et leur orthographe, consultez le [Glossaire](#glossary).

N'abrégez pas les noms de produits ou de fonctionnalités sauf dans les cas suivants :

* Pour correspondre à l'interface
* Pour respecter des contraintes d'espace limitées

N'utilisez jamais les noms de produits ou de fonctionnalités comme verbes.

N'utilisez jamais d'apostrophe après Braze (exemple : « Braze's »). Cela sonne maladroit. Formez plutôt les possessifs en utilisant une préposition (« de, à, depuis ») suivie du nom de l'entreprise.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">La dernière mise à jour produit de Braze</td><td style="width: 50%;">La dernière mise à jour produit de Braze's</td></tr>
<tr><td style="width: 50%;">C'est l'une des caractéristiques distinctives de Braze.</td><td style="width: 50%;">C'est l'une des caractéristiques distinctives de Braze's</td></tr>
</tbody>
</table>
{:/}

Faites référence à « Braze » comme « nous/notre/nos ». Jamais « il/son/ils/leur ».

#### Tableaux {#tables}

L'utilisation de tableaux peut être un moyen utile et organisé d'afficher des informations. Assurez-vous d'avoir des en-têtes clairs et descriptifs et des données pertinentes dans les colonnes et lignes respectives.

Utilisez toujours une phrase d'introduction pour décrire l'objectif du tableau. Évitez d'utiliser des tableaux au milieu de procédures numérotées. Envisagez plutôt d'utiliser une liste.

#### Unités de mesure {#units-of-measurement}

Pour le HTML et le Markdown, utilisez une espace insécable (&nbsp) entre le nombre et l'unité lors de la spécification d'une unité de mesure. Cela inclut la plupart des unités de mesure telles que la distance, les pixels, les points, le poids et les degrés de température (entre le degré et l'unité de mesure).

Pour la devise, le pourcentage ou les degrés d'un angle, n'utilisez pas d'espace entre le nombre et l'unité.

Pour les plages de nombres avec des unités, répétez l'unité pour chaque nombre. De même, pour les taux, utilisez « par » au lieu d'une barre oblique (/).

### Liens {#linking}

#### Liens de référence croisée {#cross-reference-links}

Utilisez des références croisées pour guider les utilisateurs vers des ressources supplémentaires. Dans la documentation Braze, utilisez des URL relatives à la racine du site pour créer des liens vers d'autres documents Braze (remplacez « www.braze.com/docs » par « {{site.baseurl}} »).

Évitez d'ajouter plusieurs liens vers le même document sur une même page, car cela peut provoquer une fatigue des liens. Les liens en double sont acceptables avec modération si vous créez un lien vers une section spécifique d'une autre page, ou si la page source est longue.

#### Intégration de vidéos {#embedding-videos}

Comme pour les images, utilisez des vidéos pour créer de la variété dans vos supports pédagogiques. La plupart des gens apprennent mieux avec une combinaison de supports, alors assurez-vous que tout contenu inclus dans une vidéo est également couvert dans l'article ou la leçon.

Pour intégrer une vidéo dans la documentation Braze, consultez [Embedded Video Test]({{site.baseurl}}/home/styling_test_page/#embedded-video-test).

#### En-têtes comme cibles de liens {#headings-as-link-targets}

Dans la documentation Braze, les ancres sont automatiquement créées pour les en-têtes. Cependant, vous pouvez vouloir ajouter une ancre personnalisée à un en-tête si :

* Votre ancre générée automatiquement est très longue.
* Votre en-tête est susceptible d'être fréquemment lié. L'ajout d'une ancre personnalisée réduit la probabilité de casser des liens si le texte de l'en-tête est modifié ultérieurement.

Pour ajouter une ancre à un en-tête dans la documentation Braze, consultez [Custom Anchors]({{site.baseurl}}/home/styling_test_page/#custom-header-anchor).

#### Texte de lien {#link-text}

Un texte de lien efficace contribue à améliorer la trouvabilité, la découvrabilité et l'accessibilité de votre contenu.

##### Structurer les liens {#structuring-links}

Utilisez l'un des formats suivants lors de la rédaction de liens :

* Faites correspondre le texte du lien au titre ou à l'en-tête de la destination du lien.
* Utilisez une description de la destination du lien comme texte de lien.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire : <em>Faire correspondre le texte du lien au titre ou à l'en-tête de la destination du lien.</em></th><th style="width: 50%;">À faire : <em>Utiliser une description de la destination du lien comme texte de lien.</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Commencez avec le <a href="{{site.baseurl}}/user_guide/getting_started/web_sdk/">SDK Web</a> de Braze.</td><td style="width: 50%;">Pour connaître votre cluster ou endpoint spécifique, <a href="{{site.baseurl}}/braze_support/">contactez le support</a>.</td></tr>
<tr><td style="width: 50%;">Pour plus d'informations, consultez <a href="{{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/">Annuler les messages Liquid</a>.</td><td style="width: 50%;">En cas de doute, vous pouvez toujours <a href="{{site.baseurl}}/user_guide/administrative/access_braze/accessing_your_account/#resetting-your-password">réinitialiser votre mot de passe</a>.</td></tr>
</tbody>
</table>
{:/}

Vous devrez peut-être reformuler une phrase pour créer un bon texte de lien.

Si vous créez un lien vers une section de la même page, utilisez une formulation standard qui indique cette action. Par exemple :

* Sur cette page, consultez [en-tête].
* Dans ce document, consultez [en-tête].
* Pour plus d'informations, consultez la section [en-tête].

##### Rédiger des liens {#writing-links}

Appliquez les directives suivantes lors de la rédaction du texte de lien :

* Placez le lien dans les mots-clés pertinents.
* Si vous rédigez une phrase complète qui renvoie le lecteur à un autre article, utilisez la formule « Pour plus d'informations, consultez » ou « Pour plus d'informations sur [sujet], consultez ».
* N'ajoutez une phrase « En savoir plus… » que si le texte d'aide aborde plus d'un concept, chacun pouvant être lié à son propre document d'aide. Dans ce cas, choisissez le lien le plus approprié et contextualisez-le avec « En savoir plus… »
* Pour garder un ton informel, n'utilisez pas « veuillez » pour introduire le texte de lien. Par exemple, évitez les formules « Veuillez consulter », « Veuillez voir » et « Veuillez contacter ».
* Rédigez un texte de lien unique et descriptif qui a du sens sans le texte environnant. Les recherches du [Nielsen Norman Group](https://www.nngroup.com/articles/link-promise/#links-should-stand-alone) (NN/g) montrent que les lecteurs parcourent la page à la recherche d'informations saillantes, alors assurez-vous que les liens peuvent se suffire à eux-mêmes.
* N'utilisez pas les mots ou expressions suivants comme texte de lien. Ils nuisent à l'accessibilité et à la lisibilité.
 * En savoir plus (seul)
 * Cliquez ici
 * ici
 * ce document
 * cet article

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire : <em>S'assurer que le texte du lien a du sens sans le texte environnant</em></th><th style="width: 50%;">À éviter : <em>Utiliser un texte de lien vague ou non descriptif</em></th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Pour plus d'informations sur l'importation de données client, consultez <a href="{{site.baseurl}}">Importation d'utilisateurs</a>.</td><td style="width: 50%;">Pour plus d'informations, <a href="{{site.baseurl}}">cliquez ici</a>.</td></tr>
<tr><td style="width: 50%;">Cette fonctionnalité se connecte à l'endpoint <a href="{{site.baseurl}}">Track users</a>.</td><td style="width: 50%;">Consultez <a href="{{site.baseurl}}">cet article</a>.</td></tr>
<tr><td style="width: 50%;">En savoir plus sur <a href="{{site.baseurl}}">les nouveautés du SDK Android 16.0.0</a>.</td><td style="width: 50%;">Suivez les instructions <a href="{{site.baseurl}}">ici</a>.</td></tr>
<tr><td style="width: 50%;">En savoir plus sur la <a href="https://www.braze.com/product">plateforme Braze</a>.</td><td style="width: 50%;">Pour les étapes, consultez <a href="{{site.baseurl}}">ce document</a>. <a href="{{site.baseurl}}">En savoir plus</a>.</td></tr>
<tr><td style="width: 50%;">Les clés API Storefront sont uniques par vitrine Hydrogen, mais leurs portées d'autorisation sont partagées par toutes les vitrines Hydrogen. En savoir plus sur les <a href="{{site.baseurl}}">jetons API Storefront.</a></td><td style="width: 50%;">Les <a href="{{site.baseurl}}">jetons API Storefront</a> sont uniques par <a href="{{site.baseurl}}">vitrine Hydrogen</a>, mais leurs <a href="{{site.baseurl}}">portées d'autorisation</a> sont partagées entre toutes les vitrines Hydrogen.</td></tr>
</tbody>
</table>
{:/}

#### Liens pour les endpoints {#links-for-endpoints}

Lorsque vous faites référence à des articles d'endpoints, assurez-vous d'utiliser un [texte de lien significatif](https://docs.google.com/document/d/e/2PACX-1vTluyDFO3ZEV7V6VvhXE4As_hSFwmnFFdU9g6_TrAYTgH1QmbRoEDDdn5GzKAB9vdBbIdyiFdoaJcNk/pub#h.79ujl0qtumog) qui a du sens hors contexte. Si vous utilisez le chemin de l'endpoint comme lien, assurez-vous de fournir des détails dans le texte environnant car le chemin peut ne pas communiquer clairement la fonction de l'endpoint.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire</th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Supprimez les profils utilisateur à l'aide de l'<a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">endpoint Delete user</a> de Braze.</td><td style="width: 50%;">Supprimez les profils utilisateur à l'aide de l'endpoint <a href="{{site.baseurl}}/api/endpoints/user_data/post_user_delete/">Delete user</a> de Braze.</td></tr>
<tr><td style="width: 50%;"><a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/">endpoint <code>/users/export/id</code></a></td><td style="width: 50%;">endpoint <a href="{{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/"><code>/users/export/id</code></a></td></tr>
</tbody>
</table>
{:/}

#### Liens de téléchargement de fichiers {#links-for-file-download}

Si un lien télécharge un fichier, indiquez-le clairement dans le texte du lien et mentionnez le type de fichier.

{::nomarkdown}
<table class="style-guide-table" style="table-layout: fixed; width: 100%;">
<thead>
<tr><th style="width: 50%;">À faire : <em>S'assurer que le texte du lien communique que le sélectionner télécharge un fichier</em></th><th style="width: 50%;">À éviter</th></tr>
</thead>
<tbody>
<tr><td style="width: 50%;">Pour des conseils, téléchargez le <a href="{{site.baseurl}}">PDF Aide-mémoire Regex</a>.</td><td style="width: 50%;">Consultez notre <a href="{{site.baseurl}}">Aide-mémoire RegEx</a>.</td></tr>
<tr><td style="width: 50%;">Pour plus d'informations, téléchargez le <a href="{{site.baseurl}}">PDF Manuel des services de réussite et de support</a>.</td><td style="width: 50%;"><a href="{{site.baseurl}}">Manuel des services de réussite et de support</a></td></tr>
</tbody>
</table>
{:/}

#### Liens vers d'autres sites {#links-to-other-sites}

En règle générale, ne créez pas de lien vers un autre site si vous pouvez couvrir l'information avec une brève explication. Nous ne pouvons pas suivre quand le contenu d'un autre site change.

Si vous créez un lien vers un site externe, assurez-vous que le site vers lequel vous créez le lien est de haute qualité, fiable et respectable. Si possible, créez un lien vers l'en-tête le plus pertinent d'une page.

Utilisez une icône de lien externe pour indiquer que le lien mène à un domaine différent. Pour la documentation Braze, cela est automatiquement appliqué aux liens externes.

#### URL pour les images {#urls-for-images}

Dans la documentation Braze, utilisez des URL relatives à la racine du site pour créer des liens vers les images. Pour plus d'informations, consultez [Ajouter et modifier des images](https://github.com/braze-inc/braze-docs/wiki/Editing-Content#adding-and-editing-images).

### Glossaire {#glossary}

⚠️ = À utiliser avec précaution, consultez les notes pertinentes
⛔️ = À ne pas utiliser

#### Chiffres

**24/7**
Utilisez un trait d'union (24-7) uniquement lorsqu'il est utilisé comme modificateur avant un nom.

**2D / bidimensionnel**

**3D / tridimensionnel**

#### A

**test A/B**

⚠️ **abort**
Évitez d'utiliser sauf pour faire référence à un processus spécifiquement nommé. Utilisez plutôt des mots comme « arrêter », « quitter », « annuler » ou « terminer ».

**boutons d'action**

**livraison par événement**
En minuscules sauf lorsque vous faites référence à un élément d'interface en majuscules.

⛔️ **ad hoc**
À ne pas utiliser. Utilisez « ponctuel » ou similaire.

**IA**
Préféré à « intelligence artificielle » après la première mention.

**AI item recommendation**

**Alloys / Braze Alloys**
Toujours en majuscules.

**alphanumérique**
Sans trait d'union.

**always-on**

**am**
En minuscules lorsqu'il est utilisé pour l'heure (par exemple, « 10 am »). Voir aussi [pm](#glossary).

**Amazon S3**

**Amazon Web Services (AWS)**
Toujours en majuscules. Développez à la première mention, puis il est acceptable d'utiliser l'acronyme.

**AMP for Email / Braze AMP for Email**

**Android**

**API / Interface de programmation d'applications**
Développez à la première mention, puis il est acceptable d'utiliser l'acronyme.

**Clé API**

**APNs / Apple Push Notification service**

**⛔️ groupe d'applications**
À ne pas utiliser. Le groupe d'applications a été renommé en espace de travail.

**Plateforme Apple iOS**

**AppleWatch**

**.avro**

#### B

**comportement, comportements**

**Benchmarks**

**bêta**

**BI Insights**

**binge-watching**

**Binge-watch**

**Bonfire / communauté Bonfire / communauté Braze Bonfire**
Utilisez « communauté Braze Bonfire » à la première mention, puis il est acceptable d'utiliser simplement « Bonfire » ou « communauté Bonfire ».

**booléen**

⛔️ **blacklist**
À ne pas utiliser. Utilisez plutôt « liste de blocage » ou « liste de refus ». Pour la forme verbale de ces mots, envisagez de reformuler la phrase pour supprimer le terme problématique. Par exemple :

>✅ **Recommandé :** Pour empêcher une propriété existante d'être utilisée dans de nouveaux messages, sélectionnez **Gérer les propriétés**. <br>
>⛔️ **Non recommandé :** Pour mettre sur liste de blocage une propriété existante, sélectionnez **Gérer les propriétés**.

**Webhook Braze-to-Braze**

**Aide à la décision (BI)**
Développez à la première mention, puis il est acceptable d'utiliser l'acronyme.

#### C

**California Consumer Privacy Act (CCPA)**
Développez à la première mention, puis il est acceptable d'utiliser l'acronyme. Voir aussi [conformité CCPA (nom) / conforme au CCPA (adjectif)](#ccpa-compliance)

**can**
Utilisez « can » pour faire référence à une action ou un résultat facultatif. Par exemple :

> ✅ **Recommandé :** Vous pouvez également télécharger et mettre à jour les profils utilisateur avec des fichiers CSV.
> ✅ **Recommandé :** Le processus d'importation peut prendre quelques minutes.

N'utilisez pas « can » pour les instructions. Préférez plutôt le verbe à l'impératif. Pour des exemples, consultez [Deuxième personne et première personne](#second-person-and-first-person).

**Canvas**
Toujours en majuscules. Le pluriel est « Canvas ».

**Canvas Flow**
À utiliser pour différencier l'éditeur Canvas original de Canvas Flow. Sinon, utilisez « Canvas ».

**campagne**
En minuscules sauf lorsque vous faites référence à un élément d'interface en majuscules.

**capacité**
À utiliser pour faire référence aux limites de données personnalisées au lieu du mot « limite ».

**catalogue**
En minuscules sauf lorsque vous faites référence à un élément d'interface en majuscules.

**conformité CCPA (nom) / conforme au CCPA (adjectif)** {#ccpa-compliance}

**CEO, CFO, CMO, COO, CTO**

**churn**
À utiliser pour faire référence au taux de désabonnement ou à la perte de clients.

**churn prediction**
En minuscules sauf lorsque vous faites référence à l'interface.

**case à cocher**

**Check-in (nom) / check in (verbe)**

**City x City**

**Cofondateur**

**Cartes de contenu / Braze Content Cards**

**Content Blocks**

**groupe de contrôle**

**conversion**

**analyse des groupes de conversion**
En minuscules.

**Cordova**

**Currents / Braze Currents**
Toujours en majuscules.

**CRM / gestion de la relation client**
Développez à la première mention, puis il est acceptable d'utiliser l'acronyme.

**communication cross-canal / personnalisation cross-canal**

**C-suite**

**CSV / valeurs séparées par des virgules**

**attributs personnalisés**
En minuscules sauf lorsque vous faites référence à un élément d'interface en majuscules.

**événements personnalisés**
En minuscules sauf lorsque vous faites référence à un élément d'interface en majuscules.

**attributs client**

**comportement des clients**

**plateforme de données client (CDP)**
En minuscules.

**engagement client**

**événements client**

**parcours client**

**autorisations du client**

**rétention client**

#### D

**Thème mode sombre / Prévisualisation mode sombre / concept de mode sombre**

**tableau de bord / tableau de bord de Braze**
À utiliser pour faire référence à Braze en tant que plateforme. Utilisez les minuscules (tableau de bord, pas Tableau de bord).

**piloté par les données (adjectif)**

**confidentialité des données**

**fiche technique**

**streaming de données**

**DAU / Utilisateurs actifs par jour**

**Arbres décisionnels**

**création de liens profonds**

**Messages différés**

**Temps d'arrêt**

**glisser-déposer (verbe) / glisser-déposer (adjectif)** {#drag-and-drop}
À utiliser pour faire référence au glissement de fichiers dans une zone de téléchargement.

**Éditeur par glisser-déposer**
Utilisez la casse de titre lorsque vous faites référence à la fonctionnalité dans l'interface. Sinon, utilisez les minuscules (éditeur par glisser-déposer). Utilisez le verbe lorsque vous faites référence à la façon dont les clients peuvent [glisser-déposer](#drag-and-drop) des éléments dans l'éditeur.

**approfondir (verbe) / approfondissement (nom ou adjectif)**
À utiliser dans le contenu sur les données et les rapports générés à partir de celles-ci.

**DTC / direct au consommateur**

**contenu dynamique**

#### E

**accès anticipé**

⛔️ **e.g.**
À ne pas utiliser. Utilisez les expressions « par exemple », « comme » ou similaire.

**eBook**

**e-commerce**
Pas « ecommerce » ou « eCommerce ».

**écosystème**

**e-mail**
Pas « Email » ou « e-mail ».

**livrabilité des e-mails**

**réputation e-mail**

**EMEA (Europe, Moyen-Orient et Asie)**

**emoji**
Forme singulière et plurielle.

**utilisateur final (nom) / d'utilisateur final (adjectif)**
Préférez « vos utilisateurs » à « utilisateurs finaux ».

⚠️ **ensure**
Évitez d'utiliser lorsque vous parlez de ce qu'une fonctionnalité fait. Consultez [Éviter les garanties](#avoid-guarantees) pour plus d'informations.

**ESP / fournisseur de services d'e-mailing**

**prédiction d'événement**

**propriétés d'événement / propriétés d'événement personnalisé**
En minuscules sauf lorsque vous faites référence à un élément d'interface en majuscules.

**événements d'exception**

**extraire**
Utilisez « extraire » au lieu de « dézipper » pour faire référence à l'extraction de fichiers d'un dossier compressé.

**ID externe**
Pas « External ID ». Lorsque vous faites référence à des extraits de code, utilisez external_id.

#### F

**Facebook**

**FCM / Firebase Cloud Messaging**

**Firebrand / Firebrands**

**Forge [ANNÉE]**

**limite de fréquence**

**Plein écran**
Lorsqu'il est utilisé comme adjectif (par exemple, « Messages in-app plein écran »), sans trait d'union.

#### G

**RGPD / Règlement général sur la protection des données**
Développez à la première mention, puis il est acceptable d'utiliser l'acronyme.

**conformité RGPD (nom) / conforme au RGPD (adjectif)**

**géorepérage**

**GIF**

**GitHub**
Pas « Github » ou « github ».

**Google / googlable**

#### H

**Haute performance**

**Actions à forte valeur**

**QG / siège social**

**Éditeur d'e-mail HTML**

**HTTP**

#### I

⛔️ **i.e.**
À ne pas utiliser. Utilisez l'expression « c'est-à-dire » ou similaire.

**messages in-app**

**message dans le navigateur (IBM)**

**infographie**

**attribution d'installation**

**entier**

**Intelligence Suite**
Utilisez la casse de titre.

**Canal intelligent**
Utilisez la casse de titre.

**Sélection intelligente**
Utilisez la casse de titre.

**Timing intelligent**
Utilisez la casse de titre.

⛔️ **Internet des objets**
À ne pas utiliser.

**iOS**

**Réchauffement d'adresses IP**

**iPad**

**iPhone**

**IT**

#### J

**JavaScript**

**JPEG / JPG**

**JSON / JavaScript Object Notation**

#### K

**Keynote (programme) / keynote (nom)**

**lancer (verbe) / lancement (nom)**

⚠️ **kill**
Évitez d'utiliser sauf pour faire référence à un processus spécifiquement nommé. Utilisez plutôt des mots comme « arrêter », « quitter », « annuler » ou « terminer ».

**KPI / indicateur clé de performance**

#### L

**page d'accueil**

**cycle de vie**

**Taux d'amélioration**

**LinkedIn**

**Liquid**
Toujours en majuscules.

**Prévisualisation instantanée**

**long terme (nom) / à long terme (adjectif)**

**LTV / Valeur vie client**

#### M

**technologie marketing**
Préféré à « martech ».

**MAU / Utilisateurs actifs par mois**

**maximum**
Pas « max ».

**bibliothèque multimédia**
En minuscules sauf lorsque vous faites référence à un élément d'interface en majuscules.

**Microsoft**

**Microsoft Azure**

**ML / machine learning**

**marketing mobile**

**automatisation du marketing mobile**

**moment mobile**

**téléphone mobile**

**campagne multicanal**
En minuscules sauf lorsque vous faites référence à un élément d'interface en majuscules. Sans trait d'union.

**support multilingue**

**test multivarié**

#### N

**N/A**
Pas « NA ». Utilisez « N/A » selon les besoins dans les tableaux pour indiquer le contenu de colonne ou de ligne qui ne s'applique pas à une cellule particulière. Dans le texte en ligne, préférez « non disponible » ou « non applicable » pour plus de clarté.

⚠️ **nouveau**
Évitez d'utiliser dans la documentation produit et le matériel pédagogique, car cela peut rapidement dater votre contenu. Pour plus d'informations, consultez [Fonctionnalités futures](#describing-limitations).

**NRT / quasi temps réel (adjectif) / quasi temps réel (nom)**

**NYC / New York City**

#### O

**à la demande**

**onboarding**

**une fois**
À utiliser pour faire référence à l'exécution d'une action une seule fois. N'utilisez pas « une fois » à la place de « après » ou « lorsque ».

**taux d'ouverture (OR)**

**demande d'abonnement**

**orchestration**

**OS / Système d'exploitation**

**OTT / Services de médias over-the-top**

⛔️ **clé en main**
À ne pas utiliser. Utilisez plutôt une alternative comme « par défaut ».

#### P

**partenaire, partenaires, partenariat**

**persona (singulier) / personas (pluriel)**

**personnalisation**

**informations personnellement identifiables (PII)**

**Personalized Path**
Utilisez la casse de titre.

**Personalized Variant**
Utilisez la casse de titre.

**PhD / PhDs**

**pm**
En minuscules lorsqu'il est utilisé pour l'heure (par exemple, « 10 pm »). Voir aussi [am](#glossary).

**précédent**

**prédiction**
En minuscules sauf si précédé de « Braze », comme « Une Braze Prediction est… ».

**analyse prévisionnelle**

**Predictive Churn**
Utilisez la casse de titre. Predictive Churn est le nom du produit, tandis que les clients créent une [churn prediction](#glossary).

**Predictive Events**
Utilisez la casse de titre.

**Predictive Purchases**
Utilisez la casse de titre. Predictive Purchases est le nom du produit, tandis que les clients créent une [purchase prediction](#glossary).

**Predictive Suite**
Utilisez la casse de titre.

**centre de préférences**
En minuscules sauf lorsque vous faites référence à un élément d'interface en majuscules.

**amorçage de localisation**

**amorçage de push**

**code de promotion**
En minuscules sauf lorsque vous faites référence à un élément d'interface en majuscules. N'utilisez pas « code promo ».

**purchase prediction**
En minuscules sauf lorsque vous faites référence à un élément d'interface en majuscules.

**propriétés d'achat**
En minuscules sauf lorsque vous faites référence à un élément d'interface en majuscules.

**boutons d'action push**

**Push Max**
Utilisez la casse de titre.

**notification push**

**Push Stories**
Utilisez la casse de titre.

#### Q

**Q&R**

⛔️ **QA (assurance qualité)**
N'utilisez pas l'acronyme comme verbe. Reformulez plutôt en « effectuer une assurance qualité ».

**heures calmes**
Utilisez « Heures calmes » en début de phrase et « heures calmes » en milieu de phrase. N'utilisez pas la casse de titre « Heures Calmes » car ce n'est pas une fonctionnalité de marque.

⚠️ **rapide / rapidement**
Évitez d'utiliser. Ce qui est rapide pour vous peut ne pas l'être pour d'autres. Pour des directives connexes, consultez [Langage condescendant](#condescending-language).

#### R

**limite de débit**

**temps réel (nom) / en temps réel (adjectif)**

**réengagement**

⚠️ **expression régulière / regex**
Préférez la version développée à son abréviation « regex ». N'utilisez pas « RegEx ».

**marketing relationnel**

**reciblage**

**rétention**

**push riche**

**clic droit**

**balayage vers la droite**

**ROI / retour sur investissement**

#### S

**Sage AI by Braze™**

⛔️ **sanity check**
À ne pas utiliser. Utilisez plutôt un terme comme « vérification rapide » ou « vérification préliminaire ». Vous pouvez aussi introduire les instructions de vérification avec une phrase comme « Vérifions que tout fonctionne correctement ».

**livraison planifiée**
En minuscules sauf lorsque vous faites référence à un élément d'interface en majuscules.

**capture d'écran**

**capture d'écran**

**SDK / Kit de développement logiciel**

**segment (audience)**

**Extensions de segments**
Utilisez la casse de titre.

**Statistiques des segments**
Utilisez la casse de titre.

**Segmentation**

**sélection**
Comme dans la fonctionnalité au sein des catalogues. En minuscules sauf lorsque vous faites référence à un élément d'interface en majuscules.

**SF / San Francisco**

**Silicon Valley**

**silo, silos, cloisonné**

**enquête simple**

**diaporama**

**Smartphone**

**Smartwatch**

**SMS**

**logiciel en tant que service (SaaS)**
Développez à la première mention, puis il est acceptable d'utiliser l'acronyme.

**tests de courrier indésirable**

**SQL / langage de requête structuré**

**Extensions de segments SQL**
Utilisez la casse de titre.

**adhérence**

**streaming**

**chaîne de caractères**
Pour les audiences non techniques, définissez une chaîne de caractères comme du texte contenant des « caractères alphanumériques ». Pour les audiences techniques, il n'est pas nécessaire de définir ce terme.

**groupe d'abonnement**

**temporisation**

#### T

**réponse ciblée**

⚠️ **terminate**
Évitez d'utiliser sauf pour faire référence à un processus spécifiquement nommé. Utilisez plutôt des mots comme « arrêter », « quitter », « annuler » ou « terminer ».

**tiers**

**fuseau horaire**
Pas « timezone ».

**horodatage**

**écran tactile**

**message déclenché**

**Twitter**

#### U

**UK / Royaume-Uni**

⛔️ **dézipper**
À ne pas utiliser. Utilisez plutôt « extraire ».

**URL**
Prononcé comme les lettres individuelles U-R-L, donc écrivez « une URL ». Utilisez les majuscules. Pour les pluriels, utilisez URL.

**US / USA**
Sans points.

**cas d'utilisation**

**attributs utilisateur / attributs utilisateur par défaut**
À utiliser pour faire référence aux données utilisateur automatiquement capturées par Braze.

**profil utilisateur**

**nom d'utilisateur**

⚠️ **utiliser**
N'utilisez pas « utiliser » quand vous voulez dire « employer ». Utilisez « utiliser » pour faire référence à quelque chose qui est employé au-delà de son objectif initial prévu.

#### V

**variante**

⛔️ **via**
À ne pas utiliser. Utilisez plutôt des termes comme « par » ou des expressions comme « au moyen de » ou « par le biais de ».

⛔️ **vice versa**
À ne pas utiliser. Utilisez plutôt des termes comme « inversement » ou une expression comme « l'inverse ».

**en lecture seule**

⚠️ **vs.**
N'utilisez pas « vs. » comme abréviation de « versus ». Écrivez plutôt le mot en entier.

#### W

**communication web**

**web push**

**webhook**

**webinaire**

**marque blanche**

⛔️ **whitelist**
À ne pas utiliser sauf pour faire référence à l'interface. Utilisez plutôt « liste d'autorisation » ou « liste sûre ». Pour la forme verbale de ces mots, envisagez de reformuler la phrase pour supprimer le terme problématique. Pour des exemples, consultez [blacklist](#glossary).

⚠️ **Wi-Fi**
N'utilisez pas « WiFi », « wi-fi » ou « wifi ».

**will**
Évitez d'utiliser « will » ou « would ». Consultez [Présent](#present-tense).

**Winning Path**
Utilisez la casse de titre.

**Winning Variant**
Utilisez la casse de titre.

⛔️ **wizard**
À ne pas utiliser. Utilisez plutôt « compositeur ».

**WordPress**

**espace de travail**

**www**

#### Y

**YAML**
N'utilisez pas d'extension de fichier pour faire référence au type de fichier. Par exemple, utilisez « fichier YAML » au lieu de « fichier .yaml ».

**YouTube**

#### Z

**code postal**

**fichier zip / fichiers zippés**

**ZIP**
N'utilisez pas d'extension de fichier pour faire référence au type de fichier. Par exemple, utilisez « fichier ZIP » au lieu de « fichier .zip ».