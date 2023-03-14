---
nav_title: Parcours d’audience 
article_title: Parcours d’audience 
alias: /audience_paths/
page_order: 1
page_type: reference
description: "Cet article de référence décrit la façon d’utiliser des parcours d’audience dans votre Canvas afin de filtrer et de segmenter les utilisateurs de manière intuitive à une grande échelle avec des regroupements d’utilisateurs en fonction de la priorité stratégique."
tool: Canvas

---

# Parcours d’audience 

> Les parcours d’audience Canvas vous permettent de filtrer et de segmenter les utilisateurs de manière intuitive à une grande échelle avec des regroupements d’utilisateurs en fonction de la priorité. Ce composant de Canvas supplante la nécessité de créer des étapes complètes superflues basées sur l’audience, ce qui vous permet de regrouper 8 composants complets en un seul ! Ce nouveau composant de parcours d’audience vous permettra de simplifier le ciblage de l’utilisateur en supprimant de vos Canvas encombrement et complexité inutiles. 

![][0]{: style="float:right;max-width:13%;margin-left:15px;margin-top:15px;"}

Les Parcours d’audience sont identiques aux entonnoirs de tri avec des critères de classement. Les utilisateurs seront évalués pour chaque critère dans l’ordre de priorité et devront suivre l’itinéraire d’évaluation des meilleurs classements, pour lesquels ils sont éligibles. En d’autres termes, il n’y aura jamais d’ambiguïté par rapport au parcours des utilisateurs et aux messages qu’ils recevront. 

Le parcours d’audience vous permet d’effectuer les actions suivantes :

- Envoyer des utilisateurs vers différents parcours en fonction des critères d’audience.
- Affecter une priorité à différents groupes d’audiences, vos messages peuvent ainsi être transférés aux utilisateurs appropriés. 
  - Précédemment, si les utilisateurs répondaient aux critères de deux étapes complètes éventuelles, ils étaient affectés de manière aléatoire. 
- Ciblez les utilisateurs précisément à grande échelle.
  - Vous pouvez créer jusqu’à 8 groupes d’audiences (2 par défaut et 6 groupes supplémentaires) par composant, mais les utilisateurs voudront peut-être connecter plusieurs étapes de parcours d’audience pour un tri ultérieur. 

## Créer des parcours d’audience

![][1]{: style="float:right;max-width:20%;margin-left:15px;"}

Pour créer des parcours d’audience, commencez par ajouter une étape à votre Canvas. Pour Canvas Flow, glissez-déplacez le composant depuis la barre latérale ou cliquez le bouton plus <i class="fas fa-plus-circle"></i> en bas d’une étape et sélectionnez **Parcours d’audience**. Pour l’éditeur Canvas d’origine, utilisez le menu déroulant en haut de la nouvelle étape complète dans votre flux de travail et sélectionnez **Parcours d’audience**.

Dans le composant Parcours d’audience par défaut affiché à droite, il y a déjà deux groupes d’audiences par défaut, **Groupe 1** et **Tout les autres**. Le groupe Tout le monde inclut tout utilisateur qui ne relève pas d’un groupe d’audiences défini. Ce groupe sera toujours en fin de classement.
<br><br><br>

### Définir des groupes d’audiences

La capture d’écran suivante présente la structure d’un composant Parcours d’audience développé. À ce niveau, vous pouvez définir jusqu’à 8 groupes d’audience (1 prédéfini et 7 personnalisables). Pour définir un groupe d’audiences, sélectionnez le nom du groupe dans l’assistant Parcours d’audience. À ce niveau, vous pouvez renommer votre groupe d’audiences, sélectionner les filtres et les segments qui s’appliquent à votre groupe et ajouter ou supprimer des groupes.

Par exemple, si vous souhaitez envoyer des informations de flux utiles à un groupe d’utilisateurs, vous devrez peut-être sélectionner des filtres d’attribut personnalisés que vous avez déjà créés par exemple, « J’aime la cuisine asiatique », « J’aime la cuisine latine », « J’aime la cuisine européenne », etc. 

![][3]{: style="max-width:90%;margin-left:15px;"}

