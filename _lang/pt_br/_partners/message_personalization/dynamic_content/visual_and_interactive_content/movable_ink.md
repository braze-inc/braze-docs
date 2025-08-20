---
title: "Movable Ink"
article_title: Movable Ink
alias: "/partners/movable_ink/"
description: "Este artigo de referência descreve a parceria entre a Braze e a Movable Ink, uma plataforma de software baseada em nuvem que oferece aos profissionais de marketing digital uma maneira de criar experiências visuais atraentes, exclusivas e cativantes para os clientes."
page_type: partner
search_tag: Partner

---

# Movable Ink

> [A Movable Ink](https://www.movableink.com/) é uma plataforma de software baseada em nuvem que oferece aos profissionais de marketing digital uma maneira de criar experiências visuais atraentes, exclusivas e cativantes para os clientes. A plataforma da Movable Ink oferece opções de personalização valiosas que podem ser facilmente inseridas nas suas campanhas. 

_Essa integração é mantida pela Movable Ink._

## Sobre a integração

Expanda seus recursos criativos aproveitando os recursos do Intelligent Creative da Movable Ink, como enquetes, contagem regressiva e raspadinha. A integração entre a Movable Ink e a Braze oferece uma abordagem mais completa para mensagens dinâmicas orientadas por dados, fornecendo aos usuários elementos em tempo real sobre as coisas que importam.

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta da Movable Ink | É necessário ter uma conta da Movable Ink para usar a parceria. |
| Fonte de dados | Você precisará conectar uma fonte de dados à Movable Ink. Isso pode ser feito por CSV, importação do site ou API. Passe os dados com um identificador unificador entre a Braze e a Movable Ink (por exemplo, `external_id`).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

- Retrospectivas mensais ou de fim de ano personalizadas
- Personalize dinamicamente as imagens para envio de e-mail, push ou notificações Rich com base no último comportamento conhecido.<br>
	Por exemplo: 
	- Usar uma mensagem push Rich para criar dinamicamente um cronograma de eventos por extração de dados da API. 
	- Usar a contagem regressiva para notificar os usuários quando um grande período de vendas estiver prestes a começar (por exemplo, Black Friday, Dia dos Namorados ou ofertas de feriados)
	- Usar a raspadinha como uma forma divertida e interativa de distribuir códigos de promoção.

## Funcionalidades suportadas da Movable Ink

O Intelligent Creative tem muitas ofertas das quais os usuários da Braze podem tirar proveito. A lista a seguir mostra quais funcionalidades são compatíveis. 

| Funcionalidade da Movable Ink | Recurso | Notificações de Rich push | Mensagens no app / Cartões de conteúdo / E-mail | Informações |
| ---------------------- |---| ---------------------- | -------------------------------- | ------- |
| Otimizador criativo | Exibir conteúdo A/B | ✗ | ✔ | |
|| Otimizar | ✗ | ✔* | \* Requer a solução de deep linking da Branch |
| Regras de direcionamento | Data | ✔* | ✔ | \* Suportada, mas não recomendada porque as notificações por push são armazenadas em cache após o recebimento e não são atualizadas. |
|| Dia da semana | ✔* | ✔ | \* Suportada, mas não recomendada porque as notificações por push são armazenadas em cache após o recebimento e não são atualizadas. |
|| Hora do dia | ✔* | ✔ | \* Suportada, mas não recomendada porque as notificações por push são armazenadas em cache após o recebimento e não são atualizadas. |
| Histórias ou atividade de comportamento | | ✔* | ✔* | \* O identificador de usuário exclusivo usado para a Braze precisa estar vinculado ao identificador do seu provedor de serviços de e-mail |
| Deep linking no app | | ✔* | ✔* | \* Para proporcionar uma experiência simplificada aos seus clientes, use uma solução de deep linking estabelecida via Branch ou uma solução validada com a equipe de experiência do cliente da Movable Ink. |
| Apps | Contagem regressiva | ✔* | ✔ | \* Suportada, mas não recomendada porque as notificações por push são armazenadas em cache após o recebimento e não são atualizadas. |
|| Enquete | ✗ | ✔* | \* Após a votação, o usuário sai do app e acessa uma landing page móvel |
|| Raspadinha | ✔* | ✔* | \* Ao clicar, o usuário sai do app e acessa a experiência da raspadinha |
|| Vídeo | ✔* | ✔* | \* Apenas GIFs animados. <br>Para Android, o Braze requer [suporte a GIFs]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs/) na implementação |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integração

### Etapa 1: crie uma fonte de dados para a Movable Ink

Os clientes precisarão criar uma fonte de dados que pode ser um CSV, uma importação de site ou uma integração de API.

![Diferentes opções de fonte de dados que serão exibidas: upload de CSV, site ou integração de API.]({% image_buster /assets/img/movable_ink/movable_ink1.png %})

