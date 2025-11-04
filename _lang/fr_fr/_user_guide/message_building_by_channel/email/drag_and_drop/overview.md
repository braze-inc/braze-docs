---
nav_title: "Création d'un e-mail"
article_title: Créer un e-mail par glisser-déposer
alias: "/dnd/overview/"
channel: email
page_order: 0
description: "Cet article explique comment configurer et utiliser correctement l'éditeur par glisser-déposer pour les messages e-mail."
tool:
- Campaigns
- Canvas
---

# Créer un e-mail par glisser-déposer

> Grâce à l'éditeur par glisser-déposer, vous pouvez créer des messages e-mail entièrement personnalisés pour les campagnes ou les toiles, sans utiliser le langage HTML pour construire le corps de votre e-mail.

## À propos de l'éditeur

L'éditeur par glisser-déposer utilise le [contenu](#content) et les [rangées](#rows) comme les deux composants clés pour simplifier votre flux de travail, sans utilisation supplémentaire de HTML.

<table style="width: 100%; table-layout: fixed;">
    <tr>
        <th style="width: 50%;">Contenu</th>
        <th style="width: 50%;">Rangs</th>
    </tr>
    <tr>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_content.png %}" alt="L&apos;onglet &quot;rangées&quot; comprend différentes combinaisons structurelles pour la mise en page de votre e-mail." style="max-width: 100%; height: auto;">
        </td>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_rows.png %}" alt="L&apos;onglet &quot;Contenu&quot; qui comprend les blocs de base, les médias et les blocs avancés." style="max-width: 100%; height: auto;">
        </td>
    </tr>
</table>
{: .reset-td-br-1 role="presentation"}

### Contenu

Le **contenu** comprend une série de tuiles qui conseillent les différents types de contenu que vous pouvez utiliser dans votre message. Celles-ci sont organisées en trois catégories : basique, média et avancée. 

{% tabs %}
{% tab Basic %}

Les blocs de base constituent le fondement de votre e-mail. Grâce à ces blocs, vous pouvez ajouter l'un des éléments suivants dans le corps de votre e-mail :

- Titre
- Paragraphe
- Liste
- Bouton
- Diviseur
- Entretoise

{% endtab %}
{% tab Media %}

Avec les blocs médias, vous pouvez ajouter différents contenus visuels tels que des images, des vidéos, des icônes et des liens de réseaux sociaux, ainsi que des icônes personnalisables.

{% endtab %}
{% tab Advanced %}

Bien que l'éditeur par glisser-déposer simplifie votre flux de travail avec ces blocs, vous pouvez également utiliser des blocs avancés pour insérer du HTML ou pour ajouter un menu dans le corps de votre e-mail. Notez que l'utilisation de votre propre code HTML peut affecter le rendu du message.

{% endtab %}
{% endtabs %}

### Rangs

Les **lignes** sont des unités structurelles qui définissent la composition horizontale d'une section du message à l'aide de colonnes. Vous pouvez soit vider des lignes, soit des [blocs de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/). L'utilisation de plusieurs colonnes vous permet de placer différents éléments de contenu côte à côte. Vous pouvez ainsi ajouter à votre message tous les éléments structurels dont vous avez besoin, quel que soit le modèle que vous avez sélectionné au départ.

#### Style des cartes

Le **style de carte** est une propriété de ligne qui vous permet d'ajouter de l'espace entre les colonnes et d'arrondir leurs angles. Grâce à la mise en forme sous forme de carte, vous pouvez créer des mises en page plus attrayantes pour mettre en valeur vos contenus les plus importants, tels que les fonctionnalités des nouveaux produits, les témoignages, les offres spéciales, les mises à jour, etc.

## Utiliser l'éditeur par glisser-déposer

Vous ne savez pas si votre message e-mail doit être envoyé par le biais d'une campagne ou d'un canvas ? Les campagnes sont plus adaptées aux campagnes d'envoi de messages simples et uniques, tandis que les Canevas sont plus adaptés aux parcours utilisateurs en plusieurs étapes.

