---
nav_title: LILT
article_title: LILT
description: "Este artigo de referência descreve a parceria entre a Braze e a LILT."
alias: /partners/lilt/
page_type: partner
search_tag: Partner
---

# LILT

> [A LILT](https://lilt.com/) é a solução completa de IA para tradução empresarial e criação de conteúdo. A LILT ativa organizações globais para dimensionar e otimizar suas operações de conteúdo, produtos, comunicações e suporte, com agentes de IA e fluxos de trabalho totalmente automatizados.

_Essa integração é mantida pela LILT._

## Sobre essa integração

O LILT Braze Connector ativa a tradução de modelos de e-mail em HTML com velocidade IA e qualidade de nível empresarial. Solicite a Tradução instantânea alinhada à marca ou a Tradução verificada com garantia de qualidade e receba o conteúdo de e-mails em vários idiomas da LILT diretamente no Braze. 

## Casos de uso

A integração da LILT Braze automatiza e acelera o processo de tradução, ativando as equipes de marketing global para lançar suas campanhas multilíngues rapidamente e com consistência de marca.

### Lançamento de campanha global simplificada

Lance campanhas de marketing em várias regiões simultaneamente, sem postergações decorrentes de transferências manuais de tradução.

- **Cenário:** Sua empresa está lançando um novo produto em 10 países.
- **Solução:** A sua equipe de marketing finaliza o modelo de e-mail em inglês no Braze, tag com `LILT: Ready`, e o LILT Connector extrai automaticamente o conteúdo. Os linguistas específicos do domínio revisam os prompts de tradução de IA na plataforma LILT para garantir a qualidade, e o conector empurra as versões traduzidas de volta para o Braze.
- **Benefício:** Reduz o tempo de colocação no mercado de suas campanhas globais de dias para horas, para que todos os clientes possam receber o anúncio do novo produto no momento ideal.

### Localização instantânea alinhada à marca

Use a IA da LILT para obter traduções imediatas e de acordo com a marca para comunicações urgentes.

- **Cenário:** É necessário enviar e-mails imediatamente para uma promoção relâmpago, uma oferta por tempo limitado ou uma interrupção urgente de serviço em cinco mercados geográficos.
- **Solução:** Você marca o modelo de e-mail com `LILT: Instant`. A LILT usa sua IA e ativos linguísticos específicos de sua empresa (como terminologia e guias de estilo) para gerar uma tradução de alta qualidade e consistente com a marca em questão de minutos.
- **Benefício:** Permite comunicações hiper-responsivas e em tempo real sem sacrificar a voz ou a qualidade da marca, o que é fundamental para o marketing sensível ao tempo.

## Pré-requisitos

| Pré-requisito       | Descrição |                        
|-----------------------|-----------------|
| Uma conta LILT   | É necessário ter uma conta LILT para aproveitar essa parceria.  |
| Uma chave da API REST da Braze  | Uma chave da API REST do Braze com as seguintes permissões:<br>- `templates.email.create`<br>- `templates.email.update`<br>- `templates.email.info`<br>- `templates.email.list`<br>- `templates.translations.source.get`<br>- `templates.translations.update`<br>- `templates.translations.get`<br>- `templates.translations.all.get`. <br><br> Crie essa chave no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Um endpoint Braze REST | [Sua URL de endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Seu endpoint depende do URL do Braze para sua instância.  |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}


## Integração

### Etapa 1: Configurar o conector Braze da LILT

1. Registre-se na LILT e acesse **Acessar** > **Novo conector** > **Braze**.
	
![Braze o conector em LILT.]({% image_buster /assets/img/lilt/image_1_select_connector.png %})

{: start="2"}
2\. Selecione o fluxo de trabalho de localização desejado para seu conteúdo Braze.

![Braze o fluxo de trabalho em LILT.]({% image_buster /assets/img/lilt/image_2_select_workflow.png %})	

{: start="3"}
3\. Insira e verifique os detalhes de configuração necessários:
- Sua chave de API do Braze
- Endpoint REST  do Braze

![Credenciais completas da API.]({% image_buster /assets/img/lilt/image_3_api_creds.png %})	

{: start="4"}
4\. Selecione **Verify (Verificar** ) para testar a configuração. Depois que a conexão for confirmada, salve a configuração.

### Etapa 2: Prepare seu espaço de trabalho no Braze

1. Ative os recursos multilíngues nas configurações de seu espaço de trabalho do Braze.

![Configure as localizações no Braze.]({% image_buster /assets/img/lilt/image_4_lilt_locales.png %})	

{: start="2"}
2\. Crie as seguintes tags no Braze para seu fluxo de trabalho LILT: 
- `LILT: Ready`
- `LILT: In progress`
- `LILT: Sent to LILT`
- `LILT: Delivered`
- `LILT: Needs Attention`
- `LILT: Instant`

![Configure as tags LILT no Braze.]({% image_buster /assets/img/lilt/image_5_lilt_tags.png %})	

{: start="3"}
### Etapa 3: Enviar conteúdo para a LILT para tradução 

1. Depois de configurar o conector LILT Braze, use as tags de tradução Liquid em seus modelos de e-mail Braze para identificar o conteúdo a ser traduzido. 
- Exemplo:  {% raw %}`{% translation id_0 %}`Olá, `{{first_name}}!{% endtranslation %}`{% endraw %}
2. Inicie a tradução atualizando a tag do modelo para indicar o fluxo de trabalho desejado: 
- Escolha `LILT: Ready` para uma tradução verificada
- Escolha `LILT: Instant` para uma tradução instantânea alinhada à marca
3. O LILT Braze Connector é executado em seu tempo predefinido para puxar o conteúdo marcado para o LILT. Acompanhe o progresso da tradução, pois as tags de conteúdo são atualizadas automaticamente no Braze para refletir o estágio de seu projeto. 
	
![Modelo de e-mail do Braze com tags de tradução.]({% image_buster /assets/img/lilt/image_6_braze_template.png %})	