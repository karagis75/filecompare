
import './App.css';
import React, { useState, useEffect } from 'react'; 

  function App() {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
  
    useEffect(() => {
      const fetchData = async () => {
        try {
          const response = await fetch('https://services.nvd.nist.gov/rest/json/cves/2.0?cveId=CVE-2019-1010218');
          if (!response.ok) {
            throw new Error('Failed to fetch data');
          }
          const jsonData = await response.json();
          setData(jsonData);
        } catch (error) {
          setError(error.message);
        } finally {
          setLoading(false);
        }
      };
  
      fetchData();
    }, []);
  
    if (loading) return <div>Loading...</div>;
    if (error) return <div>Error: {error}</div>;
    if (!data) return null;
  
    return (
      <div>
        <h1>Data from API</h1>
        <pre>{JSON.stringify(data, null, 2)}</pre>
      </div>
    );
  }
  
  export default App;