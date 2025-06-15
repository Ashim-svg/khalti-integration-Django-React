import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import PaymentUI from "./assets/Paymentui"; // Adjust the path if needed

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<PaymentUI />} />
        {/* Add other routes here */}
      </Routes>
    </Router>
  );
}

export default App;