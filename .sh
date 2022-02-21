mkdir -p medical_record_files
mkdir -p medical_record_uploads
pip install -r requirements.txt
cp env_example .env
python manage.py migrate
python manage.py collectstatic

