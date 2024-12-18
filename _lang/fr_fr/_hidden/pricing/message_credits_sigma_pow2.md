---
nav_title: Crédits des messages - Sigma
permalink: "/message_credits_sigma_pow2/"
hidden: true
noindex: true
hide_toc: true
---

# Crédits des messages - Sigma (confidentiel)

> Crédits des messages correspond à la structure de packaging cross-canal de Braze pour nos offres natives de SMS, MMS et WhatsApp. Les crédits de message offrent une expérience flexible et transparente lorsque vous tirez parti des canaux d'envoi de messages de Braze. Les crédits vous donnent accès à n'importe laquelle des chaînes présentées dans le tableau de cette page.

{% alert note %}
Les unités de mesure utilisées dans les rapports varient d'un canal à l'autre.<br><br>
<b>WhatsApp :</b> Conversations<br>
<b>SMS :</b> Segments<br>
<b>MMS :</b> Segments<br><br>
En d'autres termes, les crédits par messages WhatsApp seront calculés sur les initiations de conversation, et les crédits par pour les messages SMS et MMS seront calculés sur les segments envoyés.
<br><br>
Enfin, les frais d’opérateur sont facturés séparément (à terme échu) et ne sont pas pris en compte dans l'unité de gestion des stocks des crédits de messages.
{% endalert %}

## Définitions

Les définitions des colonnes sont les suivantes :

|---------|-------------------------------------------------|
| **Ratio de crédit du canal** | Montant de référence pour chaque canal |
| **Destination** | Région finale spécifique, pays ou type de message envoyé par l'intermédiaire de la plateforme Braze |
| **Multiplicateur** | Échelle du ratio de crédits des canaux, en fonction de la tarification de la destination spécifique |
| **Crédits pour 1 envoi** | Nombre exact de crédits de messages pour l'envoi d'un message<br> (crédits par message = taux de crédit du canal x multiplicateur de destination) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


## Tableau de ratio de crédit pour les envois de messages - Sigma

