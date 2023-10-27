import fetch from 'node-fetch';

const consumerKey = 'ck_0a1d0af37fc58d63e8925d487fa92f3c17e93726';
const consumerSecret = 'cs_54f05f6e23f158b1abde94968fb3a2d40aeb7ba7';

async function getData() {
  try {
    const url = `https://aveluxecosmetics.com/wp-json/wc/v3/products?consumer_key=${consumerKey}&consumer_secret=${consumerSecret}`;
    const response = await fetch(url);

    if (!response.ok) {
      throw new Error('Request failed');
    }

    const data = await response.json();

    // Transform the received data into an array of product objects
    const products = data.map((item) => {
      return {
        title: item.title,
        price: item.sale_price,
        Image: item.images[0].src,
        id: item.id
      };
    });

    return products; // Return the products
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
}

let result = null; // Declare the result variable

async function fetchData() {
  try {
    result = await getData();
  } catch (error) {
    console.error('Error:', error);
  }
}

fetchData();

function getResult() {
  return result; // Return the result from the function
}

export { getResult };
