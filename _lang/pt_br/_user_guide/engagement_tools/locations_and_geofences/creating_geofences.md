---
nav_title: Criando geofences
article_title: Criando geofences
page_order: 1
page_type: reference
toc_headers: h2
description: "Este artigo de referência aborda o que são geofences e como criar e configurar eventos de geofence."
tool: 
  - Location
search_rank: 9
---

# Geofences

> No centro de nossa oferta de local em tempo real está o conceito de geofence. Uma geofence é uma área geográfica virtual, representada como latitude e longitude combinadas com um raio, formando um círculo em torno de uma posição global específica. As geofences podem variar do tamanho de um prédio até o tamanho de uma cidade inteira.

## 

 Os usuários que entram ou saem de suas geofences adicionam uma nova camada de dados de usuários que podem ser usados para segmentação e direcionamento.

As geofences são organizadas em conjuntos de geofences - um grupo de geofences que pode ser usado para segmentar ou engajar usuários em toda a plataforma. Cada conjunto de geofences pode conter um máximo de 10.000 geofences.



- Os apps para Android só podem armazenar até 100 geofences locais de cada vez. A Braze está configurado para armazenar apenas até 20 geofences localmente por app.
- Os dispositivos iOS podem monitorar até 20 geofences ao mesmo tempo por app. A Braze monitorará até 20 locais se houver espaço disponível. 
- 
- Para que as geofences funcionem corretamente, você deve garantir que seu app não esteja usando todos os pontos de geofence disponíveis.



|  |  |
|---|---|
|  |  |
|  |   |
|  |    |


## 

###  



1. 
2. 
3. 
4. 

###  



1.  
2. 
3. 


Recomendamos a criação de geofences com um raio de pelo menos 200 metros para otimizar a funcionalidade. 




## 

As geofences podem ser feitas upload em massa como um objeto GeoJSON do tipo `FeatureCollection`.   





- 
- 

### 



```
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-73.992473, 40.755669]
      },
      "properties": {
        "radius": 200,
        "name": "Braze HQ"
      }
    },
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-74.044468, 40.689225]
       },
      "properties": {
        "radius": 100,
        "name": "Statue of Liberty"
      }
    }
  ]
}
```

## Uso de eventos de geofence



### 

Para usar os dados de geofence como parte dos disparos da campanha e do canva, escolha **Entrega baseada em ação** para o método de entrega. Em seguida, adicione uma ação-gatilho de `Trigger a Geofence`. Por fim, escolha o conjunto de geofences e os tipos de eventos de transição de geofences para sua mensagem. Também é possível avançar os usuários em um Canva usando eventos de geofence.



### 

Para usar dados de geofence para personalizar uma mensagem, você pode usar a seguinte sintaxe de personalização do Liquid:

{% raw %}
* `{{event_properties.${geofence_name}}}`
* `{{event_properties.${geofence_set_name}}}`
{% endraw %}

## Atualização de conjuntos de geofences

Para usuários ativos, o SDK da Braze solicitará geofences apenas uma vez por dia no início da sessão. Isso significa que, se forem feitas alterações nos conjuntos de geofences após o início da sessão, você precisará aguardar 24 horas a partir do momento em que os conjuntos forem baixados pela primeira vez para receber o conjunto atualizado.

{% alert note %}
Se as geofences não forem carregadas localmente no dispositivo, o usuário não poderá disparar a geofence mesmo que entre na área.
{% endalert %}

## 

### 

 

1. 
2. 
3. 


 








## Perguntas frequentes

### 

   

  

### 

 

  



### 



### 

  

 

### 

  

### 



