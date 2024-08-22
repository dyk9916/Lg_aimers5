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
#     'lgbm', train_data_fill1
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
#     n_estimators = 2287, 
    # learning_rate = 0.046904208411195795, 
    # max_depth = 8, 
    # alpha = 1.9343531171735368e-05, 
    # gamma = 0.002118564280859176, 
    # reg_alpha = 0.6827713868263061, 
    # reg_lambda = 0.05035980721174918, 
    # colsample_bytree = 0.8959193125044248, 
    # subsample = 0.43471952905681815,
    # objective = 'binary:logistic',  # 이진 분류
    # tree_method = "exact", 
    # random_state=RANDOM_STATE
# )
# F1 Score: 0.26099290780141843

# 2-2. Dam
# train_model_Dam = train_and_evaluate_model(
#     'xgb', train_data_dam
#     , n_estimators = 1509
#     , learning_rate = 0.06418917852996714
#     , max_depth = 6
#     , alpha = 0.00017309557032608048
#     , gamma = 0.00398067155434722
#     , reg_alpha = 0.756006595834120
#     , reg_lambda = 0.3962538649486449
#     , colsample_bytree =0.8752205595930229
#     , subsample = 0.224637741333797
#     , objective = 'binary:logistic'
#     , tree_method = 'exact'
#     , random_state=RANDOM_STATE
# )
# F1 Score: 0.2385321100917431

# 2-3. AutoClave
# train_model_AutoClave = train_and_evaluate_model(
#     'xgb', train_data_autoclave
#     n_estimators = 1539, 
    # learning_rate = 0.026860419341696404, 
    # max_depth = 14, 
    # alpha = 1.9237525550524492e-05, 
    # gamma = 2.2016346534611754e-05, 
    # reg_alpha = 0.9148863773292526, 
    # reg_lambda = 0.6194458787523232, 
    # colsample_bytree = 0.902872150299903, 
    # subsample = 0.10750014546599479,
    # objective = 'binary:logistic',  # 이진 분류
    # tree_method = "exact", 
    # random_state=RANDOM_STATE
# )
# F1 Score: 0.2530487804878049

# 2-4. Fill1
# train_model_Fill1 = train_and_evaluate_model(
#     'xgb', train_data_fill1,
#     n_estimators = 1707, 
#     learning_rate = 0.0321470219836192, 
#     max_depth = 7, 
#     alpha = 7.368872823521818e-05, 
#     gamma = 0.0007930035188326916, 
#     reg_alpha = 0.644199314174124, 
#     reg_lambda = 0.588270569327407, 
#     colsample_bytree = 0.883929103208459, 
#     subsample = 0.2534703342501092,
#     objective = 'binary:logistic',
#     tree_method = 'exact',
#     random_state=RANDOM_STATE
# )
# F1 Score: 0.2297734627831715

# 2-5. Fill2
# train_model_Fill2 = train_and_evaluate_model(
#     'xgb', train_data_fill2
#     n_estimators = 1998, 
    # learning_rate = 0.030898693059763598, 
    # max_depth = 8, 
    # alpha = 0.0017554538174868774, 
    # gamma = 0.0007257577447593802, 
    # reg_alpha = 0.7581280398368035, 
    # reg_lambda = 0.5872331353519633, 
    # colsample_bytree = 0.56275606593282, 
    # subsample = 0.8342870707789082,
    # objective = 'binary:logistic',
    # tree_method = 'exact',
    # random_state=RANDOM_STATE
# )
# F1 Score: 0.24233983286908078

## ------------ 3. cat(catboost)

# 3-1. total
# train_model_All = train_and_evaluate_model(
#     'cat', train_data
#     , iterations=1852
#     , learning_rate=0.19270140909662298
#     , depth=11
#     , l2_leaf_reg=1.3258713856672897
#     , random_strength=9.206702306227765
#     , bagging_temperature=10.55412053150983
#     , border_count=255
#     , scale_pos_weight=1.5636124382284884
#     , 'grow_policy' = 'Lossguide'
#     , random_seed = RANDOM_STATE
#     , eval_metric = 'F1'
#     , logging_level = 'Silent'
#     , boosting_type = 'Plain'
# )
# F1 Score: 0.2518301610541727