Une fois que vous avez choisi l'endroit où créer votre message, passons aux étapes de la création d'un e-mail par glisser-déposer.

### Étape 1 : Sélectionnez votre modèle

Après avoir sélectionné l'éditeur par glisser-déposer comme expérience d'édition, vous pouvez choisir :

- Commencez par un modèle vierge.
- Utilisez un modèle d'e-mail prédéfini à glisser-déposer de Braze.
- Utilisez un modèle d'e-mail enregistré par glisser-déposer.

{% alert note %}
Pour utiliser un modèle HTML personnalisé existant ou des modèles créés par un tiers, vous devez recréer le modèle en allant dans **Modèles** > **Modèles** **d'e-mail** et en sélectionnant l'**éditeur glisser-déposer** comme expérience d'édition.
{% endalert %}

Vous pouvez également accéder à tous les modèles à partir de la section **Modèles**.

Après avoir sélectionné votre modèle, vous obtiendrez un aperçu de votre e-mail sous **Variantes d'e-mail** qui comprend les informations d'envoi et le corps de l'e-mail. 

Ensuite, sélectionnez **Modifier le corps de l'e-mail** pour commencer à concevoir la structure de l'e-mail dans l'éditeur par glisser-déposer. 

!La section "Variantes d'e-mail" avec un exemple de corps d'e-mail.]({% image_buster /assets/img/dnd/dnd_emailvariant.png %})

### Étape 2 : Créez votre e-mail

