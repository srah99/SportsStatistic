import React, { useState } from 'react';
import './App.css';

function App() {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = () => {
    if (file) {
      // Code to read the file and process the data
      console.log('File uploaded:', file.name);
      // Add your logic to parse and calculate statistics here
    }
  };

  return (
    <div className="App">
      <input type="file" onChange={handleFileChange} accept=".csv" />
      <button className="btn-3d" onClick={handleSubmit}>Send</button>
    </div>
  );
}

export default App;
