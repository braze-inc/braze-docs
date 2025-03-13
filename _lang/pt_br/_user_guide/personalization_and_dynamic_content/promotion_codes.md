---
nav_title: Códigos de promoção
article_title: Códigos de promoção
page_order: 5
alias: "/promotion_codes/"
description: "Este artigo de referência ensina como criar listas de códigos de promoção e adicioná-las às suas campanhas e canvas."

---

# Códigos promocionais

> Códigos promocionais—também chamados de códigos de promoção—são uma ótima maneira de manter os usuários engajados, incentivando interações com forte ênfase em compras.<br><br>Esta página aborda como criar listas de códigos promocionais e adicioná-los a suas campanhas e Canvas.

Com a funcionalidade Liquid da Braze, oferecemos uma maneira de facilitar o uso generalizado de códigos promocionais, permitindo que as mensagens agora sejam extraídas da lista de promoções que você forneceu, de forma automática e intuitiva. O recurso de códigos promocionais oferece datas de vencimento de até seis meses e suporte para até 20MM de códigos individuais por lista.

{% alert important %}
Códigos promocionais não podem ser enviados em mensagens no app.
{% endalert %}

## Criando uma lista de códigos promocionais

### Etapa 1: Navegue até a seção Código de Promoção

![][1]{: style="float:right;max-width:30%;margin-left:15px;"}

No dashboard, Acessar **Configurações de Dados** > **Códigos Promocionais**, depois selecione **Criar Lista de Códigos Promocionais**.

{% alert note %}
Se você estiver usando a [navegação mais antiga]({{site.baseurl}}/navigation), você pode encontrar **Códigos de Promoção** em **Integrações**.
{% endalert %}

### Etapa 2: Como nomear e criar seu código de promoção

Nomeie sua lista de códigos promocionais e adicione uma descrição opcional.

![][2]{: style="max-width:90%"}

Em seguida, crie um trecho de código para o código de promoção. Este trecho de código será o que você irá referenciar no Liquid para exibir este conjunto específico de códigos promocionais. Certifique-se de que é um trecho de código que não está sendo usado em outra lista.

{% alert important %}
Trechos são sensíveis a maiúsculas e minúsculas. Por exemplo, "Birthday_promo" e "birthday_promo" serão reconhecidos como dois trechos diferentes.
{% endalert %}

![][3]{: style="max-width:90%"}

{% alert warning %}
Você não pode alterar o trecho de código após salvá-lo!
{% endalert %}

### Etapa 3: Opções de código promocional

Cada lista de códigos promocionais tem uma data e hora de expiração correspondente que é definida no momento da criação. O comprimento máximo de expiração é de seis meses no futuro a partir do dia em que você está criando ou editando sua lista. Dentro desse período, você pode alterar e atualizar a data de expiração repetidamente. Esta data de expiração se aplicará a todos os códigos adicionados a esta lista. Após a expiração, os códigos serão excluídos do sistema Braze e quaisquer mensagens que chamarem o trecho de código dessa lista não serão enviadas.

![][4]{: style="max-width:90%"}

Você também tem a opção de configurar alertas de limite opcionais e personalizados. Se configurados, esses alertas enviarão um e-mail ao destinatário designado quando a lista estiver com poucos códigos promocionais disponíveis nesta lista ou quando sua lista de códigos promocionais estiver próxima do vencimento. O destinatário será notificado uma vez por dia.

![][5]

### Etapa 4: Upload do código de promoção

O Braze não gerencia a criação ou o resgate de códigos, o que significa que você deve gerar seus códigos promocionais em um arquivo CSV e fazer upload deles no Braze. Certifique-se de que o arquivo CSV siga estas diretrizes:

- Inclui uma coluna para códigos de promoção.
- Tem um código de promoção por linha.

Você pode usar nossa integração embutida com [Voucherify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/voucherify/) ou [Talon.One]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/talonone/) para criar e exportar códigos de promoção.

{% alert note %}
O tamanho máximo do arquivo é 100 MB e o tamanho máximo da lista é 20MM de códigos não utilizados. Se você descobrir que o arquivo errado foi carregado, carregue um novo para substituir o anterior.
{% endalert %}

![][6]

Após o fazer upload ser concluído, selecione **Salvar Lista** para salvar todos os detalhes e códigos que você acabou de inserir.

![][7]

Depois de selecionar salvar, uma nova linha aparecerá no **Histórico de Importação**. Para atualizar a tabela para ver se sua importação foi concluída, selecione <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sincronizar** no topo da tabela.

