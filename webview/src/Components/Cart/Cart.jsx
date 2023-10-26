const React = require("react");
const { useState, useEffect } = React;
require ("./Cart.css");
const Button = require(path.join(__dirname, ".../Button/Button")).default;
function Cart({ cartItems, onCheckout }) {
  const totalPrice = cartItems.reduce((a, c) => a + c.price * c.quantity, 0);

  return (
    <div className="cart__container">
      {cartItems.length === 0 ? "No items in cart" : ""}
      <br /> <span className="">Total Price: ${totalPrice.toFixed(2)}</span>
      <Button
        title={`${cartItems.length === 0 ? "Order !" : "Checkout"} `}
        type={"checkout"}
        disable={cartItems.length === 0 ? true : false}
        onClick={onCheckout}
      />
    </div>
  );
}

export default Cart;
