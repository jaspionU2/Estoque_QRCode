async function pao() {
    try {
        const response = await fetch('http://localhost:8000/equipamento', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer ' + localStorage.getItem('token')
            },
            body: JSON.stringify({
                "nome": "pao",
                "descricao": "pao",
                "numero_serie": "pao",
                "categoria_id": 1,
                "status_id": 1,
                "localizacao": "pao"
            })
        });
        const data = await response.json();
        
        return data;
    } catch (error) {
        console.error(error);
    }
}



pao();