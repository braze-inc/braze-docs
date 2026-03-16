---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes pour les segments
page_order: 12
page_type: reference
tool: 
  - Segments
description: "Cet article de référence couvre les étapes de résolution des problèmes et les considérations à garder à l'esprit lors de l'utilisation des segments."
---

# Résolution des problèmes pour les segments

## Erreurs

### L'audience cible est trop complexe pour être lancée

Cette erreur rare se produit si votre public cible contient un nombre excessif de valeurs d'expression régulière, des valeurs d'expression régulière trop longues, des filtres trop détaillés (tels que « correspond à l'un des 30 000 codes postaux ») ou un nombre trop important de filtres. Cela inclut tous les filtres d'une campagne ou d'une audience Canvas, qu'ils se trouvent dans les segments référencés ou qu'ils aient été ajoutés en tant que filtres à l'étape **« Audience cible** ».

![Erreur pour une audience cible qui atteint le seuil de complexité.]({% image_buster /assets/img/segment/target_audience_too_complex_error.png %})

Lorsque vous ajoutez des filtres de segment à une campagne ou à un canvas, ces filtres sont convertis en requêtes dans Braze (le nombre de caractères de ces requêtes ne correspond pas exactement au nombre de caractères affichés par l'utilisateur du tableau de bord). Lorsque Braze envoie une campagne ou un canvas, nous exécutons une requête qui combine tous les filtres de l'audience ciblée. Nous appliquons un seuil limitant le nombre de caractères dans la requête résultante pour une audience cible. Pour une campagne ou un canvas donné, nous calculons le nombre total de caractères dans tous les segments référencés, y compris tous les filtres supplémentaires. Pour un segment donné, nous calculons le nombre total de caractères pour tous les filtres et toutes les valeurs de filtre.

Votre tableau de bord affichera une erreur lorsqu'une campagne, un canvas ou un segment dépassera le seuil et ne pourra pas être lancé. Si vous rencontrez cette erreur, veuillez simplifier votre audience cible avant de relancer, notamment :

- Si votre audience fait référence à plusieurs segments, veuillez vous assurer que ces segments ne présentent pas de redondances, telles que les mêmes filtres apparaissant dans plusieurs segments.
- Veuillez vous assurer que vous ne faites pas référence à des données obsolètes dans les filtres de segment. Par exemple, un filtre obsolète pourrait rechercher les utilisateurs qui n'ont pas reçu une certaine étape du canvas au cours de la semaine écoulée, même si le canvas a été interrompu depuis plusieurs mois.
- Les segments qui ne sont que des listes d'ID d'utilisateurs ou d'adresses e-mail (qui utilisent souvent une expression régulière) peuvent être convertis en [import]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) [CSV]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) et simplifiés en un seul filtre CSV.
- Si vous disposez d'un CDI, vous pouvez créer un segment CDI qui extrait le groupe directement de votre entrepôt de données.

Vous pouvez également [contacter le service d'assistance]({{site.baseurl}}/braze_support/) pour obtenir de l'aide concernant l'optimisation des filtres.

{% alert note %}
Nous avons commencé à limiter le nombre de caractères en avril 2025. Les campagnes et les canvases lancés avant avril 2025 ont bénéficié d'une clause d'antériorité, ce qui signifie qu'ils peuvent continuer à dépasser la limite, tandis que les campagnes et les canvases nouvellement créés ne peuvent pas dépasser la limite. Si vous modifiez ou clonez une campagne ou un canvas bénéficiant d'une clause d'antériorité, vous **ne** **pourrez pas** la lancer tant que l'audience n'aura pas été mise à jour pour être inférieure à la limite.
{% endalert %}

### Les campagnes actives ou interrompues ou les canevas dépassent le seuil de complexité de l'audience.

Cette bannière s'affiche en haut d'une campagne ou d'une liste Canvas chaque fois que des campagnes ou des Canvases actives ou arrêtées ont des audiences qui dépassent le seuil de complexité de l'audience. Veuillez sélectionner la bannière pour filtrer la liste et n'afficher que les campagnes ou les canevas dépassant le seuil, puis suivez les étapes de résolution des problèmes décrites dans [La cible est trop complexe pour être lancée](#target-audience-is-too-complex-to-launch).

![Une bannière d'erreur indiquant que 4 canevas actifs ou arrêtés dépassent le seuil de complexité de l'audience.]({% image_buster /assets/img/segment/audience_complexity_threshold_banner.png %})

### Le filtre dépasse 10 000 octets ou est trop long pour être enregistré.

Braze limite les filtres de segment individuels à un maximum de 10 000 octets, ce qui équivaut à 10 000 caractères anglais ou 3 333 caractères japonais. Un avertissement s'affiche dès qu'un filtre individuel dépasse 10 000 octets, que ce filtre se trouve dans un segment ou qu'il ait été ajouté directement à une campagne ou à Canvas. 

![Bannière d'erreur pour un filtre dont la valeur dépasse 10 000 caractères.]({% image_buster /assets/img/segment/filter_error.png %})

![Erreur pour un filtre d'attribut personnalisé dont`menu_item`, la valeur d'attribut dépasse 10 000 caractères.]({% image_buster /assets/img/segment/segment_filter_error.png %})


Cette erreur est très rare, mais lorsqu'elle se produit, elle concerne généralement les filtres d'expression régulière qui effectuent le ciblage d'une liste d'ID d'utilisateurs ou d'adresses de e-mail. Dans ce cas, veuillez suivre les étapes suivantes pour convertir les filtres au format CSV :

1. Veuillez exporter les utilisateurs du segment concerné ou du filtre d'expression régulière spécifique. 
2. Veuillez nettoyer le fichier CSV si nécessaire. Vous avez besoin soit d'un ID Braze, soit d'un ID Appboy, mais vous pouvez supprimer toutes les autres colonnes si elles ne sont pas nécessaires. Nous vous recommandons également de vérifier vos données afin de vous assurer qu'elles sont récentes (par exemple, supprimez les utilisateurs que vous ne souhaitez plus cibler).
3. [Veuillez réimporter]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) le fichier CSV, ce qui regroupera automatiquement les utilisateurs dans un filtre CSV unique et hautement efficace.

## Comportement des utilisateurs

### L'utilisateur n'est plus dans une segmentation

Si un utilisateur n'est pas disponible lors de la création d'un segment, les données utilisateur qui déterminent son éligibilité au segment peuvent avoir changé en raison de sa propre activité ou d'autres campagnes et canevas avec lesquels il a interagi précédemment. Si la rééligibilité est activée, leur profil utilisateur affichera les données les plus récentes de la campagne reçue.

### Les informations s'affichent pour les utilisateurs d'autres applications lorsque je filtre pour une application spécifique

Les utilisateurs peuvent avoir plusieurs applications, donc en sélectionnant une application spécifique dans la section **Apps utilisées de** la page de segmentation, vous obtiendrez des résultats pour les utilisateurs qui ont au moins cette application. Le filtre ne donne pas de résultats pour les utilisateurs qui ont exclusivement cette application.

## Filtrage

### Options de filtre modifiées

Vos options de filtre sont liées au format (type de données) que vous passez à Braze pour votre attribut personnalisé. Pour consulter le type de données reconnu par Braze pour vos attributs personnalisés, accédez à **Paramètres des données** > **Attributs personnalisés**.

Si vos options de filtre ont changé, cela signifie que vos données sont transmises à Braze dans un format différent (type de données). Pour une description détaillée des différents types de données et de leurs options de filtrage, reportez-vous aux [types de données d'attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes#custom-attribute-data-types).

N’oubliez pas que la modification du type de données d’un attribut personnalisé sur le tableau de bord entraînera le rejet des données envoyées à Braze dans un format différent.

## Analyses et rapports

### Les *messages envoyés* ou les *destinataires uniques* dans Campaign Analytics ne correspondent pas au nombre de segments. 

Si le nombre de *messages envoyés* ou de *destinataires uniques* de votre analyse de campagne ne correspond pas au nombre d'utilisateurs dans le filtre du segment `Has received message from campaign X`, il peut y avoir deux raisons à cela :

1. **Les utilisateurs peuvent avoir été archivés, rendus orphelins ou supprimés depuis le lancement de la campagne.**<br><br>Par exemple, admettons que 1 000 utilisateurs reçoivent une campagne et que vous fassiez une exportation CSV le même jour. Vous verrez que 1 000 utilisateurs ont été signalés. Au cours du mois suivant, 50 de ces 1 000 utilisateurs sont supprimés (par exemple, par l'endpoint `users/delete`). Lorsque vous effectuez une autre exportation CSV, vous verrez 950 utilisateurs déclarés alors que le nombre de *destinataires uniques* dans **Campaign Analytics** est toujours de 1 000.<br><br>En d'autres termes, la mesure des *destinataires uniques* est un décompte incrémenté, tandis que le segmentateur et l'exportation CSV fournissent un décompte des utilisateurs existants.<br><br>

2. **La campagne est rééligible, de sorte que les utilisateurs peuvent participer plusieurs fois à la campagne**<br><br>Prenons l'exemple d'une campagne e-mail dont la rééligibilité est définie sur zéro minute (les utilisateurs peuvent réintégrer la campagne tant qu'ils répondent aux exigences de segmentation de l'audience), et qui est en cours depuis plus d'un mois. Le nombre de *messages envoyés* dans **Campaign Analytics** ne correspondrait pas à celui du segment, car ce champ inclurait les messages envoyés à des utilisateurs en double.<br><br>En effet, Braze comptabilise les utilisateurs uniques en tant que *destinataires uniques quotidiens*, c'est-à-dire le nombre d'utilisateurs ayant reçu un message particulier au cours d'une journée. Cela signifie que les utilisateurs rééligibles seront comptés plus d'une fois en tant que destinataire unique, car la fenêtre "unique" ne dure qu'un jour. Le nombre de *destinataires uniques quotidiens* peut ainsi être supérieur au nombre de profils utilisateurs dans l'exportation CSV. Les profils utilisateurs figurant dans le fichier CSV seront véritablement uniques.

### L'utilisateur est affecté à deux applications bien qu'il ne se soit connecté qu'à une seule application.

Lors de la création d'un segment, vous pouvez cibler les utilisateurs qui ont [utilisé des applications spécifiques]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform). Un utilisateur doit avoir eu une session dans une application spécifique pour être affecté à cette application ; cependant, il existe deux cas de figure dans lesquels un utilisateur peut tout de même être affecté à une application spécifique sans avoir eu de session dans cette application. 

Le premier scénario concerne le cas où le`app_id`champ est renseigné lors de l'utilisation de`/users/track`l'endpoint, en particulier lors de l'utilisation d'un [événement]({{site.baseurl}}/api/objects_filters/event_object/) ou [d'un objet d'achat]({{site.baseurl}}/api/objects_filters/purchase_object/), comme dans l'exemple suivant :

```json
{
    "events": [
    {
      "external_id": "john_doe123",
      "app_id": "my_web_app_id",
      "name": "Custom Event",
      "time": "2025-08-17T19:20:30+1:00"
    }
  ]
}
```

Le deuxième scénario concerne le cas où le`app_id`champ est renseigné lors de l'utilisation de`/users/track`l'endpoint pour effectuer la migration des tickets push, comme dans cet exemple : 

```json
{
"app_group_id": "{YOUR_APP_GROUP_ID}",
"attributes": [
{
      "push_token_import": false,
      "external_id": "external_id1",
      "country": "US",
      "language": "en",
      "{YOUR_CUSTOM_ATTRIBUTE}": "{YOUR_VALUE}",
      "push_tokens": [
        {"app_id": "{APP_ID_OF_OS}", "token": "{PUSH_TOKEN_STRING}"}
      ]
  }
]
}
```
