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

| Valeurs explicatif               | Logistic Regression  | Decision Tree         | Random Forest         |   |
|----------------------------------|----------------------|-----------------------|-----------------------|---|
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

Logistic Regression - Accuracy: 0.6011493779917432, F1-score: 0.5145404263765965 => pas super bien : normal car pas que les transactions.
Logistic Regression - Feature Importance:
recurrent_group_id       0.946329
account_id               0.844271
recurrent                0.797317
date                     0.626211
created_at               0.577907
id                       0.438061
user_id                  0.358175
is_bling                 0.297061
balance                  0.126662
is_debt                  0.100294
is_debit_reject          0.081438
is_n26_rejected_debit    0.060717
is_gambling              0.053043
category                 0.051548
is_debit_refund          0.045429
is_unemployment          0.032650
amount                   0.029185
is_interim               0.028146
is_check                 0.023328
is_deleted               0.021819
is_loan                  0.019411
bridge_category          0.018392
is_uber                  0.010231
is_caf                   0.007763
is_debt_collection       0.006454
is_btc                   0.001075
is_principal_account     0.000000
dtype: float64


Decision Tree - Accuracy: 0.7099164712175452, F1-score: 0.7065020830229256
Decision Tree - Feature Importance:
account_id               0.371096 
user_id                  0.268631
date                     0.075224
id                       0.063817
balance                  0.061810
created_at               0.057464
recurrent_group_id       0.035374
amount                   0.033910
bridge_category          0.011964
category                 0.011725

Decision Tree - Accuracy: 0.6886296616329945, F1-score: 0.6787796711191676
Random Forest - Feature Importance:
account_id               0.177984
user_id                  0.164033
id                       0.137543
created_at               0.124357
balance                  0.103509
date                     0.096161
amount                   0.077244
category                 0.037612
bridge_category          0.037494
recurrent_group_id       0.025809


## Result 

1. 
<tb><td> hfgvjedv </td></tb>

3. 
