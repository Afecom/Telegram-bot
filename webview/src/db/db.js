import fetch from 'node-fetch';

const consumerKey = 'ck_0a1d0af37fc58d63e8925d487fa92f3c17e93726';
const consumerSecret = 'cs_54f05f6e23f158b1abde94968fb3a2d40aeb7ba7';

let result; // Declare the result variable outside the function

async function getData() {
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

    // Transform the received data into an array of product objects
    const products = data.map((item) => {
      return {
        title: item.title,
        price: item.price,
        Image: item.Image,
        id: item.id
      };
    });

    result = products; // Assign the result to the variable
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
}

function getResult() {
  return result; // Return the result from the function
}

export { getResult };
