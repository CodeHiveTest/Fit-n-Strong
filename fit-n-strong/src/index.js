import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import reportWebVitals from './reportWebVitals';
import "primereact/resources/themes/lara-light-indigo/theme.css";     
import "primereact/resources/primereact.min.css";
import "primeflex/primeflex.css";
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import Home from './routes/Home';
import Navbar from './components/navbar';
import Rutinas from './routes/Rutinas';
import VerRutina from './routes/VerRutina';
import 'bootstrap/dist/css/bootstrap.min.css';
                                       
const root = ReactDOM.createRoot(document.getElementById('root'));
const routes = createBrowserRouter([
  {path: '/', element: <Home></Home>, errorElement: <h1>Error 404</h1>}, 
  {path: '/rutinas', element: <Rutinas></Rutinas>},
  {path: '/ver-rutina/:id', element: <VerRutina></VerRutina>}
]);

root.render(
  <React.StrictMode>
  <Navbar></Navbar>
  <RouterProvider router={routes}></RouterProvider>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
