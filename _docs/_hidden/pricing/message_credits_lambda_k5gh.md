---
nav_title: Message Credits - Lambda
permalink: "/message_credits_lambda_k5gh/"
hidden: true
noindex: true
hide_toc: true
---

# Message Credits - Lambda (Confidential)

> Message Credits is Braze’s cross-channel packaging structure for our native SMS, MMS, and WhatsApp offerings. We use Message Credits to provide a flexible and transparent experience when taking advantage of Braze messaging channels. You may use the allotment of credits purchased across any of the channels presented in the table on this page.

{% alert note %}
Different channels will have different units of measure in reporting.<br><br>
<b>WhatsApp:</b> Conversations<br>
<b>SMS:</b> Segments<br>
<b>MMS:</b> Segments<br><br>
In other words, credits used for WhatsApp messages will be calculated on conversation initiations, and credits used for both SMS and MMS messages will be calculated on segments sent.
<br><br>
Lastly, carrier fees are billed separately (in arrears) and are not considered as part of this Message Credits SKU.
{% endalert %}

## Definitions

Column definitions are as follows:

|---------|-------------------------------------------------|
| **Channel Credit Ratio** | Baseline credit amount for each channel |
| **Destination** | Specific final region, country, or type of message being sent through the Braze platform |
| **Multiplier** | Scaler to the Channel Credit Ratio, depending on pricing of the specific destination |
| **Credits per Message** | Exact number of Message Credits used to send one message<br> (credits per message = channel credit ratio x destination multiplier)  |
{: .reset-td-br-1 .reset-td-br-2}


## Credit ratio table for Message Credits - Lambda

