Les ID utilisateur doivent être définis pour chacun de vos utilisateurs. Ils doivent être inchangés et accessibles lorsqu’un utilisateur ouvre l’application. Nommer correctement vos ID utilisateur dès le départ est l’une des étapes les plus **importantes** de la configuration des ID utilisateur. Nous recommandons vivement d’utiliser la norme Braze des UUID/GUID (détaillée ci-dessous). Nous vous recommandons également vivement de fournir cet identifiant, car vous pourrez ainsi :

- Suivre vos utilisateurs sur les appareils et plates-formes, améliorant la qualité de vos données comportementales et démographiques.
- Importer des données sur vos utilisateurs en utilisant notre [API de données utilisateur][1].
- Cibler des utilisateurs spécifiques avec notre [API de messagerie][2] pour les messages généraux et transactionnels.

{% alert note %}
Si un tel identifiant n’est pas disponible, Braze attribue un identifiant unique à vos utilisateurs, mais il vous manquera les capacités énumérées pour les ID utilisateur. Vous devez éviter de définir des ID utilisateur pour les utilisateurs pour lesquels vous n’avez pas d’identifiant unique qui leur soit lié en tant qu’individus. La transmission d’un identifiant d’appareil n’offre aucun avantage par rapport au suivi automatique d’utilisateur anonyme que Braze propose par défaut.
{% endalert %}

{% alert warning %}
Ces ID d’utilisateur doivent être privés et ne sont pas faciles à obtenir (p. ex., ils ne peuvent pas être une adresse e-mail ou un nom d’utilisateur simple).

Pour plus de sécurité, nous vous recommandons d’ajouter l’[authentification SDK](https://www.braze.com/docs/developer_guide/platform_wide/sdk_authentication/) afin d’empêcher l’usurpation d’identité des utilisateurs.
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[2]: {{site.baseurl}}/api/endpoints/messaging/
