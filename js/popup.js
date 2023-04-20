function displayResults(products) {
  const resultsContainer = document.getElementById('results');
  resultsContainer.innerHTML = '';

  products.forEach(product => {
    const productElement = document.createElement('div');
    productElement.innerHTML = `
      <h2>${product.title}</h2>
      <p>Price: ${product.price ? `$${product.price}` : 'N/A'}</p>
    `;
    resultsContainer.appendChild(productElement);
  });
}

document.getElementById('fetchSimilarProducts').addEventListener('click', () => {
  chrome.tabs.query({ active: true, currentWindow: true }, tabs => {
    chrome.tabs.sendMessage(tabs[0].id, { action: 'fetchSimilarProducts' }, displayResults);
  });
});
