import React, { useState } from "react";

const API_BASE = "http://localhost:8000/api/khalti"; // Update if your backend runs elsewhere

export default function PaymentUI() {
  const [banks, setBanks] = useState([]);
  const [initiateResult, setInitiateResult] = useState(null);
  const [lookupResult, setLookupResult] = useState(null);

  // Fetch bank list
  const fetchBanks = async () => {
    const res = await fetch(`${API_BASE}/bank-list/?payment_type=ebanking`);
    const data = await res.json();
    setBanks(data);
  };

  // Initiate payment
  const initiatePayment = async (payload) => {
    const res = await fetch(`${API_BASE}/epayment/initiate/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await res.json();
    setInitiateResult(data);
  };

  // Lookup payment
  const lookupPayment = async (payload) => {
    const res = await fetch(`${API_BASE}/epayment/lookup/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });
    const data = await res.json();
    setLookupResult(data);
  };

  return (
    <div>
      <button onClick={fetchBanks}>Fetch Banks</button>
      <ul>
        {banks.map((bank) => (
          <li key={bank.idx}>{bank.name}</li>
        ))}
      </ul>
      <button
        onClick={() =>
          initiatePayment({
            // Fill with required payload fields
            return_url: "http://localhost:5173/success",
            website_url: "http://localhost:5173",
            amount: 1000,
            purchase_order_id: "order123",
            purchase_order_name: "Test Order",
            customer_info: {
              name: "John Doe",
              email: "john@example.com",
              phone: "9800000000",
            },
          })
        }
      >
        Initiate Payment
      </button>
      {initiateResult && <pre>{JSON.stringify(initiateResult, null, 2)}</pre>}

      <button
        onClick={() =>
          lookupPayment({
            pidx: "your_pidx_here", // Replace with actual pidx from initiate response
          })
        }
      >
        Lookup Payment
      </button>
      {lookupResult && <pre>{JSON.stringify(lookupResult, null, 2)}</pre>}
    </div>
  );
}