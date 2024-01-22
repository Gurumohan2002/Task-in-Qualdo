import React, { useState } from 'react';
import axios from 'axios';

const Signup = () => {
  const [first_name, setFirstName] = useState('');
  const [last_name, setLastName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [company, setCompany] = useState('');
  const [phone_number, setPhoneNumber] = useState('');
  const [username, setUsername] = useState('');
  const [error, setError] = useState('');

  const validateEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };

  const validatePasswordFormat = (password) => {
    const passwordRegex = /^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    return passwordRegex.test(password);
  };

  const handleSignup = async () => {
    try {
   
      if (
        !first_name ||
        !last_name ||
        !company ||
        !phone_number ||
        !username ||
        !validateEmail(email) ||
        !validatePasswordFormat(password) ||
        password !== confirmPassword
      ) {
        setError('Please fill in all the required fields with the correct formats.');
        return;
      }

      const response = await axios.post(
        'https://dev-qualdo.eastus.cloudapp.azure.com/iam/signup',
        {
          first_name,
          last_name,
          email,
          password,
          company,
          phone_number,
          username,
          user_signup_type: 'qualdo_db_auth',
        },
        {
          headers: {
            'Api-Type': 'qualdo_db_auth',
          },
        }
      );

      console.log(response.data);
    } catch (error) {
      console.error('Signup failed:', error.message);
      setError('Signup failed. Please try again.');
    }
  };

  return (
    <div>
      <h2>Signup</h2>
      {error && <p style={{ color: 'red' }}>{error}</p>}

      <label>First Name:</label>
      <input type="text" value={first_name} onChange={(e) => setFirstName(e.target.value)} required /><br></br>
      <label>Last Name:</label>
      <input type="text" value={last_name} onChange={(e) => setLastName(e.target.value)} required /><br></br>
      <label>Email:</label>
      <input type="text" value={email} onChange={(e) => setEmail(e.target.value)} required /><br></br>

      <label>Password:</label>
      <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required /><br></br>

      <label>Confirm Password:</label>
      <input
        type="password"
        value={confirmPassword}
        onChange={(e) => setConfirmPassword(e.target.value)}
      /><br></br>

      <label>Company:</label>
      <input type="text" value={company} onChange={(e) => setCompany(e.target.value)} required /><br></br>

      <label>Mobile Number:</label>
      <input type="text" value={phone_number} onChange={(e) => setPhoneNumber(e.target.value)} required /><br></br>

      <label>Username:</label>
      <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} required /><br></br>

      <button type='submit' onClick={handleSignup}>Signup</button>
    </div>
  );
};

export default Signup;