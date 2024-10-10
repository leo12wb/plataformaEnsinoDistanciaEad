
# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente
# No Windows
venv\Scripts\activate
# No Linux/Mac
source venv/bin/activate

# Importar
pip install -r requirements.txt

# Instale as dependências novamente
pip install sqlalchemy mysql-connector-python fastapi uvicorn

# exec

python -m uvicorn main:app --reload
