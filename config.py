import os


class Config:
    DB_USERNAME = os.environ.get('DB_USERNAME')
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    DB_NAME = 'database'
    MONGODB_HOST = f"mongodb+srv://{DB_USERNAME}:{DB_PASSWORD}@flaskcluster.tscjm.mongodb.net/{DB_NAME}?retryWrites" \
                   f"=true"
