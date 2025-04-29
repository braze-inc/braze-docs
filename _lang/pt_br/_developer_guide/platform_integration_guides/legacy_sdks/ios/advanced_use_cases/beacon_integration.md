---
nav_title: Integração de beacons
article_title: Integração de beacon para iOS
platform: iOS
page_order: 4
description: "Este artigo aborda o registro de eventos personalizados usando Gimbal Beacons para iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integração de beacons

Aqui, veremos como integrar tipos específicos de beacons ao Braze para permitir a segmentação e o envio de mensagens.

## Gimbal Beacons

Depois de configurar os Gimbal Beacons e integrá-los ao seu app, é possível registrar eventos personalizados, como o início ou o fim de uma visita ou o avistamento de um beacon. Também é possível registrar propriedades para esses eventos, como o nome do local ou o tempo de permanência.

Para registrar um evento personalizado quando um usuário entrar em um local, insira este código no método `didBeginVisit`:

{% tabs %}
{% tab OBJECTIVE C %}

```objc
[[Appboy sharedInstance] logCustomEvent:@"Entered %@", visit.place.name];
[[Appboy sharedInstance] flushDataAndProcessRequestQueue];
```

{% endtab %}
{% tab swift %}

```swift
Appboy.sharedInstance()?.logCustomEvent("Entered %@", visit.place.name)
Appboy.sharedInstance()?.flushDataAndProcessRequestQueue()
```

{% endtab %}
{% endtabs %}

O site `flushDataAndProcessRequestQueue` confirma que seu evento será registrado mesmo que o app esteja em segundo plano, e o mesmo processo pode ser implementado para sair de um local. Note que isso criará e incrementará um evento personalizado exclusivo para cada novo local em que o usuário entrar. Se você prevê a criação de mais de 50 lugares, recomendamos que crie um evento personalizado genérico "Place Entered" (Lugar inserido) e inclua o nome do lugar como uma propriedade do evento.
