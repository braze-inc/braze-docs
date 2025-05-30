---
nav_title: Créer des messages accessibles
article_title: Créer des messages accessibles dans Braze
page_order: 3.5
page_type: reference
description: "Cet article de référence explique pourquoi il est important de prendre en compte l’accessibilité dans votre contenu marketing et comment vous pouvez créer des messages accessibles dans Braze."
---

# Créer des messages accessibles dans Braze

> Le contenu marketing qui exclut les personnes présentant un handicap, même involontairement, peut empêcher des millions de personnes d’interagir avec votre marque. L’accessibilité dans le marketing consiste à faciliter l’utilisation de celui-ci, à recevoir et à comprendre vos communications, et de permettre à tous de s’investir ou de devenir fan de votre produit, service ou marque. Lorsque vous concevez vos envois de message, prenez le temps de réfléchir à la façon dont vous pouvez rendre vos conceptions accessibles à tous vos clients.

## Pourquoi l’accessibilité compte

- **Meilleure convivialité :** L’accessibilité vous encourage à réfléchir à la convivialité de votre application ou de votre site, car vous devez réfléchir à la manière dont l’utilisateur interagit avec votre contenu. Cela signifie qu’elle améliore souvent l’expérience en ligne pour tous les utilisateurs, pas seulement ceux ayant un handicap.
- **Étendre la portée du marché :** Le marché mondial des personnes handicapées comprend plus d’un milliard de personnes avec une puissance de dépenses de près de 7 billions de dollars.
   > « Le marché des personnes présentant un handicap est important et augmente avec le vieillissement de la population mondiale. Au Royaume-Uni, où le grand marché de l’invalidité est connu sous le nom de Purple pound (Livre pourpre), les personnes handicapées et leurs familles dépensent au moins 249 milliards GBP chaque année. Aux États-Unis, les dépenses discrétionnaires annuelles des personnes handicapées sont supérieures à 200 milliards USD. L’estimation mondiale du marché des handicaps est de près de 7 billions USD. »<br>*Source : [W3C](https://www.w3.org/WAI/business-case/)*
- **Minimiser les risques juridiques :** De nombreux pays ont des lois exigeant une accessibilité au numérique.

## Domaines d’invalidité à envisager

*Cette section est partiellement adaptée de [W3C : Capacités et obstacles divers](https://www.w3.org/WAI/people-use-web/abilities-barriers/).*

### Visuel

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

### Audition

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

### Physique

Les handicaps physiques peuvent comprendre une faiblesse et des limitations dans le contrôle ou la sensation musculaire, des troubles articulaires, des douleurs qui gênent les mouvements et des membres manquants.

Ces utilisateurs s’appuient sur le support clavier pour activer la fonctionnalité (même s’ils n’utilisent pas de clavier standard). Pour interagir avec votre contenu, ces utilisateurs ont besoin de :

- Larges zones cliquables
- Suffisamment de temps pour terminer les tâches
- Indicateurs visibles du sujet actuel
- Mécanismes permettant de sauter des blocs de contenu, comme des en-têtes de page ou des barres de navigation

{% alert note %}
Près de 2 millions de personnes aux États-Unis vivent avec une perte de membre (voir [Amputee Coalition](https://www.amputee-coalition.org/limb-loss-resource-center/resources-filtered/resources-by-topic/limb-loss-statistics/limb-loss-statistics/#1)).
{% endalert %}

### Cognitif

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

## Bonnes pratiques

### Contenu

- Centrez votre contenu sur la marque, mais utilisez un langage simple. Écrivez à un niveau de lecture équivalent à la cinquième en France. Vous pouvez utiliser des ressources telles que [Hemingway App](https://hemingwayapp.com/) pour vérifier le niveau de lecture de votre texte.
- Structurez votre contenu logique et assurez-vous que les en-têtes suivent une hiérarchie correcte. Ne sautez pas le niveau des titres.
- Évitez le texte centré pour de longs blocs de contenu. Il peut être difficile à lire pour les utilisateurs souffrant d’incapacité cognitive ou d’apprentissage. Le contenu qui s’étend sur plus de deux lignes doit être aligné à gauche.
- Utilisez des polices sans serif, qui sont plus faciles à lire sur les appareils numériques.
- Testez toujours votre texte en [envoyant un message test]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) à un appareil pour vous assurer que votre texte n'est pas tronqué. Si votre message est coupé, cela a un impact sur vous et l’utilisateur, car il empêche votre contenu d’atteindre vos utilisateurs.

### Liens

Utilisez des liens pour la navigation, par exemple pour diriger les utilisateurs vers une page externe.

{% alert tip %}
Si vous voulez quelque chose qui ressemble et agit comme un bouton, essayez d’utiliser toujours un vrai bouton plutôt que de formater un lien comme un bouton. Les liens et les boutons peuvent « sembler » les mêmes pour les utilisateurs moyens : ils peuvent utiliser leur souris pour survoler le lien ou le bouton et cliquer dessus. Cependant, les boutons et les liens ont des commandes différentes (par exemple, les boutons peuvent être activés en appuyant sur la touche <kbd>Espace</kbd> ou <kbd>Entrée</kbd>, mais les liens ne peuvent être activés que par la touche <kbd>Entrée</kbd>), ce qui peut entraîner la confusion si vous formatez un lien comme un bouton.
{% endalert %}

Écrivez le texte du lien qui décrit clairement l’endroit où se rendra l’utilisateur. Les utilisateurs de lecteurs d’écran passent souvent d’un lien à l’autre pour parcourir le contenu, assurez-vous donc que votre texte de lien s’explique de lui-même. Évitez les expressions comme « cliquez ici », « plus » et « cliquez pour obtenir des détails », car ils sont ambigus lorsqu’ils sont lus hors du contexte.

Par exemple, réfléchissez à la manière dont vous pourriez rédiger un lien pour afficher un rapport météorologique.

| Mauvais  | Mieux | Le meilleur |
| --- | --- | --- | 
| Cliquez ici | Cliquez ici pour accéder aux conditions météorologiques d’aujourd’hui | Météo d’aujourd’hui |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Comme avec tout contenu, faites en sorte qu’il soit direct avec le moins de mots supplémentaires possible.

### Boutons

Utilisez des boutons pour des actions cliquables, comme l’envoi d’un formulaire ou la lecture d’un carrousel.

Comme pour le texte du lien, rédigez le texte du bouton en décrivant clairement l'action qui se produira lorsque l'utilisateur appuiera dessus (par exemple, "Lire l'intégralité de l'article" plutôt que "Lire la suite"). Vérifiez que votre texte de bouton n’est pas trop long. Si le bouton ne peut pas afficher tout le texte, il tronquera avec une ellipse, contrairement au texte qui passe sur une nouvelle ligne.

### Images

Certains utilisateurs ne peuvent pas voir les images de votre contenu marketing. Si vous ne tenez pas compte de l’accessibilité, les images peuvent devenir une barrière à tous les utilisateurs recevant le même contenu.

#### Texte alternatif

Le texte alternatif est une brève description du contenu de l’image que les lecteurs d’écran et autres technologies d’assistance fournissent à leurs utilisateurs.

- Pour chaque image, écrivez un texte alternatif qui fournit les informations ou la fonction de l’image.
- Si l'image est [décorative](https://www.w3.org/WAI/tutorials/images/decorative/) (n'apporte rien au contenu), utilisez un attribut alt vide (`alt=""`).
- N’utilisez pas le mot « photo » ou « image » dans votre texte alternatif.

#### Images de texte

Évitez d’utiliser des images de texte, car les lecteurs d’écran ne peuvent pas lire le texte contenu à l’intérieur d’une image. Les images de texte se redimensionnent mal et ne peuvent pas être personnalisées selon les besoins et préférences de l’utilisateur. Avec un vrai texte, les utilisateurs peuvent personnaliser des éléments comme la couleur et le contraste, ainsi que redimensionner le texte sans perdre de qualité. Lorsque les images de texte sont agrandies, elles deviennent pixelisées et de qualité inférieure, ce qui les rend difficiles à lire.

### Vidéos

Fournissez des sous-titres pour les vidéos. Ils aident les personnes qui souffrent d’une perte de vision, celles qui regardent dans un endroit bruyant et celles qui parlent une langue différente de celle de la vidéo.

### Contraste de couleurs

Un contraste de couleurs suffisant peut constituer un gain rapide d’accessibilité. Le rapport de contraste entre les couleurs de premier plan (texte) et d'arrière-plan doit être conforme aux [exigences du niveau AA des WCAG 2.1 :](https://www.w3.org/TR/WCAG/#contrast-minimum)

- Rapport de contraste de 4.5:1 pour le texte normal (texte du corps, boutons et liens)
- Rapport de contraste de 3:1 pour les gros textes (en-têtes)

Vous pouvez utiliser l'[outil de vérification du contraste de WebAim](https://webaim.org/resources/contrastchecker/) pour voir si votre texte est lisible par rapport aux couleurs d'arrière-plan.

### Formulaires

**Découper les formes les plus longues en sections plus petites** <br>Pour réduire la charge cognitive, divisez les formulaires longs en sections plus petites. C’est ce que l’on appelle former des blocs, un modèle d’affichage progressif utilisé pour rendre les informations plus faciles à assimiler. Ceci profite à tous les utilisateurs, mais est particulièrement utile pour les personnes souffrant d’un handicap cognitif.

**Ne cachez pas de contenu important dans les infobulles ou autres états de survol.** <br>Le contenu de survol de la souris est moins lisible et les utilisateurs mobiles et agrandissant l’écran auront des difficultés à afficher le contenu qui n’est disponible que lors du survol.

**Évitez de bloquer les caractères non valides dans les champs** <br>N’empêchez pas certains types de caractères d’être saisis dans les champs de formulaire. Il est préférable de permettre aux utilisateurs de saisir ce qu’ils veulent, puis d’envoyer un message d’erreur concernant ce qui est incorrect. Bloquer la saisie au clavier pose un problème particulier pour les utilisateurs de technologie d’assistance, car elles dépendent fortement de la validation en ligne pour déterminer si elles ont rempli le formulaire correctement.

**Rédiger des messages d'erreur clairs** <br>Un bon message d’erreur est composé de trois parties : ce qui s’est passé, ce qui s’est mal passé et comment cela peut être résolu. Le message d’erreur doit être clair et facile à comprendre. Essayez de parler en langage simple. N’utilisez pas de jargon trop technique.
<br>

### HTML personnalisé

Si vous utilisez un HTML personnalisé dans vos envois de message :

- Utilisez du [HTML sémantique](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML). Cela signifie d’utiliser les éléments HTML appropriés pour leur objectif prévu plutôt que de formater un élément pour qu’il ressemble à un autre. La plupart des éléments HTML ont leur propre support d’accessibilité intégré.
- Définissez l’attribut de langue dans votre HTML pour identifier la langue dans laquelle votre contenu est affiché. Les lecteurs d’écran utilisent différentes bibliothèques sonores pour chaque langue en fonction de la prononciation et des caractéristiques de celle-ci. Si la langue est spécifiée, les lecteurs d’écran peuvent basculer automatiquement entre les bibliothèques de langue si nécessaire. Par exemple :

{% raw %}
```html
<html lang="en-us">
```
{% endraw %}