{% details Cliquez pour agrandir %}
<table>
    <colgroup>
        <col span="4" style="background-color:background-color:#FFFFFF;">
        <col style="background-color:#f0f0f5">
    </colgroup>
    <tr>
        <th><b>Canal</b></th>
        <th><b>Ratio de crédit du canal</b></th>
        <th><b>Destination</b></th>
        <th><b>Multiplicateur</b></th>
        <th class="credits-column"><b>Crédits pour 1 envoi</b></th>
    </tr>
    <tbody><tr>
        <td>SMS - États-Unis / CA</td>
        <td>1</td>
        <td>États-Unis</td>
        <td>1.00</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>SMS - États-Unis / CA</td>
        <td>1</td>
        <td>États-Unis Sans frais</td>
        <td>1.50</td>
        <td>1.50</td>
    </tr>
    <tr>
        <td>SMS - États-Unis / CA</td>
        <td>1</td>
        <td>Canada</td>
        <td>1.00</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>SMS - États-Unis / CA</td>
        <td>1</td>
        <td>Numéro gratuit Canada</td>
        <td>1.30</td>
        <td>1.30</td>
    </tr>
    <tr>
        <td>MMS - États-Unis / CA</td>
        <td>3</td>
        <td>États-Unis</td>
        <td>1.00</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>MMS - États-Unis / CA</td>
        <td>3</td>
        <td>États-Unis Sans frais</td>
        <td>2.00</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>MMS - États-Unis / CA</td>
        <td>3</td>
        <td>Code long du Canada</td>
        <td>1.50</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>MMS - États-Unis / CA</td>
        <td>3</td>
        <td>Code court Canada</td>
        <td>4.00</td>
        <td>12.00</td>
    </tr>
    <tr>
        <td>MMS - États-Unis / CA</td>
        <td>3</td>
        <td>Numéro gratuit Canada</td>
        <td>1.30</td>
        <td>3.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Abkhazie</td>
        <td>0.62</td>
        <td>4.65</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Afghanistan</td>
        <td>9.47</td>
        <td>71.03</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Albanie</td>
        <td>2.29</td>
        <td>17.18</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Algérie</td>
        <td>5.23</td>
        <td>39.23</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Samoa américaines</td>
        <td>4.74</td>
        <td>35.55</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Andorre</td>
        <td>3.32</td>
        <td>24.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Angola</td>
        <td>2.24</td>
        <td>16.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Anguilla</td>
        <td>3.33</td>
        <td>24.98</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Antigua-et-Barbuda</td>
        <td>2.47</td>
        <td>18.53</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Argentine</td>
        <td>1.02</td>
        <td>7.65</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Arménie</td>
        <td>3.49</td>
        <td>26.18</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Aruba</td>
        <td>2.61</td>
        <td>19.58</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Australie SMS</td>
        <td>0.36</td>
        <td>2.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Australie MMS</td>
        <td>3.10</td>
        <td>23.25</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Autriche</td>
        <td>1.77</td>
        <td>13.28</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Azerbaïdjan</td>
        <td>9.77</td>
        <td>73.28</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Bahamas</td>
        <td>1.23</td>
        <td>9.23</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Bahreïn</td>
        <td>0.92</td>
        <td>6.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Bengladesh</td>
        <td>5.81</td>
        <td>43.58</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Barbade</td>
        <td>3.09</td>
        <td>23.18</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Biélorussie</td>
        <td>6.35</td>
        <td>47.63</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Belgique</td>
        <td>2.40</td>
        <td>18.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Belize</td>
        <td>6.90</td>
        <td>51.75</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Bénin</td>
        <td>3.64</td>
        <td>27.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Bermudes</td>
        <td>2.99</td>
        <td>22.43</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Bhoutan</td>
        <td>10.10</td>
        <td>75.75</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Bolivie</td>
        <td>3.66</td>
        <td>27.45</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Bosnie-Herzégovine</td>
        <td>2.12</td>
        <td>15.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Botswana</td>
        <td>2.52</td>
        <td>18.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Brésil</td>
        <td>0.25</td>
        <td>1.88</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Brunei</td>
        <td>0.50</td>
        <td>3.75</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Bulgarie</td>
        <td>2.70</td>
        <td>20.25</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Burkina Faso</td>
        <td>3.35</td>
        <td>25.13</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Burundi</td>
        <td>9.47</td>
        <td>71.03</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Cambodge</td>
        <td>4.30</td>
        <td>32.25</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Cameroun</td>
        <td>3.49</td>
        <td>26.18</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Cap-Vert</td>
        <td>3.66</td>
        <td>27.45</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Pays-Bas caribéens</td>
        <td>2.17</td>
        <td>16.28</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Îles Caïmans</td>
        <td>3.37</td>
        <td>25.28</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>République centrafricaine</td>
        <td>3.07</td>
        <td>23.03</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Tchad</td>
        <td>7.30</td>
        <td>54.75</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Chili</td>
        <td>1.64</td>
        <td>12.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Chine</td>
        <td>0.64</td>
        <td>4.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Colombie</td>
        <td>0.02</td>
        <td>0.15</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Comores</td>
        <td>6.19</td>
        <td>46.43</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Congo</td>
        <td>5.04</td>
        <td>37.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Îles Cook</td>
        <td>3.52</td>
        <td>26.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Costa Rica</td>
        <td>1.06</td>
        <td>7.95</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Croatie</td>
        <td>2.31</td>
        <td>17.33</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Cuba</td>
        <td>2.12</td>
        <td>15.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Curaçao</td>
        <td>0.99</td>
        <td>7.43</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Chypre</td>
        <td>2.18</td>
        <td>16.35</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>République tchèque</td>
        <td>1.01</td>
        <td>7.58</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Danemark</td>
        <td>1.01</td>
        <td>7.58</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Djibouti</td>
        <td>4.09</td>
        <td>30.68</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Dominique</td>
        <td>3.79</td>
        <td>28.43</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>République dominicaine</td>
        <td>1.29</td>
        <td>9.68</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>RD Congo</td>
        <td>5.77</td>
        <td>43.28</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Équateur</td>
        <td>2.76</td>
        <td>20.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Égypte</td>
        <td>2.43</td>
        <td>18.23</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>El Salvador</td>
        <td>2.45</td>
        <td>18.38</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Guinée équatoriale</td>
        <td>4.36</td>
        <td>32.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Érythrée</td>
        <td>2.48</td>
        <td>18.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Estonie</td>
        <td>2.41</td>
        <td>18.08</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Eswatini</td>
        <td>0.58</td>
        <td>4.35</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Éthiopie</td>
        <td>8.63</td>
        <td>64.73</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Îles Falkland</td>
        <td>3.43</td>
        <td>25.73</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Îles Féroé</td>
        <td>1.70</td>
        <td>12.75</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Fiji</td>
        <td>4.16</td>
        <td>31.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Finlande</td>
        <td>1.46</td>
        <td>10.95</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>France</td>
        <td>0.98</td>
        <td>7.35</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Guinée française</td>
        <td>4.64</td>
        <td>34.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Polynésie française</td>
        <td>4.53</td>
        <td>33.98</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Gabon</td>
        <td>6.64</td>
        <td>49.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Gambie</td>
        <td>4.18</td>
        <td>31.35</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Géorgie</td>
        <td>2.63</td>
        <td>19.73</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Allemagne</td>
        <td>1.88</td>
        <td>14.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Ghana</td>
        <td>2.26</td>
        <td>16.95</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Gibraltar</td>
        <td>2.75</td>
        <td>20.63</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Grèce</td>
        <td>0.99</td>
        <td>7.43</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Groenland</td>
        <td>1.03</td>
        <td>7.73</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Grenade</td>
        <td>4.09</td>
        <td>30.68</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Guadeloupe</td>
        <td>3.40</td>
        <td>25.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Guam</td>
        <td>1.73</td>
        <td>12.98</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Guatemala</td>
        <td>3.20</td>
        <td>24.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Guernesey</td>
        <td>0.87</td>
        <td>6.53</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Guinée</td>
        <td>3.82</td>
        <td>28.65</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Guinée-Bissau</td>
        <td>3.97</td>
        <td>29.78</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Guyane</td>
        <td>4.50</td>
        <td>33.75</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Haïti</td>
        <td>5.94</td>
        <td>44.55</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Honduras</td>
        <td>2.13</td>
        <td>15.98</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Hong Kong</td>
        <td>1.35</td>
        <td>10.13</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Hongrie</td>
        <td>1.91</td>
        <td>14.33</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Islande</td>
        <td>1.75</td>
        <td>13.13</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Inde</td>
        <td>1.00</td>
        <td>7.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Indonésie</td>
        <td>6.63</td>
        <td>49.73</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Iran</td>
        <td>6.25</td>
        <td>46.88</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Iraq</td>
        <td>4.79</td>
        <td>35.93</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Irlande</td>
        <td>1.31</td>
        <td>9.83</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Île de Man</td>
        <td>0.81</td>
        <td>6.08</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Israël</td>
        <td>3.74</td>
        <td>28.05</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Italie</td>
        <td>0.78</td>
        <td>5.85</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Côte d'Ivoire</td>
        <td>2.48</td>
        <td>18.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Jamaïque</td>
        <td>3.05</td>
        <td>22.88</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Japon</td>
        <td>1.02</td>
        <td>7.65</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Jersey</td>
        <td>0.70</td>
        <td>5.25</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Jordanie</td>
        <td>5.56</td>
        <td>41.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Kazakhstan</td>
        <td>5.52</td>
        <td>41.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Kenya</td>
        <td>2.62</td>
        <td>19.65</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Kiribati</td>
        <td>3.67</td>
        <td>27.53</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>République de Corée</td>
        <td>0.69</td>
        <td>5.18</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Kosovo</td>
        <td>0.97</td>
        <td>7.28</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Koweït</td>
        <td>3.34</td>
        <td>25.05</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Kirghizistan</td>
        <td>6.12</td>
        <td>45.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>RDP Laos</td>
        <td>1.54</td>
        <td>11.55</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Lettonie</td>
        <td>1.80</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Liban</td>
        <td>3.07</td>
        <td>23.03</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Lesotho</td>
        <td>5.14</td>
        <td>38.55</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Liberia</td>
        <td>3.47</td>
        <td>26.03</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Lybie</td>
        <td>8.17</td>
        <td>61.28</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Liechtenstein</td>
        <td>0.84</td>
        <td>6.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Lituanie</td>
        <td>1.37</td>
        <td>10.28</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Luxembourg</td>
        <td>1.86</td>
        <td>13.95</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Macao</td>
        <td>1.49</td>
        <td>11.18</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Macédoine</td>
        <td>1.88</td>
        <td>14.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Madagascar</td>
        <td>9.40</td>
        <td>70.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Malawi</td>
        <td>5.72</td>
        <td>42.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Malaisie</td>
        <td>1.47</td>
        <td>11.03</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Maldives</td>
        <td>1.80</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Mali</td>
        <td>3.97</td>
        <td>29.78</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Malte</td>
        <td>1.64</td>
        <td>12.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Îles Marshall</td>
        <td>4.00</td>
        <td>30.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Martinique</td>
        <td>3.33</td>
        <td>24.98</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Mauritanie</td>
        <td>6.51</td>
        <td>48.83</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Maurice</td>
        <td>4.02</td>
        <td>30.15</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Mayotte</td>
        <td>2.33</td>
        <td>17.48</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Mexique</td>
        <td>0.27</td>
        <td>2.03</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Micronésie</td>
        <td>1.85</td>
        <td>13.88</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Moldavie</td>
        <td>1.59</td>
        <td>11.93</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Monaco</td>
        <td>4.68</td>
        <td>35.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Mongolie</td>
        <td>7.03</td>
        <td>52.73</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Monténégro</td>
        <td>2.87</td>
        <td>21.53</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Montserrat</td>
        <td>2.77</td>
        <td>20.78</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Maroc</td>
        <td>2.64</td>
        <td>19.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Mozambique</td>
        <td>2.76</td>
        <td>20.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Birmanie</td>
        <td>5.84</td>
        <td>43.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Namibie</td>
        <td>1.58</td>
        <td>11.85</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Nauru</td>
        <td>1.12</td>
        <td>8.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Népal</td>
        <td>3.82</td>
        <td>28.65</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Pays-Bas</td>
        <td>1.65</td>
        <td>12.38</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Nouvelle-Calédonie</td>
        <td>4.44</td>
        <td>33.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Nouvelle-Zélande</td>
        <td>1.92</td>
        <td>14.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Nicaragua</td>
        <td>1.95</td>
        <td>14.63</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Niger</td>
        <td>7.49</td>
        <td>56.18</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Nigéria</td>
        <td>5.01</td>
        <td>37.58</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Niue</td>
        <td>4.86</td>
        <td>36.45</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Île Norfolk Island</td>
        <td>0.71</td>
        <td>5.33</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Macédoine du Nord</td>
        <td>0.34</td>
        <td>2.55</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Chypre du Nord</td>
        <td>0.20</td>
        <td>1.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Norvège</td>
        <td>1.05</td>
        <td>7.88</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Oman</td>
        <td>3.60</td>
        <td>27.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Pakistan</td>
        <td>7.46</td>
        <td>55.95</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Palaos</td>
        <td>2.52</td>
        <td>18.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Territoire palestinien</td>
        <td>7.68</td>
        <td>57.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Panama</td>
        <td>2.23</td>
        <td>16.73</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Papouasie-Nouvelle-Guinée</td>
        <td>19.01</td>
        <td>142.58</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Paraguay</td>
        <td>1.84</td>
        <td>13.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Pérou</td>
        <td>0.81</td>
        <td>6.08</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Philippines</td>
        <td>0.28</td>
        <td>2.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Pologne</td>
        <td>0.52</td>
        <td>3.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Portugal</td>
        <td>0.60</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Porto Rico</td>
        <td>1.06</td>
        <td>7.95</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Qatar</td>
        <td>0.52</td>
        <td>3.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Réunion/Mayotte</td>
        <td>4.82</td>
        <td>36.15</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Roumanie</td>
        <td>1.06</td>
        <td>7.95</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Russie</td>
        <td>9.54</td>
        <td>71.55</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Rwanda</td>
        <td>4.66</td>
        <td>34.95</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Saint-Christophe-et-Niévès</td>
        <td>0.92</td>
        <td>6.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Sainte-Lucie</td>
        <td>1.07</td>
        <td>8.03</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Saint-Pierre-et-Miquelon</td>
        <td>2.31</td>
        <td>17.33</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Saint-Vincent-et-les-Grenadines</td>
        <td>1.06</td>
        <td>7.95</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Samoa</td>
        <td>4.68</td>
        <td>35.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Saint-Marin</td>
        <td>2.76</td>
        <td>20.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Sao Tomé-et-Principe</td>
        <td>3.29</td>
        <td>24.68</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Arabie saoudite</td>
        <td>1.91</td>
        <td>14.33</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Sénégal</td>
        <td>5.15</td>
        <td>38.63</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Serbie</td>
        <td>6.09</td>
        <td>45.68</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Seychelles</td>
        <td>0.94</td>
        <td>7.05</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Sierra Leone</td>
        <td>4.73</td>
        <td>35.48</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Singapour</td>
        <td>0.70</td>
        <td>5.25</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Saint-Martin (Pays-Bas)</td>
        <td>0.16</td>
        <td>1.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Slovaquie</td>
        <td>2.23</td>
        <td>16.73</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Slovénie</td>
        <td>3.76</td>
        <td>28.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Îles Salomon</td>
        <td>2.09</td>
        <td>15.68</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Somalie</td>
        <td>4.74</td>
        <td>35.55</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Afrique du Sud</td>
        <td>0.32</td>
        <td>2.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Ossétie du Sud</td>
        <td>2.05</td>
        <td>15.38</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Soudan du Sud</td>
        <td>0.80</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Espagne</td>
        <td>0.80</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Sri Lanka</td>
        <td>5.60</td>
        <td>42.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Soudan</td>
        <td>4.15</td>
        <td>31.13</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Suriname</td>
        <td>3.28</td>
        <td>24.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Swaziland</td>
        <td>2.32</td>
        <td>17.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Suède</td>
        <td>0.86</td>
        <td>6.45</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Suisse</td>
        <td>0.60</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Syrie</td>
        <td>7.86</td>
        <td>58.95</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Taiwan</td>
        <td>0.84</td>
        <td>6.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Tadjikistan</td>
        <td>11.35</td>
        <td>85.13</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Tanzanie</td>
        <td>5.38</td>
        <td>40.35</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Thaïlande</td>
        <td>0.36</td>
        <td>2.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Timor oriental</td>
        <td>2.86</td>
        <td>21.45</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Togo</td>
        <td>3.84</td>
        <td>28.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Tonga</td>
        <td>3.14</td>
        <td>23.55</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Trinité-et-Tobago</td>
        <td>3.02</td>
        <td>22.65</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Tunisie</td>
        <td>7.06</td>
        <td>52.95</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Turquie</td>
        <td>0.77</td>
        <td>5.78</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Turkménistan</td>
        <td>5.04</td>
        <td>37.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Îles Turks et Caïques</td>
        <td>3.38</td>
        <td>25.35</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Tuvalu</td>
        <td>3.36</td>
        <td>25.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Ouganda</td>
        <td>4.05</td>
        <td>30.38</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Ukraine</td>
        <td>2.86</td>
        <td>21.45</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Émirats arabes unis</td>
        <td>1.24</td>
        <td>9.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Royaume-Uni</td>
        <td>0.65</td>
        <td>4.88</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Inconnu</td>
        <td>3.92</td>
        <td>29.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Uruguay</td>
        <td>2.15</td>
        <td>16.13</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Ouzbékistan</td>
        <td>6.88</td>
        <td>51.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Vanuatu</td>
        <td>4.18</td>
        <td>31.35</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Venezuela</td>
        <td>2.15</td>
        <td>16.13</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Vietnam</td>
        <td>3.05</td>
        <td>22.88</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Îles Vierges britanniques</td>
        <td>4.73</td>
        <td>35.48</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Îles Vierges, U.S.</td>
        <td>0.50</td>
        <td>3.75</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Wallis-et-Futuna</td>
        <td>2.77</td>
        <td>20.78</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Yémen</td>
        <td>6.03</td>
        <td>45.23</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Zambie</td>
        <td>6.76</td>
        <td>50.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>7.5</td>
        <td>Zimbabwe</td>
        <td>3.55</td>
        <td>26.63</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification de l'Argentine</td>
        <td>0.95</td>
        <td>7.13</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing en Argentine</td>
        <td>1.65</td>
        <td>12.38</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Argentine</td>
        <td>0.90</td>
        <td>6.75</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification du Brésil</td>
        <td>0.85</td>
        <td>6.38</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing Brésil</td>
        <td>1.65</td>
        <td>12.38</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Brésil</td>
        <td>0.21</td>
        <td>1.58</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification du Chili</td>
        <td>1.40</td>
        <td>10.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing au Chili</td>
        <td>2.35</td>
        <td>17.63</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Chili</td>
        <td>0.53</td>
        <td>3.98</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification de la Colombie</td>
        <td>0.20</td>
        <td>1.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing en Colombie</td>
        <td>0.35</td>
        <td>2.63</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Colombie</td>
        <td>0.01</td>
        <td>0.08</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification de l'Égypte</td>
        <td>1.65</td>
        <td>12.38</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing en Égypte</td>
        <td>2.85</td>
        <td>21.38</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Égypte</td>
        <td>0.14</td>
        <td>1.05</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification France</td>
        <td>1.85</td>
        <td>13.88</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing France</td>
        <td>3.80</td>
        <td>28.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire France</td>
        <td>0.80</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification Allemagne</td>
        <td>2.05</td>
        <td>15.38</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing Allemagne</td>
        <td>3.60</td>
        <td>27.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Allemagne</td>
        <td>1.46</td>
        <td>10.95</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification de l'Inde</td>
        <td>0.04</td>
        <td>0.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification de l'Inde - International</td>
        <td>0.74</td>
        <td>5.55</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing Inde</td>
        <td>0.25</td>
        <td>1.88</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Inde</td>
        <td>0.04</td>
        <td>0.30</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification de l'Indonésie</td>
        <td>0.80</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification de l'Indonésie - International</td>
        <td>3.61</td>
        <td>27.08</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing Indonésie</td>
        <td>1.10</td>
        <td>8.25</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Indonésie</td>
        <td>0.55</td>
        <td>4.13</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification d'Israël</td>
        <td>0.45</td>
        <td>3.38</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing en Israël</td>
        <td>0.95</td>
        <td>7.13</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Israël</td>
        <td>0.14</td>
        <td>1.05</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification Italie</td>
        <td>1.00</td>
        <td>7.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing Italie</td>
        <td>1.85</td>
        <td>13.88</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Italie</td>
        <td>0.80</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification Malaisie</td>
        <td>0.50</td>
        <td>3.75</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing Malaisie</td>
        <td>2.30</td>
        <td>17.25</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Malaisie</td>
        <td>0.37</td>
        <td>2.78</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification du Mexique</td>
        <td>0.65</td>
        <td>4.88</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing au Mexique</td>
        <td>1.15</td>
        <td>8.63</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Mexique</td>
        <td>0.27</td>
        <td>2.03</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification des Pays-Bas</td>
        <td>1.90</td>
        <td>14.25</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing Pays-Bas</td>
        <td>4.25</td>
        <td>31.88</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Pays-Bas</td>
        <td>1.33</td>
        <td>9.98</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification du Nigeria</td>
        <td>0.75</td>
        <td>5.63</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing au Nigeria</td>
        <td>1.35</td>
        <td>10.13</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Nigeria</td>
        <td>0.18</td>
        <td>1.35</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification Amérique du Nord</td>
        <td>0.35</td>
        <td>2.63</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing pour l'Amérique du Nord</td>
        <td>0.65</td>
        <td>4.88</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Amérique du Nord</td>
        <td>0.11</td>
        <td>0.83</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Autre authentification</td>
        <td>0.80</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Autres marketing</td>
        <td>1.60</td>
        <td>12.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Autres</td>
        <td>0.20</td>
        <td>1.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification du Pakistan</td>
        <td>0.60</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing au Pakistan</td>
        <td>1.25</td>
        <td>9.38</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Pakistan</td>
        <td>0.14</td>
        <td>1.05</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification du Pérou</td>
        <td>1.00</td>
        <td>7.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing au Pérou</td>
        <td>1.85</td>
        <td>13.88</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Pérou</td>
        <td>0.53</td>
        <td>3.98</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification pour le reste de l'Afrique</td>
        <td>0.40</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing pour le reste de l'Afrique</td>
        <td>0.60</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Reste de l'Afrique</td>
        <td>0.16</td>
        <td>1.20</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification Reste de l'Asie-Pacifique</td>
        <td>1.15</td>
        <td>8.63</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing dans le reste de l'Asie-Pacifique</td>
        <td>1.95</td>
        <td>14.63</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Reste de l'Asie-Pacifique</td>
        <td>0.42</td>
        <td>3.15</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification Reste de l'Europe centrale et de l’Est</td>
        <td>1.50</td>
        <td>11.25</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing Reste de l'Europe centrale et de l’Est</td>
        <td>2.30</td>
        <td>17.25</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Reste de l'Europe centrale et de l’Est</td>
        <td>0.94</td>
        <td>7.05</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification Reste de l'Amérique latine</td>
        <td>1.20</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing Reste de l'Amérique latine</td>
        <td>1.95</td>
        <td>14.63</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Reste de l'Amérique latine</td>
        <td>0.30</td>
        <td>2.25</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification Reste du Moyen-Orient</td>
        <td>0.45</td>
        <td>3.38</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing pour le reste du Moyen-Orient</td>
        <td>0.90</td>
        <td>6.75</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Reste du Moyen-Orient</td>
        <td>0.42</td>
        <td>3.15</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification Reste de l'Europe occidentale</td>
        <td>1.00</td>
        <td>7.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing Reste de l'Europe occidentale</td>
        <td>1.55</td>
        <td>11.63</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Reste de l'Europe occidentale</td>
        <td>0.80</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification de la Russie</td>
        <td>1.15</td>
        <td>8.63</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing Russie</td>
        <td>2.15</td>
        <td>16.13</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Russie</td>
        <td>1.06</td>
        <td>7.95</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification Arabie Saoudite</td>
        <td>0.60</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing Arabie Saoudite</td>
        <td>1.10</td>
        <td>8.25</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Arabie Saoudite</td>
        <td>0.31</td>
        <td>2.33</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification Afrique du Sud</td>
        <td>0.50</td>
        <td>3.75</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing Afrique du Sud</td>
        <td>1.00</td>
        <td>7.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Afrique du Sud</td>
        <td>0.20</td>
        <td>1.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification Espagne</td>
        <td>0.90</td>
        <td>6.75</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing Espagne</td>
        <td>1.65</td>
        <td>12.38</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Espagne</td>
        <td>0.53</td>
        <td>3.98</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification de la Turquie</td>
        <td>0.20</td>
        <td>1.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing de la Turquie</td>
        <td>0.30</td>
        <td>2.25</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Turquie</td>
        <td>0.14</td>
        <td>1.05</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification Émirats Arabes Unis</td>
        <td>0.45</td>
        <td>3.38</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing Émirats Arabes Unis</td>
        <td>0.90</td>
        <td>6.75</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Émirats Arabes Unis</td>
        <td>0.42</td>
        <td>3.15</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Authentification Royaume-Uni</td>
        <td>0.95</td>
        <td>7.13</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Marketing Royaume-Uni</td>
        <td>1.40</td>
        <td>10.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>7.5</td>
        <td>Utilitaire Royaume-Uni</td>
        <td>0.58</td>
        <td>4.35</td>
    </tr>
    <tr>
        <td>LINE</td>
        <td>1</td>
        <td>Toutes les régions</td>
        <td>0.15</td>
        <td>0.15</td>
    </tr>
    </tbody></table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% enddetails %}