# 3-2. Dam
# train_model_Dam = train_and_evaluate_model(
#     'cat', train_data_dam
#     , iterations=2083
#     , learning_rate=0.023925705983940986
#     , depth=11
#     , l2_leaf_reg=0.05919257514332274
#     , random_strength=7.259397831551647
#     , bagging_temperature=5.39094676652102
#     , border_count=234
#     , scale_pos_weight=1.776413991309166
#     , grow_policy = 'Lossguide'
#     , random_seed = RANDOM_STATE
#     , eval_metric = 'F1'
#     , logging_level = 'Silent'
#     , boosting_type = 'Plain'
# )
# F1 Score: 0.2450704225352113

# 3-3. AutoClave
# train_model_AutoClave = train_and_evaluate_model(
#     'cat', train_data_autoclave
#     , iterations=2786
#     , learning_rate=0.016342560305036093
#     , depth=8
#     , l2_leaf_reg=3.7187150890684246 
#     , random_strength=0.13164684607188099
#     , bagging_temperature=9.823498597792092
#     , border_count=158
#     , scale_pos_weight=1.8735070170496537
#     , grow_policy = 'SymmetricTree'
#     , random_seed = RANDOM_STATE
#     , eval_metric = 'F1'
#     , logging_level = 'Silent'
#     , boosting_type = 'Plain'
# )
# F1 Score: 0.24691358024691357

# 3-4. Fill1
# train_model_Fill1 = train_and_evaluate_model(
#     'cat', train_data_fill1
#     , iterations=1489
#     , learning_rate=0.011481405951174946
#     , depth=6
#     , l2_leaf_reg=0.12082259365361882
#     , random_strength=2.5111358694495056
#     , bagging_temperature=2.06264856742851
#     , border_count=331
#     , scale_pos_weight=2.3505422278535173
#     , grow_policy = 'Lossguide'
#     , random_seed = RANDOM_STATE
#     , eval_metric = 'F1'
#     , logging_level = 'Silent'
#     , boosting_type = 'Plain'
# )
# F1 Score: 0.2425742574257426

# 3-5. Fill2
# train_model_Fill2 = train_and_evaluate_model(
#     'cat', train_data_fill2
#     , iterations=481
#     , learning_rate=0.018742270357007457
#     , depth=5
#     , l2_leaf_reg=1.0871571324663387
#     , random_strength=3.49632241801363
#     , bagging_temperature=5.717049796462913
#     , border_count=183
#     , scale_pos_weight=3.4406776189795383
#     , grow_policy = 'SymmetricTree'
#     , random_seed = RANDOM_STATE
#     , eval_metric = 'F1'
#     , logging_level = 'Silent'
#     , boosting_type = 'Plain'
# )
# F1 Score: 0.24322446143154972

## ------------ 4. rf(randomforest)

# 4-1. total
# train_model_All = train_and_evaluate_model(
#     'rf', train_data
#     , n_estimators = 1082
#     , max_depth = 54
#     , min_samples_split = 6
#     , min_samples_leaf = 1
#     , criterion = 'entropy'
#     , class_weight = balanced
#     , random_state=RANDOM_STATE
# )
# F1 Score: 0.24115044247787612

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
# F1 Score: 0.2136422136422136

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
# F1 Score: 0.21639344262295085

# 4-4. Fill1
# train_model_Fill1 = train_and_evaluate_model(
#     'rf', train_data_fill1
#     , n_estimators = 1861
#     , max_depth = 91
#     , min_samples_split = 7
#     , min_samples_leaf = 5
#    , criterion = 'entropy'
#    , class_weight = 'balanced'
#    , random_state=RANDOM_STATE
# )
# F1 Score: 0.2207670720299345

# 4-5. Fill2
# train_model_Fill2 = train_and_evaluate_model(
#     'rf', train_data_fill2
#     , n_estimators = 2663
#     , max_depth = 100
#    , min_samples_split = 6
#    , min_samples_leaf = 1
#    , criterion = 'entropy'
#    , class_weight = 'balanced'
#    , random_state=RANDOM_STATE
# )
# F1 Score: 0.1924342105263158

## ------------ 5. et(extratree)

# 5-1. total
# train_model_All = train_and_evaluate_model(
#     'et', train_data
#     , n_estimators = 2884
#     , max_depth = 56
#     , min_samples_split = 3
#     , min_samples_leaf = 1
#     , criterion = 'entropy'
#     , bootstrap = False
#     , random_state=RANDOM_STATE
# )
# F1 Score: 0.2034548944337812

