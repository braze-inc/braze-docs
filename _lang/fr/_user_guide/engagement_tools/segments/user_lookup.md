---
nav_title: Recherche d’utilisateur
article_title: Recherche d’utilisateur
page_order: 5.5
page_type: reference
description: "Cet article de référence décrit comment rechercher un utilisateur pour confirmer si un utilisateur correspond à un segment ou filtre donné."
---

# Recherche d’utilisateur

> Lorsque vous configurez votre audience pour une campagne ou un Canvas, vous pouvez rechercher un utilisateur spécifique directement à partir du compositeur pour tester si vos filtres et vos segments sont configurés correctement. Cela peut également être utile lors de la résolution des problèmes d’une campagne ou d’un Canvas qui n’envoie pas comme prévu : par exemple, si les utilisateurs ne reçoivent pas de message alors qu’ils le devraient.

La recherche d’utilisateur est disponible lors de :

- La création d’un segment
- La configuration d’une campagne ou d’une audience Canvas
- La configuration d’une étape de Parcours d'audience

![Fonctionnalité de recherche d’utilisateur lors de la création d’une audience.][1]{: style="max-width:60%"}

Pour vérifier si un utilisateur correspond aux critères d’audience, cliquez sur **Lookup User (Rechercher un utilisateur)** et recherchez un `external_id` ou un `braze_id` d’utilisateur.

## Résultats

Lorsqu’un utilisateur correspond aux critères de segment, de filtre et d’application, vous voyez les éléments suivants :

![Résultats de la recherche d’utilisateur indiquant « user007 correspond à tous les segments, filtres et applications ».][2]{: style="max-width:60%"}

Lorsqu’un utilisateur ne correspond pas à une partie ou à la totalité des critères du segment, du filtre ou de l’application, les critères manquants sont répertoriés à des fins de résolution des problèmes.

![Résultats de la recherche d’utilisateur indiquant « user1234 ne correspondent pas aux critères de ciblage suivants » avec deux segments répertoriés dans un tableau.][3]{: style="max-width:60%"}


[1]: {% image_buster /assets/img_archive/user_lookup.png %}
[2]: {% image_buster /assets/img_archive/user_lookup_match.png %}
[3]: {% image_buster /assets/img_archive/user_lookup_nomatch.png %}