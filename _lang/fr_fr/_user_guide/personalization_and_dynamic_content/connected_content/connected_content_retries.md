---
nav_title: Nouvelles tentatives de contenu connecté
article_title: Nouvelles tentatives de contenu connecté
page_order: 5
description: "Cet article de référence explique comment gérer les tentatives de contenu connecté."

---

# 

> Cette page explique comment ajouter des tentatives à vos appels de contenu connecté.

##  

 Dans ce cas, Braze prend en charge la logique de nouvelle tentative pour tenter de nouveau la demande à l’aide d’un délai exponentiel.

{% alert note %}
Contenu connecté `:retry` n’est pas disponible pour les messages dans l’application.
{% endalert %}

## 




```
{% connected_content https://yourwebsite.com/api/endpoint :retry %}
{% connected_content https://www.braze.com :save my_content :basic_auth auth_name :retry %}
```
{% endraw %}



### Résultats des tentatives

#### Lorsqu'une nouvelle tentative réussit



#### Lorsque l'appel API échoue et que les tentatives sont activées

 Le braze déplace les messages défaillants vers l’arrière de la file d’attente et ajoute des minutes supplémentaires, si nécessaire, au nombre total de minutes qu’il faudrait pour envoyer votre message.

