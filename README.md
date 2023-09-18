1) Python 3.8.10
2) pip install -r req.txt
3) восстановить бд backup_db

4) http://127.0.0.1:8011/


admin/
[name='login']
home/ [name='home']
graph/ [name='graph']
details/<int:pk> [name='details']
table/ [name='table']
api/

// python -m pip install -U channels["daphne"]
// pip install -U asgi_redis


# Удалить всё 
- docker system prune
    volumes:
      - .:/app
