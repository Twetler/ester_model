from model.models import TModel
from src.utils.functions import *

if __name__ == '__main__':
    all_experiments = experiment_init(experiments=experiment_loader())
    model_A = TModel(experiments_list=all_experiments)

    print('end')