# 5-2. Dam
# train_model_Dam = train_and_evaluate_model(
#     'et', train_data_dam
#     , n_estimators = 2242
#     , max_depth = 32
#     , min_samples_split = 2
#     , min_samples_leaf = 1
#     , criterion = 'entropy'
#     , bootstrap = False
#     , random_state=RANDOM_STATE
# )
# F1 Score: 0.20063694267515925

# 5-3. AutoClave
# train_model_AutoClave = train_and_evaluate_model(
#     'et', train_data_autoclave,
#     n_estimators = 2708,
#     max_depth = 41,
#     min_samples_split = 8,
#     min_samples_leaf = 1,
#     criterion = 'entropy',
#     bootstrap = False,
#     random_state=RANDOM_STATE
# )
# F1 Score: 0.2409937888198758

# 5-4. Fill1
# train_model_Fill1 = train_and_evaluate_model(
    # 'et', train_data_fill1,
    # n_estimators = 1520,
    # max_depth = 30,
    # min_samples_split = 2,
    # min_samples_leaf = 1,
    # criterion = 'entropy',
    # bootstrap = False,
    # random_state=RANDOM_STATE
# )
# F1 Score: 0.19471153846153846

# 5-5. Fill2
# train_model_Fill2 = train_and_evaluate_model(
    # 'et', train_data_fill2
    # , n_estimators = 1001
    # , max_depth = 45
    # , min_samples_split = 3
    # , min_samples_leaf = 1
    # , criterion = 'entropy'
    # , bootstrap = False
    # , random_state=RANDOM_STATE
# )
# F1 Score: 0.17269544924154023

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

# ... Adaboost

# RANDOM_STATE = 42

# base_estimator = DecisionTreeClassifier(
#     max_depth=22,
#     min_samples_split=5,
#     min_samples_leaf=2,
#     max_features=0.9449544624225188,
#     # n_estimators=517,
#     random_state=RANDOM_STATE
# )

# model_Dam = fit_all_train_data_function(
#     'ada', train_data_dam
#     , estimator=base_estimator
#     , n_estimators=439
#     , learning_rate=0.30985993372769294
#     , random_state=RANDOM_STATE
# )

# base_estimator = DecisionTreeClassifier(
#     max_depth=13,
#     min_samples_split=34,
#     min_samples_leaf=5,
#     max_features=0.7473309094470472,
#     # n_estimators=517,
#     random_state=RANDOM_STATE
# )

# model_AutoClave = fit_all_train_data_function(
#     'ada', train_data_autoclave
#     , estimator=base_estimator
#     , n_estimators=570
#     , learning_rate=0.2040105705276999
#     , random_state=RANDOM_STATE
# )

# base_estimator = DecisionTreeClassifier(
#     max_depth=14,
#     min_samples_split=33,
#     min_samples_leaf=8,
#     max_features=0.7113128413756866,
#     # n_estimators=517,
#     random_state=RANDOM_STATE
# )

# model_Fill1 = fit_all_train_data_function(
#     'ada', train_data_fill1
#     , estimator=base_estimator
#     , n_estimators=913
#     , learning_rate=0.055237331816147595
#     , random_state=RANDOM_STATE
# )

# base_estimator = DecisionTreeClassifier(
#     max_depth=7,
#     min_samples_split=13,
#     min_samples_leaf=8,
#     max_features=0.6266118401157937,
#     # n_estimators=517,
#     random_state=RANDOM_STATE
# )

# model_Fill2 = fit_all_train_data_function(
#     'ada', train_data_fill2
#     , estimator=base_estimator
#     , n_estimators=293
#     , learning_rate=0.620377973483163
#     , random_state=RANDOM_STATE
# )

# base_estimator = DecisionTreeClassifier(
#     max_depth=6,
#     min_samples_split=28,
#     min_samples_leaf=7,
#     max_features=0.7331591188366589,
#     # n_estimators=517,
#     random_state=RANDOM_STATE
# )

# model_All = fit_all_train_data_function(
#     'ada', train_data
#     , estimator=base_estimator
#     , n_estimators=677
#     , learning_rate=0.6713565955468803
#     , random_state=RANDOM_STATE
# )
