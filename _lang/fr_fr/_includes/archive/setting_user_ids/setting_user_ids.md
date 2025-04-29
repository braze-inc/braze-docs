Les ID utilisateur doivent être définis pour chacun de vos utilisateurs. Ils doivent être inchangés et accessibles lorsqu’un utilisateur ouvre l’application. Nommer correctement vos ID d'utilisateur dès le départ est l'une des étapes les plus **cruciales** de la mise en place des ID d'utilisateur. Nous vous conseillons vivement d'utiliser la norme Braze pour les UUID et les GUID (voir ci-dessous). Nous vous recommandons vivement de fournir cet identifiant, car il vous permettra de.. :

- Suivre vos utilisateurs sur les appareils et plateformes, améliorant la qualité de vos données comportementales et démographiques.
- Importez des données sur vos utilisateurs à l'aide de notre [API de données d'utilisateurs][1].
- Ciblez des utilisateurs spécifiques avec notre [API d'envoi de messages][2] pour les messages généraux et transactionnels.

{% alert note %}
Si un tel identifiant n’est pas disponible, Braze attribue un identifiant unique à vos utilisateurs, mais il vous manquera les capacités énumérées pour les ID utilisateur. Vous devez éviter de définir des ID utilisateur pour les utilisateurs pour lesquels vous n’avez pas d’identifiant unique qui leur soit lié en tant qu’individus. La transmission d’un identifiant d’appareil n’offre aucun avantage par rapport au suivi automatique d’utilisateur anonyme que Braze propose par défaut.
{% endalert %}

{% alert warning %}
Si vous souhaitez inclure une valeur identifiable comme ID utilisateur, pour plus de sécurité, nous **vous recommandons vivement d'** ajouter notre fonctionnalité d'[authentification SDK]({{site.baseurl}}/developer_guide/authentication/) afin d'empêcher l'usurpation d'identité.
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[2]: {{site.baseurl}}/api/endpoints/messaging/
