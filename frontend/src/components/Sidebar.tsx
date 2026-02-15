import React from 'react';
import { NavLink } from 'react-router-dom';
import { 
  LayoutDashboard, 
  Laptop, 
  Users, 
  ClipboardList, 
  UserCircle, 
  LogOut,
  QrCode,
  Tag
} from 'lucide-react';
import './Sidebar.css';

const Sidebar: React.FC = () => {
  const handleLogout = () => {
    localStorage.removeItem('token');
    window.location.href = '/login';
  };

  return (
    <aside className="sidebar glass-card">
      <div className="sidebar-header">
        <QrCode className="logo-icon" size={32} />
        <h2>Stock<span>QR</span></h2>
      </div>

      <nav className="sidebar-nav">
        <NavLink to="/" className={({ isActive }) => isActive ? 'nav-item active' : 'nav-item'}>
          <LayoutDashboard size={20} />
          <span>Dashboard</span>
        </NavLink>

        <NavLink to="/equipment" className={({ isActive }) => isActive ? 'nav-item active' : 'nav-item'}>
          <Laptop size={20} />
          <span>Equipamentos</span>
        </NavLink>

        <NavLink to="/users" className={({ isActive }) => isActive ? 'nav-item active' : 'nav-item'}>
          <Users size={20} />
          <span>Usuários</span>
        </NavLink>

        <NavLink to="/loans" className={({ isActive }) => isActive ? 'nav-item active' : 'nav-item'}>
          <ClipboardList size={20} />
          <span>Empréstimos</span>
        </NavLink>

        <NavLink to="/categories" className={({ isActive }) => isActive ? 'nav-item active' : 'nav-item'}>
          <Tag size={20} />
          <span>Categorias</span>
        </NavLink>

        <NavLink to="/profile" className={({ isActive }) => isActive ? 'nav-item active' : 'nav-item'}>
          <UserCircle size={20} />
          <span>Perfil</span>
        </NavLink>
      </nav>

      <div className="sidebar-footer">
        <button onClick={handleLogout} className="logout-btn">
          <LogOut size={20} />
          <span>Sair</span>
        </button>
      </div>
    </aside>
  );
};

export default Sidebar;
