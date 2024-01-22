import React, { Component } from 'react';
import axios from 'axios';

class Signup1 extends Component {
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
        !company ||
        !phone_number ||
        !username ||
        !this.validateEmail(email) ||
        !this.validatePasswordFormat(password) ||
        password !== confirmPassword
      ) {
        this.setState({
          error: 'Please fill in all the required fields with the correct formats.',
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
      this.setState({
        error: 'Signup failed. Please try again.',
      });
    }
  };

  render() {
    const { error, first_name, last_name, email, password, confirmPassword, company, phone_number, username } = this.state;

    return (
      <div>
        <h2>Signup</h2>
        {error && <p style={{ color: 'red' }}>{error}</p>}

        <label>First Name:</label>
        <input type="text" value={first_name} onChange={(e) => this.setState({ first_name: e.target.value })} required /><br></br>

        <label>Last Name:</label>
        <input type="text" value={last_name} onChange={(e) => this.setState({ last_name: e.target.value })} required /><br></br>

        <label>Email:</label>
        <input type="text" value={email} onChange={(e) => this.setState({ email: e.target.value })} required /><br></br>

        <label>Password:</label>
        <input type="password" value={password} onChange={(e) => this.setState({ password: e.target.value })} required /><br></br>

        <label>Confirm Password:</label>
        <input
          type="password"
          value={confirmPassword}
          onChange={(e) => this.setState({ confirmPassword: e.target.value })}
        /><br></br>

        <label>Company:</label>
        <input type="text" value={company} onChange={(e) => this.setState({ company: e.target.value })} required /><br></br>

        <label>Mobile Number:</label>
        <input type="text" value={phone_number} onChange={(e) => this.setState({ phone_number: e.target.value })} required /><br></br>

        <label>Username:</label>
        <input type="text" value={username} onChange={(e) => this.setState({ username: e.target.value })} required /><br></br>

        <button type='button' onClick={this.handleSignup}>Signup</button>
      </div>
    );
  }
}

export default Signup1;
