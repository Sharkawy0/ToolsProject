// ManageOrdersPage.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ManageOrdersPage = () => {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
    async function fetchOrders() {
      const response = await axios.get('/api/admin/orders');
      setOrders(response.data);
    }
    fetchOrders();
  }, []);

  const updateOrderStatus = async (orderId, status) => {
    await axios.post(`/api/admin/orders/${orderId}/status`, { status });
    setOrders(orders.map(order => order.id === orderId ? { ...order, status } : order));
  };

  const deleteOrder = async (orderId) => {
    await axios.delete(`/api/admin/orders/${orderId}`);
    setOrders(orders.filter(order => order.id !== orderId));
  };

  return (
    <div>
      <h2>Manage Orders</h2>
      <table>
        <thead>
          <tr>
            <th>Order ID</th>
            <th>Status</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {orders.map(order => (
            <tr key={order.id}>
              <td>{order.id}</td>
              <td>{order.status}</td>
              <td>
                <select onChange={(e) => updateOrderStatus(order.id, e.target.value)}>
                  <option value="Pending">Pending</option>
                  <option value="In Progress">In Progress</option>
                  <option value="Completed">Completed</option>
                </select>
                <button onClick={() => deleteOrder(order.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ManageOrdersPage;