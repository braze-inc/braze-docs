---
nav_title: Clonage des Canvas
permalink: "/cloning_canvases/"
hidden: true
---

# Clonage des Canvas vers Canvas V2

Le passage au workflow Canvas V2 comprend de nombreux avantages, tels que l’accès à des [composants Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components) légers, des [propriétés d’entrées persistantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/), et [d’édition après lancement]({{site.baseurl}}/post-launch_edits). Si vous avez un Canvas existant que vous souhaitez déplacer vers le workflow V2, vous pouvez cloner votre Canvas pour en créer une copie dans le workflow Canvas V2. Lorsque vous clonez votre Canvas dans le worklow V2 Canvas, votre Canvas original ne sera pas altéré ni supprimé. 

{% alert note %}
Vous ne pouvez cloner que des Canvas avec le statut **Arrêté**. Après le clonage, le nouveau Canvas V2 aura le statut **Ébauche**. 
{% endalert %}

Pour cloner votre Canvas, commencez par aller sur le tableau de bord Canvas. Ensuite, identifiez le Canvas que vous souhaitez créer dans le workflow Canvas V2. Cliquez sur <i class="fas fa-ellipsis-vertical"></i> **More actions** (Plus d’actions) pour le Canvas et sélectionnez **Clone to V2 Workflow** (Cloner vers le workflow V2). 

![][1]{: style="max-width:25%;"}

Ensuite, entrez le nom de votre nouveau Canvas et cliquez sur **Clone to V2 Workflow** (Cloner vers le workflow V2). 

![][2]{: style="max-width:70%;"}

Vous disposez maintenant de deux versions pour votre Canvas : le Canvas original et la version V2. Votre Canvas original aura toujours le statut **Arrêté** et le Canvas cloné aura le statut **Ébauche**. Vous pouvez toujours accéder au Canvas original, mais Braze recommande d’utiliser le workflow Canvas V2 pour continuer à concevoir vos Canvas. 

![Tableau de bord de Canvas avec deux Canvas répertoriés : Copie V2 de Canvas V1,et Canvas V1. La copie V2 de Canvas V1 comporte une icône qui indique qu’elle utilise le workflow Canvas V2.][3]

Vous avez terminé de cloner votre Canvas dans le workflow Canvas V2. Vous pouvez désormais continuer à générer vos Canvas avec cette mise à jour !

## Limitations

Si votre Canvas présente une correspondance avec l’un des éléments suivants, votre Canvas ne peut pas être clonée vers un Canvas V2 :

- Le statut est **Actif** 
- Le statut est **Ébauche**
- Comporte des étapes complètes qui ont des événements d’exception et utilisent le filtre de délai « dans » ou « suivant »/« prochain »"
- Comporte d’une étape complète qui se divise en plusieurs étapes, et n’est pas la première étape du Canvas

Pour en savoir plus sur les différences entre Canvas V1 et Canvas V2, consultez notre article [Canvas V2 101]({{site.baseurl}}/canvas_v2_101/#what-are-the-main-differences-between-canvas-v2-and-canvas-v1).


[1]: {% image_buster /assets/img_archive/clone_to_v2_workflow.png %}
[2]: {% image_buster /assets/img_archive/clone_to_v2_modal.png %}
[3]: {% image_buster /assets/img_archive/clone_to_v2_dashboard.png %}