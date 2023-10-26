import axios from 'axios';

const consumerKey = 'ck_0a1d0af37fc58d63e8925d487fa92f3c17e93726';
const consumerSecret = 'cs_54f05f6e23f158b1abde94968fb3a2d40aeb7ba7';

export async function getData() {
  try {
    const response = await fetch(
      "https://aveluxecosmetics.com/wp-json/wc/v3/products?consumer_key="+consumer_key+"&consumer_secret="+consumer_secret
    );

    if (!response.ok) {
      throw new Error('Request failed');
    }

    const data = await response.json();
    console.log(data);
    return data;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
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