{% details Click to expand %}
<table>
    <colgroup>
        <col span="4" style="background-color:background-color:#FFFFFF;">
        <col style="background-color:#f0f0f5">
    </colgroup>
    <tr>
        <th><b>Channel</b></th>
        <th><b>Channel Credit Ratio</b></th>
        <th><b>Destination</b></th>
        <th><b>Multiplier</b></th>
        <th class="credits-column"><b>Credits per Message</b></th>
    </tr>
    <tr>
        <td>SMS - US / CA</td>
        <td>1</td>
        <td>United States</td>
        <td>1.00</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>SMS - US / CA</td>
        <td>1</td>
        <td>United States Toll Free</td>
        <td>1.50</td>
        <td>1.50</td>
    </tr>
    <tr>
        <td>SMS - US / CA</td>
        <td>1</td>
        <td>Canada</td>
        <td>1.00</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>SMS - US / CA</td>
        <td>1</td>
        <td>Canada Toll Free</td>
        <td>1.30</td>
        <td>1.30</td>
    </tr>
    <tr>
        <td>MMS - US / CA</td>
        <td>3</td>
        <td>United States</td>
        <td>1.00</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>MMS - US / CA</td>
        <td>3</td>
        <td>United States Toll Free</td>
        <td>2.00</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>MMS - US / CA</td>
        <td>3</td>
        <td>Canada Long Code</td>
        <td>1.50</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>MMS - US / CA</td>
        <td>3</td>
        <td>Canada Short Code</td>
        <td>4.00</td>
        <td>12.00</td>
    </tr>
    <tr>
        <td>MMS - US / CA</td>
        <td>3</td>
        <td>Canada Toll Free</td>
        <td>1.30</td>
        <td>3.90</td>
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
        <td>Afghanistan</td>
        <td>2.48</td>
        <td>24.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Albania</td>
        <td>1.04</td>
        <td>10.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Algeria</td>
        <td>3.26</td>
        <td>32.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>American Samoa</td>
        <td>0.99</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Andorra</td>
        <td>1.18</td>
        <td>11.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Angola</td>
        <td>0.81</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Anguilla</td>
        <td>0.99</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Antigua and Barbuda</td>
        <td>0.98</td>
        <td>9.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Argentina</td>
        <td>1.40</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Armenia</td>
        <td>1.84</td>
        <td>18.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Aruba</td>
        <td>0.95</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Australia SMS</td>
        <td>0.39</td>
        <td>3.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Australia MMS</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Austria</td>
        <td>0.53</td>
        <td>5.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Azerbaijan</td>
        <td>3.32</td>
        <td>33.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Bahamas</td>
        <td>0.93</td>
        <td>9.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Bahrain</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Bangladesh</td>
        <td>2.76</td>
        <td>27.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Barbados</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Belarus</td>
        <td>3.20</td>
        <td>32.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Belgium</td>
        <td>1.48</td>
        <td>14.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Belize</td>
        <td>1.66</td>
        <td>16.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Benin</td>
        <td>0.92</td>
        <td>9.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Bermuda</td>
        <td>1.04</td>
        <td>10.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Bhutan</td>
        <td>2.50</td>
        <td>25.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Bolivia</td>
        <td>1.40</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Bosnia and Herzegovina</td>
        <td>1.01</td>
        <td>10.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Botswana</td>
        <td>1.23</td>
        <td>12.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Brazil</td>
        <td>0.21</td>
        <td>2.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Brunei</td>
        <td>0.27</td>
        <td>2.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Bulgaria</td>
        <td>1.94</td>
        <td>19.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Burkina Faso</td>
        <td>1.44</td>
        <td>14.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Burundi</td>
        <td>1.84</td>
        <td>18.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Cambodia</td>
        <td>2.41</td>
        <td>24.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Cameroon</td>
        <td>1.13</td>
        <td>11.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Cape Verde</td>
        <td>1.43</td>
        <td>14.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Caribbean Netherlands</td>
        <td>2.17</td>
        <td>21.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Cayman Islands</td>
        <td>0.99</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Central African Republic</td>
        <td>0.31</td>
        <td>3.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Chad</td>
        <td>2.31</td>
        <td>23.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Chile</td>
        <td>0.78</td>
        <td>7.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>China</td>
        <td>0.17</td>
        <td>1.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Colombia</td>
        <td>0.03</td>
        <td>0.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Comoros</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Congo</td>
        <td>0.68</td>
        <td>6.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Cook Islands</td>
        <td>0.68</td>
        <td>6.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Costa Rica</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Croatia</td>
        <td>0.85</td>
        <td>8.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Cuba</td>
        <td>1.86</td>
        <td>18.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Curacao</td>
        <td>0.99</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Cyprus</td>
        <td>0.22</td>
        <td>2.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Czech Republic</td>
        <td>0.90</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Denmark</td>
        <td>0.85</td>
        <td>8.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Djibouti</td>
        <td>1.09</td>
        <td>10.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Dominica</td>
        <td>0.96</td>
        <td>9.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Dominican Republic</td>
        <td>1.02</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>DR Congo</td>
        <td>1.48</td>
        <td>14.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Ecuador</td>
        <td>2.20</td>
        <td>22.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Egypt</td>
        <td>2.10</td>
        <td>21.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>El Salvador</td>
        <td>0.86</td>
        <td>8.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Equatorial Guinea</td>
        <td>0.54</td>
        <td>5.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Eritrea</td>
        <td>1.47</td>
        <td>14.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Estonia</td>
        <td>0.94</td>
        <td>9.40</td>
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
        <td>Ethiopia</td>
        <td>2.64</td>
        <td>26.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Falkland Islands</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Faroe Islands</td>
        <td>0.23</td>
        <td>2.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Fiji</td>
        <td>1.40</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Finland</td>
        <td>1.15</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>France</td>
        <td>0.93</td>
        <td>9.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>French Guiana</td>
        <td>2.01</td>
        <td>20.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>French Polynesia</td>
        <td>1.58</td>
        <td>15.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Gabon</td>
        <td>2.12</td>
        <td>21.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Gambia</td>
        <td>1.24</td>
        <td>12.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Georgia</td>
        <td>2.18</td>
        <td>21.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Germany</td>
        <td>1.73</td>
        <td>17.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Ghana</td>
        <td>1.74</td>
        <td>17.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Gibraltar</td>
        <td>0.16</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Greece</td>
        <td>1.02</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Greenland</td>
        <td>0.16</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Grenada</td>
        <td>1.03</td>
        <td>10.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Guadeloupe</td>
        <td>2.00</td>
        <td>20.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Guam</td>
        <td>0.62</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Guatemala</td>
        <td>1.86</td>
        <td>18.60</td>
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
        <td>Guinea</td>
        <td>1.83</td>
        <td>18.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Guinea-Bissau</td>
        <td>1.45</td>
        <td>14.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Guyana</td>
        <td>1.06</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Haiti</td>
        <td>1.16</td>
        <td>11.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Honduras</td>
        <td>0.72</td>
        <td>7.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Hong Kong</td>
        <td>0.98</td>
        <td>9.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Hungary</td>
        <td>1.16</td>
        <td>11.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Iceland</td>
        <td>1.15</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>India</td>
        <td>0.84</td>
        <td>8.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Indonesia</td>
        <td>3.66</td>
        <td>36.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Iran</td>
        <td>1.59</td>
        <td>15.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Iraq</td>
        <td>2.38</td>
        <td>23.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Ireland</td>
        <td>1.06</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Isle of Man</td>
        <td>0.81</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Israel</td>
        <td>1.50</td>
        <td>15.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Italy</td>
        <td>0.89</td>
        <td>8.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Ivory Coast</td>
        <td>1.55</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Jamaica</td>
        <td>1.10</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Japan</td>
        <td>0.92</td>
        <td>9.20</td>
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
        <td>Jordan</td>
        <td>2.58</td>
        <td>25.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Kazakhstan</td>
        <td>2.54</td>
        <td>25.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Kenya</td>
        <td>2.25</td>
        <td>22.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Kiribati</td>
        <td>0.31</td>
        <td>3.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Korea Republic of</td>
        <td>0.30</td>
        <td>3.00</td>
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
        <td>2.45</td>
        <td>24.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Kyrgyzstan</td>
        <td>2.64</td>
        <td>26.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Laos PDR</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Latvia</td>
        <td>0.74</td>
        <td>7.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Lebanon</td>
        <td>1.94</td>
        <td>19.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Lesotho</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Liberia</td>
        <td>0.72</td>
        <td>7.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Libya</td>
        <td>2.68</td>
        <td>26.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Liechtenstein</td>
        <td>0.38</td>
        <td>3.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Lithuania</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Luxembourg</td>
        <td>1.03</td>
        <td>10.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Macao</td>
        <td>0.38</td>
        <td>3.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Macedonia</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Madagascar</td>
        <td>2.22</td>
        <td>22.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Malawi</td>
        <td>2.24</td>
        <td>22.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Malaysia</td>
        <td>0.79</td>
        <td>7.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Maldives</td>
        <td>0.87</td>
        <td>8.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Mali</td>
        <td>2.17</td>
        <td>21.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Malta</td>
        <td>1.05</td>
        <td>10.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Marshall Islands</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Martinique</td>
        <td>1.88</td>
        <td>18.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Mauritania</td>
        <td>1.95</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Mauritius</td>
        <td>1.89</td>
        <td>18.90</td>
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
        <td>Mexico</td>
        <td>0.28</td>
        <td>2.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Micronesia</td>
        <td>0.93</td>
        <td>9.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Moldova</td>
        <td>0.87</td>
        <td>8.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Monaco</td>
        <td>1.62</td>
        <td>16.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Mongolia</td>
        <td>1.93</td>
        <td>19.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Montenegro</td>
        <td>0.99</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Montserrat</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Morocco</td>
        <td>1.55</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Mozambique</td>
        <td>0.61</td>
        <td>6.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Myanmar</td>
        <td>2.48</td>
        <td>24.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Namibia</td>
        <td>0.50</td>
        <td>5.00</td>
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
        <td>1.85</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Netherlands</td>
        <td>1.82</td>
        <td>18.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>New Caledonia</td>
        <td>1.49</td>
        <td>14.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>New Zealand</td>
        <td>1.42</td>
        <td>14.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Nicaragua</td>
        <td>1.27</td>
        <td>12.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Niger</td>
        <td>1.60</td>
        <td>16.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Nigeria</td>
        <td>2.13</td>
        <td>21.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Niue</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Norfolk Island</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>North Macedonia</td>
        <td>0.34</td>
        <td>3.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Northern Cyprus</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Norway</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Oman</td>
        <td>1.68</td>
        <td>16.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Pakistan</td>
        <td>2.22</td>
        <td>22.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Palau</td>
        <td>0.37</td>
        <td>3.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Palestinian Territory</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Panama</td>
        <td>0.93</td>
        <td>9.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Papua New Guinea</td>
        <td>0.99</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Paraguay</td>
        <td>0.28</td>
        <td>2.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Peru</td>
        <td>1.10</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Philippines</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Poland</td>
        <td>0.39</td>
        <td>3.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Portugal</td>
        <td>0.37</td>
        <td>3.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Puerto Rico</td>
        <td>0.13</td>
        <td>1.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Qatar</td>
        <td>0.39</td>
        <td>3.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Reunion/Mayotte</td>
        <td>1.13</td>
        <td>11.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Romania</td>
        <td>0.78</td>
        <td>7.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Russia</td>
        <td>1.89</td>
        <td>18.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Rwanda</td>
        <td>1.21</td>
        <td>12.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Saint Kitts and Nevis</td>
        <td>0.92</td>
        <td>9.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Saint Lucia</td>
        <td>1.07</td>
        <td>10.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Saint Pierre and Miquelon</td>
        <td>2.31</td>
        <td>23.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Saint Vincent and The Grenadines</td>
        <td>1.06</td>
        <td>10.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Samoa</td>
        <td>0.75</td>
        <td>7.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>San Marino</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Sao Tome and Principe</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Saudi Arabia</td>
        <td>1.07</td>
        <td>10.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Senegal</td>
        <td>2.02</td>
        <td>20.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Serbia</td>
        <td>0.89</td>
        <td>8.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Seychelles</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Sierra Leone</td>
        <td>1.35</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Singapore</td>
        <td>0.62</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Sint Maarten</td>
        <td>0.16</td>
        <td>1.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Slovakia</td>
        <td>0.81</td>
        <td>8.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Slovenia</td>
        <td>0.28</td>
        <td>2.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Solomon Islands</td>
        <td>0.78</td>
        <td>7.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Somalia</td>
        <td>1.78</td>
        <td>17.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>South Africa</td>
        <td>0.27</td>
        <td>2.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>South Ossetia</td>
        <td>2.05</td>
        <td>20.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>South Sudan</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Spain</td>
        <td>0.70</td>
        <td>7.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Sri Lanka</td>
        <td>2.51</td>
        <td>25.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>St Kitts and Nevis</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>St Lucia</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>St Pierre and Miquelon</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>St Vincent Grenadines</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Sudan</td>
        <td>2.24</td>
        <td>22.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Suriname</td>
        <td>0.73</td>
        <td>7.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Swaziland</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Sweden</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Switzerland</td>
        <td>0.61</td>
        <td>6.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Syria</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Taiwan</td>
        <td>1.63</td>
        <td>16.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Tajikistan</td>
        <td>3.45</td>
        <td>34.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Tanzania</td>
        <td>1.62</td>
        <td>16.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Thailand</td>
        <td>0.13</td>
        <td>1.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Timor-Leste</td>
        <td>0.87</td>
        <td>8.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Togo</td>
        <td>0.62</td>
        <td>6.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Tonga</td>
        <td>0.61</td>
        <td>6.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Trinidad and Tobago</td>
        <td>1.02</td>
        <td>10.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Tunisia</td>
        <td>2.20</td>
        <td>22.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Turkey</td>
        <td>0.05</td>
        <td>0.50</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Turkmenistan</td>
        <td>1.97</td>
        <td>19.70</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Turks and Caicos Islands</td>
        <td>0.99</td>
        <td>9.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Tuvalu</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Uganda</td>
        <td>1.90</td>
        <td>19.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Ukraine</td>
        <td>2.28</td>
        <td>22.80</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>United Arab Emirates</td>
        <td>0.42</td>
        <td>4.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>United Kingdom</td>
        <td>0.61</td>
        <td>6.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Unknown</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Uruguay</td>
        <td>0.71</td>
        <td>7.10</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Uzbekistan</td>
        <td>3.52</td>
        <td>35.20</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Vanuatu</td>
        <td>1.43</td>
        <td>14.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Venezuela</td>
        <td>0.84</td>
        <td>8.40</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Vietnam</td>
        <td>1.49</td>
        <td>14.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Virgin Islands, British</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Virgin Islands, U.S.</td>
        <td>N/A</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Wallis and Futuna</td>
        <td>1.46</td>
        <td>14.60</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Yemen</td>
        <td>1.63</td>
        <td>16.30</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Zambia</td>
        <td>1.99</td>
        <td>19.90</td>
    </tr>
    <tr>
        <td>SMS / MMS - Global</td>
        <td>10</td>
        <td>Zimbabwe</td>
        <td>1.64</td>
        <td>16.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Argentina Authentication</td>
        <td>0.95</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Argentina Marketing</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Argentina Service</td>
        <td>0.85</td>
        <td>8.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Argentina Utility</td>
        <td>1.10</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Brazil Authentication</td>
        <td>0.85</td>
        <td>8.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Brazil Marketing</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Brazil Service</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Brazil Utility</td>
        <td>0.95</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Chile Authentication</td>
        <td>1.40</td>
        <td>14.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Chile Marketing</td>
        <td>2.35</td>
        <td>23.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Chile Service</td>
        <td>1.20</td>
        <td>12.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Chile Utility</td>
        <td>1.55</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Colombia Authentication</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Colombia Marketing</td>
        <td>0.35</td>
        <td>3.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Colombia Service</td>
        <td>0.15</td>
        <td>1.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Colombia Utility</td>
        <td>0.25</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Egypt Authentication</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Egypt Marketing</td>
        <td>2.85</td>
        <td>28.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Egypt Service</td>
        <td>1.70</td>
        <td>17.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Egypt Utility</td>
        <td>1.80</td>
        <td>18.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>France Authentication</td>
        <td>1.85</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>France Marketing</td>
        <td>3.80</td>
        <td>38.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>France Service</td>
        <td>2.30</td>
        <td>23.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>France Utility</td>
        <td>2.05</td>
        <td>20.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Germany Authentication</td>
        <td>2.05</td>
        <td>20.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Germany Marketing</td>
        <td>3.60</td>
        <td>36.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Germany Service</td>
        <td>2.15</td>
        <td>21.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Germany Utility</td>
        <td>2.25</td>
        <td>22.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>N/A</td>
        <td>India Authentication</td>
        <td>0.04</td>
        <td>0.40</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>India Marketing</td>
        <td>0.25</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>India Service</td>
        <td>0.10</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>India Utility</td>
        <td>0.10</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>N/A</td>
        <td>Indonesia Authentication</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Indonesia Marketing</td>
        <td>1.10</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Indonesia Service</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Indonesia Utility</td>
        <td>0.55</td>
        <td>5.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Israel Authentication</td>
        <td>0.45</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Israel Marketing</td>
        <td>0.95</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Israel Service</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Israel Utility</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Italy Authentication</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Italy Marketing</td>
        <td>1.85</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Italy Service</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Italy Utility</td>
        <td>1.10</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Malaysia Authentication</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Malaysia Marketing</td>
        <td>2.30</td>
        <td>23.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Malaysia Service</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Malaysia Utility</td>
        <td>0.55</td>
        <td>5.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Mexico Authentication</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Mexico Marketing</td>
        <td>1.15</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Mexico Service</td>
        <td>0.30</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Mexico Utility</td>
        <td>0.70</td>
        <td>7.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Netherlands Authentication</td>
        <td>1.90</td>
        <td>19.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Netherlands Marketing</td>
        <td>4.25</td>
        <td>42.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Netherlands Service</td>
        <td>2.35</td>
        <td>23.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Netherlands Utility</td>
        <td>2.10</td>
        <td>21.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Nigeria Authentication</td>
        <td>0.75</td>
        <td>7.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Nigeria Marketing</td>
        <td>1.35</td>
        <td>13.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Nigeria Service</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Nigeria Utility</td>
        <td>0.85</td>
        <td>8.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>North America Authentication</td>
        <td>0.35</td>
        <td>3.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>North America Marketing</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>North America Service</td>
        <td>0.25</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>North America Utility</td>
        <td>0.40</td>
        <td>4.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Other Authentication</td>
        <td>0.80</td>
        <td>8.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Other Marketing</td>
        <td>1.60</td>
        <td>16.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Other Service</td>
        <td>0.40</td>
        <td>4.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Other Utility</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Pakistan Authentication</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Pakistan Marketing</td>
        <td>1.25</td>
        <td>12.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Pakistan Service</td>
        <td>0.40</td>
        <td>4.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Pakistan Utility</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Peru Authentication</td>
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
        <td>Peru Service</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Peru Utility</td>
        <td>1.10</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Africa Authentication</td>
        <td>0.40</td>
        <td>4.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Africa Marketing</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Africa Service</td>
        <td>0.95</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Africa Utility</td>
        <td>0.40</td>
        <td>4.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Asia Pacific Authentication</td>
        <td>1.15</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Asia Pacific Marketing</td>
        <td>1.95</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Asia Pacific Service</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Asia Pacific Utility</td>
        <td>1.25</td>
        <td>12.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Central &amp; Eastern Europe Authentication</td>
        <td>1.50</td>
        <td>15.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Central &amp; Eastern Europe Marketing</td>
        <td>2.30</td>
        <td>23.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Central &amp; Eastern Europe Service</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Central &amp; Eastern Europe Utility</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Latin America Authentication</td>
        <td>1.20</td>
        <td>12.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Latin America Marketing</td>
        <td>1.95</td>
        <td>19.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Latin America Service</td>
        <td>1.10</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Latin America Utility</td>
        <td>1.30</td>
        <td>13.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Middle East Authentication</td>
        <td>0.45</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Middle East Marketing</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Middle East Service</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Middle East Utility</td>
        <td>0.55</td>
        <td>5.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Western Europe Authentication</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Western Europe Marketing</td>
        <td>1.55</td>
        <td>15.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Western Europe Service</td>
        <td>1.05</td>
        <td>10.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Rest of Western Europe Utility</td>
        <td>1.10</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Russia Authentication</td>
        <td>1.15</td>
        <td>11.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Russia Marketing</td>
        <td>2.15</td>
        <td>21.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Russia Service</td>
        <td>1.05</td>
        <td>10.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Russia Utility</td>
        <td>1.25</td>
        <td>12.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Saudi Arabia Authentication</td>
        <td>0.60</td>
        <td>6.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Saudi Arabia Marketing</td>
        <td>1.10</td>
        <td>11.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Saudi Arabia Service</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Saudi Arabia Utility</td>
        <td>0.65</td>
        <td>6.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>South Africa Authentication</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>South Africa Marketing</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>South Africa Service</td>
        <td>0.45</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>South Africa Utility</td>
        <td>0.55</td>
        <td>5.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Spain Authentication</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Spain Marketing</td>
        <td>1.65</td>
        <td>16.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Spain Service</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Spain Utility</td>
        <td>1.00</td>
        <td>10.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Turkey Authentication</td>
        <td>0.20</td>
        <td>2.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Turkey Marketing</td>
        <td>0.30</td>
        <td>3.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Turkey Service</td>
        <td>0.10</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>Turkey Utility</td>
        <td>0.25</td>
        <td>2.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>United Arab Emirates Authentication</td>
        <td>0.45</td>
        <td>4.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>United Arab Emirates Marketing</td>
        <td>0.90</td>
        <td>9.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>United Arab Emirates Service</td>
        <td>0.50</td>
        <td>5.00</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>United Arab Emirates Utility</td>
        <td>0.55</td>
        <td>5.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>United Kingdom Authentication</td>
        <td>0.95</td>
        <td>9.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>United Kingdom Marketing</td>
        <td>1.85</td>
        <td>18.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>United Kingdom Service</td>
        <td>1.05</td>
        <td>10.50</td>
    </tr>
    <tr>
        <td>WhatsApp</td>
        <td>10</td>
        <td>United Kingdom Utility</td>
        <td>1.05</td>
        <td>10.50</td>
    </tr>
