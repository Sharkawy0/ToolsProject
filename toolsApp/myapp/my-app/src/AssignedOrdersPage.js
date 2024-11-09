// AssignedOrdersPage.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AssignedOrdersPage = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    async function fetchOrders() {
      const response = await axios.get('/api/courier/orders');
      setOrders(response.data);
    }
    fetchOrders();
  }, []);

  const handleOrderStatus = async (orderId, status) => {
    await axios.post(`/api/courier/orders/${orderId}/status`, { status });
    setOrders(orders.map(order => order.id === orderId ? { ...order, status } : order));
  };


  return (
    <div>
      <h2>Assigned Orders</h2>
      {orders.map(order => (
        <div key={order.id}>
          <p>Order ID: {order.id} - Status: {order.status}</p>
          <button onClick={() => handleOrderStatus(order.id, 'Accepted')}>Accept</button>
          <button onClick={() => handleOrderStatus(order.id, 'Declined')}>Decline</button>
        </div>
      ))}
    </div>
  );
};

// Update order status in AssignedOrdersPage.js
const handleOrderProgress = async (orderId, status) => {
    await axios.post(`/api/courier/orders/${orderId}/status`, { status });
    setOrders(orders.map(order => order.id === orderId ? { ...order, status } : order));
  };
  
  // In render for each order
  <select onChange={(e) => handleOrderProgress(order.id, e.target.value)}>
    <option value="Picked Up">Picked Up</option>
    <option value="In Transit">In Transit</option>
    <option value="Delivered">Delivered</option>
  </select>
  

export default AssignedOrdersPage;