---
nav_title: WSC Sports
article_title: WSC Sports
description: "Cet article de référence décrit le partenariat entre Braze et WSC Sports, une plateforme de vidéos sportives qui vous permet d'inclure des médias sportifs riches et robustes dans vos notifications push Braze."
alias: /partners/wsc_sports/
page_type: partner
search_tag: Partner

---

# WSC Sports

> La plateforme [WSC Sports](https://wsc-sports.com/) génère des vidéos sportives personnalisées pour chaque plateforme numérique et chaque fan de sport, automatiquement et en temps réel. 

_Cette intégration est maintenue par le CSM Sports._

## À propos de l'intégration

L'intégration de Braze et WSC Sports vous permet d'inclure des médias sportifs riches et robustes dans vos notifications push Braze. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| compte WSC | Un compte WSC est nécessaire pour bénéficier de ce partenariat. |
| Clé d'API REST Braze | Une clé API REST de Braze avec des autorisations pour les **messages**, les **segments**, les **campagnes** et les **canvas**. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

L'application WSC Sports gère le processus de bout en bout, de la sélection de la vidéo à l'arrivée de la notification push sur l'appareil de l'utilisateur final. 

### Étape 1 : Sélectionnez les paramètres d'envoi

![]({% image_buster /assets/img/wsc_sports/braze_integration.jpg %} "braze_integration.jpg"){: style="float:right;max-width:25%;margin-bottom:15px;"}

Avant de commencer l'intégration, assurez-vous que la campagne et les segments d'utilisateurs souhaités sont intégrés à Braze. Lorsque vous avez terminé, sur la plateforme WSC Sports, sélectionnez la vidéo de votre choix, puis dans les paramètres d'envoi, sélectionnez le segment utilisateur Braze et l'ID de campagne que vous souhaitez utiliser. Enfin, choisissez l'heure à laquelle vous souhaitez que votre message push soit envoyé. 

#### Appel d'API

Une fois envoyée, WSC Sports enverra la notification push aux segments d'utilisateurs sélectionnés, en utilisant les points de terminaison Braze suivants, en fonction des options sélectionnées :
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

### Étape 2 : Envoyer un test

À ce stade, votre campagne devrait être prête à être testée et envoyée. Consultez les journaux des messages d'erreur de Braze si vous rencontrez des erreurs. 


