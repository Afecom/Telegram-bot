const fetch = require('node-fetch');

export async function getData() {
  const consumer_key = "ck_0a1d0af37fc58d63e8925d487fa92f3c17e93726";
  const consumer_secret = "cs_54f05f6e23f158b1abde94968fb3a2d40aeb7ba7";
  try {
    const response = await fetch(
      "https://aveluxecosmetics.com/wp-json/wc/v3/products?consumer_key="+consumer_key+"&consumer_secret="+consumer_secret
    );

    if (!response.ok) {
      throw new Error("Failed to fetch products from the API.");
    }

    const productsData = await response.json();
    console.log(productsData);

    return productsData.map((product) => ({
      title: product.name,
      price: product.sale_price,
      Image: product.image[0].src,
      id: product.id,
    }));
  } catch (error) {
    console.error(error);
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