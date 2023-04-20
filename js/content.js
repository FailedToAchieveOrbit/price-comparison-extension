function extractProductData(productElement) {
  try {
    const title = productElement.querySelector('span.a-text-normal').innerText;
    const priceElement = productElement.querySelector('span.a-price-whole');
    const price = priceElement ? priceElement.innerText : null;
    const imageUrl = productElement.querySelector('img.s-image').src;

    return { title, price, imageUrl };
  } catch (error) {
    return null;
  }
}

function fetchSimilarProducts(searchQuery) {
  const encodedQuery = encodeURIComponent(searchQuery);
  const searchUrl = `https://www.amazon.com/s?k=${encodedQuery}&ref=nb_sb_noss`;

  return fetch(searchUrl)
    .then(response => response.text())
    .then(html => {
      const parser = new DOMParser();
      const doc = parser.parseFromString(html, 'text/html');
      const productElements = doc.querySelectorAll('div.s-result-item');
      const products = Array.from(productElements)
        .map(extractProductData)
        .filter(product => product !== null);

      return products;
    });
}

chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
  if (request.action === 'fetchSimilarProducts') {
    const currentProductTitle = document.querySelector('#productTitle').innerText.trim();

    fetchSimilarProducts(currentProductTitle).then(products => {
      const sortedProducts = products.sort((a, b) => {
        if (!a.price) return 1;
        if (!b.price) return -1;
        return parseFloat(a.price.replace(/,/g, '')) - parseFloat(b.price.replace(/,/g, ''));
      });

      sendResponse(sortedProducts.slice(0, 10)); // Return top 10 sorted products
    });

    return true; // Response will be sent asynchronously
  }
});
