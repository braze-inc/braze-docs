---
nav_title: Acessar a Braze
permalink: "/braze_go/"
hidden: true
noindex: true
hide_toc: true
---

# Acessar a Braze

> O Braze Go oferece acesso simplificado à plataforma de engajamento com clientes Braze para ajudar suas equipes de marketing a começar em qualquer lugar e ir a qualquer lugar. Desenvolvido para ser simples e eficiente, o Braze Go é feito sob medida para mercados emergentes selecionados.

{% alert important %}
O Braze Go não está disponível em todos os mercados. Para saber mais sobre o Braze Go, fale com seu gerente de conta.
{% endalert %}

O Braze Go oferece as mesmas funcionalidades da Braze, com as principais diferenças concentradas nos seguintes recursos: 

- Você pode ter até 30 campanhas ativas.
- Você pode ter até 20 telas ativas.
- O limite de frequência padrão total da API REST é de 50.000 por hora, por espaço de trabalho.
    - Para uso fora do Braze Go, saiba mais sobre [os limites da API REST]({{site.baseurl}}/api/api_limits/#rate-limits-by-request-type).
- A retenção de dados de interação da campanha e do canva é de 2 meses, sem restauração.
    - Para uso não-Braze Go, saiba mais sobre a [disponibilidade de dados de interação de mensagens]({{site.baseurl}}/messaging_interaction_data/).

{% alert note %}
Os dados de interação para campanhas e telas são diferentes dos dados do Snowflake e não têm efeito algum.
{% endalert %}

- Não há suporte para webhooks Braze-to-Braze.
- Não há suporte para filtros relacionados a tags, especificamente os seguintes filtros:
    - Campanha ou tela clicada ou aberta com tag
    - Última mensagem recebida da campanha ou da tela com tag
    - Campanha recebida ou canvas com tag
- A Braze também poderá implementar uma política de retenção de dados para eventos de perfil de usuário e dados de compra que remova eventos, compras ou ambos com mais de 1 ano que não tenham sido realizados novamente em 1 ano. No entanto, esses dados ainda estariam disponíveis nas extensões de segmento do SQL por dois anos.

Se alguma funcionalidade acima for atualizada, isso será refletido neste artigo e anotado em nossas [notas de versão]({{site.baseurl}}/help/release_notes/#most-recent-braze-release-notes).