L'expérience de modification par glisser-déposer est divisée en trois sections : **Paramètres d'envoi**, **contenu** et **aperçu & Test**. La magie de créer le corps de votre e-mail se produit dans la section **Contenu.**  Avant de créer votre e-mail, il est important de comprendre les éléments clés qui guident votre expérience de création d'e-mails. Si vous avez besoin d'une révision, consultez la rubrique [À propos de l'éditeur.](#about-the-editor)

Lorsque vous êtes prêt, utilisez les blocs de contenu à glisser-déposer pour créer votre e-mail.

1. Sélectionnez le panneau **Lignes.**  Glissez-déposez les configurations de ligne dans l'éditeur principal. Cela permet de mapper la mise en page du contenu de votre e-mail.
- Notez que les nouvelles configurations doivent être glissées en haut ou en bas d'une section existante.
- Lorsque vous sélectionnez une configuration de ligne, les paramètres des **propriétés de la ligne** apparaissent pour une personnalisation plus poussée des couleurs d'arrière-plan de la ligne, des images et des tailles de colonne personnalisées.
2. Sélectionnez le panneau **Contenu**. Glissez-déposez les tuiles de contenu de votre choix sur les composants de la ligne.
- Vous pouvez également faire glisser n'importe quelle tuile de **contenu** dans l'éditeur principal. Cela crée une ligne pour la tuile.
- Vous pouvez affiner davantage le carreau en le sélectionnant et en ajustant les champs dans les **propriétés du contenu** et les **options du bloc**. Il s'agit notamment de modifier l'espacement des lettres, le remplissage, la hauteur de ligne, etc.

Consultez la rubrique [Autres personnalisations](#other-customizations) pour découvrir d'autres moyens de personnaliser davantage votre e-mail glissé-déposé.

Au fur et à mesure que vous créez votre e-mail, vous pouvez basculer entre une vue de bureau et une vue mobile pour prévisualiser l'aspect de votre envoi de messages pour vos groupes d'utilisateurs. Vous vérifierez ainsi que votre contenu est réactif, et vous pourrez procéder aux ajustements nécessaires en cours de route.

{% alert tip %}
Vous avez besoin d'aide pour créer un texte percutant ? Essayez d'utiliser l'[assistant de rédaction de l'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Saisissez le nom ou la description d'un produit, et l'intelligence artificielle générera un texte marketing semblable à celui d'un humain, que vous pourrez utiliser dans vos messages.

!bouton Copywriter, situé dans le panneau Contenu à côté de Paramètres de style dans l'éditeur glisser-déposer.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_dnd.png %})
{% endalert %}

### Étape 3 : Ajoutez vos informations d'envoi

Une fois que vous avez fini de concevoir et de créer votre message e-mail, il est temps d'ajouter vos informations d'envoi dans la section **Paramètres d'envoi.** 

1. Sous **Informations sur l'envoi**, sélectionnez un e-mail comme **Nom d'affichage de l'expéditeur + adresse**. Vous pouvez également la personnaliser en sélectionnant **Personnaliser à partir de l'affichage du nom et de l'adresse.**
2. Sélectionnez un e-mail comme **adresse de réponse.** Vous pouvez également la personnaliser en sélectionnant **Personnaliser l'adresse de réponse.**
3. Ensuite, sélectionnez un e-mail comme **adresse CCI** pour que votre e-mail soit visible à cette adresse.
4. Ajoutez une ligne d'objet à votre e-mail. Vous pouvez également ajouter un accroche et un espace après l'accroche.

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

Un aperçu dans le panneau de droite s'affiche avec les informations d'envoi que vous avez ajoutées. Ces informations peuvent également être mises à jour en accédant à **Paramètres** > **Préférences e-mail** > **Configuration de l'envoi.**

#### Personnalisation de l'en-tête de votre e-mail (avancé)

Sous **Paramètres d'envoi**, vous pouvez ajouter une personnalisation pour les en-têtes et les extras des e-mails, ce qui vous permet de renvoyer des données supplémentaires à d'autres fournisseurs de services e-mail. La personnalisation de l'en-tête d'un e-mail, par exemple en y incluant le nom du destinataire, peut également contribuer à la probabilité d'ouverture de votre e-mail.

{% alert note %}
Les fonctionnalités avancées apparaîtront dans le compositeur de la campagne ou du canvas. Dans les fonctionnalités avancées, vous pouvez modifier vos paramètres CSS en ligne et saisir un en-tête ou des paires clé-valeur supplémentaires (si elles sont configurées).
{% endalert %}

### Étape 4 : Testez votre e-mail

Après avoir ajouté vos informations d'envoi, il est temps de tester enfin votre e-mail. 

Allez dans la section **Prévisualisation et test.**  Ici, vous avez la possibilité de prévisualiser votre e-mail en tant qu'utilisateur ou d'envoyer un message test. Cette section comprend également [Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/), qui vous permet de vérifier que le rendu de vos e-mails est correct sur les différents clients mobiles et web.

{% alert tip %}
Vous pouvez également basculer l'**aperçu en mode sombre** dans le panneau d'aperçu pour afficher le corps de votre e-mail en mode sombre et l'ajuster si nécessaire.
{% endalert %}

Comme vous pouvez visualiser trois versions différentes du même e-mail dans l'éditeur actuel, dans Inbox Vision et en tant qu'e-mail de test réel, il est important d'aligner les détails sur toutes vos plateformes.

#### Prévisualisation et test d'envoi
 
Sous l'onglet **Prévisualiser en tant qu'utilisateur**, vous pouvez sélectionner les types d'utilisateurs suivants pour prévisualiser votre message.

- **Utilisateur aléatoire :** Braze sélectionnera au hasard un utilisateur dans la base de données et prévisualisera l'e-mail en fonction de ses attributs ou des informations relatives à l'événement.
- **Sélectionnez Utilisateur :** Vous pouvez sélectionner un utilisateur spécifique sur la base de son adresse e-mail ou de son ID externe. L'e-mail sera prévisualisé en fonction des attributs de l'utilisateur et des informations relatives à l'événement.
- **Utilisateur personnalisé :** Vous pouvez personnaliser un utilisateur. Braze proposera des entrées pour tous les attributs et événements disponibles. Vous pouvez saisir toutes les informations que vous souhaitez voir figurer dans l'e-mail de prévisualisation.

{% alert note %}
L'utilisateur aléatoire peut ou non faire partie de vos critères de segmentation. La segmentation est sélectionnée par la suite, de sorte que Braze ne connaît pas votre audience cible à ce stade.
{% endalert %}

Vous pouvez également sélectionner **Copier le lien de prévisualisation** pour générer et copier un lien de prévisualisation partageable qui montre à quoi ressemblera l'e-mail pour un utilisateur aléatoire. Le lien durera sept jours avant de devoir être régénéré. 

Notez que toute modification apportée à un modèle d'e-mail ne se reflétera pas dans un lien généré précédemment. Vous devrez générer un nouvel aperçu du lien pour voir les modifications.

!Aperçu de l'e-mail avec un bouton pour "Copier le lien d'aperçu" et copier le lien généré.]({% image_buster /assets/img/dnd_email_link_preview.png %})

#### Utilisez la boîte de réception Vision

Inbox Vision vous permet de visualiser vos campagnes d'e-mail du point de vue des clients de messagerie et des appareils mobiles. Pour tester votre message e-mail à l'aide de Inbox Vision, sélectionnez **Inbox Vision** dans la section **Preview & Test** et sélectionnez **Run Inbox Vision.**

{% alert tip %}
Les images d'arrière-plan dans les envois de messages e-mail peuvent parfois provoquer l'apparition de lignes blanches ou de déconnexions entre les images. Il est donc important de tester et de vérifier les moindres détails de votre message e-mail.
{% endalert %}

Après avoir utilisé l'éditeur glisser-déposer pour concevoir et créer votre message e-mail, continuez à [créer]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas) le reste de votre campagne ou Canvas.

{% details About the updated HTML engine %}
Le moteur sous-jacent qui produit le code HTML à partir de l'éditeur par glisser-déposer a été optimisé et mis à jour, ce qui se traduit par des avantages liés à la compression et au rendu des fichiers HTML.

La taille moyenne de l'empreinte de nos données HTML exportées a été réduite, ce qui se traduit par un chargement et un rendu plus rapides, une réduction de l'écrêtage mobile et une diminution de la consommation de bande passante.

Le rendu HTML a été amélioré grâce aux mises à jour suivantes qui minimisent le nombre de commentaires conditionnels et de requêtes média CSS. En conséquence, les fichiers HTML sont plus petits et plus efficacement codés.
- Migration d'une conception basée sur les éléments `<div>` vers une base de code formatée standard `<table>` 
- Les [blocs éditeurs]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) ont été recodés pour plus de concision.
- Le code HTML final est compressé pour supprimer les espaces entre les tags.
- Les séparations transparentes sont automatiquement converties en rembourrage de contenu.
{% enddetails %}

## Autres personnalisations

En continuant à créer des e-mails par glisser-déposer, vous pouvez personnaliser davantage chaque corps d'e-mail en utilisant une combinaison de ces détails créatifs pour attirer l'attention de votre audience et susciter son intérêt pour votre message.

{% alert tip %}
Vous pouvez créer un thème personnalisé pour votre éditeur par glisser-déposer à l'aide des [paramètres de style globaux]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings/).
{% endalert %}

### Images à largeur automatique

Les images ajoutées à votre e-mail seront automatiquement réglées sur la **largeur automatique.** Pour ajuster ce paramètre, basculez sur " **Largeur automatique"** et ajustez le pourcentage de largeur selon vos besoins.

!Option de largeur automatique dans l'onglet Contenu de l'éditeur par glisser-déposer.]({% image_buster /assets/img/dnd/dnd1.png %})

