---
nav_title: Aperçu
article_title: Aperçu de l'éditeur de glisser & déposer
alias: "/dnd/aperçu/"
channel: Email
page_order: 1
description: "Cet article de référence couvre divers détails créatifs des blocs de l'éditeur Glisser & Déposer."
tool:
  - Campagnes
  - Toile
---

# Aperçu de l'éditeur de glisser & déposer

{% include video.html id="4dTrkxe8DLo" align="right" %}

> Avec Braze Email, vous pouvez créer des messages électroniques personnalisés et personnalisés dans les campagnes ou Canvas en utilisant une expérience d'édition par glisser & déposer.

## Créer un email de glisser & déposer

### Étape 1 : Sélectionnez l'expérience d'édition

Accédez à l'assistant de messagerie et sélectionnez votre expérience d'édition. Deux options d'édition seront affichées :

- Sélectionnez __Éditeur Glisser & Déposer__ pour sélectionner les modèles créés en utilisant l'éditeur Glisser & Déposer.
- Sélectionnez l'éditeur de code HTML pour utiliser les éditeurs existants et pour voir vos modèles de courriels existants. <br><br>!\[Drag & Drop Editor Workflow\]\[6\]{: style="max-width:80%;"}

{% alert tip %}
Vous pouvez également accéder à tous les modèles dans la page **Modèles & Médias** dans la section **Engagement**.
{% endalert %}

### Étape 2 : Construire la structure de l'e-mail

1. __Assembler des lignes__ - Glisser & déposer différentes configurations de lignes pour concevoir la structure de votre email. Les nouvelles configurations doivent être déplacées au début ou à la fin d'une section existante.
2. __Ajouter du contenu__ - Ajouter des types de contenu désirés aux différentes composantes de ligne.<br><br>!\[Drag & Drop Email GIF\]\[1\]

## Édition de l'expérience

L'expérience d'édition par glisser & déposer est divisée en 3 sections : __Paramètres d'envoi__, __Contenu__et __Aperçu & Test__.

{% tabs %}
{% tab Send Settings %}
__Paramètres d'envoi__

La section Paramètres d'envoi vous permet de configurer votre adresse de départ et de réponse et de définir la ligne de sujet ou le pré-en-tête.

{% alert note %}
Des fonctionnalités avancées apparaîtront dans la campagne ou dans le compositeur de pas de Canvas . Dans les fonctionnalités avancées, vous pouvez modifier vos paramètres CSS en ligne, définir une adresse email BCC, et entrer dans un en-tête ou des paires de valeur clé supplémentaire (si configuré).
{% endalert %}

{% endtab %}
{% tab Content %}
__Contenus__

La section Contenu contient l'éditeur. Il y a trois composants clés dans cette section.

- __Contenu__: Cette section comprend une série de tuiles qui représentent les différents types de contenu que vous pouvez utiliser dans votre message. D'autres seront disponibles à l'avenir. Pour les utiliser, faites simplement glisser un à l'intérieur d'un segment de ligne existant; il s'ajustera automatiquement à la largeur de la colonne. Chaque bloc a ses propres paramètres, tels que le contrôle granulaire du remplissage. Le panneau de droite passe automatiquement à un panneau de propriétés pour l'élément de contenu sélectionné.<br><br> Pour plus d'informations, voir [Propriétés de bloc de l'éditeur]({{site.baseurl}}/dnd/editor_blocks/)<br><br>
- __Lignes__: Les lignes sont des unités de structure qui définissent la composition horizontale d'une section du message en utilisant des colonnes. L'utilisation de plus d'une colonne vous permet de mettre différents éléments de contenu côte à côte. Vous pouvez ajouter tous les éléments structurels dont vous avez besoin à votre message, quel que soit le modèle que vous avez sélectionné au démarrage.<br><br>
- __Paramètres__: Paramètres généraux du message. Ils sont hérités par les sections Lignes et Contenus. Par exemple, la famille de police définie dans les paramètres du message est alors utilisée partout dans votre message, sauf lorsque vous utilisez un paramètre personnalisé.

Ceci est très utile pour construire un message cohérent très rapidement.

{% endtab %}
{% tab Preview and Test %}
__Aperçu & Test__

La section Aperçu & Test vous permet de prévisualiser votre e-mail en fonction de différents utilisateurs.

- __Utilisateur Aléatoire__: Braze sélectionnera aléatoirement un utilisateur dans la base de données et prévisualisera l'email en fonction de ses attributs/informations sur l'événement.
{% alert note %}
Cet utilisateur peut ou non faire partie de vos critères de segmentation. La segmentation est ensuite sélectionnée, de sorte que Braze ne connaît pas votre public cible à ce stade.
{% endalert %}
- __Sélectionner l'utilisateur__: Vous pouvez sélectionner un utilisateur spécifique en fonction de son adresse e-mail ou `external_id`. L'e-mail sera prévisualisé en fonction des attributs et des informations de l'événement de cet utilisateur<br><br>
- __Utilisateur personnalisé__: Vous pouvez personnaliser un utilisateur. Braze offrira des entrées pour tous les attributs et événements disponibles. Vous pouvez entrer toutes les informations que vous souhaitez voir dans l'e-mail de prévisualisation.
{% endtab %}
{% endtabs %}

{% alert note %}
Vision de la boîte de réception est actuellement indisponible durant cette phase de test et sera disponible dans le futur
{% endalert %}

## Détails de la création

### Auto width images

Les images ajoutées à votre e-mail seront automatiquement réglées à __largeur automatique__. Pour ajuster ce paramètre, désactivez __autowidth__ et ajustez le pourcentage de largeur au besoin.

!\[Drag & Drop Image Widths\]\[2\]

### Couleurs de calque

L'éditeur Drag & Drop vous permet de changer la couleur de l'arrière-plan de l'e-mail, de la zone de contenu et des différents composants de contenu. L'ordre des couleurs de l'avant à l'arrière est la couleur du composant de contenu, la couleur de fond de la zone de contenu et la couleur de l'arrière-plan.

!\[Drag & Drop Color Layering\]\[3\]

### Content padding

!\[Drag & Drop Block Options\]\[4\]{: style="float:right;max-width:25%;margin-left:15px;"}

Pour ajuster le remplissage, faites défiler vers le bas vers __Options de bloc__et activez __Plus d'options__. Cela vous permettra de peaufiner votre remplissage pour que votre e-mail soit juste ! <br><br>
### Ajout de liquide

!\[Drag & Drop Personalization\]\[5\]{: style="float:right;max-width:25%;margin-left:15px;"}

Liquid de base est pris en charge dans notre éditeur Drag & Drop. Pour ajouter Liquid dans votre e-mail, sélectionnez __Personnalisation__ sous __Conception / Build__.

Ici, vous pouvez ajouter différents types de personnalisation tels que les attributs par défaut, les attributs périphériques, les attributs personnalisés et plus encore !

Ensuite, prenez votre snippet Liquid généré et ajoutez-le à votre email.
[1]: {% image_buster /assets/img/dnd/dnd.gif %} [2]: {% image_buster /assets/img/dnd/dnd1.png %} [3]: {% image_buster /assets/img/dnd/dnd2. ng %} [4]: {% image_buster /assets/img/dnd/dnd3.png %} [5]: {% image_buster /assets/img/dnd/dndnd4. ng %} [6]: {% image_buster /assets/img/dnd_editor_workflow.png %}