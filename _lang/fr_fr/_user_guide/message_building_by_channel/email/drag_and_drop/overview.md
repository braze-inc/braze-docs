---
nav_title: Création d’un e-mail
article_title: "Création d'un e-mail par glisser-déposer"
alias: "/dnd/overview/"
channel: email
page_order: 0
description: "Cet article explique comment configurer et utiliser correctement l'éditeur de glisser-déposer pour les messages électroniques."
tool:
- Campaigns
- Canvas
---

# Créer un e-mail par glisser-déposer

> Grâce à l'éditeur par glisser-déposer, vous pouvez créer des messages e-mail entièrement personnalisés pour les campagnes ou les toiles, sans utiliser le langage HTML pour construire le corps de votre e-mail.

## À propos de l'éditeur

L'éditeur de glisser-déposer utilise [Contenu](#content) et [Lignes](#rows) comme les deux composants clés pour simplifier votre flux de travail, sans utilisation supplémentaire de HTML.

<table style="width: 100%; table-layout: fixed;">
    <tr>
        <th style="width: 50%;">Contenu</th>
        <th style="width: 50%;">Lignes</th>
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

**Le contenu** comprend une série de tuiles qui représentent différents types de contenu que vous pouvez utiliser dans votre message. Elles sont organisées en trois catégories : de base, multimédia et avancé. 

{% tabs %}
{% tab De base %}

Les blocs de base constituent la fondation de votre e-mail. En utilisant ces blocs, vous pouvez ajouter n'importe lequel des éléments suivants dans le corps de votre e-mail :

- Titre
- Paragraphe
- Liste
- Bouton
- Ligne de séparation
- Espaceur

{% endtab %}
{% tab Les médias %}

Avec des blocs multimédias, vous pouvez ajouter différents contenus visuels tels que des images, des vidéos, des icônes et des liens de réseaux sociaux, ainsi que des icônes personnalisables.

