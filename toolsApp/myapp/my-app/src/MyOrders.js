// MyOrders.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

const MyOrders = () => {
  const [orders, setOrders] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchOrders = async () => {
      try {
        const response = await axios.get("http://localhost:8000/api/orders/my-orders");
        setOrders(response.data);
      } catch (error) {
        setError("Failed to fetch orders. Please try again.");
      }
    };
    fetchOrders();
  }, []);

  return (
    <div>
      <h2>My Orders</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {orders.length === 0 ? (
        <p>No orders found.</p>
      ) : (
        <ul>
          {orders.map((order) => (
            <li key={order.id}>
              <Link to={`/order-details/${order.id}`}>
                {order.pickupLocation} to {order.dropoffLocation} - Status: {order.status}
              </Link>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default MyOrders;