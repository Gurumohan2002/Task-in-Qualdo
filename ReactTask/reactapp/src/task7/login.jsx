import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

const Loginpage = ({ onLogin }) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [successMessage, setSuccessMessage] = useState("");
  const navigate = useNavigate();

  const validateEmail = (email) => {
    const emailRegex = /.com$/i;
    return emailRegex.test(email);
  };

  const validatePassword = (password) => {
    const passwordRegex =
      /^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    return passwordRegex.test(password);
  };
  const navigateToSignup = () => {
    
    navigate('/signup');
  };

  const handleLogin = async () => {
    if (!email || !password) {
      setError("Please enter both email and password.");
      return;
    }

    if (!validateEmail(email)) {
      setError('Email must end with "@gmail.com".');
      return;
    }

    if (!validatePassword(password)) {
      setError(
        "Password must be at least 8 characters long and contain at least 1 uppercase letter, 1 special character, and 1 number."
      );
      setSuccessMessage("");
      return;
    }

    try {
      const response = await axios.post(
        "https://dev-qualdo.eastus.cloudapp.azure.com/iam/login",
        { email, password },
        {
          headers: {
            "Api-Type": "qualdo_db_auth",
          },
        }
      );

      if (response && response.data) {
        if (response.data.account_features.code === 200) {
          onLogin();
          navigate("/layout"); // Redirect to the home page
          setSuccessMessage("Login successful:");
          setError("");
        }
      }
    } catch (error) {
      console.error("Login failed:", error.message);
      setError("Login failed. Please check your credentials.");
      setSuccessMessage("");
    }
  };

  return (
    <div>
      <h2>Login</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {successMessage && <p style={{ color: "green" }}>{successMessage}</p>}
      <label>Email:</label>
      <input
        type="email"
        className="form-control"
        value={email}
        placeholder="Enter a valid email id"
        onChange={(e) => setEmail(e.target.value)}
        required
      />
      <br />
      <label>Password:</label>
      <input
        type="password"
        value={password}
        placeholder="Enter the password"
        onChange={(e) => setPassword(e.target.value)}
        required
      />
      <br /><br></br>
      <button type="button"  onClick={handleLogin}>
        Login
      </button> &nbsp; &nbsp;
      <button type="button" onClick={navigateToSignup}>
        Signup</button>
    </div>
  );
};

export default Loginpage;