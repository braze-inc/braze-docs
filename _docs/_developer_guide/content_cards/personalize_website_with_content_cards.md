---
nav_title: "Personalize Your Website with Content Cards"
article_title: "Personalize Your Website with Content Cards"
description: "Learn how to use Braze Content Cards to create personalized, dynamic website modules that can be updated without code deployments."
page_order: 5
channel:
  - content cards
platform:
  - Web
---

# Personalize your website with Content Cards

This page discusses how to personalize part of your website utilizing Braze Content Cards. Content Cards are a messaging channel in Braze that typically populate in a feed such as a notification center. However, with some customization, the format and display of the cards can blend in with your overall website design, creating a personalized experience for each user.

The benefits of creating this service include:

- Non-technical Braze users populate personalized content for users once implemented - no need for separate engineering releases for every website content update!
- Each user can see their own version of your website, creating a more personalized, one-to-one user experience.
- Content Cards can be triggered based on user actions and/or personalized based on user data.

Follow the steps on this page to set up Content Cards in the Braze platform, and manually retrieve and display them on your website with a custom implementation.

## Prerequisites

To implement this solution, you need the following:

- Access to the Braze Content Cards product
- Intermediate knowledge of JavaScript to code the custom display of Content Cards

## Step 1: Create your Content Card campaigns in the Braze dashboard

1. **Create a New Campaign**: Click on **Create Campaign** and select **Content Cards** as the messaging type.
2. **Compose Your Card**:
   - **Title and Description**: Enter the title and description for your Content Card. These fields are what users will see on your website.
   - **Image and URL** (optional): Add an image and a URL that the card will link to when clicked.
   - **Personalize Attributes**: Use custom attributes to personalize the content. For example, you can use tags like {% raw %}`{{${first_name}}}`{% endraw %} to dynamically insert user-specific data.
3. **Target Your Audience**: Define the audience for your Content Card. Use segmentation to target specific user groups based on their behavior or attributes.
4. **Choose Delivery**: Choose when or how the Content Card should be delivered. You can set it to be sent immediately, schedule it for a later time, or trigger it based on a certain action.

## Step 2: Integrate Braze Content Cards into Your Website with Custom Implementation

1. **Include Braze Web SDK**: Integrate the Braze Web SDK into your website. This involves adding the Braze JavaScript library to your website's codebase.
2. **Initialize the SDK**:
   - Use the `braze.initialize` function to set up the SDK with your Braze API key and other configuration options.
3. **Manually Retrieve Content Card Data**:
   - Use the `braze.subscribeToContentCardsUpdates` method to fetch Content Cards from Braze. This method allows you to access the data model of the Content Cards directly, extracting the JSON data structure that contains all the card details such as title, description, image URL, and any custom attributes.
   - Call `braze.requestContentCardsRefresh()` to trigger an immediate fetch of Content Cards after subscribing to updates.
4. **Custom Display Logic**:
   - Implement a custom function to parse the Content Card data model. This function should extract the necessary fields and format them according to your website's design requirements.
   - Create custom HTML elements and styles to display the Content Card data. This allows you to have full control over how the content is presented on your website.

**Sample Code Snippet**:

```html
<div id="content-cards-container"></div>
<script>
  braze.subscribeToContentCardsUpdates(function(updates) {
    const cards = updates.cards;
    const container = document.getElementById('content-cards-container');
    container.innerHTML = ''; // Clear existing content

    cards.forEach(card => {
      if (!card.isControl) { // Ensure it's not a control card
        const cardElement = document.createElement('div');
        cardElement.className = 'content-card';
        
        const title = document.createElement('h2');
        title.textContent = card.title || '';
        cardElement.appendChild(title);
        
        const description = document.createElement('p');
        description.textContent = card.description || '';
        cardElement.appendChild(description);
        
        if (card.imageUrl) {
          const img = document.createElement('img');
          img.src = card.imageUrl;
          img.alt = card.title || '';
          cardElement.appendChild(img);
        }
        
        if (card.url) {
          const link = document.createElement('a');
          link.href = card.url;
          link.target = '_blank';
          link.rel = 'noopener noreferrer';
          link.textContent = 'Learn More';
          cardElement.appendChild(link);
        }
        
        container.appendChild(cardElement);
      }
    });
  });
  
  braze.requestContentCardsRefresh();
</script>
```

**Styling**: Use CSS to style the Content Cards to match your website's design. For example:

```css
.content-card {
  border: 1px solid #ccc;
  padding: 16px;
  margin: 16px 0;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.content-card img {
  max-width: 100%;
  height: auto;
  border-radius: 4px;
}
```

## Testing

After completing the above instructions, complete the following steps:

1. Target your user profile and send yourself the Content Card campaign
2. Navigate to your website and ensure the Content Card displays correctly
3. Keep a close eye on results as you launch your campaign

## Considerations

- **Responsive Design**: Ensure that Content Cards are responsive and display well on different devices and screen sizes.
- **Test the Integration**: Ensure that Content Cards are displaying correctly on your website and that personalization is working as expected.