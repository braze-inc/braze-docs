---
nav_title: Clonage des toiles
article_title: Clonage des toiles
page_order: 3
alias: "/cloning_canvases/"
description: "Cet article de référence décrit comment cloner un canvas à partir de l'éditeur de canvas d'origine dans le flux de travail Canvas Flow."
tool: Canvas
---

# Clonage de toiles dans Canvas Flow

{% alert important %}
Vous ne pouvez plus créer ou dupliquer des toiles en utilisant l'expérience Canvas originale. Braze recommande aux clients qui utilisent l'expérience Canvas originale de passer à Canvas Flow, l'expérience Canvas actuelle.
{% endalert %}

> Si vous disposez d'un canvas existant dans l'éditeur d'origine, vous pouvez cloner ce canvas pour en créer une copie dans Canvas Flow. En adoptant le flux de travail Canvas actuel, vous avez accès à des [composants Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/) légers, à des [propriétés d'entrées persistantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/canvas_persistent_entry_properties/) et à des [modifications après le lancement]({{site.baseurl}}/post-launch_edits). Votre Canvas original ne sera ni modifié ni supprimé.

Pour cloner votre Canvas, procédez comme suit :

1. Accédez au tableau de bord de Canvas. 
2. Identifiez le canvas dont vous souhaitez créer une copie dans le flux de travail Canvas Flow. Vous pouvez cloner des toiles dont le statut est **Brouillon**, **Actif** ou **Arrêté.**  
3. Cliquez sur <i class="fas fa-ellipsis-vertical"></i> **More actions** et sélectionnez **Clone to Canvas Flow.**

\![]({% image_buster /assets/img_archive/clone_to_v2_workflow.png %}){: style="max-width:25%;"}

{: start="4"}
4\. Saisissez le nom de votre nouveau canvas et cliquez sur **Cloner dans le flux de canvas**. 

\![]({% image_buster /assets/img_archive/clone_to_v2_modal.png %}){: style="max-width:70%;"}

Vous disposez désormais de deux versions de votre Canvas : le Canvas original et la version Canvas Flow. Votre canvas d'origine conserve son statut d'origine et le canvas cloné a un statut de **brouillon**. Vous pouvez toujours accéder au canvas original, mais Braze recommande d'utiliser le flux de travail Canvas Flow pour continuer à créer vos canvas.

Auparavant, certaines toiles comportant des ramifications ne pouvaient pas être clonées. Désormais, vous pouvez cloner des toiles avec des ramifications. Notez que le clonage de toiles avec des ramifications peut entraîner des étapes déconnectées. Résolvez ces étapes déconnectées (étapes qui ne sont pas précédées d'une autre étape) pour vous assurer que votre parcours Canvas est correctement mappagé.

{% alert note %}
Si vous clonez un canvas actif, Braze continuera à envoyer les utilisateurs via le canvas d'origine. Nous vous recommandons d'arrêter un Canvas avant de le cloner pour éviter d'envoyer des messages en double aux utilisateurs des deux Canvas.
{% endalert %}

!Tableau de bord des toiles avec deux toiles répertoriées : V2 Copie de Canvas V1 et Canvas V1. La copie V2 de Canvas V1 comporte une icône qui indique qu'elle utilise le flux de travail Canvas Flow.]({% image_buster /assets/img_archive/clone_to_v2_dashboard.png %})

Vous avez terminé le clonage de votre canvas dans le flux de travail Canvas Flow. Maintenant, vous pouvez continuer à créer vos toiles dans cette expérience mise à jour !

## Recommandations

Pour permettre aux utilisateurs existants de poursuivre leur parcours après avoir cloné votre Canvas original vers Canvas Flow, vous pouvez ajouter des filtres à votre Canvas existant qui empêchent les nouveaux utilisateurs d'entrer dans le nouveau Canvas.

Si la rééligibilité est désactivée, ajoutez le filtre "Variation de toile saisie". Si la rééligibilité est activée, voici les méthodes possibles à envisager pour s'assurer que les utilisateurs n'entrent pas deux fois dans la même toile :
- Mettez à jour le canvas existant pour y inclure une étiquette unique. Pour le nouveau Canvas, ajoutez un filtre "Dernier message reçu d'une campagne ou d'un Canvas avec étiquette". Cela empêche les utilisateurs d'entrer deux fois dans le Canvas après une date d'entrée spécifique (nombre total de jours après l'envoi du dernier message depuis le Canvas d'origine plus la fenêtre de conversion). 
- **La méthode suivante permet d'enregistrer des points de données.** Mise à jour du Canvas original pour inclure un webhook Braze à Braze qui déclenche un attribut personnalisé date et heure à l'entrée. Cet attribut peut être utilisé pour empêcher les utilisateurs d'entrer dans le nouveau Canvas après la date spécifiée (nombre total de jours après l'envoi du dernier message depuis le Canvas d'origine plus la fenêtre de conversion).

Pour les Canvas déclenchés par l'API, coordonnez-vous avec votre équipe d'ingénieurs pour vous assurer que ces Canvas utilisent le nouvel ID de Canvas lorsque les nouveaux Canvas sont prêts à être lancés.

Pour plus d'informations sur les différences entre l'éditeur Canvas original et l'expérience Canvas Flow, consultez la [FAQ Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/faqs/#what-are-the-main-differences-between-canvas-flow-and-the-original-canvas-editor).