### Superposition de couleurs

Grâce à la superposition de couleurs, vous pouvez modifier la couleur de l'arrière-plan de l'e-mail, de la zone de contenu et des différents composants du contenu. L'ordre des couleurs, de l'avant vers l'arrière, est le suivant : couleur du composant de contenu, couleur d'arrière-plan de la zone de contenu et couleur d'arrière-plan.

Exemple de superposition de couleurs dans l'éditeur par glisser-déposer.]({% image_buster /assets/img/dnd/dnd2.png %})

### Rembourrage du contenu

\![Bloc Options pour l'éditeur par glisser-déposer.]({% image_buster /assets/img/dnd/dnd3.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Pour ajuster le rembourrage, faites défiler vers le bas jusqu'à **Block Options** et sélectionnez **More Options.** Vous pouvez affiner votre remplissage pour que votre e-mail ait l'air parfait.

### Contexte du contenu

Vous pouvez ajouter une image d'arrière-plan à votre configuration de ligne, ce qui vous permet d'intégrer davantage de design et de contenu visuel dans votre campagne d'e-mail.

### Attribut linguistique

Vous pouvez définir l'attribut de la langue en allant dans l'onglet **Paramètres** et en sélectionnant la langue souhaitée. Vous pouvez également cibler l'attribut utilisateur {%raw%} `{{${language}}}` {%endraw%} si le message est destiné à des utilisateurs ayant des valeurs linguistiques dynamiques.

\![Réglage de la valeur "Langue" d'un e-mail.]({% image_buster /assets/img/dnd/language_setting_dnd.png %}){: style="max-width:70%;"}

### Personnalisation

\![Options de personnalisation de l'éditeur par glisser-déposer.]({% image_buster /assets/img/dnd/dnd4.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Basic Liquid est pris en charge dans l'éditeur par glisser-déposer des e-mails. Pour ajouter de la personnalisation à votre e-mail :

1. Sélectionnez **Personnalisation** dans la section **Contenu.**  
2. Sélectionnez le type de personnalisation. Il peut s'agir d'attributs par défaut (standard), d'attributs d'appareil, d'attributs personnalisés, etc. 
3. Recherchez l'attribut à ajouter.
4. Copiez l'extrait de code Liquid généré et collez-le dans le corps de votre e-mail.

La personnalisation liquide n'est pas prise en charge pour les blocs d'images et les champs de type lien bouton. 

#### Images dynamiques

Vous pouvez choisir d'inclure des images dynamiques dans vos messages e-mail en incluant Liquid dans l'attribut source de votre image. Par exemple, au lieu d'une image statique, vous pouvez insérer {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} comme URL de l'image pour inclure le prénom d'un utilisateur dans l'image. Cela permet de personnaliser vos e-mails pour chaque utilisateur.

### Sens du texte

Lors de la rédaction de votre message, vous pouvez basculer la direction du texte de gauche à droite ou de droite à gauche en sélectionnant le bouton correspondant à la **direction du texte**. Vous pouvez utiliser cette option pour créer des messages dans des langues telles que l'arabe et l'hébreu.

!Menu de l'éditeur glisser-déposer de l'e-mail avec bouton pour basculer l'alignement du texte entre la droite et la gauche et la gauche et la droite.]({% image_buster /assets/img/dnd/dnd_template1.png %}){: style="max-width:50%;"}

L'aspect final des messages de droite à gauche dépend largement de la manière dont les fournisseurs de services les restituent. Pour connaître les meilleures pratiques en matière d'élaboration de messages de droite à gauche qui s'affichent le plus précisément possible, reportez-vous à la section [Création de messages de droite à gauche.]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/)

### HTML

#### Attributs HTML pour les liens

La section "Attributs" avec l'attribut "clicktracking" désactivé pour un lien.]({% image_buster /assets/img/dnd_custom_attributes.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Lorsque vous utilisez des liens, des boutons, des images et des vidéos dans l'éditeur glisser-déposer, sélectionnez **Ajouter un nouvel attribut** sous **Attributs** dans la section **Contenu** pour ajouter des informations supplémentaires aux étiquettes HTML dans les e-mails. Cela peut être particulièrement utile pour la personnalisation des messages, la segmentation et la stylisation.

Un cas d'utilisation courant consiste à insérer un attribut dans votre étiquette d'ancrage pour désactiver le suivi des clics lors de l'envoi via Braze.

* **SendGrid :** `clicktracking = "off"`
* **SparkPost :** `data-msys-clicktrack = "0"`

Un autre cas d'utilisation courant consiste à signaler des liens spécifiques comme étant des liens universels. Les liens universels sont des liens qui redirigent vers votre application, offrant ainsi à vos utilisateurs une expérience sur l'application intégrée.

* **SendGrid :** `universal = "true"`
* **SparkPost :** `data-msys-sublink = "open-in-app"` (un [sous-chemin personnalisé](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#custom-link-sub-paths) doit être configuré).

Pour configurer les liens universels, reportez-vous aux [liens universels et aux liens d'application]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/).

Vous pouvez également intégrer l'un de nos partenaires d'attribution, tels que [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) ou [AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/#email-deep-linking-and-click-tracking), pour gérer les liens universels.

Enfin, des attributs prédéfinis sont disponibles pour faciliter l'accessibilité de votre message. Pour en savoir plus, consultez notre article dédié [Créer des messages accessibles dans Braze]({{site.baseurl}}/help/accessibility).

#### Étiquettes personnalisées

Utilisez les étiquettes `<head>` pour ajouter des CSS et des métadonnées dans votre message e-mail. Par exemple, vous pouvez utiliser ces étiquettes pour ajouter une feuille de style ou un favicon. Liquid est pris en charge dans les étiquettes `<head>`.

Tout ce qui est ajouté en dehors des tags `<head>` sera ajouté après l'étiquette `<body>` dans votre e-mail. Cela signifie que le contenu ajouté s'affichera dans l'e-mail.

##### Tags et attributs autorisés par étiquette

| Nom de l'étiquette | Description | Exemple |
| --- | --- | --- |
| `base` | Spécifie l'URL de base pour tous les URL relatifs dans le message. | `<base href="https://example.com" target="_blank">` |
| `link`| Définit les relations entre le message et les ressources externes. | `<link href="styles.css" rel="stylesheet" type="text/css">` |
| `meta` | Fournit des métadonnées telles que la description de la page ou des mots-clés. | `<meta name="description" content="Free Web tutorials">` |
| `style` | Incorpore des styles CSS internes. | `<style type="text/css" media="screen">body { font-size: 16px; }</style>` |
| `title` | Définit le titre du document affiché dans les onglets du navigateur. | `<title>StyleRyde</title>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

| Tags | Attribut | Description | Exemple |
| --- | --- | --- | --- |
| `base` | `href` | URL de base à utiliser pour les URL relatifs. | ```<base href="https://braze.com">``` |
| `base` | `target`| Cible par défaut pour tous les hyperliens et formulaires. | ```<base target="_blank">``` |
| `link` | `href` | URL de la ressource externe. | ```<link href="style.css">``` |
| `link` | `rel` | Définit les relations entre le message actuel et le message lié. | ```<link rel="stylesheet">``` |
| `link` | `type` | Type de ressource liée. | ```<link type="text/css">``` |
| `link` | `sizes` | Spécifie la taille des icônes. | ```<link rel="icon" sizes="32x32" href="favicon-32.png">``` |
| `link` | `media` | Spécifie le support ou l'appareil pour lequel les styles s'appliquent. | ```<link rel="stylesheet" media="screen" href="style.css">``` |
| `meta` | `name` | Définit le titre du document affiché dans les onglets du navigateur. | ```<meta name="viewport" content="width=device-width, initial-scale=1">``` |
| `meta` | `content` | Définit le titre du document affiché dans les onglets du navigateur. | ```<meta name="description" content="Page about our newest products">``` |
| `meta` | `charset` | Déclare l'encodage des caractères. | ```<meta charset="UTF-8">``` |
| `meta` | `property` | Définit le titre du document affiché dans les onglets du navigateur. | ```<meta property="og:title" content="Website title">``` |
| `style` | `type` | Type MIME du contenu du style. | {% raw %}```<style type="text/css">p { color: red; }</style>```{% endraw %} |
| `style` | `media` | Spécifie le support ou l'appareil pour lequel les styles s'appliquent. | ```<style media="print">body { font-size: 12pt; }</style>``` |
| `title` | Aucun attribut | L'étiquette `title` n'accepte aucun attribut. | ```<title>Kitchenerie</title>``` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }
