import React, { useEffect, useState } from 'react';
import { User, Info } from 'lucide-react';
import api from '../services/api';
import './Equipment.css';

const Loans: React.FC = () => {
  const [loans, setLoans] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchLoans();
  }, []);

  const fetchLoans = async () => {
    try {
      const response = await api.get('/emprestimo/getAllEmprestimosFromAlunos');
      setLoans(response.data);
    } catch (error) {
      console.error("Erro ao buscar empréstimos", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="page-container">
      <header className="page-header">
        <div>
          <h1>Empréstimos</h1>
          <p className="subtitle">Relatório detalhado de retiradas e devoluções</p>
        </div>
      </header>

      <div className="table-container glass-card">
        {loading ? (
          <div className="loader">Carregando relatórios...</div>
        ) : (
          <table className="custom-table">
            <thead>
              <tr>
                <th>Equipamento</th>
                <th>Responsável</th>
                <th>Data Início</th>
                <th>Data Fim</th>
                <th>Motivo</th>
              </tr>
            </thead>
            <tbody>
              {loans.map((loan: any, idx: number) => (
                <tr key={idx}>
                  <td>
                    <div className="flex-col">
                       <strong>{loan.matricula_equipamento}</strong>
                       <span className="small-text">{loan.numero_de_serie_equipamento}</span>
                    </div>
                  </td>
                  <td>
                    <div className="flex-row">
                      <User size={14} className="text-muted" />
                      {loan.nome_aluno} ({loan.serie_aluno}º {loan.turma_aluno})
                    </div>
                  </td>
                  <td>{new Date(loan.data_inicio_emprestimo).toLocaleDateString()}</td>
                  <td>{new Date(loan.data_fim_emprestimo).toLocaleDateString()}</td>
                  <td>
                    <div className="motivo-cell">
                      <Info size={14} />
                      {loan.motivo_emprestimo}
                    </div>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
};

export default Loans;
