import { useState } from 'react';
import './App.css';

const defaultUsers = [
  { 
    email: 'user5@example.com', 
    first_name: 'User5', 
    last_name: 'Test', 
    resources_to_grant: [ 
      { name: 'rodo-eks-db', 'type': 'POSTGRES' }
    ], 
    resources_to_revoke: [] 
  }
];

function App() {
  const [status, setStatus] = useState('');
  const [users, setUsers] = useState(JSON.stringify(defaultUsers, null, 2));
  const baseUrl = process.env.REACT_APP_API_BASE_URL || '';

  const sendData = () => {
    setStatus('');
    setUsers(JSON.stringify(JSON.parse(users), null, 2));
    fetch(`${baseUrl}/api/v1/user-resources`, { 
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: users
    }).then(() => {
        setStatus('Users changed :-)');
      })
      .catch(error => console.log(error));    
  };

  const handleUsersChange = function(event) {
    setUsers(event.target.value);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Update user resources</h1>
        <p><small>Simple app that uses the SDM API to update user resources</small></p>
        <textarea 
          value={users} 
          onChange={handleUsersChange}
          rows="20"
          cols="50" 
        />
        <p>{status}</p>
        <button onClick={sendData}>Send data</button>
      </header>
    </div>
  );
}

export default App;
