---
nav_title: Le ciblage des utilisateurs
article_title: Le ciblage des utilisateurs
page_order: 9
page_type: reference
description: "Cet article de référence explique comment cibler votre audience dans votre campagne et les éditeurs de Canvas."
tool:
    - Campaigns
    - Canvas
---

# Le ciblage des utilisateurs

> Déterminer comment cibler vos utilisateurs est l'une des étapes les plus cruciales lors de la création d'une campagne ou d'un Canvas. En comprenant comment segmenter votre audience en fonction de ses comportements, de ses préférences et de ses caractéristiques démographiques, vous pouvez adapter et personnaliser vos messages.

## Création d'une audience ciblée

### Étape 1 : Choisissez les utilisateurs

Sous **Options de ciblage**, vous pouvez utiliser les options suivantes pour choisir les utilisateurs que vous souhaitez cibler pour votre campagne ou Canvas. Seuls les utilisateurs correspondant aux critères que vous avez définis recevront le message. N'oubliez pas que l'appartenance exacte à un segment est toujours calculée juste avant l'envoi du message.

{% tabs local %}
{% tab single segment %}
Pour cibler les membres d'un segment précédemment créé, sélectionnez un segment dans le menu déroulant sous **Cibler les utilisateurs par segment.**
{% endtab %}

{% tab multiple segments %}
Pour cibler des utilisateurs appartenant à plusieurs segments créés précédemment, ajoutez plusieurs segments dans le menu déroulant sous **Cibler les utilisateurs par segment.** L'audience cible qui en résulte sera composée d'utilisateurs du premier segment, du deuxième segment, du troisième segment, etc.
{% endtab %}

{% tab multiple filters %}
Pour cibler les utilisateurs sans ajouter de segmentation, vous pouvez utiliser une série de filtres. Il s'agit d'une audience improvisée lors de la création du message, qui vous permet d'ignorer la création de segments lors de l'envoi à des audiences ponctuelles.

\![Filtres supplémentaires pour un message qui cible les utilisateurs qui ont ouvert une application pour la dernière fois dans la journée, qui n'ont jamais reçu de campagne ou d'étape du canvas et qui ont effectué un achat il y a moins de 30 jours.]({% image_buster /assets/img_archive/additional_filters.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab segments & filters %}
Vous pouvez également cibler les utilisateurs d'un ou de plusieurs segments créés précédemment et qui répondent également à des filtres supplémentaires. Après avoir sélectionné vos segments, vous pouvez affiner votre audience dans la section **Filtres supplémentaires.**  La capture d'écran suivante en témoigne : elle cible les utilisateurs qui font partie du segment "Utilisateurs actifs par jour", du segment "N'ont jamais ouvert d'e-mail" et qui ont effectué un achat il y a plus de 30 jours.

Options de ciblage pour un message comprenant deux segments et un filtre supplémentaire pour un dernier achat effectué il y a moins de 30 jours.]({% image_buster /assets/img_archive/target_segmenter.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab Specific apps %}

Vous pouvez diffuser un message de campagne ou une étape du canvas à des apps spécifiques, par exemple en envoyant un message in-app ou une notification push uniquement aux apps Android ou iOS.

Toutefois, n'oubliez pas qu'un même utilisateur peut utiliser plusieurs applications. Le filtre "Has app" identifie tous les utilisateurs qui possèdent l'application sélectionnée, mais ne contrôle pas les applications qui reçoivent les messages. Par exemple, si vous appliquez un filtre de segment où "A l'app" est défini sur Android, tous les utilisateurs qui ont également l'app iOS recevront également le message sur leur app iOS.

Un filtre pour les utilisateurs qui ont l'application "Hello, World (Android)".]({% image_buster /assets/img_archive/has_app_hello_world.png %}){: style="max-width:60%;"}

Imaginons que vous souhaitiez envoyer un message in-app uniquement aux applications Android.

1. Créez un segment et définissez **Apps et sites web ciblés** sur les **Utilisateurs d'apps spécifiques**, puis sélectionnez votre app Android.

\![Un segment ciblant les utilisateurs d'une application spécifique, "Test_Android".]({% image_buster /assets/img_archive/app_test_android.png %}){: style="max-width:60%;"}

{: start="2"}
2\. Dans votre campagne ou Canvas, allez à l'étape des **audiences cibles** et confirmez que votre segment est ajouté dans la section **Utilisateurs ciblés par segment.**  

\![L'étape "Audiences ciblées" avec un exemple de segmentation sélectionné.]({% image_buster /assets/img_archive/target_users_by_segment_example.png %})

{% alert note %}
Cela ne fonctionnera pas si vous ajoutez votre segment dans la section **Filtres supplémentaires** par le biais d'un filtre d'appartenance à un segment. Vous devez faire directement référence à votre segment dans **Cibler les utilisateurs par segment** pour que votre message ne soit envoyé qu'à cette application.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert tip %}
Pour les campagnes d'e-mail, vous pouvez cibler les groupes initiateurs dans la section **Groupes initiateurs**. Notez que les groupes initiateurs ne sont pas disponibles pour les campagnes API, bien que vous puissiez inclure des groupes initiateurs via une entrée déclenchée par l'API dans une campagne. Pour plus d'informations, voir [Groupes initiateurs]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#seed-groups).
{% endalert %}

### Étape 2 : Testez votre audience

Après avoir ajouté des segments et des filtres à votre audience, vous pouvez tester si votre audience est configurée comme prévu en [recherchant un utilisateur]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) pour confirmer s'il correspond aux critères de l'audience.

La section "Recherche d'un utilisateur" avec un bouton "Recherche d'un utilisateur".]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

#### Résumé pour l'audience

Le **résumé de l'audience** donne un aperçu des personnes qui font partie de votre audience cible. Ici, vous pouvez limiter davantage votre audience en fixant un nombre maximum d'utilisateurs ou en [limitant la]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) vitesse de [réception/distribution]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/).

