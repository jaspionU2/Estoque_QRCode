import React, { useEffect, useState } from 'react';
import { Plus, GraduationCap, School } from 'lucide-react';
import api from '../services/api';
import './Equipment.css'; // Reusing table styles

const Users: React.FC = () => {
  const [students, setStudents] = useState([]);
  const [professors, setProfessors] = useState([]);
  const [activeTab, setActiveTab] = useState<'students' | 'professors'>('students');
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchUsers();
  }, []);

  const fetchUsers = async () => {
    try {
      const [stdRes, profRes] = await Promise.all([
        api.get('/usuario/getAllAlunos'),
        api.get('/usuario/getAllProfessores')
      ]);
      setStudents(stdRes.data);
      setProfessors(profRes.data);
    } catch (error) {
      console.error("Erro ao buscar usuários", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-container">
      <header className="page-header">
        <div>
          <h1>Usuários</h1>
          <p className="subtitle">Gerencie Alunos e Professores cadastrados</p>
        </div>
        <button className="btn-primary">
          <Plus size={20} />
          <span>Novo Usuário</span>
        </button>
      </header>

      <div className="tab-bar">
        <button 
          className={activeTab === 'students' ? 'tab-btn active' : 'tab-btn'}
          onClick={() => setActiveTab('students')}
        >
          <GraduationCap size={18} />
          Alunos
        </button>
        <button 
          className={activeTab === 'professors' ? 'tab-btn active' : 'tab-btn'}
          onClick={() => setActiveTab('professors')}
        >
          <School size={18} />
          Professores
        </button>
      </div>

      <div className="table-container glass-card">
        {loading ? (
          <div className="loader">Carregando usuários...</div>
        ) : (
          <table className="custom-table">
            <thead>
              {activeTab === 'students' ? (
                <tr>
                  <th>Nome</th>
                  <th>Série</th>
                  <th>Turma</th>
                  <th>Ações</th>
                </tr>
              ) : (
                <tr>
                  <th>Nome</th>
                  <th>Matéria</th>
                  <th>Ações</th>
                </tr>
              )}
            </thead>
            <tbody>
              {activeTab === 'students' ? (
                students.map((item: any) => (
                  <tr key={item.id_aluno}>
                    <td>{item.nome_aluno}</td>
                    <td>{item.serie_aluno}ª Série</td>
                    <td>{item.turma_aluno}</td>
                    <td className="actions-cell">
                       {/* Actions same as equipment */}
                    </td>
                  </tr>
                ))
              ) : (
                professors.map((item: any) => (
                  <tr key={item.id_professor}>
                    <td>{item.nome_professor}</td>
                    <td>{item.nome_materia || 'N/A'}</td>
                    <td className="actions-cell">
                       {/* Actions */}
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
};

export default Users;
