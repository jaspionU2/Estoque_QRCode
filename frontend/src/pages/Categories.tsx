import React, { useEffect, useState } from 'react';
import { Plus, Trash2, Tag } from 'lucide-react';
import api from '../services/api';
import Modal from '../components/Modal';
import './Equipment.css'; // Reusing table styles

const Categories: React.FC = () => {
  const [categories, setCategories] = useState([]);
  const [loading, setLoading] = useState(true);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [newCategoryName, setNewCategoryName] = useState('');

  useEffect(() => {
    fetchCategories();
  }, []);

  const fetchCategories = async () => {
    setLoading(true);
    try {
      const response = await api.get('/categoria/getAllCategorias');
      setCategories(response.data);
    } catch (error) {
      console.error("Erro ao buscar categorias", error);
    } finally {
      setLoading(false);
    }
  };

  const handleCreate = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      // The backend expects a list of dicts: list[dict]
      // Based on Model_Categoria: categoria is the field name for the title
      await api.post('/categoria/addNewCategoria', [
        { categoria: newCategoryName }
      ]);
      
      setIsModalOpen(false);
      setNewCategoryName('');
      fetchCategories();
    } catch (error: any) {
      alert("Erro ao criar categoria: " + (error.response?.data?.detail || "Verifique os dados"));
    }
  };

  const handleDelete = async (id: number) => {
    if (!confirm("Deseja realmente excluir esta categoria?")) return;
    
    try {
      await api.delete(`/categoria/deleteOneCategoria${id}`);
      fetchCategories();
    } catch (error) {
      console.error("Erro ao deletar categoria", error);
      alert("Erro ao deletar categoria. Verifique se existem equipamentos vinculados a ela.");
    }
  };

  return (
    <div className="page-container">
      <header className="page-header">
        <div>
          <h1>Categorias</h1>
          <p className="subtitle">Gerencie as classificações dos equipamentos</p>
        </div>
        <button className="btn-primary" onClick={() => setIsModalOpen(true)}>
          <Plus size={20} />
          <span>Nova Categoria</span>
        </button>
      </header>

      <div className="table-container glass-card">
        {loading ? (
          <div className="loader">Carregando categorias...</div>
        ) : (
          <table className="custom-table">
            <thead>
              <tr>
                <th>ID</th>
                <th>Nome da Categoria</th>
                <th style={{ textAlign: 'right' }}>Ações</th>
              </tr>
            </thead>
            <tbody>
              {categories.map((cat: any) => (
                <tr key={cat.id}>
                  <td><span className="badge-matricula">{cat.id}</span></td>
                  <td>
                    <div className="flex-row">
                      <Tag size={16} className="text-muted" />
                      {cat.categoria}
                    </div>
                  </td>
                  <td className="actions-cell" style={{ justifyContent: 'flex-end' }}>
                    <button 
                      className="icon-btn delete" 
                      onClick={() => handleDelete(cat.id)}
                    >
                      <Trash2 size={16} />
                    </button>
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
        title="Nova Categoria"
      >
        <form onSubmit={handleCreate} className="modal-form">
          <div className="form-group">
            <label>Nome da Categoria</label>
            <input 
              type="text" 
              className="input-field" 
              placeholder="Ex: Chromebook, Mouse, Carregador..."
              value={newCategoryName}
              onChange={(e) => setNewCategoryName(e.target.value)}
              required
            />
          </div>

          <button type="submit" className="btn-primary" style={{ marginTop: '20px' }}>
            Salvar Categoria
          </button>
        </form>
      </Modal>
    </div>
  );
};

export default Categories;
