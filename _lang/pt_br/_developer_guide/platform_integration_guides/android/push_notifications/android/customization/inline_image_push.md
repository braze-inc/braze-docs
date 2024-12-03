---
nav_title: Push de imagem em linha
article_title: Push de imagem inline para Android
platform: Android
page_order: 5.9
description: "Este artigo de referência aborda como implementar um push de imagem inline em seu aplicativo Android."
channel:
  - push

---

# Push de imagem em linha

![]({% image_buster /assets/img/android/push/inline_image_push_android_1.png %}){: style="float:right;max-width:30%;margin-left:15px;border: 0;"}

> Exiba uma imagem maior em sua notificação por push do Android usando o push de imagem em linha. Com esse design, os usuários não precisarão expandir manualmente o push para ampliar a imagem. 

Não é necessária nenhuma integração adicional ou alterações no SDK para usar esse recurso. Em vez disso, os dispositivos ou SDKs que não atenderem aos requisitos mínimos de versão mostrarão uma notificação por push de imagem grande padrão.

## Requisitos de uso

- Esse tipo de notificação requer o SDK da Braze para Android v10.0.0+ e dispositivos Android M+. 
- Dispositivos ou SDKs sem suporte voltarão a usar a notificação por push de imagem grande padrão.
- Ao contrário das notificações por push normais do Android, as imagens inline por push têm uma proporção de 3:2.

{% alert note %}
Os dispositivos que executam o Android 12 serão renderizados de forma diferente devido a alterações nos estilos de notificação por push personalizados.
{% endalert %}

## Configuração do dashboard

Ao criar uma mensagem push para Android, esse recurso está disponível no menu suspenso **Notification Type (Tipo de notificação** ).

![O editor de campanhas push mostra o local do menu suspenso "Notification Type" (acima da prévia padrão do push).]({% image_buster /assets/img/android/push/android_inline_image_notification_type.png %})