------

## Détails du canal SMS/MMS

### Segments de SMS

Les segments de messages SMS sont la manière dont les messages de l’industrie SMS sont envoyés. Un segment de message est un groupement allant jusqu’à un nombre défini de caractères (160 pour le codage GSM-7 ; 67 pour le codage UCS-2) qui sera envoyé dans une seule distribution par SMS. Si vous envoyez un SMS avec 161 caractères à l’aide du codage GSM-7, vous verrez qu’il y a deux (2) segments de messages envoyés. L'envoi de plusieurs segments de messages entraîne des frais supplémentaires.

### Segments MMS

Pour les MMS, la limite des messages est de 5 Mo (ceci inclut la ressource multimédia et la taille du corps du message). Pour plus de sécurité, Braze recommande de ne pas dépasser 600 Ko pour votre ressource multimédia et le corps de message.

## Détails du canal WhatsApp

WhatsApp est un canal de communication axé sur l'envoi de messages dans les deux sens, et donc sur les conversations (plutôt que sur le nombre de messages individuels). Une conversation est un fil de discussion de 24 heures entre une entreprise et un utilisateur final.

### Définitions des types de conversation

**Conversations marketing :** Des conversations initiées par l’entreprise qui vous permettent d'atteindre un large éventail d'objectifs, de la sensibilisation à la stimulation des ventes, en passant par le reciblage des clients. Il peut s'agir, par exemple, d'annonces de nouveaux produits, services ou fonctionnalités, de promotions/offres ciblées ou de rappels en cas d'abandon de panier.

