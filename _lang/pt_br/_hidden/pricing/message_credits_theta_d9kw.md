---
nav_title: Créditos de mensagens - Theta
permalink: "/message_credits_theta_d9kw/"
hidden: true
noindex: true
hide_toc: true
---

# Créditos do envio de mensagens - Theta (Confidencial)

> Créditos de mensagem é a estrutura de envio de mensagens entre canais da Braze para nossas ofertas nativas de SMS, MMS e WhatsApp. Os Créditos de Mensagens proporcionam uma experiência flexível e transparente ao aproveitar os canais de envio de mensagens da Braze. Os créditos lhe dão acesso a qualquer um dos canais apresentados na tabela desta página.

{% alert note %}
Diferentes canais terão diferentes unidades de medida nos relatórios.<br><br>
<b>WhatsApp:</b> Conversas<br>
<b>SMS:</b> Segmentos<br>
<b>MMS:</b> Segmentos<br><br>
Em outras palavras, os créditos por mensagens do WhatsApp serão calculados sobre os inícios de conversas, e os créditos por mensagens SMS e MMS serão calculados sobre os segmentos de mensagens enviados.
<br><br>
Por fim, as taxas da operadora são cobradas separadamente (em atraso) e não são consideradas como parte dessa SKU de créditos de mensagens.
{% endalert %}

## Definições

As definições das colunas são as seguintes:

|---------|-------------------------------------------------|
| **Índice de crédito do canal** | Valor do crédito de linha de base para cada canal |
| **Destino** | Região final específica, país ou tipo de mensagem que está sendo enviada por meio da plataforma Braze |
| **Multiplicador** | Escalonamento da taxa de crédito do canal, dependendo do preço do destino específico |
| **Créditos por 1 envio** | Número exato de Message Credit para enviar uma mensagem<br> (créditos por mensagem = taxa de crédito do canal x multiplicador de destino) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


## Tabela de proporção de crédito para créditos de mensagens - Theta

