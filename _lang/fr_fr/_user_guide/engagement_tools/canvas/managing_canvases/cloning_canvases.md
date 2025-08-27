---
nav_title: Clonage des Canvas
article_title: Clonage des Canvas
page_order: 3
alias: "/cloning_canvases/"
description: "Cet article de référence décrit comment cloner un Canvas depuis l’éditeur Canvas d’origine vers le flux de travail Canvas Flow."
tool: Canvas
---

# Clonage des Canvas vers Canvas Flow

{% alert important %}
Depuis le 28 février 2023, vous ne pouvez plus créer ou dupliquer de Canvas à l’aide de l’expérience Canvas d’origine. Braze recommande aux clients qui utilisent l’expérience Canvas d’origine de passer à Canvas Flow.
{% endalert %}

> Si vous disposez d’un Canvas de l’éditeur d’origine, vous pouvez le cloner pour créer une copie dans Canvas Flow. En adoptant le flux de travail Canvas Flow, vous avez accès à des [composants Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) légers, à des [propriétés d'entrées persistantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) et à des [modifications a posteriori]({{site.baseurl}}/post-launch_edits). Votre Canvas d’origine ne sera ni altéré ni supprimé.

Pour cloner votre Canvas, procédez comme suit :

1. Accédez au tableau de bord de Canvas. 
2. Identifiez le canvas dont vous souhaitez créer une copie dans le flux de travail Canvas Flow. Vous pouvez cloner des toiles dont le statut est **Brouillon**, **Actif** ou **Arrêté.**  
3. Cliquez sur <i class="fas fa-ellipsis-vertical"></i> **More actions** et sélectionnez **Clone to Canvas Flow.**

![]({% image_buster /assets/img_archive/clone_to_v2_workflow.png %}){: style="max-width:25%;"}

{: start="4"}
4\. Saisissez le nom de votre nouveau canvas et cliquez sur **Cloner dans le flux de canvas**. 

![]({% image_buster /assets/img_archive/clone_to_v2_modal.png %}){: style="max-width:70%;"}

Vous disposez à présent de deux versions de votre Canvas : le Canvas original et la version Canvas Flow. Votre canvas original conserve son statut d'origine et le canvas cloné affiche le statut **Brouillon**. Vous pouvez toujours accéder au Canvas originel, mais Braze recommande d’utiliser Canvas Flow pour continuer à concevoir vos Canvas.

Auparavant, certaines toiles comportant des ramifications ne pouvaient pas être clonées. Désormais, vous pouvez cloner des toiles avec des ramifications. Notez que le clonage de toiles avec des ramifications peut entraîner des étapes déconnectées. Résolvez ces étapes déconnectées (étapes qui ne sont pas précédées d'une autre étape) pour vous assurer que votre parcours Canvas est correctement mappagé.

{% alert note %}
Si vous clonez un canvas actif, Braze continuera à envoyer les utilisateurs via le canvas d'origine. Nous vous recommandons d’arrêter un Canvas avant de le cloner pour éviter d’envoyer des messages en double aux utilisateurs depuis les deux Canvas.
{% endalert %}

![Tableau de bord de Canvas avec deux Canvas répertoriés : Copie V2 de Canvas V1 et Canvas V1. La copie V2 de Canvas V1 comporte une icône indiquant qu'elle utilise le flux de travail Canvas Flow.]({% image_buster /assets/img_archive/clone_to_v2_dashboard.png %})

Vous avez terminé de cloner votre Canvas dans le flux de travail Canvas Flow. Vous pouvez désormais continuer à générer vos Canvas avec cette mise à jour !

## Recommandations

Pour permettre aux utilisateurs existants de poursuivre leur parcours utilisateur après avoir cloné votre Canvas d’origine dans Canvas Flow, vous pouvez ajouter des filtres à votre Canvas existant qui empêchent les nouveaux utilisateurs d’entrer dans le nouveau Canvas.

Si la rééligibilité est désactivée, ajoutez le filtre « Entrés dans une variante du Canvas ». Si la rééligibilité est activée, voici les méthodes possibles à envisager pour s'assurer que les utilisateurs n'entrent pas deux fois dans la même toile :
- Mettez à jour le Canvas existant pour inclure une balise unique. Pour le nouveau Canvas, ajoutez un filtre « Dernier message reçu de la campagne ou Canvas avec balise ». Cela empêche les utilisateurs d'entrer deux fois dans le Canvas après une date d'entrée spécifique (nombre total de jours après l'envoi du dernier message depuis le Canvas d'origine plus la fenêtre de conversion). 
- **La méthode suivante consommera des points de données.** Mettez à jour le Canvas d’origine pour inclure un webhook Braze à Braze qui déclenche un horodatage d’attribut personnalisé à la saisie. Cet attribut peut être utilisé pour empêcher les utilisateurs d’accéder à un nouveau Canvas après la date d’entrée spécifiée (nombre total de jours après l’envoi du dernier message à partir du Canvas d’origine plus la fenêtre de conversion).

Pour les Canvas déclenchés par l'API, coordonnez-vous avec votre équipe d'ingénieurs pour vous assurer que ces Canvas utilisent le nouvel ID de Canvas lorsque les nouveaux Canvas sont prêts à être lancés.

Pour plus d'informations sur les différences entre l'éditeur Canvas original et l'expérience Canvas Flow, consultez la [FAQ Canvas.]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#what-are-the-main-differences-between-canvas-flow-and-the-original-canvas-editor)