{% endtab %}
{% tab L'avancement %}

Bien que l'éditeur par glisser-déposer simplifie votre flux de travail avec ces blocs, vous pouvez également utiliser des blocs avancés pour insérer du HTML ou ajouter un menu au corps de votre e-mail. Notez que l'utilisation de votre propre HTML peut affecter la façon dont le message est rendu.

{% endtab %}
{% endtabs %}

### Lignes

**Les lignes** sont des unités structurelles qui définissent la composition horizontale d'une section du message en utilisant des colonnes. Vous pouvez soit vider les lignes, soit [blocs de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/). L’utilisation de plusieurs colonnes permet de placer différents éléments de contenu côte à côte. De cette façon, vous pouvez ajouter tous les éléments structurels dont vous avez besoin à votre message, quel que soit le modèle que vous avez sélectionné au début.

#### Style des cartes

Le **style de carte** est une propriété de ligne qui vous permet d'ajouter de l'espace entre les colonnes et d'arrondir leurs angles. Grâce à la mise en forme sous forme de carte, vous pouvez créer des mises en page plus attrayantes pour mettre en valeur vos contenus les plus importants, tels que les fonctionnalités des nouveaux produits, les témoignages, les offres spéciales, les mises à jour, etc.

## Utiliser l'éditeur par glisser-déposer

Vous ne savez pas si votre e-mail doit être envoyé à l’aide d’une campagne ou d’un Canvas ? Les campagnes sont mieux adaptées aux campagnes de communication simples et uniques, tandis que les Canvas sont mieux adaptés aux parcours client en plusieurs étapes.

Une fois que vous avez choisi l'endroit où créer votre message, passons aux étapes de la création d'un e-mail par glisser-déposer.

### Étape 1 : Sélectionnez votre modèle

Après avoir sélectionné l'éditeur par glisser-déposer comme votre expérience d'édition, vous pouvez choisir de :

- Commencez avec un modèle vierge.
- Utilisez un modèle d'e-mail prédéfini à glisser-déposer de Braze.
- Utilisez un modèle d'e-mail par glisser-déposer enregistré.

{% alert note %}
Pour utiliser un modèle HTML personnalisé existant ou des modèles créés par un tiers, vous devez recréer le modèle en sélectionnant **Modèles** > **Modèles d'e-mail** et en sélectionnant **l'éditeur par glisser-déposer** comme expérience d'édition.
{% endalert %}

Vous pouvez également accéder à tous les modèles depuis la section **Modèles**.

Après avoir sélectionné votre modèle, vous verrez un aperçu de votre e-mail sous **Variantes d'e-mails** qui inclut les informations d'envoi et le corps de l'e-mail. 

Ensuite, sélectionnez **Modifier le corps de l'e-mail** pour commencer à concevoir la structure de l'e-mail dans l'éditeur par glisser-déposer. 

![La section "Variantes d'e-mail" avec un exemple de corps d'e-mail.]({% image_buster /assets/img/dnd/dnd_emailvariant.png %})

### Étape 2 : Créez votre e-mail

L'expérience d'édition par glisser-déposer est divisée en trois sections : **Envoi des paramètres**, **Contenu**, et **Aperçu et test**. La magie de la création de votre corps d’e-mail se produit dans la section **Contenu**. Avant de créer votre e-mail, il est important de comprendre les principaux composants de votre expérience de création d’e-mail. Si vous avez besoin d'une révision, consultez la rubrique [À propos de l'éditeur.](#about-the-editor)

Lorsque vous êtes prêt, utilisez les blocs de contenu à glisser-déposer pour créer votre e-mail.

1. Sélectionnez le panneau des **lignes**. Faites glisser et déposez les configurations de ligne dans l'éditeur principal. Cela permettra de définir la mise en page du contenu de votre e-mail.
- Notez que les nouvelles configurations doivent être déplacées vers le haut ou le bas d'une section existante.
- Lorsque vous sélectionnez une configuration de ligne, les paramètres des **propriétés de la ligne** apparaissent pour une personnalisation plus poussée des couleurs d'arrière-plan de la ligne, des images et des tailles de colonne personnalisées.
2. Sélectionnez le panneau **Contenu**. Faites glisser et déposez les tuiles de contenu souhaitées dans les composants de la ligne.
- Vous pouvez également faire glisser n'importe laquelle des tuiles de **Contenu** dans l'éditeur principal. Cela crée une ligne pour la tuile.
- Vous pouvez affiner davantage la tuile en sélectionnant la tuile et en ajustant les champs dans **Propriétés du contenu** et **Options de bloc**. Cela inclut l’espacement des lettres, la marge intérieure, la hauteur de ligne, etc.

Consultez la rubrique [Autres personnalisations](#other-customizations) pour découvrir d'autres moyens de personnaliser davantage votre e-mail par glisser-déposer.

Lorsque vous créez votre e-mail, vous pouvez basculer entre un affichage de bureau et un affichage mobile pour visualiser la façon dont votre communication par e-mail recherchera vos groupes d’utilisateurs. Cela vérifiera que votre contenu est réactif et vous pourrez apporter les ajustements nécessaires en cours de route.

{% alert tip %}
Besoin d’aide pour créer un texte d’exception ? Essayez d'utiliser l'[assistant de rédaction de l'intelligence artificielle]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Saisissez le nom ou la description d'un produit, et l'intelligence artificielle générera un texte marketing semblable à celui d'un humain, que vous pourrez utiliser dans vos messages.

![Bouton de rédaction, situé dans le panneau Contenu à côté des paramètres de style dans l’éditeur par glisser-déposer.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_dnd.png %})
{% endalert %}

### Étape 3 : Ajoutez vos informations d'envoi

Une fois que vous avez terminé de concevoir et de créer votre message électronique, il est temps d'ajouter vos informations d'envoi dans la section **Paramètres d'envoi**.

1. Sous **Envoi d'informations**, sélectionnez un e-mail comme **Nom d'affichage + Adresse de l'expéditeur**. Vous pouvez également personnaliser cela en sélectionnant **Personnaliser à partir du nom d'affichage + adresse**.
2. Sélectionnez un e-mail comme l'**adresse de réponse**. Vous pouvez également personnaliser ceci en sélectionnant **Personnaliser l'adresse de réponse**.
3. Ensuite, sélectionnez un e-mail comme **BCC Address** pour rendre votre e-mail visible à cette adresse.
4. Ajoutez une ligne d'objet à votre e-mail. Vous avez également la possibilité d’ajouter une accroche suivie d’un espace.

Les informations d'envoi que vous avez ajoutées sont renseignées dans un aperçu dans le panneau de droite. Cette information peut également être mise à jour en accédant à **Paramètres** > **Préférences de messagerie** > **Configuration de l'envoi**.

#### Personnalisation de l'en-tête de votre e-mail (avancé)

Sous **Paramètres d'envoi**, vous pouvez ajouter une personnalisation pour les en-têtes d'e-mail et les extras d'e-mail, ce qui vous permet d'envoyer des données supplémentaires à d'autres fournisseurs de services de messagerie. Personnaliser un en-tête d'e-mail, comme inclure le nom d'un destinataire, peut également contribuer à la probabilité que votre e-mail soit ouvert.

{% alert note %}
La fonctionnalité avancée apparaîtra dans le composeur de campagne ou de Canvas. Dans les fonctionnalités avancées, vous pouvez modifier votre paramètre CSS en ligne et entrer un en-tête ou des paires clé-valeur supplémentaires (si configuré).
{% endalert %}

### Étape 4 : Tester votre e-mail

Après avoir ajouté vos informations d'envoi, il est enfin temps de tester votre e-mail. 

Allez à la section **Prévisualiser et tester**. Ici, vous avez la possibilité de prévisualiser votre e-mail en tant qu'utilisateur ou d'envoyer un message de test. Cette section inclut également [Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/), qui vous permet de vérifier que votre e-mail s'est affiché correctement sur différents clients mobiles et web.

{% alert tip %}
Vous pouvez également utiliser l’**aperçu du mode sombre** dans le panneau d'aperçu pour afficher le corps de votre e-mail en mode sombre et, si nécessaire, ajuster votre e-mail.
{% endalert %}

Étant donné que vous pouvez afficher trois versions différentes du même e-mail dans l’éditeur proprement dit, dans Inbox Vision et en testant effectivement l’e-mail, il est important d’aligner les détails entre toutes vos plateformes.

#### Aperçu et test d'envoi
 
Sous l'onglet **Prévisualiser en tant qu'utilisateur**, vous pouvez sélectionner les types d'utilisateurs suivants pour prévisualiser votre message.

- **Utilisateur Aléatoire:** Braze sélectionnera de manière aléatoire un utilisateur de la base de données et prévisualisera l’e-mail en fonction de ses attributs ou informations sur l’événement.
- **Sélectionner un utilisateur :** Vous pouvez sélectionner un utilisateur spécifique en fonction de son adresse e-mail ou de son identifiant externe. L'e-mail sera prévisualisé en fonction des attributs de l'utilisateur et des informations relatives à l'événement.
- **Utilisateur personnalisé:** Vous pouvez personnaliser un utilisateur. Braze offre des entrées pour tous les attributs et événements disponibles. Vous pouvez saisir toutes les informations que vous souhaitez voir dans l’aperçu d’e-mail.

{% alert note %}
L’utilisateur aléatoire peut ou non faire partie de vos critères de segmentation. La segmentation est sélectionnée par la suite, Braze n’est donc pas au courant de votre audience cible à ce stade.
{% endalert %}

Vous pouvez également sélectionner **Copier le lien de prévisualisation** pour générer et copier un lien de prévisualisation partageable qui montre à quoi ressemblera l'e-mail pour un utilisateur aléatoire. Le lien durera sept jours avant de devoir être régénéré. 

Notez que toute modification apportée à un modèle d'e-mail ne se reflétera pas dans un lien généré précédemment. Vous devrez générer un nouvel aperçu du lien pour voir les modifications.

![Aperçu de l'e-mail avec un bouton permettant de "Copier le lien d'aperçu" et de copier le lien généré.]({% image_buster /assets/img/dnd_email_link_preview.png %})

#### Utiliser Inbox Vision

Inbox Vision vous permet de voir vos campagnes d'e-mails du point de vue des clients de messagerie et des appareils mobiles. Pour tester votre message e-mail à l'aide de Inbox Vision, sélectionnez **Inbox Vision** dans la section **Prévisualisation et test** et choisissez **Exécuter Inbox Vision.**

{% alert tip %}
Les images d’arrière-plan dans les envois de messages par e-mail peuvent parfois entraîner l’apparition de lignes blanches ou de déconnexions entre les images. Il est donc important de tester et de vérifier les plus petits détails de votre message par e-mail.
{% endalert %}

Après avoir utilisé l'éditeur glisser-déposer pour concevoir et créer votre message e-mail, continuez à [créer]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas) le reste de votre campagne ou Canvas.

{% details À propos du moteur HTML mis à jour %}
Le moteur sous-jacent qui produit du HTML à partir de l'éditeur de glisser-déposer a été optimisé et mis à jour, ce qui entraîne des avantages liés à la compression et au rendu des fichiers HTML.

La taille moyenne de l’empreinte de nos données HTML exportées a été réduite, ce qui permet un chargement et un rendu plus rapides, une réduction du clipping sur les appareils mobiles et une consommation réduite de bande passante.

Le rendu HTML s'est amélioré grâce aux mises à jour suivantes qui minimisent le nombre de commentaires conditionnels et de requêtes média CSS. En conséquence, les fichiers HTML sont plus petits et mieux codés.
- Migration d'une conception basée sur des éléments `<div>` vers une base de code formatée `<table>` standard
- Les [blocs éditeurs]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) ont été recodés pour plus de concision.
- Le code HTML final est compressé pour supprimer les espaces entre les tags.
- Les lignes de séparation transparentes sont automatiquement converties en marge intérieure de contenu
{% enddetails %}

## Autres personnalisations

Au fur et à mesure que vous continuez à créer des e-mails par glisser-déposer, vous pouvez personnaliser davantage chaque corps d'e-mail en utilisant une combinaison de ces détails créatifs pour capter l'attention et l'intérêt de votre audience pour votre message.

{% alert tip %}
Vous pouvez créer un thème personnalisé pour votre éditeur de glisser-déposer en utilisant [les paramètres de style globaux]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings/).
{% endalert %}

### Images à largeur automatique

Les images ajoutées à votre e-mail seront automatiquement définies sur **Largeur automatique**. Pour ajuster ce paramètre, désactivez **Largeur automatique** et ajustez le pourcentage de largeur selon vos besoins.

![Option de largeur automatique dans l'onglet Contenu de l'éditeur par glisser-déposer.]({% image_buster /assets/img/dnd/dnd1.png %})

### Superposition de couleurs

En utilisant la superposition de couleurs, vous pouvez changer la couleur de l'arrière-plan de l'email, de la zone de contenu et des différents composants de contenu. L'ordre des couleurs de l'avant vers l'arrière est : couleur du composant de contenu, couleur de fond de la zone de contenu et couleur de fond.

![Exemple de superposition de couleurs dans l'éditeur par glisser-déposer.]({% image_buster /assets/img/dnd/dnd2.png %})

### Marge intérieure de contenu

![Options de bloc pour l'éditeur par glisser-déposer.]({% image_buster /assets/img/dnd/dnd3.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Pour ajuster le remplissage, faites défiler vers le bas jusqu'à **Options de bloc** et sélectionnez **Plus d'options**. Vous pouvez ajuster votre espacement pour que votre e-mail soit parfait.

### Arrière-plan du contenu

Vous pouvez ajouter une image d’arrière-plan pour votre configuration de ligne, ce qui vous permet d’incorporer plus d’esthétique et de contenu visuel dans votre campagne e-mail.

### Ajouter une personnalisation

![Options de personnalisation de l'éditeur par glisser-déposer.]({% image_buster /assets/img/dnd/dnd4.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Le Liquid de base est pris en charge dans l'éditeur d'e-mails par glisser-déposer. Pour ajouter une personnalisation à votre e-mail :

1. Sélectionnez **Personnalisation** dans la section **Contenu**. 
2. Sélectionnez le type de personnalisation. Ceci inclut les attributs par défaut (standard), les attributs de l'appareil, les attributs personnalisés, et plus encore. 
3. Recherchez l'attribut à ajouter.
4. Copiez l'extrait de code Liquid généré et collez-le dans le corps de votre e-mail.

La personnalisation liquide n'est pas prise en charge pour les blocs d'images et les champs de type lien de bouton. 

#### Images dynamiques

Vous pouvez choisir d'insérer des images dynamiques dans vos e-mails en incluant du code Liquid dans l'attribut source de votre image. Par exemple, au lieu d'une image statique, vous pouvez insérer {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} comme URL de l'image pour inclure le prénom d'un utilisateur dans l'image. Ceci vous aide à personnaliser vos e-mails pour chaque utilisateur.

### Changer le sens du texte

Lors de la rédaction de votre message, vous pouvez basculer la direction du texte de gauche à droite ou de droite à gauche en sélectionnant le bouton correspondant à la **direction du texte**. Vous pouvez utiliser cette option pour créer des messages dans des langues telles que l'arabe et l'hébreu.

![Menu de l'éditeur par glisser-déposer de l'e-mail avec bouton permettant de basculer l'alignement du texte de droite à gauche ou de gauche à droite.]({% image_buster /assets/img/dnd/dnd_template1.png %}){: style="max-width:50%;"}

L'aspect final des messages de droite à gauche dépend largement de la manière dont les fournisseurs de services les restituent. Pour connaître les meilleures pratiques en matière d'élaboration de messages de droite à gauche qui s'affichent le plus précisément possible, reportez-vous à la section [Création de messages de droite à gauche.]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/)

### Ajouter des attributs HTML aux liens

![La section "Attributs" avec l'attribut "clicktracking" désactivé pour un lien.]({% image_buster /assets/img/dnd_custom_attributes.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Lors de l'utilisation de liens, de boutons, d'images et de vidéos dans l'éditeur de glisser-déposer, sélectionnez **Ajouter un nouvel attribut** sous **Attributs** dans la section **Contenu** pour ajouter des informations supplémentaires aux balises HTML dans les e-mails. Ceci peut être particulièrement utile dans le cadre de la personnalisation, de la segmentation et de la mise en page de messages.

Un cas d'utilisation courant consiste à insérer un attribut dans votre balise d'ancrage pour désactiver le suivi des clics lors de l'envoi via Braze.

* **SendGrid:** `clicktracking = "off"`
* **SparkPost:** `data-msys-clicktrack = "0"`

Un autre cas d’utilisation courant consiste à marquer des liens spécifiques en tant que liens universels. Les liens universels sont des liens qui redirigent vers votre application, offrant à vos utilisateurs une expérience intégrée.

* **SendGrid:** `universal = "true"`
* **SparkPost:** `data-msys-sublink = "open-in-app"` (un [sub-chemin personnalisé](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#custom-link-sub-paths) doit être configuré)

Pour configurer des liens universels, consultez [Liens universels et liens d'application]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/).

Vous pouvez également vous intégrer à l'un de nos partenaires d'attribution, tels que [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) ou [AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/#email-deep-linking-and-click-tracking), pour gérer les liens universels.

Enfin, des attributs prédéfinis sont disponibles pour faciliter l'accessibilité de votre message. Pour en savoir plus, consultez notre article dédié [Créer des messages accessibles dans Braze]({{site.baseurl}}/help/accessibility).

### Choix d'une langue pour l'e-mail

Vous pouvez définir l'attribut linguistique en accédant à l'onglet **Paramètres** et en sélectionnant la langue souhaitée. Vous pouvez également cibler l'attribut utilisateur {%raw%} `{{${language}}}` {%endraw%} si le message est destiné à des utilisateurs ayant des valeurs linguistiques dynamiques.

![Réglage de la valeur "Langue" pour un e-mail.]({% image_buster /assets/img/dnd/language_setting_dnd.png %})

