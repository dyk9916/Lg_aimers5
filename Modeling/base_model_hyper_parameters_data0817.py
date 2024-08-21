# model 별 hyper parameter 기록

## ------------ 1. lgbm(lightgbm)

# 1-1. total
# train_model_All = train_and_evaluate_model(
#     'lgbm', train_data
#     , n_estimators=2383
#     , num_leaves=2528
#     , max_depth=343
#     , learning_rate=0.04661896043153508
#     , min_child_samples=209
#     , boosting_type='dart'
#     , random_state=RANDOM_STATE
#     , verbose=-1
# )
# F1 Score: 0.24501424501424504

# 1-2. Dam
# train_model_Dam = train_and_evaluate_model(
#     'lgbm', train_data_dam
#     , n_estimators=1467
#     , num_leaves=2545
#     , max_depth=37
#     , learning_rate=0.04353920224587149 
#     , min_child_samples=83
#     , boosting_type='dart'
#     , random_state=RANDOM_STATE
#     , verbose=-1
# )
# F1 Score: 0.2222222222222222

# 1-3. AutoClave
# train_model_AutoClave = train_and_evaluate_model(
#     'lgbm', train_data_autoclave
#     , n_estimators=1563
#     , num_leaves=1885
#     , max_depth=15
#     , learning_rate=0.07033655355880039 
#     , min_child_samples=158
#     , boosting_type='dart'
#     , random_state=RANDOM_STATE
#     , verbose=-1
# )
# F1 Score: 0.2511078286558346

# 1-4. Fill1
# train_model_Fill1 = train_and_evaluate_model(
#     'lgbm', train_data_Fill1
#     , n_estimators=1452
#     , num_leaves=1581
#     , max_depth=22
#     , learning_rate=0.002000452888170992 
#     , min_child_samples=43
#     , boosting_type='dart'
#     , random_state=RANDOM_STATE
#     , verbose=-1
# )
# F1 Score: 0.2260668973471742

# 1-5. Fill2
# train_model_Fill2 = train_and_evaluate_model(
#     'lgbm', train_data_fill2
#     , n_estimators=1632
#     , num_leaves=1426
#     , max_depth=8
#     , learning_rate=0.07487990991624197 
#     , min_child_samples=90
#     , boosting_type='dart'
#     , random_state=RANDOM_STATE
#     , verbose=-1
# )
# F1 Score: 0.21999999999999997

## ------------ 2. xgb(xgboost)

# 2-1. total
# train_model_All = train_and_evaluate_model(
#     'xgb', train_data
#     , n_estimators = 488
#     , learning_rate = 0.27456156507923796
#     , max_depth = 18
#     , alpha = 0.001345329538356762
#     , gamma = 0.001271261094255318
#     , reg_alpha = 0.8757519133030134
#     , reg_lambda = 0.08373579326505055
#     , colsample_bytree = 0.8186279659279335
#     , subsample = 0.24909941675865316
#     , objective = 'binary:logistic'
#     , tree_method = 'exact'
#     , random_state=RANDOM_STATE
# )
# F1 Score: XX

# 2-2. Dam
# train_model_Dam = train_and_evaluate_model(
#     'xgb', train_data_dam
#     , n_estimators = 488
#     , learning_rate = 0.27456156507923796
#     , max_depth = 18
#     , alpha = 0.001345329538356762
#     , gamma = 0.001271261094255318
#     , reg_alpha = 0.8757519133030134
#     , reg_lambda = 0.08373579326505055
#     , colsample_bytree = 0.8186279659279335
#     , subsample = 0.24909941675865316
#     , objective = 'binary:logistic'
#     , tree_method = 'exact'
#     , random_state=RANDOM_STATE
# )
# F1 Score: XX

