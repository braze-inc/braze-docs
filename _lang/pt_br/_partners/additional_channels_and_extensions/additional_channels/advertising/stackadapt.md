---
nav_title: StackAdapt
article_title: StackAdapt
description: "Este artigo de referência descreve a parceria entre a Braze e a StackAdapt."
alias: /partners/stackadapt/
page_type: partner
search_tag: Partner
---

# StackAdapt

> [StackAdapt](https://www.stackadapt.com/) é a principal plataforma de marketing impulsionada por IA usada por profissionais de marketing digital para entregar publicidade direcionada e orientada por desempenho.

_Esta integração é mantida pela StackAdapt._

A integração entre Braze e StackAdapt permite que você sincronize dados de perfil de usuário da Braze no StackAdapt Data Hub. Ao conectar as duas plataformas, você pode criar uma visão unificada de seus clientes e ativar dados primários para melhorar o desempenho dos anúncios.

## Casos de uso

- **Reengajar usuários inativos:** Identifique usuários que se desinscreveram das listas de marketing por e-mail na Braze e direcione-os com anúncios programáticos na StackAdapt para reengajá-los por meio de um canal diferente.
- **Criar experiências multicanal:** Estenda a jornada de um usuário além do e-mail. Por exemplo, se um usuário clicar em uma campanha de e-mail na Braze, você pode usar a StackAdapt para mostrar a ele um anúncio programático complementar, reforçando a mensagem e impulsionando uma ação adicional.
- **Personalizar em escala:** Aproveite pontos de dados granulares da Braze, como "Cidade Natal" ou "Idioma", para servir anúncios e e-mails altamente relevantes, localizados e específicos para o idioma.
- **Aprofundar a compreensão do seu público:** Ao sincronizar atributos de perfil, você pode criar segmentos de público mais ricos na StackAdapt, permitindo um direcionamento mais preciso e experiências de anúncios personalizadas.

## Pré-requisitos

| Requisito | Descrição         |
| ----------- | ------------------- |
| **Conta StackAdapt**  | Você precisa de uma conta StackAdapt ativa com permissões para gerenciar integrações do Data Hub. |
| **Chave da API REST do Braze**  | Uma chave da API REST do Braze com as seguintes permissões: <br>- users.export.ids<br>- users.export.segment<br>- email.unsubscribe<br>- email.hard_bounces<br>- messages.schedule_broadcasts<br>- campaigns.list<br>- campaigns.details<br>- canvas.list<br>- canvas.details<br>- segments.list<br>- segments.details<br>- purchases.product_list<br>- events.list<br>- feed.list<br>- feed.details<br>- templates.email.info<br>- templates.email.list<br>- subscription.status.get<br>- subscription.groups.get<br><br>Isso pode ser criado no painel da Braze em **Configurações** > **Chaves de API.** |
| **Endpoint REST  do Braze** | [Sua URL de endpoint REST.](https://www.braze.com/docs/api/basics/#endpoints) Seu endpoint depende do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Como funciona?

O StackAdapt Data Hub se conecta diretamente à sua conta Braze para puxar atributos de perfil de usuário. Isso permite que você aproveite os dados de cliente do Braze diretamente no StackAdapt para segmentação e ativação avançadas do público.

### Fluxo de dados

1. O StackAdapt inicia uma conexão segura com sua instância do Braze usando as credenciais da API fornecidas.
2. O StackAdapt recupera dados de perfil de usuário e especificamente as propriedades que você selecionou e mapeou.
3. Os dados são normalizados e ingeridos em seu Hub de Dados do StackAdapt, tornando-se disponíveis para segmentação e uso em suas campanhas.
4. A integração permite sincronizações de dados programadas (por exemplo, diárias) para manter seus públicos do StackAdapt atualizados com os dados de perfil mais recentes do Braze.

## Campos sincronizados

O StackAdapt pode sincronizar uma variedade de campos de perfil do Braze, incluindo, mas não se limitando a:

{% tabs local %}
{% tab Standard attributes %}
- E-mail
- Data de nascimento
- Nome
- Sobrenome
- Telefone
- Cidade
- País
- Gênero
- Fuso horário
- Criação às
- ID externo
- Idioma 

{% endtab %}
{% tab Custom attributes %}
Atributos que são específicos para seu app ou negócio, definidos com base nas necessidades específicas do seu negócio.

{% endtab %}
{% tab Attribution data %}
- Anúncio atribuído
- Grupo de anúncios atribuídos
- Campanha de atribuição
- Fonte atribuída

{% endtab %}
{% tab Subscription status %}
- Status de inscrição no e-mail
- Status de inscrição para push 

É crucial mapear com precisão os campos no Braze que refletem o consentimento do usuário para comunicações de marketing (por exemplo, status de inscrição em e-mail) para que seus esforços publicitários permaneçam em conformidade com as preferências e regulamentos de privacidade do usuário.

{% endtab %}
{% endtabs %}

## Configuração da integração

Siga estas etapas para importar seus perfis de usuário do Braze:

1. Faça login na sua conta do StackAdapt.
2. No menu de navegação, selecione **Hub de Dados**.
3. Selecione **Importar Perfis**, em seguida, selecione **Braze** na lista de integrações disponíveis.
4. Insira suas credenciais da API do Braze quando solicitado.
- **Chave da API REST do Braze:** Localizada no Braze indo para **Configurações** > **Chaves da API**. Como uma melhor prática de segurança, recomendamos criar uma chave de API dedicada para sua integração com o StackAdapt.
- **Chave do App Braze:** Localizada no Braze indo para **Configurações** > **Chaves da API** ou **Gerenciar Apps**.
- **Braze URL do Endpoint REST:** A URL base para sua instância do Braze (por exemplo, ```https://rest.iad-01.braze.com```).
5. Selecione **Conectar** para verificar as credenciais.

![Conexão Braze no StackAdapt.]({% image_buster /assets/img/stackadapt/stackadapt_braze_connection_settings.png %})

{: start="6"}
6\. Escolha sua conexão e selecione seu anunciante do StackAdapt.
7\. Configure suas **Mapeamentos de Propriedades**. Revise e confirme os mapeamentos padrão e as propriedades pré-selecionadas que o StackAdapt sugere.
8\. (Opcional) Se você quiser importar propriedades adicionais, selecione-as marcando as respectivas caixas de seleção e especifique se contêm PII e seu tipo de dado.

![Conexão Braze no StackAdapt.]({% image_buster /assets/img/stackadapt/stackadapt_mappings.png %})

{: start="9"}
9\. Adicione seus perfis a uma **Lista** ou crie uma nova para que você possa agrupar e segmentar seus perfis.
10\. Selecione **Ativar Integração** para iniciar a sincronização inicial de dados.

## Considerações

- **Importando eventos e propriedades personalizados:** Este recurso ainda não é suportado.
- **Latência de dados:** Pode levar até 24 horas para importar todos os dados do perfil do usuário.
- **Gerenciamento de consentimento:** Confirme que suas práticas de coleta de dados no Braze estão alinhadas com as regulamentações de privacidade e que você possui o consentimento necessário para usar dados de clientes para fins publicitários. O StackAdapt depende do status de consentimento passado de seus sistemas de origem.
- **Consistência de atributos:** Para maximizar a eficácia de seus dados, mantenha a consistência na forma como os atributos são nomeados e preenchidos no Braze antes de sincronizá-los com o StackAdapt.
