---
nav_title: "Botões de ação"
article_title: Botões de ação
page_order: 1
page_type: reference
description: "Este artigo de referência aborda o que são botões de ação e a diferença entre as plataformas iOS e Android."
channel:
  - Push

---

# Botões de ação

\![Uma notificação push do iOS com dois botões de ação push: Aceitar e recusar.]({% image_buster /assets/img_archive/push_action_example.png %}){: style="float:right;max-width:40%;margin-left:15px;border:none;"}

> Os botões de ação por push permitem que você defina o conteúdo e as ações dos botões ao usar as notificações por push do Braze para iOS e Android. Com os botões de ação, seus usuários podem interagir diretamente com seu aplicativo a partir de uma notificação, sem precisar clicar em uma experiência de aplicativo.

## Criação de botões de ação

Cada botão interativo pode ser vinculado a uma página da Web ou a um deep link ou abrir o aplicativo. 

- Para campanhas push padrão, você pode especificar seus botões de ação push na seção **On-Click Behavior (Comportamento ao clicar** ) do compositor de mensagens push no painel.
- Para [campanhas de envio rápido]({{site.baseurl}}/quick_push), os botões de ação podem ser configurados separadamente para cada plataforma na guia **Settings (Configurações** ).

{% tabs %}
{% tab iOS %}
### iOS {#ios}

Para usar botões de ação em suas mensagens push do iOS, faça o seguinte:

1. Ative os botões de ação na guia **Compose** para uma campanha padrão ou na guia **Settings** para um envio rápido.
2. Selecione sua **categoria de notificação do iOS** entre as seguintes combinações de botões disponíveis:
 - Aceitar / Recusar
 - Sim / Não
 - Confirmar / Cancelar
 - Mais informações
 - Categoria iOS personalizada pré-registrada

\![Menu suspenso Categoria de notificação do iOS.]({% image_buster /assets/img_archive/push_action_buttons_ios.png %}){: style="max-width:70%"}

{% alert note %}
Devido ao manuseio de botões pelo iOS, você precisa executar etapas adicionais de integração ao configurar botões de ação, que estão descritas em nossa [documentação para desenvolvedores]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift#swift_customizing-push-categories). Em particular, você precisa configurar as categorias do iOS ou selecionar determinadas opções de botão padrão. Para integrações com Android, esses botões funcionarão automaticamente.
{% endalert %}
{% endtab %}
{% tab Android %}
### Android {#android}

Para usar botões de ação em suas mensagens push do Android, faça o seguinte:

1. Ative os botões de ação na guia **Compose** para uma campanha padrão ou na guia **Settings** para um envio rápido.
2. Selecione <i class="fas fa-plus-circle"></i> **Add Button** e especifique o texto do botão e **o On-Click Behavior**. Você pode selecionar entre as seguintes ações disponíveis:
  - Abrir aplicativo
  - Redirecionar para URL da Web
  - [Deep Link]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) para o aplicativo

\![Selecionando "Abrir aplicativo" como o comportamento ao clicar em um botão de notificação.]({% image_buster /assets/img_archive/push_action_buttons_android.png %}){: style="max-width:70%"}

Você pode adicionar até três botões em seu push.

#### Limites de caracteres do Android

Ao contrário dos botões do iOS, que são empilhados, os botões do Android são exibidos lado a lado em uma linha. Isso significa que quanto mais botões você adicionar (até três), menos espaço terá para a cópia do botão. 

\![Botões de ação do Android com texto truncado.]({% image_buster /assets/img_archive/push_action_truncated.png %}){: style="max-width:50%"}

A tabela a seguir descreve quantos caracteres você pode adicionar antes que a cópia do botão seja truncada, dependendo de quantos botões você tem:

| Número de botões | Máximo de caracteres por botão |
| --- | --- |
| 1 | 46 caracteres |
| 2 | 20 caracteres |
| 3 | 11 caracteres |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endtab %}
{% endtabs %}

