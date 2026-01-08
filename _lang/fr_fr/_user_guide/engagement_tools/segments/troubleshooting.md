---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes segmentations
page_order: 12
page_type: reference
tool: 
  - Segments
description: "Cet article de référence couvre les étapes de résolution des problèmes et les considérations à garder à l'esprit lors de l'utilisation des segments."
---

# Résolution des problèmes de segmentation

## Erreurs

### L'audience ciblée est trop complexe pour être lancée

Cette erreur rare se produit si votre audience cible contient trop de valeurs d'expressions régulières, des valeurs d'expressions régulières trop longues, des filtres trop détaillés (tels que "est l'un des 30 000 codes postaux"), ou trop de filtres. Cela inclut tous les filtres d'une campagne ou d'une audience Canvas, que les filtres soient situés dans les segments référencés ou ajoutés en tant que filtres à l'étape du **ciblage de l'audience**.

Lorsque vous ajoutez des filtres de segmentation à une campagne ou à un Canvas, ces filtres sont traduits en requêtes dans Braze (le nombre de caractères de ces requêtes n'est pas 1:1 par rapport au nombre de caractères que voit un utilisateur du tableau de bord). Lorsque Braze envoie une campagne ou un canvas, nous lançons une requête qui combine tous les filtres de l'audience ciblée. Nous appliquons un seuil limitant le nombre de caractères dans la requête résultante pour une audience ciblée. Pour une campagne ou un Canvas donné, nous additionnons le nombre de caractères sur l'ensemble des segments référencés, y compris tous les filtres supplémentaires. Pour un segment donné, nous additionnons le nombre de caractères pour tous les filtres et toutes les valeurs de filtre.

Votre tableau de bord affichera une erreur lorsqu'une campagne, un Canvas ou un segment dépasse le seuil et ne peut être lancé. Si vous recevez cette erreur, simplifiez votre audience cible avant de procéder à un nouveau ciblage, notamment :

- Si votre audience fait référence à plusieurs segments, assurez-vous que les segments ne sont pas redondants, par exemple que les mêmes filtres apparaissent dans plusieurs segments.
- Assurez-vous que vous ne faites pas référence à des données obsolètes dans les filtres de segmentation. Par exemple, un filtre obsolète peut rechercher les utilisateurs qui n'ont pas reçu une certaine étape du canvas au cours de la semaine écoulée, même si le canvas a été arrêté depuis des mois.
- Les segments qui ne sont que des listes d'ID d'utilisateurs ou d'e-mails (qui utilisent souvent un filtre expression régulière) peuvent être convertis en [importation]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) CSV et être simplifiés en un seul filtre CSV.
- Si vous disposez de CDI, vous pouvez créer un segment CDI qui extrait le groupe directement de votre entrepôt de données.

Vous pouvez également [contacter le service d'assistance]({{site.baseurl}}/braze_support/) pour obtenir de l'aide sur l'optimisation des filtres.

{% alert note %}
Nous avons commencé à limiter le nombre de caractères en avril 2025. Les campagnes et les canevas lancés avant avril 2025 ont bénéficié de droits acquis, ce qui signifie qu'ils peuvent continuer à dépasser la limite, alors que les campagnes et les canevas nouvellement créés ne peuvent pas dépasser la limite. Si vous modifiez ou clonez une campagne ou un Canvas bénéficiant de droits acquis, vous **ne pourrez pas** le lancer tant que l'audience n'aura pas été mise à jour pour être inférieure à la limite.
{% endalert %}

### X campagnes ou canevas actifs ou arrêtés dépassent le seuil de complexité de l'audience.

Cette bannière s'affiche en haut de la liste d'une campagne ou d'un canvas lorsque des campagnes ou des canevas actifs ou arrêtés ont des audiences qui dépassent le seuil de complexité de l'audience. Sélectionnez la bannière pour filtrer la liste jusqu'aux seules campagnes ou Toiles dépassant le seuil, puis suivez les étapes de résolution des problèmes dans [L'audience cible est trop complexe pour être lancée](#target-audience-is-too-complex-to-launch).

### Le filtre dépasse 10 000 caractères ou est trop long pour être enregistré

Braze limite les filtres de segmentation individuels à un maximum de 10 000 caractères. Un avertissement apparaît dès qu'un filtre individuel dépasse 10 000 caractères, que le filtre se trouve dans un segment ou qu'il soit ajouté directement à la campagne ou au Canvas. 

Cette erreur se produit très rarement, mais lorsqu'elle se produit, c'est généralement avec des filtres d'expression régulière qui ciblent une liste d'ID d'utilisateurs ou d'adresses e-mail. Dans ce cas, vous pouvez suivre les étapes suivantes pour convertir les filtres en un fichier CSV :

1. Exportez les utilisateurs du segment concerné ou du filtre d'expression régulière spécifique. 
2. Nettoyez le CSV si nécessaire. Vous avez besoin de l'ID Braze ou de l'ID Appboy, mais vous pouvez supprimer toutes les autres colonnes si elles ne sont pas nécessaires. Nous vous recommandons également d'examiner vos données pour confirmer qu'elles sont récentes (par exemple, supprimez les utilisateurs que vous n'essayez plus de cibler).
3. [Importez]({{site.baseurl}}/user_guide/data/unification/user_data/import_users/csv/) à nouveau le fichier CSV, qui regroupe automatiquement les utilisateurs en un seul filtre CSV très efficace.

## Comportement des utilisateurs

### L'utilisateur n'est plus dans une segmentation

Si un utilisateur n'est pas disponible lors de la création d'un segment, les données utilisateur qui déterminent son éligibilité au segment peuvent avoir changé en raison de sa propre activité ou d'autres campagnes et canevas avec lesquels il a interagi précédemment. Si la rééligibilité est activée, leur profil utilisateur affichera les données les plus récentes de la campagne reçue.

### Les informations s'affichent pour les utilisateurs d'autres applications lorsque je filtre pour une application spécifique

Les utilisateurs peuvent avoir plusieurs applications, donc en sélectionnant une application spécifique dans la section **Apps utilisées de** la page de segmentation, vous obtiendrez des résultats pour les utilisateurs qui ont au moins cette application. Le filtre ne donne pas de résultats pour les utilisateurs qui ont exclusivement cette application.

## Filtrage

### Modification des options de filtrage

Vos options de filtrage sont liées au format (type de données) que vous transmettez à Braze pour votre attribut personnalisé. Pour consulter le type de données reconnu par Braze pour vos attributs personnalisés, accédez à **Paramètres des données** > Attributs personnalisés.

Si vos options de filtrage ont changé, cela indique que vos données sont transmises à Braze dans un format (type de données) différent de celui d'avant. Pour une description détaillée des différents types de données et de leurs options de filtrage, reportez-vous aux [types de données d'attributs personnalisés]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes#custom-attribute-data-types).

Gardez à l'esprit que la modification du type de données d'un attribut personnalisé dans le tableau de bord rejettera les données envoyées à Braze dans un format différent.

## Analyse/analytique (si utilisé asjectivement)

### Les *messages envoyés* ou les *destinataires uniques* dans Campaign Analytics ne correspondent pas au nombre de segments. 

Si le nombre de *messages envoyés* ou de *destinataires uniques* de votre analyse de campagne ne correspond pas au nombre d'utilisateurs dans le filtre du segment `Has received message from campaign X`, il peut y avoir deux raisons à cela :

1. **Les utilisateurs peuvent avoir été archivés, rendus orphelins ou supprimés depuis le lancement de la campagne.**<br><br>Par exemple, supposons que 1 000 utilisateurs reçoivent une campagne et que vous fassiez une exportation CSV le même jour. Vous verrez que 1 000 utilisateurs ont été signalés. Au cours du mois suivant, 50 de ces 1 000 utilisateurs sont supprimés (par exemple, par l'endpoint `users/delete` ). Lorsque vous effectuez une autre exportation CSV, vous verrez 950 utilisateurs déclarés alors que le nombre de *destinataires uniques* dans **Campaign Analytics** est toujours de 1 000.<br><br>En d'autres termes, la mesure des *destinataires uniques* est un décompte incrémenté, tandis que le segmentateur et l'exportation CSV fournissent un décompte des utilisateurs existants.<br><br>

2. **La campagne est rééligible, de sorte que les utilisateurs peuvent participer plusieurs fois à la campagne.**<br><br>Prenons l'exemple d'une campagne e-mail dont la rééligibilité est réglée sur zéro minute (les utilisateurs peuvent réintégrer la campagne tant qu'ils répondent aux exigences de la segmentation de l'audience), et qui est en cours depuis plus d'un mois. Le nombre de *messages envoyés* dans **Campaign Analytics** ne correspondrait pas à celui du segment, car ce champ inclurait les messages envoyés à des utilisateurs en double.<br><br>En effet, Braze comptabilise les utilisateurs uniques en tant que *destinataires uniques quotidiens*, c'est-à-dire le nombre d'utilisateurs ayant reçu un message particulier au cours d'une journée. Cela signifie que les utilisateurs rééligibles seront comptés plus d'une fois en tant que destinataire unique, car la fenêtre "unique" ne dure qu'un jour. Le nombre de *destinataires uniques quotidiens* peut ainsi être supérieur au nombre de profils utilisateurs dans l'exportation CSV. Les profils utilisateurs figurant dans le fichier CSV seront véritablement uniques.

### L'utilisateur est affecté à deux applications alors qu'il n'enregistre une session que dans une seule application.

Lors de la création d'un segment, vous pouvez cibler les utilisateurs qui ont [utilisé des apps spécifiques.]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#step-3-choose-your-app-or-platform) Un utilisateur doit avoir ouvert une session dans une application spécifique pour être affecté à cette application ; cependant, il existe deux scénarios dans lesquels un utilisateur peut être affecté à une application spécifique sans avoir ouvert de session dans l'application. 

Le premier scénario est le suivant : le champ `app_id` est rempli lors de l'utilisation de l'endpoint `/users/track`, en particulier lors de l'utilisation d'un [événement]({{site.baseurl}}/api/objects_filters/event_object/) ou d'un [objet d'achat]({{site.baseurl}}/api/objects_filters/purchase_object/), comme dans cet exemple :

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

Le deuxième scénario est le suivant : le champ `app_id` est rempli lors de l'utilisation de l'endpoint `/users/track` pour migrer des tickets push, comme dans cet exemple : 

```json
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
```
