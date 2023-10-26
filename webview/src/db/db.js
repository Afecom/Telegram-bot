const fetch = require('node-fetch');

export async function getData() {
  try {
    const response = await fetch('https://your-woocommerce-api-endpoint/wp-json/wc/v3/products', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_API_TOKEN' // Replace with your WooCommerce API token
      }
    });

    if (!response.ok) {
      throw new Error('Failed to fetch products from the WooCommerce API');
    }

    const products = await response.json();

    // Transform the fetched products into the desired format
    const transformedProducts = products.map(product => ({
      title: product.name,
      price: product.price,
      image: product.images[0]?.src,
      id: product.id
    }));

    return transformedProducts;
  } catch (error) {
    console.error('Error fetching products:', error);
    return [];
  }
}

// Usage example
// getData()
//   .then((products) => {
//     console.log(products);
//   })
//   .catch((error) => {
//     console.error(error);
//   });