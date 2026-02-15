import React, { useEffect, useState } from 'react';
import { Search, Plus, Edit, Trash2, QrCode } from 'lucide-react';
import api from '../services/api';
import Modal from '../components/Modal';
import './Equipment.css';

const Equipment: React.FC = () => {
  const [equipments, setEquipments] = useState([]);
  const [categories, setCategories] = useState([]);
  const [statuses, setStatuses] = useState([]);
  const [loading, setLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  
  // Form State
  const [formData, setFormData] = useState({
    numero_serie_equipamento: '',
    matricula_equipamento: '',
    id_categoria_equipamento: 0,
    id_status_equipamento: 0
  });

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    setLoading(true);
    try {
      const [equiRes, catRes, statRes] = await Promise.all([
        api.get('/equipamento/getAllEquipamentos'),
        api.get('/categoria/getAllCategorias'),
        api.get('/status/getAllStatus')
      ]);
      setEquipments(equiRes.data);
      setCategories(catRes.data);
      setStatuses(statRes.data);
    } catch (error) {
      console.error("Erro ao buscar dados", error);
    } finally {
      setLoading(false);
    }
  };

  const handleCreate = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await api.post('/equipamento/createEquipmanento', {
        ...formData,
        id_categoria_equipamento: Number(formData.id_categoria_equipamento),
        id_status_equipamento: Number(formData.id_status_equipamento)
      });
      setIsModalOpen(false);
      setFormData({
        numero_serie_equipamento: '',
        matricula_equipamento: '',
        id_categoria_equipamento: 0,
        id_status_equipamento: 0
      });
      fetchData(); // Refresh list
    } catch (error: any) {
      alert("Erro ao criar equipamento: " + (error.response?.data?.detail || "Verifique os dados"));
    }
  };

  return (
    <div className="page-container">
      <header className="page-header">
        <div>
          <h1>Equipamentos</h1>
          <p className="subtitle">Gerencie o estoque de Chromebooks e periféricos</p>
        </div>
        <button className="btn-primary" onClick={() => setIsModalOpen(true)}>
          <Plus size={20} />
          <span>Novo Equipamento</span>
        </button>
      </header>

      <div className="filters-bar glass-card">
        <div className="search-box">
          <Search size={20} color="var(--text-muted)" />
          <input type="text" placeholder="Buscar por número de série ou matrícula..." />
        </div>
        <div className="actions">
          <button className="btn-secondary">
             <QrCode size={18} />
             Escaneamento Rápido
          </button>
        </div>
      </div>

      <div className="table-container glass-card">
        {loading ? (
          <div className="loader">Carregando itens...</div>
        ) : (
          <table className="custom-table">
            <thead>
              <tr>
                <th>Matrícula</th>
                <th>Série</th>
                <th>Categoria</th>
                <th>Status</th>
                <th>Carregador</th>
                <th>Ações</th>
              </tr>
            </thead>
            <tbody>
              {equipments.map((item: any, idx: number) => (
                <tr key={idx}>
                  <td><span className="badge-matricula">{item.matricula_equipamento}</span></td>
                  <td>{item.numero_serie_equipamento}</td>
                  <td>{item.categoria_equipamento}</td>
                  <td>
                    <span className={`status-badge ${(item.status_equipamento || '').toLowerCase().replace(' ', '-')}`}>
                      {item.status_equipamento}
                    </span>
                  </td>
                  <td>{item.carregador?.matricula_carregador || 'N/A'}</td>
                  <td className="actions-cell">
                    <button className="icon-btn edit"><Edit size={16} /></button>
                    <button className="icon-btn delete"><Trash2 size={16} /></button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>

      <Modal 
        isOpen={isModalOpen} 
        onClose={() => setIsModalOpen(false)} 
        title="Novo Equipamento"
      >
        <form onSubmit={handleCreate} className="modal-form">
          <div className="form-group">
            <label>Número de Série (15 caracteres)</label>
            <input 
              type="text" 
              className="input-field" 
              placeholder="Ex: Qwz803dftTp8MsC"
              value={formData.numero_serie_equipamento}
              onChange={(e) => setFormData({...formData, numero_serie_equipamento: e.target.value})}
              required
            />
          </div>

          <div className="form-group">
            <label>Matrícula (Ex: E0001)</label>
            <input 
              type="text" 
              className="input-field" 
              placeholder="Ex: E0001"
              value={formData.matricula_equipamento}
              onChange={(e) => setFormData({...formData, matricula_equipamento: e.target.value})}
              required
            />
          </div>

          <div className="form-group">
            <label>Categoria</label>
            <select 
              className="input-field"
              value={formData.id_categoria_equipamento}
              onChange={(e) => setFormData({...formData, id_categoria_equipamento: Number(e.target.value)})}
              required
            >
              <option value="">Selecione...</option>
              {categories.map((c: any) => (
                <option key={c.id} value={c.id}>{c.categoria}</option>
              ))}
            </select>
          </div>

          <div className="form-group">
            <label>Status</label>
            <select 
              className="input-field"
              value={formData.id_status_equipamento}
              onChange={(e) => setFormData({...formData, id_status_equipamento: Number(e.target.value)})}
              required
            >
              <option value="">Selecione...</option>
              {statuses.map((s: any) => (
                <option key={s.id} value={s.id}>{s.status}</option>
              ))}
            </select>
          </div>

          <button type="submit" className="btn-primary" style={{marginTop: '20px'}}>
            Salvar Equipamento
          </button>
        </form>
      </Modal>
    </div>
  );
};

export default Equipment;