{% tabs local %}
{% tab Fonte de dados CSV %}
- **Fonte de dados CSV**: Cada linha deve ter pelo menos uma coluna de segmento e uma coluna de conteúdo. Após o upload do seu CSV, selecione quais colunas devem ser usadas para direcionamento do conteúdo. [Exemplo de arquivo CSV]({% image_buster /assets/download_file/movable_ink_CSV.csv %})

![Os campos que serão exibidos ao selecionar "CSV" como sua fonte de dados.]({% image_buster /assets/img/movable_ink/movable_ink2.png %})
{% endtab %}
{% tab Fonte de dados do site %}
- **Fonte de dados do site**: Cada linha deve ter pelo menos uma coluna de segmento e uma coluna de conteúdo. Após o upload do seu CSV, selecione quais colunas devem ser usadas para direcionamento do conteúdo.
  - Nesse processo, você precisará mapear:
    - Quais campos serão usados como segmentos
    - Quais campos deseja como campos de dados que podem ser personalizados dinamicamente no criativo (por exemplo: atributos de usuários ou atributos personalizados como nome, sobrenome, cidade etc.)

![Os campos que serão exibidos ao selecionar "Site" como sua fonte de dados.]({% image_buster /assets/img/movable_ink/movable_ink3.png %})
{% endtab %}
{% tab Integrações de API %}
- **Integrações de API**: Use a API de sua empresa para alimentar o conteúdo diretamente de uma resposta de API.

![Os campos que serão exibidos ao selecionar "Integração de API" como sua fonte de dados]({% image_buster /assets/img/movable_ink/movable_ink4.png %})
{% endtab %}
{% endtabs %}

### Etapa 2: crie uma campanha na plataforma da Movable Ink

Na tela inicial da Movable Ink, crie uma campanha. Você pode selecionar entre envio de e-mail a partir de HTML, e-mail a partir de imagem ou um bloco que pode ser usado em qualquer canal, incluindo push, mensagem no app e cartões de conteúdo (sugeridos).

Sugerimos também que dê uma olhada nas várias opções de conteúdo disponíveis nos blocos.

![Uma imagem da plataforma da Movable Ink ao criar uma nova campanha da Movable Ink.]({% image_buster /assets/img/movable_ink/movable_ink5.png %}){: style="max-width:70%"}

O Movable Ink tem um editor fácil para você arrastar e soltar elementos como texto ou imagens. Se tiver preenchido sua fonte de dados, você poderá gerar dinamicamente uma imagem usando as propriedades de dados. Além disso, também é possível criar fallbacks dentro desse fluxo para os usuários caso a campanha seja enviada a destinatários que não se enquadrem nos critérios de personalização.

![O editor de blocos da Movable Ink mostra os diferentes elementos personalizáveis.]({% image_buster /assets/img/movable_ink/create_campaign2.png %})

Antes de terminar sua campanha, certifique-se de fazer uma prévia das imagens dinâmicas e testar os parâmetros de consulta para ver como as imagens serão exibidas. Quando concluído, será gerado um URL dinâmico que poderá ser inserido no Braze!

Para saber mais sobre como usar a Movable Ink Platform, visite o [centro de suporte da Movable Ink](https://support.movableink.com/)

### Etapa 3: obtenha o URL do conteúdo da Movable Ink

Para incluir o conteúdo da Movable Ink nas mensagens do Braze, encontre o URL da fonte que a Movable forneceu a você. 

Para obter o URL da fonte, configure o conteúdo no dashboard da Movable Ink e, em seguida, finalize e exporte o conteúdo. Na página **Finish** (Concluir), copie o URL da fonte (`img src`) da tag de criativo.

![A página que aparece após a conclusão da campanha da Movable Ink, onde você encontra o URL do seu conteúdo.]({% image_buster /assets/img/movable_ink/obtain_url.png %}){: style="max-width:80%;"}

Em seguida, na plataforma da Braze, cole o URL no campo apropriado. Os campos apropriados para seu canal de envio de mensagens podem ser encontrados na etapa 4. Por fim, substitua todas as tags de mesclagem (como {% raw %}```&mi_u=%%email%%```{% endraw %}) pela variável Liquid correspondente (como {% raw %}```&mi_u={{${email_address}}}```{% endraw %}).

### Etapa 4: experiência da Braze

{% tabs local %}
{% tab E-mail %}
Na plataforma da Braze, cole sua tag de criativo no corpo do e-mail.![]({% image_buster /assets/img/movable_ink/web2.png %}){: style="max-width:90%"}<br><br>

{% endtab %}
{% tab Notificação por push %}

1. Na plataforma da Braze:
	- Push para Android: cole o URL nos campos **Imagem do ícone de push** e **Imagem da notificação expandida**.<br>![]({% image_buster /assets/img/movable_ink/android.png %}){: style="max-width:60%"}<br><br>
	- Push para iOS: cole o URL no campo **Mídia** e indique o formato de arquivo em uso.<br>![]({% image_buster /assets/img/movable_ink/ios.png %}){: style="max-width:60%"}<br><br>
	- Push para Web: cole o URL nos campos **Imagem do ícone de push** e **Imagem grande da notificação**.<br>![]({% image_buster /assets/img/movable_ink/web.png %}){: style="max-width:60%"}<br><br>
2. Para evitar que as imagens sejam armazenadas em cache, prefixe o URL na mensagem com tags Liquid vazias: <br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}

