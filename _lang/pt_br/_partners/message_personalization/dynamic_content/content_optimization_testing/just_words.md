---
nav_title: Apenas palavras
article_title: Apenas palavras
description: "Este artigo de referência descreve a parceria entre o Braze e a Just Words, uma plataforma de negócios SaaS baseada em IA que cria versões personalizadas de campanhas existentes e otimiza linhas de assunto, conteúdo criativo e layouts de e-mail em HTML ao longo do tempo."
alias: /partners/just_words/
page_type: partner
---

# Guia de integração do Just Words

> [O Just Words](https://www.justwords.ai/) hiperpersonaliza o envio de mensagens em escala nos canais de envio de mensagens do ciclo de vida, permitindo que você teste dinamicamente centenas de variações e atualize automaticamente o conteúdo com baixo desempenho.

Quando você usar o Just Words com o Braze [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) para personalizar suas campanhas e canvas Braze existentes, o Just Words usará o Braze Currents para otimizar o conteúdo dinamicamente - para que você não precise fazer isso.

## Quais são os benefícios?

Depois que sua integração estiver concluída, você poderá aproveitar a plataforma Just Works para:

- Veja os resultados dos experimentos em tempo real
- Editar dinamicamente a cópia
- Ver insights de performance

{% alert note %}
Dúvidas? Entre em contato com a Just Words na [página de reservas](https://www.justwords.ai/book-demo) ou pelo canal compartilhado do Slack.
{% endalert %}

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta Just Words | É necessário ter uma conta [do Just Words](https://www.justwords.ai/) para aproveitar essa parceria. Se você não tiver uma conta do Just Words, agende [uma chamada de integração de 30 minutos](https://www.justwords.ai/book-demo). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração do Just Words com o Braze

### Etapa 1: Criar um modelo do Just Words

1. Acesse o console do Just Words e [crie um novo modelo](https://console.justwords.ai/new).
2. Escolha uma ID fácil de lembrar que use apenas letras, números e sublinhados.
3. Preencha os detalhes básicos da campanha.
4. Use IA para gerar variações personalizadas.

![A plataforma de criação de modelos do Just Words.]({% image_buster /assets/img/just_words/creation_interface.png %}){: style="max-width:80%;"}

### Etapa 2: Criar uma chave de API do Just Words

1. Acesse **Configurações da organização** > **Chaves de API** > **Gerar chave de API**.
2. Copie e salve a chave de API em um local seguro.

![Formulário da chave de API do Just Words.]({% image_buster /assets/img/just_words/api_key_form.png %}){: style="max-width:80%;"}

### Etapa 3: Use Just Words em seu conteúdo do Braze

O Just Words trabalha com Canvas e campanhas usando o Connected Content. Se estiver criando um Canva, cada etapa do e-mail deve corresponder a um modelo exclusivo do Just Words.

#### Etapa 3.1: Configure seu teste A/B

{% tabs %}
{% tab Canvas %}

1. Em uma tela, selecione **Adicionar variante** > **Adicionar variante** até obter o número desejado de variantes e adicione etapas a cada variante (como uma etapa de envio de e-mail).
2. Divida o tráfego do público conforme desejado. Por exemplo, se você tiver duas variantes, poderá dar 50% a cada uma delas. Ou, você poderia ter duas variantes com 40% cada e um grupo de controle com 20%. Para saber mais sobre testes A/B para Canvas, consulte [Criar um Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).
3. Nos criadores das etapas da mensagem que você deseja usar com o Connected Content, cole o snippet do Connected Content do Just Words Console, como o snippet a seguir.

{% raw %}
```liquid
{% connected_content https://worker.justwords.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

![Configuração do Testes A/B do Braze.]({% image_buster /assets/img/just_words/braze_canvas.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Campaign %}

1. Na etapa **Criador de mensagens** de sua campanha, crie duas variantes.
2. Na etapa **Público-alvo**, acesse a seção **Testes A/B** e modifique as porcentagens de usuários que receberão cada uma de suas variantes (e seu grupo de controle opcional). Você pode personalizar ainda mais seu teste selecionando uma opção de otimização. Para saber mais sobre testes A/B para campanhas, consulte [Criação de testes multivariantes e A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/).
3. No criador de mensagens, cole o snippet Connected Content do Just Words Console, como o snippet a seguir.

{% raw %}
```liquid
{% connected_content https://worker.justwords.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

{% endtab %}
{% endtabs %}

#### Etapa 3.2:  Adicione personalização com atributos personalizados (opcional)

Para personalizar suas mensagens com atributos personalizados (como `industry`), use o seguinte formato Liquid:

{% raw %}
```liquid
{% connected_content https://worker.justwords.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}&attrs.industry={{ custom_attribute.industry }}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

Note que o atributo personalizado de `industry` é indicado por {% raw %}```&attrs.industry={{ custom_attribute.industry }}```{% endraw %}. 

![Lógica Braze Liquid em um criador de mensagens HTML.]({% image_buster /assets/img/just_words/just_words_personalization.png %}){: style="max-width:80%;"}

### Etapa 4: Pré-visualização do e-mail

Certifique-se de fazer uma prévia do e-mail no Braze para confirmar se o conteúdo personalizado está sendo renderizado corretamente.

![Prévia da mensagem do Braze para um e-mail do Just Words.]({% image_buster /assets/img/just_words/just_words_preview.png %}){: style="max-width:80%;"}

### Etapa 5: Configurar Braze Currents

O Braze Currents ativa o rastreamento e a otimização da performance ao longo do tempo.

1. No Braze, acesse **Integrações de Parceiros** > **Exportação de Dados**.
2. Selecione **Criar novo teste atual** e, em seguida, selecione **Testar exportação de dados do Amazon S3**.

![Menu suspenso "Create New Test Current" (Criar novo teste atual) com a opção "Test Amazon S3 Data Export" (Testar exportação de dados do Amazon S3).]({% image_buster /assets/img/just_words/test_amazon_s3.png %}){: style="max-width:80%;"}

{: start="3" }
3\. Digite o ID de acesso S3, a chave de acesso secreto da AWS, o nome do bucket e a pasta que foram fornecidos pela Just Words durante a integração.

![Seção "Credentials" para a chave de acesso secreta da AWS.]({% image_buster /assets/img/just_words/aws_secret_access_key.png %}){: style="max-width:80%;"}

{: start="4" }
4\. Selecione os eventos a serem rastreados, como envios, aberturas, cliques, cancelamentos de inscrição, conversões e outros.

![Seção "Message Engagement Events" (Eventos de engajamento com mensagens) com eventos a serem selecionados.]({% image_buster /assets/img/just_words/message_engagement_events.png %}){: style="max-width:80%;"}

{: start="5" }
5\. Inicie o Braze Currents.

Está tudo pronto! Agora você pode usar o Just Words com o Braze Connected Content.