# 2-3. AutoClave
# train_model_AutoClave = train_and_evaluate_model(
#     'xgb', train_data_autoclave
#     , n_estimators = 488
#     , learning_rate = 0.27456156507923796
#     , max_depth = 18
#     , alpha = 0.001345329538356762
#     , gamma = 0.001271261094255318
#     , reg_alpha = 0.8757519133030134
#     , reg_lambda = 0.08373579326505055
#     , colsample_bytree = 0.8186279659279335
#     , subsample = 0.24909941675865316
#     , objective = 'binary:logistic'
#     , tree_method = 'exact'
#     , random_state=RANDOM_STATE
# )
# F1 Score: XX

# 2-4. Fill1
# train_model_Fill1 = train_and_evaluate_model(
#     'xgb', train_data_fill1
#     , n_estimators = 488
#     , learning_rate = 0.27456156507923796
#     , max_depth = 18
#     , alpha = 0.001345329538356762
#     , gamma = 0.001271261094255318
#     , reg_alpha = 0.8757519133030134
#     , reg_lambda = 0.08373579326505055
#     , colsample_bytree = 0.8186279659279335
#     , subsample = 0.24909941675865316
#     , objective = 'binary:logistic'
#     , tree_method = 'exact'
#     , random_state=RANDOM_STATE
# )
# F1 Score: XX

# 2-5. Fill2
# train_model_Fill2 = train_and_evaluate_model(
#     'xgb', train_data_fill2
#     , n_estimators = 488
#     , learning_rate = 0.27456156507923796
#     , max_depth = 18
#     , alpha = 0.001345329538356762
#     , gamma = 0.001271261094255318
#     , reg_alpha = 0.8757519133030134
#     , reg_lambda = 0.08373579326505055
#     , colsample_bytree = 0.8186279659279335
#     , subsample = 0.24909941675865316
#     , objective = 'binary:logistic'
#     , tree_method = 'exact'
#     , random_state=RANDOM_STATE
# )
# F1 Score: XX

## ------------ 3. cat(catboost)

# 3-1. total
# train_model_All = train_and_evaluate_model(
#     'cat', train_data
#     , iterations=1080
#     , learning_rate=0.27700365060588783
#     , depth=5
#     , l2_leaf_reg=1.253973786965849
#     , random_strength=9.22514112631014
#     , bagging_temperature=8.810531538725536
#     , border_count=205
#     , scale_pos_weight=1.1080635788286048
#     , random_seed = RANDOM_STATE
#     , eval_metric = 'F1'
#     , logging_level = 'Silent'
#     , boosting_type = 'Plain'
# )
# F1 Score: xx

# 3-2. Dam
# train_model_Dam = train_and_evaluate_model(
#     'cat', train_data_dam
#     , iterations=1415
#     , learning_rate=0.07701213944704571
#     , depth=12
#     , l2_leaf_reg=2.6328100798019762 
#     , random_strength=9.510403770860803
#     , bagging_temperature=5.8234148306877715
#     , border_count=258
#     , scale_pos_weight=0.8513945387463904
#     , random_seed = RANDOM_STATE
#     , eval_metric = 'F1'
#     , logging_level = 'Silent'
#     , boosting_type = 'Plain'
# )
# F1 Score: xx

# 3-3. AutoClave
# train_model_AutoClave = train_and_evaluate_model(
#     'cat', train_data_autoclave
#     , iterations=672
#     , learning_rate=0.32067318144871304
#     , depth=4
#     , l2_leaf_reg=4.200323262290698 
#     , random_strength=2.1487257714690915
#     , bagging_temperature=6.901535824166224
#     , border_count=81
#     , scale_pos_weight=1.0091261797689637
#     , random_seed = RANDOM_STATE
#     , eval_metric = 'F1'
#     , logging_level = 'Silent'
#     , boosting_type = 'Plain'
# )
# F1 Score: xx

