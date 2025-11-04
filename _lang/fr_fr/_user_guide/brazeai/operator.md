---
nav_title: Opérateur
article_title: Opérateur BrazeAI
page_order: 0.7
alias: /operator/
description: "Cet article de référence porte sur BrazeAI Operator, un assistant doté d'une intelligence artificielle créé dans le tableau de bord de Braze."
---

# Opérateur <sup>BrazeAITM</sup> 

> <sup>BrazeAITM</sup> Operator est un assistant doté d'une intelligence artificielle créé dans le tableau de bord de Braze. Operator vous aide à trouver des réponses, à résoudre des problèmes et à apprendre les meilleures pratiques sans quitter votre flux de travail.

{% alert important %}
<sup>BrazeAITM</sup> Operator est actuellement en version bêta privée avec des fonctionnalités limitées. Pour obtenir de l'aide, contactez votre gestionnaire satisfaction client.
{% endalert %}

## À propos de l'opérateur

Operator est votre assistant d'intelligence artificielle intégré au tableau de bord de Braze. Il vous aide à avancer plus rapidement en répondant à vos questions, en vous suggérant les étapes suivantes et en vous guidant dans l'exécution des tâches, le tout sans quitter votre flux de travail.

Pendant la phase bêta, Operator ne prend en charge que le mode **Demande.**  Vous pouvez le faire :

- Obtenez des réponses de la documentation de Braze
- Résolution des problèmes à l'aide d'un [contexte tenant compte de la page](#page-aware-context)
- Apprenez les meilleures pratiques et les conseils en matière d'onboarding.

## Comment accéder à l'opérateur

Vous pouvez ouvrir Operator à partir de n'importe quelle page du tableau de bord de Braze.  

1. Sélectionnez **Opérateur <sup>BrazeAITM</sup>**, à côté de votre profil utilisateur.

!L'icône de l'opérateur BrazeAI à côté d'un profil utilisateur.]({% image_buster /assets/img/operator/operator_profile.png %}){:style="max-width:60%"}

{: start="2"}
2\. Le panneau de discussion de l'opérateur s'ouvre sur le côté droit de l'écran.

Le panneau de discussion de l'opérateur.]({% image_buster /assets/img/operator/operator_panel.png %})

{% alert tip %}
Essayez de maximiser le panneau pour en faciliter la lecture ou de le minimiser pour que l'opérateur reste disponible pendant que vous continuez à travailler.  
{% endalert %}

## Comment parler à l'opérateur

Utilisez les messages-guides pour communiquer avec l'opérateur. La meilleure approche consiste à parler naturellement, comme vous le feriez avec un collègue ou un ami. Vos invites peuvent aller de simples questions à des demandes complexes :

- **Simple :** Comment puis-je m'assurer que les utilisateurs ne reçoivent pas d'e-mail d'abandon de panier alors qu'ils sont encore sur le site en train de faire des achats ?
- **Complexe :** Comment puis-je faire en sorte que l'étiquette `abort_message` de mon message inclue l'attribut de l'utilisateur qui a provoqué l'interruption ?

L'opérateur peut fournir des instructions étape par étape, des liens vers la documentation de Braze et des explications en langage clair. Plus votre question est claire et précise, plus la réponse sera utile. 

### Meilleures pratiques

Considérez Operator comme une conversation, et non comme un moteur de recherche. Les messages courts et naturels sont généralement les plus efficaces.

- **Soyez précis :** Au lieu de "Parlez-moi de Canvas", essayez plutôt "Comment utiliser les parcours d'action dans Canvas ?  
- **Utilisez les suivis :** Si la première réponse ne correspond pas à ce dont vous avez besoin, posez des questions complémentaires. L'opérateur peut affiner ses réponses.
- **Appuyez-vous sur le contexte :** L'opérateur sait sur quelle page vous vous trouvez dans Braze. Ouvrez Operator lorsque vous êtes sur la page sur laquelle vous travaillez pour obtenir les résultats les plus pertinents.

## Fonctionnalités

L'opérateur inclut les fonctionnalités suivantes pendant la phase bêta :

### Contexte adapté à la page

Operator comprend la page sur laquelle vous travaillez actuellement dans Braze et peut adapter les réponses en fonction de ce contexte. Par exemple, si vous ouvrez Operator pendant que vous créez un Canvas, il peut vous suggérer des étapes ou vous fournir des conseils en rapport avec le Canvas, sans que vous ayez besoin d'expliquer où vous en êtes. 

### Suggestions de textes

Lorsque vous ouvrez Operator, vous verrez quelques suggestions pour vous aider à démarrer. Sélectionnez-en une pour commencer ou tapez votre propre question.

### Visualisation du raisonnement

L'opérateur présente ses étapes de raisonnement dans des sections repliables intitulées **Raisonné**. Sélectionnez le menu déroulant pour développer ces sections et voir comment l'opérateur est parvenu à une réponse.

Le menu déroulant "Raisonné" s'est élargi avec plus de détails sur la façon dont l'opérateur a répondu.]({% image_buster /assets/img/operator/operator_reasoning.png %}){:style="max-width:60%"}