{% details Clique para expandir %}
<table>
    <colgroup>
        <col span="4" style="background-color:background-color:#FFFFFF;">
        <col style="background-color:#f0f0f5">
    </colgroup>
    <tr>
        <th><b>Canal</b></th>
        <th><b>Índice de crédito do canal</b></th>
        <th><b>Destino</b></th>
        <th><b>Multiplicador</b></th>
        <th class="credits-column"><b>Créditos por 1 envio</b></th>
    </tr>
    <tbody><tr>
        <td>SMS - EUA / CA</td>
        <td>0.7</td>
        <td>Estados Unidos</td>
        <td>1.00</td>
        <td>0.70</td>
    </tr>
    <tr>
        <td>SMS - EUA / CA</td>
        <td>0.7</td>
        <td>Estados Unidos Ligação gratuita</td>
        <td>1.50</td>
        <td>1.05</td>
    </tr>
    <tr>
        <td>SMS - EUA / CA</td>
        <td>0.7</td>
        <td>Canadá</td>
        <td>1.00</td>
        <td>0.70</td>
    </tr>
    <tr>
        <td>SMS - EUA / CA</td>
        <td>0.7</td>
        <td>Ligação gratuita para o Canadá</td>
        <td>1.30</td>
        <td>0.91</td>
    </tr>
    <tr>
        <td>MMS - EUA / CA</td>
        <td>2</td>
        <td>Estados Unidos</td>
        <td>1.00</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>MMS - EUA / CA</td>
        <td>2</td>
        <td>Estados Unidos Ligação gratuita</td>
        <td>2.00</td>
        <td>4.00</td>
    </tr>
    <tr>
        <td>MMS - EUA / CA</td>
        <td>2</td>
        <td>Código longo do Canadá</td>
        <td>1.50</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>MMS - EUA / CA</td>
        <td>2</td>
        <td>Código curto do Canadá</td>
        <td>4.00</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>MMS - EUA / CA</td>
        <td>2</td>
        <td>Ligação gratuita para o Canadá</td>
        <td>1.30</td>
        <td>2.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Abkhazia</td>
        <td>0.62</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Afeganistão</td>
        <td>9.47</td>
        <td>94.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Albânia</td>
        <td>2.29</td>
        <td>22.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Argélia</td>
        <td>5.23</td>
        <td>52.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Samoa Americana</td>
        <td>4.74</td>
        <td>47.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Andorra</td>
        <td>3.32</td>
        <td>33.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Angola</td>
        <td>2.24</td>
        <td>22.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Anguilla</td>
        <td>3.33</td>
        <td>33.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Antígua e Barbuda</td>
        <td>2.47</td>
        <td>24.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Argentina</td>
        <td>1.02</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Armênia</td>
        <td>3.49</td>
        <td>34.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Aruba</td>
        <td>2.61</td>
        <td>26.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Austrália SMS</td>
        <td>0.36</td>
        <td>3.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Austrália - MMS</td>
        <td>3.10</td>
        <td>31.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Áustria</td>
        <td>1.77</td>
        <td>17.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Azerbaijão</td>
        <td>9.77</td>
        <td>97.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Bahamas</td>
        <td>1.23</td>
        <td>12.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Bahrein</td>
        <td>0.92</td>
        <td>9.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Bangladesh</td>
        <td>5.81</td>
        <td>58.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Barbados</td>
        <td>3.09</td>
        <td>30.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Belarus</td>
        <td>6.35</td>
        <td>63.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Bélgica</td>
        <td>2.40</td>
        <td>24.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Belize</td>
        <td>6.90</td>
        <td>69.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Benin</td>
        <td>3.64</td>
        <td>36.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Bermudas</td>
        <td>2.99</td>
        <td>29.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Butão</td>
        <td>10.10</td>
        <td>101.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Bolívia</td>
        <td>3.66</td>
        <td>36.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Bósnia e Herzegovina</td>
        <td>2.12</td>
        <td>21.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Botsuana</td>
        <td>2.52</td>
        <td>25.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Brasil</td>
        <td>0.25</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Brunei</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Bulgária</td>
        <td>2.70</td>
        <td>27.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Burkina Faso</td>
        <td>3.35</td>
        <td>33.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Burundi</td>
        <td>9.47</td>
        <td>94.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Camboja</td>
        <td>4.30</td>
        <td>43.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Camarões</td>
        <td>3.49</td>
        <td>34.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Cabo Verde</td>
        <td>3.66</td>
        <td>36.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Caribe Neerlandês</td>
        <td>2.17</td>
        <td>21.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Ilhas Cayman</td>
        <td>3.37</td>
        <td>33.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>República Centro-Africana</td>
        <td>3.07</td>
        <td>30.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Chade</td>
        <td>7.30</td>
        <td>73.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Chile</td>
        <td>1.64</td>
        <td>16.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>China</td>
        <td>0.64</td>
        <td>6.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Colômbia</td>
        <td>0.02</td>
        <td>0.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Comores</td>
        <td>6.19</td>
        <td>61.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Congo</td>
        <td>5.04</td>
        <td>50.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Ilhas Cook</td>
        <td>3.52</td>
        <td>35.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Costa Rica</td>
        <td>1.06</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Croácia</td>
        <td>2.31</td>
        <td>23.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Cuba</td>
        <td>2.12</td>
        <td>21.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Curaçao</td>
        <td>0.99</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Chipre</td>
        <td>2.18</td>
        <td>21.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>República Tcheca</td>
        <td>1.01</td>
        <td>10.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Dinamarca</td>
        <td>1.01</td>
        <td>10.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Djibuti</td>
        <td>4.09</td>
        <td>40.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Dominica</td>
        <td>3.79</td>
        <td>37.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>República Dominicana</td>
        <td>1.29</td>
        <td>12.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>República Democrática do Congo</td>
        <td>5.77</td>
        <td>57.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Equador</td>
        <td>2.76</td>
        <td>27.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Egito</td>
        <td>2.43</td>
        <td>24.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>El Salvador</td>
        <td>2.45</td>
        <td>24.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Guiné Equatorial</td>
        <td>4.36</td>
        <td>43.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Eritreia</td>
        <td>2.48</td>
        <td>24.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Estônia</td>
        <td>2.41</td>
        <td>24.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Eswatini</td>
        <td>0.58</td>
        <td>5.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Etiópia</td>
        <td>8.63</td>
        <td>86.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Ilhas Malvinas</td>
        <td>3.43</td>
        <td>34.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Ilhas Faroé</td>
        <td>1.70</td>
        <td>17.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Fiji</td>
        <td>4.16</td>
        <td>41.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Finlândia</td>
        <td>1.46</td>
        <td>14.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>França</td>
        <td>0.98</td>
        <td>9.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Guiana Francesa</td>
        <td>4.64</td>
        <td>46.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Polinésia Francesa</td>
        <td>4.53</td>
        <td>45.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Gabão</td>
        <td>6.64</td>
        <td>66.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Gâmbia</td>
        <td>4.18</td>
        <td>41.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Geórgia</td>
        <td>2.63</td>
        <td>26.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Alemanha</td>
        <td>1.88</td>
        <td>18.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Gana</td>
        <td>2.26</td>
        <td>22.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Gibraltar</td>
        <td>2.75</td>
        <td>27.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Grécia</td>
        <td>0.99</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Groenlândia</td>
        <td>1.03</td>
        <td>10.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Granada</td>
        <td>4.09</td>
        <td>40.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Guadalupe</td>
        <td>3.40</td>
        <td>34.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Guam</td>
        <td>1.73</td>
        <td>17.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Guatemala</td>
        <td>3.20</td>
        <td>32.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Guernsey</td>
        <td>0.87</td>
        <td>8.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Guiné</td>
        <td>3.82</td>
        <td>38.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Guiné-Bissau</td>
        <td>3.97</td>
        <td>39.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Guiana</td>
        <td>4.50</td>
        <td>45.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Haiti</td>
        <td>5.94</td>
        <td>59.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Honduras</td>
        <td>2.13</td>
        <td>21.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Hong Kong</td>
        <td>1.35</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Hungria</td>
        <td>1.91</td>
        <td>19.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Islândia</td>
        <td>1.75</td>
        <td>17.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Índia</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Indonésia</td>
        <td>6.63</td>
        <td>66.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Irã</td>
        <td>6.25</td>
        <td>62.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Iraque</td>
        <td>4.79</td>
        <td>47.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Irlanda</td>
        <td>1.31</td>
        <td>13.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Ilha de Man</td>
        <td>0.81</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Israel</td>
        <td>3.74</td>
        <td>37.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Itália</td>
        <td>0.78</td>
        <td>7.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Costa do Marfim</td>
        <td>2.48</td>
        <td>24.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Jamaica</td>
        <td>3.05</td>
        <td>30.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Japão</td>
        <td>1.02</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Jersey</td>
        <td>0.70</td>
        <td>7.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Jordânia</td>
        <td>5.56</td>
        <td>55.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Cazaquistão</td>
        <td>5.52</td>
        <td>55.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Quênia</td>
        <td>2.62</td>
        <td>26.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Kiribati</td>
        <td>3.67</td>
        <td>36.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Coreia do Sul</td>
        <td>0.69</td>
        <td>6.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Kosovo</td>
        <td>0.97</td>
        <td>9.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Kuwait</td>
        <td>3.34</td>
        <td>33.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Quirguistão</td>
        <td>6.12</td>
        <td>61.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Laos PDR</td>
        <td>1.54</td>
        <td>15.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Letônia</td>
        <td>1.80</td>
        <td>18.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Líbano</td>
        <td>3.07</td>
        <td>30.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Lesoto</td>
        <td>5.14</td>
        <td>51.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Libéria</td>
        <td>3.47</td>
        <td>34.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Líbia</td>
        <td>8.17</td>
        <td>81.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Liechtenstein</td>
        <td>0.84</td>
        <td>8.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Lituânia</td>
        <td>1.37</td>
        <td>13.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Luxemburgo</td>
        <td>1.86</td>
        <td>18.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Macau</td>
        <td>1.49</td>
        <td>14.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Macedônia</td>
        <td>1.88</td>
        <td>18.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Madagascar</td>
        <td>9.40</td>
        <td>94.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Malawi</td>
        <td>5.72</td>
        <td>57.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Malásia</td>
        <td>1.47</td>
        <td>14.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Maldivas</td>
        <td>1.80</td>
        <td>18.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Mali</td>
        <td>3.97</td>
        <td>39.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Malta</td>
        <td>1.64</td>
        <td>16.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Ilhas Marshall</td>
        <td>4.00</td>
        <td>40.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Martinica</td>
        <td>3.33</td>
        <td>33.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Mauritânia</td>
        <td>6.51</td>
        <td>65.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Ilhas Maurício</td>
        <td>4.02</td>
        <td>40.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Mayotte</td>
        <td>2.33</td>
        <td>23.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>México</td>
        <td>0.27</td>
        <td>2.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Micronésia</td>
        <td>1.85</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Moldávia</td>
        <td>1.59</td>
        <td>15.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Mônaco</td>
        <td>4.68</td>
        <td>46.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Mongólia</td>
        <td>7.03</td>
        <td>70.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Montenegro</td>
        <td>2.87</td>
        <td>28.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Montserrat</td>
        <td>2.77</td>
        <td>27.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Marrocos</td>
        <td>2.64</td>
        <td>26.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Moçambique</td>
        <td>2.76</td>
        <td>27.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Mianmar</td>
        <td>5.84</td>
        <td>58.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Namíbia</td>
        <td>1.58</td>
        <td>15.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Nauru</td>
        <td>1.12</td>
        <td>11.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Nepal</td>
        <td>3.82</td>
        <td>38.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Países Baixos</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Nova Caledônia</td>
        <td>4.44</td>
        <td>44.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Nova Zelândia</td>
        <td>1.92</td>
        <td>19.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Nicarágua</td>
        <td>1.95</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Níger</td>
        <td>7.49</td>
        <td>74.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Nigéria</td>
        <td>5.01</td>
        <td>50.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Niue</td>
        <td>4.86</td>
        <td>48.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Ilha Norfolk</td>
        <td>0.71</td>
        <td>7.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Macedônia do Norte</td>
        <td>0.34</td>
        <td>3.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Chipre do Norte</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Noruega</td>
        <td>1.05</td>
        <td>10.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Omã</td>
        <td>3.60</td>
        <td>36.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Paquistão</td>
        <td>7.46</td>
        <td>74.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Palau</td>
        <td>2.52</td>
        <td>25.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Território Palestino</td>
        <td>7.68</td>
        <td>76.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Panamá</td>
        <td>2.23</td>
        <td>22.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Papua-Nova Guiné</td>
        <td>19.01</td>
        <td>190.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Paraguai</td>
        <td>1.84</td>
        <td>18.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Peru</td>
        <td>0.81</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Filipinas</td>
        <td>0.28</td>
        <td>2.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Polônia</td>
        <td>0.52</td>
        <td>5.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Portugal</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Porto Rico</td>
        <td>1.06</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Catar</td>
        <td>0.52</td>
        <td>5.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Reunião/Mayotte</td>
        <td>4.82</td>
        <td>48.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Romênia</td>
        <td>1.06</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Rússia</td>
        <td>9.54</td>
        <td>95.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Ruanda</td>
        <td>4.66</td>
        <td>46.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>São Cristóvão e Neves</td>
        <td>0.92</td>
        <td>9.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Santa Lúcia</td>
        <td>1.07</td>
        <td>10.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>São Pedro e Miquelon</td>
        <td>2.31</td>
        <td>23.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>São Vicente e Granadinas</td>
        <td>1.06</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Samoa</td>
        <td>4.68</td>
        <td>46.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>San Marino</td>
        <td>2.76</td>
        <td>27.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>São Tomé e Príncipe</td>
        <td>3.29</td>
        <td>32.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Arábia Saudita</td>
        <td>1.91</td>
        <td>19.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Senegal</td>
        <td>5.15</td>
        <td>51.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Sérvia</td>
        <td>6.09</td>
        <td>60.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Ilhas Seychelles</td>
        <td>0.94</td>
        <td>9.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Serra Leoa</td>
        <td>4.73</td>
        <td>47.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Singapura</td>
        <td>0.70</td>
        <td>7.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>São Martinho</td>
        <td>0.16</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Eslováquia</td>
        <td>2.23</td>
        <td>22.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Eslovênia</td>
        <td>3.76</td>
        <td>37.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Ilhas Salomão</td>
        <td>2.09</td>
        <td>20.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Somália</td>
        <td>4.74</td>
        <td>47.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>África do Sul</td>
        <td>0.32</td>
        <td>3.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Ossétia do Sul</td>
        <td>2.05</td>
        <td>20.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Sudão do Sul</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Espanha</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Sri Lanka</td>
        <td>5.60</td>
        <td>56.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Sudão</td>
        <td>4.15</td>
        <td>41.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Suriname</td>
        <td>3.28</td>
        <td>32.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Essuatíni</td>
        <td>2.32</td>
        <td>23.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Suécia</td>
        <td>0.86</td>
        <td>8.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Suíça</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Síria</td>
        <td>7.86</td>
        <td>78.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Taiwan</td>
        <td>0.84</td>
        <td>8.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Tajiquistão</td>
        <td>11.35</td>
        <td>113.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Tanzânia</td>
        <td>5.38</td>
        <td>53.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Tailândia</td>
        <td>0.36</td>
        <td>3.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Timor-Leste</td>
        <td>2.86</td>
        <td>28.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Togo</td>
        <td>3.84</td>
        <td>38.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Tonga</td>
        <td>3.14</td>
        <td>31.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Trinidad e Tobago</td>
        <td>3.02</td>
        <td>30.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Tunísia</td>
        <td>7.06</td>
        <td>70.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Turquia</td>
        <td>0.77</td>
        <td>7.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Turcomenistão</td>
        <td>5.04</td>
        <td>50.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Ilhas Turks e Caicos</td>
        <td>3.38</td>
        <td>33.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Tuvalu</td>
        <td>3.36</td>
        <td>33.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Uganda</td>
        <td>4.05</td>
        <td>40.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Ucrânia</td>
        <td>2.86</td>
        <td>28.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Emirados Árabes Unidos</td>
        <td>1.24</td>
        <td>12.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Reino Unido</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Desconhecido</td>
        <td>3.92</td>
        <td>39.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Uruguai</td>
        <td>2.15</td>
        <td>21.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Uzbequistão</td>
        <td>6.88</td>
        <td>68.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Vanuatu</td>
        <td>4.18</td>
        <td>41.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Venezuela</td>
        <td>2.15</td>
        <td>21.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Vietnã</td>
        <td>3.05</td>
        <td>30.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Ilhas Virgens Britânicas</td>
        <td>4.73</td>
        <td>47.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Ilhas Virgens, U.S.</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Wallis e Futuna</td>
        <td>2.77</td>
        <td>27.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Iêmen</td>
        <td>6.03</td>
        <td>60.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Zâmbia</td>
        <td>6.76</td>
        <td>67.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Zimbábue</td>
        <td>3.55</td>
        <td>35.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação Argentina</td>
        <td>0.95</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Argentina – Marketing</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Argentina – Utilidade</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Brasil – Autenticação</td>
        <td>0.85</td>
        <td>8.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Brasil – Marketing</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Brasil – Utilidade</td>
        <td>0.21</td>
        <td>2.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação do Chile</td>
        <td>1.40</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Chile – Marketing</td>
        <td>2.35</td>
        <td>23.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Chile – Utilidade</td>
        <td>0.53</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação da Colômbia</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Colômbia – Marketing</td>
        <td>0.35</td>
        <td>3.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Colômbia – Utilidade</td>
        <td>0.01</td>
        <td>0.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação do Egito</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Marketing no Egito</td>
        <td>2.85</td>
        <td>28.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Egito – Utilidade</td>
        <td>0.14</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>França – Autenticação</td>
        <td>1.85</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>França – Marketing</td>
        <td>3.80</td>
        <td>38.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>França – Utilidade</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação da Alemanha</td>
        <td>2.05</td>
        <td>20.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Alemanha – Marketing</td>
        <td>3.60</td>
        <td>36.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Alemanha – Utilidade</td>
        <td>1.46</td>
        <td>14.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação da Índia</td>
        <td>0.04</td>
        <td>0.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação da Índia - Internacional</td>
        <td>0.74</td>
        <td>7.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Marketing na Índia</td>
        <td>0.25</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Índia – Utilidade</td>
        <td>0.04</td>
        <td>0.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação da Indonésia</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação da Indonésia - Internacional</td>
        <td>3.61</td>
        <td>36.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Profissionais de marketing da Indonésia</td>
        <td>1.10</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Indonésia – Utilidade</td>
        <td>0.55</td>
        <td>5.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação de Israel</td>
        <td>0.45</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Marketing em Israel</td>
        <td>0.95</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Israel – Utilidade</td>
        <td>0.14</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação da Itália</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Itália – Marketing</td>
        <td>1.85</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Itália – Utilidade</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Malásia – Autenticação</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Malásia – Marketing</td>
        <td>2.30</td>
        <td>23.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Malásia – Utilidade</td>
        <td>0.37</td>
        <td>3.70</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação do México</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Profissionais de marketing do México</td>
        <td>1.15</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>México – Utilidade</td>
        <td>0.27</td>
        <td>2.70</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação na Holanda</td>
        <td>1.90</td>
        <td>19.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Países Baixos – Marketing</td>
        <td>4.25</td>
        <td>42.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Países Baixos – Utilidade</td>
        <td>1.33</td>
        <td>13.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação da Nigéria</td>
        <td>0.75</td>
        <td>7.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Marketing na Nigéria</td>
        <td>1.35</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Nigéria – Utilidade</td>
        <td>0.18</td>
        <td>1.80</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação na América do Norte</td>
        <td>0.35</td>
        <td>3.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>América do Norte – Marketing</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>América do Norte – Utilidade</td>
        <td>0.11</td>
        <td>1.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Outra autenticação</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Outros – Marketing</td>
        <td>1.60</td>
        <td>16.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Outros serviços públicos</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação do Paquistão</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Marketing no Paquistão</td>
        <td>1.25</td>
        <td>12.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Paquistão – Utilidade</td>
        <td>0.14</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação do Peru</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Peru Marketing</td>
        <td>1.85</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Peru – Utilidade</td>
        <td>0.53</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação no resto da África</td>
        <td>0.40</td>
        <td>4.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Marketing para o resto da África</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Restante da África – Utilidade</td>
        <td>0.16</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Restante da Ásia-Pacífico – Autenticação</td>
        <td>1.15</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Restante da Ásia-Pacífico – Marketing</td>
        <td>1.95</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Restante da Ásia-Pacífico – Utilidade</td>
        <td>0.42</td>
        <td>4.20</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Restante da Europa Central e Oriental – Autenticação</td>
        <td>1.50</td>
        <td>15.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Restante da Europa Central e Oriental – Marketing</td>
        <td>2.30</td>
        <td>23.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Restante da Europa Central e Oriental – Utility</td>
        <td>0.94</td>
        <td>9.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Restante da América Latina – Autenticação</td>
        <td>1.20</td>
        <td>12.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Restante da América Latina – Marketing</td>
        <td>1.95</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Restante da América Latina – Utilidade</td>
        <td>0.30</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Restante do Oriente Médio – Autenticação</td>
        <td>0.45</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Restante do Oriente Médio – Marketing</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Restante do Oriente Médio – Utilidade</td>
        <td>0.42</td>
        <td>4.20</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Restante da Europa Ocidental – Autenticação</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Restante da Europa Ocidental – Marketing</td>
        <td>1.55</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Restante da Europa Ocidental – Utilidade</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação da Rússia</td>
        <td>1.15</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rússia – Marketing</td>
        <td>2.15</td>
        <td>21.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rússia – Utilidade</td>
        <td>1.06</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação da Arábia Saudita</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Marketing na Arábia Saudita</td>
        <td>1.10</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Arábia Saudita – Utilidade</td>
        <td>0.31</td>
        <td>3.10</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação da África do Sul</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Marketing na África do Sul</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>África do Sul – Utilidade</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação na Espanha</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Marketing na Espanha</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Espanha – Utilidade</td>
        <td>0.53</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação da Turquia</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Profissionais de marketing da Turquia</td>
        <td>0.30</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Turquia – Utilidade</td>
        <td>0.14</td>
        <td>1.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação dos Emirados Árabes Unidos</td>
        <td>0.45</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Emirados Árabes Unidos – Marketing</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Emirados Árabes Unidos – Utilidade</td>
        <td>0.42</td>
        <td>4.20</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Autenticação do Reino Unido</td>
        <td>0.95</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Reino Unido – Marketing</td>
        <td>1.40</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Reino Unido – Utilidade</td>
        <td>0.58</td>
        <td>5.80</td>
    </tr>
    <tr>
        <td>LINE</td>
        <td>1</td>
        <td>Todas as regiões</td>
        <td>0.15</td>
        <td>0.15</td>
    </tr>
    </tbody></table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% enddetails %}

