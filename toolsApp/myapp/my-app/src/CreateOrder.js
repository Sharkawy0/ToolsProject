import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const CreateOrder = ({ onOrderCreated }) => {
  const [formData, setFormData] = useState({
    pickupLocation: "",
    dropoffLocation: "",
    packageDetails: "",
    deliveryTime: ""
  });
  const [error, setError] = useState(null);
  const [successMessage, setSuccessMessage] = useState(null);
  const navigate = useNavigate();

  // Handle input changes
  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  // Handle order creation form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:8000/api/orders/create", formData);
      if (response.status === 201) {
        setSuccessMessage("Order created successfully!");
        setError(null);
        onOrderCreated(); // Notify parent component that order is created
      }
    } catch (error) {
      setError(error.response?.data?.error || "Order creation failed. Please try again.");
    }
  };

  return (
    <div>
      <h2>Create Order</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {successMessage && <p style={{ color: "green" }}>{successMessage}</p>}

      {/* Navigation Buttons */}
      <h3>Navigation</h3>
      <div style={{  display: "flex", justifyContent: "center", gap: "10px", width: "100%" }}>
        <button onClick={() => navigate("/my-orders")}>My Orders</button>
        <button onClick={() => navigate("/order-details/1")}>Order Details</button> {/* Example orderId = 1 */} 
        <button onClick={() => navigate("/assigned-orders")}>Assigned Orders</button> 
        <button onClick={() => navigate("/manage-orders")}>Manage Orders</button>
        <button onClick={() => navigate("/assigned-orders-to-courier")}>Assigned Orders to Courier</button>
      </div>

      <br /> <br />

      {/* Order Creation Form */}
      <form onSubmit={handleSubmit}>
        <label>
          Pickup Location: <div style={{ display: "inline" }}>{""}</div>
          <input
            type="text"
            name="pickupLocation"
            value={formData.pickupLocation}
            onChange={handleChange}
            required
          />
        </label>
        <br /> <br></br>
        <label>
          Drop-off Location: <div style={{ display: "inline" }}>{""}</div>
          <input
            type="text"
            name="dropoffLocation"
            value={formData.dropoffLocation}
            onChange={handleChange}
            required
          />
        </label>
        <br /> <br />
        <label>
          Package Details: <div style={{ display: "inline" }}>{""}</div>
          <textarea
            name="packageDetails"
            value={formData.packageDetails}
            onChange={handleChange}
            required
          />
        </label>
        <br /> <br />
        <label>
          Delivery Time: <div style={{ display: "inline" }}>{""}</div>
          <select
            name="deliveryTime"
            value={formData.deliveryTime}
            onChange={handleChange}
            required
          >
            <option value="">Select Delivery Time</option>
            <option value="morning">Morning (8 AM - 12 PM)</option>
            <option value="afternoon">Afternoon (12 PM - 4 PM)</option>
            <option value="evening">Evening (4 PM - 8 PM)</option>
          </select>
        </label>
        <br /> <br />
        <button type="submit">Create Order</button>
      </form>
      <br /> <br />
      
    </div>
  );
};

export default CreateOrder;