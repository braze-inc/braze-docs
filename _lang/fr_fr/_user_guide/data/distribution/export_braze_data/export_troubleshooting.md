---
nav_title: Résolution des problèmes d’exportation
article_title: Résolution des problèmes d’exportation
page_order: 10
page_type: reference
description: "Cet article de référence traite des scénarios de résolution des problèmes courants pour les exportations dans les flux de travail CSV et API."
---

# Résolution des problèmes d’exportation

> Cette page traite des scénarios de résolution des problèmes courants pour les exportations dans les flux de travail CSV et API.  

Veuillez utiliser les onglets pour indiquer si vous exportez vers le **compartiment S3 de Braze par défaut** ou vers un **partenaire de stockage cloud**.

{% sdktabs %}
{% sdktab Default export %}

Si aucun partenaire de stockage n'est défini comme destination d'exportation par défaut, Braze utilise son propre compartiment Amazon S3 pour stocker vos fichiers d'exportation. Les fichiers dans cette configuration sont temporaires et expirent après quatre heures.  

## Exportations CSV  
Lorsque vous exportez un fichier CSV depuis le tableau de bord de Braze, Braze envoie un lien de téléchargement par e-mail à l'utilisateur connecté. Ce lien renvoie vers un fichier ZIP hébergé dans le compartiment S3 de Braze. Le fichier ZIP contient plusieurs fichiers plus petits qui, ensemble, constituent votre exportation.  

Il est nécessaire d'être connecté au tableau de bord de Braze pour utiliser le lien, et le fichier n'est disponible que pendant quatre heures. Par la suite, le lien ne sera plus fonctionnel et les données seront supprimées. Si vous rencontrez des échecs répétés avec des exportations très volumineuses (plus de 500 000 utilisateurs), l'exportation peut échouer. Dans ce cas, veuillez envisager de diviser votre exportation en groupes ou champs plus petits, ou envisager de faire appel à un partenaire de stockage.  

### Erreurs courantes

- Si vous rencontrez une`AccessDenied`erreur, il est possible que le fichier ait déjà expiré ou que vous ayez tenté de l'ouvrir avant qu'il ne soit prêt. Les rapports volumineux peuvent prendre plus de temps à générer. Veuillez patienter quelques minutes et réessayer.  
- Une`ExpiredToken`erreur indique que le délai de quatre heures est écoulé. Veuillez relancer l'exportation afin de générer un nouveau lien.  
- Ce message apparaît`Looks like the file doesn't exist anymore` généralement lorsque l'e-mail est envoyé, mais que le fichier n'a pas encore fini d'être téléchargé vers S3. En attendant quelques minutes, le problème est généralement résolu.  
- Les apostrophes ajoutées au début de certains champs (tels `-`que , `=`,`+` ou `@`) sont attendues. Par exemple,`-1943`cela devient`'-1943`dans le fichier CSV. Braze procède ainsi afin d'éviter que les tableurs n'interprètent incorrectement les données. Cela ne s'applique pas aux exportations JSON, telles que celles renvoyées par l' [endpoint`/users/export/segment` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/).  

## Exportations d'API  
Lorsque vous effectuez une exportation via les API d'exportation sans stockage dans le cloud, Braze enregistre les fichiers dans son compartiment S3. Vous ne recevrez pas d'e-mail. À la place, la réponse API inclura une URL de téléchargement temporaire. L'exportation se présente sous la forme d'un fichier ZIP contenant plusieurs fichiers JSON, chacun avec un utilisateur par ligne.  

Tout comme les exportations CSV, les liens provenant de l'API expirent au bout de quatre heures. Si vous cliquez sur le lien trop tôt, des erreurs peuvent apparaître car le fichier n'est pas encore prêt. Veuillez indiquer`callback_endpoint`dans votre demande si vous souhaitez que Braze vous informe lorsque le fichier sera disponible.  

Les exportations API volumineuses peuvent également expirer. Dans ce cas, veuillez envisager de réduire la taille de vos requêtes ou de connecter un partenaire de stockage pour gérer le volume.  