!La section "Résumé de l'audience" avec des options permettant de fixer un plafond d'utilisateurs ou une limite de débit pour la réception/distribution.]({% image_buster /assets/img_archive/audience_summary.png %})

#### Test A/B

Dans la section **Test A/B**, vous pouvez configurer un test pour comparer les réponses des utilisateurs à plusieurs versions de la même campagne marketing. Ces versions partagent des objectifs marketing similaires mais diffèrent par leur formulation et leur style. L'objectif est d'identifier la version de la campagne qui répond le mieux à vos objectifs de marketing. 

Pour plus d'informations et de bonnes pratiques, consultez le site [Multivarié & Test A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

#### Statistiques d'audience

Braze fournit des statistiques d'audience détaillées des chaînes ciblées dans le pied de page. Plus votre base d'utilisateurs est importante, plus le nombre d'**utilisateurs joignables** est une estimation approximative. Le nombre d'utilisateurs joignables peut diminuer si vous utilisez un [groupe de contrôle global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) ou si vous configurez l'éligibilité des messages. 

- Pour déterminer le nombre exact d'utilisateurs joignables, sélectionnez [Calculer les statistiques exactes]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics), car vous effectuerez une recherche parmi tous les utilisateurs de votre base.
- Pour connaître le pourcentage de votre base d'utilisateurs ciblé ou la valeur vie client (LTV) de ce segment, sélectionnez **Afficher les statistiques supplémentaires.**

##### Pourquoi le nombre d'audiences cibles peut-il différer du nombre d'utilisateurs atteignables ?

{% multi_lang_include segments.md section='Differing audience size' %}

La section "Population totale" avec les comptes estimés pour les utilisateurs joignables dans chaque canal ciblé.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

{% alert note %}
Le calcul de statistiques exactes peut prendre quelques minutes. Cette fonction ne calcule les statistiques exactes qu'au niveau du segment, et non au niveau du filtre ou du groupe de filtres.<br><br>
Pour les segments de grande taille, il est normal d'observer de légères variations, même en calculant des statistiques exactes. La précision de cette fonctionnalité devrait être supérieure ou égale à 99,999 %.
{% endalert %}

## Comment l'audience cible et les critères d'admission s'articulent-ils ?

Lorsque vous créez une campagne ou un canvas dans Braze, le ciblage se fait en deux temps :

1. **Audience ciblée :** Qui peut en bénéficier ?
2. **Critères d'admission :** Qu'est-ce qui déclenche la réception/distribution ?

L'ordre est important : Braze vérifie si une personne fait partie de l'audience cible avant d'évaluer les critères d'entrée. Si un utilisateur n'est pas déjà qualifié pour l'audience à ce moment-là, il n'entrera pas dans la campagne ou dans le Canvas, même s'il déclenche plus tard l'événement d'entrée. Considérez l'audience cible comme une salle d'attente : seuls les utilisateurs qui sont déjà à l'intérieur lorsque le déclencheur se produit peuvent avancer.

### Exemple 1

Vous souhaitez envoyer un message push lors de la première session d'un utilisateur.

Vous définissez :

- **Audience ciblée :** Utilisateurs avec nombre de sessions = 0
- **Événement d'entrée :** Début de la session

Lorsque l'utilisateur ouvre votre application, Braze constate que son nombre de sessions est désormais de 1 et qu'il n'est plus éligible à l'audience. L'événement d'entrée se produit après qu'ils soient éligibles, le message n'est donc pas envoyé.

Pour que cela fonctionne, l'utilisateur doit se qualifier pour l'audience avant le début de la session (retournez l'audience cible et le déclencheur d'entrée).

### Exemple 2

Vous souhaitez envoyer un e-mail aux utilisateurs qui ont dépensé plus de 10 $ au cours des 7 derniers jours.

Vous définissez :

- **Audience ciblée :** Utilisateurs ayant dépensé plus de 10 $ au cours des 7 derniers jours
- **Événement d'entrée :** Tout achat

Imaginez maintenant qu'un utilisateur dépense 12 dollars aujourd'hui. Cela ne déclenche pas l'envoi du message, mais les rend éligibles à l'audience. Ils ne recevront l'e-mail que s'ils effectuent un autre achat ultérieurement.

Une meilleure approche consisterait à faire appel à une audience plus large et à intégrer le filtre dans les critères d'entrée :

- **L'audience :** Tous les utilisateurs (ou votre audience de base)
- **Événement d'entrée :** Effectuer un achat
- **Filtre d'entrée :** Dépenses totales au cours des 7 derniers jours > 10

De cette façon, un achat qualifié répond au filtre et déclenche le message, sans qu'aucune autre action ne soit nécessaire.

## Meilleures pratiques

- Assurez-vous que le segment d'audience inclut les utilisateurs avant les critères de segmentation.
- Évitez d'utiliser des filtres d'audience qui ne s'appliquent qu'après votre événement. Si un filtre dépend de quelque chose qui se produit au moment du déclencheur (comme "nombre de sessions = 0"), il se peut que l'utilisateur ne remplisse plus les conditions requises au moment de la vérification par Braze.
- Utilisez la logique temporelle de manière réfléchie. Par exemple, si vous souhaitez cibler les nouveaux utilisateurs :
    - Définissez votre audience cible sur "première utilisation de l'application au cours des 7 derniers jours".
    - Définissez votre événement d'entrée sur "début de session".
    - De cette façon, seuls les utilisateurs qui en sont encore à leur première semaine se qualifieront et s'inscriront lorsqu'ils commenceront une session.
