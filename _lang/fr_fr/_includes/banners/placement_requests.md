Lorsque vous [créez des emplacements dans votre application ou votre site Web]({{site.baseurl}}/developer_guide/banners/placements/#requestBannersRefresh), votre application envoie une requête à Braze afin de récupérer les messages bannière pour chaque emplacement.  

- Vous pouvez demander jusqu'à **10 placements par requête pour actualiser**.  
- Pour chaque emplacement, Braze renvoie la **bannière ayant la priorité la plus élevée** que l'utilisateur est éligible à recevoir.  
- Si plus de 10 placements sont demandés lors de l'actualisation, seuls les 10 premiers sont renvoyés ; les autres sont ignorés.  

Par exemple, une application peut demander trois emplacements dans une requête pour actualiser :`homepage_promo` `cart_abandonment`, et `seasonal_offer`. Chaque requête renvoie la bannière la plus pertinente pour cet emplacement.

#### Limite de débit pour les requêtes d'actualisation

Si vous utilisez des versions SDK antérieures (antérieures à Swift 13.1.0, Android 38.0.0, Web 6.1.0, React native 17.0.0 et Flutter 15.0.0), une seule demande pour actualiser l'application est autorisée par session utilisateur.

Si vous utilisez les versions SDK minimales les plus récentes (Swift 13.1.0+, Android 38.0.0+, Web 6.1.0+, React native 17.0.0+ et Flutter 15.0.0+), les requêtes d'actualisation sont contrôlées par un algorithme de type « token bucket » afin d'éviter un sondage excessif :

- Chaque session utilisateur commence avec cinq jetons pour actualiser.
- Les jetons se rechargent à raison d'un jeton toutes les 180 secondes (3 minutes).

Chaque appel à`requestBannersRefresh`  consomme un jeton. Si vous essayez d'actualiser alors qu'aucun jeton n'est disponible, le SDK n'effectue pas la requête et enregistre une erreur jusqu'à ce qu'un jeton soit réapprovisionné. Ceci est important pour les mises à jour en cours de session et déclenchées par des déclencheurs d'événements. Pour mettre en œuvre des mises à jour dynamiques (par exemple, après qu'un utilisateur a effectué une action sur la même page), veuillez appeler la méthode d'actualisation après l'enregistrement de l'événement personnalisé, mais notez le délai nécessaire à Braze pour ingérer et traiter l'événement avant que l'utilisateur ne soit éligible à une autre campagne Banner.