![][8]

{% alert note %}
Arquivos maiores levarão alguns minutos para importar. Enquanto você espera, pode sair da página e trabalhar em outra coisa enquanto a importação está em andamento. Quando a importação for concluída, o status será alterado para **Complete** na tabela.
{% endalert %}

#### Atualizando uma lista de códigos de promoção

Para atualizar uma lista, selecione uma de suas listas existentes. Você pode alterar o nome, a descrição, a expiração da lista e os alertas de limite. Você também pode adicionar mais códigos à lista carregando novos arquivos e selecionando **Atualizar Lista**.

Todos os códigos da lista terão a mesma expiração, independentemente da data de importação.

### Etapa 5: Use códigos promocionais

Para enviar códigos promocionais em mensagens, selecione **Copiar Trecho** para copiar o trecho de código que você definiu ao criar sua lista de códigos promocionais.

![][9]{: style="max-width:70%"}

A partir daí, você pode colar este código em uma mensagem dentro do dashboard.

![][10]{: style="max-width:70%"}

Usando [Liquid][11], você pode inserir um dos códigos de promoção únicos do arquivo CSV carregado em uma mensagem. Esse código será marcado como enviado no backend do Braze para garantir que nenhuma outra mensagem envie o mesmo código. 

Quando um trecho de código é usado em uma campanha multicanal ou etapa do canva, cada usuário sempre recebe um código único. Para diferentes etapas em uma canva, cada usuário recebe vários códigos de promoção.

Se um usuário específico for elegível para receber um código por mais de um canal, esse usuário receberá o mesmo código por cada canal. Por exemplo, se um usuário receber duas mensagens por dois canais, ele receberá apenas um código. O mesmo se aplica para fins de relatório: um código será enviado e o usuário receberá esse código através dos dois canais. Por exemplo, para uma etapa do canva multicanal, apenas um código seria usado pelo usuário.

{% alert important %}
Se não houver mais códigos de promoção disponíveis ao enviar mensagens de teste ou ao vivo de uma campanha que utiliza códigos de promoção, a mensagem não será enviada.
{% endalert %}

#### Enviando mensagens de teste com códigos promocionais

Os envios de teste e os envios de e-mail do grupo de teste usarão códigos de promoção, a menos que solicitado de outra forma. Entre em contato com o gerente da sua conta Braze para atualizar o comportamento deste recurso para que os códigos de promoção não sejam usados durante os envios de teste e envios de e-mail do grupo de teste.

## Determinando quantos códigos foram usados

Você pode encontrar a contagem de códigos restantes na coluna **Restante** da lista de códigos promocionais, localizada na página **Códigos Promocionais**.

![][12]{: style="max-width:90%"}

Este código de contagem também pode ser encontrado ao revisitar uma página de lista de códigos de promoção pré-existente. 

![][13]{: style="max-width:50%"}

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

Se a mensagem deveria ter contido um código de promoção de uma lista vazia ou expirada, a mensagem será cancelada.

Se a mensagem contiver lógica Liquid que insere condicionalmente um código de promoção, a mensagem só será cancelada se ela deveria ter contido um código de promoção. Se a mensagem não deveria conter um código de promoção, a mensagem será enviada normalmente.

### Como faço para salvar um código promocional no perfil de um usuário para que ele possa ser usado em mensagens de acompanhamento?

Para fazer referência ao mesmo código de promoção em mensagens subsequentes, o código deve ser salvo no perfil do usuário como um atributo personalizado. Isso pode ser feito anexando um [webhook Braze-to-Braze]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/) à mesma campanha ou etapa do Canva Message.

[1]:{% image_buster /assets/img/promocodes/promocode1.png %}
[2]:{% image_buster /assets/img/promocodes/promocode2.png %}
[3]:{% image_buster /assets/img/promocodes/promocode3.png %}
[4]:{% image_buster /assets/img/promocodes/promocode4.png %}
[5]:{% image_buster /assets/img/promocodes/promocode5.png %}
[6]:{% image_buster /assets/img/promocodes/promocode6.png %}
[7]:{% image_buster /assets/img/promocodes/promocode7.png %}
[8]:{% image_buster /assets/img/promocodes/promocode8.png %}
[9]:{% image_buster /assets/img/promocodes/promocode9.png %}
[10]:{% image_buster /assets/img/promocodes/promocode10.png %}
[11]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[12]: {% image_buster /assets/img/promocodes/promocode11.png %}
[13]: {% image_buster /assets/img/promocodes/promocode12.png %}
