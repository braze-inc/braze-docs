Lorsque vous [créez des placements dans votre application ou sur votre site web]({{site.baseurl}}/developer_guide/banners/placements/#requestBannersRefresh), votre application envoie une requête à Braze pour récupérer les messages de Banner pour chaque placement.  

- Vous pouvez demander jusqu'à **10 placements par demande d'actualisation**.  
- Pour chaque placement, **Braze** renvoie la **bannière la plus prioritaire que** l'utilisateur est susceptible de recevoir.  
- Si plus de 10 placements sont demandés lors d'une actualisation, seuls les 10 premiers sont renvoyés ; les autres sont abandonnés.  

Par exemple, une application peut demander trois placements dans une demande d'actualisation : `homepage_promo`, `cart_abandonment`, et `seasonal_offer`. Chaque demande renvoie la bannière la plus pertinente pour ce placement.

#### Limite de débit pour les demandes d'actualisation

Si vous utilisez des versions plus anciennes du SDK (avant Swift 13.1.0, Android 38.0.0, Web 6.1.0, React Native 17.0.0 et Flutter 15.0.0), une seule demande d'actualisation est autorisée par session d'utilisateur.

Si vous utilisez des versions minimales plus récentes du SDK (Swift 13.1.0+, Android 38.0.0+, Web 6.1.0+, React Native 17.0.0+ et Flutter 15.0.0+), les demandes d'actualisation sont contrôlées par un algorithme de compartiment à jetons afin d'éviter un polling excessif :

- Chaque session d'utilisateur commence avec cinq jetons d'actualisation.
- Les jetons se rechargent au rythme d'un jeton toutes les 180 secondes (3 minutes).

Chaque appel à `requestBannersRefresh` consomme un jeton. Si vous tentez d'actualiser un jeton alors qu'aucun n'est disponible, le SDK n'effectue pas la demande et enregistre une erreur jusqu'à ce qu'un jeton soit à nouveau disponible. Ceci est important pour les mises à jour à mi-session et déclenchées par des événements. Pour mettre en œuvre des mises à jour dynamiques (par exemple, après qu'un utilisateur ait effectué une action sur la même page), appelez la méthode d'actualisation après l'enregistrement de l'événement personnalisé, mais notez le délai nécessaire à Braze pour ingérer et traiter l'événement avant que l'utilisateur ne se qualifie pour une autre campagne Banner.
