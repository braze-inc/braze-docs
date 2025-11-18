Lorsque vous [créez des placements dans votre application ou sur votre site web]({{site.baseurl}}/developer_guide/banners/placements/#requestBannersRefresh), votre application envoie une requête à Braze pour récupérer les messages de Banner pour chaque placement.  

- Vous pouvez demander jusqu'à **10 placements par session d'utilisateur.**  
- Pour chaque placement, **Braze** renvoie la **bannière la plus prioritaire que** l'utilisateur est susceptible de recevoir.  
- Si plus de 10 placements sont demandés au cours d'une session, seuls les 10 premiers sont renvoyés ; les autres sont abandonnés.  

Par exemple, une application peut demander trois placements au cours d'une même session : `homepage_promo` `cart_abandonment` , et `seasonal_offer`. Chaque demande renvoie la bannière la plus pertinente pour ce placement.