### Actions proposées

Dans certains cas, Operator vous recommandera les prochaines étapes et vous fournira des liens directs vers les pages concernées dans votre tableau de bord de Braze. Par exemple, si vous posez une question sur le taux de rebond des e-mails, Operator peut vous renvoyer à la page de votre **Centre de livrabilité**. Ces raccourcis vous permettent d'agir plus rapidement sans avoir à naviguer manuellement.

### Arrêter la génération

Pendant que l'opérateur génère une réponse, le bouton d'**envoi** devient un bouton d'**arrêt.**  Si vous souhaitez mettre fin à la réponse de manière anticipée, sélectionnez **Arrêter**.

### Effacer l'historique des chats

Pour réinitialiser votre conversation, sélectionnez **Effacer l'historique du chat.** Cette opération supprime le contenu actuel afin que vous puissiez repartir sur de nouvelles bases.

### Maximiser et minimiser le panel

Vous pouvez utiliser le bouton d'**agrandissement** pour développer Operator afin d'en faciliter la lecture, ou le bouton de **réduction** pour garder le panneau rangé pendant que vous continuez à travailler dans Braze.

### Envoi d'un retour d'information

Au bas de chaque réponse, utilisez les boutons "pouce vers le haut" ou "pouce vers le bas" pour fournir un retour d'information rapide. Cela permet d'améliorer les réponses de l'opérateur.

## Résolution des problèmes

| Enjeu | Résolution des problèmes |
| --- | --- |
| Pas de réponse | Essayez d'actualiser la page et de rouvrir le panneau de l'opérateur. |
| Réponses hors sujet | Reformulez votre question de manière plus précise. Mentionnez la fonctionnalité ou le flux de travail sur lequel vous vous interrogez. |
| Messages d'erreur | Si Operator ne peut pas vous envoyer de contenu en continu, il se peut que vous receviez un message "Essayez à nouveau". L'opérateur peut être temporairement indisponible ou votre connexion a été interrompue. Réessayez après quelques minutes. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Limites

Operator est conçu pour vous aider à naviguer dans Braze et à travailler plus efficacement, mais il y a quelques limites actuelles à garder à l'esprit :

### Pas d'accès à vos données

Bien qu'il ait accès au contexte du travail que vous effectuez dans Braze, Operator ne peut pas interroger les données de votre entreprise stockées dans Braze ni renvoyer des réponses à leur sujet. Par exemple, il **ne peut pas** répondre à des demandes telles que :

- "Donnez-moi une liste de toutes mes campagnes d'e-mail de l'année dernière".
- "Montrez-moi quels segments ont eu le plus fort taux d'engagement au cours du dernier trimestre".
- "Analyser les performances de mon Canvas et proposer des améliorations".

### Stabilité bêta

En tant que version bêta privée, Operator peut présenter des erreurs occasionnelles, des interruptions ou des fonctionnalités incomplètes.

Si vous n'êtes pas sûr qu'une question soit prise en charge, essayez de la formuler en expliquant comment l'opérateur peut vous aider à naviguer ou à prendre des mesures dans le tableau de bord de Braze, plutôt que de tirer des analyses ou des données historiques.
