---
nav_title: WSC Sports
article_title: WSC Sports
description: "Cet article de référence présente le partenariat entre Braze et WSC Sports, une plateforme de vidéos sportives qui vous permet d’inclure des médias sportifs riches et attrayants dans vos notifications push de Braze."
alias: /partners/wsc_sports/
page_type: partner
search_tag: Partenaire

---

# WSC Sports

> La plateforme [WSC Sports][1] génère des vidéos sportives personnalisées pour chaque plateforme numérique et chaque fan de sport, automatiquement et en temps réel. 

L’intégration de Braze et WSC Sports vous permet d’inclure des médias sportifs riches et attrayants dans vos notifications push de Braze. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte WSC | Un compte WSC est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

L’application WSC Sports gère le processus de bout en bout, de la sélection de la vidéo à l’arrivée de la notification push sur l’appareil de l’utilisateur final. 

### Étape 1 : Sélectionner les paramètres d’envoi

![][2]{: style="float:right;max-width:25%;margin-bottom:15px;"}

Avant de commencer l’intégration, assurez-vous que vous avez la campagne et les segments d’utilisateur souhaités construits dans Braze. Une fois terminé, dans la plateforme WSC Sports, sélectionnez la vidéo de votre choix, et dans les paramètres d’envoi, sélectionnez le segment d’utilisateur Braze et l’ID de campagne que vous souhaitez utiliser. Enfin, choisissez l’heure à laquelle vous souhaitez envoyer votre notification push. 

#### Appel API

Une fois l’envoi effectué, WSC Sports délivre la notification push aux segments d’utilisateurs choisis, en utilisant les endpoints Braze suivants, en fonction des options sélectionnées :
- [/messages/schedule/create]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages#create-scheduled-messages)
- [/messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#sending-messages-immediately-via-api-only)

Le corps du message qui en résulte est le suivant : 
```
{
  "apple_push": {
    "alert": {
      "body": "Push Message Title"
    },
    "asset_url": "internalURI.mp4",
    "asset_file_type": "mp4"
  }
}
```

### Étape 2 : Envoi de test

À ce stade, votre campagne doit être prête à être testée et envoyée. Vérifiez les journaux des messages d’erreur de Braze si vous rencontrez des erreurs. 

[1]: https://wsc-sports.com/
[2]: {% image_buster /assets/img/wsc_sports/braze_integration.jpg %} "braze_integration.jpg"