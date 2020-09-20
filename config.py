import argparse

parser = argparse.ArgumentParser()



parser.add_argument('--name', type=str, 
                    default='FLICKR',
                    choices=['FLICKR'],
                    help=""" crawler name """)     

parser.add_argument('--max_num', type=int, 
                    default='100',
                    help=""" # of images """)    

parser.add_argument('--tags', type=list, 
                    default=['apple', 'cup', 'surfboard'],
                    help=""" # of images """)    


parser.add_argument('--num_core', type=int, 
                    default='30',
                    help=""" # of cores """)    

# parser.add_argument('--gpus', type=int, nargs='*', default=[0])     # << number of gpus
# parser.add_argument('--model', type=str, default='attention02', 
#     choices=[
#         'enc_dec',   
#     ])
# parser.add_argument('--train_json_path', type=str, default='./cache/kspon_valid.json')
# parser.add_argument('--valid_json_path', type=str,  default='./cache/kspon_valid.json')
# parser.add_argument('--load_model_path', type=str, default='./weights/model01.h5')
# parser.add_argument('--resume_training', type=bool, default=False)
# parser.add_argument('--input_feature', type=str, default='mfcc', choices=['mfcc', 'filter_bank'])
# parser.add_argument('--input_dim',  type=int, default=20)
# parser.add_argument('--output_dim',  type=int, default=54)
# parser.add_argument('--sample_rate', type=int, default=16000)
# parser.add_argument('--optimizer', type=str, default='sgd', choices=['sgd','adam'])
# parser.add_argument('--lr', type=float, default=0.01)    
# parser.add_argument('--lr_reduction_factor', type=float, default=0.1)
# parser.add_argument('--batch_size', type=int, default=64)
# parser.add_argument('--num_epochs', type=int, default=2)
# parser.add_argument('--fine_tuning', type=bool, default=False)
# parser.add_argument('--freeze_top_layer_num', type=int, default=0)    # <<  0: train all
# parser.add_argument('--output_dir', type=str, default='./output')
# parser.add_argument('--training_model_cp_filename', type=str, default='model.{epoch:03d}-{loss:.2f}.h5')
# parser.add_argument('--tb_log', type=str, default='/tb_log')
# parser.add_argument('--num_workers', type=int, default=multiprocessing.cpu_count())


FLAGS = parser.parse_args()
