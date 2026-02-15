import React, { useEffect, useState } from 'react';
import { Laptop, ClipboardCheck, History, AlertCircle } from 'lucide-react';
import api from '../services/api';
import './Dashboard.css';

const Dashboard: React.FC = () => {
  const [stats, setStats] = useState({
    total: 0,
    available: 0,
    inUse: 0,
    maintenance: 0,
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const response = await api.get('/equipamento/getAllEquipamentos');
        const equipments = response.data;
        
        setStats({
          total: equipments.length,
          available: equipments.filter((e: any) => e.status_equipamento === 'Disponível').length,
          inUse: equipments.filter((e: any) => e.status_equipamento === 'Em uso').length,
          maintenance: equipments.filter((e: any) => e.status_equipamento === 'Em manutenção').length,
        });
      } catch (error) {
        console.error("Erro ao buscar estatísticas", error);
      } finally {
        setLoading(false);
      }
    };

    fetchStats();
  }, []);

  if (loading) return <div>Carregando Dashboard...</div>;

  return (
    <div className="dashboard-container">
      <header>
        <h1>Dashboard</h1>
        <p className="subtitle">Visão geral do sistema de estoque</p>
      </header>

      <section className="stats-grid">
        <div className="stat-card glass-card">
          <div className="stat-icon total"><Laptop /></div>
          <div className="stat-info">
            <h3>Total</h3>
            <span className="value">{stats.total}</span>
          </div>
        </div>

        <div className="stat-card glass-card">
          <div className="stat-icon available"><ClipboardCheck /></div>
          <div className="stat-info">
            <h3>Disponíveis</h3>
            <span className="value">{stats.available}</span>
          </div>
        </div>

        <div className="stat-card glass-card">
          <div className="stat-icon inuse"><History /></div>
          <div className="stat-info">
            <h3>Em Uso</h3>
            <span className="value">{stats.inUse}</span>
          </div>
        </div>

        <div className="stat-card glass-card">
          <div className="stat-icon alert"><AlertCircle /></div>
          <div className="stat-info">
            <h3>Manutenção</h3>
            <span className="value">{stats.maintenance}</span>
          </div>
        </div>
      </section>

      <section className="dashboard-main grid-1-1">
        <div className="chart-card glass-card">
          <h2>Distribuição de Equipamentos</h2>
          <div className="chart-placeholder">
             {/* Simple SVG Chart */}
             <svg viewBox="0 0 100 60" className="bar-chart">
               <rect x="10" y={60 - (stats.available * 4)} width="15" height={stats.available * 4} fill="var(--success)" rx="2" />
               <rect x="42" y={60 - (stats.inUse * 4)} width="15" height={stats.inUse * 4} fill="var(--primary)" rx="2" />
               <rect x="75" y={60 - (stats.maintenance * 4)} width="15" height={stats.maintenance * 4} fill="var(--error)" rx="2" />
             </svg>
             <div className="chart-labels">
               <span>Disp.</span>
               <span>Uso</span>
               <span>Mant.</span>
             </div>
          </div>
        </div>

        <div className="recent-card glass-card">
          <h2>Atividades Recentes</h2>
          <div className="activity-list">
             <div className="activity-item">
               <div className="dot available"></div>
               <div className="activity-info">
                 <p>Novo Chromebook cadastrado</p>
                 <span>Há 2 horas</span>
               </div>
             </div>
             <div className="activity-item">
               <div className="dot inuse"></div>
               <div className="activity-info">
                 <p>Empréstimo realizado p/ Aluno João</p>
                 <span>Há 5 horas</span>
               </div>
             </div>
          </div>
        </div>
      </section>
    </div>
  );
};

export default Dashboard;
