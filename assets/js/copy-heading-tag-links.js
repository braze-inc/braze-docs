// Add copy link buttons to headings with IDs
  function addHeadingCopyButtons() {
    const headings = $('#article-main h1[id], #article-main h2[id], #article-main h3[id], #article-main h4[id], #article-main h5[id], #article-main h6[id]');
    
    headings.each(function() {
      const $heading = $(this);
      const headingId = $heading.attr('id');
      
      if (headingId) {
        // Create a container for the heading content and copy button
        const $container = $('<div class="heading-with-copy">');
        const $copyButton = $(`<button class="heading-copy-btn" data-clipboard-text="#${headingId}" title="Copy link to this section">`);
        const $copyIcon = $(`<i alt="Copy link" title="Copy link" class="heading-copy-icon fas fa-link"></i>`);
        
        $copyButton.append($copyIcon);
        
        // Wrap the heading content but preserve the heading tag
        $heading.wrapInner($container);
        $heading.find('.heading-with-copy').append($copyButton);
      }
    });

    // Initialize ClipboardJS for heading copy buttons
    const headingClipboard = new ClipboardJS('.heading-copy-btn', {
      text: function(trigger) {
        const hash = trigger.getAttribute('data-clipboard-text');
        // Take current URL and replace/add the anchor tag
        const currentUrl = window.location.href.split('#')[0]; // Remove existing hash if any
        return currentUrl + hash;
      }
    });

    headingClipboard.on('success', function(e) {
      const $icon = $(e.trigger).find('.heading-copy-icon');
      $icon.removeClass('fa-link fa-close').addClass('fa-check');
      setTimeout(function() {
        $icon.removeClass('fa-check').addClass('fa-link');
      }, 1500);
    });

    headingClipboard.on('error', function(e) {
      const $icon = $(e.trigger).find('.heading-copy-icon');
      $icon.removeClass('fa-link fa-check').addClass('fa-close');
      setTimeout(function() {
        $icon.removeClass('fa-close').addClass('fa-link');
      }, 1500);
    });
  }

  $(document).ready(function() {    
    // Call the function to add heading copy buttons
    addHeadingCopyButtons();
  });
