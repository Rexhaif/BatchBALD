store = {}
store['args']={'dataset': 'DatasetEnum.repeated_mnist_w_noise5', 'num_inference_samples': 10, 'available_sample_k': 10, 'seed': 420620, 'type': 'AcquisitionFunction.bald', 'acquisition_method': 'AcquisitionMethod.multibald', 'experiment_description': 'RMNIST with noise k10 b5 and b10 (and k100 b10), BALD, BatchBALD and heuristic', 'initial_samples': [38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329], 'batch_size': 64, 'scoring_batch_size': 512, 'test_batch_size': 512, 'validation_set_size': 3072, 'early_stopping_patience': 3, 'epochs': 40, 'epoch_samples': 5056, 'target_accuracy': 1.0, 'target_num_acquired_samples': 300, 'initial_percentage': 100, 'reduce_percentage': 0, 'min_remaining_percentage': 100, 'min_candidates_per_acquired_item': 100, 'log_interval': 20, 'experiment_task_id': 'repeated_mnist_w_noise5_multibald_bald_k10_b10_420620', 'experiments_laaos': 'experiment_configs/rmnist_w_noise_2_5/configs.py', 'no_cuda': False, 'quickquick': False, 'initial_samples_per_class': 2, 'balanced_validation_set': False, 'balanced_test_set': False}
store['cmdline']=['./src/ignite_mnist.py', '--experiment_task_id=repeated_mnist_w_noise5_multibald_bald_k10_b10_420620', '--experiments_laaos=experiment_configs/rmnist_w_noise_2_5/configs.py']
store['iterations']=[]
store['initial_samples']=[38043, 40091, 17418, 2094, 39879, 3133, 5011, 40683, 54379, 24287, 9849, 59305, 39508, 39356, 8758, 52579, 13655, 7636, 21562, 41329]
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.6517, 'nll': 1.797270081977691}, 'chosen_targets': [8, 5, 2, 1, 3, 3, 3, 2, 6, 7], 'chosen_samples': [222691, 42379, 289773, 135713, 182740, 258049, 56654, 269050, 71479, 66361], 'chosen_samples_score': [1.4688014119534683, 2.1040209107526295, 2.2599698903515444, 2.2913720504401995, 2.299567847686057, 2.301707890856874, 2.2932039928508123, 2.303356068735046, 2.3070196649043773, 2.3032189965949357], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 9.801589470996987, 'batch_acquisition_elapsed_time': 1264.1942545380007})
store['iterations'].append({'num_epochs': 4, 'test_metrics': {'accuracy': 0.7375, 'nll': 0.8876793619818458}, 'chosen_targets': [9, 2, 4, 8, 0, 2, 4, 7, 4, 8], 'chosen_samples': [70443, 265510, 148253, 141650, 266117, 152949, 59657, 67085, 265234, 201650], 'chosen_samples_score': [1.113940374396949, 1.783709111657918, 2.109203953086447, 2.2286254897532616, 2.2730621370889605, 2.2902216220313414, 2.291643342378777, 2.300375901702405, 2.306448265975235, 2.3051069385345846], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 5.023338480008533, 'batch_acquisition_elapsed_time': 1264.601449445996})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.7943, 'nll': 0.7632089480212098}, 'chosen_targets': [9, 6, 5, 9, 8, 3, 5, 9, 8, 7], 'chosen_samples': [184368, 122044, 117593, 185062, 284638, 241260, 57271, 213358, 130359, 22790], 'chosen_samples_score': [1.512342432398318, 2.061938651393291, 2.241732549128992, 2.287681646749935, 2.298597751018418, 2.3015152269175525, 2.308269426831899, 2.2985961463507993, 2.297879597091731, 2.295451681015465], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 6.974199108008179, 'batch_acquisition_elapsed_time': 1264.7337505659962})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.8365, 'nll': 0.597163161287977}, 'chosen_targets': [5, 2, 8, 7, 4, 3, 5, 8, 2, 6], 'chosen_samples': [42321, 262, 184727, 18810, 5835, 165266, 244723, 169259, 205157, 214284], 'chosen_samples_score': [1.2772105539914422, 2.044295346021105, 2.2249603471762165, 2.282625098945107, 2.2968584023002947, 2.30096294987504, 2.2945163172711167, 2.2906396589562297, 2.310148512899951, 2.3036595154963], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 7.015364163991762, 'batch_acquisition_elapsed_time': 1264.0317115820071})
store['iterations'].append({'num_epochs': 10, 'test_metrics': {'accuracy': 0.8726, 'nll': 0.4813779114353917}, 'chosen_targets': [7, 8, 0, 0, 9, 5, 8, 3, 0, 2], 'chosen_samples': [46874, 119294, 136866, 287156, 239314, 143189, 261395, 20150, 113936, 142852], 'chosen_samples_score': [1.3482575192489505, 2.1116194703805915, 2.2700343541528536, 2.29887789505644, 2.301772785471406, 2.302426555056884, 2.2940007342191824, 2.3003794376878277, 2.3074747516053007, 2.2995416309085503], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 11.078602241002955, 'batch_acquisition_elapsed_time': 1263.9012239550066})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.8694, 'nll': 0.45435132378864457}, 'chosen_targets': [4, 5, 3, 6, 3, 7, 0, 2, 5, 0], 'chosen_samples': [63370, 229348, 180581, 249468, 192117, 89212, 141279, 27598, 231176, 211310], 'chosen_samples_score': [1.400946750408682, 2.116449637210153, 2.276420491603599, 2.2939680180276563, 2.299879480454488, 2.3019677163281886, 2.303475666752475, 2.2968091020624883, 2.2957610338811345, 2.305632476527987], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 9.157910139998421, 'batch_acquisition_elapsed_time': 1264.7853046389937})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.8792, 'nll': 0.41215629489168093}, 'chosen_targets': [7, 4, 0, 2, 0, 7, 4, 2, 4, 7], 'chosen_samples': [182118, 57972, 191133, 155298, 217529, 274677, 199907, 245166, 233546, 27083], 'chosen_samples_score': [1.3458084451107828, 2.08265719911418, 2.257012739403301, 2.290994412819801, 2.2997305037529028, 2.301854596020503, 2.3042885212426913, 2.2985427934739873, 2.3056250494895054, 2.304627990350964], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 9.037092565995408, 'batch_acquisition_elapsed_time': 1263.569205947002})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.8938, 'nll': 0.374715254098625}, 'chosen_targets': [2, 7, 9, 7, 2, 3, 1, 2, 0, 7], 'chosen_samples': [226447, 80226, 31961, 108852, 106447, 47605, 185842, 82083, 235278, 233956], 'chosen_samples_score': [1.430668874025889, 2.0327365902885868, 2.223871097368668, 2.276719607950266, 2.295335158480501, 2.3001985049481606, 2.292376756603471, 2.3002957997410487, 2.304245710546443, 2.3166223779698245], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 8.011354262998793, 'batch_acquisition_elapsed_time': 1265.5865943579993})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.8972, 'nll': 0.3698843337538352}, 'chosen_targets': [9, 9, 9, 9, 2, 6, 6, 2, 0, 5], 'chosen_samples': [165917, 132768, 296753, 62798, 182184, 234994, 111993, 12985, 270439, 91266], 'chosen_samples_score': [1.2115796443602418, 1.923906342631228, 2.194023209874085, 2.265040645304115, 2.2895390731731657, 2.29897429152856, 2.302558474775409, 2.302893166502744, 2.302428125927866, 2.292778692446227], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 9.016649314013193, 'batch_acquisition_elapsed_time': 1265.621546932991})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.9014, 'nll': 0.35779340407589416}, 'chosen_targets': [6, 7, 5, 6, 5, 9, 5, 7, 5, 2], 'chosen_samples': [151954, 237334, 92519, 54196, 267778, 235496, 22272, 289867, 123634, 194901], 'chosen_samples_score': [1.230439261786294, 1.9620169406596273, 2.2380957814510714, 2.285410130393309, 2.29877491128734, 2.3015641190186193, 2.298271061581993, 2.301591966674239, 2.2979790744161868, 2.303124794932669], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 10.088831604996813, 'batch_acquisition_elapsed_time': 1264.6658272890054})
store['iterations'].append({'num_epochs': 11, 'test_metrics': {'accuracy': 0.9218, 'nll': 0.30530448857540704}, 'chosen_targets': [2, 8, 8, 9, 3, 9, 4, 3, 9, 4], 'chosen_samples': [48356, 188031, 229493, 285800, 82542, 194844, 138190, 132377, 196628, 102099], 'chosen_samples_score': [1.3170766745184825, 2.130086770792646, 2.2719992055704807, 2.296754203173349, 2.3015816996163467, 2.302340778966477, 2.2949819466250982, 2.3041794062757512, 2.312471776437123, 2.2982379547480005], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 12.034033160001854, 'batch_acquisition_elapsed_time': 1264.7857472519972})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.9097, 'nll': 0.3447709124839376}, 'chosen_targets': [2, 0, 3, 9, 2, 4, 2, 5, 2, 3], 'chosen_samples': [258084, 162632, 46269, 24860, 211063, 160169, 201023, 229890, 78084, 286269], 'chosen_samples_score': [1.1558508099412417, 1.9190495892043258, 2.1696210913910785, 2.25765664092445, 2.28711273833538, 2.2976115759645324, 2.3156971527747454, 2.309363077461956, 2.287957238463213, 2.3034898594732094], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 7.015762341005029, 'batch_acquisition_elapsed_time': 1264.5371326800087})
store['iterations'].append({'num_epochs': 12, 'test_metrics': {'accuracy': 0.9164, 'nll': 0.30569834921177025}, 'chosen_targets': [8, 8, 5, 5, 6, 4, 5, 4, 7, 9], 'chosen_samples': [142591, 68432, 113529, 47741, 132271, 206546, 24887, 139112, 282415, 39351], 'chosen_samples_score': [1.2337196950782268, 2.008620068052142, 2.219507239051128, 2.282735863779382, 2.298161804968263, 2.3013408219604385, 2.296384911648277, 2.299913088751016, 2.30306621758523, 2.2997288725058036], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.047756225001649, 'batch_acquisition_elapsed_time': 1264.118852455009})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.925, 'nll': 0.2956646977174908}, 'chosen_targets': [5, 2, 2, 9, 4, 5, 3, 8, 5, 7], 'chosen_samples': [199638, 157974, 126944, 227662, 226374, 52686, 230317, 131734, 180278, 39316], 'chosen_samples_score': [1.1605019566239425, 1.8361236039694542, 2.1526949341382573, 2.2483004561412714, 2.282795112925908, 2.2944344225686035, 2.2986684385590648, 2.3027894347216886, 2.2998361715038405, 2.2851117171823017], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 7.078661269988515, 'batch_acquisition_elapsed_time': 1264.3449181680044})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.9287, 'nll': 0.26838543483909016}, 'chosen_targets': [2, 0, 2, 2, 2, 0, 2, 8, 9, 8], 'chosen_samples': [271512, 158744, 232169, 243719, 232548, 100456, 43760, 299101, 208192, 37605], 'chosen_samples_score': [1.2147070191124913, 2.0097117259199795, 2.2056159203552164, 2.2794057591300643, 2.2960353728750142, 2.300445693687667, 2.2948982227815646, 2.303981225417648, 2.307017478934192, 2.3052932426264054], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 10.024778028993751, 'batch_acquisition_elapsed_time': 1264.3101618999935})
store['iterations'].append({'num_epochs': 13, 'test_metrics': {'accuracy': 0.9297, 'nll': 0.26127640288910026}, 'chosen_targets': [2, 7, 7, 7, 7, 8, 1, 5, 3, 2], 'chosen_samples': [206733, 22481, 242381, 10716, 213057, 39355, 284800, 45602, 76678, 193508], 'chosen_samples_score': [1.3530099004245382, 2.057551959129936, 2.2354345131432956, 2.2870737970559807, 2.2987504611142375, 2.3015316336223424, 2.304763218353072, 2.30390150066456, 2.295459257414381, 2.308228886369133], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 14.129880188003881, 'batch_acquisition_elapsed_time': 1264.4304496209952})
store['iterations'].append({'num_epochs': 12, 'test_metrics': {'accuracy': 0.9298, 'nll': 0.2655774573781374}, 'chosen_targets': [8, 6, 3, 8, 1, 2, 8, 8, 8, 4], 'chosen_samples': [124348, 140855, 2803, 210322, 239783, 239913, 270451, 76860, 116001, 281319], 'chosen_samples_score': [1.3204510368186464, 1.9877583209068999, 2.206781472226144, 2.2794145042852505, 2.297608692258566, 2.301215954579543, 2.3034590565715067, 2.304713977287655, 2.308937818600154, 2.3069071434536204], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.142061013000784, 'batch_acquisition_elapsed_time': 1264.6480913080013})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.9376, 'nll': 0.28585814180037494}, 'chosen_targets': [2, 2, 0, 3, 9, 4, 2, 7, 0, 0], 'chosen_samples': [172971, 36704, 15779, 173156, 139824, 34406, 164898, 61127, 136286, 152427], 'chosen_samples_score': [1.0218104669715835, 1.6162480915241697, 1.949809582740313, 2.1282214158260846, 2.216959632060104, 2.2571463576382023, 2.281419191290211, 2.2879288339239645, 2.3057216558980986, 2.2997689376654566], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 7.017075923999073, 'batch_acquisition_elapsed_time': 1264.5598819559964})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9301, 'nll': 0.3078340007221673}, 'chosen_targets': [5, 3, 8, 3, 6, 3, 5, 5, 6, 9], 'chosen_samples': [152344, 234074, 41464, 166923, 10304, 294074, 92344, 35747, 107260, 215421], 'chosen_samples_score': [1.0897991246225986, 1.781977132651834, 2.074963406048709, 2.2040257104970125, 2.269403699643291, 2.2874054896066016, 2.3036269217964502, 2.301575872972752, 2.2922087651274206, 2.304248514839488], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 8.056723821995547, 'batch_acquisition_elapsed_time': 1263.8840401530033})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.9384, 'nll': 0.2814530932926494}, 'chosen_targets': [3, 3, 5, 2, 2, 3, 9, 1, 3, 9], 'chosen_samples': [260869, 74367, 257739, 125129, 185103, 258739, 281295, 72375, 232785, 297728], 'chosen_samples_score': [1.116400842088414, 1.7763728492223714, 2.1067033880078494, 2.22692918207391, 2.2756154675139033, 2.2916301228781455, 2.2974310340381825, 2.2958800194581634, 2.2964519530448406, 2.298997037547509], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 9.090617156005464, 'batch_acquisition_elapsed_time': 1264.590286392995})
store['iterations'].append({'num_epochs': 15, 'test_metrics': {'accuracy': 0.9414, 'nll': 0.2347795649433288}, 'chosen_targets': [5, 4, 0, 1, 0, 2, 9, 1, 5, 6], 'chosen_samples': [49672, 291261, 177659, 60134, 207429, 129396, 92668, 134, 191154, 179369], 'chosen_samples_score': [1.4313030500239259, 2.1244665808354517, 2.2603646537670854, 2.293947029924055, 2.300973889596091, 2.3022663994603323, 2.302920019741826, 2.3114938147752064, 2.3005302906831657, 2.3030302396548024], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 16.119850795992534, 'batch_acquisition_elapsed_time': 1263.1953050259908})
store['iterations'].append({'num_epochs': 12, 'test_metrics': {'accuracy': 0.9435, 'nll': 0.23058830014788437}, 'chosen_targets': [7, 5, 5, 5, 6, 8, 6, 1, 3, 2], 'chosen_samples': [64530, 82193, 231144, 225250, 15870, 46776, 3524, 119297, 149294, 156072], 'chosen_samples_score': [1.2885839190006871, 2.0167638073236387, 2.241618529835012, 2.284375753358012, 2.297638724987446, 2.3012147011811015, 2.3013886554008174, 2.293698471846707, 2.291090099090059, 2.304547895390625], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 13.016909504003706, 'batch_acquisition_elapsed_time': 1263.5860220650065})
store['iterations'].append({'num_epochs': 13, 'test_metrics': {'accuracy': 0.9407, 'nll': 0.22796392621455444}, 'chosen_targets': [4, 5, 2, 4, 5, 7, 3, 3, 6, 5], 'chosen_samples': [282181, 98698, 48912, 220702, 29505, 5821, 104350, 105658, 206940, 169928], 'chosen_samples_score': [1.3033604548059063, 2.0275168453509793, 2.2514774014708934, 2.2878884502030035, 2.2983498957684834, 2.30158865533356, 2.3000418695059355, 2.3060989560056253, 2.3054708495426213, 2.2959175662958735], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 14.168208550996496, 'batch_acquisition_elapsed_time': 1263.5751783130108})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.9341, 'nll': 0.32723257510562803}, 'chosen_targets': [8, 2, 3, 4, 1, 8, 5, 0, 3, 5], 'chosen_samples': [106368, 248978, 168300, 212776, 206444, 49660, 162428, 212880, 137766, 74100], 'chosen_samples_score': [0.9381630627512301, 1.6110810772212858, 1.9766277500571399, 2.1478006435959958, 2.2265810101954293, 2.2602104103923155, 2.2885488748973692, 2.2925473714414455, 2.299260362398634, 2.2954095600995696], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 7.0437097730027745, 'batch_acquisition_elapsed_time': 1265.3380692390056})
store['iterations'].append({'num_epochs': 6, 'test_metrics': {'accuracy': 0.9297, 'nll': 0.3297306346081007}, 'chosen_targets': [8, 6, 3, 8, 8, 6, 2, 9, 8, 6], 'chosen_samples': [103629, 214520, 241611, 101078, 181239, 154520, 184646, 198598, 221078, 94520], 'chosen_samples_score': [1.1369397653554214, 1.7086870295950045, 2.0002149999155936, 2.1737576704367227, 2.241466140106752, 2.2741032843194158, 2.2750443380063774, 2.2932585342979195, 2.3035624406860276, 2.295206025557934], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 7.038299289997667, 'batch_acquisition_elapsed_time': 1265.1329990180093})
store['iterations'].append({'num_epochs': 9, 'test_metrics': {'accuracy': 0.9431, 'nll': 0.24099273238728425}, 'chosen_targets': [2, 3, 5, 4, 0, 9, 7, 8, 9, 3], 'chosen_samples': [172851, 72211, 219482, 102216, 58560, 256981, 257420, 50639, 117683, 130260], 'chosen_samples_score': [1.0351462629044166, 1.752756762254112, 2.0836675818311394, 2.207374978434525, 2.2627224796399483, 2.288645578447272, 2.293646518731167, 2.282752976647847, 2.303510002245165, 2.301836763124972], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 10.247336600004928, 'batch_acquisition_elapsed_time': 1264.101367411})
store['iterations'].append({'num_epochs': 8, 'test_metrics': {'accuracy': 0.95, 'nll': 0.23186508626646177}, 'chosen_targets': [6, 8, 2, 0, 2, 8, 6, 8, 6, 7], 'chosen_samples': [106088, 191146, 49474, 81355, 299757, 274946, 286088, 274758, 183268, 36818], 'chosen_samples_score': [1.105393935317378, 1.8184478975414171, 2.1047283349902233, 2.2228823008811194, 2.2680234125103356, 2.2873504932762785, 2.3017441278773596, 2.293319460364085, 2.3000485716479844, 2.3036817243631926], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 9.048485184001038, 'batch_acquisition_elapsed_time': 1263.0007722660084})
store['iterations'].append({'num_epochs': 10, 'test_metrics': {'accuracy': 0.9423, 'nll': 0.2353690217326177}, 'chosen_targets': [3, 0, 1, 3, 3, 0, 8, 3, 5, 3], 'chosen_samples': [53943, 169889, 182831, 103833, 137010, 72184, 106313, 95447, 57211, 266909], 'chosen_samples_score': [1.0085230090460722, 1.6775830213654581, 2.0106776991418736, 2.171676326788188, 2.2467496926158694, 2.2752722486360444, 2.295795030640268, 2.2939318125485935, 2.3057744742477926, 2.2936598778414927], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 11.07602777799184, 'batch_acquisition_elapsed_time': 1263.6258609740034})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9529, 'nll': 0.25113571032175863}, 'chosen_targets': [5, 7, 3, 8, 9, 2, 9, 3, 4, 7], 'chosen_samples': [156268, 229829, 120207, 242761, 80641, 269017, 180424, 180207, 159123, 60969], 'chosen_samples_score': [1.0507675310728415, 1.6978826954995256, 2.052877437164439, 2.1866005136500366, 2.2447761982893324, 2.2745448929121697, 2.291174227676043, 2.2932504003261593, 2.3014587317485597, 2.297715670033715], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 8.154504186008126, 'batch_acquisition_elapsed_time': 1263.4474079409993})
store['iterations'].append({'num_epochs': 7, 'test_metrics': {'accuracy': 0.9542, 'nll': 0.23994678889674273}, 'chosen_targets': [9, 8, 2, 9, 9, 4, 2, 9, 0, 9], 'chosen_samples': [262597, 65430, 94650, 69428, 82597, 78398, 274650, 80820, 257365, 83463], 'chosen_samples_score': [1.0063275079916405, 1.6288754908551186, 1.9724945248001902, 2.1630799168194534, 2.230316804586682, 2.264941179151272, 2.2700623575847985, 2.279861887418263, 2.306862255991697, 2.3007561842142144], 'chosen_samples_orignal_score': None, 'train_model_elapsed_time': 8.032057350996183, 'batch_acquisition_elapsed_time': 1264.371192096005})
