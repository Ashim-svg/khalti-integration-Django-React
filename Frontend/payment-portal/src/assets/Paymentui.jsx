import React, { useState } from "react";
import axios from "axios";

const PaymentUI = () => {
  const [amount, setAmount] = useState("");
  const [productName, setProductName] = useState("");
  const [orderId, setOrderId] = useState("");
  const [isLoading, setIsLoading] = useState(false);

  const handlePayment = async (e) => {
    e.preventDefault();
    setIsLoading(true);

    try {
      const payload = {
        return_url: "https://example.com/payment/",
        website_url: "https://example.com/",
        amount: parseInt(amount),
        purchase_order_id: orderId,
        purchase_order_name: productName,
        customer_info: {
          name: "Test User",
          email: "test@example.com",
          phone: "9800000000"
        }
      };
      const res = await axios.post("http://127.0.0.1:8000/khalti/epayment/initiate/", payload);
      if (res.data.status === "success" && res.data.data.payment_url) {
        window.location.href = res.data.data.payment_url;
      } else {
        alert("Payment initiation failed: " + JSON.stringify(res.data.data));
      }
    } catch (err) {
      alert("Payment initiation failed. Please try again.");
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 400, margin: "40px auto", padding: 24, border: "1px solid #ddd", borderRadius: 8 }}>
      <h2>Khalti Payment</h2>
      <form onSubmit={handlePayment}>
        <div style={{ marginBottom: 12 }}>
          <label>Amount (in paisa):</label>
          <input
            type="number"
            value={amount}
            onChange={(e) => setAmount(e.target.value)}
            required
            style={{ width: "100%", padding: 8 }}
          />
        </div>
        <div style={{ marginBottom: 12 }}>
          <label>Product Name:</label>
          <input
            type="text"
            value={productName}
            onChange={(e) => setProductName(e.target.value)}
            required
            style={{ width: "100%", padding: 8 }}
          />
        </div>
        <div style={{ marginBottom: 16 }}>
          <label>Order ID:</label>
          <input
            type="text"
            value={orderId}
            onChange={(e) => setOrderId(e.target.value)}
            required
            style={{ width: "100%", padding: 8 }}
          />
        </div>
        <button type="submit" style={{ width: "100%", padding: 10, background: "#5c2d91", color: "#fff", border: "none", borderRadius: 4 }} disabled={isLoading}>
          {isLoading ? "Processing..." : "Pay with Khalti"}
        </button>
      </form>
    </div>
  );
};

export default PaymentUI;