------

## Detalhes do canal SMS/MMS

### Segmentos de SMS

Os segmentos de mensagens SMS são a forma como o setor de SMS conta as mensagens. Um segmento de mensagem é um agrupamento de até um número definido de caracteres (160 para codificação GSM-7; 67 para codificação UCS-2) que será enviado em um único envio de SMS. Se você enviar um SMS com 161 caracteres usando a codificação GSM-7, verá que há 2 (dois) segmentos de mensagens que foram enviados. O envio de vários segmentos de mensagens resultará em cobranças adicionais.

### Segmentos de MMS

Para MMS, o tamanho máximo das mensagens é de 5 MB (isso inclui o ativo multimídia e o tamanho do corpo da mensagem). Para ter mais segurança, a Braze sugere não ultrapassar 600 KB no seu arquivo multimídia, incluindo o corpo da mensagem.

## Detalhes do canal do WhatsApp

O WhatsApp é um canal focado no envio de mensagens bidirecionais e, portanto, se concentra nas conversas (em vez do número de mensagens individuais). Uma conversa é um fio condutor de 24 horas entre uma empresa e um usuário final.

### Definições de tipo de conversa

**Conversas sobre marketing:** Conversas iniciadas por empresas que ativam uma ampla gama de metas, desde a geração de conscientização até a condução de vendas e o redirecionamento de clientes. Os exemplos incluem anúncios de novos produtos, serviços ou recursos, promoções/ofertas direcionadas e lembretes de abandono de carrinho.

