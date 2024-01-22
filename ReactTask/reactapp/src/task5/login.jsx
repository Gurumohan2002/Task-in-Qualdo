import React, { useState } from 'react';
import axios from 'axios';

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async () => {
    try {
     
      if (!email || !password) {
        setError('Please enter both email and password.');
        return;
      }

      const response = await axios.post('https://dev-qualdo.eastus.cloudapp.azure.com/iam/login',
       {
        email,
        password,
      },
      {headers:{
        "Api-Type":"qualdo_db_auth"
      },
    });


      console.log(response.data);
      
    } catch (error) {

      console.error('Login failed:', error.message);
      setError('Login failed. Please check your credentials.');
    }
  };

  return (
    <div className="col-sm-6 offset-sm-3">
      <h2>Login</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      <label>Email:</label>
      <input type="email" className='form-control' value={email} onChange={(e) => setEmail(e.target.value)} required/>
      <br />
      <label>Password:</label>
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required/>
      <br />
      <button type="submit" onClick={handleLogin}>Login</button>
    </div>
  );
};

export default Login;