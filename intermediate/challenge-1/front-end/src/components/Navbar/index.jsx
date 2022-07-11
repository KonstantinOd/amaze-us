import React from 'react';
import { Link } from 'react-router-dom';

import './index.scss';

const links = [
  { to: '/', label: 'Home' }
  // { to: '/bus-schedules', label: 'Bus Schedules' },
  // { to: '/driver-schedules', label: 'Driver Schedules' }
];

const Navbar = () => (
  <nav className={'navbar-wrp'}>
    <ul className={'navbar-wrp__list'}>
      {links.map(({ to, label }, index) => (
        <li key={index} className={'navbar-wrp__list__item'}>
          <Link to={to} className={'navbar-wrp__list__link'}>
            {label}
          </Link>
        </li>
      ))}
    </ul>
  </nav>
);

export default Navbar;
