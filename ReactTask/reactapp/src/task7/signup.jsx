import React, { Component } from 'react';
import axios from 'axios';

class Signuppage extends Component {
  constructor(props) {
    super(props);
    this.state = {
      first_name: '',
      last_name: '',
      email: '',
      password: '',
      confirmPassword: '',
      company: '',
      phone_number: '',
      username: '',
      error: '',
    };
  }

  validateEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
  };

  validatePasswordFormat = (password) => {
    const passwordRegex = /^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    return passwordRegex.test(password);
  };

  handleSignup = async () => {
    try {
      const {
        first_name,
        last_name,
        email,
        password,
        confirmPassword,
        company,
        phone_number,
        username,
      } = this.state;

      if (
        !first_name ||
        !last_name ||
        !email ||
        !password ||
        password !== confirmPassword ||
        !company ||
        !phone_number ||
        !username
      ) {
        this.setState({ error: 'Please fill in all the required fields.' });
        return;
      }

      if (!this.validateEmail(email)) {
        this.setState({ error: 'Invalid email format.' });
        return;
      }

      if (!this.validatePasswordFormat(password)) {
        this.setState({
          error:
            'Password must be at least 8 characters long and contain at least 1 uppercase letter, 1 special character, and 1 number.',
        });
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
      this.setState({ error: 'Signup failed. Please try again.' });
    }
  };

  render() {
    const {
      first_name,
      last_name,
      email,
      password,
      confirmPassword,
      company,
      phone_number,
      username,
      error,
    } = this.state;

    return (
      <div>
        <h2>Signup</h2>
        {error && <p style={{ color: 'red' }}>{error}</p>}

        <label>First Name:</label>
        <input
          type="text"
          value={first_name}
          placeholder='Please enter your name'
          onChange={(e) => this.setState({ first_name: e.target.value })}
          required
        /><br></br>
        <label>Last Name:</label>
        <input
          type="text"
          value={last_name}
          placeholder='Please enter your name'
          onChange={(e) => this.setState({ last_name: e.target.value })}
          required
        /><br></br>
        <label>Email:</label>
        <input
          type="text"
          value={email}
          placeholder='Enter your email id'
          onChange={(e) => this.setState({ email: e.target.value })}
          required
        /><br></br>

        <label>Password:</label>
        <input
          type="password"
          value={password}
          placeholder='Enter your password'
          onChange={(e) => this.setState({ password: e.target.value })}
          required
        /><br></br><br />

        <label>Confirm Password:</label>
        <input
          type="password"
          value={confirmPassword}
          placeholder='Confirm your password'
          onChange={(e) => this.setState({ confirmPassword: e.target.value })}
        /><br></br><br />

        <label>Company:</label>
        <input
          type="text"
          value={company}
          placeholder='Enter your company name'
          onChange={(e) => this.setState({ company: e.target.value })}
          required
        /><br></br>

        <label>Mobile Number:</label>
        <input
          type="text"
          placeholder='Enter your phone number with country code'
          value={phone_number}
          onChange={(e) => this.setState({ phone_number: e.target.value })}
          required
        /><br></br>

        <label>Username:</label>
        <input
          type="text"
          value={username}
          placeholder='Enter  your name'
          onChange={(e) => this.setState({ username: e.target.value })}
          required
        /><br></br>
        <button type="submit" onClick={this.handleSignup}>Signup</button>
      </div>
    );
  }
}

export default Signuppage;