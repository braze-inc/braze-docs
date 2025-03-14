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

> Les parcours d’audience Canvas vous permettent de filtrer et de segmenter les utilisateurs de manière intuitive à une grande échelle avec des regroupements d’utilisateurs en fonction de la priorité. 

Ce composant Canvas remplace la nécessité de créer des étapes complètes superflues basées sur l'audience, ce qui vous permet de combiner huit composants complets en un seul. Cela vous permet de simplifier le ciblage des utilisateurs tout en débarrassant vos Canvas de tout encombrement et complexité inutiles. 

![][0]{: style="float:right;max-width:13%;margin-left:15px;margin-top:15px;"}

Les Parcours d’audience sont identiques aux entonnoirs de tri avec des critères de classement. Les utilisateurs sont évalués pour chaque critère par ordre de priorité et sont dirigés vers le critère le plus élevé auquel ils répondent. Cela réduit l'ambiguïté quant à l'endroit où les utilisateurs se rendront et aux messages qu'ils recevront. Notez que les classements ne sont pas [modifiables après le lancement]({{site.baseurl}}/post-launch_edits/).

Le parcours d’audience vous permet d’effectuer les actions suivantes :

- Envoyez les utilisateurs vers différents parcours d'audience (Canvas) en fonction de critères d'audience.
- Affecter une priorité à différents groupes d’audiences, vos messages peuvent ainsi être transférés aux utilisateurs appropriés. 
  - Précédemment, si les utilisateurs répondaient aux critères de deux étapes complètes éventuelles, ils étaient affectés de manière aléatoire. 
- Ciblez les utilisateurs précisément à grande échelle.
  - Créez jusqu'à huit groupes d'audience (deux groupes par défaut et six groupes supplémentaires) par composant, mais il est recommandé de connecter plusieurs étapes de parcours d'audience pour trier davantage vos utilisateurs. 

## Créer un parcours d'audience

![][1]{: style="float:right;max-width:20%;margin-left:15px;"}

Pour ajouter une étape Parcours d'audience, procédez comme suit : 

1. Ajoutez une étape à votre Canvas. 
2. Glissez-déposez le composant depuis la barre latérale ou cliquez sur <i class="fas fa-plus-circle"></i> **Ajouter** au bas d'une étape et sélectionnez **Parcours d'audience**.

Le composant Parcours audience par défaut contient deux groupes d'audience par défaut, **Groupe 1** et **Tous les autres**. Le groupe **Everybody Else** comprend tous les utilisateurs qui ne font pas partie d'un groupe d'audience défini. Ce groupe sera toujours en fin de classement.

### Définir les groupes d'audience

La capture d'écran suivante montre la disposition d'une étape Parcours d'audience développée. Ici, vous pouvez définir jusqu'à huit groupes d'audience (un prédéfini et sept personnalisables). Pour définir un groupe d'audience, sélectionnez le nom du groupe dans l'éditeur de parcours d'audience. Vous pouvez renommer votre groupe d'audience, choisir les filtres et les segments qui s'appliquent à votre groupe, et ajouter ou supprimer des groupes.

Par exemple, si vous souhaitez envoyer à un groupe d'utilisateurs des recommandations alimentaires utiles, vous pouvez sélectionner des filtres d'attributs personnalisés que vous avez déjà créés, tels que "Aime la cuisine asiatique", "Aime la cuisine latine" et "Aime la cuisine européenne". 

![][3]{: style="max-width:90%;margin-left:15px;"}

Une fois l'étape Parcours d'audience terminée, chaque groupe d'audience disposera d'une branche distincte. Vous pouvez continuer à utiliser Parcours d'audience pour filtrer davantage votre audience, ou poursuivre votre parcours Canvas avec les étapes de canvas standard. 

![][4]{: style="max-width:90%;margin-left:15px;"}

### Tester les groupes d’audience

