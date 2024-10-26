// App.js
import React from "react";
import "./App.css";
import Registration from './registration.js';
import Login from './Login.js'; 

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to the App</h1>
        <Login />
        <Registration />
      </header>
    </div>
  );
}

export default App;