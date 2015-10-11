## AS-Ext-Apis

A dedicated worker for determining trending NFL players. 

## Uses

Sub.py watches a redis queue for tasks. Default listening is blocking. All data is stored in a PostgreSQL database.

## Tasks

```python
'GET TRENDING PLAYERS'
```  
- Checks frequency of player name mentions on reddit/r/nfl and reddit/r/fantasyfootball.