**Conversations utilitaires :** Conversations initiées par l'entreprise qui vous permettent d'assurer le suivi des actions ou des demandes des utilisateurs. Il peut s'agir par exemple de la confirmation d'un abonnement, de la gestion d'une commande ou d'une livraison (e.g., informations sur une livraison), d’informations ou d’alertes sur les comptes (e.g., rappel de paiement) ou encore d'une enquête de satisfaction.

**Conversations d'authentification :** Vous permettent d’authentifier les utilisateurs avec des codes d’accès à usage unique, potentiellement à plusieurs étapes, lors du processus de connexion (e.g, vérification de compte, récupération de compte, défis d’intégrité).

{% alert note %}
Les conversations d’authentification seront prises en charge au cas par cas et Braze ne peut pas garantir des SLA spécifiques. En outre, Braze ne prend pas en charge la génération de codes PIN.
{% endalert %}

**Conversations de service :** Conversations initiées par l'utilisateur auxquelles il est répondu par un message non modélisé.

{% alert note %}
À partir du 1er novembre 2024, les conversations de type service sont gratuites et ne viendront pas en déduction des attributions de crédits achetés.
{% endalert %}

## Répartition par région de facturation

#### Amérique du Nord

États-Unis, Canada

#### Reste de l’Afrique

Algérie, Angola, Bénin, Botswana, Burkina Faso, Burundi, Cameroun, Tchad, Congo, Érythrée, Éthiopie, Gabon, Gambie, Ghana, Guinée-Bissau, Côte d'Ivoire, Kenya, Lesotho, Libéria, Libye,
Madagascar, Malawi, Mali, Maroc, Mauritanie, Mozambique, Namibie, Niger, Rwanda, Sénégal, Sierra Leone, Somalie, Soudan du Sud, Soudan, Swaziland, Tanzanie, Togo, Tunisie, Ouganda, Zambie

