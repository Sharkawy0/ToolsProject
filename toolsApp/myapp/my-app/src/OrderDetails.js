// OrderDetails.js
import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const OrderDetails = () => {
  const { orderId } = useParams();
  const [order, setOrder] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchOrderDetails = async () => {
      try {
        const response = await axios.get(`http://localhost:8000/api/orders/${orderId}`);
        setOrder(response.data);
      } catch (error) {
        setError("Failed to fetch order details. Please try again.");
      }
    };
    fetchOrderDetails();
  }, [orderId]);

  const handleCancelOrder = async () => {
    try {
      await axios.delete(`http://localhost:8000/api/orders/${orderId}`);
      setOrder({ ...order, status: "Cancelled" });
    } catch (error) {
      setError("Failed to cancel order. Please try again.");
    }
  };

  if (error) return <p style={{ color: "red" }}>{error}</p>;
  if (!order) return <p>Loading...</p>;

  return (
    <div>
      <h2>Order Details</h2>
      <p>Pickup Location: {order.pickupLocation}</p>
      <p>Drop-off Location: {order.dropoffLocation}</p>
      <p>Package Details: {order.packageDetails}</p>
      <p>Delivery Time: {order.deliveryTime}</p>
      <p>Status: {order.status}</p>
      <p>Courier Info: {order.courierInfo || "Not assigned yet"}</p>

      {order.status === "Pending" && (
        <button onClick={handleCancelOrder}>Cancel Order</button>
      )}
    </div>
  );
};

export default OrderDetails;