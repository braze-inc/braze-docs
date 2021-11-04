### Yotpo
Yotpo, the leading eCommerce marketing platform, helps thousands of forward-thinking brands like Patagonia, Rebecca Minkoff, MVMT, Tweezerman, and Bob’s Discount Furniture accelerate direct-to-consumer growth. Yotpo’s single-platform approach integrates data-driven solutions for reviews, loyalty, SMS marketing, and more, empowering brands to create smarter, higher-converting customer experiences. 

### Yotpo & Braze
With the integration between Yotpo and Braze you will be able to dynamically pull and display star ratings, top reviews, and visual UGC on products within emails and other communication channels within Braze.

In addition, the integration allows to include customer-level loyalty data in emails and other communication methods to create a more personalized interaction and boost sales and loyalty.


###
### Prerequisites


|Requirement|Origin|Access|Description|
| :- | :- | :- | :- |
|Yotpo Reviews API key|Yotpo|[Find you API key](https://support.yotpo.com/en/article/finding-your-yotpo-app-key-and-secret-key)|This API key will be implemented within the ‘connected content’ code snippet.|
|Yotpo Loyalty API key|Yotpo |[Find your API key and GUID](https://support.yotpo.com/en/article/finding-your-loyalty-referrals-api-key-and-guid)|This API key and GUID will be implemented within the ‘connected content’ code snippet.|

Please confirm that the **Yotpo product ID is the same as Braze**

**Product ID** that will be pulled dynamically from Braze - this is mandatory for the integration to work.

How to find your Yotpo Product  ID:

\1. Go to your store website.

\2. Open the product page.

\3. Right-click and select Inspect.

\4. Press Ctrl+F and search for ‘**yotpo-main**’ in the code. The **data-product ID** variable and its value appear in the Yotpo div:



###
### Integrating Yotpo and Braze
1. Open your Braze [dashboard](https://dashboard.braze.com/)
1. Go to Campaigns > Create Campaign > Select the Campaign channel
1. Select your preferred template
1. Click Edit email body

All you need to do is add the below [Connected Content](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/) snippet for any of the applicable use case/s:

**Display a product’s star rating and review count**

This snippet provides the public average score and number of total reviews for a product that is included in the email:

{% connected\_content https://api.yotpo.com/products/##YOTPO API KEY##/{{event\_properties.${product\_id}}}/bottomline :save result %}		

{% if {{result.response.bottomline.average\_score}} != 0 %}

The average rating for this product is: <br />

`                    `{{result.response.bottomline.average\_score}}/5, based on  

`                    `{{result.response.bottomline.total\_reviews}} reviews.

{% else %}                    

{% endif %}

\*Note: The ##YOTPO API KEY## needs to be replaced with your Yotpo Reviews API Key. In addition, it’s important to note that the {product\_id}  will be pulled dynamically from Braze - for the integration to work, **the product\_ID in Braze has to match the product ID in Yotpo** (typically the e-commerce parent product ID)





**Display a Recent 5 Star Review for a Product** 

This snippet provides a top (published) review for a specific product that is included in the email:



{% connected\_content https://api.yotpo.com/v1/widget/##YOTPO API KEY##/products/{{event\_properties.${product\_id}}}/reviews.json?per\_page=50&star=5&sort=votes\_up :save result %}



{% if {{result.response.reviews[0].score}} == 5 %}

Recent 5 Star Review for this product: <br />

`              `{{result.response.reviews[0].content}}

{% else %}              

{% endif %}


\*Note: Don’t forget that the ##YOTPO API KEY## needs to be replaced with your Yotpo Reviews API Key (see instructions for finding this key above). In addition, it’s important to note that that {product\_id} is a dynamic parameter that will be pulled from Braze - for the integration to work, **the product\_ID in Braze needs to be identical to the product ID in Yotpo** (typically the e-commerce parent product ID)

Here’s what the snippet in your email editor will look like:



**Displaying Visual UGC by Product**

Retrieve images that were tagged and published in Yotpo and add them to your emails instead of the stock image or as an additional gallery:

{% connected\_content https://api.yotpo.com/v1/widget/##YOTPO API KEY##/albums/product/{{event\_properties.${product\_id}}}?per\_page=1 :save result %}

`												`{% if {{result.response.images[0].tagged\_products[0].image\_url}} != null %}

`												`The Visual content of the product: <br/>							<img src="{{result.response.images[0].tagged\_products[0].image\_url}}" border="0" width="200" height="200" alt="" />

{% else %}              

`              `Image return NULL

{% endif %}

The snippet will look something like this:























**Displaying a Customer’s Loyalty Balance in an Email**


{% connected\_content

`     `https://loyalty.yotpo.com/api/v2/customers?customer\_email=**{{${email\_address}}}**

`     `:method get

`     `:headers {

`       `"x-guid": "##YOTPO LOYALTY GUID##",

`       `"x-api-key": "##YOTPO LOYALTY API KEY##"

` 	`}

`     `:content\_type application/json

`     `:save publication

%}

You have {{publication.points\_balance}} points <br>

Only  {{publication.vip\_tier\_upgrade\_requirements.points\_needed}} more points to become part of our VIP Tier!


\*Note: The ##YOTPO LOYALTY GUID## and ##YOTPO LOYALTY API KEY##  need to be replaced with your Yotpo Loyalty credentials as explained above. In addition, it’s important to note that **{{${email\_address}}}**is a dynamic parameter and will be pulled dynamically from Braze - for the integration to work, the email needs to be the email of the customer that is receiving the email. 


The snippet will look something like this:

**FAQ**

Q. What happens if I do not have a 5-star review?

A. The connected content endpoint for retrieving 5-star review will not display any content if the endpoint response returns NULL for the product image or 5-star review. 

Q. What happens if I do not have an image published for a product?

1. The connected content endpoint for retrieving an image will not display any content if the endpoint response returns NULL for the product image.

Q. Can I customize the look and feel, or pull other data fields from Yotpo? 

A. Yes, simply follow [this guide](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) about Braze Connected Content to discover what other data points and customization options are available.

You may need some assistance from a front-end developer to do so.

Please note - Yotpo does not support any custom requirements beyond what is described in this guide.
