# Banners

> Com os Banners, é possível criar envios de mensagens personalizados para seus usuários e, ao mesmo tempo, ampliar o alcance de seus outros canais, como e-mail ou notificações por push. Você pode incorporar Banners diretamente no seu app ou site, o que permite o engajamento com os usuários por meio de uma experiência que parece natural.

![Um exemplo de banner renderizado em um dispositivo.]({% image_buster /assets/img/banners/sample_banner.png %})

## Pré-requisitos

A disponibilidade dos banners depende de seu pacote Braze. Entre em contato com seu gerente de conta ou gerente de sucesso do cliente para começar.

## Por que usar Banners?

Os banners permitem que as equipes de marketing e de produtos personalizem o conteúdo do app ou do site de forma dinâmica, refletindo a elegibilidade e o comportamento do usuário em tempo real. Eles exibem mensagens persistentemente em linha, fornecendo experiências não intrusivas e contextualmente relevantes que são atualizadas automaticamente no início de cada sessão do usuário.

Depois que os banners são integrados a um aplicativo ou site, os profissionais de marketing podem projetar e lançar banners usando um simples editor de arrastar e soltar, eliminando a necessidade de assistência contínua ao desenvolvedor, reduzindo a complexidade e melhorando a eficiência.

| Caso de uso | Explicação |
| --- | --- |
| Anúncios | Mantenha anúncios como eventos futuros ou mudanças de política na vanguarda da experiência no app. |
| Personalização de ofertas | Mostre promoções e incentivos personalizados com base no histórico de navegação de cada usuário, no conteúdo do carrinho, no nível de inscrição e no status de fidelidade. |
| Direcionamento para o engajamento de novos usuários | Orientar os novos usuários nos fluxos de integração e na configuração da conta. |
| Vendas e promoções | Destaque conteúdo em destaque, produtos em alta e campanhas de marca em andamento de forma persistente e direta na sua página inicial sem interromper a experiência do usuário. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Recursos

Os recursos para Banners incluem:

- **Criação fácil de conteúdo:** Crie e prévia seu Banner usando um editor visual de arrastar e soltar com suporte para imagens, texto, botões, formulários de captura de e-mail, código personalizado e muito mais.
- **Colocações flexíveis:** Defina vários locais em seu aplicativo ou site onde os banners podem ser exibidos, ativando o direcionamento preciso para contextos ou experiências de usuário específicos.
- **Personalização dinâmica:** Os banners são atualizados dinamicamente a cada nova sessão de usuário, garantindo que o conteúdo permaneça atualizado e personalizado usando as ferramentas de personalização integradas do Braze e a lógica Liquid.
- **Priorização de nativos:** Defina a prioridade de exibição para quando vários Banners direcionarem o mesmo posicionamento, garantindo que a mensagem certa chegue aos usuários no momento certo.
- **Suporte a HTML personalizado:** Incorpore blocos HTML personalizados para personalização avançada ou integração perfeita com seus estilos da Web existentes.

## Sobre Banners {#about-banners}

### IDs de colocação {#placement-id}

Os posicionamentos de banner são locais específicos em seu app ou site [criados com o SDK do Braze]({{site.baseurl}}/developer_guide/banners/placements/) que designam onde os banners podem aparecer.

Os locais comuns incluem a parte superior de sua página inicial, páginas de detalhes de produtos e fluxos de checkout. Depois que os canais são criados, os banners podem ser [atribuídos em sua campanha de banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/).

Não há limite fixo para o número de colocações que podem ser criadas por espaço de trabalho, e você pode criar quantas IDs de colocação forem necessárias para sua experiência. Cada colocação deve ser exclusiva em um espaço de trabalho. Um único ID de posicionamento pode ser referenciado por até 10 campanhas ativas ao mesmo tempo.

{% alert important %}
Evite modificar os IDs de posicionamento após o lançamento de uma campanha de banner.
{% endalert %}

### Prioridade do banner {#priority}

Quando várias campanhas fazem referência ao mesmo ID de posicionamento, os banners são exibidos em ordem de prioridade: alta, média ou baixa. Por padrão, os Banners recém-criados são definidos como médios, mas você pode [definir manualmente a prioridade]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/#set-priority) ao criar ou editar sua campanha de Banner. 

Se vários Banners estiverem definidos com a mesma prioridade, o Banner mais novo para o qual o usuário é elegível será exibido primeiro.

### Solicitações de colocação {#requests}

{% multi_lang_include banners/placement_requests.md %}

### Envio de mensagens

As mensagens no app ou no site são entregues como conteúdo HTML, normalmente renderizado em um iframe. Isso garante que seus Banners sejam renderizados de forma consistente em todos os dispositivos e ajuda a manter seus estilos e scripts separados do restante do seu código.

Os iframes permitem atualizações de conteúdo dinâmicas e personalizadas que não exigem alterações em sua base de código. Cada iframe recupera e exibe o HTML de cada sessão de usuário usando a lógica de direcionamento e personalização de campanhas.

### Dimensões e dimensionamento

Veja a seguir o que você precisa saber sobre as dimensões e o tamanho do Banner:

- Embora o criador permita que você faça uma prévia dos banners em diferentes dimensões, essas informações não são salvas nem enviadas ao SDK.
- O HTML ocupará toda a largura do contêiner em que for renderizado.
- Recomendamos criar um elemento de dimensão fixa e testar essas dimensões no criador.

## Limitações

Cada espaço de trabalho pode suportar até 200 campanhas ativas do Banner. Se esse limite for atingido, você precisará arquivar [ou desativar]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) uma campanha existente antes de criar uma nova.

Além disso, as mensagens de banner não são compatíveis com os seguintes recursos:

- Integração do Canva
- Campanhas acionadas por API e baseadas em ações
- Conteúdo conectado
- Códigos promocionais
- Demissões controladas pelo usuário
- `catalog_items` usando a [tag`:rerender` ]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid)

{% alert tip %}
Quer ajudar a priorizar o que está por vir? Entre em contato com [banners-feedback@braze.com](mailto:banners-feedback@braze.com).
{% endalert %}

## Próximos passos

Agora que você já sabe sobre Banners, está pronto para as próximas etapas:

1. [Criação de posicionamentos de banner em seu app ou site]({{site.baseurl}}/developer_guide/banners/placements/)
2. [Criação de campanhas de banner no Braze]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/)
3. [Tutorial: Exibição de um banner por ID de posicionamento]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
