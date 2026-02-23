{% if include.content == "Differences" %}

Vous pouvez utiliser les [Teams]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/), les [jeux de permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) et les [rôles d'utilisateur]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) pour gérer l'accès et les responsabilités des utilisateurs du tableau de bord au sein de Braze. Chaque fonctionnalité englobe un ensemble différent d'autorisations et de contrôles d'accès.

### Différences clés

De manière générale, chaque fonctionnalité a une portée différente :
- Les jeux de permissions contrôlent ce que les utilisateurs du tableau de bord peuvent faire dans tous les espaces de travail.
- Les rôles contrôlent ce que les utilisateurs du tableau de bord peuvent faire dans des espaces de travail spécifiques.
- Les Teams contrôlent les audiences que les utilisateurs du tableau de bord peuvent atteindre avec leurs messages.

| Fonctionnalité | Ce que vous pouvez faire | Champ d'application de l'accès |
| - | - | - |
| [Ensembles d’autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) | Regroupez les autorisations liées à des domaines ou à des actions spécifiques (par exemple pour les "développeurs" et les "marketeurs"), puis appliquez-les aux utilisateurs du tableau de bord qui ont besoin des mêmes autorisations dans différents espaces de travail. | A l'échelle de l'entreprise |
| [Rôles]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) | Regrouper les autorisations personnalisées et les contrôles d'accès aux espaces de travail (tels que "Marketer - Fashion Brands", où l'utilisateur dispose de certaines autorisations associées à son rôle de marketeur et est limité aux espaces de travail "Fashion Brands"). Attribuez ensuite un rôle aux utilisateurs du tableau de bord pour leur accorder directement les autorisations et l'accès à l'espace de travail associés. <br><br>Les utilisateurs disposant de ce niveau d'accès sont généralement des gestionnaires dans des configurations plus étroitement contrôlées avec de nombreuses marques ou espaces de travail régionaux dans un tableau de bord. | Espaces de travail spécifiques |
| [Équipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/#creating-teams) | Limitez l'accès des utilisateurs du tableau de bord aux ressources en fonction de l'audience (comme l'emplacement/localisation de la base de clients, la langue et les attributs personnalisés). <br><br>Les utilisateurs disposant de ce niveau d'accès sont généralement responsables d'un périmètre spécifique au sein de la marque sur laquelle ils travaillent, comme par exemple créer du contenu spécifique à une langue pour une marque multilingue. | Tableau de bord spécifique |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endif %}