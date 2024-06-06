import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    <iframe 
    width="600" 
    height="450" 
    style={{ border: 0 }}   
    loading="lazy" 
    allowFullScreen 
    src="https://www.google.com/maps/embed/v1/view?zoom=15&center=34.0442%2C-118.2439&key=AIzaSyAmjKtxOHaWhPsBgkRYb5akhEOh5TMoMCI">
    </iframe>
    </div>

  );
}

export default App;
