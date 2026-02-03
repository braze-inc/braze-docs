---
nav_title: Accessibilité
article_title: Créer des messages accessibles en Braze
page_order: 0.5
page_type: reference
description: "Cet article de référence explique pourquoi il est important de prendre en compte l’accessibilité dans votre contenu marketing et comment vous pouvez créer des messages accessibles dans Braze."
---

# Créer des messages accessibles en Braze

> Comprenez pourquoi l'accessibilité est importante à prendre en compte dans votre contenu marketing, et comment vous pouvez créer des messages accessibles dans Braze. Pour plus de conseils, consultez notre cours d'apprentissage sur [les fondements de l'envoi de messages accessibles](https://learning.braze.com/accessible-messaging-foundations) sur Braze.

Le contenu marketing qui exclut les personnes présentant un handicap, même involontairement, peut empêcher des millions de personnes d’interagir avec votre marque. L'accessibilité en marketing consiste à permettre à chacun de faire l'expérience de votre marketing, de comprendre votre communication et d'avoir la possibilité d'investir dans votre produit, votre service ou votre marque ou d'en devenir fan. 

Lorsque vous concevez vos envois de message, prenez le temps de réfléchir à la façon dont vous pouvez rendre vos conceptions accessibles à tous vos clients.

{% alert important %}
Ce contenu est destiné à servir d'orientation générale et ne garantit pas la conformité aux normes d'accessibilité telles que les WCAG. Braze propose des outils qui facilitent la création de messages plus accessibles, mais il vous incombe de veiller à ce que votre contenu final réponde aux exigences applicables. L'accessibilité est un sujet complexe qui comporte de nombreux éléments mobiles. De nombreuses entreprises travaillent avec des spécialistes de l'accessibilité ou des consultants pour s'assurer que leur contenu, leur conception et leurs pratiques de développement répondent aux besoins de tous les utilisateurs.
{% endalert %}

## L'accessibilité à Braze

Soutenir la communication accessible signifie rester ouvert, curieux et désireux d'apprendre. Chez Braze, nous avons à cœur d'aider les gens à se connecter, et nous savons que faire de la place à tout le monde fait partie d'un bon travail. L'accessibilité n'est pas une chose que nous considérons comme acquise et nous nous réjouissons de pouvoir continuer à apprendre.

{% multi_lang_include accessibility/feedback.md %}

## Domaines d’invalidité à envisager

*Cette section est partiellement adaptée de [W3C : Capacités et obstacles divers](https://www.w3.org/WAI/people-use-web/abilities-barriers/).*

{% tabs local %}
{% tab Visual %}

Les handicaps visuels peuvent varier d’une perte de vision légère ou modérée dans un œil ou les deux yeux, à une perte de vision importante ou complète dans les deux yeux. Certaines personnes ont une sensibilité réduit ou absente pour certaines couleurs ou ont une sensibilité plus fortes aux couleurs vives.

Pour interagir avec votre contenu, ces utilisateurs ont besoin de :

- Agrandir ou réduire la taille du texte et des images
- Personnaliser les paramètres des polices, couleurs et espacement
- Écouter une synthèse vocale du contenu (c’est-à-dire, utiliser un lecteur d’écran)
- Écouter des descriptions audio de la vidéo
- Lire le texte à l’aide de braille actualisable

{% alert note %}
- Dans le monde, au moins 2,2 milliards de personnes souffrent d'une déficience visuelle de près ou de loin (voir [OMS](https://www.who.int/news-room/fact-sheets/detail/blindness-and-visual-impairment)).
- Environ 1 homme sur 12 et 1 femme sur 200 présentent un certain degré de déficience de la vision des couleurs, soit environ 300 millions de personnes dans le monde (voir [NHS](https://www.nhs.uk/conditions/colour-vision-deficiency/)).
{% endalert %}

{% endtab %}
{% tab Hearing %}

Les handicaps de l'ouïe ou de l'audition peuvent inclure une déficience auditive légère à modérée dans une oreille ou les deux. Même une perte d’audition partielle peut s’avérer problématique en ce qui concerne le contenu audio.

Pour comprendre votre contenu, ces utilisateurs comptent sur :

- Transcriptions et légendes du contenu audio
- Des lecteurs multimédia qui affichent des légendes et fournissent des options pour ajuster la taille du texte et les couleurs des légendes
- Options d’arrêt, de pause et d’ajustement du volume du contenu audio (indépendamment du volume du système)
- Audio de premier plan de haute qualité, clairement reconnaissable par rapport aux bruits de fond

{% alert note %}
- Une personne sur huit aux États-Unis (13 % ou 30 millions) âgée de 12 ans ou plus présente une perte auditive dans les deux oreilles, selon les examens d’audition standard
- Environ 15 % des adultes américains (37,5 millions) âgés de 18 ans et plus déclarent avoir des problèmes d'audition (voir [NIH](https://www.nidcd.nih.gov/health/statistics/quick-statistics-hearing)).
{% endalert %}

{% endtab %}
{% tab Physical %}

Les handicaps physiques peuvent comprendre une faiblesse et des limitations dans le contrôle ou la sensation musculaire, des troubles articulaires, des douleurs qui gênent les mouvements et des membres manquants.

Ces utilisateurs s’appuient sur le support clavier pour activer la fonctionnalité (même s’ils n’utilisent pas de clavier standard). Pour interagir avec votre contenu, ces utilisateurs ont besoin de :

- Larges zones cliquables
- Suffisamment de temps pour terminer les tâches
- Indicateurs visibles du sujet actuel
- Mécanismes permettant de sauter des blocs de contenu, comme des en-têtes de page ou des barres de navigation

{% alert note %}
Près de 2 millions de personnes aux États-Unis vivent avec une perte de membre (voir [Amputee Coalition](https://www.amputee-coalition.org/limb-loss-resource-center/resources-filtered/resources-by-topic/limb-loss-statistics/limb-loss-statistics/#1)).
{% endalert %}

{% endtab %}
{% tab Cognitive %}

Les troubles cognitifs, d’apprentissage et neurologiques impliquent la neurodiversité et les troubles neurologiques, ainsi que les troubles comportementaux et mentaux qui ne sont pas nécessairement neurologiques. Ils peuvent affecter n’importe quelle partie du système nerveux et influencer la façon dont les personnes entendent, se déplacent, voient, parlent et comprennent les informations.

Selon leurs besoins individuels, ces utilisateurs comptent sur :

- Contenu clairement structuré
- Étiquetage cohérent des formulaires, des boutons et autres contenus
- Cibles de liens prévisibles et interaction globale
- Différentes façons de naviguer, comme les menus et les barres de recherche
- Paramètres pour désactiver le clignotement ou un contenu provoquant des distractions
- Texte plus simple soutenu par des images


{% alert note %}
- Aux États-Unis, une personne sur cinq souffre de troubles de l'apprentissage et de l'attention (voir [LDA](https://ldaamerica.org/lda_today/the-state-of-learning-disabilities-today/#:~:text=LD%20Today,have%20learning%20and%20attention%20issues.)).
- Environ 10 à 20 % de la population mondiale est considérée comme neurodivergente (voir [Deloitte](https://www2.deloitte.com/us/en/insights/topics/talent/neurodiversity-in-the-workplace.html)).
- Environ 1 enfant sur 100 est atteint d'autisme dans le monde (voir [OMS](https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders)).
{% endalert %}

{% endtab %}
{% endtabs %}

## Bonnes pratiques

La création d'un contenu accessible ne doit pas être une tâche insurmontable. De petits choix réfléchis peuvent faire une grande différence. Cette section présente des conseils pratiques qui permettent à un plus grand nombre de personnes de lire vos messages, d'y naviguer et d'interagir avec eux. Qu'il s'agisse d'ajuster votre texte, de styliser vos boutons ou d'ajouter un texte alt aux images, chaque modification s'ajoute à une expérience plus inclusive. Voyons ce qu'il en est.

### Contenu

#### Structure et flux

Commençons par les fondations. Lorsque votre contenu a une structure claire, il est plus facile à suivre pour tout le monde, en particulier pour les personnes qui utilisent des lecteurs d'écran ou la navigation au clavier.

- **Divisez votre contenu en sections :** L'utilisation de titres, de puces et de listes aide les gens à comprendre et à parcourir rapidement votre contenu, même lorsqu'ils sont pressés. 
- **Ne sautez pas de niveaux de rubriques :** Les titres structurent votre contenu et aident les lecteurs à comprendre rapidement les liens entre les différentes sections. Lorsque vous sautez des niveaux de rubriques (par exemple, en passant directement d'une rubrique H2 à une rubrique H4), vous rompez cette structure logique. Il est donc plus difficile pour les utilisateurs, notamment ceux qui utilisent des lecteurs d'écran, de naviguer et de comprendre clairement votre message. Respectez toujours une hiérarchie logique et séquentielle des titres (H1, H2, H3, etc.) pour vous assurer que votre contenu reste organisé, accessible et facile à suivre pour tout le monde.

#### Lisibilité

Une fois votre structure en place, l'étape suivante consiste à s'assurer que vos mots sont faciles à lire. Cela signifie que les choses doivent rester simples, scannables et agréables à lire quel que soit l'appareil utilisé et les besoins de l'utilisateur.

- **Rédigez des phrases courtes et claires :** Les phrases courtes sont faciles à comprendre pour tout le monde, en particulier pour les personnes qui utilisent des lecteurs d'écran ou qui ont des difficultés à traiter des informations complexes. Écrivez à un niveau de lecture équivalent à la cinquième en France. Vous pouvez utiliser des ressources telles que [Hemingway App](https://hemingwayapp.com/) pour vérifier le niveau de lecture de votre texte.
- **Choisissez une taille de police et un espacement lisibles :** Un texte trop petit peut être difficile à lire, surtout sur un téléphone portable. Utilisez au moins 14 px pour le corps du texte. Agrandissez les titres pour que les utilisateurs puissent voir clairement la différence. Un espacement plus important entre les lignes (environ 1,5 ligne) et les paragraphes améliore la lisibilité, en particulier pour les personnes ayant des besoins visuels ou cognitifs.
- **Évitez les textes justifiés :** Le texte justifié crée un espacement inégal entre les mots, ce qui rend la lecture difficile pour les personnes souffrant de dyslexie ou de troubles cognitifs. Pensez à aligner à gauche le contenu qui s'étend sur plus de deux lignes pour les langues allant de gauche à droite ou à droite pour les [langues allant de droite à gauche]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages).
- **Utilisez les caractères gras, italiques et majuscules avec parcimonie :** Le fait de mettre trop d'emphase sur le texte rend la lecture difficile, en particulier pour les personnes souffrant de dyslexie ou de déficiences visuelles. Restez simple.

#### Clarté et facilité d'utilisation

Enfin, parlons des détails les plus fins, ceux qui permettent aux utilisateurs non seulement de voir votre contenu, mais aussi de le comprendre et d'interagir avec lui. 

- **Identifiez clairement les liens et les boutons :** Veillez à ce que le texte de votre [lien](#links) et de votre [bouton](#buttons) explique clairement ce qui se passe ensuite. Il aide les personnes qui utilisent des lecteurs d'écran ou qui naviguent avec un clavier à savoir à quoi s'attendre.
- **Allez-y doucement avec les symboles et les emojis :** Les caractères spéciaux et les emojis peuvent rendre votre contenu ludique, mais ils peuvent être source de confusion lorsqu'ils sont lus par des lecteurs d'écran. Utilisez-les avec parcimonie et veillez à ce qu'ils ne remplacent pas un texte clair et descriptif.
- **Test de troncature :** Testez toujours votre texte en [envoyant un message test]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) à un appareil pour vous assurer que votre texte n'est pas tronqué. Si votre message est coupé, cela nuit à la fois à vous et à votre audience, car cela empêche votre contenu de les atteindre.

### Boutons

Utilisez des **boutons** pour indiquer une action, comme l'envoi d'un formulaire ou la lecture d'un carrousel. Si vous naviguez vers une nouvelle URL, pensez à utiliser un [lien à](#links) la place.

#### Rédiger un texte clair et orienté vers l'action

Tout comme le texte des liens, les étiquettes des boutons doivent décrire clairement l'action. Un texte de bouton efficace est spécifique et orienté vers l'action. Par exemple, "Soumettre la commande" indique clairement à l'utilisateur ce qui se passera lorsqu'il cliquera, alors que "Soumettre" peut être ambigu. Chaque étiquette doit décrire précisément l'action prévue, afin que les lecteurs d'écran et tous les utilisateurs puissent facilement comprendre et prédire le résultat lorsqu'ils interagissent avec vos boutons.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bon texte de bouton <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Le texte du bouton est médiocre <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Soumettre la commande"</td>
      <td>"Soumettre"</td>
    </tr>
    <tr>
      <td>"Créer un compte"</td>
      <td>"Inscription</td>
    </tr>
    <tr>
      <td>"Téléchargez notre brochure</td>
      <td>"Télécharger"</td>
    </tr>
    <tr>
      <td>"Voir les détails du produit"</td>
      <td>"En savoir plus</td>
    </tr>
    <tr>
      <td>"S'abonner aux mises à jour"</td>
      <td>"S'abonner"</td>
    </tr>
  </tbody>
</table>

Veillez à ce que le texte du bouton soit concis afin d'éviter qu'il ne soit tronqué. Si le texte d'un bouton est trop long, il peut être coupé par une ellipse au lieu d'être enveloppé.

#### Utilisez un contraste de couleurs suffisant

Le texte du bouton doit être facile à lire sur la couleur d'arrière-plan du bouton. Vérifiez que le texte de votre bouton est conforme aux [normes minimales de contraste](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) WCAG 2.2 AA :

- Rapport de contraste de 4,5:1 pour un texte de taille normale (la plupart des boutons)
- Rapport de contraste de 3:1 pour les textes de grande taille (typiquement au-dessus de 18 pt)

Un contraste élevé permet aux boutons de rester lisibles et cliquables pour tout le monde, y compris pour les utilisateurs souffrant de déficiences visuelles ou pour ceux qui visualisent votre message dans des environnements difficiles. Pour plus d'informations, reportez-vous à la section sur le [contraste des couleurs](#color-contrast).

#### Faites en sorte que les boutons soient faciles à toucher

Assurez-vous que vos boutons (et vos liens) sont suffisamment grands et espacés pour les utilisateurs d'appareils mobiles. Les [cibles tactiles de](#touch-targets) petite taille ou encombrées peuvent être frustrantes, voire impossibles à utiliser pour les utilisateurs souffrant d'un handicap moteur.  

### Liens

Utilisez des liens pour la navigation, par exemple pour diriger les utilisateurs vers une page externe.

#### Rédigez un texte de lien descriptif

Écrivez le texte du lien qui décrit clairement l’endroit où se rendra l’utilisateur. Les utilisateurs de lecteurs d’écran passent souvent d’un lien à l’autre pour parcourir le contenu, assurez-vous donc que votre texte de lien s’explique de lui-même. Évitez les expressions comme « cliquez ici », « plus » et « cliquez pour obtenir des détails », car ils sont ambigus lorsqu’ils sont lus hors du contexte.

Par exemple, réfléchissez à la manière dont vous pourriez rédiger un lien pour afficher un rapport météorologique.

| Mauvais  | Mieux | Le meilleur |
| --- | --- | --- | 
| Cliquez ici | Cliquez ici pour accéder aux conditions météorologiques d’aujourd’hui | Météo d’aujourd’hui |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Comme avec tout contenu, faites en sorte qu’il soit direct avec le moins de mots supplémentaires possible.

#### Évitez de styliser les liens comme des boutons

Les éditeurs glisser-déposer de Braze produisent par défaut du HTML sémantique, de sorte que les liens n'y sont pas stylisés comme des boutons. Cependant, si vous travaillez avec du [HTML personnalisé](#custom-html) ou si vous apportez des modifications au niveau du code, gardez cela à l'esprit :

- Les **liens (`<a>`** ) répondent à la touche <kbd>Entrée.</kbd> 
- Les **boutons (`<button>`** ) réagissent à la fois à la touche <kbd>Entrée</kbd> et à la touche <kbd>Espace.</kbd> 

Le fait de donner à un lien l'apparence d'un bouton peut perturber les personnes qui naviguent à l'aide d'un clavier : elles pourraient essayer d'appuyer sur <kbd>Espace et</kbd> s'attendre à ce que cela fonctionne.

Utilisez le bon élément pour l'action :

- Utilisez `<button>` pour les actions, comme la soumission d'un formulaire ou l'ouverture d'une fenêtre modale, etc.
- Utilisez `<a>` pour la navigation, par exemple pour créer un lien vers une autre page ou un autre fichier.

{% raw %}

```html
<!-- Recommended: A true button for an action -->
<button type="button">Download report</button>

<!-- Not recommended: A link styled as a button -->
<a href="#" class="btn">Download report</a>
```

{% endraw %}

### Cibles à toucher

Les cibles tactiles sont toutes les parties de votre message sur lesquelles les utilisateurs appuient pour agir, comme les boutons, les liens ou les icônes. Ces éléments doivent être suffisamment grands et espacés pour que les gens puissent les toucher facilement, en particulier sur les appareils mobiles.

Lorsque les cibles tactiles sont trop petites ou trop proches les unes des autres, il peut être frustrant, voire impossible, pour les utilisateurs ayant des problèmes de mobilité ou de dextérité d'interagir avec votre message. L'amélioration de cet aspect peut contribuer à réduire les erreurs et à créer une expérience plus fluide pour tout le monde.

Voici ce qu'il faut retenir :
- **Utilisez une taille de ciblage adéquate.** Visez une taille minimale de 44 x 44 pixels pour les cibles tactiles. Ceci est conforme aux directives WCAG 2.2 pour les [ciblages tactiles](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) et aux normes courantes de convivialité mobile.
- **Donnez à chaque cible une marge de manœuvre.** Si les cibles de tapotement sont trop proches les unes des autres, comme des liens empilés ou des boutons étroitement groupés, il peut être facile de les manquer ou de tapoter sur la mauvaise cible. Ajoutez de l'espacement ou du rembourrage entre les éléments pour éviter cela.
- **Ne vous fiez pas uniquement aux images.** Même les petites icônes peuvent être rendues plus utilisables grâce à un rembourrage supplémentaire, ce qui leur permet de respecter les exigences minimales en matière de taille sans modifier la mise en page.
- **Prévisualisation sur mobile.** Testez votre message sur différentes tailles d'écran et assurez-vous que les éléments interactifs sont faciles à utiliser.

L'amélioration des ciblages tactiles est l'un des moyens les plus efficaces de rendre votre message plus accessible sur mobile - et c'est une bonne UX pour tout le monde.

### Images

#### Fournir un texte alternatif

Le texte alternatif (alt text) est une courte description du contenu ou de la fonction d'une image que les lecteurs d'écran et autres technologies d'assistance fournissent aux utilisateurs. Pour chaque image significative, rédigez un texte alt descriptif afin que les utilisateurs qui ne peuvent pas voir les images comprennent quand même votre message ou votre appel à l'action. 

#### Évitez les images de texte

Dans la mesure du possible, évitez de placer du texte dans des images - les lecteurs d'écran ne peuvent pas lire un texte basé sur une image et les utilisateurs ne peuvent pas facilement ajuster la taille ou la couleur de la police pour une meilleure visibilité. Tenez compte de ces conseils :

- **Supprimez du texte là où vous le pouvez :** Déplacez le texte descriptif ou promotionnel de l'image dans un champ de texte de votre message. Ainsi, les utilisateurs peuvent la redimensionner ou la recolorer selon leurs besoins en utilisant les préférences de leur appareil ou de leur navigateur.
- **Vérifiez la lisibilité et le contraste :** Si vous devez conserver le texte dans l'image, suivez les meilleures pratiques en matière de [contraste des couleurs](#color-contrast) et utilisez une [police de grande taille](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html#dfn-large-scale). Cela signifie que le texte doit avoir une taille d'au moins 18 points (environ 24 pixels) s'il n'est pas en gras ou de 14 points (environ 18 pixels) s'il est en gras. L'utilisation de ces tailles permet au texte de rester lisible sans obliger les utilisateurs à zoomer, et améliore le contraste général et la lisibilité du contenu. Testez-le pour confirmer qu'il est toujours lisible sur les petits écrans.
- **Fournissez un texte alternatif :** Pour le texte essentiel qui doit rester dans l'image, incluez un texte alt décrivant les mots.

Lorsque les images contiennent du texte qui ne peut être modifié, les utilisateurs souffrant de déficiences visuelles perdent la possibilité de procéder à des ajustements de lecture. En séparant le texte des images, vous permettez à un plus grand nombre d'utilisateurs de lire et d'interagir confortablement avec votre message.

#### Conseils pour la rédaction d'un texte alt

- [Décrivez ce qui se trouve réellement dans l'image](#tip-1)
- [Soyez bref, mais précis](#tip-2)
- [Évitez les termes "image de" ou "photo de"](#tip-3) 
- [Refléter le texte qui apparaît dans l'image](#tip-4)
- [S'en tenir au contexte pertinent - pas de jargon marketeur supplémentaire](#tip-5)
- [Considérez l'objectif de l'image](#tip-6)

##### Décrivez ce qui se trouve réellement dans l'image {#tip-1}

Les utilisateurs de lecteurs d'écran s'appuient sur le texte alt pour comprendre le contenu ou la fonction d'une image. Évitez le "discours marketing" générique qui ne correspond pas à ce qui est visuellement montré.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bons exemples <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Mauvais exemples <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Femme souriante, vêtue d'une veste en jean bleu, tenant un sac à provisions.</td>
      <td>"Il est temps de se faire plaisir" (aucune mention de ce qui se trouve réellement dans l'image)</td>
    </tr>
    <tr>
      <td>"Homme portant un T-shirt noir, appuyé sur un vélo dans une rue de la ville.</td>
      <td>"Embrassez votre meilleure vie maintenant" (Ignore le vélo et la ville)</td>
    </tr>
    <tr>
      <td>"Immeuble d'habitation bleu avec un panneau 'A louer' devant".</td>
      <td>"La clé d'un avenir meilleur" (ne correspond pas à l'appartement ou à l'enseigne)</td>
    </tr>
  </tbody>
</table>

##### Soyez bref, mais précis {#tip-2}

Un texte alt concis facilite le traitement par les utilisateurs. Incluez suffisamment de détails pour faire comprendre l'objectif, mais évitez tout ce qui est superflu. En règle générale, le texte alt ne doit pas dépasser 125 caractères. Si vous avez besoin de plus qu'une brève expression ou phrase, envisagez d'utiliser l'une des [méthodes de description longue du](https://www.w3.org/WAI/tutorials/images/complex/) W3C.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Bons exemples <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Mauvais exemples <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Chaussures de course rouges sur fond blanc</td>
      <td>"Des chaussures de course extrêmement confortables et parfaites pour votre style de vie actif, dans une nuance de rouge vibrant" (trop long et rempli d'éléments promotionnels).</td>
    </tr>
    <tr>
      <td>"Quatre ordinateurs portables sur un présentoir</td>
      <td>"Découvrez l'ultime stimulateur de productivité qui redéfinit votre façon de travailler chaque jour, de toutes les manières imaginables" (Ne décrit pas ce qui est réellement montré).</td>
    </tr>
    <tr>
      <td>"Groupe d'amis mangeant une glace par une journée ensoleillée</td>
      <td>"Capturez le bonheur à l'état pur avec la friandise la plus sucrée - la vie est meilleure avec notre marque de glace" (trop abstrait et trop axé sur la marque).</td>
    </tr>
  </tbody>
</table>

##### Évitez les termes "image de" ou "photo de" {#tip-3}

Les lecteurs d'écran annoncent déjà une image. Passez directement à la description du sujet.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bons exemples <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Mauvais exemples <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"La table est dressée pour un brunch avec des crêpes, des fruits et du café.</td>
      <td>"Image d'une table dressée pour un brunch"</td>
    </tr>
    <tr>
      <td>Panneau d'affichage en bord de route avec texte en gras "Grande ouverture"".</td>
      <td>"Photo d'un panneau d'affichage sur le bord d'une route"</td>
    </tr>
    <tr>
      <td>"Paysage de montagne enneigée au coucher du soleil"</td>
      <td>"Photo de neige et de montagnes</td>
    </tr>
  </tbody>
</table>

##### Refléter le texte qui apparaît dans l'image {#tip-4}

Si une image comporte un texte essentiel, indiquez cette information dans le texte alt afin que les utilisateurs ne la manquent pas.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bons exemples <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Mauvais exemples <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Bannière indiquant "Soldes d'été - 50 % de réduction sur tous les maillots de bain".</td>
      <td>"Bannière promouvant une vente" (ne mentionne pas la réduction réelle)</td>
    </tr>
    <tr>
      <td>Logo avec le texte "Café Toscana" en caractères d'imprimerie".</td>
      <td>Image du logo d'un café (ne comprend pas le texte "Café Toscana")</td>
    </tr>
    <tr>
      <td>Publicité annonçant "Billets de concert disponibles dès maintenant-début le 5 juin".</td>
      <td>"Annonce de concert" (Pas de détails sur l'événement)</td>
    </tr>
  </tbody>
</table>

##### S'en tenir au contexte pertinent - pas de jargon marketeur supplémentaire {#tip-5}

Ne remplissez pas le texte alt avec des termes de référencement ou des appels à l'action qui ne sont pas directement liés à l'image. Apportez une valeur ajoutée à ceux qui ne peuvent pas voir l'image.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Bons exemples <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Mauvais exemples <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Ordinateur portable montrant le tableau de bord de Braze analyse/analytique".</td>
      <td>"Boostez les conversions et faites grimper en flèche le ROI grâce à la meilleure plateforme au monde !" (Ajout d'un langage marketing inutile).</td>
    </tr>
    <tr>
      <td>"Ensemble de patio d'arrière-cour comprenant quatre chaises et une table en verre".</td>
      <td>"Organisez dès maintenant une incroyable fête d'été pour tous vos amis et votre famille" (décrit un scénario, pas l'image)</td>
    </tr>
    <tr>
      <td>"Téléphone portable affichant une application de prévisions météorologiques avec 75°F en vue"</td>
      <td>"Faites l'expérience d'innovations en temps réel en matière de suivi météorologique qui changent la donne" (Ne reflète pas ce qui est visiblement affiché)</td>
    </tr>
  </tbody>
</table>

##### Considérez l'objectif de l'image {#tip-6}

Si une image fonctionne comme un lien ou un appel à l'action, décrivez l'action envisagée ("Acheter", "Lien vers", "S'inscrire"), et pas seulement l'étiquette ou le produit représenté.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Bons exemples <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Mauvais exemples <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Magasinez la collection d'automne"</td>
      <td>"Collection d'automne" (action intentionnelle manquante)</td>
    </tr>
    <tr>
      <td>"Lien vers un livre électronique gratuit</td>
      <td>"Free eBook" (n'indique pas clairement qu'il s'agit d'un lien)</td>
    </tr>
    <tr>
      <td>"Inscrivez-vous à la liste de diffusion"</td>
      <td>"Liste de diffusion" (Ne décrit pas ce que l'utilisateur peut faire)</td>
    </tr>
  </tbody>
</table>

Si l'image n'a pas de raison d'être, faites-le savoir également. Les images décoratives, comme les tags, doivent avoir une étiquette alt vide (`alt=""`) pour que les lecteurs d'écran sachent qu'il ne faut pas l'annoncer. Sans cela, c'est généralement le nom du fichier image qui est lu.

### Vidéos

Les vidéos sont attrayantes, mais si elles ne sont pas accessibles, vous risquez d'exclure une partie de votre audience. Utilisez les conseils suivants pour rendre votre contenu vidéo plus inclusif :

- [Fournir des sous-titres codés](#closed-captions)
- [Fournir des contrôles de lecture](#playback-controls)
- [Évitez la lecture automatique](#no-auto-play)
- [Évitez les contenus clignotants ou stroboscopiques](#no-seizures)

#### Fournir des sous-titres codés {#closed-captions}

Incluez des sous-titres codés dans vos vidéos afin que les utilisateurs puissent suivre les dialogues, les effets sonores et les autres contenus audio. Les légendes sont utiles :

- Personnes sourdes ou malentendantes
- Les téléspectateurs qui regardent dans un environnement sans bruit
- Les locuteurs non natifs qui préfèrent lire en même temps que vous

Les sous-titres peuvent être basculés, ce qui permet aux utilisateurs de choisir ce qui leur convient le mieux.

{% multi_lang_include accessibility/video.md %}

#### Fournir des contrôles de lecture {#playback-controls}

Assurez-vous que votre vidéo intégrée comporte des commandes de lecture accessibles (lecture, pause, sourdine et recherche) afin que les utilisateurs puissent interagir avec elle de la manière qui leur convient le mieux.

#### Évitez la lecture automatique {#no-auto-play}

Dans la mesure du possible, évitez de configurer la lecture automatique des vidéos. La lecture automatique peut être dérangeante ou désorientante pour les utilisateurs :

- Utilisateurs utilisant des lecteurs d'écran ou la navigation au clavier
- Personnes sensibles aux mouvements
- Toute personne se trouvant dans un environnement calme (comme un lieu de travail ou un environnement nocturne).

Laissez les utilisateurs choisir le moment de la lecture d'une vidéo en incluant des contrôles clairs.

#### Évitez les contenus clignotants ou stroboscopiques {#no-seizures}

N'incluez pas de vidéos avec des effets de clignotement ou de stroboscopie, surtout à haute fréquence. Ceux-ci peuvent déclencher des crises chez les utilisateurs souffrant d'épilepsie photosensible et provoquer une gêne chez les autres.

### Contraste de couleurs

Un contraste de couleurs suffisant permet de s'assurer que vos messages sont faciles à lire pour tout le monde, y compris les personnes malvoyantes ou celles qui regardent votre contenu dans des conditions lumineuses ou difficiles. Visez des taux de contraste conformes aux [exigences du niveau AA des WCAG 2.2 :](https://www.w3.org/TR/WCAG/#contrast-minimum)

- Rapport de contraste de 4,5:1 pour le texte normal (corps du texte, boutons et liens)
- Rapport de contraste de 3:1 pour les textes de grande taille (pensez aux titres et aux étiquettes de grande taille)

Vous pouvez tester vos choix de couleurs à l'aide de l'[outil de vérification du contraste de WebAim](https://webaim.org/resources/contrastchecker/).

{% multi_lang_include accessibility/color.md %}

### HTML personnalisé

Si vous utilisez un HTML personnalisé dans vos envois de message :

- Utilisez du [HTML sémantique](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML). Cela signifie d’utiliser les éléments HTML appropriés pour leur objectif prévu plutôt que de formater un élément pour qu’il ressemble à un autre. La plupart des éléments HTML ont leur propre support d’accessibilité intégré.
- Définissez l'[attribut`lang` ](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang) dans votre HTML pour identifier la langue dans laquelle votre contenu est rédigé. Les lecteurs d’écran utilisent différentes bibliothèques sonores pour chaque langue en fonction de la prononciation et des caractéristiques de celle-ci. Si cela n'est pas spécifié, un lecteur d'écran suppose que le contenu est écrit dans la langue par défaut que l'utilisateur a choisie lors de la configuration du lecteur d'écran. Si le message n'est pas rédigé dans la langue par défaut, le lecteur d'écran risque de ne pas prononcer le message correctement. 

{% raw %}
```html
<html lang="en-us">
```
{% endraw %}

{% alert note %}
Lorsque vous utilisez l'éditeur par glisser-déposer d'un e-mail, la valeur de la langue de l'e-mail peut être définie en allant dans l'onglet **Paramètres** et en sélectionnant la valeur de la langue appropriée.
{% endalert %}

- Utilisez les [attributs ARIA](#aria-attributes) pour donner un contexte supplémentaire. Ces attributs fournissent des informations supplémentaires aux technologies d'assistance, en aidant à clarifier le rôle, l'état ou les propriétés des éléments de l'interface utilisateur qui, autrement, ne seraient pas clairs. 

### Attributs ARIA

Lorsque vous utilisez du code personnalisé dans les éditeurs Braze, vous pouvez utiliser les applications Internet riches accessibles[(ARIA)](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA) pour fournir une assistance supplémentaire en matière d'accessibilité aux utilisateurs qui dépendent d'une technologie d'assistance. Les rôles et attributs ARIA aident les lecteurs d'écran à interpréter votre contenu plus clairement, en particulier lorsque vous utilisez des éléments qui n'ont pas de signification en eux-mêmes (comme `<div>` ou `<span>`).

{% alert important %}
Bien qu'ARIA soit conçu pour rendre le contenu web plus accessible, il peut faire plus de mal que de bien s'il n'est pas utilisé correctement. ARIA ne remplace pas le HTML sémantique, il le complète. N'utilisez donc ARIA que lorsque les éléments HTML natifs ne répondent pas à vos besoins.
{% endalert %}

Voici quelques exemples particulièrement utiles dans les contextes d'envoi de messages :

- [aria-label](#aria-label)
- [aria-labelledby](#aria-labelledby)
- [aria-hidden="true"](#aria-hiddentrue)
- [role="presentation"](#rolepresentation)
- [aria-live="poli"](#aria-livepolite)

#### aria-label

`aria-label` ajoute un nom accessible aux éléments qui n'ont pas de texte visible. Si vous utilisez une icône sans texte (comme une poubelle ou un "X" pour fermer), une personne utilisant un lecteur d'écran ne saura pas ce qu'elle fait - à moins que vous ne l'étiquiez. `aria-label` donne une voix à cette icône.

{% raw %}
```html
<button aria-label="Close message">
  <svg ...></svg>
</button>
```
{% endraw %}

#### aria-labelledby

`aria-labelledby` relie un élément à quelque chose qui a déjà une étiquette visible. Ainsi, si vous avez une bannière ou une région qui doit être lue à haute voix avec un titre, vous pouvez utiliser `aria-labelledby` pour indiquer aux technologies d'assistance : "Hé, utilisez ce titre pour nommer cette partie".

{% raw %}
```html
<h2 id="banner-title">Important Update</h2>
<div role="region" aria-labelledby="banner-title">...</div>
```
{% endraw %}

#### aria-hidden="true"

`aria-hidden="true"` cache des éléments aux lecteurs d'écran.  Elle est utile pour les textes ou les images qui ne véhiculent pas de signification importante, comme une étincelle, une coche ou un émoji utilisé uniquement pour le style.

Cela permet aux utilisateurs de lecteurs d'écran de bénéficier d'une expérience plus propre, car ils risqueraient sinon d'entendre un contenu redondant ou confus. Il est également utile pour masquer des éléments tels que le contenu d'un accordéon hors écran qui n'a pas encore été développé.

{% raw %}
```html
<span aria-hidden="true">✔️</span>
```
{% endraw %}

En général, il est préférable d'utiliser `alt=""` pour les [images décoratives](#images) et les icônes plutôt que `aria-hidden="true"`. Alors que le HTML sémantique est largement pris en charge par tous les lecteurs d'écran et logiciels d'assistance, la prise en charge de l'ARIA varie. Même si vous utilisez `aria-hidden`, vous devez toujours inclure un attribut alt vide.

#### role="presentation"

`role="presentation"` indique aux technologies d'assistance d'ignorer les éléments de mise en page uniquement, tels que les tableaux de conception. Par exemple, les e-mails utilisent souvent des tableaux pour aligner les choses. Sans ce rôle, les lecteurs d'écran pourraient supposer que votre mise en page est un tableau de données et commencer à lire les numéros de lignes et de colonnes.  

{% raw %}
```html
<table role="presentation">...</table>
```
{% endraw %}

Les e-mails créés dans l'éditeur par glisser-déposer ont des éléments de présentation automatiquement marqués avec l'attribut ARIA `role="presentation"`.

#### aria-live="poli"

`aria-live="polite"` annonce des mises à jour lorsque le contenu est modifié sans que l'utilisateur n'ait à intervenir. Utilisez-le lorsque vous affichez des mises à jour dynamiques dans un message, comme des succès, des erreurs ou d'autres notifications.

{% raw %}
```html
<div aria-live="polite">Your preferences have been saved.</div>
```
{% endraw %}

## Tests d'accessibilité automatisés

Pour vous aider à identifier et à résoudre rapidement les problèmes d'accessibilité, Braze propose des tests d'accessibilité automatisés dans les domaines suivants :

- [Boîte de réception Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#accessibility-testing) pour les e-mails
- [Scanner d'accessibilité]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/?tab=in-app%20message#accessibility-scanner) pour les messages créés à l'aide de notre éditeur HTML (par exemple, les messages in-app en HTML, les blocs de contenu en HTML, les [pieds de page des e-mails personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer), les [pages d'abonnement aux e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#creating-a-custom-opt-in-page) et les [pages de désabonnement aux e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#creating-a-custom-unsubscribe-page)).

Ces tests comparent votre message aux normes[WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)(Web Content Accessibility Guidelines), un ensemble de normes techniques internationalement reconnues pour l'accessibilité des contenus. Tous les problèmes qui peuvent être détectés automatiquement sont signalés et classés par ordre de gravité pour vous aider à établir des priorités.

{% alert note %}
Inbox Vision fonctionne aussi bien pour les e-mails en HTML que pour les e-mails glissés-déposés. Le scanner ne fonctionne que sur le contenu créé avec l'éditeur HTML.
{% endalert %}

### Ce que les tests automatisés peuvent et ne peuvent pas détecter

Les tests d'accessibilité automatisés constituent un excellent point de départ, mais ils ne peuvent pas tout détecter. Certaines questions nécessitent une touche humaine pour être évaluées correctement, en particulier lorsque le contexte ou la conception visuelle joue un rôle dans la façon dont les utilisateurs perçoivent votre e-mail.

Il se peut que certaines questions soient marquées comme **nécessitant une révision.** Il s'agit de cas où le vérificateur ne peut pas dire avec certitude si quelque chose pose un problème d'accessibilité. Dans ce cas, nous vous recommandons de l'examiner manuellement.

Voici quelques exemples de ce que les outils automatisés ne peuvent pas détecter de manière fiable :

- Si l'ordre de focalisation des éléments interactifs suit une séquence logique
- Si le contenu est entièrement utilisable à l'aide d'un clavier, sans nécessiter de souris
- Si le texte alt décrit de manière significative une image
- Si les titres sont utilisés correctement pour organiser le contenu
- Si les liens et les boutons sont clairement identifiés et faciles à comprendre
- Si les cibles tactiles sont suffisamment grandes et espacées de manière appropriée
- Si le texte sur les images d'arrière-plan répond aux exigences en matière de contraste des couleurs
- Si les instructions ou les étiquettes sont claires et utiles pour tous les utilisateurs

Ces limitations ne sont pas uniques à Braze : elles sont communes à tous les outils d'accessibilité automatisés. Les contrôles automatisés ne peuvent pas reproduire toutes les technologies d'assistance, tous les lecteurs d'écran ou tous les besoins des utilisateurs. C'est pourquoi l'accessibilité n'est pas un contrôle ponctuel, mais une pratique continue.

Même si votre message passe avec succès tous les contrôles automatisés, il est important d'en tenir compte :

- Examinez attentivement les questions signalées, en particulier celles qui doivent faire l'**objet d'un examen.**
- Testez manuellement dans la mesure du possible, en particulier pour la mise en page et les modèles d'interaction.
- Utilisez des outils tels que les lecteurs d'écran, la navigation au clavier et l'agrandissement du navigateur pour simuler différents besoins d'accès.

En associant des tests automatisés à une révision manuelle réfléchie, vous détecterez davantage de problèmes potentiels et créerez des campagnes plus complètes et utilisables par tous les destinataires.
