---
nav_title: Códigos promocionais
article_title: Códigos promocionais
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "Este artigo de referência aborda como criar listas de códigos promocionais e adicioná-los a suas campanhas e Canvases."
---

# Códigos promocionais

> Esta página aborda como criar listas de códigos promocionais e adicioná-los às suas campanhas e Canvases.

## Sobre códigos promocionais

Os códigos de promoção - também chamados de códigos promocionais - são uma ótima maneira de manter os usuários envolvidos, promovendo interações com forte ênfase nas compras. Você pode criar mensagens que extraem de sua lista de códigos promocionais. 

Cada código promocional tem uma data de validade de até seis meses. Você pode armazenar e gerenciar até 20 milhões de códigos por lista. Ao gerenciar e analisar o desempenho de seus códigos promocionais, você pode tomar decisões direcionadas para suas estratégias e mensagens promocionais.

{% alert important %}
Os códigos promocionais não podem ser enviados em mensagens in-app no Canvas.
{% endalert %}

## Criação de uma lista de códigos promocionais {#create}

### Etapa 1: Vá para a seção Código promocional

Botão para criar um código promocional.]({% image_buster /assets/img/promocodes/promocode1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

1. No painel, vá para **Data Settings (Configurações de dados** ) > **Promotion Codes (Códigos de promoção**).
2. Selecione **Criar lista de códigos promocionais**.

### Etapa 2: Nomear o código promocional

1. Dê um nome à sua lista de códigos promocionais e adicione uma descrição opcional.
2. Em seguida, crie um snippet de código para o código promocional. 

Aqui estão alguns detalhes a serem considerados ao criar um trecho de código:

- Uma vez salvos, os trechos de código não podem ser editados.
- Os snippets diferenciam maiúsculas de minúsculas. Por exemplo, "Birthday_promo" e "birthday_promo" serão reconhecidos como dois snippets diferentes.
- Use o nome do snippet no Liquid para fazer referência a esse conjunto de códigos promocionais.
- Verifique se o trecho de código já não está sendo usado em outra lista.

\![Uma lista de códigos promocionais denominada "SpringSale2025" com o snippet de código "spring25".]({% image_buster /assets/img/promocodes/promocode3.png %}){: style="max-width:80%"}

### Etapa 3: Selecionar opções de código promocional

Cada lista de códigos promocionais tem uma data e hora de expiração correspondente que é definida na criação. A duração máxima da expiração é de seis meses no futuro, a partir do dia em que você estiver criando ou editando sua lista. 

Dentro desse período, você pode alterar e atualizar a data de validade repetidamente. Essa data de expiração se aplicará a todos os códigos adicionados a essa lista. Após a expiração, os códigos serão excluídos do sistema Braze, e todas as mensagens que chamarem o trecho de código dessa lista não serão enviadas.

Configurações de expiração da lista de que todos os códigos restantes expirarão em 30 de abril de 2025 às 12 horas.]({% image_buster /assets/img/promocodes/promocode4.png %}){: style="max-width:80%"}

Você também tem a opção de configurar alertas de limite opcionais e personalizados. Se configurados, esses alertas enviarão um e-mail ao destinatário designado quando a lista estiver com poucos códigos promocionais disponíveis nessa lista ou quando sua lista de códigos promocionais estiver perto de expirar. O destinatário será notificado uma vez por dia.

\![Um exemplo de um alerta de limite para notificar "marketing@abc.com" quando a lista de códigos promocionais expirar em 5 dias.]({% image_buster /assets/img/promocodes/promocode5.png %}){: style="max-width:80%"}

### Etapa 4: Fazer upload de códigos promocionais

O Braze não gerencia a criação ou o resgate de códigos, o que significa que você deve gerar seus códigos promocionais em um arquivo CSV e carregá-los no Braze. 

Certifique-se de que seu arquivo CSV siga essas diretrizes:

- Inclui uma coluna para códigos promocionais.
- Possui um código promocional por linha.

Você pode usar nossa integração interna com o [Voucherify]({{site.baseurl}}/partners/ecommerce/loyalty/voucherify/) ou [Talon.One]({{site.baseurl}}/partners/ecommerce/loyalty/talonone/) para criar e exportar códigos promocionais.

{% alert important %}
O tamanho máximo do arquivo é de 100 MB, e o tamanho máximo da lista é de 20MM de códigos não utilizados. Se você descobrir que foi feito o upload do arquivo errado, faça o upload de um novo arquivo e o anterior será substituído.
{% endalert %}

1. Após a conclusão do upload, selecione **Save List (Salvar lista** ) para salvar todos os detalhes e códigos que você acabou de inserir.

\![arquivo CSV denominado "springsale" que foi carregado com sucesso.]({% image_buster /assets/img/promocodes/promocode7.png %})

{:start="2"}
2\. Depois de selecionar salvar, uma nova linha aparecerá no **Import History (Histórico de importação**).
3\. Para atualizar a tabela e verificar se a importação foi concluída, selecione <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sync** na parte superior da tabela.

\![Os códigos de promoção estão sendo carregados.]({% image_buster /assets/img/promocodes/promocode8.png %})

{% alert note %}
Arquivos maiores levarão alguns minutos para serem importados. Enquanto espera, você pode sair da página e trabalhar em algo enquanto a importação está em andamento. Quando a importação for concluída, o status será alterado para **Complete** na tabela.
{% endalert %}

## Atualização de uma lista de códigos promocionais

Para atualizar uma lista, selecione uma de suas listas existentes. Você pode alterar o nome, a descrição, a expiração da lista e os alertas de limite. Você também pode adicionar mais códigos à lista fazendo upload de novos arquivos e selecionando **Update List**. Todos os códigos da lista terão a mesma expiração, independentemente da data de importação.

{% alert important %}
Os códigos promocionais não podem ser excluídos.
{% endalert %}

### Modificação da lista de códigos promocionais incorretos 

Se você tiver carregado um arquivo CSV com os códigos promocionais incorretos e selecionado **Salvar lista**, poderá resolver isso por qualquer um dos métodos:

- Eliminar a lista inteira: Pare de usar a lista atual de códigos promocionais em qualquer campanha, tela ou modelo. Em seguida, carregue o arquivo CSV com os códigos corretos e use-os em suas mensagens.
- Use os códigos incorretos: Crie uma campanha que envie códigos promocionais da lista de códigos promocionais incorretos para um espaço reservado até que todos os códigos incorretos sejam usados. Em seguida, carregue os códigos promocionais corretos na mesma lista.

## Uso de códigos promocionais {#update}

Para enviar um código promocional em uma mensagem, selecione **Copy Snippet** ao lado da lista de códigos promocionais [que você criou anteriormente](#create).

\![Uma opção para copiar o snippet e colá-lo em sua mensagem.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:50%"}

Cole os trechos de código em uma de suas mensagens no Braze e, em seguida, use [o Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) para inserir um dos códigos promocionais exclusivos de sua lista. Esse código será marcado como enviado, garantindo que nenhuma outra mensagem envie o mesmo código.

\![Um exemplo de mensagem "Treat yourself to something nice this spring with our exclusive offer" (Presenteie-se com algo agradável nesta primavera com nossa oferta exclusiva) seguida pelo trecho de código.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:50%"}

### Etapas do Canvas

Quando um snippet de código é usado em uma campanha ou no Canvas com mensagens multicanal, cada usuário recebe um código exclusivo. Em um Canvas com várias etapas que fazem referência a códigos promocionais, um usuário recebe um novo código para cada etapa que entra.

Para atribuir um código de promoção em um Canvas e reutilizá-lo em todas as etapas:

1. Atribua o código promocional como um atributo personalizado na primeira etapa (Atualização do usuário).
2. Use Liquid em etapas posteriores para fazer referência a esse atributo personalizado em vez de gerar um novo código.

Quando um usuário se qualifica para um código em vários canais, ele recebe o mesmo código em cada canal. Por exemplo, se eles receberem mensagens por e-mail e push, o mesmo código será enviado para ambos. Os relatórios também refletem um único código.

{% alert note %}
Se não houver códigos promocionais disponíveis, as mensagens de teste ou em tempo real que dependem de códigos não serão enviadas.
{% endalert %}

### Em campanhas de mensagens in-app {#promotion-codes-iam-campaigns}

Depois de criar uma [campanha de mensagem in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages), você pode inserir um [snippet de lista de códigos promocionais]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) no corpo da mensagem in-app. 

Os códigos promocionais em mensagens in-app serão deduzidos e usados somente quando um usuário acionar a exibição da mensagem in-app.

### Em mensagens de teste

Os envios de teste e os envios de e-mail de grupos de sementes usarão os códigos promocionais, a menos que seja solicitado o contrário. Entre em contato com o gerente da sua conta Braze para atualizar o comportamento desse recurso, de modo que os códigos promocionais não sejam usados durante os envios de teste e os envios de e-mail de grupo de sementes.

### Com mensagens extras para o Currents

{% multi_lang_include shopify.md section='Liquid promotion codes with Currents' %}

## Salvar códigos promocionais nos perfis de usuário {#save-to-profile}

Para fazer referência ao mesmo código de promoção em mensagens subsequentes, o código deve ser salvo no perfil do usuário como um atributo personalizado. Isso pode ser feito por meio de uma [etapa de atualização do usuário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) que atribui o código de desconto a um atributo personalizado, como "Código promocional", diretamente antes de uma etapa de mensagem.

Primeiro, selecione o seguinte para cada campo na etapa Atualização do usuário:

- **Nome do atributo:** Código promocional
- **Ação:** Atualização
- **Valor-chave:** O trecho de código Liquid do código promocional, como {% raw %}`{% promotion('spring25') %}`{% endraw %}

Em segundo lugar, adicione o atributo personalizado (neste exemplo, {% raw %}`{{custom_attribute.${Promo Code}}`{% endraw %}) a uma mensagem. O código de desconto será modelado em.

## Visualização do uso do código promocional

Você pode encontrar a contagem de códigos restantes na coluna **Remanescente** da lista de códigos promocionais na página **Códigos promocionais**.

\![Um exemplo de um código promocional com códigos não utilizados.]({% image_buster /assets/img/promocodes/promocode11.png %})

Essa contagem de códigos também pode ser encontrada ao revisitar uma página de lista de códigos promocionais pré-existente. Você também pode exportar códigos não utilizados como um arquivo CSV. 

Um código promocional chamado "Black Friday Sale" com 992 códigos restantes.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:50%"}

## Envios multicanal e de canal único

Para campanhas multicanal e de envio único e Canvases, todos os códigos promocionais referenciados no Liquid de uma mensagem são deduzidos para serem usados **antes de** a mensagem ser enviada para garantir que o seguinte ocorra:

- Os mesmos códigos promocionais são usados em todos os canais em uma mensagem multicanal.
- Os códigos promocionais extras não são usados se uma mensagem falhar ou for cancelada.

Se um usuário tiver duas listas de códigos promocionais referenciadas em uma mensagem que é dividida por uma tag de lógica condicional Liquid, todos os códigos promocionais ainda serão deduzidos, independentemente do fluxo condicional que o usuário seguir.

Se um usuário entrar em uma nova etapa do Canvas ou entrar novamente em um Canvas, e o snippet Liquid do código promocional for aplicado novamente a uma mensagem para esse usuário, um novo código promocional será usado.

### Exemplo

No exemplo a seguir, as duas listas de códigos promocionais `vip-deal` e `regular-deal` serão deduzidas. Aqui está o Liquid:

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %} 
```
{% endraw %}

A Braze recomenda fazer o upload de mais códigos promocionais do que você estima que será usado. Se uma lista de códigos promocionais expirar ou ficar sem códigos promocionais, as mensagens subsequentes serão canceladas.

{% alert tip %}
**Aqui está uma analogia de como os códigos promocionais são usados no Braze.** <br><br>Imagine que enviar sua mensagem é como enviar uma carta pelo correio. Você entrega a carta a um funcionário e ele vê que sua carta deve incluir um cupom. O funcionário retira o primeiro cupom da pilha e o coloca no envelope. O funcionário envia a carta, mas, por algum motivo, ela se perde no correio (e o cupom também se perde). <br><br>Nesse cenário, o Braze é o funcionário dos correios, e seu código promocional é o cupom. Não podemos recuperá-lo depois de ter sido retirado da pilha de códigos promocionais, independentemente do resultado do webhook.
{% endalert %}

## Perguntas frequentes

### Quais canais de mensagens posso usar com códigos promocionais?

Atualmente, os códigos promocionais são compatíveis com e-mail, mobile push, web push, Content Cards, webhook, SMS e WhatsApp. No momento, as campanhas de Braze Transactional Email e as mensagens no aplicativo não suportam códigos promocionais.

### Os envios de teste e semente contam para o uso?

Por padrão, os envios de teste e os envios de e-mail de grupos de sementes usarão códigos promocionais por usuário, por envio de teste. No entanto, você pode entrar em contato com o gerente da sua conta Braze para atualizar esse comportamento e não usar códigos promocionais durante o teste.

### O que acontece quando vários canais de mensagens usam o mesmo snippet de código de promoção?

Se um determinado usuário estiver qualificado para receber um código por meio de vários canais, ele receberá o mesmo código em cada canal. Apenas um código promocional será usado, independentemente dos canais recebidos.

### Posso usar vários snippets do Liquid para fazer referência à mesma lista de códigos promocionais em uma mensagem?

Sim. O Braze aplicará o mesmo código promocional em todas as instâncias desse snippet na mensagem, garantindo que o usuário receba apenas um código exclusivo.

### O que acontece quando uma lista de códigos promocionais está expirada ou vazia?

Os códigos expirados são excluídos após seis meses.

Se a mensagem deveria conter um código promocional de uma lista vazia ou expirada, a mensagem será cancelada. 

Se a mensagem contiver a lógica Liquid que insere condicionalmente um código promocional, a mensagem só será cancelada se deveria conter um código promocional. Se a mensagem não deveria conter um código promocional, a mensagem será enviada normalmente.

### Se eu tiver carregado os códigos promocionais errados, posso atualizá-los?

Sim. Você pode resolver isso depreciando a lista inteira ou usando um espaço reservado para excluir a lista. Para obter mais informações, consulte [Atualização de códigos promocionais](#update).

### Posso salvar um código promocional no perfil de um usuário para mensagens futuras?

Sim. É possível salvar códigos promocionais no perfil de um usuário por meio de uma etapa de atualização do usuário. Para obter mais informações, consulte [Como salvar códigos promocionais em perfis de usuário](#save-to-profile).
