---
nav_title: Integração de Beacon
article_title: Integração de Beacon para Android e FireOS
platform: 
  - Android
  - FireOS
page_order: 2
description: "Este artigo de referência cobre como registrar eventos personalizados usando Gimbal Beacons para Android ou FireOS."

---

# Integração de Beacon

> Este artigo irá guiá-lo sobre como integrar tipos específicos de beacons com a Braze para permitir a segmentação e o envio de mensagens.

## Gimbal Beacons

Depois de configurar e integrar seus Gimbal Beacons no seu app, você pode registrar eventos personalizados para coisas como o início ou o fim de uma visita, ou a visualização de um beacon. Você também pode registrar propriedades para esses eventos, como o nome do local ou o tempo de permanência.

Para registrar um evento personalizado quando um usuário entra em um lugar, inclua este código no método `onVisitStart`:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace());
Braze.getInstance(context).requestImmediateDataFlush();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace())
Braze.getInstance(context).requestImmediateDataFlush()
```

{% endtab %}
{% endtabs %}

O `requestImmediateDataFlush` verifica se o seu evento será registrado mesmo se o app estiver em segundo plano, e o mesmo processo pode ser implementado para sair de um local. Nota que a atividade e o contexto em que você está trabalhando podem mudar exatamente como você integra as linhas `logCustomEvent` e `requestImmediateDataFlush`. Além disso, este código criará e incrementará um evento personalizado exclusivo para cada novo lugar que o usuário entrar. Portanto, se você prevê a criação de mais de 50 lugares, recomendamos criar um evento personalizado genérico “Place Entered” (Lugar em que entrou) e incluir o nome do lugar como uma propriedade do evento.
