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

Logistic Regression - Accuracy: 0.9973302822273074, F1-score: 0.9962243072305119 => elevée 

Logistic Regression - Feature Importance:
reimbursement_date            1.435125 # evident car si remboursement alors pas d'incident.
reco_last_update              0.645303
reco_creation                 0.621037
recovery_status               0.572138
allowed_amount                0.522940 
deleted_account_id            0.477822 # pourquoi ?
transfer_type                 0.436112 
cash_request_received_date    0.417309 
money_back_date               0.404578 # evident 
id                            0.369839 # pourquoi ? 
user_id                       0.259122 # certain profil type ? 
name_bank                     0.215212 # banque type 
created_at                    0.184088
cash_request_debited_date     0.159690
card_description              0.086038
updated_at                    0.068112
amount                        0.039190 # remboursement ne depent pas du montant
dtype: float64

Decision Tree - Accuracy: 0.9956140350877193, F1-score: 0.9956905224058519 => elevée

Decision Tree - Feature Importance:
cash_request_received_date    0.845411
money_back_date               0.066294 # evident 
recovery_status               0.043318 # evident 
id                            0.014408 # pourquoi ? 
reco_last_update              0.014135
updated_at                    0.007865
reimbursement_date            0.001605 # evident ?
created_at                    0.001485
deleted_account_id            0.001294
allowed_amount                0.001241
card_description              0.001206
name_bank                     0.000981
user_id                       0.000431
amount                        0.000168
reco_creation                 0.000157
cash_request_debited_date     0.000000
transfer_type                 0.000000
dtype: float64

Decision Tree - Accuracy: 0.998093058733791, F1-score: 0.9977036605427676 => elevée 

Random Forest - Feature Importance:
money_back_date               0.360369 # evident 
cash_request_received_date    0.328690
updated_at                    0.188017
recovery_status               0.041619 # evident 
reco_last_update              0.022176
reco_creation                 0.021944
reimbursement_date            0.006723 # evident 
id                            0.006630 # pourquoi ?
created_at                    0.006613 
deleted_account_id            0.005131
cash_request_debited_date     0.003788
user_id                       0.003731 # certain profil ? 
name_bank                     0.001564
amount                        0.001050
card_description              0.000823
allowed_amount                0.000769
transfer_type                 0.000364
dtype: float64

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
2. 