**Conversas sobre serviços públicos:** Conversas iniciadas pela empresa que ativam o acompanhamento das ações ou solicitações do usuário. Os exemplos incluem confirmação de aceitação, gerenciamento de pedido/entrega (e.g., atualização de entrega), atualizações ou alertas de conta (e.g., lembrete de pagamento) ou pesquisas de feedback.

**Conversas de autenticação:** Capacita a autenticação de usuários com senhas de uso único, potencialmente em várias etapas do processo de login (e.g., verificação de conta, recuperação de conta, desafios de integridade).

{% alert note %}
As conversas de autenticação somente serão suportadas caso a caso e a Braze não pode garantir SLAs específicos. Além disso, a Braze não oferece suporte à geração de PIN.
{% endalert %}

**Conversas sobre serviços:** Conversas iniciadas pelo usuário que são respondidas com uma mensagem não modelada.

{% alert note %}
A partir de 1º de novembro de 2024, as conversas do tipo serviço são gratuitas e não serão deduzidas das alocações de créditos comprados.
{% endalert %}

## Detalhamento da região de faturamento

#### América do Norte

Estados Unidos, Canadá

#### Resto da África

Argélia, Angola, Benin, Botsuana, Burkina Faso, Burundi, Camarões, Chade, Congo, Eritreia, Etiópia, Gabão, Gâmbia, Gana, Guiné-Bissau, Costa do Marfim, Quênia, Lesoto, Libéria, Líbia,
Madagascar, Malawi, Mali, Mauritânia, Marrocos, Moçambique, Namíbia, Níger, Ruanda, Senegal, Serra Leoa, Somália, Sudão do Sul, Sudão, Suazilândia, Tanzânia, Togo, Tunísia, Uganda, Zâmbia

#### Resto da Ásia-Pacífico

Afeganistão, Austrália, Bangladesh, Camboja, China, Hong Kong, Japão, Laos, Mongólia, Nepal, Nova Zelândia, Papua Nova Guiné, Filipinas, Cingapura, Sri Lanka, Taiwan, Tajiquistão e Tailândia,
Turcomenistão, Uzbequistão, Vietnã

#### Restante da Europa Central e Oriental

Albânia, Armênia, Azerbaijão, Belarus, Bulgária, Croácia, República Tcheca, Geórgia, Grécia, Hungria, Letônia, Lituânia, Macedônia, Moldávia, Polônia, Romênia, Sérvia, Eslováquia, Eslovênia, Ucrânia

#### Resto da América Latina

Bolívia, Costa Rica, República Dominicana, Equador, El Salvador,
Guatemala, Haiti, Honduras, Jamaica, Nicarágua, Panamá, Paraguai, Porto Rico, Uruguai, Venezuela

#### Resto do Oriente Médio

Bahrein, Iraque, Jordânia, Kuwait, Líbano, Omã, Catar, Iêmen

#### Restante da Europa Ocidental

Áustria, Bélgica, Dinamarca, Finlândia, Irlanda, Noruega, Portugal, Suécia, Suíça
