### General 
main : main.py
nettoyer : data_processor.py
model : train_model.py 
function utile : utils.py


Logistic Regression = Ce modèle suppose une relation linéaire entre les variables explicatives et la variable cible "status". 
                    Variable par varaible avec la cible.

Arbres de décision  = Ce modèle est capable de capturer des relations non-linéaires complexes. Il le fait a chaque noeud.

Forêts aléatoires = Ces modèles sont capables de capturer des relations non-linéaires complexes. Il le fait sur tout l'arbre, il fait une moyenne des  importances.


Différents algorithmes pour etre surs des resultats, voir toutes les variables explicatives potentielles, reduire le risque de surapprentissage ou de sous-apprentissage, voir les variables explicatives recurrentes ( potentiellement celles qui sont vraiment les plus importantes)

Pour chaque modele entrainé, j'affiche l'accurancy et le f1-score : check si le modele à bien appris.

### Usage 
``
python main.py
``

### Result 

| Valeurs explicatif               | Logistic Regression  | Decision Tree         | Random Forest         |
|----------------------------------|----------------------|-----------------------|-----------------------|
| Accuracy                         | 0.9973 (élevée)      | 0.9956 (élevée)       | 0.9981 (élevée)       |
| F1-score                         | 0.9962 (élevée)      | 0.9957 (élevée)       | 0.9977 (élevée)       |
| reimbursement_date               | 1.4351               | 0.0016                | 0.0067                |
| reco_last_update                 | 0.6453               | 0.0141                | 0.0222                |
| reco_creation                    | 0.6210               | 0.0002                | 0.0219                |
| recovery_status                  | 0.5721               | 0.0433                | 0.0416                |
| allowed_amount                   | 0.5229               | 0.0012                | 0.0008                |
| deleted_account_id               | 0.4778               | 0.0013                | 0.0051                |
| transfer_type                    | 0.4361               | 0.0000                | 0.0004                |
| cash_request_received_date       | 0.4173               | 0.8454                | 0.3287                |
| money_back_date                  | 0.4046               | 0.0663                | 0.3604                |
| id                               | 0.3698               | 0.0144                | 0.0066                |
| user_id                          | 0.2591               | 0.0004                | 0.0037                |
| name_bank                        | 0.2152               | 0.0010                | 0.0016                |
| created_at                       | 0.1841               | 0.0015                | 0.0066                |
| cash_request_debited_date        | 0.1597               | 0.0000                | 0.0038                |
| card_description                 | 0.0860               | 0.0012                | 0.0008                |
| updated_at                       | 0.0681               | 0.0079                | 0.1880                |
| amount                           | 0.0392               | 0.0002                | 0.0011                |

## Result explication 

1. reco_last_update : Horaire. Peut être utilisé pour déterminer la date de clôture de l’incident.
2. reco_creation : Horaire de la création de la récupération.
3. cash_request_received_date : Date of the receipt of the CR. Based on user's bank history.
4. updated_at


### result transaction 

| Valeurs explicatif               | Logistic Regression          | Decision Tree                | Random Forest                |
|----------------------------------|------------------------------|------------------------------|------------------------------|
| Accuracy                         | 0.6011                       | 0.7099                       | 0.6887                       |
| F1-score                         | 0.5145                       | 0.7065                       | 0.6788                       |
| recurrent_group_id               | 0.9463                       | 0.0353                       | 0.0263                       |
| account_id                       | 0.8443                       | 0.3717                       | 0.1795                       |
| recurrent                        | 0.7973                       | 0.0004                       | 0.0039                       |
| date                             | 0.6262                       | 0.0751                       | 0.0959                       |
| created_at                       | 0.5779                       | 0.0514                       | 0.1241                       |
| id                               | 0.4381                       | 0.0697                       | 0.1381                       |
| user_id                          | 0.3582                       | 0.2683                       | 0.1618                       |
| is_bling                         | 0.2971                       | 0.0013                       | 0.0018                       |
| balance                          | 0.1267                       | 0.0619                       | 0.1037                       |
| is_debt                          | 0.1003                       | 0.0008                       | 0.0015                       |
| is_debit_reject                  | 0.0814                       | 0.0007                       | 0.0013                       |
| is_n26_rejected_debit           | 0.0607                       | 0.0001                       | 0.0002                       |
| is_gambling                      | 0.0530                       | 0.0016                       | 0.0023                       |
| category                         | 0.0515                       | 0.0118                       | 0.0377                       |
| is_debit_refund                 | 0.0454                       | 0.0001                       | 0.0005                       |
| is_unemployment                  | 0.0327                       | 0.0002                       | 0.0002                       |
| amount                           | 0.0292                       | 0.0339                       | 0.0774                       |
| is_interim                       | 0.0281                       | 0.0002                       | 0.0003                       |
| is_check                         | 0.0233                       | 0.0001                       | 0.0003                       |
| is_deleted                       | 0.0218                       | 0.0031                       | 0.0043                       |
| is_loan                          | 0.0194                       | 0.0002                       | 0.0004                       |
| bridge_category                  | 0.0184                       | 0.0120                       | 0.0376                       |
| is_uber                          | 0.0102                       | 0.0000                       | 0.0001                       |
| is_caf                           | 0.0078                       | 0.0002                       | 0.0005                       |
| is_debt_collection               | 0.0065                       | 0.0000                       | 0.0001                       |
| is_btc                           | 0.0011                       | 0.0000                       | 0.0002                       |
| is_principal_account             | 0.0000                       | 0.0000                       | 0.0000                       |


