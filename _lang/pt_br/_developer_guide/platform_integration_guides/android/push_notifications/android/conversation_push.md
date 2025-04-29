---
nav_title: Push de conversa
article_title: Push de Conversa para Android
platform: Android
page_order: 5.92
description: "Este artigo aborda como implementar um push de conversa android em seu app para Android."
channel:
  - push

---

# push de conversa

> Este artigo aborda como implementar um push de conversa android em seu app para Android.

![]({% image_buster /assets/img/android/push/conversations_android.png %}){: style="float:right;max-width:35%;margin-left:15px;border: 0;"}

A [iniciativa de pessoas e conversas](https://developer.android.com/guide/topics/ui/conversations) existe há vários anos no Android e tem como objetivo destacar pessoas e conversas na superfície do sistema do smartphone. Esta prioridade é baseada no fato de que a comunicação e a interação com outras pessoas ainda são a área funcional mais valorizada e importante para a maioria dos usuários de Android em todas as faixas demográficas.

Não é necessária nenhuma integração adicional ou alterações no SDK para usar esse recurso. Em vez disso, os dispositivos ou SDKs que não atenderem aos requisitos mínimos de versão mostrarão uma notificação por push padrão.

## Requisitos de uso

- Esse tipo de notificação requer o SDK da Braze para Android v15.0.0+ e dispositivos Android 11+. 
- Dispositivos ou SDKs sem suporte voltarão a usar uma notificação por push padrão.

Este recurso está disponível apenas na API REST da Braze. Consulte o [objeto push do Android]({{site.baseurl}}/api/objects_filters/messaging/android_object#android-conversation-push-object) para saber mais.

