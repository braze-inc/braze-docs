# Banners

> Com Banners, você pode criar mensagens personalizadas para seus usuários, enquanto amplia o alcance de seus outros canais, como e-mail ou notificações por push. Você pode incorporar Banners diretamente em seu app ou site, o que permite interagir com os usuários por meio de uma experiência que parece natural.

![Um exemplo de Banner exibido em um dispositivo.]({% image_buster /assets/img/banners/sample_banner.png %})

## Pré-requisitos

A disponibilidade de Banners depende do seu pacote Braze. Entre em contato com seu gerente de conta ou gerente de sucesso do cliente para começar.

## Por que usar Banners?

Os Banners permitem que as equipes de marketing e produto personalizem o conteúdo do app ou site dinamicamente, refletindo a elegibilidade e o comportamento do usuário em tempo real. Eles exibem mensagens de forma persistente, proporcionando experiências contextualmente relevantes e não intrusivas que se atualizam automaticamente no início de cada sessão do usuário.

Depois que os Banners são integrados a um app ou site, os profissionais de marketing podem projetar e lançar Banners usando um simples editor de arrastar e soltar, eliminando a necessidade de assistência contínua de desenvolvedores, reduzindo a complexidade e melhorando a eficiência.

| Caso de uso | Explicação |
| --- | --- |
| Anúncios | Mantenha anúncios como eventos futuros ou mudanças de políticas em destaque na experiência do seu app. |
| Personalizando ofertas | Mostre promoções e incentivos personalizados com base no histórico de navegação, conteúdo do carrinho, nível de inscrição e status de fidelidade de cada usuário. |
| Direcionamento de engajamento de novos usuários | Guie novos usuários através de fluxos de integração e configuração de conta. |
| Vendas e promoções | Destaque conteúdo em destaque, produtos em tendência e campanhas de marca em andamento de forma persistente e direta na sua página inicial, sem interromper a experiência do usuário. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Recursos

Os recursos dos Banners incluem:

- **Construção de conteúdo fácil:** Crie e visualize seu Banner usando um editor visual de arrastar e soltar com suporte para imagens, texto, botões, formulários de captura de e-mail, código personalizado e muito mais.
- **Posicionamentos flexíveis:** Defina múltiplos locais dentro do seu aplicativo ou site onde os Banners podem aparecer, permitindo direcionamento preciso a contextos ou experiências de usuário específicas.
- **Personalização dinâmica:** Os banners são atualizados dinamicamente a cada nova sessão de usuário, garantindo que o conteúdo permaneça atual e personalizado usando as ferramentas de personalização integradas do Braze e a lógica Liquid.
- **Priorização nativa:** Defina a prioridade de exibição para quando vários banners visam o mesmo local, garantindo que a mensagem certa chegue aos usuários no momento certo.
- **Bloco de editor de código personalizado:** Use o bloco de editor de código personalizado para adicionar HTML personalizado para personalização avançada ou integração perfeita com seus estilos web existentes.

## Sobre os Banners {#about-banners}

### IDs de colocação {#placement-id}

As colocações de banners são locais específicos em seu app ou site [que você cria com o SDK do Braze]({{site.baseurl}}/developer_guide/banners/placements/) que designam onde os banners podem aparecer.

Locais comuns incluem o topo da sua página inicial, páginas de detalhes de produtos e fluxos de checkout. Depois que as colocações são criadas, os banners podem ser [atribuídos na sua campanha de Banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/).

Não há um limite fixo para o número de colocações que você pode criar por espaço de trabalho, e você pode criar quantos IDs de colocação sua experiência exigir. Cada colocação deve ser única dentro de um espaço de trabalho. Um único ID de colocação pode ser referenciado por até 25 mensagens ativas ao mesmo tempo.

{% alert important %}
Evite modificar IDs de colocação após lançar uma campanha de Banner.
{% endalert %}

### Prioridade do Banner {#priority}

Quando várias mensagens de Banner referenciam o mesmo ID de colocação, os banners são exibidos em ordem de prioridade: alta, média ou baixa. Por padrão, os banners são definidos como médios, mas você pode [definir manualmente a prioridade]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#set-priority) ao criar ou editar sua campanha de Banner. 

Se vários banners estiverem definidos para a mesma prioridade, o banner mais recente que o usuário é elegível é exibido primeiro.

### Solicitações de colocação {#requests}

{% multi_lang_include banners/placement_requests.md %}

### Entrega de mensagens

Mensagens de banner são entregues ao seu app ou site como conteúdo HTML, tipicamente renderizado dentro de um iframe. Isso garante que seus banners sejam renderizados de forma consistente em diferentes dispositivos e ajuda a manter seus estilos e scripts separados do restante do seu código.

Iframes permitem atualizações de conteúdo dinâmico e personalizado que não requerem alterações em sua base de código. Cada iframe recupera e exibe o HTML para cada sessão de usuário usando direcionamento de campanha e lógica de personalização.

{% multi_lang_include alerts/important_alerts.md alert='network dependency' %}

### Dimensões e tamanhos

Aqui está o que você precisa saber sobre dimensões e tamanhos de banners:

- Enquanto o criador permite que você visualize banners em diferentes dimensões, essa informação não é salva ou enviada para o SDK.
- O HTML ocupa toda a largura do contêiner em que é renderizado.
- Recomendamos criar um elemento de dimensão fixa e testar essas dimensões no criador.

## Limitações

Cada espaço de trabalho pode suportar até 200 campanhas de banner ativas. Se esse limite for atingido, você precisará [arquivar ou desativar]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#changing-the-status) uma campanha existente antes de criar uma nova.

Além disso, mensagens de banner não suportam os seguintes recursos:

- Campanhas acionadas por API e baseadas em ações
- Conteúdo conectado
- Códigos promocionais
- Desativações controladas pelo usuário
- `catalog_items` usando a [`:rerender` tag]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid)

{% alert tip %}
Quer ajudar a priorizar o que vem a seguir? Entre em contato com [banners-feedback@braze.com](mailto:banners-feedback@braze.com).
{% endalert %}

## Próximos passos

Agora que você sabe sobre banners, está pronto para os próximos passos:

1. [Criando colocações de banner em seu app ou site]({{site.baseurl}}/developer_guide/banners/placements/)
2. [Criando campanhas de Banner no Braze]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/)
3. [Tutorial: Exibindo um Banner pelo ID de Colocação]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