</table>
{: .reset-td-br-1 .reset-td-br-2}
{% enddetails %}

------

## SMS/MMS channel details

### SMS segments

SMS message segments are how the SMS industry counts messages. A message segment is a grouping of up to a defined number of characters (160 for GSM-7 encoding; 67 for UCS-2 encoding) that will be sent in a single SMS dispatch. If you dispatch an SMS with 161 characters using GSM-7 encoding, you will see that there are two (2) message segments that were sent. Sending multiple message segments will result in additional charges.

### MMS segments

For MMS, the message limit is 5 MB (this includes the multimedia asset and the message body size). To be on the safer side, Braze recommends not exceeding 600 KB for your multimedia asset while also including a message body.

## WhatsApp channel details

WhatsApp is a channel focused on two-way messaging and thus anchors on Conversations (instead of number of individual messages). A Conversation is a 24-hour thread between a business and an end-user.

### Conversation type definitions

**Marketing Conversations:** Business-initiated conversations that enable you to achieve a wide range of goals, from generating awareness to driving sales and retargeting customers. Examples include new product, service, or feature announcements, targeted promotions/offers, and cart abandonment reminders.

**Utility Conversations:** Business-initiated conversations that enable you to follow-up on user actions or requests. Examples include opt-in confirmation, order/delivery management (e.g., delivery update), account updates or alerts (e.g., payment reminder), or feedback surveys.