# 3-4. Fill1
# train_model_Fill1 = train_and_evaluate_model(
#     'cat', train_data_fill1
#     , iterations=1080
#     , learning_rate=0.27700365060588783
#     , depth=5
#     , l2_leaf_reg=1.253973786965849
#     , random_strength=9.22514112631014
#     , bagging_temperature=8.810531538725536
#     , border_count=205
#     , scale_pos_weight=1.1080635788286048
#     , random_seed = RANDOM_STATE
#     , eval_metric = 'F1'
#     , logging_level = 'Silent'
#     , boosting_type = 'Plain'
# )
# F1 Score: xx

# 3-5. Fill2
# train_model_Fill2 = train_and_evaluate_model(
#     'cat', train_data_fill2
#     , iterations=942
#     , learning_rate=0.0663329773137215
#     , depth=9
#     , l2_leaf_reg=2.8579737675612154
#     , random_strength=7.119939923407122
#     , bagging_temperature=7.446487630118915
#     , border_count=73
#     , scale_pos_weight=1.1824356154616613
#     , random_seed = RANDOM_STATE
#     , eval_metric = 'F1'
#     , logging_level = 'Silent'
#     , boosting_type = 'Plain'
# )
# F1 Score: xx

## ------------ 4. rf(randomforest)

# 4-1. total
# train_model_All = train_and_evaluate_model(
#     'rf', train_data
#     , n_estimators = 1083
#     , max_depth = 43
#     , min_samples_split = 6
#     , min_samples_leaf = 1
#     , criterion = 'entropy'
#     , class_weight = balanced
#     , random_state=RANDOM_STATE
# )
# F1 Score: 0.2408026755852843

# 4-2. Dam
# train_model_Dam = train_and_evaluate_model(
#     'rf', train_data_dam
#     , n_estimators = 1330
#     , max_depth = 36
#     , min_samples_split = 6
#     , min_samples_leaf = 1
#     , criterion = 'entropy'
#     , bootstrap = False
#     , random_state=RANDOM_STATE
# )
# F1 Score: 0.20075757575757575

# 4-3. AutoClave
# train_model_AutoClave = train_and_evaluate_model(
#     'rf', train_data_autoclave
#     , n_estimators = 1103
#     , max_depth = 36
#     , min_samples_split = 8
#     , min_samples_leaf = 1
#     , criterion = 'entropy'
#     , bootstrap = False
#     , random_state=RANDOM_STATE
# )
# F1 Score: 0.2214765100671141

# 4-4. Fill1
# train_model_Fill1 = train_and_evaluate_model(
#     'rf', train_data_fill1
#     , n_estimators = 1298
#     , max_depth = 20
#     , min_samples_split = 6
#     , min_samples_leaf = 1
#     , criterion = 'entropy'
#     , bootstrap = False
#     , random_state=RANDOM_STATE
# )
# F1 Score: 0.1932938856015779

# 4-5. Fill2
# train_model_Fill2 = train_and_evaluate_model(
#     'rf', train_data_fill2
#     , n_estimators = 2879
#     , max_depth = 27
#     , min_samples_split = 4
#     , min_samples_leaf = 1
#     , criterion = 'entropy'
#     , bootstrap = False
#     , random_state=RANDOM_STATE
# )
# F1 Score: 0.18563922942206654

## ------------ 5. et(extratree)

# 5-1. total
# train_model_All = train_and_evaluate_model(
#     'et', train_data
#     , n_estimators = 1959
#     , max_depth = 48
#     , min_samples_split = 5
#     , min_samples_leaf = 1
#     , criterion = 'entropy'
#     , bootstrap = False
#     , random_state=RANDOM_STATE
# )
# F1 Score: xx

# 5-2. Dam
# train_model_Dam = train_and_evaluate_model(
#     'et', train_data_dam
#     , n_estimators = 1959
#     , max_depth = 48
#     , min_samples_split = 5
#     , min_samples_leaf = 1
#     , criterion = 'entropy'
#     , bootstrap = False
#     , random_state=RANDOM_STATE
# )
# F1 Score: xx

