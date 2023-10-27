import fetch from 'node-fetch';

const consumerKey = 'your_consumer_key';
const consumerSecret = 'your_consumer_secret';

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
    console.log('Data:', data); // Log the products to the console
    
    // Transform the received data into an array of product objects
    const products = data.map((item) => {
      return {
        title: item.title,
        price: item.price,
        Image: item.images[0].src,
        id: item.id
      };
    });


    return products;
  } catch (error) {
    console.error('Error fetching data:', error);
    throw error;
  }
}

export { getData };
