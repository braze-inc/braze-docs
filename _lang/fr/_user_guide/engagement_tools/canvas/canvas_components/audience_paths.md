---
nav_title: Étape de parcours d’audience
article_title: Étape de parcours d’audience
alias: /audience_paths/
page_order: 1
page_type: reference
description: "Cet article de référence décrit la façon d’utiliser des parcours d’audience dans votre Canvas afin de filtrer et de segmenter les utilisateurs de manière intuitive à une grande échelle avec des regroupements d’utilisateurs en fonction de la priorité stratégique."
tool: Canvas

---

# Étape de parcours d’audience

> Les parcours d’audience Canvas vous permettent de filtrer et de segmenter les utilisateurs de manière intuitive à une grande échelle avec des regroupements d’utilisateurs en fonction de la priorité. Dans cette Canvas Step, il est donc inutile de créer des étapes complètes superflues basées sur l’audience, ce qui vous permet de regrouper 8 étapes complètes en une seule ! L’introduction de cette nouvelle étape vous permettra de simplifier le ciblage de l’utilisateur en supprimant de vos Canvas encombrement et complexité inutiles. 

![][0]{: style="float:right;max-width:13%;margin-left:15px;margin-top:15px;"}

Les Parcours d’audience sont identiques aux entonnoirs de tri avec des critères de classement. Les utilisateurs seront évalués pour chaque critère dans l’ordre de priorité et devront suivre l’itinéraire d’évaluation des meilleurs classements, pour lesquels ils sont éligibles. En d’autres termes, il n’y aura jamais d’ambiguïté par rapport au parcours des utilisateurs et aux messages qu’ils recevront. 

Le parcours d’audience vous permet d’effectuer les actions suivantes :

- Envoyer des utilisateurs vers différents parcours en fonction des critères d’audience.
- Affecter une priorité à différents groupes d’audiences, vos messages peuvent ainsi être transférés aux utilisateurs appropriés. 
  - Précédemment, si les utilisateurs répondaient aux critères de deux étapes complètes éventuelles, ils étaient affectés de manière aléatoire. 
- Ciblez les utilisateurs précisément à grande échelle.
  - Vous pouvez créer jusqu’à 8 groupes d’audiences (2 par défaut et 6 groupes supplémentaires) par étape, mais les utilisateurs voudront peut-être connecter plusieurs étapes de parcours d’audience pour un tri ultérieur. 

## Créer des parcours d’audience

![][1]{: style="float:right;max-width:20%;margin-left:15px;"}

Pour créer des parcours d’audience, ajoutez une étape à votre Canvas. Puis, à l’aide du menu déroulant en haut de la nouvelle étape, sélectionnez `Audience Paths`.

À l’étape Parcours d’audience par défaut, indiqué à droite, il y a déjà deux groupes d’audiences par défaut, **Groupe 1** et **Tout le monde**. Le groupe Tout le monde inclut tout utilisateur qui ne relève pas d’un groupe d’audiences défini. Ce groupe sera toujours en fin de classement.
<br><br><br>

### Définir des groupes d’audiences

La capture d’écran suivante présente la structure d’une étape Parcours d’audience développée. À ce niveau, vous pouvez définir jusqu’à 8 groupes d’audience (1 prédéfini et 7 personnalisables). Pour définir un groupe d’audiences, sélectionnez le nom du groupe dans l’assistant Parcours d’audience. À ce niveau, vous pouvez renommer votre groupe d’audiences, sélectionner les filtres et les segments qui s’appliquent à votre groupe et ajouter ou supprimer des groupes.

Par exemple, si vous souhaitez envoyer des informations de flux utiles à un groupe d’utilisateurs, vous devrez peut-être sélectionner des filtres d’attribut personnalisés que vous avez déjà créés par exemple, « J’aime la cuisine asiatique », « J’aime la cuisine latine », « J’aime la cuisine européenne », etc. 

![][3]{: style="max-width:90%;margin-left:15px;"}

Une fois que l’étape Parcours d’audience est terminée, chaque groupe d’audiences aura une branche distincte vous permettant de continuer à utiliser des parcours d’audience pour filtrer davantage votre audience, le cas échéant ou poursuivre votre parcours Canvas avec les Canvas Step standard. 

![][4]{: style="max-width:90%;margin-left:15px;"}

## Utilisation de parcours d’audience

Le véritable pouvoir des parcours d’audience réside dans la capacité à affecter une priorité. Alors que cette fonctionnalité ne doit pas forcément être utilisée stratégiquement, certains marketeurs doivent transférer eux-mêmes certains produits aux utilisateurs, par exemple des éditions spéciales ou des éditions limitées. 

En attribuant une grande priorité à ces groupes, vous pouvez cibler les utilisateurs relevant de filtres et segments spécifiques tout en ciblant des utilisateurs pouvant ne pas répondre à ces critères spécifiques, le tout dans une Canvas Step.

![][2]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}
Par exemple, supposons que vous souhaitiez envoyer des annonces à un groupe d’utilisateurs pour de nouveaux produits. Vous commenceriez par le classement de filtres pour lesquels ces produits sont pertinents sur le parcours d’audience. Si vous essayez d’envoyer une campagne marketing pour la société « Big Brand » et qu’une nouvelle marque de chaussures vient juste d’être lancée, vous pourriez sélectionner des filtres tels que « Aime les chaussures Big Brand » ou « Aime Big Brand » et envoyer différents types d’e-mails en fonction du groupe pertinent. 

Lorsque des utilisateurs accèdent à cette étape de Parcours d’audience, leur niveau de classement pour le groupe d’audiences sera d’abord évalué, groupe d’audience 1 « Aime les chaussures Big Brand ». Si le classement est pertinent, ils passeront à l’étape suivante définie dans votre Canvas. Si cet utilisateur « N’aime pas les chaussures Big Brand », il sera alors évalué par rapport au niveau d’audience suivant, qui serait le groupe d’audience 2 « Aime Big Brand » et commencera le parcours à la Canvas Step suivante, si les critères sont remplis. Enfin, pour les utilisateurs n’entrant pas dans les groupes précédents, ils entreraient dans le groupe **Tout le monde** et accéderaient à la Canvas Step suivante que vous définissez pour ce parcours.

Vous pouvez également voir la performance de cette étape à l’aide [Analytique Canvas][5].

[0]: {% image_buster /assets/img/audience_path/audience_path.png %}
[1]: {% image_buster /assets/img/audience_path/audience_path1.png %}
[1]: {% image_buster /assets/img/audience_path/audience_path1.png %}
[2]: {% image_buster /assets/img/audience_path/audience_path2.png %}
[3]: {% image_buster /assets/img/audience_path/audience_path3.png %}
[4]: {% image_buster /assets/img/audience_path/audience_path4.png %}
[5]: {{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#performance-visualization