# 5-3. AutoClave
# train_model_AutoClave = train_and_evaluate_model(
#     'et', train_data_autoclave
#     , n_estimators = 1959
#     , max_depth = 48
#     , min_samples_split = 5
#     , min_samples_leaf = 1
#     , criterion = 'entropy'
#     , bootstrap = False
#     , random_state=RANDOM_STATE
# )
# F1 Score: xx

# 5-4. Fill1
# train_model_Fill1 = train_and_evaluate_model(
#     'et', train_data_fill1
#     , n_estimators = 1959
#     , max_depth = 48
#     , min_samples_split = 5
#     , min_samples_leaf = 1
#     , criterion = 'entropy'
#     , bootstrap = False
#     , random_state=RANDOM_STATE
# )
# F1 Score: xx

# 5-5. Fill2
# train_model_Fill2 = train_and_evaluate_model(
#     'et', train_data_fill2
#     , n_estimators = 1959
#     , max_depth = 48
#     , min_samples_split = 5
#     , min_samples_leaf = 1
#     , criterion = 'entropy'
#     , bootstrap = False
#     , random_state=RANDOM_STATE
# )
# F1 Score: xx

## ------------ 6. ada(adaboost)

# 6-1. total
# base_estimator = DecisionTreeClassifier(
#     max_depth=8,
#     min_samples_split=12,
#     min_samples_leaf=8,
#     max_features=0.6796666797648274,
#     random_state=RANDOM_STATE
# )
# train_model_All = train_and_evaluate_model(
#     'ada', train_data
#     , base_estimator=base_estimator
#     , n_estimators=127
#     , learning_rate=0.7120937821282903
#     , random_state=RANDOM_STATE
# )
# F1 Score: xx

# 6-2. Dam
# base_estimator = DecisionTreeClassifier(
#     max_depth=8,
#     min_samples_split=12,
#     min_samples_leaf=8,
#     max_features=0.6796666797648274,
#     random_state=RANDOM_STATE
# )
# train_model_Dam = train_and_evaluate_model(
#     'ada', train_data_dam
#     , base_estimator=base_estimator
#     , n_estimators=127
#     , learning_rate=0.7120937821282903
#     , random_state=RANDOM_STATE
# )
# F1 Score: xx

# 6-3. AutoClave
# base_estimator = DecisionTreeClassifier(
#     max_depth=4,
#     min_samples_split=12,
#     min_samples_leaf=3,
#     max_features=0.8791373212174012,
#     random_state=RANDOM_STATE
# )
# train_model_AutoClave = train_and_evaluate_model(
#     'ada', train_data_autoclave
#     , base_estimator=base_estimator
#     , n_estimators=219
#     , learning_rate=0.9780046775396287
#     , random_state=RANDOM_STATE
# )
# F1 Score: xx

# 6-4. Fill1
# base_estimator = DecisionTreeClassifier(
#     max_depth=13,
#     min_samples_split=37,
#     min_samples_leaf=8,
#     max_features=0.903347592245114,
#     random_state=RANDOM_STATE
# )
# train_model_Fill1 = train_and_evaluate_model(
#     'ada', train_data_fill1
#     , base_estimator=base_estimator
#     , n_estimators=872
#     , learning_rate=0.9180520600986571
#     , random_state=RANDOM_STATE
# )
# F1 Score: xx

# 6-5. Fill2
# base_estimator = DecisionTreeClassifier(
#     max_depth=10,
#     min_samples_split=8,
#     min_samples_leaf=10,
#     max_features=0.9218116956137874,
#     random_state=RANDOM_STATE
# )

# train_model_Fill2 = train_and_evaluate_model(
#     'ada', train_data_fill2
#     , base_estimator=base_estimator
#     , n_estimators=546
#     , learning_rate=0.04158318798724073
#     , random_state=RANDOM_STATE
# )
# F1 Score: xx

# ...