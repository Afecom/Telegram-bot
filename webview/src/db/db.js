const consumerKey = 'ck_0a1d0af37fc58d63e8925d487fa92f3c17e93726';
const consumerSecret = 'cs_54f05f6e23f158b1abde94968fb3a2d40aeb7ba7';

// Then you can use them in your HTTP request code
export async function getData() {
  try {
    const response = await fetch('https://aveluxecosmetics.com/wp-json/wc/v3/products', {
      headers: {
        Authorization: `Bearer ${consumerKey}:${consumerSecret}`
      }
    });

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