**Authentication Conversations:** Enable you to authenticate users with one-time passcodes, potentially at multiple steps in the login process (e.g., account verification, account recovery, integrity challenges).

{% alert note %}
Authentication conversations will only be supported on a case-by-case basis and Braze cannot guarantee specific SLAs. Additionally, Braze does not support PIN generation.
{% endalert %}

**Service Conversations:** User-initiated conversations that are responded to with a non-templated message.

{% alert note %}
User-initiated conversations that are responded to with a marketing or utility template will be charged as such.
{% endalert %}

## Billing region breakdown

#### North America

United States, Canada

#### Rest of Africa

Algeria, Angola, Benin, Botswana, Burkina Faso, Burundi, Cameroon, Chad, Congo, Eritrea, Ethiopia, Gabon, Gambia, Ghana,  Guinea-Bissau, Ivory Coast, Kenya, Lesotho, Liberia, Libya,
Madagascar, Malawi, Mali, Mauritania, Morocco, Mozambique, Namibia, Niger, Rwanda, Senegal, Sierra Leone, Somalia, South Sudan, Sudan, Swaziland, Tanzania, Togo, Tunisia, Uganda, Zambia

#### Rest of Asia Pacific

Afghanistan, Australia, Bangladesh, Cambodia, China, Hong Kong, Japan, Laos, Mongolia, Nepal, New Zealand, Papua New Guinea, Philippines, Singapore, Sri Lanka, Taiwan, Tajikistan, Thailand,
Turkmenistan, Uzbekistan, Vietnam

#### Rest of Central & Eastern Europe

Albania, Armenia, Azerbaijan, Belarus, Bulgaria, Croatia, Czech Republic, Georgia, Greece, Hungary, Latvia, Lithuania, Macedonia, Moldova, Poland, Romania, Serbia, Slovakia, Slovenia, Ukraine

#### Rest of Latin America

Bolivia, Costa Rica, Dominican Republic, Ecuador, El Salvador,
Guatemala, Haiti, Honduras, Jamaica, Nicaragua, Panama, Paraguay, Puerto Rico, Uruguay, Venezuela

#### Rest of Middle East

Bahrain, Iraq, Jordan, Kuwait, Lebanon, Oman, Qatar, Yemen

#### Rest of Western Europe

Austria, Belgium, Denmark, Finland, Ireland, Norway, Portugal, Sweden, Switzerland
