import React, { useState } from "react";
import { BrowserRouter as Router, Routes, Route, Link, Navigate } from "react-router-dom";
import "./App.css";
import Registration from './registration.js';
import Login from './Login.js';
import CreateOrder from './CreateOrder.js';
import MyOrders from './MyOrders.js';
import OrderDetails from './OrderDetails.js';
import AssignedOrdersPage from './AssignedOrdersPage.js';
import ManageOrdersPage from './ManageOrdersPage.js';
import AssignedOrdersToCourierPage from './AssignedOrdersToCourierPage.js';

function App() {
  // State to track if user is signed in, user role, and if an order has been created
  const [isSignedIn, setIsSignedIn] = useState(false);
  const [userRole, setUserRole] = useState(null); // Possible values: "courier", "admin"
  const [orderCreated, setOrderCreated] = useState(false);

  // Function to handle sign-in, setting the user's role
  const handleSignIn = (role) => {
    setIsSignedIn(true);
    setUserRole(role);
  };

  // Function to handle order creation
  const handleOrderCreated = () => {
    setOrderCreated(true);
  };

  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <h1>Welcome to the Delivery Service App</h1>

          {/* Navigation Links */}
          {/*isSignedIn && (
            <nav>
              <Link to="/create-order">Create Order</Link>
            </nav>
          )*/}

          {/* Show login or registration if not signed in */}
          {!isSignedIn && <Login onSignIn={(role) => handleSignIn(role)} />}
          {!isSignedIn && <Registration />}
        </header>

        <Routes>
          {/* Home Route */}
          <Route path="/" element={<h2>Home Page</h2>} />

          {/* Route for CreateOrder page */}
          <Route
            path="/create-order"
            element={<CreateOrder onOrderCreated={handleOrderCreated} />}
          />

          {/* Courier Routes */}
          {isSignedIn && userRole === "courier" && (
            <>
              <Route path="/assigned-orders" element={<AssignedOrdersPage />} />
              <Route path="/update-order-status" element={<AssignedOrdersPage />} />
              {orderCreated && <Route path="/my-orders" element={<MyOrders />} />}
              {orderCreated && <Route path="/order-details/:orderId" element={<OrderDetails />} />}
            </>
          )}

          {/* Admin Routes */}
          {isSignedIn && userRole === "admin" && (
            <>
              <Route path="/manage-orders" element={<ManageOrdersPage />} />
              <Route path="/assigned-orders-to-courier" element={<AssignedOrdersToCourierPage />} />
            </>
          )}

          {/* Redirect to home if path doesn't match */}
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;