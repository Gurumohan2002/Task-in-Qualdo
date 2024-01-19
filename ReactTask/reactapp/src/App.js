// // import React, { Component } from 'react';
// // import Home from './home';
// // import { Route,Router } from 'react-router-dom';

// // class App extends Component {

// //   render() {
// //     return (
// //       <Router>
// //       <div>
// //         <Route exact path='/' component={Home} />
// //       </div>
// //     </Router>

// //     );
// //   }
// // }

// // export default App;

// // App.js
// // import React, { Component } from 'react';
// // import { BrowserRouter as Router, Route, Redirect } from 'react-router-dom';
// // import Home from './home';
// // import Dashboard from './dashboard';

// // class App extends Component {
// //   render() {
// //     return (
// //       <Router>
// //         <div>
// //           {/* Redirect root path to Home component */}
// //           <Route exact path="/" render={() => <Redirect to="/home" />} />
          
// //           {/* Nested route for Home component */}
// //           <Route path="/home" component={Home} />
          
// //           {/* Route for Dashboard component */}
// //           <Route path="/dashboard" component={Dashboard} />
// //         </div>
// //       </Router>
// //     );
// //   }
// // }

// // export default App;
// // App.js
// // App.js
// import React, { Component } from 'react';
// import { BrowserRouter as Router, Route } from 'react-router-dom';
// // import Dashboard from './dashboard';
// import Login from './task5/login';

// class App extends Component {
//   render() {
//     return (
//       <Router>
//         <div>
//           {/* Route for Home component */}
//           <h2>Login Page</h2>
//           <Route exact path="/" component={Login} />
//           {/* Route for Dashboard component */}
//           {/* <Route path="/dashboard" component={Dashboard} /> */}
//         </div>
//       </Router>
//     );
//   }
// }

// export default App;

import React, { Component } from 'react';
import { Routes, Route, Link, BrowserRouter as Router } from 'react-router-dom';
import MyTable from "./task1/table";
import MyForm from './task1/form';
import MyFormElements from './task1/formelements';
import AddNumbers from './task2/index';
import JSONData from "./task3/index1";
import ApiCall from "./task4/index2";
import Dashboard from './dashboard';
import Logout from './task7/logout';
import Loginpage from './task7/login';
import Signuppage from './task7/signup';
import './App.css';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      isAuthenticated: false,
    };
  }

  handleLogin = () => {
    this.setState({ isAuthenticated: true });
  };

  handleLogout = () => {
    this.setState({ isAuthenticated: false });
  };

  render() {
    const { isAuthenticated } = this.state;
    const { history } = this.props;

    return (
      <Router>
        <div>
          <nav>
            <ul>
              {isAuthenticated ? (
                <>
                  <li>
                    <Link to="/logout">Logout</Link>
                  </li>
                  <li>
                    <Link to="/layout">Dashboard</Link>
                  </li>
                </>
              ) : (
                <>
                  <li>
                    <Link to="/login">Login</Link>
                  </li>
                  <li>
                    <Link to="/signup">Signup</Link>
                  </li>
                </>
              )}
            </ul>
          </nav>
          <Routes>
            <Route
              path="/logout"
              element={<Logout onLogout={this.handleLogout} />}
            />
            <Route
              path="/login"
              element={<Loginpage onLogin={this.handleLogin} history={history} />}
            />
            <Route path="/signup" element={<Signuppage />} />
            <Route path="/layout" element={<Dashboard />} />
            <Route path="/table" element={<MyTable />} />
            <Route path="/form" element={<MyForm />} />
            <Route path="/formelements" element={<MyFormElements />} />
            <Route path="/index" element={<AddNumbers />} />
            <Route path="/index1" element={<JSONData />} />
            <Route path="/index2" element={<ApiCall />} />
          </Routes>
        </div>
      </Router>
    );
  }
}

export default App;