### Erreurs courantes  
- `AccessDenied` ou signifie`ExpiredToken` généralement que le lien a expiré ou n'était pas encore prêt. Veuillez relancer l'exportation ou patienter un peu plus longtemps.  

{% endsdktab %}

{% sdktab Cloud storage connected %}

Lorsque vous connectez un partenaire de stockage (tel qu'Amazon S3, Google cloud storage ou Azure Blob) et que vous le désignez comme destination d'exportation par défaut depuis la page **de partenaire technologique** du tableau de bord de Braze, Braze enregistre vos exportations directement dans votre compartiment. Cette configuration est généralement plus fiable pour les exportations de grande envergure.  

## Exportations CSV  
Avec les exportations CSV, Braze vous envoie un lien de téléchargement par e-mail. Ce lien expire après un court laps de temps (généralement environ quatre heures). Lorsque vous avez un partenaire de stockage connecté et défini comme destination d'exportation par défaut, Braze envoie également une copie de l'exportation vers votre compartiment connecté. Cette copie est en ligne/en production/instantanée dans votre propre infrastructure, où l'expiration et la conservation sont régies par vos politiques de stockage.  

Dans le stockage cloud, les exportations CSV sont regroupées dans un fichier ZIP. Le fichier ZIP contient plusieurs fichiers CSV de plus petite taille. Les exportations volumineuses sont souvent divisées en segments (par exemple, environ 5 000 utilisateurs chacun), et la taille des segments peut varier. Des fichiers plus petits n'indiquent pas nécessairement des données manquantes. Si le lien envoyé par e-mail ne fonctionne pas, mais que la copie dans votre espace de stockage fonctionne, vous pouvez toujours récupérer vos données directement depuis votre compartiment.  

### Erreurs courantes

- `AccessDenied` signifie que Braze n'a pas pu écrire dans votre compartiment. Veuillez vérifier que vos identifiants et autorisations sont toujours valides.  
- `ExpiredToken` apparaît si Braze n'a plus accès à votre compartiment. Veuillez mettre à jour vos informations d'identification dans le tableau de bord de Braze.  
- Si certains fichiers semblent plus petits que prévu, cela est tout à fait normal. Le processus d'exportation divise intentionnellement les fichiers pour des raisons de stabilité.  
- Les apostrophes ajoutées au début de certains champs (tels `-`que , `=`,`+` ou `@`) sont attendues. Par exemple,`-1943`cela devient`'-1943`dans le fichier CSV. Braze procède ainsi afin d'éviter que les tableurs n'interprètent incorrectement les données. Cela ne s'applique pas aux exportations JSON, telles que celles renvoyées par l' [endpoint`/users/export/segment` ]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/).  

## Exportations d'API  
Lorsque vous exportez des données via les API avec un partenaire de stockage connecté, les fichiers exportés sont enregistrés dans votre compartiment. Aucun e-mail n'est envoyé. Les objets sous-jacents sont stockés dans votre espace de stockage et respectent vos paramètres de conservation, même si les URL de téléchargement fournies par Braze peuvent toujours être limitées dans le temps. Chaque fichier ZIP contient des objets JSON, un par ligne. Les exportations volumineuses peuvent être divisées en plusieurs fichiers ZIP au lieu d'un seul fichier ZIP, ce qui rend généralement cette méthode plus fiable pour les exportations lourdes.  

### Erreurs courantes

- `AccessDenied` survient lorsque Braze ne parvient pas à écrire dans votre compartiment ou lorsque les objets ont été supprimés par la suite. Veuillez vérifier les autorisations et vous assurer qu'aucun élément externe n'efface les fichiers.  
- `ExpiredToken` signifie que les identifiants d'accès de Braze à votre compartiment sont obsolètes. Veuillez les actualiser dans le tableau de bord.  
- Si des fichiers sont manquants ou plus petits que prévu, veuillez d'abord vérifier qu'aucun élément extérieur à Braze ne supprime des objets. Des fichiers de taille réduite sont attendus.  

{% endsdktab %}
{% endsdktabs %}