---
nav_title: Configurações de TTL do push
article_title: Configurações de TTL do push
page_order: 16
page_type: reference
description: "Este artigo de referência aborda a página de configurações do Push Time to Live no dashboard da Braze."
channel: push

---

# Configurações push TTL

> Saiba mais sobre a página de configurações do Push Time-to-Live no dashboard do Braze.

A página **TTL (Push Time-To-Live) ativa** o controle da duração da tentativa de entrega para dispositivos off-line. Isso significa que, se o dispositivo de um usuário estiver off-line quando sua campanha for enviada, o Braze tentará entregar a mensagem até o horário definido.

{% alert note %}
Se estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), poderá encontrar essa página em **Configuraões** > **Gerenciar configurações** > **Configurações de Push TTL**.
{% endalert %}

Esse recurso não removerá uma notificação se ela já tiver sido recebida pelo dispositivo do usuário - ele apenas controlará por quanto tempo o provedor de push tentará entregar uma notificação.

![Guia de configurações de Push TTL no menu de Configurações][1]

{% alert tip %}
Lembre-se de clicar em **Salvar** antes de sair da página!
{% endalert %}

[1]: {% image_buster /assets/img/push_ttl.png %}
