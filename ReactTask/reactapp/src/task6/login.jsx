import React, { Component } from 'react';
import axios from 'axios';

class Login1 extends Component {
  constructor(props) {
    super(props);
    this.state = {
      email: '',
      password: '',
      error: '',
    };
  }

  handleLogin = async () => {
    try {
      const { email, password } = this.state;

      if (!email || !password) {
        this.setState({ error: 'Please enter both email and password.' });
        return;
      }

      const response = await axios.post(
        'https://dev-qualdo.eastus.cloudapp.azure.com/iam/login',
        {
          email,
          password,
        },
        {
          headers: {
            'Api-Type': 'qualdo_db_auth',
          },
        }
      );

      console.log(response.data);
    } catch (error) {
      console.error('Login failed:', error.message);
      this.setState({ error: 'Login failed. Please check your credentials.' });
    }
  };

  render() {
    const { email, password, error } = this.state;

    return (
      <div className="col-sm-6 offset-sm-3">
        <h2>Login</h2>
        {error && <p style={{ color: 'red' }}>{error}</p>}
        <label>Email:</label>
        <input
          type="email"
          className="form-control"
          value={email}
          onChange={(e) => this.setState({ email: e.target.value })}
          required
        />
        <br />
        <label>Password:</label>
        <input
          type="password"
          value={password}
          onChange={(e) => this.setState({ password: e.target.value })}
          required
        />
        <br />
        <button type="button" onClick={this.handleLogin}>
          Login
        </button>
      </div>
    );
  }
}

export default Login1;