{% endtab %}
{% tab Mensagem no app %}

1. Na plataforma da Braze, cole o URL no campo **Notificações Rich**.![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. Forneça um URL exclusivo para evitar armazenamento em cache. Para garantir que as imagens em tempo real da Movable Ink funcionem e não sejam afetadas pelo armazenamento em cache, use o Liquid para acrescentar um registro de data e hora ao final do URL da imagem da Movable Ink.

Para fazer isso, use a sintaxe a seguir, substituindo o URL da imagem conforme necessário:
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
Esse modelo pega o horário atual (em segundos), anexa-o ao fim da guia da imagem da Movable Ink (como parâmetro de consulta) e depois calcula o resultado final. Você pode visualizá-lo com a guia **Teste** \- isso avaliará o código e mostrará uma prévia.

**3\.** Por fim, reavalie a inscrição no segmento. Para fazer isso, ative a opção `Re-evaluate audience membership and liquid at send-time` localizada na etapa **Públicos-alvo** de uma campanha. Se essa opção não estiver disponível, entre em contato com seu gerente de sucesso do cliente ou com o suporte da Braze. Essa opção instruirá os SDKs do Braze a solicitar novamente a campanha, fornecendo um URL exclusivo toda vez que uma mensagem no app for disparada.

{% endtab %}
{% tab Cartão de conteúdo %}

1. Na plataforma da Braze, cole o URL no campo **Notificações Rich**.![]({% image_buster /assets/img/movable_ink/image.png %}){: style="max-width:60%"}<br><br>
2. Para dispositivos móveis: as imagens dos cartões de conteúdo no iOS e no Android são armazenadas em cache após o recebimento e não são atualizadas. 
  - Como solução alternativa, agende sua campanha como mensagem recorrente diária, semanal ou mensal, com uma expiração correspondente, para que o cartão de conteúdo seja refletido no modelo. Por exemplo, um cartão de conteúdo que deve ser atualizado uma vez por dia deve ser definido como um envio programado diário com uma expiração de 1 dia.
3. Para garantir que as imagens em tempo real da Movable Ink funcionem e não sejam afetadas pelo armazenamento em cache quando o modelo do cartão de conteúdo é atualizado, use o Liquid para acrescentar um registro de data e hora ao final do URL da imagem da Movable Ink.

Para fazer isso, use a sintaxe a seguir, substituindo o URL da imagem conforme necessário:
{% raw %}
```
{% assign timestamp = "now" | date: "%s" %}
{% assign img = "https://movable-ink-image-url-goes-here" | append:timestamp %}
{{img}}
```
{% endraw %}
Esse modelo pega o horário atual (em segundos), anexa-o ao fim da guia da imagem da Movable Ink (como parâmetro de consulta) e depois calcula o resultado final. Você pode visualizá-lo com a guia **Teste**, que avaliará o código e mostrará uma prévia.

{% endtab %}
{% endtabs %}

## Solução de problemas

### As imagens dinâmicas não são exibidas corretamente? Você está tendo dificuldades com qual canal?
- **Push**: confirme se você tem uma lógica vazia antes do URL da imagem da Movable Ink: <br>{% raw %}```{% if true %}{% endif %}https://movable-ink-image-url-goes-here```{% endraw %}
- **Mensagens no app e cartões de conteúdo**: confirme se o URL da imagem é exclusivo para cada impressão. Isso pode ser feito anexando o Liquid apropriado para que cada URL seja diferente. Consulte [as instruções das mensagens no app e no cartão de conteúdo]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/movable_ink/#step-4-braze-experience). 
- **A imagem não está carregando**: Substitua quaisquer "tags de mesclagem" pelos campos Liquid correspondentes no dashboard da Braze. Por exemplo: {% raw %}```https://mi-msg.com/p/rp/image.png?mi_u=%%email%%```{% endraw %} por {% raw %}```https://mi-msg.com/p/rp/image.png?mi_u={{${email_address}}}```{% endraw %}.

### Está tendo problemas para exibir GIFs no Android?
- O Android requer suporte a GIFs na implementação. Siga o artigo sobre [personalização de mensagens no app do]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs/) Android se não tiver essa configuração.


[1]: https://www.movableink.com/
[fonte de dados]: ({% image_buster /assets/img/movable_ink/movable_ink1.png %})
[1]: ({% image_buster /assets/img/movable_ink/android.png %})
[2]: ({% image_buster /assets/img/movable_ink/ios.png %})
[3]: ({% image_buster /assets/img/movable_ink/web.png %})
