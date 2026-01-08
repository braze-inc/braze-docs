---
nav_title: eduMe
article_title: eduMe
description: "Cet article de référence présente le partenariat entre Braze et eduMe, un outil de formation mobile qui vous permet de tirer parti du contenu connecté de Braze pour donner à vos utilisateurs un accès aux cours et leçons d'eduMe dans vos campagnes Braze."
alias: /partners/edume/
page_type: partner
search_tag: Partner

---

# eduMe

> [eduMe](https://edume.com) est un outil de formation pour appareils mobiles qui fournit à tout moment et en tout lieu à votre personnel les connaissances dont il a besoin pour réussir. 

_Cette intégration est maintenue par Edume._

## À propos de l'intégration

L'intégration de Braze et eduMe s'appuie sur le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) de Braze pour permettre à vos utilisateurs d'accéder aux cours et leçons d'eduMe dans vos campagnes Braze. Les progrès individuels et collectifs peuvent ensuite être suivis grâce à la fonctionnalité de reporting d'eduMe.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Edume | Un compte eduMe est nécessaire pour bénéficier de ce partenariat. |
| Clé API eduMe | Vous devez demander une clé API à votre contact de satisfaction client eduMe. Cette clé sera utilisée lors de votre appel au contenu connecté de Braze. |
| Secret de signature du lien Edume | Vous devez demander à votre contact de satisfaction client chez eduMe de mettre en place un secret de signature de lien pour votre entreprise. Ce secret est utilisé pour activer les liens fluides/sans heurts dans le contenu connecté. Vous n'aurez rien à faire avec ce secret. |
| ID de groupe et de contenu eduMe | Ces identifiants sont nécessaires pour configurer vos appels au contenu connecté. Contactez votre service client eduMe pour obtenir ces identifiants. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Créez votre appel à contenu connecté

Pour donner à un utilisateur l'accès à un cours, une leçon ou une enquête eNPS, et pour suivre ses progrès par rapport à votre ID utilisateur interne dans Edume, suivez l'appel API présenté dans cet exemple :

{% raw %}
```
Welcome to my Rickshaw App platform.
Access your onboarding course at:

{% connected_content
  https://connect.edume.com/
  EDUME-CONTENT-LINK-AND-CONTENT-ID&groupId=5681&externalUserId={{${driver_id}}}
  :headers {
       "x-api-key": "YOUR-EDUME-API-KEY"
  }
%}
```
{% endraw %}

1. Remplacez `YOUR-EDUME-API-KEY` par votre clé API Edume.<br><br>
2. Remplacez le site `EDUME-CONTENT-LINK-AND-CONTENT-ID` par la chaîne de caractères du contenu et l'identifiant du module, de la leçon ou de l'enquête correspondants. Ces identifiants se trouvent dans votre compte eduMe.
  - Cours : `getCourseLink?moduleId=12087`
  - Leçon : `getLessonLink?lessonId=25805`
  - Enquête eNPS : `getSurveyLink?surveyId=654`<br><br>
3. Les utilisateurs qui arrivent sur eduMe par ce lien seront ajoutés à une équipe ou à un groupe eduMe de votre choix. Remplacez `groupId` par l'ID de l'équipe ou du groupe Edume concerné. Vous utiliserez généralement l'ID de l'équipe, sauf pour les cours nécessitant une inscription, auquel cas vous devrez utiliser l'ID du groupe.<br><br>
4. Inclure un champ approprié pour mapper le champ `externalUserId`. L'exemple d'appel de contenu connecté utilise l’ID `driver_id`, mais votre champ sera probablement différent. Cet ID sera disponible dans les rapports eduMe, ce qui vous permettra d'établir une corrélation avec vos systèmes.<br><br>
5. Enfin, personnalisez et testez votre message si nécessaire. Nous vous recommandons d'envoyer au moins un message de test, d'accéder au contenu eduMe, de terminer la leçon ou le cours et de vérifier que les analyses eduMe sont bien enregistrées. 

