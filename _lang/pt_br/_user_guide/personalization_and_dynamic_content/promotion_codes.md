---
nav_title: Códigos de promoção
article_title: Códigos de promoção
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "Este artigo de referência ensina como criar listas de códigos de promoção e adicioná-las às suas campanhas e canvas."
---

# Códigos promocionais

> Esta página aborda como criar listas de códigos promocionais e adicioná-los a suas campanhas e Canvas.

## Como funciona?

Códigos promocionais—também chamados de códigos de promoção—são uma ótima maneira de manter os usuários engajados, incentivando interações com forte ênfase em compras. É possível criar envios de mensagens que extraem de sua lista de códigos promocionais. 

Cada código promocional tem uma data de expiração de até seis meses e pode ser excluído antes do vencimento entrando em contato com [o Suporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Você pode armazenar e gerenciar até 20 milhões de códigos por lista. Ao gerenciar e analisar a performance de seus códigos promocionais, é possível tomar decisões direcionadas para suas estratégias promocionais e envio de mensagens.

{% alert important %}
Os códigos promocionais não podem ser enviados em mensagens no app no Canva. Se estiver participando do [acesso antecipado](#promotion-codes-iam-campaigns), os códigos promocionais poderão ser enviados em campanhas de mensagens no app.
{% endalert %}

## Criando uma lista de códigos promocionais

### Etapa 1: Acesse a seção Código promocional

![Botão para criar um código promocional.]({% image_buster /assets/img/promocodes/promocode1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

1. No dashboard, acesse **Configurações de dados** > **Códigos promocionais**.
2. Selecione **Criar lista de códigos promocionais**.

### Etapa 2: Nomear o código promocional

1. Nomeie sua lista de códigos promocionais e adicione uma descrição opcional.
2. Em seguida, crie um trecho de código para o código de promoção. 

Aqui estão alguns detalhes a serem considerados ao criar um trecho de código:

- Uma vez salvos, os trechos de código não podem ser editados.
- Trechos são sensíveis a maiúsculas e minúsculas. Por exemplo, "Birthday_promo" e "birthday_promo" serão reconhecidos como dois trechos diferentes.
- Use o nome do snippet no Liquid para fazer referência a esse conjunto de códigos promocionais.
- Verifique se o trecho de código já não está sendo usado em outra lista.

![Uma lista de códigos promocionais chamada "SpringSale2025" com o snippet de código "spring25".]({% image_buster /assets/img/promocodes/promocode3.png %}){: style="max-width:80%"}

### Etapa 3: Selecionar opções de código promocional

Cada lista de códigos promocionais tem uma data e hora de expiração correspondente que é definida no momento da criação. O comprimento máximo de expiração é de seis meses no futuro a partir do dia em que você está criando ou editando sua lista. 

Dentro desse período, você pode alterar e atualizar a data de expiração repetidamente. Esta data de expiração se aplicará a todos os códigos adicionados a esta lista. Após a expiração, os códigos serão excluídos do sistema Braze e quaisquer mensagens que chamarem o trecho de código dessa lista não serão enviadas.

![As configurações de expiração da lista indicam que todos os códigos restantes expirarão em 30 de abril de 2025, às 12 horas.]({% image_buster /assets/img/promocodes/promocode4.png %}){: style="max-width:80%"}

Você também tem a opção de configurar alertas de limite opcionais e personalizados. Se configurados, esses alertas enviarão um e-mail ao destinatário designado quando a lista estiver com poucos códigos promocionais disponíveis nesta lista ou quando sua lista de códigos promocionais estiver próxima do vencimento. O destinatário será notificado uma vez por dia.

![Um exemplo de um alerta de limite para notificar "marketing@abc.com" quando a lista de códigos promocionais expirar em 5 dias.]({% image_buster /assets/img/promocodes/promocode5.png %}){: style="max-width:80%"}

### Etapa 4: Fazer upload de códigos promocionais

O Braze não gerencia a criação ou o resgate de códigos, o que significa que você deve gerar seus códigos promocionais em um arquivo CSV e fazer upload deles no Braze. 

Certifique-se de que seu arquivo CSV siga estas diretrizes:

- Inclui uma coluna para códigos de promoção.
- Tem um código de promoção por linha.

Você pode usar nossa integração embutida com [Voucherify]({{site.baseurl}}/partners/ecommerce/loyalty/voucherify/) ou [Talon.One]({{site.baseurl}}/partners/ecommerce/loyalty/talonone/) para criar e exportar códigos de promoção.

{% alert important %}
O tamanho máximo do arquivo é 100 MB e o tamanho máximo da lista é 20MM de códigos não utilizados. Se você descobrir que o arquivo errado foi carregado, carregue um novo para substituir o anterior.
{% endalert %}

1. Após o fazer upload ser concluído, selecione **Salvar Lista** para salvar todos os detalhes e códigos que você acabou de inserir.

![Arquivo CSV chamado "springsale" que foi feito upload com sucesso.]({% image_buster /assets/img/promocodes/promocode7.png %})

{:start="2"}
2\. Depois de selecionar salvar, uma nova linha aparecerá no **Histórico de Importação**.
3\. Para atualizar a tabela para ver se sua importação foi concluída, selecione <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sincronizar** no topo da tabela.

![Códigos promocionais em processo de fazer upload.]({% image_buster /assets/img/promocodes/promocode8.png %})

{% alert note %}
Arquivos maiores levarão alguns minutos para importar. Enquanto você espera, pode sair da página e trabalhar em outra coisa enquanto a importação está em andamento. Quando a importação for concluída, o status será alterado para **Complete** na tabela.
{% endalert %}

#### Atualizando uma lista de códigos de promoção

Para atualizar uma lista, selecione uma de suas listas existentes. Você pode alterar o nome, a descrição, a expiração da lista e os alertas de limite. Você também pode adicionar mais códigos à lista carregando novos arquivos e selecionando **Atualizar Lista**.

Todos os códigos da lista terão a mesma expiração, independentemente da data de importação.

### Etapa 5: Use códigos promocionais

Para enviar códigos promocionais em mensagens:

1. Selecione **Copy Snippet** para copiar o snippet de código que você definiu ao criar sua lista de códigos promocionais.

![Uma opção para copiar o snippet para colar em sua mensagem.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:70%"}

{:start="2"}
2\. A partir daí, você pode colar este código em uma mensagem dentro do dashboard.

![Um exemplo de mensagem "Treat yourself to something nice this spring with our exclusive offer" (Presenteie-se com algo agradável nesta primavera com nossa oferta exclusiva) seguido do trecho de código.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:70%"}

Usando o [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), você pode inserir um dos códigos promocionais exclusivos do arquivo CSV feito upload em uma mensagem. Esse código será marcado como enviado no backend do Braze para garantir que nenhuma outra mensagem envie o mesmo código.

#### Envio de códigos promocionais aos usuários

Quando um trecho de código é usado em uma campanha multicanal ou etapa do canva, cada usuário sempre recebe um código único. Para diferentes etapas em uma canva, cada usuário recebe vários códigos de promoção.

Se um usuário for elegível para receber um código por mais de um canal, ele receberá o mesmo código em cada canal. Por exemplo, se um usuário receber duas mensagens por meio de dois canais, ele receberá apenas um código. O mesmo se aplica para fins de relatório: um código será enviado e o usuário receberá esse código através dos dois canais. Por exemplo, para uma etapa do canva multicanal, apenas um código seria usado pelo usuário.

{% alert important %}
Se não houver mais códigos de promoção disponíveis ao enviar mensagens de teste ou ao vivo de uma campanha que utiliza códigos de promoção, a mensagem não será enviada.
{% endalert %}

#### Enviando mensagens de teste com códigos promocionais

Os envios de teste e os envios de e-mail do grupo de teste usarão códigos de promoção, a menos que solicitado de outra forma. Entre em contato com o gerente da sua conta Braze para atualizar o comportamento deste recurso para que os códigos de promoção não sejam usados durante os envios de teste e envios de e-mail do grupo de teste.

## Determinando quantos códigos foram usados

Você pode encontrar a contagem de códigos restantes na coluna **Remanescente** da lista de códigos promocionais na página **Códigos promocionais**.

![Um exemplo de um código promocional com códigos não utilizados.]({% image_buster /assets/img/promocodes/promocode11.png %})

Este código de contagem também pode ser encontrado ao revisitar uma página de lista de códigos de promoção pré-existente. Também é possível exportar códigos não utilizados como um arquivo CSV. 

![Um código promocional chamado "Black Friday Sale" com 992 códigos restantes.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:70%"}

### Uso de códigos promocionais em campanhas de mensagens no app {#promotion-codes-iam-campaigns}

{% alert important %}
O uso de códigos promocionais em campanhas de mensagens no app está atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar desse acesso antecipado.
{% endalert %}

Depois de criar uma [campanha de mensagens no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages), você pode inserir um [snippet de lista de códigos promocionais]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) no corpo da mensagem da mensagem no app. 

Os códigos promocionais em mensagens no app serão deduzidos e usados somente quando um usuário disparar a exibição da mensagem no app.

## Envios multicanal e de canal único

Para campanhas de envio único e multicanal e canvas, todos os códigos de promoção referenciados no Liquid de uma mensagem são deduzidos para serem usados **antes** que a mensagem seja enviada para garantir que ocorra o seguinte:

- Os mesmos códigos de promoção são usados em todos os canais em uma mensagem multicanal.
- Códigos de promoção extras não são utilizados se uma mensagem falhar ou abortar.

Se um usuário tiver duas listas de códigos de promoção referenciadas em uma mensagem que é dividida por uma tag de lógica condicional Liquid, todos os códigos de promoção ainda serão deduzidos, independentemente de qual fluxo condicional o usuário seguir.

Se um usuário entrar em uma nova etapa do canva ou reentrar em um canva, e o código de promoção Liquid snippet for aplicado novamente para uma mensagem a esse usuário, um novo código de promoção será usado.

### Caso de uso

Para o exemplo a seguir, ambas as listas de códigos promocionais `vip-deal` e `regular-deal` serão deduzidas. Aqui está o Liquid:

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %} 
```
{% endraw %}

A Braze recomenda fazer o upload de mais códigos promocionais do que você estima que serão usados. Se uma lista de códigos de promoção expirar ou se esgotar os códigos de promoção, as mensagens subsequentes serão abortadas.

{% alert tip %}
**Aqui está uma analogia de como os códigos de promoção são usados na Braze.** <br><br>Imagine que enviar sua mensagem é como enviar uma carta no correio. Você entrega a carta a um funcionário, e ele vê que sua carta deve incluir um cupom. O atendente puxa o primeiro cupom da pilha e o adiciona ao envelope. O funcionário envia a carta, mas por algum motivo, a carta se perde no correio (e o cupom também está agora perdido). <br><br>Neste cenário, Braze é o atendente dos correios e seu código de promoção é o cupom. Não podemos recuperá-lo depois de ter sido retirado da pilha de códigos de promoção, independentemente do resultado do webhook.
{% endalert %}

## Perguntas frequentes

### Quais canais de envio de mensagens posso usar com códigos promocionais?

Os códigos de promoção são atualmente aceitos para e-mail, push móvel, web push, Cartões de Conteúdo, webhook, SMS e WhatsApp. As campanhas de e-mail de transação da Braze e as mensagens no app atualmente não suportam códigos promocionais.

### Os testes de envio e testes de envio usarão meus códigos de promoção?

Por padrão, os envios de teste e os envios de e-mail do grupo de teste usarão códigos de promoção por usuário, por envio de teste. No entanto, você pode entrar em contato com o gerente da sua conta Braze para atualizar esse comportamento e não usar códigos de promoção durante os testes.

### Como funcionam os códigos promocionais em uma campanha multicanal ou etapa do canva?

Os códigos promocionais são deduzidos antes que a mensagem seja enviada. Se os canais de envio de mensagens na campanha ou canva enviarem, isso pode fazer com que o código de promoção seja usado por razões que incluem horário de silêncio, limites de taxa, limitação de frequência, critérios de saída e mais. No entanto, se algum dos canais de mensagem for enviado, um código de promoção será usado.

### O que acontece se eu tiver vários trechos de Liquid que referenciam a mesma lista de códigos promocionais na minha mensagem?

O mesmo código de promoção será modelado para todas as instâncias do trecho Liquid em sua mensagem.

### O que acontece quando uma lista de códigos de promoção está expirada ou vazia?

Os códigos expirados são excluídos após seis meses.

Se a mensagem deveria ter contido um código de promoção de uma lista vazia ou expirada, a mensagem será cancelada. 

Se a mensagem contiver lógica Liquid que insere condicionalmente um código de promoção, a mensagem só será cancelada se ela deveria ter contido um código de promoção. Se a mensagem não deveria conter um código de promoção, a mensagem será enviada normalmente.

### Como faço para salvar um código promocional no perfil de um usuário para que ele possa ser usado em mensagens de acompanhamento?

Para fazer referência ao mesmo código de promoção em mensagens subsequentes, o código deve ser salvo no perfil do usuário como um atributo personalizado. Isso pode ser feito anexando um [webhook Braze-to-Braze]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/) à mesma campanha ou etapa do Canva Message.

