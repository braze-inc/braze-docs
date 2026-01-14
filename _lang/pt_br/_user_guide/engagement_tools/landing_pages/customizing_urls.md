---
nav_title: Personalização do URL
article_title: Personalização de URLs de páginas de destino
description: "Saiba como personalizar os URLs de sua página de destino com a marca de sua empresa, conectando seu domínio ao seu espaço de trabalho no Braze."
page_order: 1
---

# Personalização de URLs de páginas de destino

> Saiba como personalizar os URLs de sua página de destino com a marca de sua empresa, conectando seu domínio ao seu espaço de trabalho no Braze.

## Como funciona

Quando você [conectar seu domínio ao Braze](#connecting-your-domain-to-braze), ele será usado como o domínio padrão para todas as páginas de destino. Por exemplo, se você conectar o subdomínio `forms.example.com`, os URLs da sua página de destino agora serão `forms.example.com/holiday-sale`.

O número de domínios personalizados que você pode conectar à sua conta Braze depende do seu [nível de plano]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/#plan-tiers). Para aumentar seu limite, entre em contato com seu gerente de conta Braze.

## Conectando seu domínio ao Braze

Para conectar um domínio à sua conta Braze, peça a um administrador que siga as etapas abaixo.

1. Vá para **Configurações** > **Configurações da página de destino**.
2. Digite o domínio ao qual deseja se conectar e selecione **Submit (Enviar**). Por exemplo, `forms.example.com`.
3. Copie e cole os registros **TXT** e **CNAME** nas configurações de DNS do seu provedor de domínio.
4. Retorne ao painel de controle do Braze para verificar a conexão.

Página Landing Page Settings com um registro TXT e dois registros CNAME listados com seus respectivos nomes e valores.]({% image_buster /assets/img/landing_pages/connect_subdomain.png %})

{% alert note %}
Dependendo do seu provedor de domínio, a conexão pode levar até 48 horas. Quando o processo for concluído, começaremos a usar seu domínio personalizado para suas páginas de destino no painel do Braze.
{% endalert %}

## Remoção de seu domínio

Se você for um administrador do Braze, poderá remover um domínio configurado anteriormente, executando as etapas a seguir:

1. Vá para **Configurações** > **Configurações da página de destino**.
2. Selecione **Remover domínio personalizado**
3. Confirmar a remoção do domínio.
4. Remova os registros DNS listados das configurações do seu domínio.

{% alert important %}
Quando você remover um domínio personalizado, esse URL não será mais válido. Todas as páginas de destino que estavam usando esse domínio serão automaticamente revertidas para o domínio padrão definido pelo Braze.
{% endalert %}


## Recursos do DNS

Abaixo estão listados recursos para criar e gerenciar registros DNS com os provedores de domínio mais usados. Se estiver usando um provedor diferente, consulte a documentação desse provedor ou entre em contato com a equipe de suporte para obter informações.

| Provedor de domínio | Recursos |
| --- | --- |
| Bluehost | [Explicação sobre registros DNS](https://my.bluehost.com/hosting/help/508)<br> [Gerenciamento de DNS Adicionar, editar ou excluir entradas de DNS](https://my.bluehost.com/hosting/help/559) |
| Dreamhost | [Como faço para adicionar registros DNS personalizados?](https://help.dreamhost.com/hc/en-us/articles/360035516812) |
| GoDaddy | [Adicionar um registro CNAME](https://www.godaddy.com/help/add-a-cname-record-19236?) |
| Cloudflare | [Gerenciar registros DNS](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) |
| Squarespace | [Adição de configurações de DNS personalizadas](https://support.squarespace.com/hc/en-us/articles/360002101888-Adding-custom-DNS-records-to-your-Squarespace-managed-domain) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Solução de problemas 

### Falha na conexão com meu domínio

Verifique se o seu domínio foi inserido corretamente e se ele corresponde ao que você enviou ao Braze a partir da sua conta de provedor de domínio. Se estiver correto e corresponder, verifique os registros TXT e CNAME fornecidos pelo Braze. Eles devem corresponder aos registros inseridos na conta do provedor de domínio.

## Perguntas frequentes

### Posso conectar vários subdomínios ao meu espaço de trabalho ou conectar um subdomínio a vários espaços de trabalho?

Não, no momento você só pode conectar um subdomínio a um espaço de trabalho.

### Posso usar o mesmo subdomínio que uso atualmente para meu site principal ou meu domínio de envio?

Não, você não pode usar subdomínios que já estejam em uso. Embora esses subdomínios sejam válidos, eles não podem ser usados para landing pages se já estiverem atribuídos a outras finalidades ou tiverem registros DNS que entrem em conflito com os registros CNAME necessários.

