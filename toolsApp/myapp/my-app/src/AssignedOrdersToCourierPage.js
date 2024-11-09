// AssignedOrdersToCourierPage.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

const AssignedOrdersToCourierPage = () => {
  const [orders, setOrders] = useState([]);
  const [couriers, setCouriers] = useState([]);

  useEffect(() => {
    async function fetchOrdersAndCouriers() {
      const [ordersResponse, couriersResponse] = await Promise.all([
        axios.get('/api/admin/assigned-orders'),
        axios.get('/api/admin/couriers')
      ]);
      setOrders(ordersResponse.data);
      setCouriers(couriersResponse.data);
    }
    fetchOrdersAndCouriers();
  }, []);

  const reassignOrder = async (orderId, courierId) => {
    await axios.post(`/api/admin/orders/${orderId}/assign`, { courierId });
    setOrders(orders.map(order => order.id === orderId ? { ...order, courierId } : order));
  };

  return (
    <div>
      <h2>Assigned Orders</h2>
      {orders.map(order => (
        <div key={order.id}>
          <p>Order ID: {order.id} - Assigned to: {order.courierName || 'Unassigned'}</p>
          <select onChange={(e) => reassignOrder(order.id, e.target.value)}>
            <option value="">Select Courier</option>
            {couriers.map(courier => (
              <option key={courier.id} value={courier.id}>
                {courier.name}
              </option>
            ))}
          </select>
        </div>
      ))}
    </div>
  );
};

export default AssignedOrdersToCourierPage;