![]({% image_buster /assets/img_archive/user_lookup.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}

Après avoir ajouté des segments et des filtres à votre audience, vous pouvez tester si vos groupes d'audience sont configurés comme prévu en [recherchant un utilisateur]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) pour confirmer qu'il correspond aux critères d'audience. 

## Utilisation de parcours d’audience

Le véritable pouvoir des parcours d’audience réside dans la capacité à affecter une priorité. Bien que cette fonctionnalité n'ait pas besoin d'être utilisée de manière stratégique, certains marketeurs peuvent se retrouver à pousser certains produits vers les utilisateurs, comme des offres spéciales ou des éditions limitées. 

En attribuant une grande priorité à ces groupes, vous pouvez cibler les utilisateurs relevant de filtres et segments spécifiques tout en ciblant des utilisateurs pouvant ne pas répondre à ces critères spécifiques, le tout dans une étape de Canvas.

![][2]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}

Par exemple, supposons que vous souhaitiez envoyer des annonces à un groupe d’utilisateurs pour de nouveaux produits. Vous commenceriez par le classement de filtres pour lesquels ces produits sont pertinents sur le parcours d’audience. Si vous créez une campagne marketing pour l'entreprise « Big Brand » et qu'une nouvelle marque de chaussures vient d'être lancée, vous pouvez sélectionner des filtres tels que « Aime les chaussures Big Brand » ou « Aime Big Brand », et envoyer des messages e-mail différents en fonction du groupe pertinent. 

Lorsque les utilisateurs entrent dans ce composant Parcours d'audience, ils sont d'abord évalués pour savoir s'ils appartiennent au groupe d'audience le mieux classé : Le groupe d'audience A « aime les chaussures Big Brand ». Si c’est le cas, ils passeront au composant suivant défini dans votre Canvas. S'ils « n'aiment pas les chaussures Big Brand », ils seront évalués pour le groupe d'audience suivant, le groupe d'audience B « aime Big Brand », et passeront au composant de canvas suivant si les critères sont remplis. Enfin, les utilisateurs qui n'entrent pas dans les groupes précédents entrent dans le groupe " **Tous les autres"** et passent à la composante Canvas suivante que vous définissez pour ce parcours.

Vous pouvez également voir la performance de cette étape à l’aide des [analyses Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#performance-visualization).

### Segmentation des parcours d'audience à l'aide de numéros de compartiment aléatoires

Si votre canvas utilise une [limitation du débit]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) (telle que la limitation du nombre total d’utilisateurs qui vont recevoir le canvas), Braze vous recommande de ne pas utiliser de numéro de compartiment aléatoire pour segmenter vos parcours d’audience. 

Un [numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) est un attribut de l'utilisateur qui peut être utilisé pour créer des segments uniformément distribués d'utilisateurs aléatoires. Braze utilise le numéro de compartiment aléatoire pour regrouper les utilisateurs durant la phase de segmentation d’entrée dans le Canvas et chaque groupe est traité séparément. Selon les groupes dont le traitement s’achève en premier, certains utilisateurs sont limités lors de l’entrée en raison de la limitation du taux qui pourrait entraîner une distribution non uniforme des utilisateurs quand ils atteignent l’étape du parcours d’audience.

Dans ce cas, essayez plutôt d'utiliser les [chemins d'expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/).

### Utiliser le filtre d'un canal intelligent avec les parcours d'audience

En combinant les étapes des parcours audience et les filtres d'un canal intelligent, vous pouvez adapter votre expérience de communication aux préférences et aux comportements de chaque utilisateur. Ainsi, vos utilisateurs recevront les messages les plus pertinents par le biais des canaux appropriés.

Par exemple, dans une étape de parcours d'audience, vous pouvez créer trois audiences : L'e-mail, le Mobile Push, et tous les autres. Pour l'audience e-mail, ajoutez le filtre `Intelligent Channel is Email`. Pour l'audience Mobile Push, ajoutez le filtre `Intelligent Channel is Mobile Push`. Ensuite, vous pouvez ajouter une étape Message pour chacun des parcours d'audience afin d'envoyer des messages personnalisés et pertinents.

{% alert tip %}
Consultez nos [modèles Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates) pour voir comment vous pouvez personnaliser ces modèles prédéfinis à votre avantage.
{% endalert %}

[0]: {% image_buster /assets/img/audience_path/audience_path.png %}
[1]: {% image_buster /assets/img/audience_path/audience_path1.png %}
[2]: {% image_buster /assets/img/audience_path/audience_path2.png %}
[3]: {% image_buster /assets/img/audience_path/audience_path3.png %}
[4]: {% image_buster /assets/img/audience_path/audience_path4.png %}