#### Reste de l’Asie-Pacifique

Afghanistan, Australie, Bangladesh, Cambodge, Chine, Hong Kong, Japon, Laos, Mongolie, Népal, Nouvelle-Zélande, Papouasie-Nouvelle-Guinée, Philippines, Singapour, Sri Lanka, Taïwan, Tadjikistan, Thaïlande,
Turkménistan, Ouzbékistan, Vietnam

#### Reste de l’Europe centrale et de l’Est

Albanie, Arménie, Azerbaïdjan, Biélorussie, Bulgarie, Croatie, République tchèque, Géorgie, Grèce, Hongrie, Lettonie, Lituanie, Macédoine, Moldavie, Pologne, Roumanie, Serbie, Slovaquie, Slovénie, Ukraine

#### Reste de l’Amérique latine

Bolivie, Costa Rica, République dominicaine, Équateur, Salvador,
Guatemala, Haïti, Honduras, Jamaïque, Nicaragua, Panama, Paraguay, Porto Rico, Uruguay, Venezuela

#### Reste du Moyen-Orient

Bahreïn, Irak, Jordanie, Koweït, Liban, Oman, Qatar, Yémen

#### Reste de l’Europe occidentale

Autriche, Belgique, Danemark, Finlande, Irlande, Norvège, Portugal, Suède, Suisse