Une fois que le composant Parcours d’audience est terminé, chaque groupe d’audiences aura une branche distincte vous permettant de continuer à utiliser des parcours d’audience pour filtrer davantage votre audience, le cas échéant ou poursuivre votre parcours Canvas avec les composants Canvas habituels. 

![][4]{: style="max-width:90%;margin-left:15px;"}

### Tester les groupes d’audience

Après avoir ajouté des segments et des filtres à votre audience, vous pouvez tester si vos groupes d’audience sont configurés comme prévu en [recherchant un utilisateur]({{site.baseurl}}/user_guide/engagement_tools/segments/user_lookup/) pour confirmer s’il correspond aux critères de l’audience.

![]({% image_buster /assets/img_archive/user_lookup.png %})

## Utilisation de parcours d’audience

Le véritable pouvoir des parcours d’audience réside dans la capacité à affecter une priorité. Alors que cette fonctionnalité ne doit pas forcément être utilisée stratégiquement, certains marketeurs doivent transférer eux-mêmes certains produits aux utilisateurs, par exemple des éditions spéciales ou des éditions limitées. 

En attribuant une priorité élevée à ces groupes, vous pouvez cibler les utilisateurs relevant de filtres et segments spécifiques tout en ciblant des utilisateurs pouvant ne pas répondre à ces critères spécifiques, le tout dans un seul composant Canvas.

![][2]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}
Par exemple, supposons que vous souhaitiez envoyer des annonces à un groupe d’utilisateurs pour de nouveaux produits. Vous commenceriez par le classement de filtres pour lesquels ces produits sont pertinents sur le parcours d’audience. Si vous essayez d’envoyer une campagne marketing pour la société « Big Brand » et qu’une nouvelle marque de chaussures vient juste d’être lancée, vous pourriez sélectionner des filtres tels que « Aime les chaussures Big Brand » ou « Aime Big Brand » et envoyer différents types d’e-mails en fonction du groupe pertinent. 

Lorsque des utilisateurs accèdent à ce composant de Parcours d’audience, ils seront tout d’abord évalués s’ils font partie du groupe d’audience le plus élevé, le groupe d’audience 1 « Aime les chaussures Grande Marque ». Si c’est le cas, ils passeront au composant suivant défini dans votre Canvas. Si cet utilisateur « N’aime pas les chaussures Grande Marque », il sera alors évalué par rapport au niveau d’audience suivant, qui serait le groupe d’audience 2 « Aime Grande Marque » et commencera le parcours au composant Canvas suivant, si les critères sont remplis. Enfin, pour les utilisateurs n’entrant pas dans les groupes précédents, ils entreraient dans le groupe **Tous les autres** et accéderaient au composant Canvas suivant que vous définissez pour ce parcours.

Vous pouvez également voir la performance de cette étape à l’aide de l’[Analytique Canvas][5].

### Les parcours d’audience sont des numéros de compartiment aléatoire

Si votre Canvas utilise une [limitation du débit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) (telle que la limitation du nombre total d’utilisateurs qui vont recevoir le Canvas), Braze vous recommande de ne pas utiliser de numéro de compartiment aléatoire pour segmenter vos parcours d’audience. 

Un [numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/ab_testing_with_random_buckets/) est un attribut utilisateur qui peut être utilisé pour créer des segments distribués uniformément d’utilisateurs aléatoires. Braze utilise le numéro de compartiment aléatoire pour regrouper les utilisateurs durant la phase de segmentation d’entrée dans le Canvas et chaque groupe est traité séparément. Selon les groupes dont le traitement s’achève en premier, certains utilisateurs sont limités lors de l’entrée en raison de la limitation du taux qui pourrait entraîner une distribution non uniforme des utilisateurs quand ils atteignent l’étape du parcours d’audience.

Dans ce scénario, essayez d’utiliser [Chemins d’expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) à la place.

[0]: {% image_buster /assets/img/audience_path/audience_path.png %}
[1]: {% image_buster /assets/img/audience_path/audience_path1.png %}
[1]: {% image_buster /assets/img/audience_path/audience_path1.png %}
[2]: {% image_buster /assets/img/audience_path/audience_path2.png %}
[3]: {% image_buster /assets/img/audience_path/audience_path3.png %}
[4]: {% image_buster /assets/img/audience_path/audience_path4.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#performance-visualization
