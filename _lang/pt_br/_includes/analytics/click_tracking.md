{% if include.section == "UTM parameters" %}

Embora o encurtamento de links permita rastrear seus URLs automaticamente, também é possível adicionar parâmetros UTM aos URLs para rastrear a performance das campanhas em ferramentas de análise de dados de terceiros, como o Google Analytics.

Para adicionar parâmetros UTM ao seu URL, faça o seguinte:

1. Comece com seu URL de base. Esse é o URL da página que você deseja rastrear (como `https://www.example.com`).
2. Adicione um ponto de interrogação (?) após o URL da base.
3. Adicione cada parâmetro UTM separado por um E comercial (&).

Um exemplo é `https://www.example.com?utm_source=newsletter&utm_medium=sms`.

{% endif %}

{% if include.section == "Frequently Asked Questions" %}

## Perguntas frequentes

### Os links que recebo ao testar o envio de URLs são reais?

Se a campanha tiver sido salva como rascunho antes do envio do teste, sim. Caso contrário, é um link de espaço reservado. Note que a URL exata enviada em uma campanha lançada pode ser diferente daquela enviada por meio de um envio de teste.

### Posso adicionar parâmetros UTM a um URL antes de ele ser encurtado?

Sim. Podem ser adicionados parâmetros estáticos e dinâmicos. 

### Por quanto tempo os URLs encurtados permanecem válidos?

Os URLs personalizados são válidos por dois meses a partir do momento do registro do URL.

### O SDK da Braze precisa ser instalado para encurtar links?

Não. O encurtamento de links funciona sem integração de SDK.

{% endif %}

{% if include.section == "Custom Domains" %}

## Domínios personalizados

O encurtamento de links também permite que você use seu próprio domínio para personalizar a aparência de seus URLs encurtados, o que ajuda a retratar uma imagem de marca consistente. Para saber mais, consulte [Domínios personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/).

{% endif %}