---
nav_title: "botões de ação por push"
article_title: botões de ação por push
page_order: 1
page_type: reference
description: "Este artigo de referência cobre o que são botões de ação por push e a diferença entre as plataformas iOS e Android."
channel:
  - Push

---

# botões de ação por push

![Uma notificação por push do iOS com dois botões de ação por push: Aceitar e recusar.]({% image_buster /assets/img_archive/push_action_example.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> botões de ação por push permitem que você defina conteúdo e ações para botões ao usar notificações por push do Braze iOS e Android. Com botões de ação, seus usuários podem interagir diretamente com seu app a partir de uma notificação sem precisar clicar em uma experiência de app.

## Criando botões de ação

Cada botão interativo pode vincular a uma página da web ou a um deep link ou abrir o app. 

- Para campanhas de mensagens padrão, é possível especificar seus botões de ação por push na seção **Comportamento ao clicar** do criador de mensagens por push no dashboard.
- Para [campanhas de push rápido]({{site.baseurl}}/quick_push), os botões de ação podem ser configurados separadamente para cada plataforma na guia **Settings (Configurações** ).

{% tabs %}
{% tab iOS %}
### iOS {#ios}

Para usar botões de ação em suas mensagens push do iOS, faça o seguinte:

1. Ative os botões de ação na guia **Compose** para uma campanha padrão ou na guia **Settings** para um push rápido.
2. Selecione sua **Categoria de Notificação do iOS** a partir das seguintes combinações de botões disponíveis:
 - Aceitar/recusar
 - Sim/Não
 - Confirmar/cancelar
 - Mais
 - Categoria iOS personalizada pré-registrada

![Menu suspenso de Categoria de notificação do iOS.]({% image_buster /assets/img_archive/push_action_buttons_ios.png %}){: style="max-width:70%"}

{% alert note %}
Devido ao manuseio de botões pelo iOS, você precisa realizar etapas adicionais de integração ao configurar botões de ação por push, que estão descritas em nossa [documentação para desenvolvedores]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories). Em particular, você precisa configurar Categorias do iOS ou selecionar entre certas opções de botões padrão. Para integrações com Android, esses botões funcionarão automaticamente.
{% endalert %}
{% endtab %}
{% tab Android %}
### Android {#android}

Para usar botões de ação em suas mensagens push do Android, faça o seguinte:

1. Ative os botões de ação na guia **Compose** para uma campanha padrão ou na guia **Settings** para um push rápido.
2. Selecione <i class="fas fa-plus-circle"></i> **Add Button** e especifique o texto do botão e **o comportamento ao clicar**. Você pode selecionar entre as seguintes ações disponíveis:
  - Abrir app
  - Redirecionar para URL da web
  - [deep link]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) no aplicativo

![Seleção de "Abrir aplicativo" como o comportamento ao clicar em um botão de notificação.]({% image_buster /assets/img_archive/push_action_buttons_android.png %}){: style="max-width:70%"}

Você pode adicionar até três botões no seu push.

#### Limites de caracteres do Android

Ao contrário dos botões do iOS, que são empilhados, os botões do Android são exibidos lado a lado em uma linha. Isso significa que quanto mais botões você adicionar (até três), menos espaço você terá para o texto do botão. 

![botões de ação por push do Android com texto truncado.]({% image_buster /assets/img_archive/push_action_truncated.png %}){: style="max-width:50%"}

A tabela a seguir descreve quantos caracteres você pode adicionar antes que a cópia do seu botão seja truncada, dependendo de quantos botões você tem:

| Número de Botões | Máximo de caracteres por botão |
| --- | --- |
| 1 | 46 caracteres |
| 2 | 20 caracteres |
| 3 | 11 caracteres |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

