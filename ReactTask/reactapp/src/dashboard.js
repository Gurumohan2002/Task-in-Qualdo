// import React from "react";
// import MyTable from "./task1/table";
// import MyForm from './task1/form';
// import MyFormElements from './task1/formelements';
// import AddNumbers from './task2/index';
// import JSONData from "./task3/index1";
// import ApiCall from "./task4/index2";
// import Login from "./task5/login";
// import Signup from "./task5/signup";
// import Login1 from "./task6/login";
// import Signup1 from "./task6/signup";
// import Login5 from "./task7/login";

// function App() {
//   return (
//     <center><><h2>React with HTML Table</h2><MyTable /><br></br>
//     <h2>React with HTML Form</h2><MyForm /><br></br><h2>React with HTML FormElements</h2><MyFormElements /><br></br>
//     <h2>Adding Two numbers</h2><AddNumbers /><br></br>
//     <h2>JSON Data Display</h2><JSONData /><br></br>
//     <h2>API CALL</h2><ApiCall /><br></br>
//     <h2>LOGIN DEV QUALDO Using function</h2><Login /><br></br>
//     <h2>SIGN UP DEV QUALDO Using function</h2><Signup /><br></br>
//     <h2>LOGIN DEV QUALDO Using Class </h2><Login1 /><br></br>
//     <h2>SIGN UP DEV QUALDO Using Class</h2><Signup1 /><br></br>
//     <h2>Login Page</h2><Login5 /><br></br>
//     </></center>
//   );
//  }
// export default App;
import { Outlet, Link } from "react-router-dom";

const Dashboard = () => {
  return (
    <>
      <nav>
        <ul className="horizontal-nav">
          <li>
            <u><Link to="/Table">Table</Link></u>
          </li>
          <li>
            <u><Link to="/Form">Form</Link></u>
          </li>
          <li>
            <u><Link to="/Formelements">Form Elements</Link></u>
          </li>
          <li>
            <u><Link to="/index">Addition</Link></u>
          </li>
          <li>
            <u><Link to="/index1">Json data in table</Link></u>
          </li>
          <li>
            <u><Link to="/index2">Weather API</Link></u>
          </li>
          {/* <li>
            <u><Link to="/login">Login</Link></u>
          </li>
          <li>
            <u><Link to="/signup">Sign up</Link></u>
          </li> */}
          {/* <li>
            <u><Link to="/loginpage">Login</Link></u>
          </li>
          <li>
            <u><Link to="/signuppage">Sign up</Link></u>
          </li> */}
        </ul>
      </nav>
      <Outlet />
    </>
  );
};

export default Dashboard;